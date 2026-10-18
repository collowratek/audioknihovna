# Audioknihovna

Přehrávač soukromého archivu audioknih uloženého na [Webshare.cz](https://webshare.cz).
Jedna statická stránka, žádné závislosti, žádný server.

Běží na <https://collowratek.github.io/audioknihovna/>.

## Použití

Otevři stránku a přihlas se jménem a heslem k Webshare. Přihlášení se ukládá
jen do prohlížeče a posílá se výhradně na Webshare. Na druhé zařízení se dá
přenést odkazem s `#t=`, aby se heslo nemuselo psát na telefonu.

Očekává strukturu `/audioknihy/<Autor - Název>/<stopy>` v soukromých souborech.
Když je ve složce knihy `cover.jpg`, použije se jako obálka.

## Funkce

- knihovna s obálkami, nové knihy nahoře, zbytek podle autora
- zapamatování místa v každé knize, přenos mezi zařízeními přes Webshare
- kód posluchače: nepovinné slovo, kterým se oddělí rozposlouchaný čas více lidí
  na jednom archivu
- časovač spánku; jeho zapnutí zároveň označí místo, kam se tlačítkem „zpět na“
  kdykoli vrátíš, i ráno a i na jiném zařízení
- automatický přechod na další stopu, převíjení po 10 až 90 s, rychlost 0,75 až 2×
- ovládání uzpůsobené telefonu, tlačítka dosažitelná i ve sbaleném přehrávači

## Upozornění

Přihlášení k Webshare opravňuje k plnému přístupu k účtu včetně mazání souborů,
protože Webshare nenabízí přístup jen pro čtení. Komu ho dáš, ten má stejná
práva jako ty. Totéž platí o odkazu s `#t=`.

Stránka proto nese pravidla `Content-Security-Policy`, podle kterých prohlížeč
pustí požadavky jen na Webshare a nespustí žádný cizí skript. Co pravidla
nepokrývají a jak se posílají změny, je v [CONTRIBUTING.md](CONTRIBUTING.md).

## Soubory

| Soubor | Co v něm je |
|---|---|
| `index.html` | celá aplikace: vzhled, přihlášení, přehrávač, synchronizace |
| `img/` | volné fotky použité jako náhradní obálky |
| `PRD.md`, `PLAN.md` | zadání a postup poslední větší změny |
| `KONTROLA.md` | záznam bezpečnostní kontroly před předáním |
