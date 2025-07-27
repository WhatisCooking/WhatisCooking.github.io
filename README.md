
## Workflow Overview

This project is a server-rendered web application for launching and managing Meta ad campaigns, with A/B testing for account signup pages. 

## How to Run

1. Install Python and Flask.
2. Run `app.py`.
3. Access the workflow pages via Flask routes (e.g., `/create-account`, `/create-account-b`, etc.).
4. All templates are in the `templates` folder.

## Data Collection & A/B Testing

- Randomly and fairly assign user to A/B landing page, persist in cookie.
- The backend (Flask) records page visits and registration completions, including which version of the signup page was used.
- All workflow pages are rendered via Flask templates in the `templates` folder.
- Visit and registration events are tracked via `/api/visit` and `/api/create-account` endpoints.
- Statistics and user events can be viewed at `/api/stats`.

The workflow is as follows:

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

8. **Monitor campaign**
   - Users monitor campaign performance and iterate (adjust budget, test structure) until the campaign ends.

