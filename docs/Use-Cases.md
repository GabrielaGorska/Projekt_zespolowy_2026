# Use Case – LSWIS

---

## UC1. Rejestracja wolontariusza
**Aktor:** Wolontariusz (nowy użytkownik)  
**Warunki wstępne:** Wolontariusz nie ma konta w systemie.  
**Wyzwalacz:** Wolontariusz wybiera „Rejestracja”.

### Scenariusz podstawowy
1. Wolontariusz otwiera formularz rejestracji.
2. System wyświetla formularz (imię, nazwisko, e-mail, hasło, potwierdzenie hasła).
3. Wolontariusz uzupełnia dane i zatwierdza formularz.
4. System sprawdza poprawność danych i tworzy konto.
5. System wyświetla komunikat o poprawnej rejestracji.

**Wynik:** Konto wolontariusza jest utworzone, użytkownik może się zalogować.

### Scenariusze alternatywne
- E-mail już istnieje → system wyświetla komunikat i prosi o inny e-mail.
- Błędne dane → system pokazuje błędy przy polach i nie tworzy konta.

---

## UC2. Rejestracja organizacji
**Aktor:** Przedstawiciel organizacji  
**Warunki wstępne:** Organizacja nie ma konta w systemie.  
**Wyzwalacz:** Przedstawiciel wybiera „Zarejestruj organizację”.

### Scenariusz podstawowy
1. Przedstawiciel organizacji otwiera formularz rejestracji organizacji.
2. System wyświetla formularz (nazwa, NIP, dane kontaktowe, e-mail, hasło).
3. Przedstawiciel uzupełnia dane i wysyła zgłoszenie.
4. System zapisuje zgłoszenie i informuje, że wymaga akceptacji administratora.
5. System wyświetla komunikat „Zgłoszenie wysłane”.

**Wynik:** Konto organizacji zostaje utworzone i oczekuje na zatwierdzenie.

### Scenariusze alternatywne
- NIP lub e-mail już istnieje → system wyświetla komunikat i nie tworzy konta.

---

## UC3. Zatwierdzenie organizacji
**Aktor:** Administrator  
**Warunki wstępne:** Istnieją zgłoszenia organizacji do zatwierdzenia.  
**Wyzwalacz:** Administrator otwiera listę organizacji.

### Scenariusz podstawowy
1. Administrator przechodzi do panelu organizacji.
2. System wyświetla listę zgłoszeń oczekujących na zatwierdzenie.
3. Administrator wybiera organizację i klika „Zatwierdź”.
4. System aktywuje konto organizacji i wyświetla komunikat.
5. System wysyła e-mail do organizacji o aktywacji konta.

**Wynik:** Organizacja może korzystać z systemu.

---

## UC4. Logowanie użytkownika
**Aktor:** Wolontariusz / Organizacja / Administrator  
**Warunki wstępne:** Konto istnieje (organizacja musi być zatwierdzona).  
**Wyzwalacz:** Użytkownik wybiera „Logowanie”.

### Scenariusz podstawowy
1. Użytkownik otwiera formularz logowania (e-mail, hasło).
2. Użytkownik wpisuje dane i klika „Zaloguj”.
3. System weryfikuje dane logowania.
4. System loguje użytkownika i przekierowuje do odpowiedniego panelu.

**Wynik:** Użytkownik jest zalogowany.

### Scenariusze alternatywne
- Błędne dane → komunikat „Nieprawidłowy e-mail lub hasło”.
- Organizacja niezatwierdzona → komunikat „Konto oczekuje na zatwierdzenie”.
- Konto zablokowane → komunikat o blokadzie konta.

---

## UC5. Reset hasła
**Aktor:** Dowolny użytkownik  
**Warunki wstępne:** Użytkownik ma konto w systemie.  
**Wyzwalacz:** Użytkownik klika „Nie pamiętasz hasła?”.

### Scenariusz podstawowy
1. Użytkownik podaje e-mail i wybiera „Wyślij link”.
2. System wysyła e-mail z linkiem do ustawienia nowego hasła.
3. Użytkownik ustawia nowe hasło i zatwierdza.
4. System zapisuje nowe hasło i wyświetla komunikat o powodzeniu.

**Wynik:** Użytkownik może zalogować się nowym hasłem.

