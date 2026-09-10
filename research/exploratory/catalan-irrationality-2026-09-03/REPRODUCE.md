# Reproduction guide

> [!CAUTION]
> The current repository verdict is that the proof in
> `arXiv:2609.04176v1` is invalid as written. Reproduction should begin with
> `HEIGHT_BOUND_COUNTERCHECK.md`, not with the final decimal constants.

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

An equivalent Poppler render is acceptable if that tool is unavailable.
Record renderer version, dimensions, and warnings. Inspect every page.

## 3. Run the original diagnostic replay

This replay corroborates constants and finite local inequalities; it is not a
proof:

```bash
python3 diagnostics/catalan_audit_replay.py \
  --pdf /path/to/2609.04176.pdf \
  --max-b 300 \
  > replay.local.json
```

Compare with `diagnostics/replay.json`.

Expected qualitative results:

```text
PDF hash matches
conservative final decimal margin exceeds the paper threshold
238 raw small-prime cells
c_odd agrees to floating precision
middle integral agrees within non-directed quadrature error
finite (5.21) search passes
5B cutoff sanity example has difference 6.
```

## 4. Run the hostile Proposition 9.5 replay

From this dossier directory:

```bash
python3 diagnostics/catalan_height_hostile_replay.py \
  --output /tmp/height_hostile_replay.json

sha256sum /tmp/height_hostile_replay.json
```

The frozen output is `diagnostics/height_hostile_replay.json`. For the default
`B` values, the one-term lower bound divided by `B^2` should be approximately:

```text
B= 100: 1.821777816169270
B= 200: 1.849984814303233
B= 300: 1.865521107324622
B= 500: 1.874889547532234
B=1000: 1.884184990849831
B=1500: 1.886035510685781
```

This script is a finite diagnostic. The proof-level result is the analytic
calculation in `HEIGHT_BOUND_COUNTERCHECK.md`.

## 5. Hand-check the fatal leading term

A review independent of all code should verify the following sequence.

1. Define the largest-summand majorant from (3.5), (4.1), and (5.24).
2. Insert `I_0={0,...,S-1}`.
3. Prove the Pascal minor is a nonzero integer.
4. Use the exact factorization
   
   \[
   |\Xi_{I_0}|/q^S
   =|D_A|\,|C_{I_0,J}|\prod_{i<S}T_{i+1}\Pi_i.
   \]
5. Verify
   
   \[
   \sum_{p\ \mathrm{odd},\nu}a_{p^\nu,B}\log p
   +\log F_B-\log\prod_i\Pi_i
   =v_2(F_B)\log2.
   \]
6. Verify
   
   \[
   \sum_{i<S}\log\Pi_i
   =2\rho B^2\log B+O(B^2).
   \]
7. Read equations (6.17)--(6.19), which give
   
   \[
   A_\rho=2\rho-\rho^2/2.
   \]
8. Verify that the Cauchy determinant is `exp(O(B^2))` and the tail product is
   `exp(O(B log B))`.
9. Conclude
   
   \[
   \mathcal M_B\ge
   (\rho^2/2)B^2\log B-O(B^2).
   \]
10. At `rho=1/20`, record the surviving coefficient `1/800`.

This directly contradicts the proof's assertion that its max-summand majorant
has complete `B^2 log B` cancellation.

## 6. Recheck the source defects

The following should also be checked against the PDF:

```text
T_0 is used but never defined;
(2.3) produces T_i, while the displayed residual uses T_{i+1} with the wrong column sign;
D is undefined and must equal 2B;
Theorem 5.1 uses but does not state S<=B/20;
Lemma 5.5's 5B support sentence is false;
the 178-cell and 235-cell artifacts are absent.
```

## 7. Repeat the source and criticism search

Search for later versions, errata, companion code, certificates, and concrete
specialist responses using:

```text
"2609.04176"
"Catalan's constant is irrational" "Zhi-Wei Sun"
"Proposition 9.5" Catalan
"B^2 log B" Catalan
"H_B^min" Catalan
```

Any v2 or erratum must receive a new source hash and a fresh review. Do not
silently apply repairs to v1.

## 8. Exact certificate reconstruction

The missing numerical artifacts remain worth reconstructing for the local
mathematics, but they cannot repair the leading-order global flaw.

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

## 9. Revised promotion criterion

The v1 theorem must not be promoted. A future corrected proof requires:

```text
new source version or explicit errata
resolution of the +B^2 log B/800 obstruction
signed Cauchy-Binet cancellation, stronger common divisibility, or redesigned scalar
all local definition/sign/hypothesis repairs
exact computational artifacts and checker replay
independent specialist proof review
source/claim SHA lock
no unresolved load-bearing findings.
```
