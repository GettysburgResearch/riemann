# A certified lower bound in the original finite-prime physical norm

Status: complete written proof plus a preregistered directed-ball certificate;
independent exact-SHA review required. No RH conclusion.

This closes a different gate from the Euclidean coefficient-frame bounds in
PR #783. The norm below is the original continuous observation norm, with its
actual kernel and every arithmetic alias. The result is for the fixed primes
`(2,3,5)`, not uniformly over growing prime sets.

The pre-computation design is frozen at
`8113cb407b6c7b2e64943b4485ead37b7ac0ccc3`. The first and only node panel was
`t_j=j`, `j=1,...,64`, at exactly 1024 bits. No node replacement, precision
ladder, subset search, or new prime was used. The matching producer, fixture,
source manifest and tests have stem `native_physical_coercivity_pass4`.
The manifest binds 25 exact source versions, including the earlier protected
tuple audits and this pass's design. It does not assert that those source
reductions prove RH.

## 1. The literal completed observation

At PR #770 head `9421846721cd788ab01615c8b6d459d9de849df7`, the source proofs
`FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md`,
`INFINITE_NATIVE_PHYSICAL_FAITHFULNESS.md`, and
`EFFECTIVE_FULL_SUPPORT_THEOREM.md` define

\[
A(z)=\sqrt{1-z^2},\quad C(z)=\sqrt{1-z},\quad
x_p(t)=p^{-1/2+it},\quad y_p(t)=\overline{x_p(t)}.
\]

Both roots use their value-one branches in the unit disk. For binary words
`a in {0,1}^3`, let `s_a(x)` be the product of A/C chosen by that word, with
primes in order `(2,3,5)`. Define the 64 functions

\[
\phi_{ab}(t)=s_a(x(t))s_b(y(t)),\qquad
F_M(t)=\sum_{a,b}M_{ab}\phi_{ab}(t),\quad M\in\mathbb C^{8\times8}.
\tag{P4.1}
\]

The matrix need not be Hermitian. The source matrix of an actual path already
contains its literal factor `2 integral d(psi_a) psi_b`, with
`psi=(1-u,u)` locally. No extra factor two is inserted or removed here.
Absolute convergence at the fixed primes identifies (P4.1) with the complete
sum of `v_n^t M v_m/sqrt(nm) * exp(it log(n/m))`. In particular every `1/d`
equal-ratio alias remains present; the radical evaluation is an exact closed
form for the whole infinite series, not an arithmetic truncation.

Use precisely

\[
d\nu(t)=\frac{|\widehat\kappa(t)|^2}{2\pi}\,dt,
\quad \kappa(u)=K_L(e^u),
\]
\[
K_L(y)=\begin{cases}
8-4\sqrt y,&1\le y<2,\\
-8(1+\sqrt2)+4\sqrt2\sqrt y,&2\le y<4,\\
8\sqrt2-2\sqrt y,&4\le y<8,\\
0,&\text{otherwise}.
\end{cases}
\tag{P4.2}
\]

### Theorem

For every complex matrix M in the declared A/C coordinates,

\[
\boxed{2^{-153}\|M\|_F^2
\le \|F_M\|_{L^2(\nu)}^2
\le 2^{27}\|M\|_F^2.}
\tag{P4.3}
\]

For the original monomial schedule matrix `M_orig`, the same physical field
satisfies

\[
\boxed{2^{-165}\|M_{\rm orig}\|_F^2
\le\|F\|_{L^2(\nu)}^2
\le2^{39}\|M_{\rm orig}\|_F^2.}
\tag{P4.4}
\]

These bounds restrict to every actual path-current variation, but do not
assert that arbitrary tensor matrices are path-attainable. Their conservative
constants are not claimed optimal or numerically well conditioned.

## 2. Global analytic bounds, with no numerical quadrature

For real t and p in `(2,3,5)`, both local functions have modulus below 2.
Their derivatives obey

\[
|A(x_p(t))'|\le\frac{(\log p)/p}{\sqrt{1-1/p}}\le\log p,
\quad
|C(x_p(t))'|\le
\frac{(\log p)/\sqrt p}{2\sqrt{1-1/\sqrt p}}<\log p.
\]

