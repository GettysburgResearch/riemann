# SQLite archive index

The index mirrors the canonical JSONL files. Rebuild it after regenerating the bibliography, theorem, finding and graph masters, using a stable checkout or checkpoint snapshot.

```bash
python scripts/export_archive_index.py build
```

This writes `graphs/archive.sqlite`, its UTF-8 logical dump `graphs/archive.sql`, and one generated Markdown page per canonical paper under `paper_views/`. Generated alias pages point to the canonical paper view and any historical source note. They are counted separately from canonical papers. The exporter uses Python's standard library and leaves the canonical inputs and contributor records intact. To run against a frozen archive tree, use `python scripts/export_archive_index.py --root /path/to/frozen/archive build`.

## Read-only queries

```bash
python scripts/export_archive_index.py id PAPER-MN2026-VERTICAL
python scripts/export_archive_index.py id THM-JUMP- --prefix --limit 10
python scripts/export_archive_index.py query "SELECT id, title, version, source_sha256 FROM papers WHERE audit_level >= 2"
python scripts/export_archive_index.py query "SELECT source_id, relation, target_id FROM proof_dependencies WHERE source_id = 'THM-E001'"
```

Results are JSON. ID lookups search canonical record IDs, graph endpoints and explicit edge IDs. Use the alias page or [paper alias register](../quality/paper_aliases.jsonl) to look up the canonical ID for a historical paper alias. A node and its corresponding paper or theorem may both match. `--limit` caps returned rows. Both commands open SQLite in read-only mode, and the SQL command additionally denies writes, attachments and pragmas.

For tools that understand SQL but cannot read the distributed binary, the dump can be loaded with Python's `sqlite3` module.

```python
import sqlite3
from pathlib import Path

with sqlite3.connect("archive-restored.sqlite") as db:
    db.executescript(Path("graphs/archive.sql").read_text(encoding="utf-8"))
    assert db.execute("PRAGMA foreign_key_check").fetchall() == []
    assert db.execute("PRAGMA integrity_check").fetchone() == ("ok",)
```

## Schema and evidence

| Table | Key fields and relationships |
| --- | --- |
| `canonical_inputs` | Canonical JSONL path, SHA-256 and indexed row count |
| `papers` | Stable paper ID, title, authors, year, family, selection and access statuses, whole-work reading flag, audit level, recorded version, source URL and fingerprint, original record and track |
| `claims` | Stable claim ID, optional FK to its primary paper, statement, kind, locator and original track |
| `connections` | Stable connection ID, recorded statement or claim text, status, evidence and original track |
| `findings` | Stable finding ID, title, classification, optional FK to a stated claim, verified-author-error flag and original track |
| `graph_nodes` | Stable node ID, node type and label |
| `graph_edges` | Edge ID, original explicit ID when supplied, indexed source and target FK to graph nodes, and relation |
| `proof_dependencies` | Edge fields above, plus original locator and track when supplied |
| `paper_claims` and `paper_findings` | FK-backed joins from explicit paper references, resolved through the alias register, with the source field identifying each link |

Each of the seven canonical record tables carries the source JSONL file and 1-based line number, a convenience status and evidence field, and the exact source JSON text in `payload` apart from the line terminator. Some source evidence and status fields are free text or structured values. The convenience columns use existing fields with table-specific fallbacks and encode structured values as JSON text. A missing convenience status is SQL NULL. Audit/access and proof interpretation remain defined by the canonical record.

Anonymous edges receive deterministic content-hash IDs. An explicitly unique edge ID is preserved as the primary ID; the `original_id` field preserves every explicit source value even when it repeats. If rows are literally identical after JSON normalization, later instances get a numbered suffix. Different parallel edges remain distinct. The generator checks that every proof dependency's source, relation and target also occur in the canonical graph.

Generated paper pages report recorded version, access, reading and whole-work audit scope, with paper, claim and finding provenance. Their links come from explicit paper references or from a finding's stated claim reference followed by that claim's paper links. The index recognizes individual existing IDs and retains the reference field; it does not expand shorthand ranges or infer links from a topical match. A paper with no recorded link may still have narrative analysis elsewhere. Fields absent from the source show as unspecified.

The build checks all row payloads and source line numbers against the inputs, fingerprints the canonical JSONL files and the paper alias register when present, checks the indexed record and input counts, validates the local original-record and track paths, runs SQLite foreign-key and integrity checks, and checks the access/reading/audit invariants. Alias resolution affects the link tables and generated views while the payload retains historical identifiers. Source hashes and citation fields are recorded provenance. The rebuild does not fetch remote sources or independently verify their mathematics.
