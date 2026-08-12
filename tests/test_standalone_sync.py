import unittest

from test_scripts import ROOT


class StandaloneSyncTests(unittest.TestCase):
    def test_standalone_fallbacks_match_package_modules(self):
        pairs = [
            ("oraclebone/tarot.py", "skills/tarot/scripts/_standalone_tarot.py"),
            ("oraclebone/iching.py", "skills/iching/scripts/_standalone_iching.py"),
            ("oraclebone/xiaoliuren.py", "skills/xiaoliuren/scripts/_standalone_xiaoliuren.py"),
        ]

        for package_path, standalone_path in pairs:
            with self.subTest(standalone=standalone_path):
                self.assertEqual(
                    (ROOT / package_path).read_text(encoding="utf-8"),
                    (ROOT / standalone_path).read_text(encoding="utf-8"),
                    f"{standalone_path} must stay in sync with {package_path}",
                )


if __name__ == "__main__":
    unittest.main()
