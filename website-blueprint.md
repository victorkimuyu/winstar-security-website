# Winstar Security Solutions: Website Blueprint

Living reference for the website's strategy, content and structure. Updated as decisions are agreed. Implementation progress belongs in `checklist.md`.

## Purpose and audiences

Present Winstar as a premier, reliable and capable private security provider in Kenya. The new website must communicate the capacity and capabilities that the previous website undersold through its design and content.

Primary audiences:
- Prospective customers currently using competing security providers.
- Individuals and organisations that do not currently purchase professional security services but may do so in future.
- Existing Winstar customers seeking contacts, support or additional services.

Visitors should be able to understand Winstar's offer, assess its suitability and credibility, explore relevant services and sectors, and make an enquiry.

## Positioning and tone

Organisational capacity is the central message: experienced, professional personnel supported by sound management and operational structures, systems, equipment, amenities and fleet.

Demonstrate competence at every level: guards, supervisors, management and office/support staff. Connect investment in resources and processes to dependable delivery for customers.

Tone: friendly, confident, measured, solemn and reassuring. Avoid flamboyance, arrogance and unsupported superlatives. Premier-provider positioning should be earned through evidence.

Protection philosophy: proactive deterrence, a reassuring visible presence, vigilant personnel, connected security technology, coordinated response and professional incident resolution.

Use 2001 as the establishment/professional operations date. Preferred wording: "Providing professional security solutions since 2001."

## Page map and navigation

Main navigation: **HOME | OUR SOLUTIONS | WHO WE SERVE | COMPANY | CONTACT US**.

Place **REQUEST FOR QUOTE** at the far right as the prominent CTA.

Agreed two-tier header: upper white row with logo, tagline "For all your corporate & private security needs" beside it, and hotlines `0722 535066 / 0734 535066` plus `info@winstarsecurity.co.ke` at the far right. Telephone and email links are clickable. Navigation sits in a separate row below. On mobile, contacts wrap beneath the logo/tagline above the compact menu row.

- Services: mega menu.
- Sectors: mega menu, retained as a top-level item.
- Company: dropdown; detailed layout to be determined.
- Careers: excluded from current scope.

Planned pages:
- Home.
- Services overview and ten individual service pages, allocated below.
- Sectors overview and six individual sector pages; depth to reflect available substantive content.
- Company/About Winstar.
- Social Responsibility, pending actual initiative content and evidence.
- Policies & Commitments.
- Contact Us.
- Data Protection Policy, Privacy Notice and Terms of Use, linked in the footer.

Company navigation should include About Winstar, Social Responsibility and Policies & Commitments, subject to content readiness.

### Service scope

Manned Guarding; CCTV Security; Access Control (including bollards, turnstiles, barriers and card/biometric access); Alarm Monitoring & Response; Electric Fencing; Canine Security; Event Security; Security Escort (VIP and cargo); Aviation Security; Facility Management.

Agreed Services mega menu:
- **Manned Security:** Manned Guarding; Canine Security; Event Security; VIP & Cargo Escorts; Aviation Security.
- **Electronic Security:** CCTV Cameras & Surveillance; Biometric & Card-Based Access; Security Alarm Systems (installation, monitoring and response).
- **Access Control:** one page covering turnstiles, bollards, vehicle barriers and related equipment; Electric Fencing as a separate page linked in this column.
- No featured strip beneath the columns. Aviation Security and Electric Fencing retain their individual pages.

Control-room support is explained within relevant services and capacity content. No separate category pages are needed initially. Facility Management remains conditional and is not scaffolded yet.

### Scaffolded page files

- Home: `index.html`.
- Services overview: `services.html`.
- Individual services: `manned-guarding.html`, `canine-security.html`, `event-security.html`, `vip-cargo-escorts.html`, `cctv-surveillance.html`, `biometric-card-access.html`, `security-alarm-systems.html`, `access-control.html`, `electric-fencing.html`, `aviation-security.html`.
- Sectors overview: `sectors.html`.
- Individual sectors: `banking-financial.html`, `hotel-recreation.html`, `real-estate-domestic.html`, `education.html`, `aviation-travel.html`, `logistics-warehousing.html`.
- Company: `about_us.html`, `social-responsibility.html`, `policies-commitments.html`.
- Contact: `contact_us.html`; the quote CTA will use the contact enquiry route, with details to be agreed.
- Footer policies: `data-protection-policy.html`, `privacy-notice.html`, `terms-of-use.html`.