### Scenariusze alternatywne
- Link nieważny lub wygasł → komunikat i możliwość ponowienia resetu.

---

## UC6. Tworzenie wydarzenia (organizacja)
**Aktor:** Organizacja  
**Warunki wstępne:** Organizacja jest zalogowana i zatwierdzona.  
**Wyzwalacz:** Organizacja klika „Dodaj wydarzenie”.

### Scenariusz podstawowy
1. Organizacja otwiera formularz tworzenia wydarzenia.
2. System wyświetla pola (tytuł, opis, data, miejsce, limit miejsc).
3. Organizacja uzupełnia dane i zapisuje wydarzenie.
4. System zapisuje wydarzenie i pokazuje jego szczegóły.

**Wynik:** Wydarzenie jest opublikowane i widoczne na liście.

### Scenariusze alternatywne
- Błędne dane → system nie zapisuje i pokazuje błędy.

---

## UC7. Przeglądanie wydarzeń
**Aktor:** Wolontariusz (zalogowany lub niezalogowany)  
**Warunki wstępne:** W systemie istnieją wydarzenia.  
**Wyzwalacz:** Użytkownik otwiera zakładkę „Wydarzenia”.

### Scenariusz podstawowy
1. System wyświetla listę wydarzeń z podstawowymi informacjami.
2. Użytkownik może użyć filtrów (np. data, kategoria, lokalizacja) i paginacji.
3. Użytkownik wybiera wydarzenie, aby zobaczyć szczegóły.

**Wynik:** Użytkownik ma dostęp do listy i szczegółów wydarzeń.

---

## UC8. Zapis na wydarzenie
**Aktor:** Wolontariusz  
**Warunki wstępne:** Wolontariusz jest zalogowany, wydarzenie ma wolne miejsca.  
**Wyzwalacz:** Wolontariusz klika „Zapisz się”.

### Scenariusz podstawowy
1. Wolontariusz wybiera „Zapisz się” na stronie wydarzenia.
2. System prosi o potwierdzenie zapisu.
3. Wolontariusz potwierdza.
4. System zapisuje wolontariusza na wydarzenie i wyświetla komunikat.
5. System wysyła e-mail potwierdzający zapis.

**Wynik:** Wolontariusz jest zapisany na wydarzenie.

### Scenariusze alternatywne
- Brak wolnych miejsc → komunikat „Zapisy zamknięte”.
- Wolontariusz już zapisany → komunikat informacyjny.

---

## UC9. Anulowanie zapisu na wydarzenie
**Aktor:** Wolontariusz  
**Warunki wstępne:** Wolontariusz jest zapisany na wydarzenie.  
**Wyzwalacz:** Wolontariusz wybiera „Anuluj udział” w „Moje wydarzenia”.

### Scenariusz podstawowy
1. Wolontariusz wybiera wydarzenie na liście „Moje wydarzenia”.
2. Wolontariusz klika „Anuluj udział”.
3. System prosi o potwierdzenie.
4. Wolontariusz potwierdza.
5. System usuwa/anuluje zapis i wyświetla komunikat.

**Wynik:** Zapis zostaje anulowany.

---

## UC10. Lista uczestników i eksport CSV (organizacja)
**Aktor:** Organizacja  
**Warunki wstępne:** Organizacja ma wydarzenie z zapisanymi wolontariuszami.  
**Wyzwalacz:** Organizacja otwiera szczegóły wydarzenia.

### Scenariusz podstawowy
1. Organizacja przechodzi do zakładki „Uczestnicy”.
2. System wyświetla listę zapisanych wolontariuszy.
3. Organizacja klika „Eksportuj do CSV”.
4. System generuje i udostępnia plik CSV do pobrania.

**Wynik:** Organizacja pobiera listę uczestników w pliku CSV.

---

## UC11. Zarządzanie użytkownikami (administrator)
**Aktor:** Administrator  
**Warunki wstępne:** Administrator jest zalogowany.  
**Wyzwalacz:** Administrator otwiera sekcję „Użytkownicy”.

### Scenariusz podstawowy
1. System wyświetla listę użytkowników.
2. Administrator wybiera użytkownika.
3. Administrator wykonuje akcję „Zablokuj” lub „Odblokuj”.
4. System zapisuje zmianę i wyświetla komunikat.

**Wynik:** Status użytkownika zostaje zmieniony.
