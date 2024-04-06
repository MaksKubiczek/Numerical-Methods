# Algorytm dekompozycji LU Doolittle'a

## Przegląd

Ten projekt implementuje algorytm dekompozycji LU Doolittle'a w języku Python. Dekompozycja LU rozkłada macierz na iloczyn macierzy trójkątnej dolnej (L) i macierzy trójkątnej górnej (U). Jest ona często stosowana do rozwiązywania układów równań liniowych oraz obliczania wyznacznika i odwrotności macierzy.

## Opis

Funkcja `doolittle` w skrypcie `doolittle.py` przyjmuje nazwę pliku jako argument wejściowy, który zawiera dane macierzy do wykonania dekompozycji LU. Funkcja odczytuje dane z pliku, konstruuje macierz rozszerzoną, wykonuje dekompozycję LU przy użyciu algorytmu Doolittle'a, a następnie rozwiązuje układ równań, aby znaleźć nieznany wektor.

Kroki zaangażowane w algorytm są następujące:

1. Odczytanie danych z pliku: Funkcja odczytuje dane liczbowe z określonego pliku, zakładając wartości oddzielone spacjami, i konstruuje macierz.

2. Tworzenie macierzy rozszerzonej: Tworzy macierz rozszerzoną przez dodanie dodatkowej kolumny do oryginalnej macierzy, która reprezentuje stałe w układzie równań liniowych.

3. Dekompozycja LU: Algorytm Doolittle'a rozkłada macierz rozszerzoną na macierz trójkątną dolną (L) i macierz trójkątną górną (U).

4. Rozwiązanie dla wektora Y: Rozwiązuje LY = B dla Y przy użyciu substytucji w przód.

5. Rozwiązanie dla wektora X: Rozwiązuje UX = Y dla X przy użyciu substytucji wstecznej.

6. Sprawdzanie zera na przekątnej: Sprawdza, czy na przekątnej macierzy U występuje zero, co spowodowałoby dzielenie przez zero i unieważniłoby rozwiązanie.

7. Wyświetlanie wyników: Funkcja wyświetla macierz rozszerzoną, macierze L i U, oraz wektory Y i X.

## Użycie

Aby użyć skryptu, wystarczy wywołać funkcję `doolittle` z nazwą pliku danych jako argumentem. Upewnij się, że plik danych zawiera macierz w poprawnym formacie.

Przykładowe użycie:

```python
result = doolittle("data.txt")
```

## Struktura plików

- `doolittle.py`: Główny skrypt zawierający implementację algorytmu dekompozycji LU Doolittle'a.

- `data.txt`: Przykładowy plik danych zawierający dane macierzy.

## Wymagania

- Python 3.x

## Autor

Ten projekt został stworzony przez [Maksymilian Kubiczek]([@MaksKubiczek](https://github.com/MaksKubiczek)).
