# Complete cusp descent for the reunited standard-face series

**Status:** proposed source-conditional composition theorem. The actual
three-cusp output of the second reflection, with every ramified and bad
prime part retained, has the larger holomorphic domain and conductor
mean proved below. This is a theorem about the reunited standard-face
Dirichlet object of PR #920. It is not an identification of that object
with the entire original Möbius fourth moment.

**Authorship:** root. The composition is a new claim requiring its own
independent review at the frozen source commit, in addition to review
of each input.

**Dependencies:** [FINITE_RAY_REUNION.md](FINITE_RAY_REUNION.md),
[FINITE_CUBE_HOMOGENEITY.md](FINITE_CUBE_HOMOGENEITY.md),
[ALL_CUSP_COEFFICIENT_ADAPTER.md](ALL_CUSP_COEFFICIENT_ADAPTER.md),
[SECOND_REFLECTION_BOOTSTRAP.md](SECOND_REFLECTION_BOOTSTRAP.md), and
[SPECTRAL_ROW_MEAN.md](SPECTRAL_ROW_MEAN.md). Their imported theta
foundation and classical sieve assumptions are retained. No zero-free
input is used by this composition.

## 1. The exact function being continued

Use the symbols and literal masks of the reunion theorem, in particular

\[
Q=Nk,\quad \kappa=\eta\rho^3,\quad
w=v-3s+\tfrac32,\quad t=1-s,\quad u=v-s.
\tag{1.1}
\]

On its initial reflected domain, write the exact identity as

\[
\mathscr R_k(w,s)=H(s)Q^{1-2s}\mathcal Y_k(s,v),
\tag{1.2}
\]

where `H(s)` is the explicitly normalized gamma factor in reunion
equation (4.3). Define Y by the right-hand series below, rather than
by division at a zero of H:

\[
\begin{split}
\mathcal Y_k(s,v)=\frac1{L_{S,k}(w,\chi^-_k)}
\sum_{\sigma,c_0}\sum_{\ell\ne0}
&d_\sigma(\ell)F_{\sigma,c_0}(s,k;\lambda^4\ell)
 \overline{\alpha(\ell)}\chi_k(\lambda^4\ell)\,(N\ell)^{-t}\\
&\qquad\times
\prod_{\substack{p\mid\lambda^4\ell\\p\nmid kS}}
\left(1+\frac{\kappa(p)(Np)^{1-v}}{1-x_p}\right).
\end{split}
\tag{1.3}
\]

Here `x_p=chi^-_k(p)(Np)^(-w)` and F is the **actual** reunited finite
function of the cube-homogeneity note, equation (1.2). The first sum
has a fixed finite number of terms. Its k-dependence includes the
original unit Gauss scalar and the original residue classes; it is
not replaced by arbitrary unrelated cusp sequences.

The reunion proof establishes local normal convergence of (1.3) on

\[
\Omega=\{\Re s<0,\ \Re s<\Re v-1\}.
\tag{1.4}
\]

In the variables `a=Re(u)`, `tau=Re(v)`, this is `a>1, tau<a`.

## 2. All bad parts are present in the canonical decomposition

For each supported frequency write uniquely

\[
\ell=\varepsilon\lambda^j n_0n\,(b_0b)^3.
\tag{2.1}
\]

The indices n,b are primary and prime to S, n is squarefree, and
`(n,b)=1` is **not** required. The index n0 is squarefree and supported
on `S` away from lambda, so has only finitely many possibilities. The
index b0 is arbitrary and supported on the same finite set of primes.
The allowed j,epsilon are exactly the complete support table of the
coefficient adapter: `j>=-4` with its stated congruence and unit
restrictions, including the two nonstandard cusp sectors at j=-4.

Freeze these bad labels and a pair sigma,c0. The actual finite
multiplier, including the intrinsic nonstandard-cusp additive phase,
has the cube covariance

\[
F_{\rm sector}(z c^3)=\overline{\rho(c)}^{\,3}
F_{\rm sector}(z)
\tag{2.2}
\]

on primary good residues. This holds even though the frozen factor
`epsilon lambda^(j+4)n0 b0^3` can be a nonunit at the bad modulus:
the finite-cube theorem holds for every integral argument, before
restriction to its good variable z. The intrinsic phase is unchanged
by primary cubes because `c^3-1` belongs to `lambda^4 O`.

Finite character orthogonality, together with the exact coefficient
adapter, therefore expresses this sector as a fixed finite sum of
canonical good parts indexed by varrho, with

\[
\varrho^3=\overline\rho^{\,3}.
\tag{2.3}
\]

