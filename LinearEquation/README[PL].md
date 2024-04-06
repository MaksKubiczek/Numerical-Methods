# Solver równań liniowych

Ten skrypt w języku Python zawiera dwie funkcje służące do rozwiązywania układów równań liniowych przy użyciu różnych metod: eliminacji Gaussa oraz eliminacji Gaussa-Crouta z częściowym wyborem kolumn. Skrypt odczytuje dane wejściowe z plików, wykonuje obliczenia i wypisuje wyniki.

## Funkcja: `solve_linear_equations`

Ta funkcja rozwiązuje układ równań liniowych za pomocą metody eliminacji Gaussa. Oto krótka charakterystyka kroków wykonywanych przez funkcję:

1. **Odczyt danych**: Funkcja odczytuje współczynniki równań liniowych z pliku.
2. **Częściowy wybór wierszy**: Wykonuje częściowy wybór wierszy w celu maksymalizacji elementu głównego.
3. **Eliminacja Gaussa**: Wykonuje eliminację Gaussa w celu przekształcenia macierzy współczynników na postać trójkątną górną.
4. **Substytucja wsteczna**: Ostatecznie stosowana jest substytucja wsteczna w celu znalezienia wartości niewiadomych.

## Funkcja: `solve_linear_equations_crout`

Ta funkcja rozwiązuje układ równań liniowych za pomocą metody eliminacji Gaussa-Crouta z częściowym wyborem kolumn. Oto co robi:

1. **Odczyt danych**: Podobnie jak pierwsza funkcja, odczytuje współczynniki równań liniowych z pliku.
2. **Częściowy wybór kolumn**: Wykonuje częściowy wybór kolumn w celu maksymalizacji elementu głównego w każdej kolumnie.
3. **Eliminacja Gaussa-Crouta**: Funkcja stosuje eliminację Gaussa-Crouta w celu przekształcenia macierzy współczynników na postać trójkątną górną.
4. **Substytucja wsteczna**: Następnie wykonuje substytucję wsteczną w celu znalezienia wartości niewiadomych.

## Wejście z pliku

Obie funkcje oczekują nazwy pliku tekstowego zawierającego macierz współczynników układu równań liniowych jako dane wejściowe. Każdy wiersz w pliku reprezentuje jedno równanie, a współczynniki są oddzielone spacją.

## Wynik

Po wykonaniu obliczeń skrypt wypisuje następujące informacje:

- Oryginalną macierz oraz macierz po obliczeniach.
- Rozwiązanie układu równań, w tym wartości niewiadomych.
- Dodatkowe informacje, takie jak wektor numerów kolumn (w przypadku metody Crouta).

## Użycie

Aby skorzystać ze skryptu, należy wywołać funkcje `solve_linear_equations` oraz `solve_linear_equations_crout` z nazwą pliku wejściowego jako argumentem.

Przykład:

```python
if __name__ == "__main__":
    solve_linear_equations("MN-6-1.txt")  # Użycie metody eliminacji Gaussa
    solve_linear_equations_crout("MN-6-2.txt")  # Użycie metody Gaussa-Crouta
```

## Autor

Ten projekt został stworzony przez [Maksymilian Kubiczek]([@MaksKubiczek](https://github.com/MaksKubiczek)).

## Licencja

Ten projekt jest objęty licencją [MIT]. Więcej informacji znajduje się w pliku LICENSE.
