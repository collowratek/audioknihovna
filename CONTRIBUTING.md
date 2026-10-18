# Jak přispívat

Knihovna je jediný soubor `index.html`. Žádný překlad, žádné knihovny, žádný
server. Co je v souboru, to je na webu.

## Spuštění u sebe

```bash
git clone https://github.com/collowratek/audioknihovna.git
cd audioknihovna
python3 -m http.server 8000
```

Otevři `http://localhost:8000/` a přihlas se svým účtem na Webshare. Soubor
neotvírej dvojklikem z disku, adresa `file://` část pravidel vypne a chování
pak neodpovídá webu.

Knihovna čeká strukturu `/audioknihy/<Autor - Název>/<stopy>` v soukromých
souborech na Webshare. Když tam `cover.jpg` je, použije se jako obálka.

## Jak poslat změnu

```bash
git switch -c nazev-zmeny
git commit -am "Krátký popis změny"
git push origin nazev-zmeny
```

Pak na GitHubu otevři pull request. Commit zprávy jsou česky, celou větou, bez
předpony typu `feat:`. První řádek říká, co se mění, odstavec pod ním proč.

## Co se nesmí

Stránka drží v prohlížeči přihlášení k Webshare a to přihlášení otevírá celý
účet včetně mazání souborů. Proto:

- Žádná nová adresa, na kterou stránka něco posílá nebo odkud něco načítá.
  Povolené adresy jsou vyjmenované v pravidlech `Content-Security-Policy`
  v hlavičce souboru. Změna toho seznamu patří do samostatného pull requestu
  s vysvětlením, proč je nutná.
- Žádná knihovna z internetu, žádný `<script src=...>`, žádné písmo nebo styl
  z cizí adresy. Všechno je v tom jednom souboru.
- Přihlášení (`wst`) se nikam neposílá, nikam nevypisuje a nikam nekopíruje.
  Nepatří do adresy odkazu, do názvu souboru ani do hlášky.
- Hodnoty, které přijdou z Webshare nebo od uživatele, se do HTML vkládají jen
  přes funkci `esc`.
- Zvukové soubory a obálky z archivu do repozitáře nepatří. V `img/` leží jen
  volné fotky použité jako náhradní obálky.

## Co se kontroluje před sloučením

Každý pull request projde kontrolou, která se dívá hlavně na nové adresy, nové
skripty, práci s přihlášením a na vkládání do HTML. Sloučení dělá vlastník
repozitáře.
