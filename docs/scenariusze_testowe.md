# LSWIS – Dokumentacja testerska - Scenariusze testowe

Wersja: 1.0 | Data: 2026

---

## 1. Cel dokumentu
Celem dokumentu jest opis podejścia do testowania systemu LSWIS oraz przygotowanie scenariuszy testowych dla funkcji MVP.
Dokument ma umożliwić:
- weryfikację zgodności z wymaganiami funkcjonalnymi,
- wykrywanie regresji po zmianach,
- udokumentowanie wyników testów na potrzeby zaliczenia.

---

## 2. Zakres testów (MVP)
Testy obejmują kluczowe funkcje:
- rejestracja wolontariusza,
- rejestracja organizacji + zatwierdzenie przez administratora,
- logowanie / wylogowanie,
- reset hasła,
- tworzenie wydarzeń (organizacja),
- przeglądanie wydarzeń (lista + filtry + paginacja),
- zapis i anulowanie zapisu,
- lista uczestników + eksport CSV,
- zarządzanie użytkownikami (blokada/odblokowanie),
- e-maile systemowe (potwierdzenia i reset hasła) – weryfikacja funkcjonalna.

Poza zakresem (na potrzeby MVP):
- moduł darowizn,
- zaświadczenia PDF,
- Q&A i moderacja treści

---

## 3. Typy testów
- *Testy funkcjonalne (manualne)* – główny zakres na potrzeby zaliczenia.
- *Testy integracyjne (manualne)* – weryfikacja przepływów FE ↔ BE.
- *Testy regresji (manualne)* – szybka lista kontrolna po zmianach.

---

## 4. Środowisko testowe
- Uruchomienie projektu lokalnie (np. Docker).
- Przeglądarki: Chrome/Edge (minimum).
- Konta testowe:
  - Wolontariusz testowy (nowy / istniejący),
  - Organizacja testowa,
  - Administrator.

Jeśli w projekcie jest środowisko do przechwytywania e-maili (np. skrzynka testowa), tester weryfikuje otrzymane wiadomości i linki.


---

## 5. Dane testowe (przykładowe)
### 5.1 Wolontariusz
- Imię: Jan
- Nazwisko: Kowalski
- E-mail: jan.kowalski.test@example.com
- Hasło: TestoweHaslo1!

### 5.2 Organizacja
- Nazwa: Fundacja Pomocna Dłoń
- NIP: 7123456789
- E-mail: fundacja.test@example.com
- Telefon: 600700800
- Hasło: Organizacja1!

### 5.3 Wydarzenie
- Tytuł: Pomoc seniorom – zakupy
- Opis: Wsparcie w zakupach dla seniorów.
- Data: przyszła data (np. +7 dni)
- Lokalizacja: Lublin, ul. Testowa 1
- Limit miejsc: 10

---

## 6. Kryteria rozpoczęcia i zakończenia testów
### 6.1 Kryteria rozpoczęcia
- Aplikacja uruchamia się bez błędów krytycznych.
- Dostępne są ekrany logowania i rejestracji.
- Dostępne są konta testowe lub możliwość ich utworzenia.

### 6.2 Kryteria zakończenia
- Wszystkie przypadki testowe MVP są wykonane co najmniej 1 raz.
- Brak błędów krytycznych blokujących kluczowe funkcje (rejestracja, logowanie, wydarzenia, zapisy, eksport).
- Wyniki testów są udokumentowane.

---

## 7. Format raportowania błędów
Błąd powinien zawierać:
- ID / tytuł,
- środowisko (lokalnie, wersja aplikacji),
- kroki odtworzenia,
- rezultat oczekiwany,
- rezultat rzeczywisty,
- priorytet (P1–P3),
- załączniki (screen, log – opcjonalnie).

---

# 8. Przypadki testowe (Test Cases)

Skrót ról: **VOL** (Wolontariusz), **ORG** (Organizacja), **ADM** (Administrator)


---

## 8.1 Rejestracja wolontariusza

