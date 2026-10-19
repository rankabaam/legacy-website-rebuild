import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.hrefs = []
    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if attributes.get("id"):
            self.ids.add(attributes["id"])
        if tag == "a":
            self.hrefs.append(attributes.get("href", ""))


class PortfolioPageTests(unittest.TestCase):
    def test_language_school_internal_navigation(self):
        text = (ROOT / "samples/community_hangul_program.html").read_text(encoding="utf-8")
        page = Parser()
        page.feed(text)
        self.assertTrue({"intro", "curriculum", "term", "gallery", "contact"}.issubset(page.ids))
        self.assertTrue(all(h.startswith("#") for h in page.hrefs))
        self.assertTrue(all(h[1:] in page.ids for h in page.hrefs))
        self.assertIn("@media", text)
        self.assertIn("포트폴리오 데모", text)

    def test_no_external_registration_or_scripts(self):
        text = (ROOT / "samples/community_hangul_program.html").read_text(encoding="utf-8")
        self.assertNotIn("<script", text.lower())
        self.assertNotIn("https://", text)
        self.assertNotIn("mailto:", text)

    def test_recent_sermon_mock_is_static(self):
        text = (ROOT / "samples/sample_recent_sermons.html").read_text(encoding="utf-8")
        self.assertIn("fictional", text.lower())
        self.assertIn("Query Loop", text)
        self.assertNotIn("<script", text.lower())


if __name__ == "__main__":
    unittest.main()
