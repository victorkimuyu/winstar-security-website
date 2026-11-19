const contactForm = document.getElementById('contact-form');
const contactDialog = document.getElementById('contact-dialog');

contactDialog.addEventListener('close', () => contactForm.elements.email.focus());

contactForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const fields = new FormData(contactForm);
  const email = fields.get('email').trim();
  const phone = fields.get('phone').trim();
  if (!email && !phone) {
    contactDialog.showModal();
    return;
  }
  const button = contactForm.querySelector('button[type="submit"]');
  if (button.disabled) return;
  const status = document.getElementById('contact-status');
  button.disabled = true;
  status.hidden = false;
  status.textContent = 'Sending your message…';
  try {
    const response = await fetch(contactForm.action, {
      method: 'POST',
      headers: { Accept: 'application/json' },
      body: fields
    });
    const result = await response.json();
    if (response.ok && result.sent === true) {
      window.location.assign('thank-you.html');
      return;
    }
    status.textContent = result.message || 'We couldn’t send your message. Please try again or call our team.';
  } catch {
    status.textContent = 'We couldn’t confirm your message was sent. Please try again or call our team.';
  }
  button.disabled = false;
});

window.addEventListener('pageshow', () => {
  contactForm.querySelector('button[type="submit"]').disabled = false;
  document.getElementById('contact-status').hidden = true;
});
