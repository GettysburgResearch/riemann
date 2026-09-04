# Reproduction and independent verification

All commands below are intended to be run from the Riemann repository root
after checking out the import branch.

## 1. Initialize the exact source

```bash
git submodule sync --recursive
git submodule update --init --recursive \
  research/exploratory/imports/lamzouri-zeta-zeros-2026-09-02/ZetaZeros

git -C research/exploratory/imports/lamzouri-zeta-zeros-2026-09-02/ZetaZeros \
  rev-parse HEAD
```

Expected:

```text
4bcaf70e544506c311d83a5a5b143a134b9fc5f7
```

Also record:

```bash
git -C research/exploratory/imports/lamzouri-zeta-zeros-2026-09-02/ZetaZeros \
  status --short
git -C research/exploratory/imports/lamzouri-zeta-zeros-2026-09-02/ZetaZeros \
  verify-commit 4bcaf70e544506c311d83a5a5b143a134b9fc5f7
```

A clean worktree and successful signature verification are expected.

## 2. Build the production library

```bash
cd research/exploratory/imports/lamzouri-zeta-zeros-2026-09-02/ZetaZeros
lake exe cache get
lake build ZetaZeros
```

Record:

```bash
lean --version
lake --version
git submodule status --recursive
```

The source pins:

```text
leanprover/lean4:v4.34.0-rc2
```

Do not build it through Riemann main's Lean 4.33 environment.

## 3. Run Comparator

Install the upstream Comparator tooling as documented by the source, then run:

```bash
lake env comparator Comparator/comparator.json
```

The six expected targets are listed in `FORMALIZATION_AUDIT.md`.

The comparator permits only:

```text
propext
Quot.sound
Classical.choice
```

and requests Nanoda.

## 4. Independent axiom report

Create a temporary file outside the source tree or remove it after use:

```lean
import ZetaZeros.Main

#print axioms ZetaZeros.simple_proportion_lower
#print axioms ZetaZeros.distinct_proportion_lower
#print axioms ZetaZeros.simple_proportion_d4
#print axioms ZetaZeros.distinct_proportion_d5
```

Run it with the pinned environment.

Expected interpretation:

- only standard logical axioms should appear;
- `RiemannVonMangoldt` and `PairCorrelation` will not appear as axioms because
  they are explicit theorem parameters;
- the theorem types must still be inspected to see those parameters.

Also print the exact abstract theorem counterparts identified by the
`zz_tag`/Comparator mapping.

## 5. Production-hole scan

At minimum:

```bash
grep -RIn --include='*.lean' -E '\b(sorry|admit)\b' \
  ZetaZeros ZetaZeros.lean Solution
```

Challenge placeholders are intentional. Any production occurrence requires
investigation.

A robust audit should parse Lean syntax rather than trust a text grep.

## 6. Source-tree receipt

```bash
git ls-tree -r --full-tree \
  4bcaf70e544506c311d83a5a5b143a134b9fc5f7 > zeta-zeros-tree.txt
sha256sum zeta-zeros-tree.txt
```

Archive build, comparator, Nanoda, axiom, and tree receipts together.

## 7. Semantic checks

Independently compare:

```text
paper Proposition 2.1
<-> Challenge prop_simple_real_lower / prop_distinct_lower
<-> production tagged declarations

paper Theorem 1.1
<-> Challenge thm_simple / thm_distinct
<-> ZetaZeros.simple_proportion_lower / distinct_proportion_lower.
```

Check every Fourier sign, `2*pi`, pair ordering, multiplicity, support endpoint,
zero range, rational weight, and strict inequality.

## 8. Exact paper receipt and render replay

The import pass used the exact supplied arXiv v1 file with receipt:

```text
SHA256:
fa33485f517b3c94d2f6e4d4366f3ab14a1e413a738db512e1862f4a0944f5f9

size:
505955 bytes

pages:
14
```

After independently downloading or receiving the paper, verify:

```bash
sha256sum 2609.02882.pdf
pdfinfo 2609.02882.pdf
```

Expected metadata includes:

```text
Title:  A new proof that more than 2/3 of the zeros of the Riemann zeta
        function are simple and on the critical line
Author: Youness Lamzouri
Pages:  14
```

Render all pages:

```bash
python /home/oai/skills/pdfs/scripts/render_pdf.py \
  2609.02882.pdf \
  --out_dir paper-renders \
  --dpi 140
```

Visually compare pages and equation numbering against `PDF_AUDIT.md`. In
particular locate:

```text
Theorem 1.1       page 3
Proposition 2.1   pages 5-9
Lemma 3.1         page 10
Lemma 3.2         pages 10-12
Remark 3.4        page 12
Appendix A        page 13
```

The importer has completed this hash and visual pass. Promotion still requires
an independent reviewer to repeat or verify the receipt.

## 9. Promotion criterion

A successful build alone is insufficient. Promotion requires:

```text
exact source SHA
paper PDF version/hash
clean production build
Comparator success
Nanoda success
axiom report
statement-equivalence review
external-input normalization review
independent mathematical review.
```
