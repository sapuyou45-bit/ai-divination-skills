import json
import unittest
from pathlib import Path

from test_scripts import ROOT, assert_script_exists, run_json


def load_schema(name):
    path = ROOT / "schemas" / name
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def validate_required_object(data, schema):
    assert schema["type"] == "object"
    for key in schema.get("required", []):
        if key not in data:
            raise AssertionError(f"Missing required key: {key}")
    for key, rules in schema.get("properties", {}).items():
        if key not in data or "type" not in rules:
            continue
        expected = rules["type"]
        value = data[key]
        if expected == "array" and not isinstance(value, list):
            raise AssertionError(f"{key} should be array")
        if expected == "object" and not isinstance(value, dict):
            raise AssertionError(f"{key} should be object")
        if expected == "string" and not isinstance(value, str):
            raise AssertionError(f"{key} should be string")
        if expected == "integer" and not isinstance(value, int):
            raise AssertionError(f"{key} should be integer")
        if expected == "boolean" and not isinstance(value, bool):
            raise AssertionError(f"{key} should be boolean")


class SchemaTests(unittest.TestCase):
    def test_tarot_output_matches_schema_required_fields(self):
        script = assert_script_exists(self, ROOT / "skills" / "tarot" / "scripts" / "draw.py")
        data = run_json(script, "--deck", "major", "--spread", "three-card", "--seed", "schema")

        validate_required_object(data, load_schema("tarot-draw.schema.json"))

    def test_iching_output_matches_schema_required_fields(self):
        script = assert_script_exists(self, ROOT / "skills" / "iching" / "scripts" / "cast.py")
        data = run_json(script, "--method", "yarrow", "--seed", "schema")

        validate_required_object(data, load_schema("iching-cast.schema.json"))

    def test_xiaoliuren_output_matches_schema_required_fields(self):
        script = assert_script_exists(self, ROOT / "skills" / "xiaoliuren" / "scripts" / "cast.py")
        data = run_json(script, "--method", "numbers", "--month", "3", "--day", "12", "--hour", "7")

        validate_required_object(data, load_schema("xiaoliuren-cast.schema.json"))


if __name__ == "__main__":
    unittest.main()
