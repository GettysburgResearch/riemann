# Genus-two `Sym^12`: master-adapter contradiction and provenance audit

Status: **EXACT SOURCE-RELATIVE LOCALIZATION AT `p=3,5,7`; NO ALL-`q`
COHOMOLOGICAL CORRECTION CLAIM**

Scope: the marked `Sym^12` arithmetic-to-ambient adapter, its exact
`q(q-1)` stack normalization, the ordered decomposable boundary, the exact
stable-channel zero, and the displayed Shmakov Eisenstein branch. No new
finite field, polynomial, curve, cohomology group, or modular-form space is
enumerated.

The replay is
`genus2_sym12_master_adapter_contradiction_audit.py`; its canonical artifact is
`genus2_sym12_master_adapter_contradiction_audit.json`.

## 1. Verdict

The arithmetic and geometric master adapter survives the audit. In
particular, no additive Tate term is missing from:

1. the monic-quintic action-groupoid denominator `q(q-1)`;
2. the conversion `r_D(12)=q^6 chi_(12,0)(U_D)`;
3. the reciprocal preclosure and its cubic, quartic, or linear rows;
4. the ordered `Y_0(2) x A_1` decomposable boundary; or
5. the exact semisimplified stable/general conclusion `G=0`.

The first unproved arrow is instead

