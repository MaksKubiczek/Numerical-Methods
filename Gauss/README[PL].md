# Opis Projektu

Projekt ten skupia się na rozwiązywaniu układów równań liniowych przy użyciu metody eliminacji Gaussa. Metoda eliminacji Gaussa jest podstawową techniką analizy numerycznej do rozwiązywania układów równań liniowych poprzez przekształcenie macierzy rozszerzonej na postać schodkową.

## Funkcje

### `load_data(filename)`
- **Opis:** Wczytuje dane z pliku zawierającego układ równań liniowych.
- **Parametry:**
  - `filename`: Nazwa pliku zawierającego dane.
- **Zwraca:** Dwie listy `A` i `b`, reprezentujące macierz współczynników i wektor stałych układu równań, odpowiednio.

### `Gauss(tab)`
- **Opis:** Implementuje metodę eliminacji Gaussa do rozwiązania układu równań liniowych.
- **Parametry:**
  - `tab`: Macierz rozszerzona reprezentująca układ równań liniowych.
- **Zwraca:** Wyświetla macierz rozszerzoną oraz wektor rozwiązania układu równań.

## Kroki

1. **Wczytaj Dane:**
   - Wczytaj układ równań liniowych z pliku za pomocą funkcji `load_data()`.

2. **Wykonaj Eliminację Gaussa:**
   - Użyj funkcji `Gauss()` do wykonania eliminacji Gaussa na macierzy rozszerzonej otrzymanej z wczytanych danych.

3. **Wyświetl Wyniki:**
   - Wyświetl macierz rozszerzoną przed i po eliminacji Gaussa, oraz wektor rozwiązania układu równań.

## Użycie

1. Zdefiniuj układ równań liniowych w pliku tekstowym, gdzie pierwsza linia reprezentuje liczbę równań (n), a kolejne linie zawierają współczynniki równań oraz stałe po prawej stronie.
2. Uruchom skrypt Pythona, aby rozwiązać układ równań przy użyciu metody eliminacji Gaussa.
3. Przejrzyj wyświetlone wyniki, w tym macierze rozszerzone i wektory rozwiązania.

## Technologie

- Python
- Metody Numeryczne
- Eliminacja Gaussa

## Autor

Ten projekt został stworzony przez [Maksymilian Kubiczek] ([@MaksKubiczek](https://github.com/MaksKubiczek)).

## Licencja

Ten projekt jest licencjonowany na [Licencji MIT]. Więcej informacji można znaleźć w pliku LICENSE.
