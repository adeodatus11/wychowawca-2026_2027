/* Podgląd infografik: pełny ekran, powiększanie i przesuwanie.
   Bez skryptu artykuł działa normalnie — infografika jest zwykłym elementem strony. */
(function () {
  'use strict';

  var figures = document.querySelectorAll('.guide-figure');
  if (!figures.length) return;

  var dialog = document.createElement('dialog');
  if (typeof dialog.showModal !== 'function') return;

  document.documentElement.classList.add('js-figures');

  var STEPS = [1, 1.25, 1.5, 2, 2.5, 3, 4];
  var step = 0;
  var baseWidth = 0;
  var stage, canvas, level, btnIn, btnOut;

  dialog.className = 'figure-viewer';
  dialog.setAttribute('aria-label', 'Podgląd infografiki');
  dialog.innerHTML =
    '<div class="figure-viewer-bar">' +
      '<p class="figure-viewer-title"></p>' +
      '<div class="figure-viewer-controls">' +
        '<button type="button" data-act="out" aria-label="Pomniejsz">−</button>' +
        '<span class="figure-viewer-level" aria-live="polite">100%</span>' +
        '<button type="button" data-act="in" aria-label="Powiększ">+</button>' +
        '<button type="button" data-act="fit">Dopasuj</button>' +
        '<button type="button" data-act="close" class="figure-viewer-close">Zamknij</button>' +
      '</div>' +
    '</div>' +
    '<div class="figure-viewer-stage"><div class="figure-viewer-canvas"></div></div>';
  document.body.appendChild(dialog);

  stage = dialog.querySelector('.figure-viewer-stage');
  canvas = dialog.querySelector('.figure-viewer-canvas');
  level = dialog.querySelector('.figure-viewer-level');
  btnIn = dialog.querySelector('[data-act="in"]');
  btnOut = dialog.querySelector('[data-act="out"]');

  function available() {
    var cs = window.getComputedStyle(stage);
    return stage.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
  }

  function apply(keepCentre) {
    var prevW = canvas.offsetWidth || 1;
    var midX = (stage.scrollLeft + stage.clientWidth / 2) / prevW;
    var prevH = canvas.offsetHeight || 1;
    var midY = (stage.scrollTop + stage.clientHeight / 2) / prevH;

    canvas.style.width = Math.round(baseWidth * STEPS[step]) + 'px';
    level.textContent = Math.round(STEPS[step] * 100) + '%';
    btnOut.disabled = step === 0;
    btnIn.disabled = step === STEPS.length - 1;

    if (keepCentre) {
      stage.scrollLeft = midX * canvas.offsetWidth - stage.clientWidth / 2;
      stage.scrollTop = midY * canvas.offsetHeight - stage.clientHeight / 2;
    }
  }

  function fit() {
    step = 0;
    baseWidth = available();
    apply(false);
    stage.scrollTop = 0;
    stage.scrollLeft = 0;
  }

  function open(figure) {
    var svg = figure.querySelector('svg');
    var title = figure.querySelector('title');
    if (!svg) return;
    var copy = svg.cloneNode(true);
    // Klon trafia do tego samego dokumentu, więc identyfikatory muszą zniknąć,
    // żeby nie powstały duplikaty id. Opis podajemy wprost w aria-label.
    copy.removeAttribute('aria-labelledby');
    copy.setAttribute('aria-label', [svg.querySelector('title'), svg.querySelector('desc')]
      .filter(Boolean).map(function (n) { return n.textContent; }).join('. '));
    Array.prototype.forEach.call(copy.querySelectorAll('[id]'), function (n) {
      n.removeAttribute('id');
    });
    canvas.innerHTML = '';
    canvas.appendChild(copy);
    dialog.querySelector('.figure-viewer-title').textContent =
      title ? title.textContent : 'Infografika';
    dialog.showModal();
    fit();
  }

  dialog.addEventListener('click', function (e) {
    var act = e.target.getAttribute && e.target.getAttribute('data-act');
    if (act === 'close') { dialog.close(); return; }
    if (act === 'in' && step < STEPS.length - 1) { step++; apply(true); return; }
    if (act === 'out' && step > 0) { step--; apply(true); return; }
    if (act === 'fit') { fit(); return; }
    // kliknięcie w tło poza sceną zamyka podgląd
    if (e.target === dialog) dialog.close();
  });

  // przeciąganie myszą (na ekranach dotykowych wystarcza zwykłe przewijanie)
  var dragging = false, startX = 0, startY = 0, startL = 0, startT = 0;
  stage.addEventListener('pointerdown', function (e) {
    if (e.pointerType === 'touch') return;
    dragging = true;
    startX = e.clientX; startY = e.clientY;
    startL = stage.scrollLeft; startT = stage.scrollTop;
    stage.classList.add('is-grabbing');
    stage.setPointerCapture(e.pointerId);
  });
  stage.addEventListener('pointermove', function (e) {
    if (!dragging) return;
    stage.scrollLeft = startL - (e.clientX - startX);
    stage.scrollTop = startT - (e.clientY - startY);
  });
  ['pointerup', 'pointercancel'].forEach(function (ev) {
    stage.addEventListener(ev, function () {
      dragging = false;
      stage.classList.remove('is-grabbing');
    });
  });

  window.addEventListener('resize', function () {
    if (dialog.open && step === 0) fit();
  });

  Array.prototype.forEach.call(figures, function (figure) {
    var button = figure.querySelector('.guide-figure-open');
    var frame = figure.querySelector('.guide-figure-frame');
    if (button) button.addEventListener('click', function () { open(figure); });
    if (frame) frame.addEventListener('click', function () { open(figure); });
  });
})();
