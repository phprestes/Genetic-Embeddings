import numpy as np

texto = "o gato comeu o rato"
palavras = texto.split()
vocab = sorted(list(set(palavras)))
word_to_id = {w: i for i, w in enumerate(vocab)}
id_to_word = {i: w for i, w in enumerate(vocab)}

print(f"Vocabulário: {vocab}")
print(f"Meta: Aprender a sequência '{texto}'\n")

# Tamanhos
N_POPULACAO = 50
N_VOCAB = len(vocab)

# Cada indivíduo é uma matriz (N_VOCAB x N_VOCAB) de pesos aleatórios
populacao = np.random.randn(N_POPULACAO, N_VOCAB, N_VOCAB)

def calcular_fitness(populacao, palavras, word_to_id):
    scores = np.zeros(len(populacao))
    
    # Percorre a frase par a par (Ex: "o" -> "gato")
    for i in range(len(palavras) - 1):
        idx_atual = word_to_id[palavras[i]]
        idx_alvo = word_to_id[palavras[i+1]]
        
        preds = populacao[:, idx_atual, :] 
        scores += preds[:, idx_alvo]
        
    return scores

# 3. Loop Evolutivo
n_geracoes = 100

for geracao in range(n_geracoes):
    # a) Avaliação
    fitness = calcular_fitness(populacao, palavras, word_to_id)
    
    # b) Seleção: Quem é o melhor indivíduo?
    melhor_idx = np.argmax(fitness)
    melhor_score = fitness[melhor_idx]
    melhor_cerebro = populacao[melhor_idx].copy() # Clonamos o vencedor
    
    if geracao % 10 == 0:
        print(f"Geração {geracao}: Melhor Score = {melhor_score:.2f}")

    # Criamos uma nova população inteira baseada no vencedor + ruído
    ruido = np.random.randn(N_POPULACAO, N_VOCAB, N_VOCAB) * 0.5
    populacao = melhor_cerebro + ruido
    populacao[0] = melhor_cerebro

print("\n--- Treinamento Concluído ---")

# 4. Testando o melhor modelo final
print("\nGerando frase com o melhor modelo evoluído:")
palavra_atual = "o" # Começa com 'o'
frase_gerada = [palavra_atual]

for _ in range(4): # Gera 4 palavras
    idx = word_to_id[palavra_atual]
    
    # Pega os pesos do melhor indivíduo (índice 0, pois usamos elitismo)
    pesos = populacao[0] 
    
    # Vê qual palavra tem o maior peso de conexão saindo da palavra atual
    prox_idx = np.argmax(pesos[idx, :])
    palavra_atual = id_to_word[prox_idx]
    frase_gerada.append(palavra_atual)

print("Resultado:", " ".join(frase_gerada))