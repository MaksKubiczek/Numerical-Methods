# Projekt: Opis

Ten projekt demonstruje dwie metody numeryczne do znajdowania pierwiastków równań: Metodę Siecznych oraz Metodę Newtona. Metody znajdowania pierwiastków są istotne w rozwiązywaniu równań, w których musimy znaleźć wartości \(x\), dla których \(f(x) = 0\). Projekt zawiera implementacje obu metod w języku Python wraz z wyjaśnieniem ich działania i teoretycznym tłem.

## Metoda Siecznych

Metoda Siecznych to iteracyjny algorytm znajdowania pierwiastków funkcji rzeczywistej. Rozpoczyna się od dwóch początkowych przybliżeń \(x_{-1}\) i \(x_0\) i iteracyjnie oblicza nowe przybliżenia, przecinając sieczną przez punkty \((x_{-1}, f(x_{-1}))\) i \((x_0, f(x_0))\) z osią x. Proces kontynuuje się, dopóki nie zostanie spełniony określony kryterium zbieżności lub osiągnięta zostanie wcześniej ustalona liczba iteracji.

## Metoda Newtona

Metoda Newtona, znana również jako Metoda Newtona-Raphsona, to kolejny iteracyjny algorytm znajdowania pierwiastków. Rozpoczyna się od początkowego przybliżenia \(x_0\) i iteracyjnie aktualizuje to przybliżenie za pomocą wzoru \(x_{\text{next}} = x - \frac{f(x)}{f'(x)}\), gdzie \(f'(x)\) jest pochodną funkcji \(f(x)\). Podobnie jak w przypadku Metody Siecznych, proces kontynuuje się, dopóki nie zostanie spełnione określone kryterium zbieżności lub osiągnięta zostanie wcześniej ustalona liczba iteracji.

## Użycie

Aby korzystać z projektu, wykonaj następujące kroki:

1. Sklonuj lub pobierz repozytorium.
2. Otwórz skrypt Pythona zawierający implementacje Metody Siecznych oraz Metody Newtona.
3. Podaj wymagane parametry, takie jak początkowe przybliżenia i liczbę iteracji.
4. Uruchom skrypt, aby zobaczyć wyniki obu metod.

## Technologie

- Python
- Metody Numeryczne
- Algorytmy Znajdowania Pierwiastków

## Autor

Ten projekt został stworzony przez [Maksymilian Kubiczek]([@MaksKubiczek](https://github.com/MaksKubiczek)).

## Licencja

Ten projekt jest licencjonowany na podstawie [Licencji MIT]. Aby uzyskać więcej informacji, zobacz plik LICENSE.
