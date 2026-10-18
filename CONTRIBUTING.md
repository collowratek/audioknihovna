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

## Po každé změně programu přepočítej otisk

Pravidla v hlavičce nepouštějí libovolný program ve stránce, ale jen ten, jehož
otisk (sha256) je v nich zapsaný. Kdo změní uvnitř značky `script` jediný znak
a otisk nechá být, tomu se stránka v prohlížeči vůbec nespustí. Je to schválně:
změna programu je pak vidět i v pravidlech a neprojde jako úprava vzhledu.

```bash
python3 otisk.py --zapis   # přepočítá a zapíše
python3 otisk.py           # jen zkontroluje, 0 = sedí
```

Změnu otisku nech v pull requestu jako samostatnou věc, ať je na ní vidět, že
patří k té tvé změně programu.

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
- Klíč z adresy (`#t=`) se smí uložit jen po potvrzení na obrazovce. Je to
  pohodlný přenos na telefon, ale touž cestou jde podstrčit cizí klíč, takže
  se tu nesmí nic zautomatizovat.
- Stránka se v cizím rámu nespouští, tahle pojistka na začátku programu musí
  zůstat první věcí, která se provede.
- Zvukové soubory a obálky z archivu do repozitáře nepatří. V `img/` leží jen
  volné fotky použité jako náhradní obálky.

## Co se kontroluje před sloučením

Každý pull request projde kontrolou, která se dívá hlavně na nové adresy, nové
skripty, práci s přihlášením a na vkládání do HTML. Sloučení dělá vlastník
repozitáře.
