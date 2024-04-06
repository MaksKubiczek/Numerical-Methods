# Projekt: Rozwiązanie układu równań za pomocą metody Jacobiego

## Opis

Projekt ten skupia się na rozwiązaniu układu równań liniowych za pomocą metody Jacobiego. Jest to algorytm iteracyjny, który znajduje przybliżone rozwiązanie układu równań liniowych. Projekt zawiera funkcje do odczytywania danych z pliku, sprawdzania, czy macierz jest słabo diagonalnie dominująca, oraz dekompozycji macierzy na formę dolną-górną i odwrotność macierzy D. Dodatkowo, zaimplementowano algorytm metody Jacobiego oraz wersję tej metody z warunkiem stopu opartym na różnicy kolejnych przybliżeń mniejszej niż zadana epsilon.

## Składniki projektu

1. **read_file(filename)**: Funkcja odczytująca dane z pliku. Plik zawiera wymiar macierzy oraz jej elementy oraz wektor wyrazów wolnych.
2. **is_diagonally_dominant(n, A)**: Funkcja sprawdzająca, czy macierz jest słabo diagonalnie dominująca.
3. **decompose(n, A)**: Funkcja dokonująca dekompozycji macierzy na formę dolną-górną (LU) oraz odwrotność macierzy D.
4. **jacobi(n, A, b, max_iter)**: Implementacja algorytmu metody Jacobiego.
5. **jacobi_stop(n, A, b, epsilon, max_iter)**: Implementacja metody Jacobiego z warunkiem stopu opartym na zadanej wartości epsilon.

## Użycie

1. Uruchomienie pliku `Jacobi.py`.
2. Plik wejściowy `data.txt` zawiera dane w formacie: wymiar macierzy, elementy macierzy, oraz wektor wyrazów wolnych.
3. Projekt wczytuje dane, sprawdza, czy macierz jest słabo diagonalnie dominująca, a następnie dokonuje dekompozycji macierzy.
4. Użytkownik może podać maksymalną liczbę iteracji oraz wartość epsilon dla warunku stopu.
5. Projekt wyświetla rozwiązania dla obu metod (standardowej i z warunkiem stopu) oraz informuje, czy warunek stopu został spełniony.

## Technologie

- Python
- Metoda Jacobiego
- Obsługa plików

## Autor

Ten projekt został stworzony przez [Maksymilian Kubiczek]([@MaksKubiczek](https://github.com/MaksKubiczek)).

## Licencja

Ten projekt jest objęty licencją [MIT]. Więcej informacji znajduje się w pliku LICENSE.