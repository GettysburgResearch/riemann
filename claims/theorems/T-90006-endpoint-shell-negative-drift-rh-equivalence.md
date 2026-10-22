# T-90006 — The endpoint shell has negative logarithmic drift, and eventual negativity is equivalent to RH

Claim ID: `T-90006` (provisional range; allocate before integration)  
Status: **PROPOSED COMPLETE RH EQUIVALENCE + CONDITIONAL ASYMPTOTIC — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-09  
Depends on: `L-90004`, `T-90001`, `T-90002`; the standard zero-counting estimate; Mellin inversion on truncated rectangles  
Scope: sharp asymptotic and sign criterion for the single surviving WSTS endpoint scalar; no unconditional sign and no proof of RH

## 1. Statement

Let

\[
A(X)=\sum_{p\le X}(\log p)r_X(p)
\]

be the undifferenced prime endpoint scalar of `T-90001`, interpreted for real
`X` by the same zero-extended seed.  Put

\[
\mathscr T(X)=A(X)-A(X/2)
\tag{T-90006.1}
\]

and, for integer `X`,

\[
T_X^s(2)=A(X)-A(\lfloor X/2\rfloor).
\tag{T-90006.2}
\]

Define

\[
\boxed{
\kappa=\frac{(1+\zeta(1/2))\log2}{2}
=-0.159546714919\ldots<0.}
\tag{T-90006.3}
\]

Assume RH.  For every fixed `0<eta<1/6`, there is a real constant `C_0` such
that

\[
\boxed{
\begin{aligned}
\mathscr T(X)
={}&\kappa\log X+C_0\\
&+\sum_\rho
\frac{m_\rho(1-2^{-(\rho-1/2)})}
     {(\rho-1/2)^2}
X^{\rho-1/2}
+O_\eta\!\left(X^{-\eta}\log^2(2X)\right),
\end{aligned}}
\tag{T-90006.4}
\]

where the sum runs over all nontrivial zeros with multiplicity.  Under RH it is
an absolutely and uniformly convergent Fourier series in `log X`.  Therefore

\[
\boxed{
\mathscr T(X)=\kappa\log X+O(1),
\qquad
T_X^s(2)=\kappa\log X+O(1).}
\tag{T-90006.5}
\]

In particular the following are equivalent:

1. RH;
2. WSTS;
3. `T_X^s(2)<=0` for every sufficiently large integer `X`;
4. `B_X=0` for every sufficiently large integer `X`.

Thus, under RH, the repository's observed `B_X=0` phenomenon is not a finite
accident: after a bounded oscillatory transient, the endpoint shell acquires a
strict negative drift of slope `kappa` in logarithmic scale.

## 2. Exact shell transform

`L-90004` proves

\[
\widehat{\mathscr T}(z)
=\frac{1-2^{-z}}{z^2}
\mathcal G\left(z+\frac12\right),
\tag{T-90006.6}
\]

where

\[
\mathcal G(s)=\frac{\mathcal D(s-1)}s-\mathcal P_1(s),
\]

\[
\mathcal P_1(s)=\sum_p\frac{\log p}{p^s},
\]

and `mathcal D` is the exact shifted-multiple series in `L-90004.5`.
The transform is initially an ordinary Mellin integral for `Re z>1/2`.

The same lemma proves the origin expansion

\[
\mathcal G\left(\frac12+z\right)
=\frac{1+\zeta(1/2)}{2z}+O(1).
\tag{T-90006.7}
\]

Since

\[
1-2^{-z}=z\log2+O(z^2),
\]

we get

\[
\boxed{
\widehat{\mathscr T}(z)
=\frac\kappa{z^2}+O(z^{-1}).}
\tag{T-90006.8}
\]

The double pole gives `kappa log X`; its residue is the prime-square pole of the
prime-only Euler series, not a zero contribution.

The numerical interval in `T-90002.P2`,

\[
-(1+\zeta(1/2))\log2
\in[0.319093429839,0.319093429868],
\]

certifies both the sign and the displayed digits of `kappa` without relying on a
floating zeta evaluation.

## 3. Pole audit under RH

The continuation