These 26 files are structural shells, not completed page content. Social Responsibility remains dependent on supplied initiatives. The pre-existing empty `careers.html` is excluded from the site map and navigation.

### Sectors

- Banking & Financial.
- Hotel & Recreation.
- Real Estate & Domestic.
- Education.
- Aviation & Travel.
- Logistics & Warehousing.

Service pages explain solutions and delivery. Sector pages explain the environment's needs and the relevant combination of solutions.

## Agreed homepage structure

1. **Navigation:** shared site navigation with Services and Sectors mega menus, Company dropdown and far-right Request for Quote CTA.
2. **Three-slide jumbotron/hero:** Main Introduction; Capacity; Differentiator.
3. **Services overview:** a large heading on the left with a short overview paragraph and Services CTA on the right; no image for now. Do not use a full service list or service-card catalogue here.
4. **Experience & Sector Expertise:** experience since 2001, breadth of sector work and relevance to different customer environments, with a CTA to Sectors. This is the agreed replacement for "Experience & Service Diversity."
5. **Client logos slider/marquee:** approved existing-client logos.
6. **Footer:** content and layout to be determined; include Data Protection Policy, Privacy Notice and Terms of Use links.

The section order above follows the agreed broad outline. Detailed copy, imagery and layout remain to be developed.

### Hero slide purposes

Homepage hero implemented with the agreed first title "For all your corporate & Private Security needs" and a Services CTA. Slide 2 links to Sectors; slide 3 links to About Winstar. Local Unsplash images are temporary illustrative placeholders (sources recorded in `static/images/slider/SOURCES.md`), not evidence of Winstar assignments. Controls include previous/next, slide selectors and pause/play. Automatic rotation uses seven-second intervals, pauses on hover/focus and respects reduced-motion preferences. Shared assets: `static/home.css` and `static/home.js`; markup helper: `src/apply_home_hero.py`. Visual review and final copy/image approval remain pending.

- **Main Introduction:** establish who Winstar is and whom it protects.
- **Capacity:** show the people, management, operational systems and resources supporting delivery.
- **Differentiator:** explain Winstar's approach through supported practices, without inventing claims of uniqueness.

Keep essential messages available beyond the carousel. Provide visible controls, readable text and restrained transitions. Slide copy, photography and CTAs remain to be agreed.

### Proposed addition awaiting decision

A short closing enquiry section before the footer was recommended, but has not been explicitly agreed. Do not treat it as required scope yet.

## Policies and responsibility content

Use one Policies & Commitments page with concise web summaries:
- Ethical Business Conduct: anti-corruption and bribery.
- Human Rights & Workplace Respect: human rights/labour and sexual harassment.
- Health & Safety.
- Service Quality & Continuity: customer service and business continuity.

No policy downloads or document links at launch. Expanded content and professionally designed documents may be introduced later. Summaries must reflect supplied policies without inventing commitments.

CSR content should describe actual initiatives and evidence; internal policies alone do not establish a community programme.

Footer pages have separate roles:
- **Data Protection Policy:** broader organisational handling of personal data; draft around actual practices and obtain management approval.
- **Privacy Notice:** website collection, purposes, handling and visitor rights, reflecting the implemented forms and tools.
- **Terms of Use:** conditions for use of the website and its content.

The user confirms possession of a valid Data Processor Certificate. The website can describe ODPC data-processor registration; publishing the registration number is not required for the agreed presentation. Do not imply controller registration or broader certification from this credential.

## Content inventory and evidence

Available sources:
- `sources/Winstar Profile.pdf` and `review/profile-extracted.txt`: company background, operational practices, service descriptions, offices and client marks.
- `sources/Notebook 260126.pdf` and related review extractions/images: brand expression, service emphasis, photography, facts and client marks.
- `sources/winstar security policies/`: six signed policy/continuity documents reviewed for web summaries.
- `inspiration websites.txt`: protection philosophy and competitor references.
- Existing review briefs and proposal documents: supporting context; current agreed decisions supersede older scope and wording.

Detailed page-by-page inventory remains to be developed. Record available copy, imagery, evidence and missing inputs as each page is outlined.

