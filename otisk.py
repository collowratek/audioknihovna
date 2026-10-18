#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Otisk programu ve stránce pro pravidla Content-Security-Policy.

Pravidla v index.html nepouštějí libovolný program ve stránce, ale jen ten
jeden, jehož otisk (sha256) je v nich zapsaný. Kdo změní uvnitř značky
<script> jediný znak, musí otisk přepočítat, jinak prohlížeč stránku vůbec
nespustí. Je to schválně: změna programu je pak vidět i v pravidlech
a nemůže proklouznout jako nenápadná úprava vzhledu.

Použití:
    python3 otisk.py            zkontroluje, že otisk v pravidlech sedí
    python3 otisk.py --zapis    přepočítá ho a zapíše do index.html

Návratový kód 0 = sedí, 1 = nesedí (hodí se do kontroly před odesláním).

Napsali Claude Code a Jiří, 18. 10. 2026.
"""

import base64
import hashlib
import io
import os
import re
import sys

SOUBOR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')


def program(html):
    """Vrátí text posledního bloku <script> ve stránce.

    Bere POSLEDNÍ, ne první: v hlavičce stránky je o těch značkách řeč
    v komentáři a naivní hledání by se chytlo na něj.
    """
    zacatky = [m.end() for m in re.finditer(r'<script>', html)]
    if not zacatky:
        raise SystemExit('ve stránce není žádný blok <script>')
    od = zacatky[-1]
    do = html.index('</script>', od)
    return html[od:do]


def spocti(text):
    """Otisk textu tak, jak ho počítá prohlížeč: sha256 v base64."""
    return base64.b64encode(hashlib.sha256(text.encode('utf-8')).digest()).decode()


def main():
    html = io.open(SOUBOR, encoding='utf-8').read()
    novy = spocti(program(html))

    nalez = re.search(r"script-src 'sha256-([A-Za-z0-9+/=]+)'", html)
    if not nalez:
        raise SystemExit('v pravidlech není žádný otisk, zkontroluj meta značku')
    stary = nalez.group(1)

    if '--zapis' in sys.argv:
        if stary == novy:
            print('otisk už sedí, není co zapisovat:', novy)
            return 0
        io.open(SOUBOR, 'w', encoding='utf-8').write(
            html.replace("'sha256-%s'" % stary, "'sha256-%s'" % novy))
        print('otisk přepsán')
        print('  byl:', stary)
        print('  je: ', novy)
        return 0

    if stary == novy:
        print('otisk sedí:', novy)
        return 0
    print('otisk NESEDÍ, stránka se v prohlížeči nespustí')
    print('  v pravidlech:', stary)
    print('  podle programu:', novy)
    print('  oprav příkazem: python3 otisk.py --zapis')
    return 1


if __name__ == '__main__':
    sys.exit(main())
