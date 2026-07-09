const CACHE_NAME = "ega-academy-v1";
const ASSETS = [
  "/",
  "/index.html",
  "/lector.html",
  "/perfil.html",
  "/certificado.html",
  "/playground.html",
  "/foro.html",
  "/style.css",
  "/app.js",
  "/manifest.json"
];

self.addEventListener("install", e => {
  e.waitUntil(
    caches.open(CACHE_NAME).then(c => c.addAll(ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener("fetch", e => {
  const url = new URL(e.request.url);

  if (url.pathname.startsWith("/api/")) {
    e.respondWith(fetch(e.request).catch(() => new Response(JSON.stringify({error: "offline"}), {status: 503})));
    return;
  }

  if (url.pathname.match(/\.(txt|json|png|jpg|jpeg|svg|ico)$/) || url.pathname.startsWith("/libros/")) {
    e.respondWith(
      caches.open(CACHE_NAME).then(c => {
        return c.match(e.request).then(r => {
          const fetchPromise = fetch(e.request).then(res => {
            if (res.ok) c.put(e.request, res.clone());
            return res;
          }).catch(() => r);
          return r || fetchPromise;
        });
      })
    );
    return;
  }

  e.respondWith(
    caches.match(e.request).then(r => r || fetch(e.request).catch(() => caches.match("/index.html")))
  );
});

self.addEventListener("activate", e => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
    ))
  );
});
