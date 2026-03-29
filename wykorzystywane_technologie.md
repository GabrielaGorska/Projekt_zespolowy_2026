# LSWIS – Technologie i narzędzia projektu (Tech Stack) w planowanym projekcie

Wersja: 1.0 | Data: 2026

---

## 1. Cel dokumentu
Celem dokumentu jest przedstawienie technologii, narzędzi oraz standardów wykorzystywanych w projekcie LSWIS.
Opis obejmuje zarówno warstwę aplikacji (frontend/backend), jak i środowisko uruchomieniowe, testowanie oraz proces wytwarzania.

---

## 2. Architektura
System LSWIS jest aplikacją webową składającą się z:
- **Frontend (SPA)** – interfejs użytkownika działający w przeglądarce.
- **Backend (API)** – logika biznesowa oraz obsługa operacji na danych.
- **Baza danych** – przechowywanie informacji o użytkownikach, wydarzeniach, zapisach itd.
- **Usługi wspierające** – wysyłka e-mail, (opcjonalnie) płatności/darowizny.

---

## 3. Backend
### 3.1 Framework
- **Node.js + NestJS**
  - modularna architektura (moduły, kontrolery, serwisy),
  - łatwa rozbudowa i utrzymanie,
  - dobre wsparcie dla dokumentacji API.

### 3.2 Baza danych i warstwa danych
- **PostgreSQL**
  - relacyjny model danych (wydarzenia, zapisy, konta).
- **ORM (np. TypeORM)**
  - mapowanie encji na tabele,
  - wygodne zarządzanie relacjami oraz migracjami.

### 3.3 Dokumentacja API
- **Swagger**
  - generowanie dokumentacji endpointów,
  - ułatwienie integracji frontend–backend.

### 3.4 Integracja e-mail
- **Zewnętrzny serwis pocztowy (SMTP/API)**
  - wysyłka e-maili systemowych (rejestracja, potwierdzenia, reset hasła).

### 3.5 (Opcjonalnie) Płatności / darowizny
- **Stripe**
  - płatności jednorazowe,
  - potwierdzenie darowizny w systemie.

---

## 4. Frontend
### 4.1 Framework
- **Angular**
  - SPA z routingiem i komponentami,
  - formularze i walidacje po stronie klienta,
  - modularność (feature modules).

### 4.2 UI/UX
- **Figma**
  - makiety ekranów i prototypy UI,
  - spójność wizualna i ergonomia.

---

## 5. Środowisko uruchomieniowe i DevOps
### 5.1 Konteneryzacja
- **Docker**
  - uruchamianie środowiska developerskiego w spójny sposób,
  - izolacja usług (frontend, backend, baza).

### 5.2 Automatyzacja CI
- **GitHub Actions**
  - automatyczne uruchamianie zadań po push/PR,
  - sprawdzanie jakości (lint/test/build),
  - budowanie artefaktów (np. build FE/BE) w pipeline.

---

## 6. Zarządzanie projektem i komunikacja
- **Jira** 
  - backlog, zadania, sprinty, priorytety.
- **GitHub**
  - repozytorium kodu, pull requesty, code review.
- **Discord**
  - komunikacja zespołu, spotkania statusowe.

---

## 7. Testowanie i jakość (zalecenia projektowe)
W projekcie zakłada się następujące podejście do jakości:
- testy jednostkowe dla kluczowych elementów logiki,
- testy integracyjne w zakresie przepływów backend–baza,
- testy funkcjonalne (manualne) dla scenariuszy MVP,
- podstawowe standardy kodowania i spójny format.

---

## 8. Standardy i konwencje pracy (propozycja)
Aby utrzymać spójność i czytelność kodu, zaleca się:
- praca na branchach funkcjonalnych (feature branches),
- pull requesty i code review,
- spójne nazewnictwo commitów i zadań,
- aktualizowanie dokumentacji wraz ze zmianami funkcjonalności.

---
