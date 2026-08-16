#!/usr/bin/env python3
"""Validate the repository's machine-readable evidence files."""

from __future__ import annotations

import csv
import datetime as dt
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
ALLOWED_STATES = {
    "verified",
    "scoped",
    "vendor_confirmed",
    "volatile",
    "not_verified",
    "disputed",
}
ALLOWED_SOURCE_TYPES = {
    "documentation",
    "repository",
    "license",
    "product",
    "pricing",
    "trust",
    "legal",
}
ALLOWED_CATEGORIES = {
    "enterprise_low_code",
    "ai_app_builder",
    "ai_coding_tool",
}


def read_csv(name: str) -> list[dict[str, str]]:
    with (DATA / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def valid_date(value: str) -> bool:
    try:
        dt.date.fromisoformat(value)
        return True
    except ValueError:
        return False


def valid_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == "https" and bool(parsed.netloc)


def platform_ids() -> set[str]:
    text = (DATA / "platforms.yaml").read_text(encoding="utf-8")
    return set(re.findall(r"^  - id: ([a-z0-9-]+)$", text, flags=re.MULTILINE))


def platform_categories() -> list[tuple[str, str]]:
    text = (DATA / "platforms.yaml").read_text(encoding="utf-8")
    return re.findall(
        r"^  - id: ([a-z0-9-]+)\n(?:    .+\n)*?    category: ([a-z_]+)$",
        text,
        flags=re.MULTILINE,
    )


def main() -> int:
    errors: list[str] = []
    platforms = platform_ids()
    categories = dict(platform_categories())
    evidence = read_csv("evidence.csv")
    capabilities = read_csv("capabilities.csv")

    if not platforms:
        errors.append("No platform IDs found in data/platforms.yaml")
    for platform in sorted(platforms):
        category = categories.get(platform)
        if category not in ALLOWED_CATEGORIES:
            errors.append(
                f"platforms.yaml: {platform} has missing or invalid category {category}"
            )

    seen_evidence: set[str] = set()
    for line, row in enumerate(evidence, start=2):
        evidence_id = row.get("evidence_id", "")
        if not evidence_id:
            errors.append(f"evidence.csv:{line}: missing evidence_id")
        elif evidence_id in seen_evidence:
            errors.append(f"evidence.csv:{line}: duplicate evidence_id {evidence_id}")
        seen_evidence.add(evidence_id)

        if row.get("platform_id") not in platforms:
            errors.append(f"evidence.csv:{line}: unknown platform {row.get('platform_id')}")
        if row.get("status") not in ALLOWED_STATES:
            errors.append(f"evidence.csv:{line}: invalid status {row.get('status')}")
        if row.get("source_type") not in ALLOWED_SOURCE_TYPES:
            errors.append(f"evidence.csv:{line}: invalid source_type {row.get('source_type')}")
        if not valid_date(row.get("verified_on", "")):
            errors.append(f"evidence.csv:{line}: invalid verified_on date")
        if not valid_url(row.get("source_url", "")):
            errors.append(f"evidence.csv:{line}: source_url must be a public HTTPS URL")
        if not row.get("claim", "").strip():
            errors.append(f"evidence.csv:{line}: empty claim")

    seen_capabilities: set[tuple[str, str]] = set()
    for line, row in enumerate(capabilities, start=2):
        key = (row.get("platform_id", ""), row.get("criterion", ""))
        if key in seen_capabilities:
            errors.append(f"capabilities.csv:{line}: duplicate platform/criterion {key}")
        seen_capabilities.add(key)

        if row.get("platform_id") not in platforms:
            errors.append(f"capabilities.csv:{line}: unknown platform {row.get('platform_id')}")
        if row.get("status") not in ALLOWED_STATES:
            errors.append(f"capabilities.csv:{line}: invalid status {row.get('status')}")
        if not valid_date(row.get("verified_on", "")):
            errors.append(f"capabilities.csv:{line}: invalid verified_on date")

        refs = [ref for ref in row.get("evidence_ids", "").split("|") if ref]
        if not refs and row.get("status") != "not_verified":
            errors.append(f"capabilities.csv:{line}: evidence is required unless status is not_verified")
        for ref in refs:
            if ref not in seen_evidence:
                errors.append(f"capabilities.csv:{line}: unknown evidence ID {ref}")

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Validation passed: {len(platforms)} platforms, "
        f"{len(evidence)} evidence records, {len(capabilities)} capability records."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
