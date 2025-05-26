#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>

#define EXECUCOES 30

void merge(int arr[], int l, int m, int r) {
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;

    int* L = malloc(n1 * sizeof(int));
    int* R = malloc(n2 * sizeof(int));

    for (i = 0; i < n1; i++) L[i] = arr[l + i];
    for (j = 0; j < n2; j++) R[j] = arr[m + 1 + j];

    i = 0; j = 0; k = l;
    while (i < n1 && j < n2)
        arr[k++] = (L[i] <= R[j]) ? L[i++] : R[j++];

    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];

    free(L);
    free(R);
}

void mergeSort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}

void preencherAleatorio(int arr[], int n) {
    for (int i = 0; i < n; i++)
        arr[i] = rand() % 100000;
}

void preencherMelhorCaso(int arr[], int n) {
    for (int i = 0; i < n; i++)
        arr[i] = i;
}

void preencherPiorCaso(int arr[], int n) {
    for (int i = 0; i < n; i++)
        arr[i] = n - i;
}

double calcularMedia(double tempos[]) {
    double soma = 0;
    for (int i = 0; i < EXECUCOES; i++)
        soma += tempos[i];
    return soma / EXECUCOES;
}

double calcularDesvioPadrao(double tempos[], double media) {
    double soma = 0;
    for (int i = 0; i < EXECUCOES; i++)
        soma += pow(tempos[i] - media, 2);
    return sqrt(soma / EXECUCOES);
}

void testarCasoCSV(FILE* arquivo, const char* nomeCaso, int tamanho, void (*preencher)(int*, int)) {
    double tempos[EXECUCOES];
    int* arr = malloc(tamanho * sizeof(int));
    int* copia = malloc(tamanho * sizeof(int));

    for (int i = 0; i < EXECUCOES; i++) {
        preencher(arr, tamanho);
        memcpy(copia, arr, tamanho * sizeof(int));

        clock_t inicio = clock();
        mergeSort(copia, 0, tamanho - 1);
        clock_t fim = clock();

        tempos[i] = (double)(fim - inicio) / CLOCKS_PER_SEC;
    }

    double media = calcularMedia(tempos);
    double desvio = calcularDesvioPadrao(tempos, media);

    // Grava no CSV
    fprintf(arquivo, "%d,%s,%.6f,%.6f\n", tamanho, nomeCaso, media, desvio);

    free(arr);
    free(copia);
}

int main() {
    srand(time(NULL));

    int tamanhos[] = {100, 1000, 10000, 1000000};
    int total = sizeof(tamanhos) / sizeof(tamanhos[0]);

    FILE* arquivo = fopen("dadosParaTabela.csv", "w");
    if (!arquivo) {
        perror("Erro ao criar o arquivo CSV");
        return 1;
    }

    // Cabeçalho do CSV
    fprintf(arquivo, "Tamanho,Caso,Tempo Medio,Desvio Padrao\n");

    for (int i = 0; i < total; i++) {
        int tamanho = tamanhos[i];

        testarCasoCSV(arquivo, "Melhor", tamanho, preencherMelhorCaso);
        testarCasoCSV(arquivo, "Medio", tamanho, preencherAleatorio);
        testarCasoCSV(arquivo, "Pior", tamanho, preencherPiorCaso);
    }

    fclose(arquivo);
    printf("Arquivo 'dadosParaTabela.csv' gerado com sucesso.\n");
    return 0;
}
