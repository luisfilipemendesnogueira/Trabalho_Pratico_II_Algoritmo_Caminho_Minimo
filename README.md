# Trabalho Prático II

Trabalho proposto da disciplina Algoritmos e Estrutura de Dados III em linguagem python.

## 1. Objetivos.

- Reforçar o aprendizado sobre os algoritmos de caminhos mínimos.
- Aplicar os conhecimentos em algoritmos para resolver problemas reais.
- Aprimorar a habilidade de programação de algoritmos em grafos.
  
## 2. Descrição

A gestão adequada de projetos é essencial para que os mesmos sejam concluídos com o escopo, prazo e recursos estabelecidos. Para assegurar o cumprimento do prazo de um projeto, uma técnica muito utilizada é o método do caminho crítico. Nesse método, identificamos a sequência de etapas e dependências entre elas mais crítica para a finalização do trabalho. Aquela na qual qualquer atraso atrasa o tempo mínimo de conclusão do projeto.

Vejamos um exemplo ligado a conclusão de um curso de graduação. Na Tabela 1, temos
8 disciplinas e a informação de dependências entre elas:

![toy](https://github.com/user-attachments/assets/677e7c56-19ae-4fb4-b856-aa67fb8a7d4f)

Nesse exemplo não é difícil identificar que a caminho crítico para conclusão do curso é:
Lógica de Programação → Engenharia de Software → Sistemas Web e Mobile. Como cada tarefa demanda um tempo de um período, o tempo mínimo de conclusão do projeto é três períodos.
A tarefa de encontrar o caminho crítico de um projeto, dados suas etapas, duração prevista e dependências pode ser automatizada através de algoritmos em grafos. O exemplo anterior poderia ser representado como um grafo da seguinte forma:

![toy_graph]([https://github.com/user-attachments/assets/ab91550f-44dc-43ea-b51d-618bdcb37511](https://github.com/user-attachments/assets/970bfffe-cadc-4def-afbe-e61f30017160))

Cada nó representa o início de uma etapa e as arestas informam as relações de dependências. O peso de cada aresta é dado pelo tempo que a tarefa origem leva para ser concluída. Temos ainda dois nós adicionais, s indicando o início do projeto e t indicando a conclusão de tarefas. O nó s se liga diretamente a todas as tarefas sem dependências e todas as tarefas se ligam ao nó t. A caminho crítico é dado pelo caminho máximo de s a t nesse grafo, ressaltado pelos nós em verde.

O professor preparou dois arquivos de teste, ambos no formato .csv. O arquivo TOY trás o exemplo da Tabela 1; e o arquivo SJM representa o curso de Sistemas de Informação da Ufop. Esse arquivo foi criado com base na grade curricular oficial dos curso.

## 3. Cada projeto deve:

- Ler o arquivo de dados e carregar o grafo correspondente ao arquivo;
- Ajustar algum algoritmo de caminho mínimo para resolver o problema do caminho máximo;
- Resolver o problema, obtendo o caminho máximo (crítico) do projeto;
- Exibir para o usuário quais tarefas fazem parte do caminho crítico e qual o tempo mínimo de conclusão do projeto;

## 4. Interação com o usuário:

A interação com o usuário deve ocorrer na função main do seu programa. O mesmo deve solicitar ao usuário o arquivo de entrada e após a execução, informar o caminho máximo de s a t, bem como o tempo mínimo de conclusão do projeto (distância do caminho). Caso o caractere 0 seja informado, o programa deve encerrar. Segue um exemplo de interação com o programa:

Informe o arquivo (0 para sair ) : <critical_path/TOY.csv>

Processando ...

Caminho Crítico :
- Lógica de Programação
- Engenharia de Software
- Sistemas Web e Mobile

Tempo Mínimo : 3

Informe o arquivo (0 para sair ) : <0>
