# Projekt Aproksymacji Wielomianowej

## Wstęp

Aproksymacja wielomianowa to podstawowa technika w analizie numerycznej, która służy do przybliżenia zestawu punktów danych za pomocą funkcji wielomianowej. Znajduje zastosowanie w różnych dziedzinach, takich jak inżynieria, fizyka, ekonomia i grafika komputerowa. Ten projekt w języku Python ma na celu przybliżenie zestawu punktów danych za pomocą wielomianu o określonym stopniu. Projekt wykorzystuje metodę najmniejszych kwadratów do znalezienia wielomianu, który najlepiej pasuje do danych punktów.

## Teoria tła

Aproksymacja wielomianowa polega na znalezieniu funkcji wielomianowej, która jak najlepiej pasuje do zestawu punktów danych. Funkcja wielomianowa jest zwykle wyrażana jako:

\[ f(x) = a_0 + a_1x + a_2x^2 + ... + a_nx^n \]

gdzie \( a_0, a_1, ..., a_n \) to współczynniki do wyznaczenia, a \( n \) to stopień wielomianu. Celem jest znalezienie współczynników \( a_0, a_1, ..., a_n \) takich, że wielomian \( f(x) \) najlepiej pasuje do danych punktów.

## Kroki

1. **Definiowanie Węzłów Interpolacji i Wartości:**
   - Zdefiniowanie węzłów interpolacji (xi) oraz odpowiadających im wartości funkcji (fi).

2. **Wybór Stopnia Wielomianu Aproksymującego:**
   - Określenie stopnia (n) wielomianu, który ma być użyty do aproksymacji.

3. **Obliczanie Funkcji Wagi:**
   - Stworzenie funkcji wagi (wi) o tej samej długości co węzły interpolacji.

4. **Obliczanie Macierzy G:**
   - Obliczenie macierzy G, która jest używana do rozwiązania układu równań dla wielomianu aproksymującego. Macierz G jest obliczana przy użyciu węzłów interpolacji, funkcji wagi i określonego stopnia wielomianu.

5. **Obliczanie Wektora F:**
   - Obliczanie wektora F, który zawiera wartości dla każdego stopnia wielomianu. Wektor F jest obliczany przy użyciu węzłów interpolacji, wartości funkcji i funkcji wagi.

6. **Rozwiązywanie Układu Równań Metodą Gaussa:**
   - Rozwiązanie układu równań w celu znalezienia współczynników wielomianu aproksymującego. Dzieje się to za pomocą metody Gaussa.

7. **Wyświetlanie Wyników:**
   - Wyświetlenie liczby węzłów interpolacji, współczynników wielomianu aproksymującego oraz węzłów interpolacji wraz z odpowiadającymi im wartościami funkcji.

## Użycie

1. Zdefiniuj węzły interpolacji (xi) oraz odpowiadające im wartości funkcji (fi).
2. Wybierz stopień (n) wielomianu aproksymującego.
3. Uruchom skrypt Pythona, aby wykonać aproksymację wielomianową.
4. Przejrzyj wyświetlone wyniki, w tym współczynniki wielomianu aproksymującego oraz węzły interpolacji wraz z odpowiadającymi im wartościami funkcji.

## Technologie

- Python
- Metody Numeryczne
- Metoda Najmniejszych Kwadratów

## Autor

Ten projekt został stworzony przez [Maksymilian Kubiczek] ([@MaksKubiczek](https://github.com/MaksKubiczek)).

## Licencja

Ten projekt jest licencjonowany na podstawie [Licencji MIT]. Aby uzyskać więcej informacji, zapoznaj się z plikiem LICENSE.
