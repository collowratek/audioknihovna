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
| Opravy nálezů | hotovo | Devět nálezů opraveno, zbytek je rozhodnutí pro Jiřího. |
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

Verdikt kontrolora (Codex, GPT-6, viděl kód poprvé a nevěděl o téhle práci):
pravidla jsou užitečná vrstva navíc a zkoušky prokázaly, že blokují cizí cíle,
ale neudrží škodlivou změnu, která projde do nasazení. Kdo sem může nasadit
program, má plnou moc nad Jiřího účtem na Webshare. Doporučuje: změny přijímat
jako návrhy z forku, sloučení vždy po přečtení vlastníkem, a aplikaci s
přihlášením dát vlastní doménu.

Souhlasím a proto návrh nastavení GitHubu níže počítá s forkem, ne se
spoluautorstvím.
