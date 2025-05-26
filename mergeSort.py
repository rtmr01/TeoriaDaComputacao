import pandas as pd
import matplotlib.pyplot as plt
import math
import os

def grafico_merge_sort_teorico():
    tamanhos = [100, 1000, 10000, 20000, 30000]
    tempos = [0.00092, 0.00794, 0.09533, 0.21541, 0.34910]
    desvios = [0.00005, 0.00043, 0.00521, 0.01132, 0.01746]

    nlogn = [n * math.log2(n) for n in tamanhos]
    nlogn_normalizado = [x / max(nlogn) * max(tempos) for x in nlogn]

    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos, tempos, marker='o', label="Tempo médio (Python)")
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

def grafico_comparacao_python_c():
    if not os.path.exists("tempos_c.csv"):
        print("Arquivo tempos_c.csv não encontrado.")
        return

    dados_c = pd.read_csv("tempos_c.csv", names=["tamanho", "tempo_c"])

    dados_python = pd.DataFrame({
        "tamanho": [100, 1000, 10000],
        "tempo_python": [0.00092, 0.00794, 0.09533]
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
    plt.show()

def grafico_curva_teorica_vs_c():
    if not os.path.exists("tempos_c.csv"):
        print("Arquivo tempos_c.csv não encontrado.")
        return

    dados_c = pd.read_csv("tempos_c.csv", names=["tamanho", "tempo_c"])
    tamanhos = dados_c["tamanho"]
    tempos_c = dados_c["tempo_c"]

    nlogn = [n * math.log2(n) for n in tamanhos]
    nlogn_normalizado = [x / max(nlogn) * max(tempos_c) for x in nlogn]

    plt.figure(figsize=(10, 6))
    plt.plot(tamanhos, tempos_c, marker='o', label="Tempo médio (C)")
    plt.plot(tamanhos, nlogn_normalizado, linestyle='--', label="Curva teórica n log n")
    plt.title("Desempenho do Merge Sort em C vs Complexidade Teórica")
    plt.xlabel("Tamanho do array")
    plt.ylabel("Tempo (segundos)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def gerar_tabela_c_csv():
    if not os.path.exists("dadosParaTabela.csv"):
        print("Arquivo dadosParaTabela.csv não encontrado.")
        return

    df = pd.read_csv("dadosParaTabela.csv")

    print("\n===== TABELA: TEMPO MÉDIO =====")
    print(df.pivot(index="Tamanho", columns="Caso", values="Tempo Medio").round(6))

    print("\n===== TABELA: DESVIO PADRÃO =====")
    print(df.pivot(index="Tamanho", columns="Caso", values="Desvio Padrao").round(6))

    # Gráfico de barras agrupadas
    pivot_df = df.pivot(index="Tamanho", columns="Caso", values="Tempo Medio")
    pivot_df = pivot_df[["Melhor", "Medio", "Pior"]]  # Ordena as colunas

    ax = pivot_df.plot(kind='bar', figsize=(10, 6))
    ax.set_title("Tempo Médio do Merge Sort por Tamanho e Caso")
    ax.set_xlabel("Tamanho do Array")
    ax.set_ylabel("Tempo Médio (s)")
    ax.grid(True, axis='y')
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.legend(title="Caso")
    plt.show()


def menu():
    while True:
        print("\n=== MENU DE GRÁFICOS ===")
        print("1 - Curva Teórica vs Merge Sort (Python)")
        print("2 - Comparação Python vs C")
        print("3 - Curva Teórica vs Merge Sort (C)")
        print("4 - Gerar Tabela a partir do CSV de C")
        print("0 - Sair")
        opcao = input("Escolha a opção: ")

        if opcao == "1":
            grafico_merge_sort_teorico()
        elif opcao == "2":
            grafico_comparacao_python_c()
        elif opcao == "3":
            grafico_curva_teorica_vs_c()
        elif opcao == "4":
            gerar_tabela_c_csv()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
