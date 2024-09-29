import csv
import networkx as nx
import matplotlib.pyplot as plt

def ler_aquivo(nome_arquivo):
    # Lê o arquivo CSV e cria os nós e arestas
    tarefas = []
    dependencias = []
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            codigo_tarefa = linha['Código']
            nome_tarefa = linha['Nome']
            duracao = int(linha['Duração'])
            deps = linha['Dependências'].split(';') if linha['Dependências'] else []
            tarefas.append((codigo_tarefa, nome_tarefa, duracao))
            for dep in deps:
                dependencias.append((dep, codigo_tarefa, duracao))
    return tarefas, dependencias

def construir_grafo(tarefas, dependencias):
    G = nx.DiGraph()
    # Adiciona todas as tarefas como nós, com os atributos 'nome' e 'duracao'
    for codigo_tarefa, nome_tarefa, duracao in tarefas:
        G.add_node(codigo_tarefa, nome=nome_tarefa, duracao=duracao)
    
    # Adiciona dependências como arestas, com 'peso' igual à duração
    for dep, codigo_tarefa, duracao in dependencias:
        G.add_edge(dep, codigo_tarefa, weight=duracao)
    
    # Adiciona os nós 's' (início) e 't' (fim)
    G.add_node('s', nome='Início', duracao=0)
    G.add_node('t', nome='Fim', duracao=0)
    
    # Conecta 's' a todas as tarefas sem dependências
    for codigo_tarefa, _, _ in tarefas:
        if not any(dep[1] == codigo_tarefa for dep in dependencias):
            G.add_edge('s', codigo_tarefa, weight=0)
    
    # Conecta todas as tarefas ao nó 't'
    for codigo_tarefa, _, _ in tarefas:
        G.add_edge(codigo_tarefa, 't', weight=1)
    
    return G

def encontrar_caminho_critico(G):
    # Inicialização
    dist = {v: float('-inf') for v in G.nodes}  # Distâncias como menos infinito
    pred = {v: None for v in G.nodes}  # Predecessores
    dist['s'] = 0  # A distância da origem é 0
    Q = list(G.nodes)  # Conjunto de vértices a processar

    while Q:
        # Encontra o vértice com a maior distância
        u = max(Q, key=lambda vertex: dist[vertex])
        Q.remove(u)  # Remove u de Q (u foi processado)

        for v in G.neighbors(u):
            # Atualiza a condição para encontrar o caminho máximo
            if dist[v] < dist[u] + G[u][v]['weight']:
                dist[v] = dist[u] + G[u][v]['weight']  # Atualiza a distância
                pred[v] = u  # Atualiza o predecessor

    # Reconstruir o caminho crítico a partir do nó 't'
    caminho_critico = []
    duracao_total = dist['t']
    atual = 't'

    while atual is not None:
        caminho_critico.append(atual)
        atual = pred[atual]

    caminho_critico.reverse()  # O caminho é construído ao contrário
    
    # Recupera os nomes das tarefas no grafo para o caminho mais longo
    caminho_critico = [G.nodes[tarefa]['nome'] for tarefa in caminho_critico if tarefa not in ('s', 't')]
    return caminho_critico, duracao_total

def visualizar_grafo(grafo):
    pos = nx.spring_layout(grafo)  # Posição dos nós
    nx.draw(grafo, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
    
    # Adicionando pesos nas arestas
    edge_labels = nx.get_edge_attributes(grafo, 'weight')
    nx.draw_networkx_edge_labels(grafo, pos, edge_labels=edge_labels)

    plt.title("Grafo das Tarefas e Dependências")
    plt.show()


def main():
    while True:
        nome_arquivo = input("Informe o arquivo (0 para sair): ")
        if nome_arquivo == '0':
            break
        try:
            print("\nProcessando ...")
            
            tarefas, dependencias = ler_aquivo(nome_arquivo)
            G = construir_grafo(tarefas, dependencias)
            caminho_critico, duracao_total = encontrar_caminho_critico(G)
            
            # Visualizar o grafo
            visualizar_grafo(G)
            
            print("\nCaminho Crítico:")
            for tarefa in caminho_critico:
                print(f"- {tarefa}")
            
            print(f"\nTempo Mínimo: {duracao_total}\n")

        except FileNotFoundError:
            print("Arquivo não encontrado. Tente novamente.")

if __name__ == "__main__":
    main()