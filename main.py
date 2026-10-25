"""
main.py
Entry point for the Kingdom InfoTech app.

Run with:
    flet run main.py          (desktop window)
    flet run main.py --web    (opens in the browser)

Layout: a gold-on-black NavigationRail on the left switches between
six pages. Only the content area is swapped — the rail and logo
stay fixed.
"""

import flet as ft

import theme as th
import content as c
from pages import home_page, why_us_page, services_page, market_page, growth_page, impact_page, contact_page


NAV_ITEMS = [
    (ft.Icons.HOME_ROUNDED, "Home"),
    (ft.Icons.EMOJI_OBJECTS_OUTLINED, "Why Us"),
    (ft.Icons.MEMORY, "Services"),
    (ft.Icons.PUBLIC, "Market"),
    (ft.Icons.TRENDING_UP, "Growth"),
    (ft.Icons.HANDSHAKE, "Impact"),
    (ft.Icons.MAIL_OUTLINE, "Contact"),
]


def main(page: ft.Page):
    # --- Window / page setup ---------------------------------------
    page.title = f"{c.COMPANY} | {c.SLOGAN}"
    page.theme_mode = ft.ThemeMode.DARK
    page.theme = th.build_theme()
    page.bgcolor = th.BLACK
    page.fonts = th.GOOGLE_FONTS
    page.padding = 0
    page.window.width = 1200
    page.window.height = 800
    page.window.min_width = 920
    page.window.min_height = 640

    content_area = ft.Container(expand=True, padding=th.PAGE_PADDING)

    def handle_form_submit(name_f, contact_f, type_f, msg_f, status_t, pg):
        """Validates and 'submits' the enquiry form."""
        if not name_f.value or not contact_f.value:
            status_t.value = "Please provide your name and a way to reach you."
            status_t.color = "#E57373"
        else:
            status_t.value = f"Thank you, {name_f.value}. Your enquiry has been received — we'll be in touch."
            status_t.color = th.GOLD
            name_f.value = contact_f.value = msg_f.value = ""
            type_f.value = None
        pg.update()

    def render(index: int):
        pages = {
            0: lambda: home_page(page),
            1: lambda: why_us_page(page),
            2: lambda: services_page(page),
            3: lambda: market_page(page),
            4: lambda: growth_page(page),
            5: lambda: impact_page(page),
            6: lambda: contact_page(page, handle_form_submit),
        }
        content_area.content = pages[index]()
        page.update()

    def on_nav_change(e: ft.ControlEvent):
        render(e.control.selected_index)

    # --- Left navigation rail, with the crest logo above it ----------
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=90,
        min_extended_width=200,
        bgcolor=th.CHARCOAL,
        indicator_color=th.GOLD_DARK,
        destinations=[
            ft.NavigationRailDestination(icon=icon, label=label) for icon, label in NAV_ITEMS
        ],
        on_change=on_nav_change,
    )

    rail_column = ft.Column(
        [
            ft.Container(
                content=ft.Image(src="logo.png", width=56, height=56, fit=ft.ImageFit.CONTAIN),
                padding=ft.padding.only(top=18, bottom=6),
                alignment=ft.alignment.center,
            ),
            rail,
        ],
        spacing=0,
    )

    layout = ft.Row(
        [
            rail_column,
            ft.VerticalDivider(width=1, color=th.GOLD_DARK),
            content_area,
        ],
        expand=True,
        spacing=0,
    )

    page.add(layout)
    render(0)


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
