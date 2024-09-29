# Calcula o caminho mais longo usando ordenação topológica
    caminho_mais_longo = nx.dag_longest_path(G, weight='weight')
    duracao_total = nx.dag_longest_path_length(G, weight='weight')
    
    # Recupera os nomes das tarefas no grafo para o caminho mais longo
    caminho_critico = [G.nodes[tarefa]['nome'] for tarefa in caminho_mais_longo if tarefa not in ('s', 't')]
    return caminho_critico, duracao_total  