### VOL-01 — Poprawna rejestracja wolontariusza
*Rola:* VOL  
*Warunki:* E-mail nieużywany  
*Kroki:*
1. Otwórz ekran rejestracji wolontariusza.
2. Wypełnij poprawnie wszystkie pola.
3. Zatwierdź formularz.
*Oczekiwany wynik:* Konto zostaje utworzone, pojawia się komunikat o powodzeniu.

### VOL-02 — Rejestracja z istniejącym e-mailem
*Rola:* VOL  
*Warunki:* E-mail już istnieje w systemie  
*Kroki:* Jak w TC-REG-VOL-01, użyj istniejącego e-maila.  
*Oczekiwany wynik:* Komunikat o zajętym e-mailu, konto nie zostaje utworzone.

### VOL-03 — Błędne dane w formularzu
*Rola:* VOL  
*Kroki:*
1. Otwórz rejestrację.
2. Pozostaw wymagane pole puste lub wpisz niepoprawny e-mail.
3. Zatwierdź formularz.
*Oczekiwany wynik:* Walidacja blokuje rejestrację, błędy przy polach.

---

## 8.2 Rejestracja i zatwierdzanie organizacji

### ORG-01 — Poprawna rejestracja organizacji
*Rola:* ORG  
*Warunki:* NIP i e-mail nieużywane  
*Kroki:*
1. Otwórz rejestrację organizacji.
2. Wypełnij formularz poprawnie.
3. Wyślij zgłoszenie.
*Oczekiwany wynik:* System przyjmuje zgłoszenie i informuje o oczekiwaniu na zatwierdzenie.

### ORG-02 — Duplikat NIP lub e-mail
*Rola:* ORG  
*Warunki:* NIP lub e-mail istnieje w systemie  
*Kroki:* Jak w ORG-01, użyj duplikatu.  
*Oczekiwany wynik:* Komunikat o duplikacie, zgłoszenie nie zostaje utworzone.

### ORG-01 — Zatwierdzenie organizacji przez administratora
*Rola:* ADM  
*Warunki:* Istnieje zgłoszona organizacja  
*Kroki:*
1. Zaloguj się jako administrator.
2. Przejdź do listy organizacji.
3. Wybierz organizację i kliknij „Zatwierdź”.
*Oczekiwany wynik:* Organizacja zostaje zatwierdzona.

---

## 8.3 Logowanie i reset hasła

### LOGIN-01 — Poprawne logowanie
*Rola:* VOL / ORG / ADM  
*Kroki:*
1. Otwórz ekran logowania.
2. Wpisz poprawny e-mail i hasło.
3. Kliknij „Zaloguj”.
*Oczekiwany wynik:* Użytkownik zostaje zalogowany i widzi właściwy panel.

### LOGIN-02 — Błędne hasło
*Rola:* VOL / ORG / ADM  
*Kroki:* Wprowadź poprawny e-mail i błędne hasło.  
*Oczekiwany wynik:* Komunikat o nieprawidłowych danych, brak logowania.

### RESET-01 — Reset hasła (poprawny)
*Rola:* Dowolna  
*Warunki:* Konto istnieje  
*Kroki:*
1. Kliknij „Nie pamiętasz hasła?”.
2. Podaj e-mail i wyślij.
3. Otwórz wiadomość i przejdź linkiem.
4. Ustaw nowe hasło.
*Oczekiwany wynik:* Hasło zostaje zmienione, możliwe logowanie nowym hasłem.

---

## 8.4 Wydarzenia – tworzenie i przeglądanie

### EVENT-ORG-01 — Utworzenie wydarzenia
*Rola:* ORG  
*Warunki:* Organizacja zalogowana i zatwierdzona  
*Kroki:*
1. Przejdź do „Moje wydarzenia”.
2. Kliknij „Dodaj wydarzenie”.
3. Wypełnij poprawne dane i zapisz.
*Oczekiwany wynik:* Wydarzenie zostaje utworzone i widoczne w systemie.

