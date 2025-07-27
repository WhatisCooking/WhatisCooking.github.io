
## Workflow Overview

This project is a server-rendered web application for launching and managing Meta ad campaigns, with A/B testing for account signup pages. The workflow is as follows:

1. **Create Account (A/B Test)**
   - Users visit either version A or B of the signup page.
   - Page visits and registrations are tracked via backend endpoints.
   - After registration, users proceed to the next step.

2. **Enter Product URL**
   - Users submit their product URL for analysis.

3. **Analyze Product**
   - The system displays (or auto-analyzes) product value propositions, target audience, and competitors.

4. **Set Targeting Criteria**
   - Users set countries and daily budget for their campaign.

5. **Generate Creative Variants**
   - Users specify the number of creative variants to generate.

6. **Draft Media Plan**
   - Users design ad sets, A/B test structure, and campaign timeline.

7. **Review & Launch**
   - Users review the plan and launch the campaign.

8. **Monitor & Iterate**
   - Users monitor campaign performance and iterate (adjust budget, test structure) until the campaign ends.

## Data Collection & A/B Testing

- The backend (Flask) records page visits and registration completions, including which version of the signup page was used.
- All workflow pages are rendered via Flask templates in the `templates` folder.
- Visit and registration events are tracked via `/api/visit` and `/api/create-account` endpoints.
- Statistics and user events can be viewed at `/api/stats`.

## How to Run

1. Install Python and Flask.
2. Run `app.py`.
3. Access the workflow pages via Flask routes (e.g., `/create-account`, `/create-account-b`, etc.).
4. All templates are in the `templates` folder.

## SEO & Best Practices

- **Meta Tags**: Each HTML template should include relevant meta tags for title, description, keywords, and viewport. Example:
  ```html
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Launch and manage Meta ad campaigns with smart targeting and creative generation.">
    <meta name="keywords" content="Meta ads, campaign, creative, targeting, A/B test, marketing">
    <title>Page Title</title>
    <!-- ...other tags... -->
  </head>
  ```

- **Semantic HTML**: Use semantic tags such as `<header>`, `<main>`, `<section>`, `<nav>`, `<footer>`, `<form>`, `<h1>`-`<h3>`, `<ul>`, `<li>`, etc. This improves accessibility and SEO.

- **Image Optimization**:
  - Use descriptive `alt` attributes for all images.
  - Compress images before uploading.
  - Use modern formats (WebP, SVG) where possible.
  - Set appropriate width/height and use responsive images (`srcset`).

- **Performance**:
  - Minimize CSS and JS.
  - Use lazy loading for images (`loading="lazy"`).
  - Avoid inline styles for large CSS blocks.

- **Accessibility**:
  - Ensure good color contrast.
  - Use labels for form fields.
  - Make navigation keyboard-accessible.

For more details, see [MDN HTML SEO Guide](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta) and [Google SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).
