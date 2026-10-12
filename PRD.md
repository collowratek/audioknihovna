# Zadání: kód posluchače a pin

Stav: ke schválení. Napsáno 10. 10. 2026, přepsáno po nezávislé kontrole.

## Problém

Knihovna si pamatuje, kde jsi v každé knize skončil, a přenáší to mezi telefonem
a počítačem. Tahle paměť je ale společná pro každého, kdo má stejný přístup
k archivu. Když Jiří půjčí přístup dalšímu člověku, posouvají si rozposlouchaný
čas navzájem: on si pustí Hyperion dopoledne, druhý večer, a oba přicházejí
o místo, kde byli.

Druhá věc je poslech před spaním. Jiří usne po pár minutách, přehrávač mezitím
běží dál a ráno je kniha o půl hodiny jinde, než kde ji naposledy vnímal.
Vracet se po slepu převíjením je otrava.

## Řešení

**Kód posluchače.** Nepovinné slovo, které si každý jednou zadá a které se
připojí k ukládanému místu. Každý tak má svůj rozposlouchaný čas, aniž by
potřeboval vlastní účet nebo přihlášení. Kdo kód nezadá, chová se knihovna
přesně jako dnes.

**Pin.** Tlačítko, kterým si posluchač před usnutím označí, kde právě je.
Druhým tlačítkem se tam kdykoli vrátí, i ráno a i na jiném zařízení. Pin
zůstává, dokud ho posluchač nepřepíše, a běžný posun v knize ho nemaže.

## Co to má umět

1. Jako posluchač chci zadat svůj kód, abych měl rozposlouchaný čas jen pro sebe,
   i když přístup k archivu sdílím s dalšími lidmi.
2. Jako posluchač chci kód zadat při připojení i kdykoli později přímo
   z knihovny, protože na telefon se přístup předává odkazem, který přihlašovací
   obrazovku přeskočí.
3. Jako posluchač, který kód nezadá, chci, aby se nic nezměnilo, protože mi
   dnešní chování vyhovuje.
4. Jako posluchač, který kód zadá poprvé, chci navázat tam, kde knihovna skončila
   doteď, abych nezačínal od začátku knihy.
5. Jako posluchač chci jedním stiskem uložit pin na místo, kde právě poslouchám,
   abych se tam ráno vrátil.
6. Jako posluchač chci jedním stiskem skočit na pin, aniž bych hledal čas
   převíjením.
7. Jako posluchač chci, aby pin přežil zavření stránky i přechod na jiné zařízení.
8. Jako posluchač chci, aby mi pin nepřepsalo běžné přehrávání, protože po jeho
   uložení zpravidla ještě chvíli poslouchám.
9. Jako posluchač chci pin ovládat jednou rukou v posteli a po tmě: krátkým
   ťuknutím, bez přidržení, bez potvrzovacího dotazu, i když mám přehrávač
   sbalený.
10. Jako posluchač bez kódu chci pin taky, protože kód je nepovinný a pin je
    užitečnější než rozdělení posluchačů.
11. Jako posluchač chci, aby se mezi zařízeními přenášela i nastavená délka
    přeskoku, abych ji nemusel nastavovat na každém zařízení zvlášť.

## Jak poznáme hotovo

- Dva různé kódy na stejném archivu mají každý svůj rozposlouchaný čas a žádný
  z nich nepřepíše ani nesmaže ten druhý.
- Bez zadaného kódu se knihovna chová stejně jako před změnou, dosavadní uložená
  místa zůstávají čitelná a žádné se nesmaže.
- Posluchač, který si kód zadá poprvé, pokračuje tam, kde kniha byla.
- Pin funguje i bez zadaného kódu.
- Pin uložený v jednom prohlížeči je po zavření a otevření stránky pořád tam.
- Pin uložený v jednom prohlížeči se objeví i ve druhém, pod stejným kódem.
- Pin uložený pod jedním kódem není vidět pod jiným kódem.
- Po uložení pinu a dalších pěti minutách poslechu je pin na původním místě.
- Piny ve dvou různých knihách existují vedle sebe a nepletou se.
- Skok na pin uloží jako místo v knize čas pinu, nikdy ne nulu. (Posluchač
  od pinu poslouchá dál, takže se místo posunout má; hlídá se jen to, aby
  skok nepřepsal rozposlouchané místo nulou.)
- Tlačítka pinu jsou vidět i ve sbaleném přehrávači a jsou vysoká aspoň 44 bodů.
- Při šířce displeje 375 bodů leží obě tlačítka celá uvnitř obrazovky, měřeno
  jejich skutečnou polohou, ne okem.
- Nastavená délka přeskoku se objeví i na druhém zařízení pod stejným kódem.

## Co v první verzi nebude

- Žádné ověřování kódu, žádná hesla, žádná ochrana proti tomu, aby si dva lidé
  zvolili stejný kód. Když se trefí do stejného, sdílejí pozice, což je přesně
  dnešní stav, takže se nic nezhorší. Takhle to navrhl Fanda a souhlasíme.
- Žádný seznam posluchačů ani přepínání mezi nimi na jedno kliknutí.
- Jen jeden pin na knihu a posluchače, ne víc záložek.
- Pin není vidět v seznamu knih, jen v přehrávači.
- Žádná fronta na zápisy, které se nepovedly kvůli výpadku sítě. Pin se v takovém
  případě uloží do prohlížeče a knihovna o tom dá vědět, odeslání se zkusí při
  dalším zápisu.

