//DIA 10
//Palíndromo: Escribir un programa que determine si una
//cadena de caracteres ingresada por el usuario es un palíndromo ¡Pero hazlo en C++! :)

#include <iostream>
#include <string>


using namespace std;

bool Palindromo(string cadena) {
    int inicio = 0;
    int fin = cadena.length() - 1;

    // Comparar los caracteres desde el inicio y el final hacia el centro
    while(inicio < fin) {
        if(cadena[inicio] != cadena[fin]) {
            return false; // No es un palíndromo
        }
        inicio++;
        fin--;
    }
    return true; // Es un palíndromo
}

int main() {
    string cadena;

    cout << "Ingrese una cadena de caracteres: ";
    getline(cin, cadena);

    if(Palindromo(cadena)) {
        cout << "La cadena es un palíndromo." << endl;
    } else {
        cout << "La cadena no es un palíndromo." << endl;
    }

    return 0;
}
