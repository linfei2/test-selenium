# test-selenium
automated registration test

Automatyzacja przypadku testowego przy pomocy Selenium Webdriver według wzoru Page Object Pattern

Przypadek testowy

ID: 001
Tytuł: Rejestracja użytkownika na stronie www.eobuwie.com.pl przy użyciu nieprawidłowego adresu e-mail
Środowisko: Chrome wersja 83.0.4103.61, Ubuntu (64-bit)
Warunek wstępny: Uruchomiona przeglądarka. Użytkownik nie jest zalogowany.
Kroki:
1. Wejdź na stronę https://www.eobuwie.com.pl/
2. Zaakceptuj zgodę na dopasowywanie treści oraz promocji
3. Kliknij „Zarejestruj”
4. Wpisz imię
5. Wpisz nazwisko
6. Wpisz nieprawidłowy adres e-mail
7. Wpisz hasło
8. Potwierdź hasło
9. Zaakceptuj regulamin
10. Kliknij „Załóż nowe konto”
Oczekiwany rezultat:
Rejestracja nie udaje się. Pojawia się komunikat „Wprowadzono niepoprawny adres e-mail”.
