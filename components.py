"""
components.py
Small, reusable visual pieces. Pages import these instead of
re-building the same card / chip / header layouts on every screen.
"""

import flet as ft
import theme as th


def gold_card(content: ft.Control, width: int = None) -> ft.Container:
    """Dark card with a soft gold border — the base unit of the whole UI."""
    return ft.Container(
        content=content,
        width=width,
        padding=th.CARD_PADDING,
        border_radius=th.RADIUS,
        bgcolor=th.CARD_BG,
        border=ft.border.all(1, th.GOLD_DARK),
        shadow=ft.BoxShadow(
            blur_radius=18,
            color=ft.Colors.with_opacity(0.35, ft.Colors.BLACK),
            offset=ft.Offset(0, 6),
        ),
        animate=ft.Animation(250, ft.AnimationCurve.EASE_OUT),
    )


def bullet_list(items: list[str]) -> ft.Column:
    """A column of bullet points styled with a small gold dot."""
    rows = []
    for item in items:
        rows.append(
            ft.Row(
                [
                    ft.Container(width=6, height=6, border_radius=3, bgcolor=th.GOLD, margin=ft.margin.only(top=7)),
                    ft.Text(item, color=th.MUTED_WHITE, size=13.5, expand=True),
                ],
                spacing=10,
                vertical_alignment=ft.CrossAxisAlignment.START,
            )
        )
    return ft.Column(rows, spacing=7)


def service_card(icon: str, title: str, items: list[str], width: int = 300) -> ft.Container:
    """A titled card listing a group of services, used on the Services page."""
    return gold_card(
        ft.Column(
            [
                ft.Row([ft.Icon(icon, color=th.GOLD, size=22), ft.Text(title, font_family=th.FONT_HEADING,
                        size=17, weight=ft.FontWeight.BOLD, color=th.OFF_WHITE, expand=True)], spacing=10),
                ft.Divider(height=14, color="transparent"),
                bullet_list(items),
            ],
            tight=True,
        ),
        width=width,
    )


def chip(label: str) -> ft.Container:
    """Small rounded gold chip used for market segments, partners, values."""
    return ft.Container(
        content=ft.Text(label, size=12.5, color=th.BLACK, weight=ft.FontWeight.W_600),
        bgcolor=th.GOLD,
        padding=ft.padding.symmetric(horizontal=13, vertical=7),
        border_radius=18,
    )


def outline_chip(label: str) -> ft.Container:
    """A lighter, outlined chip — used as a secondary/visual variant of `chip`."""
    return ft.Container(
        content=ft.Text(label, size=12.5, color=th.GOLD_LIGHT),
        border=ft.border.all(1, th.GOLD_DARK),
        padding=ft.padding.symmetric(horizontal=13, vertical=7),
        border_radius=18,
    )


def stat_card(number: str, label: str) -> ft.Container:
    """A big-number highlight card, used for the three-year goals / impact strip."""
    return gold_card(
        ft.Column(
            [
                ft.Text(number, font_family=th.FONT_HEADING, size=26, weight=ft.FontWeight.BOLD, color=th.GOLD),
                ft.Text(label, size=12, color=th.MUTED_WHITE, text_align=ft.TextAlign.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=4,
            tight=True,
        ),
        width=160,
    )


def quote_banner(text: str, attribution: str = None) -> ft.Container:
    """A centred, italicised highlight banner — used for the slogan / mission quotes."""
    controls = [
        ft.Text(f"\u201c{text}\u201d", font_family=th.FONT_HEADING, italic=True, size=18,
                color=th.GOLD_LIGHT, text_align=ft.TextAlign.CENTER)
    ]
    if attribution:
        controls.append(ft.Text(f"— {attribution}", size=12, color=th.MUTED_WHITE, text_align=ft.TextAlign.CENTER))
    return ft.Container(
        content=ft.Column(controls, horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=6),
        padding=22,
        border_radius=th.RADIUS,
        bgcolor=th.CHARCOAL,
        border=ft.border.all(1, th.GOLD_DARK),
        alignment=ft.alignment.center,
    )


def page_header(title: str, subtitle: str) -> ft.Column:
    """Standard header block (title + subtitle + gold rule) used atop every page."""
    return ft.Column(
        [
            ft.Text(title, font_family=th.FONT_HEADING, size=30, weight=ft.FontWeight.BOLD, color=th.OFF_WHITE),
            ft.Text(subtitle, size=14, color=th.MUTED_WHITE),
            th.divider(),
        ],
        spacing=4,
    )
