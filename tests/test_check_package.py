#!/usr/bin/env python3
"""Regression tests for the optional lint tool, not tests of model quality."""
import tempfile
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_package import check


class LintTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / 'PROFILE-README.md').write_text('# Noor\n\nA text utility.\n', encoding='utf-8')
        (self.root / 'PROFILE-PLAN.md').write_text('Draft. Sources checked separately.', encoding='utf-8')

    def tearDown(self):
        self.tmp.cleanup()

    def put(self, text):
        (self.root / 'PROFILE-README.md').write_text(text, encoding='utf-8')

    def test_valid_minimal(self):
        self.assertTrue(check(self.root)['passed'])

    def test_missing_plan(self):
        (self.root / 'PROFILE-PLAN.md').unlink()
        self.assertFalse(check(self.root)['passed'])

    def test_empty_readme(self):
        self.put('  \n')
        self.assertFalse(check(self.root)['passed'])

    def test_placeholder(self):
        self.put('# YOUR_USERNAME\n')
        self.assertFalse(check(self.root)['passed'])

    def test_script(self):
        self.put('<script>alert(1)</script>')
        self.assertFalse(check(self.root)['passed'])

    def test_iframe(self):
        self.put('<iframe src="example"></iframe>')
        self.assertFalse(check(self.root)['passed'])

    def test_missing_alt(self):
        self.put('![](asset.svg)')
        self.assertFalse(check(self.root)['passed'])

    def test_empty_link(self):
        self.put('[Open]()')
        self.assertFalse(check(self.root)['passed'])

    def test_arabic_plain_text(self):
        self.put('# نور\n\nأدوات صغيرة لسطر الأوامر.\n')
        self.assertTrue(check(self.root)['passed'])

    def test_does_not_pretend_fact_checking(self):
        self.put('# Invented\nUsed by a billion people.')
        self.assertTrue(check(self.root)['passed'])
        self.assertIn('facts', check(self.root)['scope'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
