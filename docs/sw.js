// Resume Pro — Service Worker v3.8.0
const CACHE_NAME = 'resume-pro-v3.8.0';
const STATIC_ASSETS = [
  './',
  './index.html',
  './editor.html',
  './preview.html',
  './pdfs/',
];

// Install: cache static assets
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => {
      return cache.addAll(STATIC_ASSETS).catch(err => {
        console.warn('SW: Failed to cache some assets:', err);
      });
    })
  );
  self.skipWaiting();
});

// Activate: clean old caches
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch: network-first with cache fallback
self.addEventListener('fetch', event => {
  const url = new URL(event.request.url);

  // Skip cross-origin requests (CDN, API, etc.)
  if (url.origin !== self.location.origin) return;

  // Skip PDF requests (always fresh from network)
  if (url.pathname.endsWith('.pdf')) return;

  // Skip non-GET requests
  if (event.request.method !== 'GET') return;

  // For navigation requests (HTML pages), use network-first
  if (event.request.mode === 'navigate' || url.pathname.endsWith('.html') || url.pathname.endsWith('/')) {
    event.respondWith(
      fetch(event.request)
        .then(response => {
          if (response.status === 200) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then(cache => {
              cache.put(event.request, clone);
            }).catch(() => {});
          }
          return response;
        })
        .catch(() => {
          return caches.match(event.request).then(cached => {
            return cached || caches.match('./index.html');
          });
        })
    );
    return;
  }

  // For other assets (JS, CSS, etc.), cache-first for speed
  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;
      return fetch(event.request).then(response => {
        if (response.status === 200) {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => {
            cache.put(event.request, clone);
          }).catch(() => {});
        }
        return response;
      });
    })
  );
});
