import random
import time
import math
import matplotlib.pyplot as plt
import pandas as pd
import os

# Implementação do Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        L = arr[:meio]
        R = arr[meio:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Função para medir tempos de execução e calcular estatísticas
def executar_testes(tamanhos, execucoes=30):
    resultados = []

    for tamanho in tamanhos:
        tempos = []

        for _ in range(execucoes):
            arr = [random.randint(0, 100000) for _ in range(tamanho)]
            inicio = time.perf_counter()
            merge_sort(arr)
            fim = time.perf_counter()
            tempos.append(fim - inicio)

        media = sum(tempos) / execucoes
        desvio = math.sqrt(sum((x - media) ** 2 for x in tempos) / execucoes)

        resultados.append({
            "tamanho": tamanho,
            "media": media,
            "desvio": desvio
        })

    return resultados

# === PARTE 1: Merge Sort vs Complexidade Teórica ===
tamanhos_teste = [100, 1000, 10000, 20000, 30000]
resultados = executar_testes(tamanhos_teste)

tamanhos = [r["tamanho"] for r in resultados]
tempos = [r["media"] for r in resultados]
desvios = [r["desvio"] for r in resultados]
nlogn = [t * math.log2(t) for t in tamanhos]
nlogn_normalizado = [x / max(nlogn) * max(tempos) for x in nlogn]

# Gráfico 1 – Tempo vs n log n
plt.figure(figsize=(10, 6))
plt.plot(tamanhos, tempos, marker='o', label="Tempo médio (Merge Sort)")
plt.plot(tamanhos, nlogn_normalizado, linestyle='--', label="Curva teórica n log n")
plt.fill_between(tamanhos, [m - d for m, d in zip(tempos, desvios)],
                 [m + d for m, d in zip(tempos, desvios)], alpha=0.2, label="Desvio padrão")
plt.title("Desempenho do Merge Sort vs Complexidade Teórica")
plt.xlabel("Tamanho do array")
plt.ylabel("Tempo (segundos)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("/Users/rodrigotorres/Downloads/grafico_merge_sort_python.png")#ALTEREM ISSO PQ ISSO EH DO MEU PC 
plt.show()

# === PARTE 2: Comparação Python vs C ===
# Certifique-se de que tempos_c.csv está no mesmo diretório
if os.path.exists("tempos_c.csv"):
    dados_c = pd.read_csv("tempos_c.csv", names=["tamanho", "tempo_c"])

    dados_python = pd.DataFrame({
        "tamanho": tamanhos,
        "tempo_python": tempos
    })

    comparacao = pd.merge(dados_python, dados_c, on="tamanho")

    plt.figure(figsize=(10, 6))
    plt.plot(comparacao["tamanho"], comparacao["tempo_python"], marker='o', label="Python")
    plt.plot(comparacao["tamanho"], comparacao["tempo_c"], marker='s', label="C")
    plt.title("Comparação de Desempenho: Merge Sort em Python vs C")
    plt.xlabel("Tamanho do array")
    plt.ylabel("Tempo médio (s)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("/Users/rodrigotorres/Downloads/grafico_comparacao_python_c.png") #ALTEREM ISSO PQ ISSO EH DO MEU PC 
    plt.show()
else:
    print("Arquivo tempos_c.csv não encontrado. Pulei o gráfico comparativo com C.")