For the latter, `sqrt(1-1/sqrt(2))>1/2`. The reflected factors obey the same
bounds. Thus `|s_a|<8`, `|s_a'|<4 log(30)<16`, and

\[
|\phi_{ab}|<64,\qquad |\phi_{ab}'|<256,\qquad
\|\phi(t)\|_2\le512,\quad \|\phi'(t)\|_2\le2048.
\tag{P4.5}
\]

The inequalities `log(30)<4`, `log(8)<3` can be obtained from finite positive
Taylor lower bounds for `exp(4)` and `exp(3)`. From (P4.2), `|kappa|<12` on
`[0,log(8)]`. Hence Plancherel and differentiation under the compact integral
give

\[
\nu(\mathbb R)=\int|\kappa|^2<432<2^9,
\quad |\widehat\kappa'(t)|
\le\int_0^{\log8}u|\kappa(u)|du<54.
\tag{P4.6}
\]

(P4.5)-(P4.6) prove the upper bound in (P4.3). The exact inherited mass is
`128(3+sqrt(2))log(2)-288`; using a coarser upper bound does not change the
measure. The zero of kappahat at the origin is not discarded; the fixed
sampling nodes start at 1.

## 3. The finite certificate and its trust boundary

Let `V[j,(a,b)]=phi_ab(j)`, with binary lexicographic column order. Directed
ACB evaluation encloses all 4096 entries. Opposite phases and conjugation
provide an additional source-symmetry check, not an independent implementation
of the numerical library.

An inverse computation supplies a candidate. Its entrywise exact dyadic
midpoint matrix W is then checked separately by directed multiplication:

\[
\epsilon=\|WV-I\|_\infty<1/2,
\qquad
\|V^{-1}\|_\infty
\le\frac{\|W\|_\infty}{1-\epsilon}\le2^{33}.
\tag{P4.7}
\]

The fixture retains exact rational upper bounds for the residual, candidate
norm and Neumann quotient. Thus containing the identity in a wide interval
matrix alone is not an acceptance rule. Both inverse-product containments
are additional controls. Since `||V^-1||_2<=8||V^-1||_infinity`,

\[
\sigma_{\min}(V)\ge2^{-36}=:\sigma.
\tag{P4.8}
\]

Each kappahat value is evaluated from the exact antiderivatives on the three
logarithmic intervals: for constants `a,b` and interval endpoints `l,h`,

\[
\int_l^h(a+b e^{u/2})e^{-itu}du
=a\frac{e^{-ith}-e^{-itl}}{-it}
+b\frac{e^{(1/2-it)h}-e^{(1/2-it)l}}{1/2-it}.
\tag{P4.9}
\]

The same fixed panel certifies

\[
\min_{1\le j\le64}|\widehat\kappa(j)|\ge2^{-12}=:\eta.
\tag{P4.10}
\]