The additional character arising from the Gauss CRT split at n0 is
cubic and does not alter (2.3). The fixed ray group may be chosen once
for all j,n0,b0: their residue data take only finitely many values at
the fixed bad modulus. Its cardinality is independent of k.

The remaining good coefficient is exactly

\[
\begin{split}
&\overline{\alpha(n)}\gamma_2(n)\varrho(n)\chi_k(n)\\
&\qquad\times
\overline{\alpha(b)}^{\,3}\varrho(b)^3\chi_k(b)^3\sqrt{Nb}.
\end{split}
\tag{2.4}
\]

The notation `chi_k(n)` here denotes the same row twist as in the
companion bootstrap; when written with the reciprocal primary
orientation `chi_n(k)`, separate the fixed reciprocity residue
classes and absorb the resulting finite characters into the fixed
ray family. The cube and CRT identities are in the inherited
convention throughout. The finite partition of k can be retained as
a subset in the spectral row theorem. All row factors at a frozen
bad index have modulus at most one.

At good primes outside k the finite deformation product in (1.3)
is now precisely the product over `p|nb` in the bootstrap's definition
of `Z_k(s,v;varrho)`. A prime dividing k is still omitted; its
nonunit contribution in the n or b row character is zero. Consequently
the complete exact representation is

\[
\boxed{
\mathcal Y_k(s,v)
=\sum_{\sigma,c_0,j,\varepsilon,n_0,b_0,\varrho}
B_{\sigma,c_0,j,\varepsilon,n_0,b_0,\varrho}(s,k)
\mathcal Z_k(s,v;\varrho).
}
\tag{2.5}
\]

This formula first follows by absolute rearrangement on
`Re(v)<1, Re(u)>1`. The coefficients B mean exactly: insert the
frozen labels in (1.3), use the explicit table and Gauss CRT, then
take ordinary multiplicative Fourier coefficients of the remaining
finite function on its primary unit group. This specifies them
uniquely after fixing that group and includes every original phase.
No estimate substitutes for this coefficient identity.

They satisfy, on every bounded real s-strip,

\[
|B_{\sigma,c_0,j,\varepsilon,n_0,b_0,\varrho}(s,k)|
\ll
3^{-j(\Re t-1/6)}(Nb_0)^{-(3\Re t-1/2)},
\tag{2.6}
\]

uniformly in k and Im(s). To verify the bound, the table gives
`|C_sector|<=27*3^(j/6)`; the norm power contributes
`3^(-j Re(t))(Nn0)^(-Re(t))(Nb0)^(-3Re(t))`; the cube coefficient
contributes `sqrt(Nb0)`. The finitely many n0 values are harmless on
a bounded real strip. Every remaining Fourier coefficient is bounded
by the supremum of a function on a fixed finite group. The factors
`(Nc0)^(1-2s)` are also bounded uniformly in Im(s), and the row
Gauss and angular factors have modulus at most one.

It follows in particular that the total absolute B-mass is uniformly
bounded on strict strips with `Re(t)>1/6`: the j sum is geometric,
and the finite-bad-prime b0 sum converges when `3Re(t)-1/2>0`.
All domains below have `Re(t)>1`, so these summations have ample
strict margins. Dependence of B on k need not be periodic for this
bound; bounded multiplication in the row norm suffices.

## 3. A larger domain for the actual complete function

### Theorem 3.1

The exact complete function Y extends holomorphically to

\[
\boxed{
\mathcal D=\left\{(s,v):
a=\Re(v-s)>\tfrac12,\quad
\tau=\Re v<\min\left(a,\frac{3a-1}{2}\right)\right\}.
}
\tag{3.1}
\]

Thus `R_k(w,s)=H(s)Q^(1-2s)Y_k(s,v)` continues holomorphically
there as well. On bounded closed real subregions with strict margins,

\[
|\mathcal Y_k(s,v)|
\ll Q^{\max(0,1-a)+\epsilon}
 (2+|\Im s|+|\Im v|)^M.
\tag{3.2}
\]

### Proof

On `a>1, tau<a`, this is the existing domain Omega and its absolute
bound for Y. On `1/2<a<=1`, (3.1) is precisely
`tau<(3a-1)/2`, hence tau<1 and the bootstrap's new domain applies.
More generally use the overlap domain

\[
\mathfrak N=\{a>\tfrac12,\ \tau<1,\ 3a-2\tau>1\}.
\tag{3.3}
\]