### EVENT-ORG-02 — Błędne dane wydarzenia
*Rola:* ORG  
*Kroki:* Utwórz wydarzenie z brakującym tytułem lub limitem 0.  
*Oczekiwany wynik:* System blokuje zapis i pokazuje błędy.

### EVENT-VOL-01 — Lista wydarzeń (paginacja/filtry)
*Rola:* VOL / niezalogowany (jeśli dopuszczone)  
*Kroki:*
1. Wejdź na listę wydarzeń.
2. Użyj filtra (np. data).
3. Przejdź na kolejną stronę listy (paginacja).
*Oczekiwany wynik:* Lista odświeża się poprawnie zgodnie z filtrami i paginacją.

---

## 8.5 Zapisy wolontariusza i anulowanie

### SIGNUP-01 — Zapis na wydarzenie
*Rola:* VOL  
*Warunki:* Wolontariusz zalogowany, wydarzenie ma wolne miejsca  
*Kroki:*
1. Otwórz szczegóły wydarzenia.
2. Kliknij „Zapisz się” i potwierdź.
*Oczekiwany wynik:* Zapis zostaje utworzony, pojawia się komunikat o powodzeniu.

### SIGNUP-02 — Brak wolnych miejsc
*Rola:* VOL  
*Warunki:* Wydarzenie osiągnęło limit  
*Kroki:* Spróbuj się zapisać.  
*Oczekiwany wynik:* System blokuje zapis i wyświetla komunikat.

### CANCEL-01 — Anulowanie zapisu
*Rola:* VOL  
*Warunki:* Wolontariusz jest zapisany  
*Kroki:*
1. Wejdź w „Moje wydarzenia”.
2. Kliknij „Anuluj udział” i potwierdź.
*Oczekiwany wynik:* Zapis zostaje anulowany, pojawia się komunikat.

---

## 8.6 Lista uczestników i eksport CSV

### PARTICIPANTS-01 — Podgląd listy uczestników
*Rola:* ORG  
*Warunki:* Istnieje wydarzenie z zapisami  
*Kroki:*
1. Otwórz szczegóły wydarzenia.
2. Przejdź do zakładki „Uczestnicy”.
*Oczekiwany wynik:* Lista uczestników wyświetla się poprawnie.

### EXPORT-CSV-01 — Eksport listy uczestników do CSV
*Rola:* ORG  
*Warunki:* Lista uczestników dostępna  
*Kroki:*
1. Wejdź w „Uczestnicy”.
2. Kliknij „Eksportuj do CSV”.
*Oczekiwany wynik:* Pobiera się plik CSV z nagłówkami i danymi.

---

## 8.7 Panel administratora – użytkownicy

### ADMIN-USERS-01 — Blokowanie użytkownika
*Rola:* ADM  
*Warunki:* Użytkownik istnieje  
*Kroki:*
1. Otwórz „Użytkownicy”.
2. Wybierz konto i kliknij „Zablokuj”.
3. Wyloguj się i spróbuj zalogować tym użytkownikiem.
*Oczekiwany wynik:* Konto nie może się zalogować, komunikat o blokadzie.

### ADMIN-USERS-02 — Odblokowanie użytkownika
*Rola:* ADM  
*Warunki:* Konto jest zablokowane  
*Kroki:* Odblokuj konto i spróbuj zalogować się ponownie.  
*Oczekiwany wynik:* Logowanie działa poprawnie.

---

# 9. Checklist regresji (szybki test po zmianach)
- [ ] Rejestracja wolontariusza działa
- [ ] Rejestracja organizacji działa + admin zatwierdza
- [ ] Logowanie działa dla 3 ról
- [ ] Reset hasła działa (link + zmiana hasła)
- [ ] Organizacja może utworzyć wydarzenie
- [ ] Wolontariusz widzi listę wydarzeń i szczegóły
- [ ] Zapis na wydarzenie działa
- [ ] Anulowanie zapisu działa
- [ ] Lista uczestników działa
- [ ] Eksport CSV działa
- [ ] Blokowanie/odblokowanie użytkownika działa

---
