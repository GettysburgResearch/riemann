# L-32412 — Carry-position cells are exact augmented binary rows

Claim ID: `L-32412`  
Title: At every integer physical parent, continuous carry-position localization is exactly a uniform nonnegative measure on binary rows of the preceding parent plus one explicit divisor-increment endpoint fiber  
Status: **PROPOSED COMPLETE EXACT PLACEMENT LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: atomized carry window `C(x,theta)` from PR #297/#325; elementary floor arithmetic  
Scope: exact physical-to-row placement for arbitrary arithmetic coefficients; no RH conclusion

## 1. Carry-position cells

For real `x>=1` and `0<=theta<=1`, retain

\[
 C(x,\theta)
 =\lfloor x\rfloor
 -\lfloor\theta x\rfloor
 -\lfloor(1-\theta)x\rfloor.
\tag{L-32412.1}
\]

Fix an integer physical parent `N>=2`. For

\[
 0\le j\le N-1,
 \qquad
 {j\over N}<\theta<{j+1\over N},
\]

write `theta N=j+r` with `0<r<1`. For every integer `q>=1`,

\[
 \left\lfloor{\theta N\over q}\right\rfloor
 =\left\lfloor{j\over q}\right\rfloor
\]

because `0<r/q<1/q`, while

\[
 \left\lfloor{(1-\theta)N\over q}\right\rfloor
 =\left\lfloor{N-j-1\over q}\right\rfloor.
\]

Hence, away from the measure-zero cell boundaries,

