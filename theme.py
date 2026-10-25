"""
theme.py
Central place for every colour, font and spacing value used in the app.
Keeping styling here means the whole look can be changed from one file
instead of hunting through every page.
"""

import flet as ft

# --- Brand palette, taken from the Kingdom InfoTech crest (black / gold / white) ---
GOLD = "#D4AF37"
GOLD_LIGHT = "#F4E5B2"
GOLD_DARK = "#8A6E1F"
BLACK = "#0B0B0D"
CHARCOAL = "#17171B"
CARD_BG = "#1F1F24"
OFF_WHITE = "#F5F3EE"
MUTED_WHITE = "#C9C7C2"
ACCENT_BLUE = "#4FA3D9"  # used sparingly for "tech" highlights (circuitry feel)

# --- Typography ---
FONT_HEADING = "Playfair Display"
FONT_BODY = "Lato"

GOOGLE_FONTS = {
    FONT_HEADING: "https://raw.githubusercontent.com/google/fonts/main/ofl/playfairdisplay/PlayfairDisplay%5Bwght%5D.ttf",
    FONT_BODY: "https://raw.githubusercontent.com/google/fonts/main/ofl/lato/Lato-Regular.ttf",
}

# --- Reusable spacing / radius values ---
RADIUS = 18
PAGE_PADDING = 32
CARD_PADDING = 24


def build_theme() -> ft.Theme:
    """Returns the ft.Theme object applied once on app start."""
    return ft.Theme(
        font_family=FONT_BODY,
        color_scheme=ft.ColorScheme(
            primary=GOLD,
            secondary=GOLD_DARK,
            background=BLACK,
            surface=CHARCOAL,
            on_primary=BLACK,
            on_surface=OFF_WHITE,
        ),
    )


def section_title(text: str, icon: str = None) -> ft.Row:
    """A consistent gold section heading used at the top of a block of content."""
    controls = []
    if icon:
        controls.append(ft.Icon(icon, color=GOLD, size=26))
    controls.append(
        ft.Text(text, font_family=FONT_HEADING, size=22, weight=ft.FontWeight.BOLD, color=OFF_WHITE)
    )
    return ft.Row(controls, spacing=10)


def divider() -> ft.Container:
    """A slim gold rule used to separate sections."""
    return ft.Container(
        height=2,
        width=70,
        gradient=ft.LinearGradient(colors=[GOLD, "transparent"]),
        margin=ft.margin.only(top=6, bottom=18),
    )
