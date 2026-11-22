#!/usr/bin/env python3
"""Regression tests for the local README checker."""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import check_readme


class IndirectUrlTests(unittest.TestCase):
    def test_direct_resource_urls_with_search_or_redirect_are_allowed(self):
        urls = [
            "https://developers.google.com/search-ads/reporting",
            "https://github.com/fivetran/dbt_apple_search_ads",
            "https://example.org/redirect-checker?mode=search",
            "https://www.google.com.evil.example/search?q=ads",
        ]
        for url in urls:
            with self.subTest(url=url):
                self.assertFalse(check_readme.is_indirect_url(url))

    def test_common_search_engines_and_redirect_services_are_rejected(self):
        urls = [
            "https://www.google.com/search?q=adops",
            "https://www.google.com/url?url=https://example.org",
            "https://www.google.com/goto?url=encoded",
            "https://www.bing.com/search?q=adops",
            "https://duckduckgo.com/?q=adops",
            "https://search.yahoo.com/search?p=adops",
            "https://search.brave.com/search?q=adops",
            "https://bit.ly/example",
            "https://www.tinyurl.com/example",
            "https://l.facebook.com/l.php?u=https://example.org",
        ]
        for url in urls:
            with self.subTest(url=url):
                self.assertTrue(check_readme.is_indirect_url(url))


class ReadmeCheckerTests(unittest.TestCase):
    def run_check(self, text):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "image").mkdir()
            (root / "image" / "alg_R.png").touch()
            (root / "image" / "alg_I.png").touch()
            readme = root / "README.md"
            readme.write_text(text, encoding="utf-8")
            output = io.StringIO()
            with patch.object(check_readme, "README", readme), patch.object(
                check_readme, "ROOT", root
            ), contextlib.redirect_stdout(output):
                result = check_readme.main()
            return result, output.getvalue()

    def test_direct_links_are_checked_by_url_not_markdown_name(self):
        result, output = self.run_check(
            "## Resources\n"
            "- [Resources](#resources)\n"
            "![web](image/alg_I.png) [Search Ads 360](https://developers.google.com/search-ads/reporting) - Read-only reporting API.\n"
            "![github](image/alg_R.png) [Redirect checker](https://github.com/example/redirect-checker) - Checks advertising redirects.\n"
        )
        self.assertEqual(result, 0, output)
        self.assertIn("checked 2 entries", output)

    def test_search_results_and_shorteners_fail_end_to_end(self):
        for url in ("https://www.google.com/search?q=adops", "https://t.co/example"):
            with self.subTest(url=url):
                result, output = self.run_check(
                    "## Resources\n"
                    f"![web](image/alg_I.png) [Resource]({url}) - An advertising resource.\n"
                )
                self.assertEqual(result, 1, output)
                self.assertIn("link looks like a search/redirect service", output)

    def test_invalid_url_fails_without_crashing(self):
        result, output = self.run_check(
            "## Resources\n"
            "![web](image/alg_I.png) [Bad URL](https:///missing-host) - An advertising resource.\n"
        )
        self.assertEqual(result, 1, output)
        self.assertIn("invalid link URL", output)

    def test_icon_and_table_of_contents_checks_still_work(self):
        result, output = self.run_check(
            "## Resources\n"
            "- [Missing](#missing)\n"
            "![github](image/alg_I.png) [Example](https://github.com/example/repo) - An advertising resource.\n"
        )
        self.assertEqual(result, 1, output)
        self.assertIn("github icon must use", output)
        self.assertIn("points to missing heading anchor", output)

    def test_repeated_checks_do_not_retain_old_failures(self):
        result, output = self.run_check(
            "## Resources\n"
            "![web](image/alg_I.png) [Bad URL](https:///missing-host) - An advertising resource.\n"
        )
        self.assertEqual(result, 1, output)
        result, output = self.run_check(
            "## Resources\n"
            "![web](image/alg_I.png) [Example](https://example.org) - An advertising resource.\n"
        )
        self.assertEqual(result, 0, output)
        self.assertIn("README format check passed", output)


if __name__ == "__main__":
    unittest.main()
