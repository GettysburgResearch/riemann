# L-99713 — A zero-safe two-mode filter turns SHARP Harnack into one compact multiplicative packet

Claim ID: `L-99713`  
Status: **PROVED EXACT OPERATOR / MELLIN THEOREM**  
Created: 2026-08-20  
Depends on: PR #647 `L-99251`; PR #653 negative-mass consumer  
RH status: **not assumed**

Let

\[
(S_aF)(x)=F(x/a),
\qquad
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\]

and let `h=H_67^sharp`.  Define

\[
\boxed{
W=(I-S_2)(I-2S_4)h.
}
\tag{L-99713.1}

Its scalar kernel is

\[
\Phi(y)
=T(y)-T(y/2)-2T(y/4)+2T(y/8).
\tag{L-99713.2}
\]

Direct activation-cell algebra gives

\[
\boxed{
\Phi(y)=
\begin{cases}
0,&0<y<1,\\
4\sqrt y-3,&1\le y<2,\\
(4-2\sqrt2)\sqrt y,&2\le y<4,\\
6-2\sqrt2\sqrt y,&4\le y<8,\\
0,&y\ge8.
\end{cases}}
\tag{L-99713.3}
\]

Thus `Phi` is bounded, supported on the fixed multiplicative annulus `[1,8]`,
and has only the unavoidable sign change on `(9/2,8)`.  In particular

\[
\boxed{
W(x)=
\sum_{x/8<n\le x}{\beta(n)\over\sqrt n}\Phi(x/n).
}
\tag{L-99713.4}
\]

No remote source index enters this packet.

## 1. Mellin safety

The endpoint filter has multiplier

\[
Q(s)=(1-2^{-s})(1-2\,4^{-s}).
\tag{L-99713.5}
\]

Therefore

\[
\boxed{
\int_1^\infty W(x)x^{-s-1}dx
=Q(s)
 { (1-67^{-(s+1/2)})(s+3/2)
  \over s(s-1/2)\zeta(s+1/2)}.
}
\tag{L-99713.6}
\]

The first factor of `Q` has zeros only on `Re s=0`; the second has zeros only
on `Re s=1/2`.  If `rho` is a nontrivial zeta zero with
`1/2<Re rho<1`, then `s=rho-1/2` satisfies `0<Re s<1/2`, so neither factor
vanishes.  The 67 factor is also nonzero because `|67^-rho|<1`.

At `s=0` and `s=1/2`, the two factors in `Q` cancel the elementary kernel
poles.  Hence (L-99713.6) is analytic at every positive real `s` and preserves
every hypothetical off-line zeta pole.

Consequently either eventual nonnegativity of `W`, or the weaker estimate

\[
\int_1^XW_-(x){dx\over x}=X^{o(1)},
\tag{L-99713.7}
\]

implies RH by the same negative-part Landau theorem used in PR #653.

## 2. Diagonal scale

Because `Phi` is bounded and `beta` is supported on a fixed finite 67-adic
fibre with `|beta(n)|<=2`,

\[
\boxed{
\sum_{x/8<n\le x}{\beta(n)^2\over n}
 |\Phi(x/n)|^2=O(1)
}
\tag{L-99713.8}
\]

uniformly in `x`.  This is the decisive improvement over the unfiltered SHARP
kernel, whose square-root tail has a power-sized diagonal.

The remaining obstruction is now purely off-diagonal: a balanced, fixed-ratio
native Möbius packet with an exact logarithmic-owner spectral gap.

## 3. Interface disposition

```text
unbounded sqrt(y) SHARP tail          cancelled exactly;
constant tail after first filter      cancelled exactly;
activation ratio                      fixed at 8;
coefficient diagonal                  O(1);
positive-real kernel singularities    removed;
off-line reciprocal-zeta poles        retained;
native beta coefficients / parity     unchanged.
```

The finite positive-filter no-go of earlier target work is not contradicted:
`Phi` necessarily changes sign.  Positivity is sought from the source-owner
quadratic structure, not from a pointwise positive compact kernel.