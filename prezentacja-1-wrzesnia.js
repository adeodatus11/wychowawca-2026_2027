const deck = document.querySelector('#deck');
const stage = document.querySelector('#deckStage');
const slides = Array.from(document.querySelectorAll('.slide'));
const prevButton = document.querySelector('#prevSlide');
const nextButton = document.querySelector('#nextSlide');
const fullscreenButton = document.querySelector('#fullscreenButton');
const counter = document.querySelector('#slideCounter');
const progressFill = document.querySelector('#progressFill');
const dots = document.querySelector('#slideDots');

let current = 0;

function clampSlide(index) {
  return Math.max(0, Math.min(slides.length - 1, index));
}

function renderDots() {
  dots.innerHTML = '';
  slides.forEach((slide, index) => {
    const dot = document.createElement('button');
    dot.className = 'slide-dot';
    dot.type = 'button';
    dot.setAttribute('aria-label', `Przejdź do slajdu ${index + 1}: ${slide.dataset.title || ''}`);
    dot.addEventListener('click', () => showSlide(index));
    dots.append(dot);
  });
}

function showSlide(index) {
  current = clampSlide(index);
  slides.forEach((slide, slideIndex) => {
    const active = slideIndex === current;
    slide.classList.toggle('is-active', active);
    slide.setAttribute('aria-hidden', active ? 'false' : 'true');
  });

  counter.textContent = `${current + 1} / ${slides.length}`;
  progressFill.style.width = `${((current + 1) / slides.length) * 100}%`;

  Array.from(dots.children).forEach((dot, indexDot) => {
    dot.classList.toggle('is-active', indexDot === current);
  });

  prevButton.disabled = current === 0;
  nextButton.disabled = current === slides.length - 1;
  window.history.replaceState(null, '', `#slajd-${current + 1}`);
}

function nextSlide() {
  showSlide(current + 1);
}

function previousSlide() {
  showSlide(current - 1);
}

function goFromHash() {
  const match = window.location.hash.match(/slajd-(\d+)/);
  if (!match) return;
  const index = Number(match[1]) - 1;
  if (Number.isFinite(index)) showSlide(index);
}

async function toggleFullscreen() {
  if (!document.fullscreenElement) {
    await deck.requestFullscreen();
    return;
  }
  await document.exitFullscreen();
}

function updateFullscreenLabel() {
  fullscreenButton.textContent = document.fullscreenElement ? 'Wyjdź z pełnego ekranu' : 'Pełny ekran';
}

function isInteractiveTarget(target) {
  return Boolean(target.closest('a, button, input, select, textarea, summary'));
}

prevButton.addEventListener('click', previousSlide);
nextButton.addEventListener('click', nextSlide);
fullscreenButton.addEventListener('click', () => {
  toggleFullscreen().catch(() => {
    fullscreenButton.textContent = 'Pełny ekran niedostępny';
    window.setTimeout(updateFullscreenLabel, 1600);
  });
});
document.addEventListener('fullscreenchange', updateFullscreenLabel);

stage.addEventListener('click', (event) => {
  if (isInteractiveTarget(event.target)) return;
  if (current < slides.length - 1) nextSlide();
});

document.addEventListener('keydown', (event) => {
  if (event.altKey || event.ctrlKey || event.metaKey) return;

  switch (event.key) {
    case 'ArrowRight':
    case 'PageDown':
    case ' ':
      event.preventDefault();
      nextSlide();
      break;
    case 'ArrowLeft':
    case 'PageUp':
      event.preventDefault();
      previousSlide();
      break;
    case 'Home':
      event.preventDefault();
      showSlide(0);
      break;
    case 'End':
      event.preventDefault();
      showSlide(slides.length - 1);
      break;
    default:
      break;
  }
});

renderDots();
slides.forEach((slide, index) => {
  slide.dataset.index = String(index);
  slide.querySelector('.slide-main')?.setAttribute('data-number', String(index + 1).padStart(2, '0'));
});
goFromHash();
if (!window.location.hash) showSlide(0);
