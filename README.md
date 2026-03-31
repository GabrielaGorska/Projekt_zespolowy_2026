# Karta projektu – Zaawansowany Projekt Zespołowy (Grupa 6)

## Projekt Zespołowy – Grupa 6
**Lubelski System Wsparcia Inicjatyw Społecznych (LSWIS)**  
_Ułatwienie organizacji wydarzeń społecznych i wspieranie wolontariuszy na terenie miasta Lublina._

---

## 1. Zespół projektowy i odpowiedzialności
- **Kierownik projektu:** ~~Szymon Chmielewski~~ → Mikołaj Łukasiewicz  
  Odpowiedzialność: plan prac, podział zadań, kontrola realizacji harmonogramu, przygotowanie prezentacji końcowej.
- **Analityk systemowy:** Damian Abramczuk  
  Odpowiedzialność: analiza wymagań, user stories, kryteria akceptacji, spójność dokumentacji funkcjonalnej.
- **Programista backend/frontend:** ~~Szymon Chmielewski~~, ~~Damian Abramczuk~~, Beata Podgórska  
  Odpowiedzialność: implementacja API oraz interfejsu użytkownika, integracja FE–BE, utrzymanie jakości kodu.
- **UI/UX Designer:** Gabriela Górska  
  Odpowiedzialność: makiety i prototyp w Figma, spójność UI, ergonomia widoków i formularzy.
- **QA / Tester:** Gabriela Górska  
  Odpowiedzialność: scenariusze testowe, testy funkcjonalne, raportowanie błędów, weryfikacja kryteriów akceptacji.

---

## 2. Tytuł projektu
**Lubelski System Wsparcia Inicjatyw Społecznych (LSWIS)**

---

## 3. Cel projektu
Celem projektu jest stworzenie działającej aplikacji webowej (prototypu) wspierającej koordynację wydarzeń społecznych i wolontariatu.

**Cel zostanie uznany za osiągnięty, jeśli:**
1. Wolontariusz może utworzyć konto, zalogować się i zapisać na wydarzenie (w tym potwierdzić zapis e-mailem).
2. Organizacja może utworzyć wydarzenie z opisem, datą i lokalizacją oraz przeglądać listę zapisów.
3. Administrator ma wgląd w konta i wydarzenia oraz może zarządzać statusem użytkowników (blokada/odblokowanie).
4. Aplikacja uruchamia się lokalnie w środowisku developerskim i umożliwia demonstrację kluczowych funkcji.

---

## 4. Uzasadnienie biznesowe / edukacyjne
Projekt odpowiada na potrzebę usprawnienia koordynacji inicjatyw społecznych w mieście Lublin poprzez:
- ułatwienie publikacji wydarzeń przez organizacje,
- zapewnienie prostych zapisów wolontariuszy,
- wsparcie komunikacji i potwierdzania udziału (e-mail).

---

## 5. Zakres projektu (MVP + rozszerzenia + poza zakresem)

### 5.1 Zakres MVP (obowiązkowy na zaliczenie)
- Rejestracja i logowanie wolontariuszy.
- Rejestracja kont organizacji oraz zatwierdzanie kont organizacji przez administratora.
- Tworzenie i publikacja wydarzeń (organizacja).
- Lista aktywnych wydarzeń (dla wolontariuszy) z możliwością zapisu.
- Zapis na wydarzenie + anulowanie zapisu.
- Podstawowy panel administratora (podgląd kont i wydarzeń, blokowanie/odblokowywanie użytkowników).
- Integracja z serwisem pocztowym w celu wysyłki e-maili systemowych.

### 5.2 Funkcje rozszerzające
- Statystyki aktywności użytkowników i wydarzeń.
- Eksport danych do CSV.
- Komunikaty globalne administratora.

### 5.3 Poza zakresem (out of scope / odrzucone)
- Płatności produkcyjne (pełna obsługa księgowa, faktury/rachunki, rozliczenia).
- Czat w czasie rzeczywistym.
- SMS-y oraz integracje powiadomień push.
- Logowanie społecznościowe.

---

## 6. Główne wymagania i kryteria akceptacji

### 6.1 Rejestracja i logowanie
**Wymaganie:** System umożliwia rejestrację i logowanie wolontariusza.  
**Kryteria akceptacji:**
- Użytkownik może utworzyć konto przy użyciu e-mail i hasła.
- Po poprawnym zalogowaniu użytkownik ma dostęp do listy wydarzeń i profilu.

### 6.2 Wydarzenia i zapisy
**Wymaganie:** Organizacja może dodać wydarzenie z opisem, datą i miejscem.  
**Kryteria akceptacji:**
- Organizacja tworzy wydarzenie, które pojawia się na liście aktywnych wydarzeń.
- Wolontariusz może zapisać się na wydarzenie, a organizator widzi zapis na liście uczestników.