\[
\mathcal P_1(s)
=\sum_{m\ge1}\mu(m)
\left(-\frac{\zeta'}{\zeta}(ms)\right)
\tag{T-90006.9}
\]

shows all singularities in the strip used for the contour shift.

- The pole at `s=1`, equivalently `z=1/2`, cancels exactly inside
  `mathcal G`; this is `L-90004.17`.
- The point `z=0` is the double pole (T-90006.8).
- At a nontrivial zero `rho`, `L-90004.23` gives the simple-pole residue
  \[
  \boxed{
  \frac{m_\rho(1-2^{-(\rho-1/2)})}{(\rho-1/2)^2}.}
  \tag{T-90006.10}
  \]
- Under RH, the `m>=2` copies of nontrivial zeros in (T-90006.9) lie at
  `Re z<=-1/4`.
- The nearest negative-real prime-zeta singularity not already extracted is the
  `m=3` copy of the main pole, at `z=-1/6`.

Hence any fixed line `Re z=-eta`, `0<eta<1/6`, is available after extracting
the origin and the critical-line zeros.

## 4. Contour shift and the zero series

Use Mellin inversion on a vertical line `Re z=c>1/2`, truncate at a standard
height sequence avoiding zeros, and move the contour to `Re z=-eta`.
The factor `z^{-2}` in (T-90006.6), together with the additional decay in the
seed kernel, makes the horizontal integrals vanish.  Standard vertical-strip
bounds for `zeta'/zeta` give the remainder

\[
O_\eta(X^{-\eta}\log^2(2X)).
\]

The residues encountered are exactly the origin term, one real constant from
the simple part of the Laurent expansion, and (T-90006.10).  This proves
(T-90006.4).

Under RH, write `rho=1/2+i gamma`.  Then

\[
\left|
\frac{m_\rho(1-2^{-i\gamma})}{(i\gamma)^2}
\right|
\le\frac{2m_\rho}{\gamma^2}.
\]

The classical zero-counting estimate gives

\[
\sum_\rho\frac{m_\rho}{1+\gamma^2}<\infty.
\]

Thus the zero series in (T-90006.4) converges absolutely and uniformly and is
bounded independently of `X`.  Equation (T-90006.5) follows.

## 5. Integer endpoints

`L-90004.24` proves

\[
A(x)-A(\lfloor x\rfloor)
\ll\frac{\log(2x)}{\sqrt x}.
\]

Therefore

\[
A(X/2)-A(\lfloor X/2\rfloor)=o(1)
\]

uniformly on integer endpoints, so (T-90006.4)--(T-90006.5) transfer unchanged
to the exact finite shell `T_X^s(2)`.

Since `kappa<0`, RH gives, for all sufficiently large integers,

\[
T_X^s(2)<0.
\tag{T-90006.11}
\]

## 6. From the endpoint sign to WSTS and back

Assume (T-90006.11) eventually.  Theorem S / Corollary C in `T-90002` gives

\[
B_X=[T_X^s(2)]_+
+O^*(X^{-3/2}\log X).
\]

Consequently

\[
B_X\ll X^{-3/2}\log X,
\]

which is WSTS.  The resident consumer in `T-90001` then gives RH.
This proves

\[
\boxed{
T_X^s(2)\le0\text{ eventually}\Longrightarrow\mathrm{RH}.}
\tag{T-90006.12}
\]

The reverse implication is Section 5, so statements 1--3 in Section 1 are
equivalent.

Under RH, the stronger drift `T_X^s(2)<=-c log X` eventually dominates the
entire `O(X^{-3/2}log X)` transition-window mass in `T-90002`.  Below the
transition, raising the tail threshold removes positive terms and only makes
the tail more negative; above it, every remaining term is nonpositive.
Therefore every tail is nonpositive and

\[
\boxed{B_X=0}
\tag{T-90006.13}
\]

for all sufficiently large `X`.  Conversely, eventual `B_X=0` is WSTS and hence
implies RH.  Statement 4 is equivalent as well.

## 7. Relation to the complete prime-power Riesz criterion

Suzuki's Theorem 1 proves that RH is equivalent to eventual nonpositivity of the
complete prime-power Riesz deficit

\[
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn-4\sqrt X.
\]

The present theorem is not a restatement of that criterion.  It concerns the
prime-only parabolic seed residual and then applies one exact dyadic shell.
The missing higher prime powers reappear analytically as the prime-square pole
at `z=0`; that pole is precisely what creates the new coefficient
`(1+zeta(1/2))log2/2`.

This places the repository's endpoint scalar in the established family of
weighted Chebyshev sign criteria while explaining the additional negative drift
seen in every finite scan.

## 8. Consequence for the proof search

The deterministic geometry is now exhausted more sharply than `WSTS <=> RH`:

```text
all tail thresholds
    -> T-90002 z-collapse
one endpoint scalar
    -> L-90004 exact prime-seed symbol
negative logarithmic drift + bounded RH zero series
    -> T-90006 eventual exact vanishing of B_X under RH.
```

Any unconditional proof of the endpoint sign must control the nonreal poles in
(L-90004.18).  If an off-line zero exists, its contribution grows like
`X^(Re rho-1/2)` and eventually dominates the logarithmic drift along suitable
phases.  Thus the remaining sign problem is exactly the zero-location problem,
not a missing floor estimate or transition-window constant.

## 9. Proof boundary

Closed, subject to independent review:

1. the RH explicit formula (T-90006.4);
2. the exact negative drift coefficient;
3. boundedness of the zero series under RH;
4. integer-endpoint transfer;
5. RH implies eventual endpoint negativity;
6. endpoint negativity implies WSTS and RH;
7. RH is equivalent to eventual exact vanishing of `B_X`.

Still open:

- an unconditional proof of the endpoint sign;
- RH.
