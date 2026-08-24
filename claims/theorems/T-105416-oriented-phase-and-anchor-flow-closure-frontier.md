# T-105416 — Oriented phase and anchor-flow closure frontier

Claim ID: `T-105416`  
Status: **MAJOR EXACT CROSS-PROGRAM REDUCTION; TWO SOURCE-SPECIFIC SIGNS OPEN**  
Created: 2026-08-24  
Depends on: `T-105220`, `T-105330`, `T-105371`; `L-105416--L-105417`; PR #726 `L-105331`, `L-105340--L-105342`, `L-105420--L-105422`  
RH status: **unproved**

## 1. The former two boundary programmes are one tangent

The source-critical programme writes, for every finite polynomial test `q` and
`a in {0,1}`,

\[
q^T\mathsf S_{k,\Omega}^{(a)}q
=q^T\mathsf A_k^{(a)}q-q^T\mathsf C_{k,\Omega}^{(a)}q.
\]

The shifted-companion programme deforms

\[
E_\alpha=F'-\alpha F,
\qquad
E_{-\alpha}=F'+\alpha F.
\]

`L-105416` proves that these are not merely related coordinates. With the
anchor pole and, for even parity, the moving central branch retained exactly,

\[
\boxed{
q^T\mathsf S_{k,\Omega}^{(a)}q
={1\over2}
\left.\partial_\alpha
\mathfrak J_{F,\Omega}^{(a)}(q;\alpha)
\right|_0.
}
\tag{T-105416.1}
\]

Therefore

\[
\boxed{
\mathrm{OSCC105371}
\Longleftrightarrow
\mathrm{OASH105350}
\Longleftrightarrow
\text{nonnegative anchor-renormalized oriented flow for every }q,a,\Omega.
}
\tag{T-105416.2}
\]

The scalar endpoint gate `ZCAP105412` is simply the case `q=1,a=0`.

## 2. The matrix gate collapses after the sharp pole sign

Assume the complete critical hierarchy `CRVH105330`: every critical pole is
real, simple on the nonconfluent stratum, and has residue `rho_c<=0`.

Define `OPG105417` by one cofinal upper-half-plane exhaustion on whose outer
boundary

\[
\liminf\operatorname{Im}{F(z)\over F'(z)}\ge0,
\]

with the central Pick atom removed and restored in the even case.

`L-105417` proves by the harmonic minimum principle that

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{OPG105417}
\Longrightarrow
F/F'\text{ is Pick in the upper half-plane}.
}
\tag{T-105416.3}
\]

The Herglotz representation then has a nonnegative affine coefficient and
only the positive atoms supplied by the signed critical poles. Consequently,

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{OPG105417}
\Longrightarrow
\mathrm{OSCC105371}
\wedge
\mathrm{ZCAP105412}.
}
\tag{T-105416.4}
\]

Thus, after the sharp critical sign is known, the entire all-order boundary
matrix hierarchy is equivalent to one scalar escape-at-infinity phase sign.

## 3. Oriented phase velocity

For the centrally regularized shifted ratio,

\[
\mathcal M_\alpha^\sharp
={F'-\alpha F\over F'+\alpha F}
\times\text{(central correction if even)},
\]

one has

\[
\boxed{
\left.\partial_\alpha
\arg\mathcal M_\alpha^\sharp(z)
\right|_0
=-2\operatorname{Im}\widehat m_F(z).
}
\tag{T-105416.5}
\]

Hence `OPG105417` is the one-sided outer-boundary inequality

\[
\boxed{
\limsup
\left.\partial_\alpha
\arg\mathcal M_\alpha^\sharp(z)
\right|_0
\le0.
}
\tag{T-105416.6}
\]

The functional equation and parity fold the left boundary onto the right one.
The tangent on the right safe line is the single reciprocal source `F/F'`,
not separate shifted canonical products.

## 4. Existing arithmetic leverage

The independent oriented-ratio programme on PR #726 proves:

1. the alpha derivative of the shifted divisor is exactly the `F/F'` current;
2. common factors cancel confluently;
3. the functional equation folds the two safe lines;
4. the omitted reciprocal Dirichlet tail is power-saving;
5. at frozen real carrier, every arithmetic tangent chaos has one global
   sign; and
6. in a one-sided Hardy frame every nontrivial translation has an explicit
   strict phase gap.

Therefore the new conclusion-facing source statement is not an abstract
all-packet determinant estimate. It is:

```text
SOPV105416 — source-owned outer phase velocity

Realize the reciprocal F/F' tangent on one folded safe boundary in the
source-owned smooth one-sided frame, and prove that the archimedean,
horizontal, pole, freezing, taper-conditioning and two-trace errors are
smaller than the explicit phase gap, uniformly along a cofinal exhaustion.
```

This is the all-order, conclusion-facing strengthening of the record-bearing
`RATIOXFER105340/HOTG105420` lane.

## 5. Terminal endpoint supplied by the Xi saddle

The fixed-width moving-saddle packet `L-105413--L-105415`, subject to hostile
review, gives a high derivative terminal rectangle in which:

```text
all zeros are real and simple;
all critical residues are negative;
F/F' is asymptotic to the tangent/cotangent Pick model;
the oriented phase has the correct sign;
r(T)=O_H(T log T).
```

Thus the terminal endpoint of (T-105416.3) is available in proposed complete
form. The remaining problem is transport of the source-owned phase sign down
the derivative ladder, not construction of another high-order endpoint.

## 6. Exact conclusion graph

On the frozen simple/noncommon exhaustion interfaces,

\[
\boxed{
\mathrm{CRVH105330}
\wedge
\mathrm{SOPV105416}
\Longrightarrow
\mathrm{PRES105220}
\wedge
\mathrm{BRP105220}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-105416.7}
\]

Equivalently, one may replace `SOPV105416` by the exact scalar gate
`OPG105417`.

Neither `CRVH105330` nor the low-order Xi outer-phase estimate is proved.

## 7. What this removes

The following should no longer be treated as independent open programmes:

```text
ZCAP105412 as a separate remote-tail moment hypothesis;
all-packet boundary Loewner positivity as unrelated matrix data;
shifted plus/minus zero families as separate explicit formulae;
left and right safe-line phase estimates as separate seams.
```

They are one anchor-renormalized oriented phase current.

## 8. Exact frontier

```text
boundary capacity = shifted-zero first variation     PROVED EXACT
central even branch correction                       PROVED EXACT
all Stieltjes tests = all oriented-flow tests         PROVED EXACT
signed poles + outer scalar phase -> Pick             PROVED EXACT
Pick -> full boundary capacity and real zeros         PROVED EXACT
fixed-width high terminal phase                       PROPOSED / REVIEW REQUIRED
source-owned arithmetic phase gap                     PROVED BEFORE PHYSICAL COLLAPSE
CRVH105330 complete critical sign                     OPEN / SHARP
SOPV105416 low-order outer phase velocity             OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVEN
```