Pending confirmations/material:
- Current workforce, instructor and office counts; approved core values.
- Current office/contact details. Policy letterheads and notebook support Liberty Plaza, 4th Floor, Mombasa Road for Nairobi; older profile gives Panesar Building.
- Current service scope and service-specific coverage.
- Current credentials other than the user-confirmed valid Data Processor Certificate.
- Approved client selection and permission to display marks.
- Original logo and operational photography; evidence supporting capacity claims.
- CSR initiatives and supporting material.
- Appropriate support, complaints and reporting contacts.
- Actual data practices and website tools for the privacy content.

Archived old website: supplied Wayback snapshot could not be loaded through research/browser attempts; its visual/navigation review is outstanding. Competitor content provides context, not a mandatory visual direction.

### Client list supplied for later sector research

Mt Kenya University; Chai Trading Sacco; Burger King; Finlays; Nas Servair; Sidian Bank; Unigroup Transporters; Englishpoint Marina; NICT (Nairobi Inland Cargo Terminal); SMEP; Prima Bank (the local client file says Prime Bank); Syokimau ICD; Diamonds Leisure Beach & Golf Resort; Jumuia Resorts; Almanara Luxury Boutique Hotel & Villas; Nyali Golf & Country Club; Nyali Golf View Residences.

Research typical security needs to enrich sector content without implying unconfirmed Winstar assignments. Reconcile Chai Trading Sacco versus Chai Trading Ltd and Prima versus Prime Bank before publication. Obtain approved logo selection/assets.

## Design direction

Target: modern, corporate, clean and reassuring.

Existing material suggests navy, red, blue/light blue and white. Exact colour specifications, typography, spacing, image treatment and responsive layouts remain to be determined from brand assets and design work.

Supplied palette (`sources/brand-colours.jpg`): slate `#39375b`, navy `#191c66`, blue `#1780b8`, light blue `#95d6e2`, red `#ec1e24`. Original `winstar-logo.svg` and `favicon.svg` are used without recolouring. Navigation uses a white surface, navy text, blue menu accents and a red quote CTA.

Shared navigation is implemented across all 26 pages. Our Solutions and Who we serve use full-width expandable mega menus at every breakpoint. Company is a compact dropdown at 640px and above, full-width below 640px. All panels use an almost-white `#fafafa` background without shadows or thick blue top borders. The desktop navigation remains white with a square red quote CTA; the red-bar experiment was reverted.

On screens up to 1050px, an icon-only, borderless hamburger sits beside the logo at the right. Phone numbers and email are shown within the expanded menu rather than the brand row. Menu panels use a 160ms fade with 6px downward movement, triggered synchronously when opened and disabled for reduced motion. Menus support keyboard activation, Escape dismissal, and outside-click dismissal.

Solution columns have rounded image placeholders (120px high, maximum width 320px). Sectors have 52px square icon placeholders beside their title and description. Hover titles and arrow icons use Winstar red; sector descriptions retain their colour. Service text indents on hover; sector text remains stationary with an 8px title-to-arrow gap. Panel introductory headings use 18px semibold, Explore links 13px bold, and service links 13px with compact row spacing.

Shared assets are `static/navigation.css` and `static/navigation.js`; `src/apply_navigation.py` reapplies markup consistently. The quote CTA currently leads to Contact Us with `?enquiry=quote`; form handling is still pending. Nunito Sans is the current font throughout; the Integral CF phone-number trial was removed.

Prioritise real Winstar people and operations. Use clear hierarchy, readable text and restrained brand motifs. Ensure responsive navigation, keyboard access and accessible carousel behaviour.

## Delivery sequence

1. Maintain this blueprint and refine the page map.
2. Scaffold individual HTML pages and shared styles.
3. Build shared navigation, mega menus, mobile navigation and footer; apply consistently across pages.
4. Refine homepage content and build the homepage.
5. Use its established direction to outline and develop the remaining pages.
6. Verify content, responsive behaviour, accessibility and enquiry functionality before launch.

Detailed page outlines, content inventory and design decisions will be added progressively. Use `checklist.md` to track completed work rather than marking discussion as implementation.

### Typography trial

Nunito Sans from Google Fonts is the main font under evaluation. Weights: 400 body, 600 supporting emphasis, 700/800 navigation and headings. No separate title font selected. Arial is the fallback.

Navigation labels updated: Services is displayed as Our Solutions; Sectors as Who we serve. Existing page paths and groupings are unchanged.

Header refinement: omit tagline from the header, use a smaller logo (110px desktop, 95px mobile) and 20px top/bottom padding. Hotlines and email remain. The brand tagline itself is unchanged.

