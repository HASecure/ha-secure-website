from __future__ import annotations
import tempfile
import unittest
from pathlib import Path
from scripts.validate_site import SiteParser
class WebsitePolicyTests(unittest.TestCase):
    def test_parser_collects_links_and_icons(self):
        parser=SiteParser()
        parser.feed('<a href="about.html">About</a><link rel="icon" href="icon.png">')
        self.assertEqual(parser.refs,[("link","about.html"),("icon","icon.png")])
if __name__=="__main__": unittest.main()
