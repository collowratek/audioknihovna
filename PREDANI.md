# Předání Fandovi: co nastavit na GitHubu

Návrh k rozhodnutí. Nic z toho není nastavené, nastavení mění jen Jiří.

## Doporučení: fork, ne spoluautorství

Fanda nepotřebuje žádné oprávnění. Repozitář je veřejný, takže si ho může
zkopírovat k sobě (fork) a posílat návrhy změn (pull request) bez jakéhokoli
práva zápisu. Stačí mu poslat odkaz na repozitář a na `CONTRIBUTING.md`.

Proč takhle: spoluautor na osobním účtu GitHubu má vždy právo zapisovat přímo
do hlavní větve a hlavní větev je okamžitě na webu. Mezi „pošle návrh“ a
„změnil web“ by nebyl žádný krok, ve kterém by se změna přečetla. Přitom právě
přečtení změny je jediná obrana proti tomu, co pravidla v hlavičce stránky
neumí ohlídat (viz `KONTROLA.md`).

## Kdybys přesto chtěl spoluautora

Pak je potřeba zamknout hlavní větev, jinak je spoluautorství nebezpečnější než
fork. Nastavení je v repozitáři: **Settings → Branches → Add branch ruleset**.

| Volba | Hodnota | Proč |
|---|---|---|
| Target branches | `main` | hlavní větev je to, co je na webu |
| Require a pull request before merging | zapnuto | žádný přímý zápis |
| Required approvals | 1 | změnu musí někdo schválit |
| Require review from Code Owners | vypnuto | není potřeba, stačí schválení |
| Dismiss stale approvals | zapnuto | po novém commitu se schválení ruší |
| Bypass list | účet Jiřího (Repository admin) | ať tobě a mně nezablokuje přidávání knih |

Bypass list je důležitý: bez něj by se ani Jiří nedostal přímo do hlavní větve
a každé přidání knihy by muselo přes pull request, který by si sám schvaloval.

## Jak kontrolovat Fandovy návrhy

Než se cokoli sloučí, projít změnu. V Claude Code:

```
/code-review high collowratek/audioknihovna#<číslo pull requestu>
```

Kontrola se dívá na celou změnu, ale u tohohle projektu rozhodují tři věci.
Projít je i očima:

1. **Nová adresa.** Cokoli nového v `Content-Security-Policy`, v `fetch`,
   v `src`, v `href`, v `location`. Pravidla v hlavičce stránky nepustí cizí
   cíl, ale nepokrývají přesměrování celé stránky ani zneužití Webshare.
2. **Cokoli nad meta značkou s pravidly.** Pravidla platí až od ní dolů, takže
   řádek nad ní je mimo jejich dosah.
3. **Práce s přihlášením.** `wst`, `localStorage`, `#t=`, `postMessage`.
   Přihlášení nemá v kódu co dělat nikde jinde než ve volání Webshare.

Sloučení dělá jen Jiří, až si změnu přečte.

## Co tím nezmizí

Kdo může nasadit program na adresu knihovny, má plnou moc nad účtem na
Webshare. Nastavení GitHubu tohle neřeší, jen zajišťuje, že nasazuje vždy Jiří
po přečtení změny. Strukturální obrany jsou v `KONTROLA.md`: vlastní doména
a účet Webshare jen pro archiv.