## Current milestone and next step

Header and navigation are accepted as the working baseline. Refine them as needed during the rest of the build. The shared footer is the next implementation item: agree its content and layout, build it responsively and apply it across all pages before moving on to the homepage body.

Shared footer now implemented across all 26 pages: navy background, white logo copy (`static/images/winstar-logo-white.svg`), Winstar introduction and tagline, selected solution links, company links, phone/email contacts and the supplied Mombasa/Nairobi office details. Lower strip contains copyright and the three footer policy links. Responsive layout moves from four columns to two, with introduction and contacts spanning the width on small screens. Original logo remains unchanged. Styles: `static/footer.css`; shared markup application: `src/apply_footer.py`. Browser visual review and final content approval remain pending. Next substantive page work is the homepage body.

Homepage refinement: sector introduction is centered on a solid almost-white background. Its client-name marquee sits directly underneath inside the same panel, using the 16 names from winstar_clients.txt as logo placeholders. The navy image treatment and sector tiles were removed. Marquee scrolls continuously, pauses on hover/focus and becomes manually scrollable for reduced-motion preferences. Logo approval and entity-name reconciliation remain pending.


## Our Solutions overview — rough-out, 16 October 2026

Current work moves from the implemented homepage to `services.html`. The overview introduces the combined offer, presents three photo-led service groups with links to all ten individual services, answers four general buying questions and closes with a Request a Quote CTA. Existing slider photographs are temporary layout assets, not representations of Winstar personnel or installations; replace with relevant photography before final approval.

Group allocations follow the current navigation: Aviation Security is under Manned Security; Electric Fencing is under Access Control. Electronic Security includes CCTV, biometric/card access and alarm systems. The overview does not introduce additional service pages or change navigation.

FAQ approach: keep broad selection, combining services, access-control distinctions and quote-preparation questions on the overview. Individual pages can answer focused questions about deployment, installation, operation and maintenance where useful and factually supported. Confirm Winstar-specific commitments before publishing; avoid invented response times, pricing, coverage or guarantees. Draft answers are for review.

Next detailed page: Manned Guarding, establishing a reusable service-page structure. Review this overview before extending it.


## International research and proposed design philosophy — 16 October 2026

See [international design research](review/international-design-research.md) for source comparisons, inspected screenshots, proposed page families, visual rules, photography brief and FAQ policy. This is a recommendation for review, not automatic approval of every proposed detail.

Working principle: visible competence, clearly explained. Services describe scope and delivery; sector pages explain operating needs; Company substantiates organisational capacity. Prefer useful photography, restrained typography, consistent spacing and evidence near relevant claims. Retain the existing three service groups, header, footer and accepted homepage direction. General FAQs belong on the overview; specific practical questions belong on applicable service pages.

Current implementation supersedes earlier design-history notes: Lab Grotesque is the body family, Integral CF remains a homepage accent, menu panels are solid desaturated navy/slate #39375b, and header contact details are removed. The shared footer and homepage are built drafts. Our Solutions is roughed out. Next proposed build is Manned Guarding to establish a reusable detailed-page template.


## Research applied to service pages — 16 October 2026

Our Solutions now has an explicit page title and breadcrumb, three photographic groups using images from Winstar’s supplied profile, a contrasting panel explaining the relationship between security layers, general FAQs and an enquiry CTA. Existing groupings and all ten service links remain.

Manned Guarding is the first detailed-page draft: introduction and photograph, section links, duties, delivery support, selected sectors, five specific FAQs, complementary services and enquiry. It shares `static/services.css` with the overview. Source for vetting, training, supervisory checks, control-room communication and written reporting: profile PDF page 6; account management: page 4; training/vetting also supported by notebook extraction page 4. Since 2001 follows the user’s confirmed professional operating date. Avoid stale headcounts, precise response-time guarantees and unverified performance claims.

Photographs are extracted from profile PDF pages 6, 11 and 13; provenance is recorded in `static/images/services/sources.md`. All remain subject to final publication review. No invented customer evidence is added.

Homepage judgement: retain the established structure and design. The immediate priority is reviewing this service-page template, followed by consistent rollout. Later homepage improvements should prioritise authentic service photography and verified testimonials over structural redesign. Browser visual review remains pending because local-file preview was blocked; local link, asset, heading and fragment checks passed.
