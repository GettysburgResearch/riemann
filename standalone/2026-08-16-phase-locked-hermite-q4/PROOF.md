# Self-contained proof extract

## Theorem A — phase-locked reality criterion

Let `Z` be a conjugation-invariant locally finite multiset in
`|Im z|<1/2` with subquadratic horizontal counting. Put

\[
P(u)=5-4\cos((\log4)u).
\]

For every integer `m>=0`, define

\[
\mathcal M_m(q,x)
=\sum_{z\in Z}m_z(z-x)^2e^{-q(z-x)^2}P(z-x)^{2m}.
\]

Then

\[
Z\subset\mathbb R
\iff
\mathcal M_m(q,x)\ge0
\quad(q>0,x\in\mathbb R).
\]

### Proof

For real `u`, `1<=P(u)<=9`, so the forward implication is termwise. If `Z`
is not real, the parabolic terminal-pair theorem supplies `t+/-iy`,
`0<y<1/2`, with strict exponent separation. Since

\[
P(iy)=5-4\cosh((\log4)y)>0,
\]

the target pair contributes

\[
-2y^2e^{qy^2}P(iy)^{2m}<0.
\]

For fixed `m`, all nuisance multipliers are bounded on the closed strip, so the
terminal asymptotic is unchanged. For an integer profile `m(q)=o(q)`, the ratio
of any nuisance multiplier to the target multiplier is `e^{o(q)}`. A finite
bounded-window / Gaussian-tail split preserves the strict terminal exponent
gap. Hence the scalar is eventually negative. `square`

For centered zeta zeros, this is an RH criterion.

## Theorem B — exact Q4 prime-side factorization

Let `L=log4` and `(T_a f)(u)=f(u-a)`. The spectral multiplier is

\[
P(v)=5-2e^{iLv}-2e^{-iLv},
\]

so its prime-log operator is

\[
D_L=5I-2T_L-2T_{-L}.
\]

For

\[
h_q(u)=\left(1-{u^2\over2q}\right)e^{-u^2/(4q)},
\qquad H_q(u)=e^{u/2}h_q(u),
\]

one has exactly

\[
e^{u/2}D_Lh_q(u)
=5H_q(u)-4H_q(u-L)-H_q(u+L)
=(I-T_L)(4I-T_{-L})H_q(u).
\]

Because translations commute,

\[
e^{u/2}D_L^{2m}h_q
=(I-T_L)^{2m}(4I-T_{-L})^{2m}H_q.
\]

Thus the filtered prime polynomial

\[
S_m(q,x)=\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
(D_L^{2m}h_q)(\log n)n^{ix}
\]

contains an exact order-`2m` backward difference before absolute values.

## Lemma C — Chebyshev shell transfer

If `G(u)=e^{u/2}g(u)` belongs to `W^{1,1}`, then

\[
\sum_{n\ge2}{\Lambda(n)\over\sqrt n}|g(\log n)|
\ll\|G\|_1+\|G'\|_1.
\]

Split into `e^j<=n<e^(j+1)`. Chebyshev gives total Mangoldt mass `O(e^j)`;
the two critical half-weights give `e^{-j}`, leaving the supremum of `G` on
the shell. Sum the unit-interval Sobolev inequality.

## Lemma D — Gaussian derivative bound

Completing the square,

\[
H_q(u)=e^{q/4}\left(1-{u^2\over2q}\right)
 e^{-(u-q)^2/(4q)}.
\]

With `v=(u-q)/(2sqrt q)`, it is a quadratic polynomial of size `O(q)` times
`e^{-v^2}`. Hermite polynomial bounds imply, for an absolute `A`,

\[
\|H_q^{(r)}\|_1+\|H_q^{(r+1)}\|_1
\le Ae^{q/4}q^{3/2-r/2}(A\sqrt{r+2})^{r+2}.
\]

Repeated integral representation gives

\[
\|(I-T_L)^rF\|_{W^{1,1}}
\le L^r(\|F^{(r)}\|_1+\|F^{(r+1)}\|_1),
\]

and `||(4I-T_-L)^r||_(1->1)<=5^r`.

Consequently

\[
|S_m(q,x)|\ll_m e^{q/4}q^{3/2-m}
\]

for fixed `m`, and, for `m<=q/C0`,

\[
|S_m(q,x)|
\le C_0e^{q/4}q^{3/2}(C_0m/q)^m.
\]

## Lemma E — archimedean reserve

The completed-zeta density satisfies

\[
\mu(t)\ge c\log(2+|t|)-C.
\]

Since `P(u)^(2m)>=1` for real `u`, integrating over
`|u|<=q^(-1/2)` gives

\[
\operatorname{gamma}_m(q,x)
\ge cq^{-3/2}\log(2+|x|)-Ce^{Cm}q^{-3/2}.
\]

The pole term is `O(e^{Cm}(1+x^2)e^{-q(x^2-1/4)})`.

## Theorem F — all-sublinear frontier

Write `ell(x)=log log(2+|x|)`. Comparison of Lemmas D and E proves positivity
whenever

\[
q/4-\ell(x)+(3/2)\log q-m\log(q/(C_0m))\to-\infty,
\qquad m=o(\ell(x)).
\]

For fixed `m>=2`, this holds throughout

\[
q\le4\ell(x)+(4m-6-\varepsilon)\log(2+\ell(x)).
\]

For arbitrary `Delta(t)=o(t)`, put

\[
\Delta^*(Q)=\sup_{1\le t\le Q}\Delta(t)=o(Q)
\]

and choose the least `m<=q/(2C0)` with

\[
m\log(q/(C_0m))\ge\Delta^*(q)/4+3\log q.
\]

The least crossing is `o(q)`. If `q<ell`, the unfiltered exponential margin is
already decisive. If `q>=ell` and `q<=4ell+Delta(ell)`, then

\[
q/4-ell\le\Delta^*(q)/4,
\]

and the chosen order makes the comparison tend to `-infinity`. Thus the
variable-order RH criterion is unconditionally positive through every
prescribed sublinear excess.

## Theorem G — scalar strip-majorant wall

For

\[
G_{q,m}(z)=e^{-qz^2}P(z)^{2m}
\]

and `0<y<1/2`, maximum modulus in `0<=Im z<=1/2` gives

\[
e^{qy^2}P(iy)^{2m}
\le\max\left\{9^{2m},
\sup_t e^{q/4-qt^2}|P(t+i/2)|^{2m}\right\}.
\]

For fixed or sublinear order, the first boundary is eventually smaller than a
fixed terminal amplitude. Hence the shifted critical saddle cannot be made
exponentially smaller than the terminal signal by this scalar analytic filter.
The fixed leading-constant problem requires signed arithmetic beyond an
absolute strip majorant.

## Exact conclusion

The packet proves a new unconditional extension of an RH-equivalent family,
not RH. It eliminates every `o(log log |x|)` correction to the constant-four
frontier and proves why scalar phase-blind filtering alone cannot eliminate the
remaining fixed leading gap.
