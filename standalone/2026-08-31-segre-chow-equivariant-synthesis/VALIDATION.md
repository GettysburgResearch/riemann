# Focused validation ledger

```text
Scope: continuation files in this standalone packet only.
No repository-wide CI, source-branch rerun, or RH/GRH validation is claimed.
```

## Authoring executions

The theorem-producing authoring versions of the three exact replays were run
as follows.

Normal Python:

```bash
python -B ternary_change_of_rings_replay.py --prime 65521
python -B ternary_change_of_rings_replay.py --prime 65537
python -B cycle_index_alternant_replay.py
python -B stable_layer_head_replay.py
```

Optimized Python:

```bash
python -B -O ternary_change_of_rings_replay.py --prime 65521
python -B -O cycle_index_alternant_replay.py
python -B -O stable_layer_head_replay.py
```

All executions passed. The two chain-level primes produced the same rank
profile. The Python sources also passed `python -m py_compile`.

The JSON files committed beside the scripts are the frozen outputs of those
authoring executions. The committed scripts are compact review-facing forms
of the same literal algorithms. This continuation commit does not claim a
byte-level source/output seal: independent review should execute the committed
bytes and compare their mathematical outputs with the frozen JSON and theorem
statements.

## Expected exact chain-level profile

At both primes 65521 and 65537:

```text
rank d1(W), internal 2 = 205
rank d2(W), internal 2 = 45
rank d1(W), internal 3 = 1000
rank d2(W), internal 3 = 1095
rank d2(W), internal 4 = 6625
rank d3(W), internal 4 = 3030
rank(C tensor B_1,2 -> B_1,3) = 65
rank(horizontal map at E^1_(2,1,4)) = 1105
rank(d2 transgression modulo W-boundaries) = 65
```

The derived first ambient dimensions are 162 quadratic equations and 1720
cubic linear syzygies.

## Expected exact cycle-index profile

The replay must:

1. reproduce all three conjugacy-class numerators at each of four declared
   diagonal panels;
2. match every coefficient with the complete `GL3 x S3` Chow-Tor table;
3. recover the trivial, sign and standard isotypic Euler polynomials by
   character inversion;
4. match the explicit cycle alternant at the generic panel `(2,3,5)`.

The exact expected values are in `cycle_index_alternant_replay.json`.

## Expected stable-head profile

The replay must recover every term in the large-part heads of the committed
layers 3, 4, 5 and 6, then produce the period-four consequences

```text
[e_14] corr_7 = 2
[e_16] corr_8 = 2.
```

The exact term dictionaries are in `stable_layer_head_replay.json`.

## Proof-only transferred-model ledger

`TRANSFERRED_KOSZUL_MODEL.md` and
`INTERNAL_DEGREE_SIX_CLOSURE.md` add no new rank computation. Their review
contract is mathematical rather than executable.

### 1. Homological-perturbation grading

For

\[
\Delta_r=\pi d_C(hd_C)^{r-1}\iota,
\]

check that

\[
\Lambda^pC\otimes B_{q,j}
\longrightarrow
\Lambda^{p-r}C\otimes B_{q+r-1,j+r}.
\]

It must preserve internal degree `p+j`, lower total homological degree `p+q`
by one, and lower the C-wedge filtration by `r`. Since `B_q=0` for `q>3`,
all `r>=5` components must vanish.

### 2. Support count

From the ten nonzero Chow bidegrees, independently recover:

```text
ordinary C-action slots: 6
arity-2 higher slots:     6
arity-3 higher slots:     4
arity-4 higher slots:     2
higher slots total:      12
```

Eleven higher slots must satisfy `j+r<=6` and hence occur in internal degree
six. The unique exception is

```text
Lambda^2 C tensor B_(2,5) -> B_(3,7),
```

whose first possible internal degree is seven.

### 3. Rank-free non-formality

Check the implication

\[
E^2_{0,2,4}=B_{2,4}\ne0,
\qquad
\operatorname{Tor}^{S_E}_2(R,k)_4=0
\]

from property `N3`. Since column zero has no outgoing differential, the
65-dimensional class must be killed by an incoming higher differential. A
formal derived `S_C`-module would make it survive as a direct summand, giving
the contradiction.

This proof forces disappearance but does not identify the page. The existing
exact replay supplies the stronger page-two surjectivity.

### 4. Internal-degree-six arithmetic

Using

```text
dim C = 17
(dim B00,B01,B02) = (1,17,11)
(dim B12,B13) = (20,65)
(dim B24,B25) = (65,20)
(dim B35,B36) = (11,17)
```

independently recover the four chain dimensions

```text
12376 -> 152796 -> 79407 -> 357
```

and the Euler characteristic

```text
12376 - 152796 + 79407 - 357 = -61370.
```

Also expand

\[
(1-T)^{20}(1+20T+48T^2+20T^3+T^4)
\]

through degree six and check

```text
1 - 162 T^2 + 1720 T^3 - 9234 T^4
  + 30456 T^5 - 61370 T^6 + ... .
```

Minimality must kill `Tor_(6,6)`, and property `N3` must kill `Tor_(3,6)`.
Thus verify

\[
\beta_{5,6}-\beta_{4,6}=61370.
\]

### 5. The split-functorial master class

For three two-dimensional factors, check

\[
(1-T)^4(1+4T+T^2)=1-9T^2+16T^3-9T^4+T^6.
\]

Property `N3`, codimension four and Gorenstein top shift six then give a
one-dimensional `K_(4,2)` of product-group character

\[
(\det U_1)^3\boxtimes(\det U_2)^3\boxtimes(\det U_3)^3.
\]

Split inclusions `U_i -> V_i` and retractions must give a split injection on
Koszul homology. The image is a highest-weight vector of weight `(3,3,0)` in
each rank-three factor, so it generates

\[
S_{(3,3)}V_1\boxtimes S_{(3,3)}V_2\boxtimes S_{(3,3)}V_3.
\]

Weyl's formula gives `dim S_(3,3)(k^3)=10`, hence the lower bounds

```text
dim K_(4,2) >= 1000
dim K_(5,1) >= 62370.
```

No equality or full character decomposition is part of this validation
contract.

## Review boundary

The finite replays certify the declared matrices, ranks and symbolic term
comparisons. The all-parameter cycle-index and stable-head statements depend
on their written proofs. The transferred model, non-formality theorem,
degree-six defect identity and master-submodule lower bound are proof-only
claims and require line-by-line mathematical review. The canonical-top note
proves the intrinsic line and comparison protocol but does not claim that the
accepted 379-term vector has already been projected coefficientwise.
