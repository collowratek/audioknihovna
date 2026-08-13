# Audioknihovna

Přehrávač soukromého archivu audioknih uloženého na [Webshare.cz](https://webshare.cz).
Jedna statická stránka, žádné závislosti, žádný server.

## Použití

Otevři stránku a vlož přihlašovací token (`wst`) svého Webshare účtu.
Token se ukládá výhradně do `localStorage` prohlížeče a nikam se neodesílá —
veškerá komunikace jde přímo z tvého prohlížeče na `webshare.cz`.

Očekává strukturu `/audioknihy/<Autor - Název>/<stopy>` v soukromých souborech.
Pokud je ve složce knihy `cover.jpg`, použije se jako obálka.

## Funkce

- knihovna s obálkami, řazení podle autora
- automatický přechod na další stopu
- zapamatování pozice zvlášť pro každou knihu
- převíjení po 30 s, rychlost přehrávání 0,75–2×
- ovládání uzpůsobené telefonu

## Upozornění

Token opravňuje k plnému přístupu k účtu včetně mazání souborů — Webshare
nenabízí přístup jen pro čtení. Komu token dáš, ten má stejná práva jako ty.
