# Projekt interpolacji wielomianowej

## Przegląd

Ten projekt w języku Python ma na celu wykonanie interpolacji wielomianowej przy użyciu metody Grama. Interpolacja wielomianowa to metoda znajdowania funkcji wielomianowej, która przechodzi przez zadany zbiór punktów danych. Metoda Grama to technika używana do przybliżenia wielomianu, który najlepiej pasuje do zadanych punktów danych.

## Składniki projektu

### 1. Wczytywanie danych

- Dane są wczytywane z pliku o nazwie "input_points.txt".
- Każda linia w pliku zawiera parę współrzędnych x i y reprezentujących punkty danych.

### 2. Funkcje obliczeniowe

- **Współczynniki Newtona:** Oblicza współczynniki dla interpolacji Newtona.
- **Funkcja wielomianowa:** Oblicza wartość funkcji wielomianowej dla określonej wartości x i jej stopnia.
- **Funkcja F:** Oblicza funkcję F używaną w metodzie Grama.
- **Obliczenie metody Grama:** Wykonuje metodę Grama w celu przybliżenia wielomianu, który najlepiej pasuje do punktów danych.

### 3. Wyświetlanie wyników

- Wyświetla liczbę węzłów (punktów danych).
- Wyświetla współczynniki ck, sk dla metody Grama.
- Wyświetla interpolowane wartości Ym(x) dla każdego punktu danych.

## Dane wejściowe

Dane wejściowe składają się z zestawu punktów danych wczytanych z pliku "input_points.txt".

## Wyniki

- Liczba węzłów: [Liczba węzłów]
- Współczynniki ck, sk:
  - [Współczynniki ck, sk]
- Interpolowane wartości Ym(x) dla każdego punktu danych:
  - [Interpolowane wartości Ym(x)]

## Autor

Ten projekt został stworzony przez [Maksymilian Kubiczek] ([@MaksKubiczek](https://github.com/MaksKubiczek)).

## Licencja

Ten projekt jest licencjonowany na licencji [MIT License]. Więcej informacji znajduje się w pliku LICENSE.
