# Kingdom InfoTech — App

A desktop/web app for **Kingdom InfoTech (Pty Ltd)**, built with [Flet](https://flet.dev) (Python).
All content is taken directly from the supplied Business Model Canvas (Expanded) and
Business Plan (Expanded) documents -- vision, mission, services, target market,
revenue streams, partnerships, three-year goals, and social impact.

## Project structure

```
kingdom_infotech_main_app/
├── main.py           # App entry point -- window setup & navigation
├── theme.py           # Colours, fonts, spacing (the black & gold brand palette)
├── components.py       # Reusable UI pieces (cards, chips, stat cards, quote banner)
├── content.py          # All text content, sourced from the canvas & business plan
├── pages.py            # Home, Why Us, Services, Market, Growth, Impact, Contact pages
├── assets/
│   └── logo.png        # Kingdom InfoTech crest, shown on the home page & nav rail
└── requirements.txt
```

## Running it in VS Code

1. Open this folder (`kingdom_infotech_main_app`) in VS Code.
2. Open a terminal (Ctrl+`) and create a virtual environment:
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   source .venv/bin/activate
   ```
3. Install Flet:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app as a desktop window:
   ```bash
   flet run main.py
   ```
   Or run it in the browser:
   ```bash
   flet run main.py --web
   ```

## Pages

| Page | What it shows |
|---|---|
| **Home** | Crest, slogan, business overview, Vision & Mission, core values |
| **Why Us** | The problem SMMEs/startups face, our solution, why clients choose us, competitive advantage |
| **Services** | ICT & Digital Solutions, Business Support Consultancy, Capacity Building |
| **Market** | Primary / secondary / strategic customer segments, channels, relationship strategy |
| **Growth** | Revenue streams, strategic partnerships (government, tech, community), 3-year goals |
| **Impact** | Social impact commitments and the company slogan |
| **Contact** | An enquiry form plus founder & location details |

## Notes

- No funding or grant figures were added anywhere in the app -- none were supplied
  in the source documents, per instruction.
- `content.py` leaves the official **email** and **phone number** blank on purpose,
  since these weren't provided in the source documents. Fill them in in that one file
  and they'll appear across the app automatically.
- The logo is loaded from `assets/logo.png` via Flet's `assets_dir`, so it displays
  both in the desktop window and in the browser build.
