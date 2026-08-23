/* Servisní worker: obsluhuje offline stopy.
   Přehrávač si vyžádá /offline/<ident>, worker odpoví souborem z úložiště.
   Uložené odpovědi jsou „neprůhledné“ (cizí doména), takže se nedají číst
   ani ověřit — jen uložit a přehrát. To pro naše účely stačí.            */
const CACHE = 'audio-offline-v1';

self.addEventListener('install', e => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil(self.clients.claim()));

self.addEventListener('fetch', e => {
  const u = new URL(e.request.url);
  if (u.origin !== self.location.origin || !u.pathname.startsWith('/audioknihovna/offline/')) return;
  e.respondWith(
    caches.open(CACHE)
      .then(c => c.match(u.pathname))
      .then(r => r || new Response('není staženo', { status: 404 }))
  );
});
