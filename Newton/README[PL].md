# Projekt: Interpolacja wielomianowa metodą Newtona

## Opis

Projekt ten koncentruje się na obliczaniu wartości wielomianu interpolacyjnego za pomocą metody Newtona. Metoda Newtona to technika interpolacji pozwalająca na znalezienie wielomianu, który najlepiej pasuje do zestawu punktów danych. Projekt zawiera funkcję obliczającą wartość wielomianu Newtona w danym punkcie oraz funkcję wczytującą dane z pliku tekstowego zawierającego węzły interpolacji i wartości funkcji w tych węzłach.

## Funkcje

1. **newton_interpolation(x, nodes, values)**: Oblicza wartość wielomianu Newtona w danym punkcie na podstawie zestawu węzłów interpolacji i wartości funkcji w tych węzłach.
2. **read_data(filename)**: Wczytuje dane z pliku tekstowego zawierającego węzły interpolacji i wartości funkcji w tych węzłach.

## Użycie

1. Uruchomienie pliku `main.py`.
2. Pliki wejściowy `data1.txt`, `data2.txt` zawiera dane w formacie: liczba węzłów interpolacji, węzły interpolacji oraz wartości funkcji w tych węzłach.
3. Projekt wczytuje dane z pliku, oblicza wartość wielomianu Newtona w wybranym punkcie, a następnie wyświetla wyniki.
4. Użytkownik może również obliczyć wartości wielomianu dla innych punktów, które są zdefiniowane bezpośrednio w skrypcie.

## Technologie

- Python
- Interpolacja wielomianowa
- Obsługa plików

## Autor

Ten projekt został stworzony przez [Maksymilian Kubiczek] ([@MaksKubiczek](https://github.com/MaksKubiczek)).

## Licencja

Ten projekt jest objęty licencją [MIT]. Więcej informacji znajduje się w pliku LICENSE.
