# O-26101 — Cross-route identifications and a source-bound residual-depth selection

Claim ID: `O-26101`  
Title: Three carry profiles are identical, two greedy hinges are equivalent, and the residual-depth Euler choice can be made source-bound  
Status: **EXACT IDENTIFICATIONS PLUS ONE EXPLICIT REPAIR INTERFACE**  
Author/reviewer: `gpt56-pro`  
Created: 2026-08-07  
Review base: `main` at `d1f72553c73037a3990f8c505d0c260d41a223f4`

## 1. One continuum carry state appears in PRs #243, #247, and #252

PR #243 defines

\[
\mathfrak C(y)
=\sum_{n\le y}\frac{\mu(n)}{\sqrt n}
\left[
8\sqrt{\frac yn}-7-\frac32\log\frac yn
\right].
\tag{O-26101.1}
\]

PR #252 defines

\[
g(t)=\sum_{n\le e^t}\frac{\mu(n)}{\sqrt n}
\left[
8e^{(t-\log n)/2}-7-\frac32(t-\log n)
\right].
\tag{O-26101.2}
\]

Substitution `y=e^t` gives the termwise identity

\[
\boxed{g(t)=\mathfrak C(e^t).}
\tag{O-26101.3}
\]

PR #247 defines the Gamma-factor density

\[
a(t)=\sum_{n\le e^t}\frac{\mu(n)}n
\left[
1-\frac78e^{-(t-\log n)/2}
-\frac3{16}(t-\log n)e^{-(t-\log n)/2}
\right].
\tag{O-26101.4}
\]

Since

\[
\frac{e^{-t/2}}{\sqrt n}
=
\frac1n e^{-(t-\log n)/2},
\]

multiplying (O-26101.2) by `e^{-t/2}/8` gives exactly (O-26101.4):

\[
\boxed{
a(t)=\frac18e^{-t/2}g(t)
     =\frac18e^{-t/2}\mathfrak C(e^t).}
\tag{O-26101.5}
\]

The transform identity is the same statement:

\[
\boxed{A(s)=\frac18G_{\rm res}(s+1/2).}
\tag{O-26101.6}
\]

### Consequence

The following global sign assertions are literally equivalent:

```text
PR #243:  mathfrak C(y) >= 0 for all y >= 1;
PR #247:  a(t) >= 0 for all t >= 0;
PR #252:  g(t) >= 0 for all t >= 0.
```

They are not three independent arithmetic hinges. The exact negative Hankel determinant in `R-9510/L-26001` shows that PR #243's displayed conditional-Hankel derivation is false; it does **not** show that the common sign assertion is false.

`FGCM` in PR #247 and `DCRS` in PR #252 remain genuinely weaker finite-horizon targets because they may replace the global state by an `X`-dependent positive minorant and charge a boundary layer.

## 2. DCRS is the Greedy Slack Theorem in a different normalization

Use the common deterministic greedy vector `d_X` of PRs #244 and #252. PR #244 proves

\[
M_X:=\sum_{n=2}^Xn d_X(n)
=8\sqrt X-2\Sigma_X+O(\log^2X),
\tag{O-26101.7}
\]

where

\[
\Sigma_X
=
\sum_{q=2}^X
\left[
 w_X(q)-\sum_{n=q}^Xd_X(n)\beta_{nq}
\right]
\ge0,
\tag{O-26101.8}
\]

and also

\[
L_X:=\sum_{n=2}^Xd_X(n)[\log(n+1)+3]
=O(\log^2X).
\tag{O-26101.9}
\]

PR #252 defines the DCRS debt

\[
\mathfrak D_X=8\sqrt X-M_X+L_X.
\tag{O-26101.10}
\]

Substitution gives

\[
\boxed{
\mathfrak D_X
=2\Sigma_X+L_X+O(\log^2X).}
\tag{O-26101.11}
\]

Because `Sigma_X,L_X>=0`, after allowing a change of the fixed logarithmic exponent,

\[
\boxed{
\mathrm{DCRS}
\iff
\Sigma_X=O(\log^A X).
}
\tag{O-26101.12}
\]

The right side is exactly PR #244's **Greedy Slack Theorem**. PR #252 adds a useful continuum resolvent and boundary-layer proof schema, but it does not introduce a second independent discrete theorem. These two branches should share one canonical claim ID and one blocker ledger.

## 3. The Green correction is the canonical exact signed flow

In PR #248 let

\[
r=v(b_X^{(0)})-w_X,
\qquad
G=G_X>0.
\]

Define

\[
T_*=G^{-1}r,
\qquad
F_*(j)=\sum_q(T_*)_q f_q(j).
\tag{O-26101.13}
\]

The exact correction identity of `L-24509` gives

