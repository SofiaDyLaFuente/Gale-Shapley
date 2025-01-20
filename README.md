# Gale-Shapley
### Repositório para a implementação do projeto 2 da disciplina de Teoria e Aplicação de Grafos - UnB

-------

Algoritmo implementado baseado no algoritmo de Gale-Shapley, usado para resolver problemas de emparelhamento estável. 

Basicamente o algoritmo de Gale-Shapey é um algoritmo que é usado para encontrar correspondência estável entre dois conjuntos de elementos, onde nenhum dos dois elementos prefere um ao outro em vez de sua correspondência atual. Foi descrito pela primeira vez por David Gale e Lloyd Shaprow em 1962.

Como o algoritmo funciona? 

https://medium.com/aiskunks/understanding-gale-shapley-stable-matching-algorithm-and-its-time-complexity-4b814ee2642

Funciona fazendo com que um conjunto de elementos, chamados proponentes, faça propostas para o outro conjunto de elementos, chamados receptores. Os proponentes têm uma lista de preferências dos receptores, e os receptores têm uma lista de preferências dos proponentes. O algoritmo começa fazendo com que cada proponente faça uma proposta para seu receptor de primeira escolha. Se um receptor receber várias propostas, ele escolhe o proponente que mais prefere e rejeita os outros. Os proponentes rejeitados então passam para sua próxima escolha e fazem uma proposta. Esse processo continua até que todos os elementos sejam correspondidos.

O pseudo código do algoritmo é:

```python
Initialize each person to be free.
while (some man is free and hasn't proposed to every woman){
    chose such a man m
    w = 1º woman on m's list to who m has not yet proposed
    if (w is free)
        assign m and w to be engaged
    else if (w prefers m to her fiancé m')
        assign m and w to be engaged, and m' to be free
    else
        w rejects m
}
```
Para o problema proposto temos 54 projetos que exigem uma nota mínima dos alunos. E existem 200 alunos com preferencia especificas pelos projetos e com determinada nota.
 
Para a implementação desse problema, os dados estavam em um arquivo chamado `entradaProj2.24TAG.txt` Para facilitar o tratamento dos dados, eu dividi o arquivo em dois: um para os alunos `(entradaTAGalunos.txt)` e outro para o projetos `(entradaTAGprojetos.txt)` sem alterar nenhum dado.

*Importante fazer um esclarecimento que na linha do Aluno 177, a separação das preferências e da nota não possuia espaço, como nas outras linhas `(A177):(P37, P21, P18)(5)`. Tomei a liberdade de acrescentar esse espaço no txt para facilitar no tratamento dos dados.*

Para a implementação eu criei três funções:
- `main()`: para iniciar o programa e fazer a chamada das outras funções;
- `lerArquivo()`: para ler os arquivos e tratar os dados corretamente, armazenando-os em dicionarios;
- `galeShapley()`: para implementar a solução do problema;

Na função `galeShapley()` eu tento emparelhar os alunos e os projetos de acordo com a nota e a preferencia pessoal desses alunos. O algoritmo realiza 10 tentativas de emparelhamento, divididos em duas chamadas do algoritmo, para garantir que o emparelhamento encontrado é estável. Em cada tentativa, a ordem dos alunos é embaralhada, para que o algoritmo possa gerar diferentes combinações.

Eu tentei anteriormente fazer sem embaralhamento, mas o algoritmo retornava apenas 54 alunos alocados. E tentei fazer o embaralhamento apenas uma vez, o que piorava ainda mais o algoritmo, retornando 48 alunos alocados.

Para o algoritmo funcionar, ele percorre a lista com todos os alunos sem projeto e verifica suas preferências e nota. O aluno é então alocado no projeto de sua maior preferência. Em seguida é feito uma verificação para ver se o aluno atinge o requisito mínimo de nota do projeto. Caso não tenha nota suficiente, esse projeto é ignorado e a verificação é feita para o próximo projeto da lista. Caso o aluno preencha os requisitos, ele é alocado na lista projeto, que é ordenada para que os alunos com maiores notas fiquem na frente. Se tiver mais alunos que vagas no projeto, o aluno com a pior nota é removido e volta para a lista de alunos sem projetos, para tentar ser realocado novamente. Ao final das 10 iterações, garantimos que o emparelhamento é estável.
