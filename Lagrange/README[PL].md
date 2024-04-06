# Projekt: Interpolacja Lagrange'a

Ten projekt w języku Python ma na celu pokazanie interpolacji Lagrange'a, zarówno z danymi z pliku, jak i z ręcznie wprowadzonymi danymi. Interpolacja Lagrange'a to metoda tworzenia nowych punktów danych w zakresie dyskretnego zestawu znanych punktów danych. W tym projekcie wielomian interpolacji Lagrange'a jest obliczany i oceniany w określonych punktach.

## Jak to działa

### Funkcja lagrange_interpolation_with_file

Ta funkcja odczytuje punkty danych z pliku zawierającego współrzędne x i y węzłów interpolacji. Następnie oblicza wielomian interpolacji Lagrange'a i ocenia go w określonym punkcie. Wyniki są wyświetlane, w tym liczba węzłów interpolacji, punkty danych, punkt, w którym oceniany jest wielomian, oraz wartość wielomianu interpolacji Lagrange'a w tym punkcie.

### Funkcja lagrange_interpolation

Ta funkcja wykonuje interpolację Lagrange'a, używając ręcznie podanych wartości x i y. Oblicza wielomian interpolacji Lagrange'a i ocenia go w określonym punkcie.

## Wyniki

1. **Interpolacja z Danymi z Pliku**
   - Liczba węzłów interpolacji: 4
   - Dane:

    ```
     1.000000 1.000000
     2.000000 4.000000
     3.000000 9.000000
     4.000000 16.000000
    ```
   - Punkt, w którym oceniany jest wielomian: -1
   - Wartość wielomianu interpolacji Lagrange'a w punkcie -1 to: -2.000000

   - Liczba węzłów interpolacji: 4
   - Dane:
     ```
     1.000000 1.000000
     2.000000 4.000000
     3.000000 9.000000
     4.000000 16.000000
     ```
   - Punkt, w którym oceniany jest wielomian: 0.5
   - Wartość wielomianu interpolacji Lagrange'a w punkcie 0.5 to: 2.625000

2. **Interpolacja z Danymi Ręcznymi**
   - Pierwiastek trzeciego stopnia z 50 wynosi około 3.6336.

Wyniki pokazują zastosowanie interpolacji Lagrange'a w przybliżaniu wartości w określonym zakresie punktów danych, zarówno z danymi z pliku, jak i ręcznie wprowadzonymi danymi.

## Technologie

- Python
- Interpolacja Lagrange'a

## Autor

Ten projekt został stworzony przez ([MaksKubiczek](https://github.com/MaksKubiczek)).

## Licencja

Ten projekt jest licencjonowany na podstawie [Licencji MIT]. Aby uzyskać więcej informacji, zobacz plik LICENSE.
