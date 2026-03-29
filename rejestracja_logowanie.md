# LSWIS – Functional Specification: Rejestracja, Logowanie

Wersja: 1.0 | Data: 2026

---

## 1. Cel modułu
Moduł rejestracji i logowania zapewnia dostęp do systemu LSWIS dla trzech ról użytkowników:
- Wolontariusz
- Organizacja
- Administrator

Moduł obejmuje rejestrację kont, logowanie, reset hasła oraz podstawowe zasady dostępu.

---

## 2. Rejestracja wolontariusza
### 2.1 Opis
System umożliwia samodzielne utworzenie konta wolontariusza poprzez formularz rejestracyjny.

### 2.2 Dane wejściowe (formularz)
- Imię
- Nazwisko
- Adres e-mail
- Hasło
- Potwierdzenie hasła

### 2.3 Reguły
- Adres e-mail musi być unikalny.
- Hasło musi spełniać minimalne wymagania bezpieczeństwa (np. długość i złożoność – dokładne progi do ustalenia w projekcie).
- Po poprawnej rejestracji konto wolontariusza jest aktywne i użytkownik może się zalogować.

### 2.4 Komunikaty i błędy
- „Konto utworzone” / „Rejestracja zakończona”
- „Konto z takim adresem e-mail już istnieje”
- „Niepoprawne dane w formularzu” (z podświetleniem błędnych pól)

---

## 3. Rejestracja organizacji
### 3.1 Opis
System umożliwia rejestrację konta organizacji przez przedstawiciela organizacji. Konto organizacji wymaga zatwierdzenia przez administratora.

### 3.2 Dane wejściowe (formularz)
- Nazwa organizacji
- NIP
- Adres (ulica, miasto, kod)
- Osoba kontaktowa (imię i nazwisko)
- Adres e-mail organizacji
- Telefon kontaktowy
- Hasło
- Potwierdzenie hasła

### 3.3 Reguły
- NIP i adres e-mail muszą być unikalne.
- Po rejestracji konto organizacji oczekuje na zatwierdzenie przez administratora.
- Do czasu zatwierdzenia organizacja nie ma pełnego dostępu do funkcji organizatora.

### 3.4 Komunikaty i błędy
- „Zgłoszenie rejestracji organizacji zostało przyjęte”
- „Organizacja o takim NIP / e-mailu już istnieje”
- „Niepoprawne dane w formularzu”

---

## 4. Zatwierdzanie organizacji przez administratora
### 4.1 Opis
Administrator podejmuje decyzję o zatwierdzeniu lub odrzuceniu konta organizacji.

### 4.2 Reguły
- Administrator może zatwierdzić konto (organizacja uzyskuje dostęp do funkcji organizatora).
- Administrator może odrzucić zgłoszenie (organizacja nie uzyskuje dostępu).

### 4.3 Komunikaty
- „Konto organizacji zostało zatwierdzone”
- „Zgłoszenie organizacji zostało odrzucone”

---

## 5. Logowanie użytkownika
### 5.1 Opis
System umożliwia logowanie użytkowników na podstawie e-maila i hasła.

### 5.2 Reguły
- System weryfikuje poprawność danych logowania.
- System odmawia dostępu kontom zablokowanym.
- W przypadku organizacji system wymaga wcześniejszego zatwierdzenia konta.

### 5.3 Wynik
Po poprawnym logowaniu użytkownik zostaje przekierowany do panelu zależnego od roli:
- Wolontariusz → „Moje wydarzenia”
- Organizacja → panel organizacji
- Administrator → panel administracyjny

### 5.4 Komunikaty i błędy
- „Zalogowano pomyślnie”
- „Nieprawidłowy e-mail lub hasło”
- „Twoje konto jest zablokowane”
- „Konto organizacji oczekuje na zatwierdzenie”

---

## 6. Reset hasła
### 6.1 Opis
System umożliwia odzyskanie dostępu do konta poprzez ustawienie nowego hasła z użyciem linku wysyłanego e-mailem.

### 6.2 Przebieg
1. Użytkownik podaje adres e-mail w formularzu resetu hasła.
2. System wysyła wiadomość z linkiem do ustawienia nowego hasła.
3. Użytkownik ustawia nowe hasło i zatwierdza.
4. System zapisuje nowe hasło i informuje o sukcesie operacji.

### 6.3 Reguły
- Link do resetu hasła jest jednorazowy i ma ograniczony czas ważności.
- Nowe hasło musi spełniać minimalne wymagania bezpieczeństwa.

### 6.4 Komunikaty i błędy
- „Link do zmiany hasła został wysłany”
- „Nie można zresetować hasła – link nieważny lub wygasł”
- „Hasło nie spełnia wymagań”

---