The bootstrap theorem supplies a normally convergent divisor series
for each Z and its bound `Q^(max(0,1-a)+epsilon)`, with polynomial
vertical growth. In this domain `Re(s)=tau-a<0` and
`Re(t)=1+a-tau>1`. Bound (2.6) therefore makes (2.5) locally
normally convergent and permits summing the quantitative bound over
every bad and ramified label. It is an identity with (1.3) on the
nonempty open overlap `tau<1, a>1`.

The union `Omega union mathfrak N` is exactly (3.1): for a>1,
the minimum is a; for a<=1, it is `(3a-1)/2`. The matching
holomorphic functions consequently glue to the same function on
that whole domain. The two defining upper bounds are affine, so
the domain is connected and convex. They also imply `Re(s)<0`,
where the gamma factor H has no poles. This proves the claim for R
and the estimate (3.2). No reciprocal outside an absolute Euler
half-plane occurs in this argument. QED.

This includes the old pole cancellation through v=1 on its stated
overlap; no possible finite-character pole is reintroduced by the
larger-domain formula.

## 4. Conductor mean for all its reflected cusp contributions together

### Theorem 4.1

On a closed real subregion of

\[
\frac58<a=\Re(v-s)<1,
\qquad \tau=\Re v<\frac{3a-1}{2},
\tag{4.1}
\]

with strict margins and bounded real coordinates,

\[
\boxed{
\sum_{\substack{Q\le Nk<2Q\\ k\ {\rm squarefree},\ (k,S)=1}}
|\mathcal Y_k(s,v)|^2
\ll Q^{1+\epsilon}
(2+|\Im s|+|\Im v|)^M.
}
\tag{4.2}
\]

Equivalently, on the same subregion,

\[
\sum_{k\sim Q}^{*}|\mathscr R_k(w,s)|^2
\ll Q^{3-4\Re s+\epsilon}
(2+|\Im s|+|\Im v|)^{M'}.
\tag{4.3}
\]

### Proof

The spectral theorem and bootstrap Proposition 6.1 give
`||Z||_ell2 << Q^(1/2+epsilon)` times a fixed polynomial in the
imaginary parts. These statements are uniform over the finite ray
family in (2.3) and over the fixed row residue subsets used to put
the twists in their canonical orientation. Apply Minkowski to the
actual sum (2.5), retaining the supremum in k of each B. The sum of
those suprema converges by (2.6). This proves (4.2), including all
cross terms between the different cusp and bad labels. It does not
discard those cross terms or claim orthogonality. Multiplying (1.2)
back and using the fixed-strip polynomial gamma bound proves (4.3).
QED.

## 5. Quantitative meaning for the moment route

The scalar in the inherited balanced Mellin representation, after
the row power in (1.2) cancels, is `D^(v-2s)`. In (4.1) its norm
exponent is `2a-tau`. The greatest permitted tau for a fixed a is
`(3a-1)/2`, so its infimum is `(a+1)/2`, tending to `13/16` as a
decreases to 5/8. Every actual application stays strictly inside the
domain. This scalar calculation is not a zero-free boundary.

Even when a legitimate compactly weighted completed covariance
inherits the resulting candidate energy `Q D^(13/8+epsilon)`, it
does not improve the minimum of the two existing physical estimates
`D(Q+Q^2)` and `Q+D^2+(QD^2)^(2/3)`. The exact exponent comparison
is recorded in the bootstrap note. At the long dual scale near
`Q=D^(3-theta)` it remains inadequate.

There is a stronger limitation of this specific contour-and-Minkowski
mechanism. If the spectral threshold 5/8 were replaced by any
`1/2<=a0<1`, its same divisor summation would give the candidate energy
`Q D^(1+a0+epsilon)`. For `Q<=D^a0`, the old factorwise bound is
at most twice that candidate. For `Q>=D^(1-a0)`, each term of the
classical bound is at most that candidate: the middle term uses the
displayed condition, and the mixed term only requires
`Q>=D^(1-3a0)`, which holds for Q>=1. Since `1-a0<=a0`, these two
ranges cover every Q>=1. Thus even lowering the spectral threshold
to 1/2 alone would not improve the old physical envelope through this
same mechanism. This observation, suggested by scale_covariance_attack,
does not rule out using the analytic family in a different joint
covariance argument.

The newly proved interface is that the complete reflected coefficient
system belongs to the canonical family needed by the shifted-variable
argument, with all its finite masks and infinite ramified sums under
control. The missing step toward the requested moments is a stronger
estimate for the actual signed covariance, uniform in its growing
auxiliaries and all row valuations, together with the passage back
through cube completion. The analytic domain by itself does not supply
that estimate.
