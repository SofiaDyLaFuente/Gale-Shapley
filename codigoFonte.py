# importa de random, a função que embaralha elementos de uma lista
from random import shuffle

# Função para ler os arquivos e tratar os dados, armazenando-os em um dicionário
def lerArquivo(arquivoProjeto, arquivoAluno):

    projetos = {}
    alunos = {}

    # Leitura do arquivo dos projetos
    with open(arquivoProjeto, 'r') as file:
        linhasProjeto = file.readlines()
        
        # começamos a contagem em dois para ignorar as linhas de comentario
        i = 2
        
        # organiza os projetos em um dicionário até a última linha do txt (linha 56)
        while i != 56:
            # dados estão nesse formato: ['P1', '2', '5']
            dadosProjetos = linhasProjeto[i].strip()[1:-1].split(", ")
            nomeProjeto = dadosProjetos[0]
            vagas = int(dadosProjetos[1])
            requisito_minimo = int(dadosProjetos[2])
            
            # Dicionario dos projetos
            projetos[nomeProjeto] = {'vagas': vagas, 'requisito': requisito_minimo, 'alunos': []}
            # faz o mesmo para proxima linha
            i = i + 1

    # Leitura do arquivo dos alunos
    with open(arquivoAluno, 'r') as file:
        linhasAluno = file.readlines()
    
        # começamos a contagem em dois para ignorar as linhas de comentário
        j = 2  
        
        while j != 202:
            linha = linhasAluno[j].strip()
            
            # dados dos alunos estão no formato ['(A1):(P1, P30, P50', '5)']
            dadosAlunos = linha.split(") (")
            
            # faz o tratamento correto dos dados, tinhando parêteses e realocando os espaços
            x = dadosAlunos[0]
            codigoAluno, preferenciasRaw = x.split(":")
            codigoAluno = codigoAluno.strip("()")

            preferencias = [y.strip() for y in preferenciasRaw.strip("()").split(",")]
            nota = int(dadosAlunos[1].strip(")"))

            # Dicionario dos alunos
            alunos[codigoAluno] = {'preferencias': preferencias, 'nota': nota}

            # itera para a leitura da proxima linha
            j = j + 1

    # retorna os dicionarios
    return alunos, projetos


# Função de emparelhamento estável
def galeShapley(alunos, projetos, flag):
    
    # Lista de alunos sem projeto
    semProjeto = list(alunos.keys())
    iteracoes = 0
    numero = 5
    
    # para a segunda chamada do programa
    if flag == 1:
        numero = 10
        iteracoes = 5
   
    # Rodar o programa 10 iterações
    while iteracoes < numero:
        iteracoes = iteracoes + 1
        print(f"\nIteração {iteracoes}:")

        # Função que embaralha os elementos da lista, nesse caso os alunos sem projeto
        shuffle(semProjeto)

        # Para cada aluno livre, vou tentar inserir em dos projetos
        for aluno in semProjeto[:]:
            
            # separa as preferencias e a nota dos alunos
            preferencias = alunos[aluno]['preferencias']
            notaAluno = alunos[aluno]['nota']

            # Se o aluno tiver preferencia, ele vai tentar ser alocado em algum projeto
            if not preferencias:
                semProjeto.remove(aluno) 
           
            else:
                # O aluno tenta o projeto de maior preferência disponível
                projetoEscolhido = preferencias.pop(0)

                # se a preferencia do aluno for um projeto que existe, vamos busca-lo no dicionário de projetos
                if projetoEscolhido in projetos:
                    projeto = projetos[projetoEscolhido]

                    # verifica se o aluno atinge o requisito minimo do projeto escolhido
                    if notaAluno >= projeto['requisito']:
                        # Caso ele possua o requisito é alocado ao projeto
                        projeto['alunos'].append((aluno, notaAluno))
                        
                        # Ordena os alunos por nota
                        projeto['alunos'] = sorted(projeto['alunos'], key=lambda x: x[1], reverse=True)

                        # Verifica se o projeto excede o número máximo de vagas
                        if len(projeto['alunos']) > projeto['vagas']:
                            # Caso exceda, o aluno com pior nota é removido
                            rejeitado = projeto['alunos'].pop()  # Remove o aluno com a menor nota
                            
                            # E é adicionado de volta para a lista de alunos sem projetos
                            semProjeto.append(rejeitado[0]) 

                        # verificação para evitar duplicação
                        if aluno in semProjeto:
                            semProjeto.remove(aluno) 

        # printa quais alunos estão em quais projetos após a iteração
        for a, b in projetos.items():
            nomesAlunos = [aluno[0] for aluno in b['alunos']]
            print(f"Projeto {a}: {len(b['alunos'])}/{b['vagas']} alunos {nomesAlunos}")

        # Verifica se houve emparelhamento perfeito
        totalAlunosEmparelhados = sum(len(b['alunos']) for b in projetos.values())
        if totalAlunosEmparelhados == sum([b['vagas'] for b in projetos.values()]):
            print(f"\nEmparelhamento perfeito encontrado na tentativa {iteracoes}!")
            break

        # Printa o total de alunos emparelhados em cada iteração
        totalAlunosEmparelhados = sum(len(b['alunos']) for b in projetos.values())
        print(f"Total de alunos emparelhados: {totalAlunosEmparelhados}")
        print("")

    # Printa emparelhamento final
    if flag == 1:
        print("------------------------", end='')
        print("\n  Emparelhamento Final:")
        print("------------------------")
        totalAlunosEmparelhados = sum(len(b['alunos']) for b in projetos.values())
        
        for a, b in projetos.items():
            print(f"Projeto {a}: {b['alunos']}")

        print(f"Total de alunos emparelhados: {totalAlunosEmparelhados}")

def main():
    arquivoProjeto = "entradaTAGprojetos.txt"
    arquivoAluno = "entradaTAGalunos.txt"

    alunos, projetos = lerArquivo(arquivoProjeto, arquivoAluno)

    # O programa será dividido em dois, onde na primeira onde rodaremos o programa 5 vezes e na segunda mais 5
    flag = 0
    galeShapley(alunos, projetos, flag)
    flag = 1
    galeShapley(alunos, projetos, flag)

if __name__ == "__main__":
    main()
