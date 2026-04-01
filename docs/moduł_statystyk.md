# LSWIS – Specyfikacja funkcjonalna: Eksport danych (CSV)

Wersja: 1.0 | Data: 2026

---

## 1. Cel modułu
Celem modułu eksportu jest umożliwienie pobrania danych z systemu LSWIS w formacie **CSV** w celu:
- analizy danych poza systemem (np. Excel),
- archiwizacji,
- raportowania na potrzeby organizacji lub administracji.

Moduł nie obejmuje prezentacji statystyk w systemie (wykresy, dashboardy).

---

## 2. Dostęp i role
### 2.1 Organizacja (Organizator)
Organizacja może eksportować dane dotyczące **własnych wydarzeń**, w szczególności:
- listę uczestników dla wybranego wydarzenia,
- (opcjonalnie) listę własnych wydarzeń w zadanym okresie.

### 2.2 Administrator
Administrator może eksportować dane systemowe w szerszym zakresie:
- dane użytkowników (wolontariusze / organizacje),
- dane wydarzeń,
- dane zapisów,
- (opcjonalnie) dane darowizn – jeśli moduł darowizn jest w zakresie.

---

## 3. Zakres eksportowanych danych
### 3.1 Eksport listy uczestników wydarzenia (organizacja)
**Dane w pliku CSV (minimum):**
- Imię i nazwisko uczestnika
- Adres e-mail
- Data zapisu
- (opcjonalnie) Status zapisu/uczestnictwa

**Warunki:**
- Eksport dotyczy wybranego wydarzenia należącego do organizacji.

---

### 3.2 Eksport danych systemowych (administrator)
Administrator może eksportować:

#### 3.2.1 Użytkownicy
- Adres e-mail
- Rola
- Status konta
- Data rejestracji

#### 3.2.2 Organizacje
- Nazwa organizacji
- NIP
- Dane kontaktowe (e-mail, telefon)
- Status konta
- Data rejestracji

#### 3.2.3 Wydarzenia
- Tytuł
- Organizacja
- Data
- Lokalizacja
- Limit miejsc

#### 3.2.4 Zapisy
- Wydarzenie
- Uczestnik (imię, nazwisko, e-mail)
- Data zapisu
- (opcjonalnie) Status zapisu

#### 3.2.5 Darowizny (opcjonalnie)
- Data darowizny
- Kwota
- (opcjonalnie) Organizacja
- E-mail darczyńcy (jeśli wymagane)

---

## 4. Filtry eksportu
Eksport może uwzględniać podstawowe filtry:
- **Zakres dat (od–do)** – dla wydarzeń, zapisów i darowizn (jeśli dotyczy)
- **Organizacja** – dostępne dla Administratora
- **Wydarzenie** – w eksporcie listy uczestników (Organizacja)

> Jeśli filtry nie są planowane w MVP, można ograniczyć eksport do wybranego wydarzenia (organizacja) oraz pełnych list (administrator).

---

## 5. Przebieg eksportu (ogólny)
1. Użytkownik (organizacja lub administrator) wybiera sekcję eksportu.
2. System wyświetla dostępne typy eksportu (np. uczestnicy / wydarzenia / zapisy / użytkownicy).
3. Użytkownik wybiera dane do eksportu oraz (opcjonalnie) filtry.
4. Użytkownik klika „Eksportuj do CSV”.
5. System generuje plik CSV i udostępnia go do pobrania.

**Wynik:** Użytkownik pobiera plik CSV.

---

## 6. Wymagania dotyczące pliku CSV
- Plik zawiera nagłówki kolumn.
- Dane są spójne z zakresem eksportu oraz uprawnieniami roli.
- Kodowanie: UTF-8 (zalecane).
- Separator: przecinek lub średnik (do ustalenia w projekcie).

---

## 7. Komunikaty i błędy
- „Plik CSV został wygenerowany”
- „Brak danych do eksportu dla wybranych filtrów”
- „Nie masz uprawnień do eksportu tych danych”

---