### 6.3 Potwierdzanie udziału e-mail
**Wymaganie:** System wysyła e-mail z linkiem potwierdzającym zapis.  
**Kryteria akceptacji:**
- Po zapisie wolontariusz otrzymuje e-mail z linkiem potwierdzającym.
- Po kliknięciu linku status zapisu zmienia się na „potwierdzony”.

### 6.4 Panel administratora
**Wymaganie:** Administrator nadzoruje konta i aktywność.  
**Kryteria akceptacji:**
- Administrator ma wgląd w listę użytkowników i organizacji.
- Administrator może zablokować/odblokować użytkownika.
- Administrator może zatwierdzić konto organizacji.

---

## 7. Metodyka pracy i organizacja
- Model pracy: **Scrum** (krótkie iteracje + backlog + regularne przeglądy).
- Planowanie: backlog w Jira, priorytetyzacja funkcji MVP.
- Komunikacja: Discord (ustalone spotkania statusowe 1× w tygodniu).
- Kontrola jakości: code review, testy podstawowe, spójna dokumentacja.

### Definicja „Done” (ukończone)
Zadanie jest ukończone, jeśli:
- zostało zaimplementowane i zintegrowane,
- spełnia kryteria akceptacji,
- działa w środowisku developerskim,
- ma podstawową weryfikację (test manualny lub automatyczny),

---

## 8. Zasoby i narzędzia
- **Technologie:** Node.js (NestJS), Angular, PostgreSQL
- **Środowisko i CI/CD:** Docker, GitHub Actions
- **Zarządzanie projektem:** Jira
- **Projektowanie UI/UX:** Figma
- **Komunikacja:** Discord
- **Dokumentacja API:** Swagger / OpenAPI

---

## 9. Harmonogram (wstępny) + produkty etapów
| Etap | Zakres prac | Produkt (deliverable) | Czas realizacji |
|------|-------------|------------------------|----------------|
| 1 | Analiza wymagań i dokumentacja | Założenia, user stories, kryteria akceptacji | 1–2 tydzień |
| 2 | Projekt UI/UX i architektury | Makiety Figma, model danych (ERD), zarys API | 3–4 tydzień |
| 3 | Implementacja MVP | Działające FE/BE + e-mail + podstawowe role | 5–7 tydzień |
| 4 | Testy i poprawki | Scenariusze testów + raport błędów + poprawki | 8 tydzień |
| 5 | Dokumentacja i prezentacja | Instrukcja użytkownika, dokumentacja dev, demo | 9–10 tydzień |

---

## 10. Ryzyka i działania zapobiegawcze
| Ryzyko | Prawdopodobieństwo | Oddziaływanie | Działanie zapobiegawcze |
|-------|---------------------|---------------|--------------------------|
| Brak regularnej komunikacji w zespole | Średnie | Wysokie | Stałe spotkanie tygodniowe na Discord + aktualizacje w Jira. |
| Opóźnienia w implementacji | Średnie | Wysokie | Priorytetyzacja MVP, dzielenie zadań, kontrola kamieni milowych. |
| Brak doświadczenia w NestJS/Angular | Wysokie | Średnie | Prototypowanie, małe iteracje, korzystanie z dokumentacji. |
| Problemy z integracją backend–frontend | Średnie | Wysokie | Wczesny kontrakt API (Swagger), testy integracyjne od początku. |
| Problemy z wysyłką e-mail (SMTP, deliverability) | Średnie | Średnie | Środowisko testowe (np. Mailpit), retry, logowanie błędów. |
| Konflikty w repozytorium Git | Średnie | Średnie | Branchowanie feature, częste merge, code review. |
| Brak czasu członków zespołu | Wysokie | Średnie | Bufor czasowy, realne planowanie zadań, równoważenie obciążenia. |

---

## 11. Oczekiwane rezultaty
- Działający **prototyp aplikacji webowej** (MVP).
- **Dokumentacja projektowa**
- **Prezentacja końcowa**
---

## 12. Kryteria sukcesu
- Aplikacja uruchamia się i działa poprawnie w przeglądarce.
- Funkcje MVP działają zgodnie z kryteriami akceptacji (rejestracja, logowanie, wydarzenia, zapisy, e-mail).
- Dostępna jest kompletna dokumentacja (funkcjonalna i developerska).
- Prezentacja końcowa obejmuje działające demo oraz omówienie architektury i procesu wytwarzania.

---

## 13. Akceptacja projektu
**Zatwierdza:**  
Prowadzący: ..............................................  
Kierownik projektu: **Mikołaj Łukasiewicz**

---

📅 _Grupa projektowa nr 6 – Lublin, 2026
_Wersja dokumentu: 1.2_
