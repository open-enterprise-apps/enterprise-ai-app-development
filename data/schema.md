# Data schema

## `platforms.yaml`

Each record contains a stable `id`, product name, owner, canonical website and documentation, profile path, and one category: `enterprise_low_code`, `ai_app_builder`, or `ai_coding_tool`.

## `evidence.csv`

| Field | Description |
| --- | --- |
| `evidence_id` | Stable unique identifier. |
| `platform_id` | Identifier from `platforms.yaml`. |
| `criterion` | Normalized evaluation criterion. |
| `claim` | Atomic, qualified English-language claim. |
| `source_url` | Direct URL supporting the claim. |
| `source_type` | `documentation`, `repository`, `license`, `product`, `pricing`, `trust`, or `legal`. |
| `status` | Evidence state defined in `METHODOLOGY.md`. |
| `verified_on` | Most recent review date in ISO format. |
| `scope` | Product family, edition, or deployment limitation. |
| `notes` | Caveats that must travel with the claim. |

## `capabilities.csv`

| Field | Description |
| --- | --- |
| `platform_id` | Platform identifier. |
| `criterion` | Normalized evaluation criterion. |
| `value` | Short normalized observation. |
| `evidence_ids` | Pipe-separated IDs from `evidence.csv`. |
| `status` | Aggregated evidence state. |
| `verified_on` | Review date. |

## Allowed evidence states

`verified`, `scoped`, `vendor_confirmed`, `volatile`, `not_verified`, `disputed`

## Category-aware interpretation

Capability rows are observations, not universal scores. Cross-category comparisons must preserve the difference between an application platform, a prompt-led managed builder, and a repository-level coding tool. An empty or `not_verified` capability must not be rewritten as an unsupported capability.