\[
\boxed{
 C(N/q,\theta)
 =\left\lfloor{N\over q}\right\rfloor
 -\left\lfloor{j\over q}\right\rfloor
 -\left\lfloor{N-j-1\over q}\right\rfloor.
}
\tag{L-32412.2]

The closing bracket in the tag is typographical only.

## 2. Binary row plus divisor increment

Let

\[
 \chi_{M,j}(q)
 =\left\lfloor{M\over q}\right\rfloor
 -\left\lfloor{j\over q}\right\rfloor
 -\left\lfloor{M-j\over q}\right\rfloor
\]

be the ordinary binary carry row. Since

\[
 \left\lfloor{N\over q}\right\rfloor
 -\left\lfloor{N-1\over q}\right\rfloor
 =\mathbf1_{q\mid N},
\]

(L-32412.2) becomes

\[
\boxed{
 C(N/q,\theta)
 =\chi_{N-1,j}(q)+\mathbf1_{q\mid N}.
}
\tag{L-32412.3}

Thus the continuous cell is not an unidentified continuum object. It is exactly

```text
binary split of parent N-1 into j and N-j-1
+
divisor endpoint increment at N.
```

The unit mass missing from the two binary children is precisely the endpoint fiber.

## 3. Arbitrary arithmetic coefficient field

Let `f` be any finitely supported complex arithmetic coefficient sequence and define

\[
 Z_f(N,\theta)
 =\sum_{q\le N}f(q)C(N/q,\theta).
\tag{L-32412.4}
\]

Put

\[
 L_{M,j}(f)=\sum_qf(q)\chi_{M,j}(q),
 \qquad
 d_f(N)=\sum_{q\mid N}f(q).
\tag{L-32412.5}

Then on the `j`th carry-position cell,

\[
\boxed{
 Z_f(N,\theta)=L_{N-1,j}(f)+d_f(N).
}
\tag{L-32412.6}

In particular the field is constant on each of the `N` open cells.

## 4. Exact nonnegative row-measure identity

For two coefficient sequences `f,g`, integration over carry position gives

\[
\boxed{
 \int_0^1Z_f(N,\theta)\overline{Z_g(N,\theta)}\,d\theta
 ={1\over N}\sum_{j=0}^{N-1}
 [L_{N-1,j}(f)+d_f(N)]
 \overline{[L_{N-1,j}(g)+d_g(N)]}.
}
\tag{L-32412.7]

Again the closing bracket in the displayed tag is typographical only.

For `f=g`,

\[
\boxed{
 \int_0^1|Z_f(N,\theta)|^2d\theta
 ={1\over N}\sum_{j=0}^{N-1}|L_{N-1,j}(f)+d_f(N)|^2.
}
\tag{L-32412.8]

Thus the continuous physical carry-position norm is an **exact uniform nonnegative row measure**, with no frame constant and no unknown physical-to-carry map.

The same identity applies bilinearly to every independent-frequency cross term after Fourier localization, because (L-32412.7) is coefficientwise and finite at fixed physical parent.

## 5. Q=4 source specializations

For the Q=4 Euler--Blaschke system of PR #325/#337, let

\[
 b_4=A_4^{-1},
 \qquad q_4=b_4*\Lambda_4,
 \qquad t_4=b_4*C_4.
\]

Since

\[
 \mathbf1*b_4=e_4,
\]

the endpoint increment of the bare source is exactly

\[
\boxed{d_{b_4}(N)=e_4(N),}
\tag{L-32412.9}

so it is zero except at the declared four-adic source atoms and is uniformly bounded by three in absolute value.

Likewise

\[
 \mathbf1*q_4=e_4*\Lambda_4=c_4,
\]

so

\[
\boxed{d_{q_4}(N)=c_4(N),}
\tag{L-32412.10}

which is exactly the raw endpoint coefficient already isolated in the real-`X` collar theorem on PR #325.

Finally

\[
\boxed{
 d_{t_4}(N)=(e_4*C_4)(N).
}
\tag{L-32412.11}

The elementary prefix bound of `L-32405` gives

\[
 \sum_{m\le x}C_4(m)=O(x\log(2x)),
\]

and the geometric four-adic support of `e_4` therefore yields the crude but sufficient endpoint estimate

\[
\boxed{
 |d_{t_4}(N)|=O(N\log(2N)).
}
\tag{L-32412.12]

Every endpoint increment is thus smaller than the cofinal quarter-balanced reserve `R_4(n,j) \gg n^2` after the appropriate quadratic/cross normalization.

## 6. Source-deformation product curvature in the same cells

Use the Q=4 Jordan deformation of PR #337,

\[
 J_\tau={A_4(s-\tau)\over A_4(s)},
 \qquad
 K_\tau=b_4*J_\tau.
\]

Then

\[
 K_0=b_4,
 \qquad K'_0=q_4,
 \qquad K''_0=t_4.
\tag{L-32412.13}

On one physical cell define

\[
 z_{N,j}(\tau)
 =L_{N-1,j}(K_\tau)+d_{K_\tau}(N).
\]

The exact real-deformation curvature is

\[
\boxed{
 {1\over2}{d^2\over d\tau^2}|z_{N,j}(\tau)|^2\bigg|_{\tau=0}
 =|Q_{N,j}^{\rm aug}|^2
 +\operatorname{Re}\bigl(
  B_{N,j}^{\rm aug}\overline{T_{N,j}^{\rm aug}}
 \bigr),
}
\tag{L-32412.14]

where

\[
 B^{\rm aug}=L(b_4)+e_4(N),
\]

\[
 Q^{\rm aug}=L(q_4)+c_4(N),
\]

and

\[
 T^{\rm aug}=L(t_4)+(e_4*C_4)(N).
\]

By the general source-convolved reflected identity `L-32710`, twice this curvature is exactly the localized **product-source term** in the same physical normalization.

Therefore the formerly abstract product-source block has an explicit row-cell placement before any inequality is applied.

## 7. Cofinal reserve scale of the augmented corrections

On quarter-balanced binary rows, PR #337 proves

\[
 { |L(q_4)|^2\over\mathcal R_4}\to0,
 \qquad
 { |L(b_4)L(t_4)|\over\mathcal R_4}\to0
\]

uniformly, while

\[
 \mathcal R_4\gg N^2.
\]

The endpoint corrections above satisfy

```text
e4(N)=O(1),
c4(N)=O(log N),
(e4*C4)(N)=O(N log N).
```

Together with the already proved logarithmic bound on `L(b_4)` and `L(t_4)=O(N log^3 N)`, every new mixed endpoint term divided by `R_4` tends to zero uniformly on the same cofinal balanced cone.

Consequently the complete augmented product curvature (L-32412.14), not merely its interior binary-row part, consumes an arbitrarily small fraction of the Q=4 reserve cofinally.

This is a placement theorem, not yet a global recurrence: one still has to use the reflected Selberg sign/orientation to show how the available reserve enters the full block budget.

## 8. Proof boundary

Closed exactly, subject to review:

- physical carry-position cells as augmented binary rows;
- exact bilinear/nonnegative row-measure formula;
- exact Q=4 endpoint increments for the bare source and first current;
- an elementary sufficient bound for the second-current endpoint increment;
- exact placement of the source-deformed product curvature into the same row cells;
- cofinal negligibility of every augmentation relative to the existing Q=4 reserve.

Still open:

- the final reflected-Selberg orientation/telescoping which makes that reserve available in the global block recurrence;
- the coefficient-one neutral recurrence;
- RH.