\[
 \boxed{
 \text{Shmakov's displayed formal associated-graded Tate ledger}
 \longrightarrow
 \text{the actual compact-support Galois Frobenius Euler class}.}
 \tag{1}
\]

Shmakov's displayed natural-`S5` projection gives `2-4L`. The exact
arithmetic branch at the three available primes is compatible with `2-5L`
and differs from the `2-4L` branch by one Tate trace. The source itself leaves
the Galois action on Eisenstein cohomology caveated, so this packet does not
promote the formal repair to an all-`q` theorem.

## 2. Stack normalization and local-system sign

For monic squarefree quintics, the exact marked-curve groupoid is

\[
 \mathcal H_5(\mathbf F_q)//\widetilde G(\mathbf F_q),
 \qquad |\widetilde G(\mathbf F_q)|=q(q-1).
\]

The central kernel is the hyperelliptic involution, so the factor of two is
already included. For the even local system `Sym^12`, its action is trivial
and orbit--stabilizer gives

\[
 T_{(12,0)}(q)
 =\frac{1}{q(q-1)}\sum_{D\in\mathcal H_5(q)}r_D(12),
 \qquad r_D(12)=q^6\chi_{(12,0)}(U_D).
 \tag{2}
\]

The nonsquare affine coset exchanges quadratic twists; it does not introduce
an additive `q` term. A denominator error would rescale the whole trace and
cannot explain the observed additive discrepancy in any event.

## 3. Arithmetic inventory audit

The reciprocal sieve gives exactly

\[
 T_{(12,0)}
 =\widehat H_{12}-(q+1)\widehat G_3-\widehat G_4
  +\widehat\Lambda_3+\widehat Q_1.
 \tag{3}
\]

The potentially dangerous lower rows check as follows:

\[
 \widehat G_3=0,
 \qquad
 \widehat\Lambda_3
 =-5q-3\Theta_\Delta-\Theta_{8,2}-\Theta_{10,2},
 \tag{4}
\]

\[
 \widehat G_4=\Theta_\Delta,
 \qquad
 \widehat Q_1=3q-9.
 \tag{5}
\]

For repeated cubics, `L^3` contributes `-(q-1)` and every ordered `L^2 M`
contributes `18-6q`, giving the normalized repeated marked row `17-6q`.
For a fixed linear modulus,

\[
 \lambda_{12}=-(q-1),\quad
 \lambda_{12}^{[2]}=\frac{q-1}{2}(5q-16),\quad
 \kappa_{12}=-\frac{q(q-1)}2,
\]

so the weighted row is `3(q-1)(q-3)` per modulus and (5) follows after
division by `q(q-1)`. These are the two most plausible locations for an
additive `q` error; neither contains one. Substitution yields

\[
 \boxed{
 T_{(12,0)}=\widehat H_{12}-2q-9
 -4\Theta_\Delta-\Theta_{8,2}-\Theta_{10,2}.}
 \tag{6}
\]

## 4. Marked open-to-ambient boundary

The marked odd theta characteristic distinguishes the elliptic factors, so
the decomposable stratum is the ordered product

\[
 \mathcal A_{1,1}(w^1)=Y_0(2)\times\mathcal A_1,
\]

not an `S2` quotient. Direct branching of
`Sym^12(W_1 direct_sum W_1)` gives

\[
 B_{12}=11-3q+4\Theta_\Delta+Theta_{8,2}+Theta_{10,2}
 -q\Theta_{14,\Gamma_0(2)}.
 \tag{7}
\]

Adding (6) and (7) therefore gives the exact ambient identity

\[
 \boxed{
 E_{\rm arith}
 =\widehat H_{12}+2-5q-q(f_++f_-).}
 \tag{8}
\]

All three inherited lower cusp channels cancel coefficientwise. There is no
unaccounted open-to-ambient `+q`.

## 5. The finite provenance correction

The finite scout directly replays only

\[
 T_{(12,0)}(p)=\frac{\sum_Dr_D(12)}{p(p-1)}
\]

from stored complete joint laws. It does **not** enumerate squarefree
degree-twelve moduli or directly sum their central coefficients `Q_5(f)`.
Its displayed `Hhat_12` and `H_12` columns apply (6), now source-locked in the
scout itself. Hence those columns are exact consequences of raw `T_(12,0)`
plus the inventory, not an independent audit of (6).

The contradiction can be stated without treating `Hhat_12` as direct data.
With the exact stable result `G=0`, Shmakov's `2-4L` branch gives

\[
 E_{\rm Shm}=2-4q-q(f_++2f_-).
\]

Eliminating `Hhat_12` from (8) using (6) gives

\[
 E_{\rm arith}-E_{\rm Shm}
 =T_{(12,0)}+9+q+4\Theta_\Delta+Theta_{8,2}+Theta_{10,2}
 +q\,a_p(f_-).
 \tag{9}
\]

The three exact stored rows are:

| `p` | direct `T_(12,0)` | inventory-derived `Hhat_12` | `a_p(f_-)` | raw-`T` residual (9) |
|---:|---:|---:|---:|---:|
| 3 | -4,587 | -3,708 | 1,236 | -3 |
| 5 | 267,251 | 287,250 | -57,450 | -5 |
| 7 | -382,735 | -449,624 | 64,232 | -7 |

Thus the Shmakov branch requires an additional `+p` at every stored row. This
is an exact three-prime contradiction between the combined arithmetic branch
and the displayed cohomological branch. It is not an independent direct
calculation of `H_12`, and it proves nothing at a fourth `q`.

## 6. Smallest formal repair and its grade

Inside the displayed constituent ledger, the difference is unique. The
weight-16 Fricke-positive level-two Siegel block has

\[
 [3,2,1]\oplus[4,2]
\]

in Shmakov's display, while the `2-5L` branch additionally needs

\[
 [5,1]\otimes\mathbb L
\]

in degree three. The natural point-stabilizer `S5` fixes one vector in
`[5,1]`, so this changes

\[
 2-4\mathbb L\longmapsto2-5\mathbb L
\]

and, after `G=0`, changes

\[
 \widehat H_{12}=\mathbb L-\mathbb Lf_-
 \longmapsto
 \widehat H_{12}=-\mathbb Lf_-.
\]

This is the unique **formal** repair within the displayed carrier ledger and
the trace correction forced at `p=3,5,7`. The packet does not construct that
class in actual compact-support `l`-adic cohomology, prove it for all odd
prime powers, or decide whether the source display or some deeper
cohomological identification must be reformulated.

## 7. Source and computation contract

The producer content-locks five committed artifacts:

1. the exact marked-Weierstrass stack adapter at commit `c8eff406f`;
2. the arithmetic inventory at commit `482e32c53`;
3. the provenance-repaired finite scout at commit `c463d4896`;
4. the raw-`T` conditional closure at commit `20abcc478`; and
5. the one-Tate constituent no-go at commit `86be60a01`.

It reads 90,961 bytes, performs three finite row checks, and uses exact Python
integers only. Hard caps are five source files, 45,000 bytes per source,
95,000 source bytes total, three rows, 32,768 output bytes, and four seconds.

No field or curve enumeration, web call, database query, numerical fit,
motivic identification, novelty claim, compatible-system claim, RH/GRH
claim, or global Euler-product claim is made.

```text
python -B research/l-families/atlas/function_field/genus2_sym12_master_adapter_contradiction_audit.py --check
python -B -O research/l-families/atlas/function_field/genus2_sym12_master_adapter_contradiction_audit.py --check
python -B -m unittest tests.test_genus2_sym12_master_adapter_contradiction_audit
python -B -O -m unittest tests.test_genus2_sym12_master_adapter_contradiction_audit
```
