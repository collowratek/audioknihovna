# Plán: kód posluchače a pin

K zadání v [PRD.md](PRD.md). Stav: ke schválení. Napsáno 10. 10. 2026, přepsáno
po nezávislé kontrole.

Celé se to odehrává v jednom souboru `index.html`. Každá etapa končí něčím, co
jde v prohlížeči předvést, a vejde se do jedné session.

## Tvar názvu, na kterém se všechno láme

Rozhodnuto předem, protože podle kontroly je to místo, kde se dá nejvíc pokazit:

```
ak2_<kod>_<kniha>_<typ>_<stopa>_<sekundy>_<cas>.txt
```

- `ak2` je nový začátek. Dnešní záznamy začínají `poz_` a nový úklid se jich
  nikdy nedotkne.
- `<kod>` je šest znaků otisku kódu posluchače. Bez kódu je tam otisk slova
  „společný“. Do názvu se tedy nikdy nedostane nic, co posluchač napsal.
- `<kniha>` je deset znaků otisku názvu knihy, stejně jako dnes.
- `<typ>` je `m` pro místo v knize, `p` pro pin.
- Všechna pole jsou pevně dané délky nebo jen číslice, takže se nedají splést,
  ani když si někdo zvolí kód „jiri_2“ nebo „2024“.

Úklid po zápisu pak maže jen soubory začínající `ak2_<kod>_<kniha>_<typ>_`,
tedy vlastní záznamy téhož typu a téhož posluchače. Cizí kódy, piny ani dnešní
záznamy do záběru nespadnou.

## Jak se bude ověřovat

Dva posluchači se simulují dvěma profily prohlížeče, ne dvěma kartami: karty
sdílejí paměť stránky, takže by se o kód praly.

Rozvržení se neměří okem. Stránka má zakázané vodorovné posouvání, takže co
přeteče, to se jen odřízne a vypadá to v pořádku. Měří se skutečná poloha
a výška tlačítek a porovnává se s šířkou okna.

Před první ostrou zkouškou si uložím seznam všeho, co je ve složce s pozicemi.
Obsah souborů je prázdný, všechno je v názvech, takže ten seznam je jediná
záloha, kdyby úklid smazal víc, než má.

## Etapa 0: Snese Webshare nový název

Co bude fungovat: budeme vědět, jestli návrh vůbec stojí na nohou, dřív než se
napíše kód.

Závisí na: nic

Potřebuju od tebe: nic

Hotovo, když:
- [ ] Nahraju tři zkušební soubory s novým tvarem názvu a všechny tři se ve
      výpisu složky vrátí se jménem znak po znaku stejným, jaké jsem poslal.
- [ ] Vím, za jak dlouho po nahrání je nový soubor vidět ve výpisu z druhého
      zařízení, změřeno, ne odhadnuto.
- [ ] Zkušební soubory jsou po měření smazané a výsledek je zapsaný do PRD.

Jak to ověříme: nahraju je do složky s pozicemi, přečtu výpis, porovnám
a uklidím.

Stav: **hotovo 10. 10. 2026.** Všechny tři názvy prošly a vrátily se znak po
znaku stejné. Z druhého zařízení jsou vidět za 17 sekund, s čímž musí počítat
zkoušky přenosu v etapách 1 a 2. Zkušební soubory smazány, 40 dosavadních
záznamů nedotčeno. Podrobnosti v PRD.

## Etapa 1: Kód posluchače

Co bude fungovat: posluchač si zadá kód a jeho rozposlouchaný čas se přestane
míchat s ostatními. Kdo kód nezadá, nepozná rozdíl.

Závisí na: etapa 0

Potřebuju od tebe: nic

Hotovo, když:
- [x] Kód jde zadat na obrazovce s připojením i kdykoli později z knihovny, bez
      odpojení. Obě cesty jsou vyzkoušené.
- [x] Kód se pamatuje po zavření stránky.
- [x] Kód se ukládá dřív, než se poprvé načtou místa ze sítě, takže první
      synchronizace po přihlášení už běží pod ním.
- [x] Nepovedené přihlášení nesmaže rozepsaný kód.
- [x] Mezery na krajích, velká písmena a nezlomitelná mezera z mobilní klávesnice
      dávají stejný kód jako jeho čistá podoba.
- [x] Kód o 300 znacích, s emoji a s uvozovkou projde a místo se pod ním zpětně
      načte.
- [x] Posluchač s kódem A a posluchač s kódem B posunou tutéž knihu jinam a po
      novém načtení má každý svoje místo.
- [x] Ve složce po té zkoušce leží oba záznamy zároveň a dnešní záznamy téže
      knihy jsou pořád na svém místě.
- [x] Bez kódu se místo ukládá i čte dál, dosavadní záznam se použije a nic se
      nesmaže.
- [x] Kdo si zadá kód poprvé a vlastní záznam nemá, naváže na dosavadní.
- [x] Místní paměť prohlížeče rozlišuje kódy, ale dosavadní místní záznam se
      použije, dokud vlastní nevznikne.
