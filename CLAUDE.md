# CLAUDE.md — Audioknihovna

Dědí z `~/.claude/CLAUDE.md`. Tady jen to, co platí navíc pro tenhle projekt.

## Co to je

Jedna statická stránka `index.html` na GitHub Pages, která přehrává soukromý
archiv audioknih z Webshare. Žádný server, žádný překlad, žádné knihovny.
Co je v souboru, to je za pár minut na webu.

## Tvrdá pravidla

1. **Žádná nová adresa bez úpravy pravidel.** Stránka drží v prohlížeči
   přihlášení k Webshare s plnými právy k účtu. Seznam povolených adres je
   v meta značce `Content-Security-Policy` na začátku souboru. Nad tu značku
   nesmí přibýt nic, co se spouští, protože pravidla platí až od ní dolů.
2. **Žádná knihovna z internetu.** Všechno je v tom jednom souboru.
3. **Hodnoty z Webshare a od uživatele jdou do HTML jen přes `esc`.**
4. **Audio a obálky z archivu do repozitáře nepatří.** V `img/` leží jen volné
   fotky použité jako náhradní obálky.
5. **Commit a push jen s Jiřího výslovným souhlasem.** Push je nasazení.

## Zvyklosti

Commit zprávy česky, celou větou, bez předpony typu. První řádek co, odstavec
pod ním proč. Komentáře v kódu česky, vysvětlují proč, ne co.

Nové knihy se píšou na **začátek** seznamu `PRVNI`, ne na konec.

## Jak se to zkouší

Lokálně `python3 -m http.server` a přihlášení svým účtem. Logiku bez Webshare
jde zkoušet tak, že se v prohlížeči přepíše `window.fetch` předstíraným
serverem; zvuk pak jde z adresy `data:`, kterou pravidla schválně pouštějí.
Mobil se ověřuje změřením skutečné polohy tlačítek při šířce 375 bodů, ne okem:
stránka má zakázané vodorovné posouvání, takže přetečení není vidět.

## Předávání

Změny od druhých lidí chodí jako pull request z forku, slučuje je Jiří.
Pravidla pro přispěvatele jsou v `CONTRIBUTING.md`, záznam o bezpečnostní
kontrole v `KONTROLA.md`.