The arithmetic contract is MIXED: CERTIFIED_BALL for transcendental and
matrix bounds, EXACT_RATIONAL for summaries and the tuple arithmetic, and
CERTIFIED_INTEGER_COVERAGE for finite indexing. All transcendental quantities
use directed balls at 1024 bits; displayed dyadic bounds are outward rational
summaries. The analytic integrals and source imports are proved here, not
machine-certified by the finite fixture. The trust base is the pinned
python-flint 0.9.0 / FLINT 3.6.0 implementation and its 44 hashed native
files, not a formal verification of that implementation. Matrix error-bound
semantics are documented by
[FLINT](https://flintlib.org/doc/acb_mat.html); the independent Neumann
residual in (P4.7) supplies the mathematical acceptance test.

## 4. From point samples to the unchanged physical norm

Put `delta=2^-51`. The 64 intervals `[j-delta,j+delta]` are disjoint. For a
coefficient vector m and every real `|s|<=delta`, (P4.5) gives

\[
\|[F_M(j+s)-F_M(j)]_{j=1}^{64}\|_2
\le8\cdot2048\delta\|m\|_2
=\frac\sigma2\|m\|_2.
\]

Together with (P4.8), this yields

\[
\sum_{j=1}^{64}|F_M(j+s)|^2\ge\frac{\sigma^2}{4}\|M\|_F^2.
\tag{P4.11}
\]

Equations (P4.6) and (P4.10) give
`|kappahat(j+s)|>=eta-54delta>=eta/2`. Since `pi<4`, the original measure
density on every interval is at least `eta^2/32`. Integrating (P4.11) over
`s in [-delta,delta]`, and using disjointness, proves

\[
\|F_M\|_\nu^2\ge
\frac{\delta\sigma^2\eta^2}{64}\|M\|_F^2
=2^{-153}\|M\|_F^2.
\]

No replacement of the physical measure by 64 point masses occurs. Point
evaluation bounds are used only to prove a bound on genuine intervals of
the original integral. No physical Fourier-coefficient extraction estimate
is assumed.

For (P4.4), the source-exact coordinate change is
`M_AC=T^t M_orig T`, where
`T=[[1,0],[-1,1]]` tensor power three. The local matrix and its inverse have
Euclidean norm below 2, so `||T||_2,||T^-1||_2<8`. The resulting congruence
and its inverse have Frobenius operator norm below 64. Applying (P4.3)
proves (P4.4). This is a quantified coordinate comparison, not a change of
the physical norm.

## 5. An explicit eventual finite-horizon consequence

In the A/C basis the complete coefficient absolute sum is
`sum_n ||v_n||_1=64`. The exact hyperbolic tail therefore gives

\[
\|F_{H,M}-F_M\|_\nu
\le\sqrt{\nu(\mathbb R)}\,4096 H^{-1/2}\|M\|_F
<2^{17}H^{-1/2}\|M\|_F.
\tag{P4.12}
\]

Consequently every integer `H>=2^190` satisfies

\[
2^{-155}\|M\|_F^2\le\|F_{H,M}\|_\nu^2\le2^{28}\|M\|_F^2.
\tag{P4.13}
\]

Indeed the error is at most `2^-78||M||_F`, less than half the completed
lower norm `2^(-153/2)||M||_F`. The upper bound follows from (P4.3) and
the same triangle inequality. The original monomial lower bound is
`2^-167`. This threshold is deliberately very conservative and is not
intended to improve the existing rank threshold H3 or fill its finite gap.
It gives an actual uniform-in-H physical norm statement for fixed primes.

## 6. Exactly what has and has not improved

PR #783, frozen at `9497db89e34669e2167c632c918c491bf6ee73ab`, proves lower
bounds for `||D R_H m||_ell2` and conditions `W D^-1(D R_H)`. These are
valid coefficient-observation statements, but are not by themselves
(P4.3). Its local tensor factorization is compatible with this result; its
inverse constants are not inputs to our certificate.

The present bound is for the original continuous physical norm and supplies
bounded dual recovery on this finite-dimensional image. It does not yield
prime-uniform coercivity: local schedule variation contains
`C(p^-1/2+it)-A(p^-1/2+it)=O(p^-1/2)`. A fixed raw-coordinate order swap
involving a new large prime can therefore have vanishing physical size.
Artificially normalizing that direction must also price the inverse source
map. No such growing-prime theorem is asserted here.

The result does not identify the full retained-gamma tuple coefficient,
choose arbitrary path mixtures, prove an infinite-horizon optimizer, or
provide a principal-moment estimate. The separate tuple note identifies the
remaining source/measure input precisely. Existing frozen sources and
failures remain unchanged.

## 7. Finite verification and exclusions

The resident suite contains 20 tests, replayed normally and with Python -O.
Six fully resealed mutations must still fail a fresh, complete reconstruction:
the lower exponent, physical measure, integer-versus-Boolean node type,
unresolved gamma status, primitive Git blob, and proof-artifact seal. The
suite also checks strict JSON caps, exact interval-to-integral inequalities,
the coordinate map, all tuple histories and independent Boolean definitions.
No assertion statement is an acceptance guard in the producer.

Each reconstruction authenticates all 25 commit/blob/LF source bindings,
all six resident artifact seals and the pinned numerical runtime. Both
producer checks and all four normal/-O fixture/source emissions are part of
the release replay. A clean detached replay and non-author proof review are
required after the science commit; self-tests alone are not that review.