- [x] Změna kódu během přehrávání uloží rozposlouchané místo pod starý kód
      a další zápis jde už pod nový, bez čekání na minutový odstup.

Jak to ověříme: ve dvou profilech se dvěma kódy posunu stejnou knihu na různá
místa, obě stránky načtu znovu a porovnám časy; vypíšu obsah složky a porovnám
se zálohou ze začátku.

Stav: **hotovo 10. 10. 2026.** Ověřeno trojím způsobem: zkouškou logiky nad
kódem vytaženým přímo z aplikace (24 bodů, vše prošlo), ostrou zkouškou proti
Webshare se dvěma kódy, kde úklid smazal jen vlastní starší záznam a nechal
cizí místo, vlastní pin i všech 41 dosavadních záznamů, a zkouškou ovládání
v náhledu s předstíraným archivem.

## Etapa 2: Pin

Co bude fungovat: před spaním jedno ťuknutí uloží místo, ráno jedno ťuknutí
vrátí přehrávač přesně tam. Funguje to i bez kódu.

Závisí na: etapa 1

Potřebuju od tebe: nic

Hotovo, když:
- [x] V přehrávači jsou dvě tlačítka, uložit pin a skočit na pin, obě viditelná
      i když je přehrávač sbalený.
- [x] Obě tlačítka reagují na krátké ťuknutí, bez přidržení a bez potvrzovacího
      dotazu.
- [x] Tlačítko pro skok ukazuje čas uloženého pinu a ten se překreslí po uložení
      pinu, po skoku, po přepnutí stopy i po přepnutí knihy.
- [x] Když pin není, tlačítko pro skok má atribut `disabled`.
- [x] Pin funguje se zadaným kódem i bez něj.
- [x] Po uložení pinu a pěti minutách dalšího poslechu je pin na původním místě.
- [x] Pin přežije zavření a otevření stránky.
- [x] Pin uložený v jednom profilu se objeví ve druhém se stejným kódem,
      do půl minuty (server ho zveřejní zhruba za 17 sekund).
- [x] Pin uložený pod kódem A není vidět pod kódem B.
- [x] Piny ve dvou různých knihách existují vedle sebe a skok vrací do té správné.
- [x] Nový pin přepíše starý a ve složce po úklidu zůstane jeden.
- [x] Běžné ukládání místa pin nesmaže.
- [x] Skok na pin ve stejné stopě nezpůsobí nové stahování a uložené místo se
      posune na čas pinu, ne na nulu. (Původně tu stálo, že se uložené místo
      nezmění. To bylo špatně: po skoku posluchač poslouchá od pinu, takže se
      místo posunout má. Hlídá se jen to, aby se neuložila nula.)
- [x] Skok na pin do jiné stopy skočí přesně a uložené místo přepíše až dalším
      běžným ukládáním, ne nulou hned po spuštění.
- [x] Pin uložený na čase do tří sekund od začátku stopy se provede správně,
      tedy skutečně skočí na začátek a nezůstane, kde byl.
- [x] Ťuknutí na pin během právě probíhajícího ukládání místa se neztratí, pin
      se uloží.
- [x] Při nedostupné síti se pin uloží v prohlížeči, tlačítko to dá najevo
      a po obnovení sítě se při dalším zápisu odešle.
- [x] Odmítnutí zápisu serverem se pozná a chová se stejně jako výpadek sítě,
      tedy tiše se neztratí.

Jak to ověříme: pustím knihu, uložím pin, nechám hrát dál, zavřu stránku, otevřu
a skočím na pin; totéž ve druhém profilu se stejným kódem a pak s jiným; výpadek
vyzkouším vypnutím sítě během ukládání; souběh vyvolám ťuknutím na pin hned po
pauze, která si bere zámek.

Stav: **hotovo 10. 10. 2026.** Ověřeno v náhledu s předstíraným archivem:
piny ve dvou knihách vedle sebe, přepsání pinu (na serveru zůstane jeden),
neviditelnost pod jiným kódem, pin bez kódu, stažení pinu z druhého zařízení,
výpadek sítě i doručení po jeho obnovení, ťuknutí během probíhajícího ukládání
a přežití zavření stránky. Skok do jiné stopy i uvnitř stopy ukládá čas pinu,
nikdy nulu.

## Etapa 3: Ovládání pod palec a délka přeskoku

Co bude fungovat: obojí se dá ovládat na telefonu po tmě a nastavená délka
přeskoku se přenese mezi zařízeními.

Závisí na: etapy 1 a 2

Potřebuju od tebe: pohled na snímek v rozměru telefonu, jestli ti to sedí

Hotovo, když:
- [x] Při šířce 375 bodů leží obě tlačítka pinu celá uvnitř okna, změřeno
      polohou prvku, ne okem.
