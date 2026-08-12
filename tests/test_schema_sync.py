"""Packaged output schemas must stay in sync with the canonical schemas/ dir."""

import unittest

from test_scripts import ROOT


class PackagedSchemaSyncTests(unittest.TestCase):
    def test_packaged_schemas_match_root_schemas(self):
        names = [
            "tarot-draw.schema.json",
            "iching-cast.schema.json",
            "xiaoliuren-cast.schema.json",
            "bazi-cast.schema.json",
        ]
        for name in names:
            with self.subTest(schema=name):
                self.assertEqual(
                    (ROOT / "schemas" / name).read_text(encoding="utf-8"),
                    (ROOT / "oraclebone" / "schemas" / name).read_text(encoding="utf-8"),
                    f"oraclebone/schemas/{name} must stay in sync with schemas/{name}",
                )


if __name__ == "__main__":
    unittest.main()
