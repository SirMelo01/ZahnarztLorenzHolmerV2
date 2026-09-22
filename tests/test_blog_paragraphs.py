"""Paragraphs must survive CMS saving and switches between both blog editors."""

import re

import pytest

from yoolink.ycms.applications.blog.services import (
    blog_code_to_markdown,
    build_default_code_from_html,
    build_default_code_from_markdown,
    html_to_markdown,
    render_blog_code_to_html,
    render_markdown_to_html,
)


def paragraphs(html):
    return re.findall(r"<p(?:\s[^>]*)?>(.*?)</p>", html, re.S)


@pytest.mark.parametrize(
    "source, expected",
    [
        ("<p>Erster Absatz.</p><p>Zweiter Absatz.</p>",
         ["Erster Absatz.", "Zweiter Absatz."]),
        ("<p>Erste Zeile<br>Zweite Zeile</p>",
         ["Erste Zeile<br>Zweite Zeile"]),
        ("<p>Erste Zeile<br/><br />Letzte Zeile</p>",
         ["Erste Zeile<br><br>Letzte Zeile"]),
        ("<p>Vorher</p><p><br></p><p><br></p><p>Nachher</p>",
         ["Vorher", "<br>", "<br>", "Nachher"]),
        ("<p><br></p><p>Text</p><p><br></p>",
         ["<br>", "Text", "<br>"]),
        ("<p>Vorher</p><p></p><p> </p><p>Nachher</p>",
         ["Vorher", "<br>", "<br>", "Nachher"]),
        ("<div>Alter Absatz</div><div>Zweiter Absatz</div>",
         ["Alter Absatz", "Zweiter Absatz"]),
        ("<div><p>Erster Absatz.</p><p>Zweiter Absatz.</p></div>",
         ["Erster Absatz.", "Zweiter Absatz."]),
        ("<p><strong>Fett</strong><br><em>Kursiv</em></p>",
         ["<strong>Fett</strong><br><em>Kursiv</em>"]),
    ],
)
def test_paragraphs_survive_saving_and_repeated_editor_switches(source, expected):
    code = [{"name": "textArea", "type": "div", "value": source}]
    for _ in range(3):
        markdown = blog_code_to_markdown(code)
        assert paragraphs(render_markdown_to_html(markdown)) == expected
        code = build_default_code_from_markdown(markdown)
        assert paragraphs(render_blog_code_to_html(code)) == expected


@pytest.mark.parametrize(
    "code",
    [
        build_default_code_from_html("<p>Erster</p><p>Zweiter</p>"),
        build_default_code_from_markdown("Erster\n\nZweiter"),
        [{"name": "textArea", "type": "p", "value": "<p>Erster</p><p>Zweiter</p>"}],
    ],
)
def test_text_blocks_do_not_nest_paragraphs(code):
    html = render_blog_code_to_html(code)
    assert html.startswith("<div")
    assert paragraphs(html) == ["Erster", "Zweiter"]


def test_normal_markdown_paragraphs_and_soft_wrapping_are_unchanged():
    markdown = "Ein langer\nAbsatz.\n\nEin weiterer Absatz."
    assert paragraphs(render_markdown_to_html(markdown)) == [
        "Ein langer Absatz.", "Ein weiterer Absatz.",
    ]


def test_line_breaks_do_not_change_code_blocks():
    markdown = html_to_markdown("<pre><code>eins\n\nzwei</code></pre>")
    assert re.search(r"<code[^>]*>eins\n\nzwei</code>", render_markdown_to_html(markdown))


def test_line_breaks_survive_inside_lists():
    markdown = html_to_markdown("<ul><li>Erste<br>Zweite</li><li>Dritte</li></ul>")
    assert "<li>Erste<br>Zweite</li>" in render_markdown_to_html(markdown)
