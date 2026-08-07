# L-24503 — Tapered divisor comb and primitive-neighbor ledger

Claim ID: `L-24503`  
Status: `PROPOSED — exact finite ledger; asymptotic unbalanced estimate proposed`  
Scope: elementary correction geometry  
Issue: #245

Fix rational `0<alpha<beta<1` and integer taper order `R>=2`. For `2<=j<=X-1`, put

\[
t_j=\frac{j/X-\alpha}{\beta-\alpha},
\]

and

\[
\phi_{X,R}(j)=
\begin{cases}
[4t_j(1-t_j)]^R,&0<t_j<1,\\
0,&\text{otherwise}.
\end{cases}
\tag{L-24503.1}
\]

Given nonnegative amplitudes `T_d`, define the divisor-comb flow

\[
F_T(j)=\phi_{X,R}(j)\sum_{d\mid j}T_d.
\tag{L-24503.2}
\]

The induced constraint matrix is

\[
C_{X,R}(q,d)=
\sum_{\substack{2\le j\le X-1\\d\mid j}}
\phi_{X,R}(j)
(\mathbf1_{q\mid j+1}-2\mathbf1_{q\mid j}+\mathbf1_{q\mid j-1}).
\tag{L-24503.3}
\]

## 1. Diagonal sign

For every `d`,

\[
\boxed{C_{X,R}(d,d)=-2\sum_{d\mid j}\phi_{X,R}(j)=:-A_d\le0.}
\tag{L-24503.4}
\]

Thus increasing `T_d` repairs the `d`-constraint directly.

## 2. Exact gcd ledger

Let `g=(q,d)`. If `g>1`, the simultaneous congruences

\[
d\mid j,\qquad q\mid j\pm1
\]

are impossible. Hence

\[
\boxed{
C_{X,R}(q,d)
=-2\sum_{\operatorname{lcm}(q,d)\mid j}\phi_{X,R}(j)\le0.
}
\tag{L-24503.5}
\]

Therefore every noncoprime interaction is favorable. No nonprimitive residue chain is omitted.

If `(q,d)=1`, write `j=ad`. The harmful contributions are exactly the primitive determinant-one solutions

\[
ad-bq=\pm1.
\]

More precisely,

\[
\boxed{
C_{X,R}(q,d)
=\sum_{\substack{ad-bq=\pm1\\2\le ad\le X-1}}\phi_{X,R}(ad)
-2\sum_{\substack{qd\mid j\\2\le j\le X-1}}\phi_{X,R}(j).
}
\tag{L-24503.6}
\]

This is the corrected Farey-type ledger: only primitive determinant-one neighbors can create positive cross-interaction.

## 3. Mean-zero periodic structure in the coprime rows

For `(q,d)=1`, define

\[
h_{q,d}(a)=
\mathbf1_{ad\equiv-1\pmod q}
+\mathbf1_{ad\equiv1\pmod q}
-2\mathbf1_{ad\equiv0\pmod q}.
\]

Then `h_{q,d}` is `q`-periodic and has mean zero over a complete residue period. Therefore repeated finite summation by parts against

\[
a\mapsto\phi_{X,R}(ad)
\]

annihilates the continuous mean at every order permitted by the taper.

For each fixed integer `r>=1`, the proposed quantitative bound is

\[
\boxed{
|C_{X,R}(q,d)|
\le C_{r,\alpha,\beta,R}\,q\left(\frac{qd}{X}\right)^{r-1}.
}
\tag{L-24503.7}
\]

In the interior of the taper, `A_d\asymp_{\alpha,\beta,R}X/d`, so choosing `r=R+1` gives

\[
\boxed{
\frac{|C_{X,R}(q,d)|}{A_d}
\ll_{\alpha,\beta,R}
\left(\frac{qd}{X}\right)^R.
}
\tag{L-24503.8}
\]

Thus cells with `qd<=eta X`, fixed `eta<1`, can be made arbitrarily small by increasing the taper order. The unresolved support is balanced and primitive: `qd\asymp X`, `(q,d)=1`, `ad-bq=+-1`.

## Review mutations

A reviewer should explicitly test:

1. `q=d=5`: the row must be present and nonpositive;
2. coprime small controls such as `(q,d)=(5,7)`;
3. endpoint values where the taper switches on/off;
4. the distinction between the exact identities (L-24503.4)--(L-24503.6) and the proposed all-scale bound (L-24503.7).

## Status boundary

The gcd and primitive-neighbor identities are exact finite algebra. The uniform high-order estimate is a proposed lemma requiring independent proof. No global contraction and no RH claim is made here.
