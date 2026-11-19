# Winstar Security Solutions website

Website planning and HTML scaffolds for Winstar Security Solutions, Kenya.

- `website-blueprint.md`: agreed strategy, page map and content direction.
- `checklist.md`: implementation progress and outstanding decisions.
- Root HTML files: 26 planned page shells, starting with `index.html`.
- `sources/`: supplied company and policy reference material.
- `review/`: extracted content and supporting reviews.

The site is at the scaffolding stage. Shared navigation, styles and page content are still to be developed. Careers is outside the agreed scope.

Open `index.html` locally to inspect the scaffold. No build step is required at this stage.
## Contact form delivery

Serve the site with PHP 8.1 or later. Run `composer install --no-dev` in the project root and deploy the resulting `vendor/` directory alongside `send-enquiry.php`. Enable the PHP OpenSSL extension for SMTP.

Set `SMTP_HOST`, `SMTP_USERNAME` and `SMTP_PASSWORD` in the hosting environment. The sender defaults to the SMTP username. Set `SMTP_FROM` if the provider requires a different verified sender address. Delivery uses STARTTLS on port 587 by default. Set `SMTP_PORT=465` for implicit TLS.

Send a test enquiry through the hosted contact page and confirm it arrives at `info@winstarsecurity.co.ke`.

