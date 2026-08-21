const search = document.querySelector('#search');
const goalFilter = document.querySelector('#goalFilter');
const cards = Array.from(document.querySelectorAll('.lesson-card'));
const goalSections = Array.from(document.querySelectorAll('.goal-section'));
const count = document.querySelector('#count');

function normalize(value) {
  return value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}

function applyFilters() {
  const query = normalize(search.value || '');
  const goal = goalFilter.value;
  let visible = 0;
  cards.forEach((card) => {
    const text = normalize(card.textContent);
    const matchesText = !query || text.includes(query);
    const matchesGoal = goal === 'all' || card.dataset.goal === goal;
    const show = matchesText && matchesGoal;
    card.hidden = !show;
    if (show) visible += 1;
  });
  goalSections.forEach((section) => {
    const hasVisibleCard = Boolean(section.querySelector('.lesson-card:not([hidden])'));
    section.hidden = !hasVisibleCard;
  });
  count.textContent = `${visible} z ${cards.length} lekcji`;
}

search.addEventListener('input', applyFilters);
goalFilter.addEventListener('change', applyFilters);
applyFilters();
