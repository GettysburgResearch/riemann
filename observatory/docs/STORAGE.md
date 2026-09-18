# Results, investigations and stored samples

## Durable numerical investigations

Default root: `~/.riemann-observatory/`, overridden by `OBSERVATORY_DATA_DIR` or `run.py --data-dir`. `objects/<sha256>.json` contains immutable result artifacts and investigation manifests. `index.sqlite3` indexes named investigations. A manifest references the current result, optional baseline and point refinements, plus viewports, selection, notes and name. Copy the entire root for a backup.

Saving identical content reuses the same object. A conflicting/corrupted existing object is refused, not overwritten. Loading verifies the manifest and referenced result hashes. Hash verification authenticates consistency, **not who produced the values, whether claimed metadata is true, or mathematical correctness**. Imported artifacts show this distinction in the interface. The file index is not an authentication boundary.

Schema 2 uses `identity.py`'s named `observatory-f64-v1` encoding. Every value has a type tag; finite numeric values use normalized binary64 hexadecimal representations (zero has one representation); dict keys are sorted. This avoids Python `1.0` versus JavaScript `1` changing the result identity on a normal browser round-trip. It is an application encoding, **not RFC 8785**. Exact large coordinates/indices must remain decimal strings at JSON boundaries.

Unknown result schema/hash versions, duplicate keys, nonfinite JSON constants, changed content and excessive/invalid renderer-facing shapes are refused. Original schema-1 hashes remain checkable with their original byte convention, but a prior browser round-trip may have changed number spelling. Do not silently repair a legacy hash: recompute its request instead. A v2 investigation envelope is required for offline inspection; legacy request/result exports can still be recomputed.

There is no automatic migration, authentication, per-user namespace, crash-recovery proof, disk quota or garbage collection. Atomic result-file replacement and transactional SQLite indexing are implemented; startup/reopen and targeted corruption tests are included. Orphaned objects after an interrupted save are harmless but are not automatically removed.

## Sampled-series import

The importer accepts JSON, not arbitrary database files or executable providers:

```json
{
  "name": "My local window",
  "provenance": "Describe the actual source, version and numerical status",
  "anchor": "763173730199776587433631628770",
  "unit": "ordinate offset",
  "coverage": "Three supplied samples only; mathematical completeness unknown",
  "samples": [
    {"offset": "-0.000002", "value": 1.2},
    {"offset": "0.000000", "value": null},
    {"offset": "0.000003", "value": -0.8}
  ],
  "events": [{"index": 1, "label": "Missing sample", "status": "coverage marker"}]
}
```

Offsets must be strictly increasing exact decimal strings. Gaps are represented by `null`, never by zero or a fabricated interpolant. Bounds: 2–250,000 samples, 10,000 events, 24 MiB per HTTP import. Exact duplicate coordinates need an explicit preprocessing decision and are rejected. `provenance` is required; it is a supplied description, not authenticated upstream replay.

Each dataset receives a content identity and a private SQLite store under `series/`. Tables hold original sample ordinal/offset/value, a pyramid of summaries, missing runs, independent registered events and metadata. The bottom summary block is 32 samples; higher levels merge pairs. A summary retains original first/last/minimum/maximum positions, finite/missing counts, signed sum and absolute sum.

Queries use **sample ordinal intervals `[start,stop)`**. Aligned interior blocks use stored summaries; boundary fragments read original samples. Zooming does not rescan the full dataset. Gaps and events are queried independently; required gap vertices can exceed the nominal display budget. Plotted gaps are not interpreted as empty mathematical intervals. Clicking a sample returns its original offset, anchor and exact decimal sum with enough decimal working precision.

Stored row/node/event/gap/metadata checksums detect the tested accidental modifications when those records are accessed. They are not a cryptographic authentication proof for an untrusted SQLite file or a full Merkle proof that no database row/index was deleted. Only validated JSON import is supported.

Signed and absolute sums are floating aggregates: sampled extrema/positions and integer counts are exact relative to stored inputs; floating sums are not directed enclosures. Different aggregation trees can change low bits. A sparse display is not evidence that unregistered mathematical events do not exist.

The current dataset view manifest references the locally stored dataset ID; it does **not** embed all raw samples or automatically export a transferable dataset archive. Retain the original input or back up the data root when sharing/moving an investigation. Exact-height-axis navigation, binary interchange, streamed append, Zarr/Arrow adapters, irregular 2D grids and billion-point performance are future work.

## HTTP/CLI contracts

- `GET/POST /api/investigations`, `GET /api/investigations/<id>`: list, save and reopen validated numerical investigations.
- `GET/POST /api/datasets`, `GET /api/datasets/<id>/view?start=0&stop=1000&buckets=256`, `GET /api/datasets/<id>/sample/<index>`: bounded import, list, indexed viewport and exact sample inspection.
- `POST /api/jobs`, `GET/DELETE /api/jobs/<id>`: bounded numerical computations and cancellation; no executable expression parameter.
- `GET /api/capabilities`: per-provider request schemas, worker budgets, optional FLINT availability. `GET /api/openapi.json`: HTTP shape.

Mutations use `X-Observatory-Client: v0.1` for compatibility with the original transport. That header is not a password. Browser clients must remain same-origin; loopback-only deployment is mandatory.
