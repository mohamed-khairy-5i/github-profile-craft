#!/usr/bin/env python3
"""Offline, dependency-free package lint. Not a factual or visual validator."""
import argparse
import json
from pathlib import Path
import re


def check(root):
    errors = []
    for name in ('PROFILE-README.md', 'PROFILE-PLAN.md'):
        path = root / name
        if not path.is_file() or not path.read_text(encoding='utf-8').strip():
            errors.append(f'{name}: missing or empty')
    readme = root / 'PROFILE-README.md'
    if readme.is_file():
        text = readme.read_text(encoding='utf-8')
        if re.search(r'\b(TODO|YOUR_USERNAME|YOUR_NAME|lorem ipsum)\b', text, re.I):
            errors.append('README: unfinished placeholder marker')
        if re.search(r'<\s*(script|iframe)\b', text, re.I):
            errors.append('README: unsupported script or iframe')
        if re.search(r'!\[\s*\]\(', text):
            errors.append('README: image missing alt text')
        if re.search(r'\]\(\s*\)', text):
            errors.append('README: empty link destination')
    return {'passed': not errors, 'errors': errors,
            'scope': 'offline lint only; facts, links, rendering, consent and quality require review'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    result = check(args.directory)
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result['passed'] else 1)


if __name__ == '__main__':
    main()
