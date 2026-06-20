import json
import unittest

from jsonschema import Draft202012Validator

from test_scripts import ROOT, assert_script_exists, run_json


def load_schema(name):
    path = ROOT / "schemas" / name
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_with_schema(data, schema_name):
    schema = load_schema(schema_name)
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(data)


class SchemaTests(unittest.TestCase):
    def test_tarot_output_matches_schema(self):
        script = assert_script_exists(self, ROOT / "skills" / "tarot" / "scripts" / "draw.py")
        data = run_json(script, "--deck", "major", "--spread", "three-card", "--seed", "schema")

        validate_with_schema(data, "tarot-draw.schema.json")

    def test_iching_output_matches_schema(self):
        script = assert_script_exists(self, ROOT / "skills" / "iching" / "scripts" / "cast.py")
        data = run_json(script, "--method", "yarrow", "--seed", "schema")

        validate_with_schema(data, "iching-cast.schema.json")

    def test_iching_random_alias_output_matches_schema(self):
        script = assert_script_exists(self, ROOT / "skills" / "iching" / "scripts" / "cast.py")
        data = run_json(script, "--method", "random", "--seed", "schema")

        self.assertIn("warning", data)
        validate_with_schema(data, "iching-cast.schema.json")

    def test_xiaoliuren_output_matches_schema(self):
        script = assert_script_exists(self, ROOT / "skills" / "xiaoliuren" / "scripts" / "cast.py")
        data = run_json(script, "--method", "numbers", "--month", "3", "--day", "12", "--hour", "7")

        validate_with_schema(data, "xiaoliuren-cast.schema.json")


if __name__ == "__main__":
    unittest.main()
