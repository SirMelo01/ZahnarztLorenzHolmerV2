from django.conf import settings
from django.shortcuts import render
from django.utils.translation import activate, get_language_from_request

from yoolink.forms import ContactForm
from yoolink.ycms.applications.content.models import (
    ImpressumBlock,
    PrivacyPolicy,
    TextContent,
)
from yoolink.ycms.models import (
    Blog,
    FAQ,
    Galerie,
    OpeningHours,
    TeamMember,
    WebsiteSettings,
    fileentry,
)


def _get_text(name):
    return TextContent.objects.filter(name=name).first()


def _get_image(place):
    return fileentry.objects.filter(place=place).first()


def _google_maps_query():
    """Suchbegriff fuer den Maps-Embed (place-Modus): Praxisname + Anschrift."""
    owner = WebsiteSettings.get_solo()
    parts = [owner.company_name or owner.owner_name, owner.address]
    query = ", ".join(part.strip() for part in parts if part and part.strip())
    return query or "Zahnarztpraxis Dr. Lorenz Holmer, Deggendorfer Str. 50A, 94447 Plattling"


def get_opening_hours():
    website_settings = WebsiteSettings.get_solo()
    context = {
        "owner_data": website_settings,
        "website_settings": website_settings,
    }
    days = [
        ("MON", "opening_day_monday"),
        ("TUE", "opening_day_tuesday"),
        ("WED", "opening_day_wednesday"),
        ("THU", "opening_day_thursday"),
        ("FRI", "opening_day_friday"),
        ("SAT", "opening_day_saturday"),
        ("SUN", "opening_day_sunday"),
    ]

    opening_hours_rows = []
    for day, label_key in days:
        opening_hour = OpeningHours.objects.filter(
            website=website_settings,
            day=day,
        ).first()
        context[f"opening_{day.lower()}"] = opening_hour

        periods = []
        if opening_hour:
            periods = [
                f"{start.strftime('%H:%M')} - {end.strftime('%H:%M')}"
                for start, end in opening_hour.calculate_opening_periods()
            ]

        opening_hours_rows.append(
            {
                "day": day,
                "label_key": label_key,
                "is_open": bool(opening_hour and opening_hour.is_open),
                "periods": periods,
            }
        )

    context["opening_hours_rows"] = opening_hours_rows
    context["has_opening_hours"] = any(row["is_open"] for row in opening_hours_rows)
    context["footerText"] = _get_text("footer")
    return context


def load_index(request):
    context = {
        "FAQ": FAQ.objects.all(),
        "form": ContactForm(),
        "google_maps_embed_api_key": settings.GOOGLE_MAPS_EMBED_API_KEY,
        "google_maps_query": _google_maps_query(),
        "service_range": range(1, 8),
    }

    context["heroText"] = _get_text("main_hero")
    context["serviceText"] = _get_text("main_service")
    context["teamText"] = _get_text("main_team")
    context["homeBlogText"] = _get_text("main_blog")
    context["contactText"] = _get_text("main_contact")
    context["faqText"] = _get_text("main_faq")
    context["praxisText"] = _get_text("main_praxis")
    context["heroImage"] = _get_image("main_hero")
    if context["praxisText"]:
        context["hasPraxisText"] = True
        context["praxisTitle"] = context["praxisText"].title
        context["praxisBeschreibung"] = context["praxisText"].description

    services = []
    before_after_services = {3, 4, 6}
    for index in range(1, 8):
        services.append(
            {
                "index": index,
                "single_image_only": index not in before_after_services,
                "text": _get_text(f"main_service_{index}"),
                "prev_image": _get_image(f"main_service_{index}_prev"),
                "after_image": (
                    _get_image(f"main_service_{index}_after")
                    if index in before_after_services
                    else None
                ),
                "icon": _get_image(f"main_service_{index}_icon"),
            }
        )
    context["services"] = services

    praxis_galerie = Galerie.objects.filter(place="main_praxis", active=True).first()
    if praxis_galerie:
        context["teamGalery"] = praxis_galerie.images.all()
        context["praxisTitle"] = context["praxisText"].title if context["praxisText"] else praxis_galerie.title
        context["praxisBeschreibung"] = (
            context["praxisText"].description if context["praxisText"] else praxis_galerie.description
        )

    context["teamMembers"] = TeamMember.objects.filter(active=True)
    context["latestBlogs"] = Blog.objects.filter(original__isnull=True, active=True).order_by("-date", "-id")[:3]
    context.update(get_opening_hours())
    return render(request, "pages/index.html", context=context)


def impressum_view(request):
    owner_data = WebsiteSettings.get_site_owner()
    blocks = []
    for block in ImpressumBlock.objects.filter(active=True):
        blocks.append({"title": block.title, "html": block.render_html(owner_data)})

    context = {
        "owner_data": owner_data,
        "impressum_blocks": blocks,
    }
    context.update(get_opening_hours())
    return render(request, "pages/impressum.html", context)


def datenschutz_view(request):
    activate(get_language_from_request(request))
    owner_data = WebsiteSettings.get_site_owner()
    policy = PrivacyPolicy.objects.first()
    privacy_content_html = ""
    use_policy = policy is not None

    if policy:
        if policy.use_html and policy.content_html.strip():
            privacy_content_html = policy.render_content(owner_data)
        elif policy.content_text.strip():
            privacy_content_html = policy.render_content(owner_data)

    context = {
        "privacy_content_html": privacy_content_html,
        "use_policy": use_policy,
        "owner_data": owner_data,
    }
    context.update(get_opening_hours())
    return render(request, "pages/datenschutz.html", context)


def cookies_view(request):
    context = {
        "textContent_hero": _get_text("main_cookies_hero"),
        "textContent_necessary": _get_text("main_cookies_necessary"),
        "textContent_analytics": _get_text("main_cookies_analytics"),
        "textContent_external": _get_text("main_cookies_external"),
        "textContent_actions": _get_text("main_cookies_actions"),
        "textContent_hinweis": _get_text("main_cookies_hinweis"),
    }
    context.update(get_opening_hours())
    return render(request, "pages/cookies.html", context=context)
