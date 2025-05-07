import random
import time
import math
import matplotlib.pyplot as plt
import numpy as np

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

# Tamanhos dos arrays para teste
tamanhos_teste = [100, 1000, 10000, 20000, 30000]

# Executar os testes
resultados = executar_testes(tamanhos_teste)

# Preparar dados para gráfico
tamanhos = [r["tamanho"] for r in resultados]
tempos = [r["media"] for r in resultados]
desvios = [r["desvio"] for r in resultados]
nlogn = [t * math.log2(t) for t in tamanhos]
nlogn_normalizado = [x / max(nlogn) * max(tempos) for x in nlogn]

# Plotar o gráfico
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
plt.show()