- [x] Obě tlačítka pinu jsou vysoká aspoň 44 bodů.
- [x] Řada s ovládáním se při 375 bodech nerozsype a žádné tlačítko z ní
      nevypadne.
- [x] Délka přeskoku nastavená v jednom profilu se po načtení objeví ve druhém
      pod stejným kódem.
- [x] Dva kódy v jednom prohlížeči si délku přeskoku navzájem nepřepisují.
- [x] Bez kódu zůstává délka přeskoku jen v tom prohlížeči, jako dosud.

Jak to ověříme: přepnu prohlížeč na šířku telefonu, změřím poloho a výšku
tlačítek, udělám snímek a pošlu ti ho.

Stav: **hotovo 10. 10. 2026.** Měřeno polohou prvků při šířce 375 bodů, ne
okem: tlačítka pinu leží na 15 až 183 a 193 až 360 bodech, obě 46 bodů vysoká,
z hlavní řady nevypadlo žádné z šesti tlačítek a stránka nepřetéká. Vidět jsou
i ve sbaleném přehrávači. Přenos délky přeskoku odhalil chybu: čtení ze serveru
znalo jen typy pro místo a pin, takže nastavení propadávalo. Opraveno a znovu
ověřeno, druhé zařízení si délku stáhne a dva kódy si ji nepřepisují.

## Etapa 4: Nasazení

Co bude fungovat: nová verze je na webu a obě funkce tam projdou stejnou
zkouškou jako lokálně.

Závisí na: etapy 1 až 3

Potřebuju od tebe: souhlas s uložením do gitu a s nasazením

Hotovo, když:
- [ ] Změna je uložená v gitu a nasazená.
- [ ] Na adrese knihovny projde zkouška dvou kódů i zkouška pinu, včetně
      přenosu mezi dvěma profily.
- [ ] Dosavadní rozposlouchaná místa jsou po nasazení pořád na svých místech,
      ověřeno u tří knih, které máš rozposlouchané.

Jak to ověříme: po tvém souhlasu nasadím a projdu obě zkoušky přímo na adrese
knihovny.

Stav: čeká

## Kontrola hotové změny, 10. 10. 2026

Celou změnu prošla nezávislá session s čistým kontextem se zadáním hledat
hlavně riziko pro 41 dosavadních záznamů a pro posluchače bez kódu. Potvrdila,
že na dosavadní záznamy nevede žádná cesta (mazání míří vždy na názvy
začínající ak2_) a že bez kódu se nic nerozbije. Našla sedm dalších věcí,
všechny opravené a znovu ověřené:

1. **Skok na pin spouštěl knihu otevřenou na obrazovce, ne tu, která hraje.**
   Kdo poslouchal jednu knihu a prohlížel si v knihovně druhou, jedním ťuknutím
   by spustil tu druhou na čase cizího pinu a přepsal v ní rozposlouchané místo
   na všech zařízeních. Nejvážnější nález.
2. Po přepnutí kódu z knihovny zůstala v paměti délka přeskoku předchozího
   posluchače a první ťuknutí ji uložilo pod nový kód.
3. Dlouhý kód v hlavičce vystrčil tlačítko Odpojit mimo obrazovku telefonu.
4. Pin odložený kvůli výpadku sítě se odesílal s časem doručení, takže mohl
   přebít novější pin z jiného zařízení.
5. Rozepsaný kód se při psaní stával rovnou platným, písmeno po písmenu.
6. Složka s pozicemi se při každém otevření knihovny četla dvakrát.
7. Jedna odrážka v PRD si odporovala s plánem (skok na pin a uložené místo).

## Co může překvapit

Z kontroly kódu, ať se na to nezapomene při stavbě:

1. **Úklid starých záznamů.** Dnes maže všechno, co patří ke knize, podle
   začátku názvu. Nový tvar názvu to řeší, ale filtr se musí opravit zároveň
   se zápisem, ne potom.
2. **Záznam v prohlížeči se ukládá jako celek**, takže pin do něj nepatří, jinak
   ho přepíše každé páté sekundy poslechu.
3. **Skok na pin nesmí jít stejnou cestou jako přepnutí stopy.** Ta cesta po
   spuštění uloží aktuální čas, což by při skoku znamenalo uložit nulu a přepsat
   rozposlouchané místo na všech zařízeních.
4. **Sbalený přehrávač skrývá druhou řadu tlačítek.** Právě ten stav je noční.
5. **Část přehrávače je mimo překreslovanou oblast**, takže čas na tlačítku pinu
   se musí aktualizovat ručně na všech místech, kde se mění stopa nebo kniha.
6. **Zápis drží jeden společný zámek.** Dokud běží ukládání místa, ťuknutí na
   pin se dnes zahodí bez hlášení.
7. **Paměť prohlížeče si pamatuje i to, co se nepovedlo.** Mezi koly zkoušek ji
   budu mazat, jinak budu ladit něco, co už je dávno jinak.
