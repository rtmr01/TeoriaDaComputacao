#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

void merge(int arr[], int esquerda, int meio, int direita) {
    int i, j, k;
    int n1 = meio - esquerda + 1;
    int n2 = direita - meio;

    int L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = arr[esquerda + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[meio + 1 + j];

    i = 0;
    j = 0;
    k = esquerda;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int esquerda, int direita) {
    if (esquerda < direita) {
        int meio = esquerda + (direita - esquerda) / 2;

        mergeSort(arr, esquerda, meio);
        mergeSort(arr, meio + 1, direita);

        merge(arr, esquerda, meio, direita);
    }
}

void gerarArrayAleatorio(int arr[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        arr[i] = rand() % 100000; // números entre 0 e 99.999
    }
}

double calcularMedia(double tempos[], int n) {
    double soma = 0.0;
    for (int i = 0; i < n; i++) {
        soma += tempos[i];
    }
    return soma / n;
}

double calcularDesvioPadrao(double tempos[], int n, double media) {
    double soma = 0.0;
    for (int i = 0; i < n; i++) {
        soma += (tempos[i] - media) * (tempos[i] - media);
    }
    return sqrt(soma / n);
}

int main() {
    int tamanhos[] = {100, 1000, 10000}; // tamanhos pequenos, médios e grandes
    int num_execucoes = 30;
    srand(time(NULL));

    for (int t = 0; t < 3; t++) {
        int n = tamanhos[t];
        double tempos[num_execucoes];

        printf("\n--- Tamanho do array: %d ---\n", n);

        for (int exec = 0; exec < num_execucoes; exec++) {
            int arr[n];
            gerarArrayAleatorio(arr, n);

            clock_t inicio = clock();
            mergeSort(arr, 0, n - 1);
            clock_t fim = clock();

            tempos[exec] = ((double)(fim - inicio)) / CLOCKS_PER_SEC;
        }

        double media = calcularMedia(tempos, num_execucoes);
        double desvio = calcularDesvioPadrao(tempos, num_execucoes, media);

        printf("Execuções: %d\n", num_execucoes);
        printf("Tempo médio: %.6f segundos\n", media);
        printf("Desvio padrão: %.6f segundos\n", desvio);
    }

    return 0;
}
