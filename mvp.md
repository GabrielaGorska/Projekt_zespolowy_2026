# LSWIS – MVP (Minimalny zakres do GO-LIVE)

Wersja: 1.0 | Data: 2026

---

## 1. Cel dokumentu
Celem dokumentu jest zdefiniowanie **minimalnego zakresu funkcjonalnego (MVP)**, który musi działać,
aby system LSWIS mógł zostać uruchomiony produkcyjnie (GO-LIVE) w podstawowej wersji.

MVP obejmuje wyłącznie funkcje niezbędne do:
- publikowania wydarzeń przez organizacje,
- zapisywania się wolontariuszy na wydarzenia,
- podstawowego nadzoru administracyjnego,
- komunikacji systemowej e-mail.

---

## 2. Zakres MVP – funkcje wymagane

### 2.1 Konta i dostęp
**Musi działać:**
- Rejestracja wolontariusza (formularz + utworzenie konta).
- Logowanie i wylogowanie użytkowników (Wolontariusz / Organizacja / Administrator).
- Reset hasła poprzez e-mail (wysłanie linku + ustawienie nowego hasła).

**Kryterium GO-LIVE:** użytkownicy mogą uzyskać dostęp do systemu i odzyskać konto.

---

### 2.2 Organizacje (rejestracja i zatwierdzanie)
**Musi działać:**
- Rejestracja organizacji (zgłoszenie konta przez formularz).
- Zatwierdzanie organizacji przez administratora.
- Blokada dostępu do funkcji organizatora dla organizacji niezatwierdzonej.

**Kryterium GO-LIVE:** tylko zatwierdzone organizacje mogą publikować wydarzenia.

---

### 2.3 Wydarzenia (tworzenie i publikacja)
**Musi działać:**
- Organizacja może utworzyć wydarzenie zawierające minimum:
  - tytuł, opis,
  - data,
  - lokalizacja (tekstowa),
  - limit miejsc.
- System pokazuje listę aktywnych wydarzeń.
- System pokazuje szczegóły wydarzenia.

**Kryterium GO-LIVE:** organizacje mogą publikować wydarzenia, a wolontariusze mogą je przeglądać.

---

### 2.4 Zapisy wolontariuszy na wydarzenia
**Musi działać:**
- Wolontariusz może zapisać się na wydarzenie.
- System egzekwuje limit miejsc (brak możliwości zapisu po osiągnięciu limitu).
- Wolontariusz może anulować zapis.
- Organizacja widzi listę uczestników dla własnego wydarzenia.

**Kryterium GO-LIVE:** cykl „wydarzenie → zapis → anulacja → lista uczestników” działa end-to-end.

---

### 2.5 E-maile systemowe (minimum)
**Musi działać:**
- E-mail resetu hasła.
- E-mail potwierdzający zapis na wydarzenie.
- E-mail potwierdzający anulowanie zapisu.

**Kryterium GO-LIVE:** kluczowe operacje użytkownika mają potwierdzenia e-mail.

---

### 2.6 Panel administratora (minimum)
**Musi działać:**
- Lista użytkowników i organizacji.
- Zatwierdzanie organizacji.
- Blokowanie / odblokowywanie kont użytkowników (co najmniej wolontariuszy i organizacji).

**Kryterium GO-LIVE:** administrator ma podstawową kontrolę nad dostępem i kontami.

---

## 3. Wymagania minimalne jakości
Minimum jakościowe:

- **Uprawnienia ról:** widoki i akcje dostępne zgodnie z rolą (RBAC w podstawowym zakresie).
- **Walidacje formularzy:** wymagane pola, poprawny format e-mail, limit > 0, data nie w przeszłości.
- **Stabilność uruchomienia:** aplikacja uruchamia się w przewidywalny sposób
- **Obsługa błędów użytkownika:** komunikaty walidacyjne i informacyjne (bez ujawniania danych wrażliwych).

---

## 4. Funkcje poza MVP (po GO-LIVE)
Funkcje, które nie są wymagane do minimalnego uruchomienia:

- Moduł darowizn i płatności online.
- Check-in i zaawansowane statusy obecności.
- Q&A, wiadomości grupowe, aktualizacje wydarzeń.
- Moderacja treści.

---

## 5. Definicja „GO-LIVE”
System może zostać uznany za gotowy do GO-LIVE, jeśli:
- wszystkie elementy z sekcji **2. Zakres MVP** działają poprawnie,
- operacje end-to-end (rejestracja → logowanie → wydarzenia → zapisy → anulacja → administracja) są przetestowane,
- e-maile resetu hasła oraz potwierdzeń zapisów/anulacji są wysyłane i zawierają poprawne informacje.

---
