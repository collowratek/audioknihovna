# Kontrola před předáním

Co se předává: webová stránka (jeden soubor `index.html`), veřejné uložiště kódu
na GitHubu, nasazené na GitHub Pages.
Komu a kam: Fanda dostane možnost posílat návrhy změn (PR). Adresa knihovny je
veřejná, obsah archivu veřejný není, chrání ho přihlášení k Webshare.

Hlavní riziko, kvůli kterému se kontrola dělá: stránka drží v prohlížeči
přihlášení k Jiřího účtu na Webshare. Jediný řádek v cizím návrhu změn, který
pošle požadavek, obrázek nebo skript na cizí adresu, ho může odeslat ven. Komu
se přihlášení dostane do ruky, má plný přístup k účtu včetně mazání souborů,
protože Webshare nenabízí přístup jen pro čtení.

| Kontrola | Výsledek | Důkaz nebo důvod |
|---|---|---|
| Hesla a klíče v souborech | prošlo | V repu nejsou žádná hesla ani klíče. Přihlášení zadává uživatel v prohlížeči a zůstává jen tam. |
| Hesla a klíče v historii | prošlo | Prohledáno všech 61 objektů v gitu včetně nedosažitelných, vlastním hledáním (gitleaks na stroji není). Jediný nález je abeceda pro kódování hesla, konstanta algoritmu. |
| Osobní údaje | prošlo | Stránka nesbírá nic. Jména knih a časy poslechu leží na Jiřího Webshare, ne v repu. |
| Co je veřejné | zapsáno | Repo i adresa knihovny jsou veřejné, ověřeno dotazem na GitHub bez přihlášení. Obsah archivu veřejný není. |
| Pojistka proti odeslání ven (CSP) | prošlo | Viz níže. |
| Kontrola kvality kódu | 12 nálezů | Vlastní kontrola na nejvyšší úroveň přes celý soubor. Seznam níže. |
| Druhý názor od jiného modelu | 6 nálezů navíc | Codex (GPT-6), samostatný běh bez znalosti téhle práce. Seznam níže. |
| Druhý názor, druhé kolo | bez nálezu | Codex znovu, 18. 10., po opravách. Žádné tajemství, žádná cesta k účtu čtením repa ani otevřením stránky, opravy z prvního kola sedí. Jeho čtyři zbylá rizika jsou ta, co stojí níže. |
| Vestavěná bezpečnostní kontrola | 5 nálezů | 18. 10., celý soubor i historie gitu, nezávisle na předchozích koly. Tři opraveny, dva jsou rozhodnutí pro Jiřího. |
| Opravy nálezů | hotovo | Devět nálezů z prvních kol, tři z posledního. Zbytek je rozhodnutí pro Jiřího. |
| Zkouška celé cesty s přihlášením | čeká | Knihovna není přihlášená v žádném prohlížeči na notebooku, token je na telefonu. |

## Pojistka proti odeslání přihlášení jinam

Do stránky přidána pravidla Content Security Policy. Prohlížeč podle nich pustí
požadavky jen na `webshare.cz` a `*.wsup.cz`, obrázky a zvuk jen z `*.wsfiles.cz`
a z vlastní adresy, a nespustí žádný skript z cizí adresy.

Domény zjištěny z provozu, ne odhadem: odkaz na soubor vrací Webshare na
`free.7.dl.wsfiles.cz` (ověřeno voláním jeho veřejného API), rozhraní běží na
`webshare.cz`, nahrávání na `upload2.wsup.cz`.

Odzkoušeno v prohlížeči čtením hlášení o porušení pravidel (chybová hláška se od
běžné síťové chyby nepozná):

- požadavek, obrázek, zvuk i skript na cizí adresu: zablokováno,
- podobné jméno `wsfiles.cz.zly.example`: zablokováno,
- `free.7.dl.wsfiles.cz` jako obrázek i zvuk: propuštěno,
- volání Webshare z aplikace: propuštěno, server odpověděl.

Co pravidla neumí: odeslání dat přesměrováním celé stránky na cizí adresu
(`location.href`). Proti tomu chrání jedině čtení návrhů změn před sloučením.
Nefunguje z nich ani zákaz vkládání stránky do rámu, ten jde nastavit jen
hlavičkou serveru a GitHub Pages hlavičky nastavit neumí.

