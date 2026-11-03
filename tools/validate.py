#!/usr/bin/env python3
"""Check dotes against the Dotes schema and the canon.

Part of Dotes, by Michael Robbins · michael@intospatia.xyz · https://dotes.xyz
MIT License (see LICENSE-CODE). The canon is CC BY 4.0; the name Dotes is free for anyone to use.

Usage:
    pip install jsonschema
    python tools/validate.py data/dotes.json

The file may hold one dote (an object) or many (a list). The script checks
each dote against schema/dote.schema.json, then checks things the schema
alone can't: that each subcategory belongs to its category, that the primary
category isn't repeated in also_seen_through, and that ids are unique.
"""
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit("This script needs jsonschema. Run: pip install jsonschema")

ROOT = Path(__file__).resolve().parent.parent


def load(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def main(argv):
    if len(argv) != 2:
        sys.exit(__doc__)
    data = load(argv[1])
    dotes = data if isinstance(data, list) else [data]
    schema = load(ROOT / "schema" / "dote.schema.json")
    categories = load(ROOT / "data" / "categories.json")
    sub_to_cat = {
        sub["name"]: cat["name"]
        for cat in categories["categories"]
        for sub in cat["subcategories"]
    }
    validator = Draft202012Validator(schema)

    problems = []
    seen_ids = set()
    for i, dote in enumerate(dotes):
        label = dote.get("id", f"item {i}") if isinstance(dote, dict) else f"item {i}"
        for error in sorted(validator.iter_errors(dote), key=lambda e: list(e.path)):
            where = "/".join(str(p) for p in error.path) or "(top level)"
            problems.append(f"{label}: {where}: {error.message}")
        if not isinstance(dote, dict):
            continue
        cat, sub = dote.get("category"), dote.get("subcategory")
        if sub in sub_to_cat and cat and sub_to_cat[sub] != cat:
            problems.append(f"{label}: '{sub}' belongs to {sub_to_cat[sub]}, not {cat}")
        if cat and cat in dote.get("also_seen_through", []):
            problems.append(f"{label}: the primary category also appears in also_seen_through")
        if label in seen_ids:
            problems.append(f"{label}: duplicate id")
        seen_ids.add(label)

    if problems:
        print(f"{len(problems)} problem(s) in {len(dotes)} dote(s):")
        for p in problems:
            print(" -", p)
        return 1
    print(f"All {len(dotes)} dote(s) are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
