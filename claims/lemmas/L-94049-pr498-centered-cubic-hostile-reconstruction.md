# L-94049 — Frozen PR #498 centered-cubic interfaces survive hostile reconstruction

Claim ID: `L-94049`  
Status: **PROPOSED COMPLETE EXACT-HEAD RECONSTRUCTION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-16  
Frozen source: PR #498 at exact head `6cc0da2fa5711017e260ebdcea4ba8c22e453288`  
Independent comparison review: PR #515 at `6728689d1dbae1891793aabbc393b25e0a7bbaba`  
Scope: normalization, finite projection, real-endpoint interpolation, Mellin pole survival, and the two claimed equivalences; no estimate for CPBD and no RH conclusion

## 1. Frozen endpoint convention

Let

\[
c_\circ(m)=\Lambda(m)-4\mathbf 1_{4\mid m}\Lambda(m/4)
 +3(\log 4)\sum_{r\ge1}\mathbf 1_{m=4^r},
\]

\[
C_\circ(x)=\sum_{m\le x}c_\circ(m),
\]

and, for an integer endpoint \(N\ge2\),

\[
R_N(j)=C_\circ(N)-C_\circ(j)-C_\circ(N-j-1),
\qquad 0\le j<N.
\tag{L-94049.1}
\]

The predecessor is \(N-j-1\). Replacing it by \(N-j\) changes the finite
projection and is a hostile mutation detected by the retained checker.

Put

\[
M_N={1\over N}\sum_{j=0}^{N-1}R_N(j),
\qquad
\mathscr V_\circ(N)
 ={1\over N^2}\sum_{j=0}^{N-1}|R_N(j)-M_N|^2.
\tag{L-94049.2}
\]

If \(Q_{\circ,N}\) is the cell-constant field with value \(R_N(j)\) on
\(j/N<\theta<(j+1)/N\), then exactly

\[
\int_0^1|Q_{\circ,N}(\theta)-M_N|^2d\theta
 =N\mathscr V_\circ(N).
\tag{L-94049.3}
\]

## 2. Mean-zero Bernoulli projection

Let

\[
w(\theta)=\theta(1-\theta)-{1\over6}=-B_2(\theta).
\tag{L-94049.4}
\]

Then

\[
\int_0^1w=0,
\qquad
\int_0^1w^2={1\over180}.
\tag{L-94049.5}
\]

Define

\[
\mathcal A_\circ(N)=\int_0^1w(\theta)Q_{\circ,N}(\theta)d\theta.
\tag{L-94049.6}
\]

Mean zero and Cauchy–Schwarz give

\[
\boxed{
|\mathcal A_\circ(N)|^2
 \le {N\over180}\mathscr V_\circ(N).
}
\tag{L-94049.7}
\]

The antiderivative kernel is

\[
K(x)=2\int_0^xw(u)du={x(1-x)(2x-1)\over3}.
\tag{L-94049.8}
\]

It satisfies

\[
K(0)=K(1)=0,
\qquad K(1-x)=-K(x),
\qquad \|K\|_\infty^2={1\over972}.
\tag{L-94049.9}
\]

Reversing the two finite prefix sums, with no limiting argument, gives

\[
\boxed{
\mathcal A_\circ(N)=\sum_{m\le N}c_\circ(m)K(m/N).
}
\tag{L-94049.10}
\]

## 3. Mellin transform and pole audit

For \(\Re s>-1\),

\[
\widehat K(s)=\int_0^1K(x)x^{s-1}dx
 ={s-1\over3(s+1)(s+2)(s+3)}.
\tag{L-94049.11}
\]

For \(\Re s>1\), Fubini gives

\[
\begin{aligned}
\int_1^\infty\mathcal A_\circ(X)X^{-s-1}dX
={}&\widehat K(s)\\
&\times\left[
(1-4^{1-s})\left(-{\zeta'\over\zeta}(s)\right)
+3(\log4){4^{-s}\over1-4^{-s}}
\right].
\end{aligned}
\tag{L-94049.12}
\]

At a nontrivial zero \(\rho\) with \(0<\Re\rho<1\), none of

\[
\rho-1,
\quad 1-4^{1-\rho},
\quad 1-4^{-\rho},
\quad (\rho+1)(\rho+2)(\rho+3)
\tag{L-94049.13}
\]

vanishes. Thus the logarithmic-derivative pole is not cancelled.

## 4. Real-endpoint interpolation

For \(N\le X<N+1\), the active integer set is unchanged and

\[
\begin{aligned}
|\mathcal A_\circ(X)-\mathcal A_\circ(N)|
&\le {X-N\over N X}\|K'\|_\infty
   \sum_{m\le N}m|c_\circ(m)|.
\end{aligned}
\tag{L-94049.14}
\]

The elementary bounds

\[
\|K'\|_\infty\le {1\over3},
\qquad
\sum_{m\le N}m|c_\circ(m)|\ll N^2
\tag{L-94049.15}
\]

give

\[
\boxed{
\mathcal A_\circ(X)-\mathcal A_\circ(N)=O(1).
}
\tag{L-94049.16}
\]

No square-root prime estimate enters this interpolation step.

## 5. Reconstructed equivalences

Under RH, von Koch gives

\[
C_\circ(x)=\psi(x)-4\psi(x/4)+O(\log x)
 =O(\sqrt x\log^2x),
\]

hence

\[
\mathscr V_\circ(N)=O(\log^4N).
\tag{L-94049.17}
\]

Conversely, if

\[
\mathscr V_\circ(N)\ll(\log N)^A,
\]

then (L-94049.7) and (L-94049.16) give

\[
\mathcal A_\circ(X)
 =O\!\left(X^{1/2}(\log X)^{A/2}\right).
\]

The Mellin integral is therefore holomorphic in \(\Re s>1/2\), while
(L-94049.12) would have a nonremovable pole at every zeta zero there. Functional
equation symmetry yields

\[
\boxed{
\mathrm{RH}
\iff
\mathscr V_\circ(N)\ll(\log N)^A
\text{ for some fixed }A.
}
\tag{L-94049.18}
\]

The scalar prime-block estimate called CPBD in PR #498 is exactly

\[
|\mathcal A_\circ(N)|^2\ll N(\log N)^B.
\tag{L-94049.19}
\]

By the same Mellin audit and the RH upper direction,

\[
\boxed{\mathrm{CPBD}\iff\mathrm{RH}.}
\tag{L-94049.20}
\]

It is a correct criterion, not an independently proved arithmetic producer.

## 6. Hostile verdict

Survives reconstruction:

```text
cell normalization and predecessor                  EXACT
Bernoulli mean cancellation                         EXACT
cubic finite identity                               EXACT
real-endpoint interpolation                         ELEMENTARY / NO RH INPUT
open-strip pole survival                            EXACT
centered energy <=> RH                              VERIFIED CRITERION
CPBD <=> RH                                         VERIFIED CRITERION
```

Does not survive as a proof claim:

```text
prime-block count or common-half-plane alignment
    does not upper-bound the scalar;
CPBD
    is not an unconditional theorem.
```

This reconstruction agrees with the mathematical verdict of PR #515 while
remaining pinned to the frozen PR #498 head.