## Co kontrola našla

Vlastní kontrola prošla celý soubor na nejvyšší úroveň a našla 12 věcí, Codex
jako nezávislý druhý model šest dalších. Ty podstatné:

**Opraveno:**

1. **Pravidla platila až od poloviny hlavičky.** Meta značka s pravidly byla až
   čtvrtá v pořadí. Skript vložený nad ni by se spustil dřív, než pravidla
   začnou platit, a jejich text by přitom zůstal netknutý, takže by změna
   vypadala neškodně. Značka je teď hned za kódováním znaků a komentář to říká.
2. **Pravidla pouštěla skripty z vlastní adresy.** `script-src 'self'` dovoloval
   načíst skript odkudkoli z `collowratek.github.io`, tedy i z jiného projektu.
   Odstraněno, zbyl jen program ve stránce.
3. **Obsluha události zapsaná v HTML se mohla spustit.** Přidáno
   `script-src-attr 'none'`, takže `onclick` a `onerror` v HTML jsou mrtvé;
   program je přiřazuje v kódu, takže se nic nerozbilo. Ověřeno zkouškou.
4. **Chyběl zákaz vlastních vláken.** Bez `worker-src` by spadl na `script-src`.
   Doplněno `worker-src 'none'`.
5. **Pravidla byla širší, než je potřeba:** celá doména `wsup.cz` zúžena na
   `upload2.wsup.cz`, u zvuku zrušeno `blob:` a vlastní adresa.
6. **Adresa obálky šla do stránky neošetřená** (dvě místa). Teď prochází stejnou
   funkcí jako všechno ostatní.
7. **Čísla z paměti prohlížeče se nekontrolovala.** Stopa a čas se teď převádějí
   na čísla, aby se nedostaly do stránky jako text.
8. **Rozbitý odkaz s `#t=`** mohl nechat přihlášení viset v adresním řádku.
   Ošetřeno.
9. **Chybějící soubory repozitáře** `.gitignore`, `CHANGELOG.md`, `CLAUDE.md`
   a zastaralé `README.md`, které popisovalo přihlášení, jaké aplikace už nemá.

**Zůstává, protože to pravidla neumí a hlídá to jedině čtení změn:**

- Odeslání přihlášení **přesměrováním stránky** (`location.href` na cizí adresu).
  Pravidla řeší požadavky, ne odchod z adresy.
- **Zneužití samotného Webshare.** Povolený cíl je povolený cíl: změna může
  nahrát přihlášení jako soubor na cizí účet Webshare, nebo rovnou smazat archiv
  přes volání, které už v programu je. K tomu není potřeba žádná cizí adresa.
- **Předání oknu, které stránku otevřelo** (`postMessage`).

## Poslední kolo, 18. 10. 2026

Proběhly dvě kontroly, které v předchozím kole chyběly: Codex podruhé (po
opravách, znovu bez znalosti téhle práce) a vestavěná bezpečnostní kontrola
přes celý soubor i historii gitu.

Codex podruhé nenašel nic nového. Potvrdil, že v souboru není žádné tajemství,
že čtením repozitáře ani otevřením stránky se nikdo k účtu nedostane a že
opravy z prvního kola jsou na místě a nic nerozbily.

Vestavěná kontrola našla pět věcí. Tři jsou opravené a vyzkoušené v prohlížeči:

1. **Klíč z adresy se bral bez ptaní.** Obsluha `#t=` uložila cokoli, co
   v odkazu přišlo, přepsala tím uložený klíč a hned uklidila adresní řádek.
   Kdo Jiřímu podstrčí odkaz `…/audioknihovna/#t=<svůj klíč>`, ten mu vymění
   přihlášení za své a od té chvíle mu každá minuta poslechu zapisuje pozici
   do CIZÍHO účtu na Webshare. Odkaz přitom vede na jeho vlastní známou adresu.
   Teď se knihovna zeptá a napíše, že nějaký klíč už uložený je.
