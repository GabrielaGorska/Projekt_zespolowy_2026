# Założenia systemu – LSWIS  
**Lubelski System Wsparcia Inicjatyw Społecznych**

---

## Założenia funkcjonalne

### 1. Użytkownicy i role
- System umożliwia rejestrację wolontariuszy.
- System umożliwia logowanie użytkowników przy użyciu adresu e-mail i hasła.
- Administrator zatwierdza konta organizacji.
- System umożliwia reset hasła poprzez wysłanie linku na adres e-mail.
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~System umożliwia logowanie za pomocą kont społecznościowych (Google/Facebook).~~

---

### 2. Wydarzenia społeczne
- Wydarzenie ma maksymalny limit miejsc.
- System wyświetla listę wszystkich aktywnych wydarzeń.
- Wolontariusz może zapisać się na wydarzenie.
- Wolontariusz może anulować zapis na wydarzenie.
- Organizator wydarzenia może przeglądać listę zapisanych wolontariuszy.
- System blokuje rekrutację po osiągnięciu limitu miejsc.
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~System umożliwia tworzenie listy rezerwowej po przekroczeniu limitu miejsc.~~
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~System umożliwia automatyczne przypisywanie wolontariuszy do wydarzeń na podstawie kompetencji.~~

---

### 3. Powiadomienia i e-mail
- System wysyła e-mail potwierdzający rejestrację.
- System wysyła e-mail potwierdzający zapis na wydarzenie.
- System wysyła e-mail potwierdzający anulowanie udziału w wydarzeniu.
- System powiadamia organizatora o nowych zapisach.
- System wysyła przypomnienie o wydarzeniu dzień wcześniej.
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~System wysyła SMS z przypomnieniem o wydarzeniu (integracja z bramką SMS).~~

---

### 4. Moduł płatności / darowizn
- System umożliwia dokonywanie dobrowolnych darowizn.
- System integruje się z zewnętrznym operatorem płatności (np. Stripe).
- Użytkownik otrzymuje potwierdzenie darowizny e-mailowo.
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~System wystawia automatyczne potwierdzenia księgowe (faktury/rachunki) dla darowizn.~~

---

### 5. Panel administracyjny
- Administrator może przeglądać wszystkie konta, wydarzenia i zapisy.
- Administrator może blokować i odblokowywać użytkowników.
- Administrator może dodawać komunikaty globalne.
- Ma wszystkie uprawnienia dostęne dla innych użytkowników.
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~Administrator może edytować treści wydarzeń utworzonych przez organizacje (bez ich udziału).~~

---

### 6. Profil i kompetencje wolontariusza
- Wolontariusz może wprowadzać swoje kompetencje i umiejętności.
- System sugeruje wydarzenia dopasowane do profilu wolontariusza.
- Wolontariusz może przeglądać historię swoich wydarzeń.
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~Wolontariusz może dodawać certyfikaty i załączniki potwierdzające kompetencje (upload plików).~~

---

### 7. Komunikacja
- Organizator może wysłać wiadomość grupową do uczestników.
- Wolontariusze mogą zadawać pytania organizatorowi (Q&A).
- Organizacja może publikować aktualizacje wydarzenia.
- System powiadamia o zmianach w wydarzeniu (np. godzina, miejsce).
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~System udostępnia czat w czasie rzeczywistym dla wydarzenia (real-time chat).~~

---

### 8. Moderacja treści
- Administrator może moderować treści użytkowników.
- System automatycznie ukrywa treści zawierające niedozwolone słowa.
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~System wykorzystuje automatyczną klasyfikację treści (AI) do wykrywania mowy nienawiści.~~

---

### 9. Geolokalizacja
- Wydarzenia mogą zawierać dane geolokalizacyjne.
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~System prezentuje wydarzenia na mapie (integracja z Google Maps / OpenStreetMap).~~

---

### 10. Statystyki
- Statystyki mogą być pobierane z systemu w formie raportów CSV.
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~System prezentuje satystyki w formie graficznej.~~

---

## Założenia niefunkcjonalne

### 13. Bezpieczeństwo
- Hasła przechowywane są w formie zahaszowanej (bcrypt).
- Wymagana jest ponowna autoryzacja po okresie nieaktywności (sesja wygasa).
- Panel administracyjny jest dostępny wyłącznie dla roli `ADMIN`.
- Komunikacja API odbywa się wyłącznie przez HTTPS.
- Ochrona przed SQL Injection jest zapewniona poprzez ORM (TypeORM).
- System posiada limit prób logowania (ochrona przed brute-force).
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~Uwierzytelnianie wieloskładnikowe (2FA) dla kont administracyjnych.~~

---

### 14. Wydajność
- API odpowiada w czasie < 300 ms dla 95% zapytań.
- Paginacja jest obowiązkowa dla list.
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~Wprowadzenie cache (np. Redis) dla list wydarzeń i statystyk.~~

---

### 15. Niezawodność
- Dostępność systemu wynosi minimum 95%.
- System automatycznie odzyskuje utracone połączenie z bazą.
- System ponawia wysyłkę e-maili w przypadku błędu (retry).
- Błąd jednej usługi nie blokuje działania całego systemu (fail-safe).
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~Wysoka dostępność bazy danych (replikacja/klaster) w środowisku produkcyjnym.~~

---

### 16. Użyteczność
- System jest responsywny na urządzeniach mobilnych.
- Formularze są walidowane po stronie klienta i serwera.
- Nawigacja i layout są zgodne z projektem.
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~Tryb dostępności WCAG 2.1 AA jako wymaganie obowiązkowe.~~

---

### 17. Skalowalność
- Baza danych może zostać przeniesiona do chmury (AWS).
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~System działa w architekturze mikroserwisowej z osobnymi usługami dla e-mail i wydarzeń.~~

---

### 18. Konserwowalność
- Testy jednostkowe zapewniają minimum 30% pokrycia.
- Dostępna jest automatyczna dokumentacja API (Swagger).
- ❌ **[ODRZUCONE PRZEZ BIZNES]** ~~Testy E2E jako wymaganie obowiązkowe (np. Cypress/Playwright) przed każdym wdrożeniem.~~
