# Reproduction guide

## 1. Verify the attached PDF

Given a local copy of the supplied file:

```bash
sha256sum 2609.04176.pdf
stat -c '%s bytes' 2609.04176.pdf
pdfinfo 2609.04176.pdf
```

Expected:

```text
SHA256:
1d05b36a5675cb8084935ec6945e004f1af9387c8fae6c48b242b4a94d73bd90

size:
378564 bytes

pages:
20
```

## 2. Render every page

Following the repository PDF-audit policy:

```bash
python /home/oai/share/slides/render_slides.py \
  2609.04176.pdf \
  --output_dir catalan_render
```

An equivalent Poppler render is acceptable if the tool above is unavailable.
Record renderer version, dimensions, and warnings. Inspect every page, not only
the first page.

## 3. Run the diagnostic replay

The replay is not part of the proof:

```bash
python3 diagnostics/catalan_audit_replay.py \
  --pdf /path/to/2609.04176.pdf \
  --max-b 300 \
  > replay.local.json
```

Compare with:

```text
diagnostics/replay.json
```

Expected qualitative results:

```text
PDF hash matches
conservative final margin exceeds the paper threshold
238 raw small-prime cells
c_odd agrees to floating precision
middle integral agrees within the reported non-directed quadrature error
finite (5.21) search passes
5B cutoff sanity example has difference 6.
```

## 4. Source search

As of the import date, no companion repository was found. Repeat searches for:

```text
"2609.04176"
"Catalan's constant is irrational" "Zhi-Wei Sun"
"33042423784278900654572890582560690565493664595111"
"0.006276744728100982604597600317605548"
```

If a source repository appears, import it at an immutable commit rather than
copying selected files.

## 5. Exact certificate reconstruction

A proper verifier should not trust the floating replay. Reconstruct:

```text
small-prime:
  238 raw cells
  178 merged cells
  rational Q_0(v)
  exact special-function endpoint expressions
  outward interval proof

middle-prime:
  235 affine cells
  exact selected marginal set on each
  exact rational integral
```

Freeze producer and checker separately.

## 6. Proof audit order

Recommended order:

```text
Theorem 2.1
D=2B repair
Proposition 3.1
Lemmas 4.1-4.2
Psi_A height lemma
Lemma 5.3
Theorem 5.1 with S<=B/20
Lemma 5.5 with corrected cutoff
Propositions 6.3 and 7.4 certificates
Section 8 piece derivation
full Proposition 9.5 ledger
Theorem 9.1 arithmetic
final integer contradiction.
```

## 7. Promotion criterion

Promotion from exploratory import requires:

```text
corrected public source or explicit errata
independent specialist proof review
exact computational artifacts
checker replay from clean bytes
complete Proposition 9.5 ledger
source/claim SHA lock
no unresolved load-bearing findings.
```