\[
v(b_{T_*})-v(b_X^{(0)})=-GT_*=-r,
\]

hence

\[
\boxed{v(b_{T_*})=w_X.}
\tag{O-26101.14}
\]

Moreover

\[
\boxed{
\mathcal G_X
=r^TG^{-1}r
=T_*^TGT_*
=
\sum_{j=0}^{X-1}[F_*(j+1)-F_*(j)]^2.}
\tag{O-26101.15}
\]

Thus `GET` is the Dirichlet energy of the canonical exact signed equality correction. Its objective change is

\[
J_X(b_{T_*})-J_X(b_X^{(0)})
=-\lambda^TGT_*
=-\lambda^Tr,
\]

so, using `lambda^Tr=J_X(b_X^(0))-S_X`,

\[
\boxed{J_X(b_{T_*})=S_X.}
\tag{O-26101.16}
\]

This does not prove a lower bound: the correction may violate `b_{T_*}>=0`, and its scalar objective cost is exactly the unknown prime-ramp discrepancy.

PR #254's Constraint-Dipole Transport can therefore be read as a positivity-preserving deformation of this canonical signed flow, potentially in the large nullspace of the prime-power constraint map. The exact target is not merely to solve the constraints; (O-26101.14) already does that. The target is to preserve nonnegativity while proving that the scalar cost is subpower.

## 4. Source-bound repair for the non-top residual-depth Euler choice

PR #250 `L-24901` proves the following tuple geometry. In a non-top row of residual depth `j`, put

\[
\ell=K-j-1\ge1,
\qquad
N=d_0\prod_{i=1}^j a_i b_i,
\qquad
d_0,a_i\le V=e^{J/K+O_K(1)}.
\]

Then some `i` satisfies

\[
\frac{a_i b_i}{V}
\ge
\exp\left(\frac{\ell J}{K^2}-O_K(1)\right).
\tag{O-26101.17}
\]

The phrase “choose one such `i`” is not yet a source-bound Euler partition because the displayed condition depends on the summation variable `b_i`. It can be repaired as follows.

Freeze all variables except `b_i` and write

\[
A_i=N/b_i.
\]

At an active tuple, (O-26101.17) and the upper output endpoint imply

\[
\frac{A_i}{a_i}
\le
\frac{e^{J+O_K(1)}}{V}
\exp\left(-\frac{\ell J}{K^2}\right).
\tag{O-26101.18}
\]

Declare `i` eligible when (O-26101.18) holds, and assign the tuple to the least eligible index. This eligibility condition depends only on the frozen complement `A_i/a_i`, not on `b_i`.

Conversely, throughout the complete active block lattice,

\[
b_i\ge e^{J-O_K(1)}/A_i,
\]

so (O-26101.18) gives

\[
\frac{a_i b_i}{V}
\ge
\exp\left(\frac{\ell J}{K^2}-O_K(1)\right).
\tag{O-26101.19}
\]

Therefore the residual cutoff `a_i b_i>V` is inactive on the whole selected lattice, and the Euler variable is complete. Also

\[
A_i\le e^{(1-\ell/K^2)J+O_K(1)},
\tag{O-26101.20}
\]

so it carries a positive logarithmic fraction.

This is the residual analogue of PR #158's frozen-complement selection rule. It repairs the selection grammar of `L-24901`. It does **not** supply the reflected Hilbert-norm ledger, the actual top-corner matrices, a positive Schur reserve, or a bounded charge injection; those remain unproved.

## 5. Hypercube stress test for Brion and boundary-charge schemas

PR #239 constructs same-sign rank-`K` Möbius product cubes inside one fixed-ratio shell. Changing one prime choice preserves the number of prime factors and therefore preserves the Möbius sign. Consequently a cube edge is not automatically a signed Möbius toggle.

This does not by itself make PR #242's `BRANK/BLINE/BSHORT` or PR #250's `RBC(K)` false. It does impose a necessary production test:

```text
for every high-rank same-sign cube edge, identify the opposite-parity
source family or other exact numerator factor that cancels it;
otherwise BLINE/charge cancellation is unproved on that face.
```

A polyhedral line direction and an arithmetic difference factor are different data. The complete source manifest must contain both.

## 6. Review boundary

Exact in this note:

- identities (O-26101.3)--(O-26101.6);
- reduction (O-26101.11)--(O-26101.12), conditional only on PR #244's proved mass--slack formula;
- canonical Green correction (O-26101.14)--(O-26101.16);
- source-bound eligibility repair (O-26101.18)--(O-26101.20).

Not proved:

- positivity of the common global carry state;
- Greedy Slack/DCRS;
- `GET` or Constraint-Dipole Transport;
- the reflected top-corner reserve or charge map;
- `BLINE/BSHORT` on production packets;
- RH.
