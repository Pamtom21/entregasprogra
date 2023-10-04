#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <pthread.h>

#define SHM_SIZE 10
#define MAX_RANDOM 10

int *shared_memory;
pthread_mutex_t mutex;
FILE *resultados;

void padre() {
    for (int i = 0; i < 10; i++) {
        int random_number = (rand() % MAX_RANDOM) + 1;

        // Escribir el número en memoria compartida
        pthread_mutex_lock(&mutex);
        *shared_memory = random_number;
        printf("padre: escribiendo %d\n", random_number);
        pthread_mutex_unlock(&mutex);

        sleep(2);
    }

    // Esperar a que el hijo termine
    wait(NULL);

    // Leer y mostrar el archivo "resultados.txt"
    char buffer[255];
    rewind(resultados);
    while (fgets(buffer, sizeof(buffer), resultados) != NULL) {
        printf("%s", buffer);
    }

    fclose(resultados);
}

void hijo() {
    int valores[10];
    int sum = 0;

    for (int i = 0; i < 10; i++) {
        // Leer el número desde memoria compartida
        pthread_mutex_lock(&mutex);
        int random_number = *shared_memory;
        printf("hijo: leyendo %d\n", random_number);
        pthread_mutex_unlock(&mutex);

        valores[i] = random_number;
        sum += random_number;
        sleep(1);
    }

    // Escribir los valores y el promedio en el archivo "resultados.txt"
    resultados = fopen("resultados.txt", "a");
    for (int i = 0; i < 10; i++) {
        fprintf(resultados, "%d", valores[i]);
        if (i < 9) fprintf(resultados, ",");
    }
    fprintf(resultados, " - Promedio: %.2f\n", (float)sum / 10);
    fclose(resultados);
}

int main() {
    // Crear memoria compartida
    int shmid = shmget(IPC_PRIVATE, sizeof(int), 0666 | IPC_CREAT);
    if (shmid == -1) {
        perror("Error en shmget");
        exit(1);
    }

    // Adjuntar memoria compartida al proceso
    shared_memory = (int *)shmat(shmid, NULL, 0);
    if ((int)shared_memory == -1) {
        perror("Error en shmat");
        exit(1);
    }

    // Inicializar mutex
    pthread_mutex_init(&mutex, NULL);

    // Crear el archivo "resultados.txt"
    resultados = fopen("resultados.txt", "w");
    if (resultados == NULL) {
        perror("Error al crear el archivo resultados.txt");
        exit(1);
    }

    // Crear proceso hijo
    pid_t pid = fork();
    if (pid == -1) {
        perror("Error en fork");
        exit(1);
    }

    if (pid == 0) {
        hijo();
    } else {
        padre();
    }

    // Liberar recursos
    pthread_mutex_destroy(&mutex);
    shmdt(shared_memory);
    shmctl(shmid, IPC_RMID, NULL);

    return 0;
}
