//DIA 9
//Ordenamiento de un Array: Escribir un programa que ordene un array de enteros utilizando ¡Pero hazlo en C++! :)

#include <iostream>
using namespace std;

int main() {
    // Declaración y inicialización del array
    int array[10] = {6, 2, 1, 10, 15, 22, 1, 0, 48, 5};
    int n = 10; // Tamaño del array

    // Implementación del algoritmo de ordenamiento por burbuja
    for(int i = 0; i < n-1; i++) {
        for(int j = 0; j < n-i-1; j++) {
            // Si el elemento actual es mayor que el siguiente, intercambiarlos
            if(array[j] > array[j+1]) {
                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;
            }
        }
    }

    // Imprimir el array ordenado
    for(int i = 0; i < n; i++) {
        cout << array[i] << " ";
    }
    cout << endl;

    return 0;
}
