# Opis Projektu

Ten projekt demonstruje metody numeryczne do rozwiązywania równań różniczkowych zwyczajnych (ODE). Zawiera implementacje metody Eulera, metody Rungego-Kutty drugiego rzędu (RK2) oraz metody Rungego-Kutty czwartego rzędu (RK4). Projekt składa się z kilku plików Pythona, z których każdy zawiera określone funkcjonalności.

## Pliki

1. **diff_equations.py**: Ten plik zawiera definicje równań różniczkowych używanych w projekcie.
2. **numerical_methods.py**: Ten plik zawiera implementacje metod numerycznych do rozwiązywania ODE, mianowicie metody Eulera, metody Rungego-Kutty drugiego rzędu (RK2) oraz metody Rungego-Kutty czwartego rzędu (RK4).
3. **main.py**: To główny skrypt, który importuje funkcje z innych plików, definiuje dane wejściowe i oblicza rozwiązania równań różniczkowych za pomocą różnych metod numerycznych.

## Użycie

1. **diff_equations.py**: W tym pliku możesz zdefiniować własne równania różniczkowe, dodając funkcje podobne do `diff_eq1` i `diff_eq2`.
2. **numerical_methods.py**: Ten plik zawiera funkcje metod numerycznych. Możesz używać tych metod do rozwiązywania równań różniczkowych zdefiniowanych w `diff_equations.py`.
3. **main.py**: Ten skrypt służy jako punkt wejścia do projektu. Możesz zdefiniować dane wejściowe, takie jak warunki początkowe i wielkość kroku, oraz obliczać rozwiązania równań różniczkowych za pomocą różnych metod numerycznych.

## Jak Uruchomić

1. Sklonuj lub pobierz repozytorium.
2. Otwórz katalog projektu w swoim preferowanym środowisku Pythona.
3. Uruchom skrypt `main.py`.

## Użyte Technologie

- Python
- Metody Numeryczne
- Równania Różniczkowe

## Autor

Ten projekt został stworzony przez [Maksymilian Kubiczek] ([@MaksKubiczek](https://github.com/MaksKubiczek)).

## Licencja

Ten projekt jest licencjonowany na zasadach [MIT License]. Więcej informacji znajduje się w pliku LICENSE.
