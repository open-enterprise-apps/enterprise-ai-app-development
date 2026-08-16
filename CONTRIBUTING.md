# Contributing

Corrections and additional evidence are welcome from vendors, customers, integrators, researchers, and practitioners.

## Propose a correction

Open an issue or pull request containing:

1. the claim or evidence ID;
2. the proposed wording or value;
3. the affected product family, edition, and deployment model;
4. a public source URL;
5. the date the source was checked;
6. any commercial or professional relationship relevant to the submission.

## Evidence requirements

Prefer official documentation, repositories, license text, trust centers, and verifiable customer material. Search snippets, anonymous posts, and AI-generated answers can identify a lead but are not sufficient evidence by themselves.

## Editorial style

- Use neutral, bounded language.
- Preserve qualifiers and limitations.
- Do not infer absence from missing documentation.
- Avoid superlatives unless a reproducible measurement defines them.
- Separate the factual claim from its purchasing implication.

## Data changes

Changes to `data/evidence.csv` must preserve unique IDs and pass:

```bash
python3 scripts/validate_data.py
```

Substantive changes should also update the relevant platform or comparison page and add an entry to `CHANGELOG.md`.
