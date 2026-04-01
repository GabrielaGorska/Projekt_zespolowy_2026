# LSWIS – Specyfikacja funkcjonalna: Moduł wydarzeń społecznych 

Wersja: 1.0 | Data: 2026

---

## 1. Cel modułu
Moduł wydarzeń społecznych umożliwia organizacjom tworzenie i publikowanie wydarzeń oraz obsługę zapisów wolontariuszy.
Zapewnia także przeglądanie wydarzeń, filtrowanie, kontrolę limitu miejsc, anulowanie zapisów i wgląd organizatora w listę uczestników.

---

## 2. Tworzenie wydarzenia (organizacja)
### 2.1 Opis
Organizacja może utworzyć wydarzenie społeczne poprzez formularz dostępny w panelu organizacji.

### 2.2 Dane wejściowe (formularz)
Wydarzenie zawiera co najmniej:
- Tytuł
- Opis
- Lokalizacja (tekstowa)
- Data rozpoczęcia
- Data zakończenia (opcjonalnie)
- Limit miejsc
- Kategoria wydarzenia (opcjonalnie)
- Zdjęcie / grafika (opcjonalnie)
- Geolokalizacja (opcjonalnie)

### 2.3 Reguły walidacji
- Tytuł, opis, data i lokalizacja są wymagane.
- Limit miejsc musi być większy od 0.
- Data wydarzenia nie może być wcześniejsza niż bieżąca data.
- Jeśli podano datę zakończenia, nie może być wcześniejsza niż data rozpoczęcia.

### 2.4 Wynik
- Po zapisaniu system tworzy wydarzenie i wyświetla jego szczegóły.
- Wydarzenie może być widoczne na liście wydarzeń (zgodnie z założeniami publikacji/aktywności).

### 2.5 Komunikaty i błędy
- „Wydarzenie zostało utworzone”
- „Nie można utworzyć wydarzenia – popraw dane w formularzu”

---

## 3. Edycja i zamykanie wydarzenia (organizacja)
### 3.1 Opis
Organizacja może modyfikować dane wydarzenia oraz zakończyć (zamknąć) rekrutację lub oznaczyć wydarzenie jako zakończone/odwołane (zgodnie z przyjętymi zasadami).

### 3.2 Reguły
- Edycja jest możliwa dla wydarzeń, które nie zostały zakończone.
- Zamykanie wydarzenia blokuje możliwość nowych zapisów.
- Odwołanie wydarzenia powinno skutkować poinformowaniem zapisanych wolontariuszy (jeśli moduł powiadomień obejmuje takie zdarzenia).

---

## 4. Przeglądanie listy wydarzeń (wolontariusz / użytkownik)
### 4.1 Opis
System udostępnia listę aktywnych wydarzeń wraz z podstawowymi informacjami.

### 4.2 Informacje na liście wydarzeń
- Nazwa wydarzenia
- Data
- Miejsce
- Nazwa organizacji
- Informacja o dostępności miejsc (np. liczba wolnych miejsc)

### 4.3 Filtry i paginacja
System umożliwia filtrowanie wydarzeń według:
- zakresu dat (od–do),
- kategorii/typu wydarzenia,
- lokalizacji,
- organizacji,
- statusu (np. aktywne/zakończone – zależnie od założeń).

**Paginacja** jest obowiązkowa dla list.

### 4.4 Szczegóły wydarzenia
Po wybraniu wydarzenia z listy system wyświetla:
- pełny opis,
- daty i lokalizację,
- dostępność miejsc,
- (opcjonalnie) mapę, jeśli dostępne dane geolokalizacyjne,
- przycisk „Zapisz się” (dla zalogowanego wolontariusza).

---

## 5. Zapis wolontariusza na wydarzenie
### 5.1 Opis
Wolontariusz może zapisać się na wydarzenie, jeśli są dostępne miejsca i wydarzenie jest aktywne.

### 5.2 Reguły
- System nie pozwala na zapis, jeśli wydarzenie osiągnęło limit miejsc.
- System nie pozwala na ponowny zapis tego samego wolontariusza na to samo wydarzenie.
- Po zapisie system wysyła potwierdzenie e-mail oraz może powiadomić organizatora o nowym uczestniku.

### 5.3 Wynik
- Wolontariusz jest dopisany do listy uczestników wydarzenia.
- System wyświetla komunikat potwierdzający zapis.

### 5.4 Komunikaty i błędy
- „Zapisano na wydarzenie”
- „Brak wolnych miejsc – zapisy zostały zamknięte”
- „Jesteś już zapisany na to wydarzenie”

---

## 6. Anulowanie zapisu
### 6.1 Opis
Wolontariusz może anulować swój zapis na wydarzenie zgodnie z zasadami anulacji.

### 6.2 Reguły
- Anulowanie jest możliwe do określonego terminu (jeśli termin anulacji jest przewidziany).
- Po anulowaniu system aktualizuje dostępność miejsc.
- System wysyła potwierdzenie anulacji e-mail oraz może powiadomić organizatora.

### 6.3 Wynik
- Wolontariusz nie jest już zapisany na wydarzenie (lub zapis jest oznaczony jako anulowany).
- System wyświetla komunikat potwierdzający anulowanie.

### 6.4 Komunikaty i błędy
- „Anulowano udział w wydarzeniu”
- „Nie można anulować udziału po wskazanym terminie” (jeśli dotyczy)

---

## 7. Lista uczestników (organizacja)
### 7.1 Opis
Organizacja ma dostęp do listy uczestników przypisanych do własnych wydarzeń.

### 7.2 Zakres danych na liście
- Imię i nazwisko
- Adres e-mail
- Data zapisu
- Status uczestnictwa (jeśli przewidziano, np. zapisany/anulowany/obecny)

### 7.3 Filtrowanie
Organizacja może filtrować listę uczestników według statusu (jeśli statusy są używane).

---

## 8. Eksport listy uczestników do CSV (organizacja)
### 8.1 Opis
Organizacja może wyeksportować listę uczestników wydarzenia do pliku CSV.

### 8.2 Reguły
- Eksport obejmuje uczestników danego wydarzenia.
- System generuje plik CSV i udostępnia go do pobrania.

### 8.3 Wynik
Organizacja pobiera plik CSV z listą uczestników.

---

## 9. Check-in (potwierdzanie obecności) – opcjonalnie
### 9.1 Opis
Jeśli funkcja check-in jest w zakresie, system umożliwia potwierdzenie obecności wolontariuszy na wydarzeniu.

### 9.2 Możliwe warianty
- wolontariusz potwierdza obecność poprzez link/akcję udostępnioną przez organizatora,
- organizator może ręcznie oznaczyć obecność wolontariusza.

### 9.3 Wynik
System odnotowuje obecność, co może wpływać na historię wydarzeń oraz możliwość generowania zaświadczeń.

---