## Rozhodnutí, na kterých to stojí

**Kód se do názvu souboru nedává v čitelné podobě, ale jako jeho otisk.**
Místo v knize se totiž nepřenáší obsahem souboru, ale jeho názvem, a čitelný kód
by do názvu zavlekl mezery, diakritiku, emoji, uvozovky nebo délku, která se
nikam nevejde. Otisk je vždy šest znaků z rozsahu 0 až 9 a a až f. Posluchač
tedy může napsat do pole cokoli a nic se nerozbije.

**Nový tvar názvu má pevný počet polí a jiný začátek než dnešní.** Dnešní
záznamy začínají `poz_`, nové začínají jinak a nesou navíc kód a typ záznamu
(místo, nebo pin). Díky tomu jde přesně zacílit, co se při úklidu smí smazat,
a dnešní záznamy zůstanou nedotčené.

**Dnešní záznamy se už nikdy nebudou mazat ani přepisovat, jen číst.** Je jich
pár desítek, místo neubírají a jsou to jediné místo, kde dnes rozposlouchaný čas
žije. Kdo nemá vlastní záznam, čte z nich.

**Prázdný kód je plnohodnotný kód.** Uvnitř se chová jako posluchač jménem
„společný“, takže i bez kódu vzniká záznam v novém tvaru a pin funguje.

## Ověřeno v kódu

Přečetl jsem, jak synchronizace funguje dnes, protože na tom plán stojí:

- Místo se nepřenáší obsahem souboru, ale jeho názvem. Prohlížeč neumí obsah
  cizího souboru přečíst, výpis složky ano, proto to autor udělal takhle.
- Po každém zápisu se dnes mažou všechny starší soubory téže knihy. S kódy a piny
  by to mazalo cizí záznamy. Tohle je největší riziko celé změny.
- Záznam z prohlížeče se ukládá jako jeden celek, takže pin uložený do stejného
  celku by zmizel při každém dalším uložení místa, a to se děje každých pět
  sekund poslechu. Pin musí být oddělený.
- Návrat na jinou stopu dnes vždy znovu žádá o odkaz na soubor a po spuštění
  uloží aktuální čas. Použít tu samou cestu pro skok na pin by znamenalo uložit
  nulu a přepsat tím rozposlouchané místo na všech zařízeních.
- Sbalený přehrávač skrývá celou druhou řadu ovládání. Právě ten stav je noční.
- Čerstvě nahraný soubor drží Webshare asi čtvrt hodiny ve stavu dokončování.
  Na čtení názvu ze seznamu to nevadí, ověřeno při nahrávání knih 26. 9. a 4. 10.

## Ověřeno zkouškou 10. 10. 2026

Jestli Webshare přijme a ve výpisu vrátí název v novém tvaru. Na tom stojí celý
návrh, takže se to vyzkoušelo dřív, než se napsal řádek kódu. Nahrály se tři
zkušební názvy (48, 48 a 51 znaků, běžné místo, pin a hraniční čísla) a pak se
zase smazaly.

- Všechny tři server přijal a ve výpisu vrátil **znak po znaku stejné**, nic
  nepřepsal ani nezkrátil.
- Z druhého zařízení, tedy při dotazu pod jiným označením zařízení, byly vidět
  **za 17 sekund** od nahrání. Pro ranní návrat k pinu to nevadí, ale zkoušky
  přenosu mezi zařízeními na to musí počkat, jinak budou vypadat jako chyba.
- Malé textové záznamy jsou ve výpisu rovnou použitelné, nečeká se na ně čtvrt
  hodiny jako u nahraných knih.
- Úklid podle začátku názvu se trefil přesně do zkušebních souborů a všech
  40 dosavadních záznamů zůstalo nedotčených. Postup mazání, který použije
  hotová verze, je tím vyzkoušený nanečisto.

## Ověřeno na nasazené verzi 12. 10. 2026

Všech 33 kritérií prošlo přímo na adrese knihovny, podrobně v [PLAN.md](PLAN.md).
Zkouška odhalila, že prohlížeč občas zahodí skok na čas a přehrávání začne od
nuly, což by uložená místa přepsalo nulou; ukládání proto o cíli skoku ví
a nulu místo něj neuloží. Nepotvrzená zůstává jediná věc: že tři rozposlouchané
knihy ukazují na skutečném archivu svoje časy. Knihovna není přihlášená v žádném
prohlížeči na notebooku, takže to musí potvrdit Jiří na telefonu.

## Známé slabiny, které touhle změnou neřešíme

Patří sem, aby se na ně nezapomnělo, ale rozsah téhle práce to není:

- O tom, čí záznam vyhraje, rozhodují hodiny zapisujícího zařízení. Zařízení
  s hodinami napřed vyhraje vždy.
- Ťuknutí do seznamu stop přepíše uložené místo bez varování.
- Adresa nahrávacího serveru je v kódu natvrdo a úspěch se pozná podle řetězce
  v odpovědi, ne podle stavu.
- Záznamy ve složce přibývají a nikdy se hromadně neuklízejí.
