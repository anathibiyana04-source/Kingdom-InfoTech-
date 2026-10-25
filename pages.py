"""
pages.py
One function per screen. Each returns a scrollable ft.Column — main.py
swaps these into the content area when the nav rail selection changes.
"""

import flet as ft
import theme as th
import content as c
from components import (gold_card, bullet_list, service_card, chip, outline_chip,
                         stat_card, quote_banner, page_header)


def home_page(page: ft.Page) -> ft.Column:
    hero = ft.Container(
        content=ft.Column(
            [
                ft.Image(src="logo.png", width=150, height=150, fit=ft.ImageFit.CONTAIN),
                ft.Text(c.COMPANY.upper(), font_family=th.FONT_HEADING, size=34,
                        weight=ft.FontWeight.BOLD, color=th.GOLD, text_align=ft.TextAlign.CENTER),
                ft.Text(c.STRUCTURE_NOTE, size=14, color=th.OFF_WHITE, text_align=ft.TextAlign.CENTER),
                ft.Text(f"\u201c{c.SLOGAN}\u201d", italic=True, size=14, color=th.MUTED_WHITE,
                        text_align=ft.TextAlign.CENTER),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
        ),
        padding=ft.padding.symmetric(vertical=30),
        alignment=ft.alignment.center,
        gradient=ft.LinearGradient(
            begin=ft.alignment.top_center, end=ft.alignment.bottom_center,
            colors=[th.CHARCOAL, th.BLACK],
        ),
        border_radius=th.RADIUS,
        border=ft.border.all(1, th.GOLD_DARK),
    )

    overview = gold_card(
        ft.Column(
            [
                ft.Row([ft.Icon(ft.Icons.INFO_OUTLINE, color=th.GOLD),
                        ft.Text("Business Overview", font_family=th.FONT_HEADING, size=18,
                                weight=ft.FontWeight.BOLD, color=th.OFF_WHITE)]),
                ft.Text(c.BUSINESS_OVERVIEW, color=th.MUTED_WHITE, size=14),
            ],
            tight=True,
        )
    )

    vision_mission = ft.ResponsiveRow(
        [
            ft.Container(
                gold_card(ft.Column([
                    ft.Row([ft.Icon(ft.Icons.VISIBILITY, color=th.GOLD), ft.Text("Our Vision",
                            font_family=th.FONT_HEADING, size=18, weight=ft.FontWeight.BOLD, color=th.OFF_WHITE)]),
                    ft.Text(c.VISION, color=th.MUTED_WHITE, size=14),
                ], tight=True)),
                col={"sm": 12, "md": 6},
            ),
            ft.Container(
                gold_card(ft.Column([
                    ft.Row([ft.Icon(ft.Icons.FLAG, color=th.GOLD), ft.Text("Our Mission",
                            font_family=th.FONT_HEADING, size=18, weight=ft.FontWeight.BOLD, color=th.OFF_WHITE)]),
                    ft.Text(c.MISSION, color=th.MUTED_WHITE, size=14),
                ], tight=True)),
                col={"sm": 12, "md": 6},
            ),
        ],
        spacing=20,
        run_spacing=20,
    )

    values_row = ft.Row([chip(v) for v in c.CORE_VALUES], wrap=True, spacing=8, run_spacing=8)

    return ft.Column(
        [
            hero,
            ft.Container(height=20),
            overview,
            vision_mission,
            ft.Container(height=6),
            ft.Text("Core Values", font_family=th.FONT_HEADING, size=18,
                    weight=ft.FontWeight.BOLD, color=th.OFF_WHITE),
            values_row,
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=16,
    )


def why_us_page(page: ft.Page) -> ft.Column:
    problem = gold_card(
        ft.Column(
            [
                ft.Row([ft.Icon(ft.Icons.REPORT_PROBLEM_OUTLINED, color=th.GOLD),
                        ft.Text("The Problem", font_family=th.FONT_HEADING, size=18,
                                weight=ft.FontWeight.BOLD, color=th.OFF_WHITE)]),
                ft.Text("Many entrepreneurs, startups and SMMEs possess innovative ideas but "
                        "struggle because of:", color=th.MUTED_WHITE, size=13),
                ft.Row([outline_chip(p) for p in c.PROBLEM_STATEMENT], wrap=True, spacing=8, run_spacing=8),
            ],
            tight=True,
        )
    )

    solution = gold_card(
        ft.Column(
            [
                ft.Row([ft.Icon(ft.Icons.LIGHTBULB_OUTLINE, color=th.GOLD),
                        ft.Text("Our Solution", font_family=th.FONT_HEADING, size=18,
                                weight=ft.FontWeight.BOLD, color=th.OFF_WHITE)]),
                ft.Text(c.SOLUTION, color=th.MUTED_WHITE, size=14),
            ],
            tight=True,
        )
    )

    why_card = gold_card(
        ft.Column(
            [
                ft.Text("Why Clients Choose Us", font_family=th.FONT_HEADING, size=18,
                        weight=ft.FontWeight.BOLD, color=th.OFF_WHITE),
                bullet_list(c.WHY_CHOOSE_US),
            ],
            tight=True,
        ),
        width=380,
    )

    advantage_card = gold_card(
        ft.Column(
            [
                ft.Text("Competitive Advantage", font_family=th.FONT_HEADING, size=18,
                        weight=ft.FontWeight.BOLD, color=th.OFF_WHITE),
                bullet_list(c.COMPETITIVE_ADVANTAGE),
            ],
            tight=True,
        ),
        width=380,
    )

    return ft.Column(
        [
            page_header("Why Kingdom InfoTech", "The gap we saw, and how we close it."),
            problem,
            solution,
            ft.Row([why_card, advantage_card], wrap=True, spacing=20, run_spacing=20),
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=16,
    )


def services_page(page: ft.Page) -> ft.Column:
    icons = {
        "ICT & Digital Solutions": ft.Icons.MEMORY,
        "Business Support Consultancy": ft.Icons.BUSINESS_CENTER,
        "Capacity Building": ft.Icons.SCHOOL,
    }
    cards = [service_card(icons[name], name, items) for name, items in c.SERVICE_GROUPS.items()]
    grid = ft.Row(cards, wrap=True, spacing=20, run_spacing=20)

    return ft.Column(
        [
            page_header("Our Services", "An integrated solution: technology, business development, "
                                         "and entrepreneurship support under one trusted partner."),
            grid,
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=16,
    )


def market_page(page: ft.Page) -> ft.Column:
    def segment_card(title, items):
        return gold_card(
            ft.Column(
                [
                    ft.Text(title, font_family=th.FONT_HEADING, size=16,
                            weight=ft.FontWeight.BOLD, color=th.OFF_WHITE),
                    ft.Row([chip(i) for i in items], wrap=True, spacing=8, run_spacing=8),
                ],
                tight=True, spacing=10,
            ),
        )

    segments = ft.Column(
        [
            segment_card("Primary Customers", c.PRIMARY_CUSTOMERS),
            segment_card("Secondary Customers", c.SECONDARY_CUSTOMERS),
            segment_card("Strategic Customers", c.STRATEGIC_CUSTOMERS),
        ],
        spacing=16,
    )

    channels = gold_card(
        ft.Column(
            [
                ft.Text("Channels", font_family=th.FONT_HEADING, size=18,
                        weight=ft.FontWeight.BOLD, color=th.OFF_WHITE),
                ft.Text("Digital", size=12, color=th.GOLD),
                ft.Row([outline_chip(x) for x in c.CHANNELS_DIGITAL], wrap=True, spacing=8, run_spacing=8),
                ft.Container(height=6),
                ft.Text("Community", size=12, color=th.GOLD),
                ft.Row([outline_chip(x) for x in c.CHANNELS_COMMUNITY], wrap=True, spacing=8, run_spacing=8),
            ],
            tight=True,
        )
    )

    relationships = gold_card(
        ft.Column(
            [
                ft.Text("How We Build Relationships", font_family=th.FONT_HEADING, size=18,
                        weight=ft.FontWeight.BOLD, color=th.OFF_WHITE),
                bullet_list(c.CUSTOMER_RELATIONSHIP_STRATEGY),
            ],
            tight=True,
        )
    )

    return ft.Column(
        [
            page_header("Target Market & Reach", "Who we serve, and how we stay connected to them."),
            segments,
            ft.Row([channels, relationships], wrap=True, spacing=20, run_spacing=20),
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=16,
    )


def growth_page(page: ft.Page) -> ft.Column:
    revenue_cards = [
        gold_card(
            ft.Column(
                [
                    ft.Text(group, font_family=th.FONT_HEADING, size=15,
                            weight=ft.FontWeight.BOLD, color=th.OFF_WHITE),
                    bullet_list(items),
                ],
                tight=True, spacing=8,
            ),
            width=280,
        )
        for group, items in c.REVENUE_STREAMS.items()
    ]

    partners = gold_card(
        ft.Column(
            [
                ft.Text("Strategic Partnerships", font_family=th.FONT_HEADING, size=18,
                        weight=ft.FontWeight.BOLD, color=th.OFF_WHITE),
                ft.Text("Government", size=12, color=th.GOLD),
                ft.Row([outline_chip(p) for p in c.GOVERNMENT_PARTNERS], wrap=True, spacing=8, run_spacing=8),
                ft.Container(height=6),
                ft.Text("Technology", size=12, color=th.GOLD),
                ft.Row([outline_chip(p) for p in c.TECH_PARTNERS], wrap=True, spacing=8, run_spacing=8),
                ft.Container(height=6),
                ft.Text("Community", size=12, color=th.GOLD),
                ft.Row([outline_chip(p) for p in c.COMMUNITY_PARTNERS], wrap=True, spacing=8, run_spacing=8),
            ],
            tight=True,
        )
    )

    goals_columns = []
    for year, goals in c.STRATEGIC_GOALS.items():
        goals_columns.append(
            gold_card(
                ft.Column(
                    [
                        ft.Text(year, font_family=th.FONT_HEADING, size=17,
                                weight=ft.FontWeight.BOLD, color=th.GOLD),
                        bullet_list(goals),
                    ],
                    tight=True, spacing=8,
                ),
                width=300,
            )
        )

    return ft.Column(
        [
            page_header("Revenue & Growth Strategy", "How the business sustains itself, and where it's heading."),
            ft.Row(revenue_cards, wrap=True, spacing=16, run_spacing=16),
            ft.Container(height=6),
            partners,
            ft.Text("Three-Year Strategic Goals", font_family=th.FONT_HEADING, size=20,
                    weight=ft.FontWeight.BOLD, color=th.OFF_WHITE),
            ft.Row(goals_columns, wrap=True, spacing=16, run_spacing=16),
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=16,
    )


def impact_page(page: ft.Page) -> ft.Column:
    impact_card = gold_card(
        ft.Column(
            [
                ft.Text("Social Impact", font_family=th.FONT_HEADING, size=18,
                        weight=ft.FontWeight.BOLD, color=th.OFF_WHITE),
                bullet_list(c.SOCIAL_IMPACT),
            ],
            tight=True,
        )
    )
    quote = quote_banner(c.SLOGAN)
    stats = ft.Row(
        [stat_card("1,000+", "Entrepreneurs supported by Year 3"),
         stat_card("3", "Year strategic roadmap"),
         stat_card("1", "Integrated ICT + consultancy partner")],
        wrap=True, spacing=16, run_spacing=16,
    )
    return ft.Column(
        [
            page_header("Our Impact", "Technology and enterprise development, in service of community transformation."),
            stats,
            impact_card,
            quote,
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=16,
    )


def contact_page(page: ft.Page, on_submit) -> ft.Column:
    name_field = ft.TextField(label="Full Name", border_color=th.GOLD_DARK, color=th.OFF_WHITE)
    email_field = ft.TextField(label="Email or Phone", border_color=th.GOLD_DARK, color=th.OFF_WHITE)
    service_type = ft.Dropdown(
        label="Service of Interest",
        border_color=th.GOLD_DARK,
        color=th.OFF_WHITE,
        options=[ft.dropdown.Option(name) for name in c.SERVICE_GROUPS.keys()] +
                [ft.dropdown.Option("General Enquiry")],
    )
    message_field = ft.TextField(label="Message", multiline=True, min_lines=4,
                                  border_color=th.GOLD_DARK, color=th.OFF_WHITE)
    status_text = ft.Text("", color=th.GOLD, size=13)

    def handle_submit(e):
        on_submit(name_field, email_field, service_type, message_field, status_text, page)

    submit_btn = ft.ElevatedButton(
        "Send Enquiry", icon=ft.Icons.SEND, bgcolor=th.GOLD, color=th.BLACK, on_click=handle_submit,
    )

    form = gold_card(
        ft.Column(
            [name_field, email_field, service_type, message_field, submit_btn, status_text],
            spacing=14, tight=True,
        ),
        width=420,
    )

    details = gold_card(
        ft.Column(
            [
                ft.Text(c.CONTACT["company"], font_family=th.FONT_HEADING, size=18,
                        weight=ft.FontWeight.BOLD, color=th.OFF_WHITE),
                ft.Text(c.FOUNDER, size=12, color=th.MUTED_WHITE),
                ft.Text(c.LOCATION, size=12, color=th.MUTED_WHITE),
                ft.Divider(color=th.GOLD_DARK),
                ft.Row([ft.Icon(ft.Icons.CHAT, color=th.GOLD, size=18),
                        ft.Text(c.CONTACT["whatsapp"], color=th.MUTED_WHITE, size=13)]),
                ft.Row([ft.Icon(ft.Icons.GROUPS, color=th.GOLD, size=18),
                        ft.Text("One-on-one consultations & mentorship", color=th.MUTED_WHITE, size=13)]),
            ],
            spacing=10, tight=True,
        ),
        width=420,
    )

    return ft.Column(
        [
            page_header("Get In Touch", "Let's talk about your business and technology needs."),
            ft.Row([form, details], wrap=True, spacing=20, run_spacing=20),
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=16,
    )
