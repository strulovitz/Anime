/* ============================================================
   LEARNIME.COM — tiny gallery lightbox
   No libraries. No tracking. Works on desktop + phone.

   How to use in HTML:

   <div class="gallery" data-gallery="stage-1">
     <a class="gal-item"
        href="images/large/pic.jpg"          <- shown big in the lightbox
        data-full="images/pic.png"           <- optional: original full-res file
        data-caption="Short human caption">
       <img src="images/thumbs/pic.jpg" loading="lazy" alt="describe the picture">
     </a>
     ... more items ...
   </div>

   Every .gallery is its OWN gallery: the arrows only move inside that block.
   Without JavaScript the thumbnails are still plain links to the big picture,
   so nothing is ever broken.
   ============================================================ */

(function () {
  'use strict';

  var galleries = [].slice.call(document.querySelectorAll('.gallery'));
  if (!galleries.length) return;

  /* ---------- build the single shared overlay ---------- */

  var overlay = document.createElement('div');
  overlay.className = 'lb';
  overlay.setAttribute('role', 'dialog');
  overlay.setAttribute('aria-modal', 'true');
  overlay.setAttribute('aria-label', 'Picture viewer');
  overlay.hidden = true;
  overlay.innerHTML =
    '<div class="lb-backdrop" data-lb-close></div>' +
    '<button class="lb-btn lb-close" type="button" data-lb-close aria-label="Close picture (Esc)">&#10005;</button>' +
    '<button class="lb-btn lb-prev" type="button" data-lb-prev aria-label="Previous picture">&#10094;</button>' +
    '<button class="lb-btn lb-next" type="button" data-lb-next aria-label="Next picture">&#10095;</button>' +
    '<figure class="lb-stage">' +
    '  <div class="lb-imgwrap">' +
    '    <div class="lb-spinner" aria-hidden="true"></div>' +
    '    <img class="lb-img" alt="">' +
    '  </div>' +
    '  <figcaption class="lb-bar">' +
    '    <span class="lb-count"></span>' +
    '    <span class="lb-caption"></span>' +
    '    <a class="lb-full" target="_blank" rel="noopener">Open full resolution &#8599;</a>' +
    '  </figcaption>' +
    '</figure>';
  document.body.appendChild(overlay);

  var imgEl     = overlay.querySelector('.lb-img');
  var wrapEl    = overlay.querySelector('.lb-imgwrap');
  var capEl     = overlay.querySelector('.lb-caption');
  var countEl   = overlay.querySelector('.lb-count');
  var fullEl    = overlay.querySelector('.lb-full');
  var prevBtn   = overlay.querySelector('.lb-prev');
  var nextBtn   = overlay.querySelector('.lb-next');
  var closeBtn  = overlay.querySelector('.lb-close');

  var items = [];        // the items of the gallery currently open
  var index = 0;
  var lastFocus = null;
  var scrollY = 0;

  /* ---------- open / show / close ---------- */

  function show(i) {
    if (!items.length) return;
    index = (i + items.length) % items.length;   // wrap around
    var it = items[index];
    var big = it.getAttribute('href');
    var full = it.getAttribute('data-full');
    var thumb = it.querySelector('img');
    var caption = it.getAttribute('data-caption') ||
                  (thumb ? thumb.getAttribute('alt') : '') || '';

    wrapEl.classList.add('is-loading');
    imgEl.src = big;
    imgEl.alt = caption;
    capEl.textContent = caption;
    countEl.textContent = (index + 1) + ' / ' + items.length;

    if (full) {
      fullEl.href = full;
      fullEl.style.display = '';
    } else {
      fullEl.removeAttribute('href');
      fullEl.style.display = 'none';
    }

    var single = items.length < 2;
    prevBtn.hidden = single;
    nextBtn.hidden = single;

    // preload the neighbours so next/prev feels instant
    if (!single) {
      [items[(index + 1) % items.length], items[(index - 1 + items.length) % items.length]]
        .forEach(function (n) { var p = new Image(); p.src = n.getAttribute('href'); });
    }
  }

  imgEl.addEventListener('load', function () { wrapEl.classList.remove('is-loading'); });
  imgEl.addEventListener('error', function () { wrapEl.classList.remove('is-loading'); });

  function open(groupItems, i, trigger) {
    items = groupItems;
    lastFocus = trigger || document.activeElement;

    // lock the page behind without losing the reading position
    scrollY = window.pageYOffset || document.documentElement.scrollTop;
    document.body.style.top = (-scrollY) + 'px';
    document.body.classList.add('lb-open');

    overlay.hidden = false;
    // let the browser paint once, then fade in
    requestAnimationFrame(function () { overlay.classList.add('is-open'); });
    show(i);
    closeBtn.focus();
  }

  function close() {
    overlay.classList.remove('is-open');
    overlay.hidden = true;
    imgEl.removeAttribute('src');

    document.body.classList.remove('lb-open');
    document.body.style.top = '';
    window.scrollTo(0, scrollY);          // back exactly where you were

    if (lastFocus && lastFocus.focus) lastFocus.focus();
    items = [];
  }

  /* ---------- wire the thumbnails ---------- */

  galleries.forEach(function (gal) {
    var groupItems = [].slice.call(gal.querySelectorAll('.gal-item'));
    groupItems.forEach(function (item, i) {
      item.addEventListener('click', function (ev) {
        // let people still ctrl/cmd/middle-click to open in a new tab
        if (ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.altKey || ev.button !== 0) return;
        ev.preventDefault();
        open(groupItems, i, item);
      });
    });
  });

  /* ---------- controls ---------- */

  overlay.addEventListener('click', function (ev) {
    if (ev.target.closest('[data-lb-close]')) { close(); return; }
    if (ev.target.closest('[data-lb-prev]'))  { show(index - 1); return; }
    if (ev.target.closest('[data-lb-next]'))  { show(index + 1); return; }
  });

  document.addEventListener('keydown', function (ev) {
    if (overlay.hidden) return;
    if (ev.key === 'Escape')     { ev.preventDefault(); close(); }
    else if (ev.key === 'ArrowLeft')  { ev.preventDefault(); show(index - 1); }
    else if (ev.key === 'ArrowRight') { ev.preventDefault(); show(index + 1); }
    else if (ev.key === 'Tab') {
      // keep keyboard focus inside the viewer
      var f = [closeBtn, prevBtn, nextBtn, fullEl].filter(function (el) {
        return !el.hidden && el.style.display !== 'none';
      });
      var pos = f.indexOf(document.activeElement);
      var nextPos = ev.shiftKey ? pos - 1 : pos + 1;
      if (pos === -1 || nextPos < 0 || nextPos >= f.length) {
        ev.preventDefault();
        f[ev.shiftKey ? f.length - 1 : 0].focus();
      }
    }
  });

  /* ---------- swipe on phones ---------- */

  var tx = 0, ty = 0, tt = 0;
  overlay.addEventListener('touchstart', function (ev) {
    if (ev.touches.length !== 1) return;
    tx = ev.touches[0].clientX;
    ty = ev.touches[0].clientY;
    tt = Date.now();
  }, { passive: true });

  overlay.addEventListener('touchend', function (ev) {
    if (!ev.changedTouches.length) return;
    var dx = ev.changedTouches[0].clientX - tx;
    var dy = ev.changedTouches[0].clientY - ty;
    if (Date.now() - tt > 700) return;                     // too slow to be a swipe
    if (Math.abs(dx) < 45 || Math.abs(dx) < Math.abs(dy)) {
      if (dy > 90 && Math.abs(dy) > Math.abs(dx)) close();  // swipe down = close
      return;
    }
    show(dx < 0 ? index + 1 : index - 1);                   // left = next
  }, { passive: true });

  /* browser back button closes the viewer instead of leaving the page */
  window.addEventListener('popstate', function () { if (!overlay.hidden) close(); });
})();