2. **Pravidla pouštěla jakýkoli program napsaný přímo ve stránce**
   (`script-src 'unsafe-inline'`). Proti cizímu souboru se skriptem to platilo,
   proti řádku přidanému do stránky v pull requestu ne. Místo toho je tam teď
   OTISK (sha256) toho jednoho programu, který ve stránce je. Kdo v něm změní
   jediný znak a nepřepíše otisk, tomu se stránka vůbec nespustí. Změna programu
   je tím pádem vidět i v pravidlech a nemůže proklouznout jako úprava vzhledu.
   Přepočet dělá `otisk.py`, pravidlo je v `CONTRIBUTING.md`.
3. **Stránku šlo vložit do cizího rámu.** Zakázat to hlavičkou nejde (GitHub
   Pages hlavičky neumí) a v meta značce prohlížeče `frame-ancestors` ignorují.
   Program se teď v rámu sám zastaví. Rám byl nosič pro bod 1 i pro klamné
   kliknutí na tlačítka přehrávače.

K tomu dvě drobnosti: `esc` ošetřuje i apostrof (dnes jsou všechny atributy
v dvojitých uvozovkách, takže to nic neřešilo, ale byla to past na prvního
přispěvatele) a z pravidel vypadla dvě mrtvá oprávnění (`style-src 'self'`,
`media-src data:`). Adresa `data:` u obrázků zůstává, drží ikonu na ploše.

Jedno tvrzení kontroly neplatí a opravuji ho tady, ať se nevrací: že
`script-src-attr` neumí Safari. Umí ho od prosince 2022, takže ta direktiva
funguje i na telefonu. Otisk ji stejně dělá nadbytečnou, zůstává jako pojistka.

Vyzkoušeno v prohlížeči na místním serveru: stránka se s otiskem spustí a
přihlašovací obrazovka i tlačítka fungují (kdyby otisk neseděl, nenaběhlo by
vůbec nic), odkaz s `#t=` ukáže potvrzení a do paměti nic nezapíše, dokud
člověk nepotvrdí, zahození vrátí přihlašovací obrazovku, potvrzení klíč uloží,
a knihovna vložená do rámu na cizím webu se nespustí a napíše proč. Žádné
hlášení o porušení pravidel v konzoli.

**Rozhodnutí pro Jiřího, sám jsem je neudělal:**

- **Sdílená adresa.** Přihlášení v prohlížeči patří celé adrese
  `collowratek.github.io`, ne jen téhle složce. Každá další stránka vydaná pod
  stejným účtem na GitHubu ho přečte a pravidla téhle knihovny pro ni neplatí.
  Odděluje se to jedině vlastní doménou.
- **Odpojit nezneplatní přihlášení na serveru.** Dá se doplnit volání odhlášení,
  ale tím by se odhlásila i ostatní zařízení, protože přihlášení je jedno
  společné. Proto to nechávám na rozhodnutí.
- **Účet Webshare jen pro archiv.** Nejúčinnější omezení škody: kdyby se
  přihlášení dostalo ven, týká se jen audioknih.
- **Heslo projde programem v čitelné podobě**, než se zašifruje. Kdo může měnit
  program, může ho odchytit. Platí pro každého, kdo smí nasazovat.
- **Tenhle soubor a `PREDANI.md` jsou veřejné.** Je v nich přesný seznam toho,
  co pravidla neuhlídají, vedle pozvánky „posílejte pull requesty". Dá se to
  vyjmout z repozitáře (`.gitignore`) nebo přesunout do soukromého. Pozor na
  dvě věci: z historie gitu to tím nezmizí a stejný seznam je i v komentáři
  nad pravidly přímo v `index.html`, takže půlka opatření nestačí. Můj názor:
  spíš nechat, poctivý popis je pro přispěvatele užitečnější, než je ta
  úspora pro útočníka. Ale je to rozhodnutí, ne samozřejmost.

Verdikt kontrolora (Codex, GPT-6, viděl kód poprvé a nevěděl o téhle práci):
pravidla jsou užitečná vrstva navíc a zkoušky prokázaly, že blokují cizí cíle,
ale neudrží škodlivou změnu, která projde do nasazení. Kdo sem může nasadit
program, má plnou moc nad Jiřího účtem na Webshare. Doporučuje: změny přijímat
jako návrhy z forku, sloučení vždy po přečtení vlastníkem, a aplikaci s
přihlášením dát vlastní doménu.

Souhlasím a proto návrh nastavení GitHubu níže počítá s forkem, ne se
spoluautorstvím.
