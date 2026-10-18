# Historie změn

Nejnovější nahoře. Podrobnosti jsou v popisech jednotlivých uložených verzí.

## 18. 10. 2026

- Pravidla `Content-Security-Policy` nově nesou otisk programu ve stránce.
  Cizí řádek přidaný do programu se bez přepsání otisku nespustí. Přepočet
  dělá `otisk.py`.
- Klíč předaný v adrese (`#t=`) se uloží až po potvrzení na obrazovce. Dřív
  se uložil sám, takže šlo odkazem podstrčit cizí přihlášení.
- V cizím rámu se knihovna nespustí.
- `esc` ošetřuje i apostrof.
- Z pravidel vypuštěna mrtvá oprávnění (`style-src 'self'`, `media-src data:`).

## 16. 10. 2026

- Pravidla `Content-Security-Policy` proti odeslání přihlášení na cizí adresu.
- Adresa obálky se do stránky vkládá ošetřená, čísla načtená z paměti
  prohlížeče se převádějí na čísla.
- Rozbitý odkaz s `#t=` už nenechá přihlášení viset v adresním řádku.
- Pokyny pro přispěvatele, záznam o kontrole, seznam ignorovaných souborů.

## 12. 10. 2026

- Kód posluchače: více lidí na jednom archivu si přestane posouvat
  rozposlouchaný čas.
- Zapnutí časovače spánku označí místo, kam se lze jedním ťuknutím vrátit.
  Ruční tlačítko na označení místa zrušeno, časovač přesunut nahoru, kde je
  vidět i ve sbaleném přehrávači.
- Pojistka proti uložení nuly, když prohlížeč zahodí skok na čas.
- Mezi zařízeními se přenáší i nastavená délka přeskoku.

## Dřívější

Obálky knih, nové knihy na začátku knihovny, rychlejší načítání, zrušený
offline poslech, přehrávač pro telefon.
