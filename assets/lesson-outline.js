(function () {
  'use strict';
  const outline = document.getElementById('lessonOutline');
  if (!outline) return;
  const headings = [...document.querySelectorAll('article > h2')];
  if (headings.length < 3) return;
  const list = outline.querySelector('ol');
  headings.forEach((heading, index) => {
    if (!heading.id) heading.id = `lesson-section-${index + 1}`;
    const item = document.createElement('li');
    const link = document.createElement('a');
    link.href = `#${heading.id}`;
    link.textContent = heading.textContent.replace(/^\d+\.\s*/, '');
    item.append(link);
    list.append(item);
  });
  const firstLab = document.querySelector('article > .foundation-lab, article > .market-lab, article > .learning-lab');
  if (firstLab && firstLab.compareDocumentPosition(headings[0]) & Node.DOCUMENT_POSITION_FOLLOWING) {
    firstLab.after(outline);
  } else {
    const title = document.querySelector('article > h1');
    if (title) title.after(outline);
  }
  outline.hidden = false;
  outline.open = window.matchMedia('(min-width: 761px)').matches;
})();
