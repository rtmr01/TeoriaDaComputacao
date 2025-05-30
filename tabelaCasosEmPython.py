import time
import random
import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

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

# Medição de tempos e desvios
def medir_tempos_para_casos(tamanho, n_execucoes=5):
    casos = {
        "Melhor": list(range(tamanho)),
        "Pior": list(range(tamanho, 0, -1)),
        "Medio": [random.randint(0, 1000000) for _ in range(tamanho)]
    }

    resultados = []
    for nome_caso, base_array in casos.items():
        tempos = []
        for _ in range(n_execucoes):
            if nome_caso == "Medio":
                arr = [random.randint(0, 1000000) for _ in range(tamanho)]
            else:
                arr = base_array.copy()
            inicio = time.time()
            merge_sort(arr)
            fim = time.time()
            tempos.append(fim - inicio)

        tempo_medio = sum(tempos) / len(tempos)
        desvio_padrao = statistics.stdev(tempos)
        resultados.append({
            "Tamanho": tamanho,
            "Caso": nome_caso,
            "Tempo (s)": tempo_medio,
            "Desvio Padrão": desvio_padrao
        })

    return resultados

# Tamanhos a testar
tamanhos = [100, 1000, 10000]  # Comente 1000000 se estiver testando
dados = []

# Executa testes
for tamanho in tamanhos:
    resultados = medir_tempos_para_casos(tamanho)
    dados.extend(resultados)

# Cria DataFrame
df_resultado = pd.DataFrame(dados)

# Tabela de tempos médios
print("\n===== TABELA DE TEMPOS POR CASO (PYTHON) =====")
print(df_resultado.pivot(index="Tamanho", columns="Caso", values="Tempo (s)").round(6))

# Tabela de desvios padrão
print("\n===== TABELA DE DESVIOS PADRÃO POR CASO (PYTHON) =====")
print(df_resultado.pivot(index="Tamanho", columns="Caso", values="Desvio Padrão").round(6))

# Gráfico
pivot_df = df_resultado.pivot(index="Tamanho", columns="Caso", values="Tempo (s)")
pivot_df = pivot_df[["Melhor", "Medio", "Pior"]]

ax = pivot_df.plot(kind='bar', figsize=(10, 6))
ax.set_title("Tempo de Execução do Merge Sort em Python por Caso")
ax.set_xlabel("Tamanho do Array")
ax.set_ylabel("Tempo (s)")
ax.grid(True, axis='y')
plt.xticks(rotation=0)
plt.tight_layout()
plt.legend(title="Caso")
plt.show()
