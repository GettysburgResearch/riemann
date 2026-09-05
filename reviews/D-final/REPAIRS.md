# Reviewer D — closeout repairs and completed proof adapters

Status: proposed exact review deductions for integrator review; no source is
rewritten and no canonical status is changed here. Baseline main is
`8d16f8d9c475db290bc85e53d775b93b9bcdb336`. The first D report at
`55a7371432760ff44d396f6e63d95d65e64ad2a5` remains immutable.

S01–S31 refer to this directory's exact source ledger. P/M references refer to
`../D/SOURCES.tsv`. Finite checks supplement, but do not prove, the analytic
arguments. None of the repairs below supplies an RH-bearing arithmetic sign.

## R11 / D-F08 — the live-marginal Farkas dual has the wrong sign

**Source:** S01, L-94023 §3. **Canonical consumer:**
`ARITH.LIVE_MARGINAL_FARKAS`.

For the printed primal

```
A z=b,  G z>=0,  z>=0,
```

the source's proposed obstruction is

```
A^T u+G^T v>=0,  v>=0,  b^T u<0.
```

These are NOT alternatives. Take the one-dimensional data
`A=G=b=1`. The primal has `z=1`, while `u=-1,v=1` satisfies the
printed obstruction: its first left side is zero and `b*u=-1`.
The failure is algebraic, not a numerical precision issue.

**Replacement:** exactly one of the primal and

```
A^T u-G^T v>=0,  v>=0,  b^T u<0
```

holds, over the real numbers. Introduce slack `s>=0` and write the primal as

```
[A 0; G -I] [z;s]=[b;0],  [z;s]>=0.
```

The ordinary equality-form Farkas alternative gives a dual `(u,w)` with
`A^T u+G^T w>=0`, `-w>=0`, and `b^T u<0`. Put `v=-w`.
Direct incompatibility also follows from

```
b^T u=z^T(A^T u-G^T v)+v^T Gz>=0
```

at every feasible primal/dual pair. Completeness is the standard
finite-dimensional separation theorem for the finitely generated cone.

The source's common-template primal construction remains meaningful.
Feasibility of the actual marginal is still open. Integrators must fix both
prose and any checker which copies the plus-sign obstruction before treating
such an obstruction as a proof of infeasibility.

## R12 / D-F09 — real Farkas separation does not guarantee rational witnesses

**Source:** S02, L-91671 §§5–6. Its dual SIGN is correct for its different
primal convention `Bx=b,Gx<=c,x>=0`:

```
B^T y+G^T z>=0,  z>=0,  b^T y+c^T z<0.
```

Do not apply R11's minus-sign edit to this source.

What needs qualification is the statement that one can always return a
*rational* obstruction for finite real data. Let

```
B = [[1,-1],[sqrt(2),-sqrt(2)]],  b=(0,-1),  x>=0.
```

The first equality forces `x1=x2`; the second then says `0=-1`.
The primal is infeasible. Its real dual conditions force

```
y1+sqrt(2)y2=0,  y2>0.
```

There is a real separator `(-sqrt(2),1)`, but no rational separator: if
`y1,y2` were rational and `y2>0`, their ratio would make `sqrt(2)` rational.
Likewise `x=sqrt(2)` is a feasible real equality with no rational primal
solution.

**Replacement contract:** rational input matrices and right sides admit
rational feasible solutions or rational Farkas separators. This follows by
normalizing the strict dual inequality to `-1` and choosing a basic feasible
solution of the resulting rational linear system. For algebraic data, work
in a declared effective real algebraic field. For general exact expressions
in logarithms, a real existence theorem does not supply a terminating
rational certificate algorithm. Equality rows must be checked symbolically,
not replaced by small interval residuals. Outward intervals suffice for
strict sign tests only after the needed weak inequalities/equalities have
been established.

The atomwise allocation summation and nonduplication identity in S02 are
unaffected. The counterexample rejects the unrestricted certificate claim,
not finite-dimensional real Farkas duality or actual-source feasibility.

## R13 / D-F10 — one-sided jump dissipation requires a real part

**Source:** S03, L-91029.9, with the two different operator actions separated.

For a finite positive jump measure and unitary operators `D_t`, let

```
L_vec f = integral (D_t f-f) dnu(t).
```

Then the correct identity is

```
-Re <f,L_vec f> = (1/2) integral ||f-D_t f||^2 dnu(t).
```

It follows by expanding the squared norm and using unitarity. Removing
`Re` is false: with one unit jump, `f=1,D_t=-i`, the left side without `Re`
is `1+i` while the right side is `1`.

This is relevant to the actual positive prime measure, not just the toy
example. At a safe Euler line the first jump moment is finite and strictly
positive. Hence the imaginary part of
`integral(1-exp(-i theta t))dnu(t)` has derivative
`integral t dnu(t)>0` at zero. It is nonzero for sufficiently small positive
`theta`. Positivity of the jump measure does not make the one-sided
convolution generator self-adjoint.

The source also defines the distinct matrix action

```
L_mat(X)=integral(D_t X D_t^*-X)dnu(t).
```

On Hilbert–Schmidt matrices the matching identity is

```
-Re Tr(X^*L_mat(X))
   =(1/2) integral ||D_t X D_t^*-X||_HS^2 dnu(t).
```

Use this formula for arbitrary complex `X`. For self-adjoint `X` the scalar
inner product is real, but that restriction must be explicit. On diagonal
matrices, diagonal-unitary conjugation is the identity; it is not the vector
multiplication action.

The positive Euler logarithm, finite compound-Poisson measure for `sigma>1`,
completely positive random-unitary semigroup, and alternating Euler-log
moment derivatives survive. Explicit jump Gram kernels remain PSD. An
unqualified assertion about all iterated carré-du-champ tensors requires a
definition and its own argument; it is not needed for the surviving first
jump identity. Symmetrizing the jump measure is another way to get a
self-adjoint generator, but it changes the original source and must be
labeled as such. Critical analytic continuation remains open.

## R14 / D-F11 — normalize the high-carrier Fredholm leading term consistently

**Sources:** S04, HC.7–HC.15; S05, FP.1–FP.10. The latter inspection covers
sections 1–4 and the beginning of §5, not the full cardinal capture proof.

The inherited zero form uses the unnormalized Fourier transform
`fhat(t)=integral f(u)exp(itu)du`. This is also fixed by S05's evaluation-vector
formula and its `1/(2pi)` Plancherel factor. The Weil gamma contribution is

```
integral mu(t)|fhat(t)|^2 dt,
mu(t)=[Re psi(1/4+it/2)-log pi]/(2pi).
```

With `J=M_(exp(-sigma u^2))(1-d^2/du^2)^(-1)` on `L2(du)` and `B=J^*J`,
a constant Fourier density `mu(T)` therefore contributes

```
mu(T) integral |(Jh)^hat(t)|^2 dt = 2pi mu(T)<h,Bh>.
```

Thus, at the inherited normalization, HC.14 must read

```
A_T=c_Tilde B+E_T,
c_Tilde=2pi mu(T)=Re psi(1/4+iT/2)-log pi,
sup_(T>=3)||E_T||_1<infinity.
```

One can instead divide the ENTIRE Weil form and operator by `2pi`; then the
source's printed `c_T=mu(T)` is appropriate. Rescaling only the gamma
coefficient is not appropriate, because the prime and zero sides fix the
same overall normalization.

This is not an error absorbable in the bounded remainder. In fact

```
Tr B = ||(1/2)exp(-|u|)||_2^2 integral exp(-2sigma u^2)du
     = (1/4)sqrt(pi/(2sigma)) >0.
```

The missing term is `(2pi-1)mu(T)B`, of trace norm comparable to `log T`.

**Proof of the corrected remainder statement.** Use the unitary Fourier
transform and the multiplier `Omega=2pi mu`. Stirling plus the compact
bound gives, uniformly for `T>=3`,

```
|Omega(T+t)-Omega(T)| <= C[1+log(2+|t|)].
```

For example the difference of `log(2+|T+t|)` and `log(2+T)` is bounded by
`log(1+|t|)`, and the difference between `Omega` and that logarithm is
bounded. The Fourier kernel of the unitary transform of `J` is a Gaussian
convolution followed by `(1+xi^2)^(-1)`. Consequently its squared
Hilbert–Schmidt norm after multiplication by
`|Omega(T+t)-Omega(T)|^(1/2)` is bounded by

```
C_sigma integral integral
 (1+log(2+|t|)) |w_hat(t-xi)|^2/(1+xi^2)^2 dt dxi < infinity.
```

Factor through this Hilbert–Schmidt map to bound the trace norm. For prime
translations, the exact overlap bound in FP.8 is unchanged by unit-modulus
carrier phases; its entire prime-power sum is trace-norm convergent.
The pole evaluation vectors have uniformly bounded norm. These facts prove
the corrected formula without an RH assumption.

For sufficiently large `T`, `c_Tilde>0` and diverges. Then
`A_T/c_Tilde -> B` in trace norm. Since `J` is injective and infinite rank,
`B` has infinitely many distinct positive eigenvalues. Every fixed exterior
coefficient and every fixed shifted-Hankel matrix has a strictly positive
limiting normalization, so the fixed-degree blindness conclusion survives.
The small-`T` division by `c_Tilde` is neither needed nor licensed at its
zeros. Exact exceptional-zero capture remains conditional here on the
separately identified cardinal-source theorem; this closeout does not
reprove that theorem.

## R15 — fill the reciprocal-zeta/Hardy upper-bound adapter

**Sources being completed:** first-pass P14/P15 (L-100130/131). This argument
concerns the correctly normalized Cauchy–Poisson energy, not the distinct
older Hardy energy. The latter retains first-pass repair R4.

Let `Theta` be the supremum of real parts of nontrivial zeta zeros. The
following familiar analytic ingredients are imported explicitly: zeta's
continuation, simple pole at one and polynomial vertical growth on fixed
strips; the absence of real nontrivial zeros; Borel–Carathéodory; Hadamard
three-lines; Fourier/Laplace Plancherel and the right-half-plane Hardy
Paley–Wiener theorem. No RH or quantitative bound on `Theta<1` is assumed.

### 1. Reciprocal growth inside the zero-free half-plane

For every fixed `a>Theta` and every `epsilon>0`,

```
|1/zeta(w)| <= C_(a,epsilon)(2+|Im w|)^epsilon,  Re w>=a.
```

For `a>1` this is the absolutely convergent Euler product. Otherwise
`Theta<1`. Choose `Theta<alpha0<alpha<a<b`, with `b>1`, and set

```
g(w)=(w-1)zeta(w)/(w+1).
```

This is holomorphic and zero-free on `Re w>Theta`, including at `w=1`.
There is an analytic logarithm `L=log g`, chosen to agree on `Re w>1` with
the Euler logarithm and the logarithm of `(w-1)/(w+1)`. On `Re w=b`, `L`
is bounded. On `Re w=alpha`, Borel–Carathéodory on discs centered at a fixed
real number to the right of one plus `it`, with outer left edge `alpha0`,
gives `L(alpha+it)=O(log(2+|t|))`. The real part is bounded above by the
polynomial vertical growth of zeta; the center value is bounded by the
chosen Euler branch. Small heights are covered by compactness.

For a fixed height `t0`, apply three-lines on `[alpha,b]` to

```
L(w) exp((w-a-it0)^2).
```

The Gaussian factor makes the boundary suprema bounded by
`C log(2+|t0|)` on the left and `C` on the right. The same vertical growth
ensures decay at horizontal infinity. Therefore

```
|L(a+it0)| <= C [log(2+|t0|)]^theta,
theta=(b-a)/(b-alpha)<1.
```

The proof is uniform for real parts between `a` and `b`. Exponentiating and
using `log(t)^theta=o(log t)` gives the asserted subpolynomial bound. The
factor `(w-1)/(w+1)` is harmless, and Euler convergence treats `Re w>=b`.
At `w=1`, `1/zeta` has its removable zero.

### 2. The missing uniform Hardy norm

Fix `sigma0>Theta+1/2`. The exact compact-wavelet multiplier satisfies

```
|Khat(sigma+it)| <= C_(sigma0)(1+|t|)^(-2), sigma>=sigma0.
```

This follows directly from its rational multiplier and bounded dyadic
factors; the relevant real parts are above one. For real `gamma` set

```
F_gamma(s)=Khat(s)/zeta(s-1/2+i gamma).
```

It is holomorphic in `Re s>Theta+1/2`. Taking `0<epsilon<1/2` in the
reciprocal bound gives

```
|F_gamma(sigma+it)|^2
 <= C (1+|t|)^(-4+2epsilon)(1+|gamma|)^(2epsilon)
```

uniformly in `sigma>=sigma0`. The integral in `t` is finite, and the
subsequent integral in `gamma` against `d gamma/[pi(1+gamma^2)]` is finite.
This proves an actual half-plane `H2` bound, not just one finite boundary
integral of a meromorphic expression.

Hardy Paley–Wiener supplies a causal inverse in logarithmic scale. On the
initial absolute-convergence half-plane `Re s>3/2`, it agrees with the
literal finite-source function from L-100130 by Laplace uniqueness. Thus
it is that same source on the entire half-line. Tonelli and Plancherel
now give finiteness of the weighted Cauchy–Poisson energy for every
`sigma0>Theta+1/2`.

The lower bound is the pole argument already reviewed: finite weighted
energy gives a holomorphic Laplace transform for almost every phase;
an uncancelled reciprocal-zeta pole to its right is impossible. The
compact multiplier has no zeros at the relevant shifted zero locations.
Hence the energy abscissa, as an INFIMUM, equals `Theta+1/2`.
Nothing here asserts convergence at the boundary abscissa. This completes
that analytic adapter without asserting any unconditional critical energy
bound or the original false energy identity.

## R16 — Bellman heredity needs no second positivity theorem

**Sources:** S17–S19 and first-pass P39–P41.

The discrete comparison in L-98020 retains repeated-prime corrections:
ordered tuples and squarefree subsets are not identical. The union bound
on repeated coordinates contributes
`e^M sum_(p>=z)p^(-2)/2`; telescoping convolution CDFs contributes
`2 Delta e^M`. Their sum gives the printed absolute Dickman discrepancy.
Prime endpoint atoms, including `p=z` when present, belong in `Delta`.

The full-base profile argument is valid for `u>=1`, a fixed positive
`eta<1/2`, `integral x^eta |dh|<infinity`, and positive total mass `a_*`.
If `L>=C log(u+2)`, the classical logarithmic derivative bound for Dickman
makes the signed convolution equal `a_*rho(u)` up to relative
`O(log(u+2)/L)`. Splitting the integral at `uL` retains the full tail.
Use `0<eta<1/2`; the printed phrase 'any eta<1/2' is insufficient for a
positive exponential-moment argument. The numerical `J_*` interval is not
needed for positivity and is not regenerated here.

Given the resulting STATE positivity, the exact least-prime identity

```
U(Y,p)=U(Y,p^+) - p^(-1) U(Y/p,p^+)
```

immediately proves

```
U(Y,p^+) >= p^(-1) U(Y/p,p^+)  iff  U(Y,p)>=0.
```

Thus at identical states this Bellman inequality is not logically stronger
than state positivity. Apply the state theorem at each descendant that
satisfies the same corridor hypotheses and sufficiently-large-endpoint
condition. No uniform iteration outside the corridor follows. This avoids
an unnecessary comparison that treats the next-prime cutoff as if it had
exactly the old `log p` coordinate.

The *actual P61* weighted-variation assertion still depends on its repaired
base expansion and derivative formula. Those primitive source formulas have
not been independently reconstructed in this closeout. The corridor retains
that explicit input and the named classical VK/de Bruijn estimates; it is
not promoted to a fixed-small-prime theorem.

## R17 — critical Taylor scope and a converse for negative mass

**Sources:** S06–S08. Positive kernels and all `m>=2` supercritical signs do
not establish the critical sign. For each fixed integer `m>=2`, the critical
kernel and its meromorphic Mellin formula are correct in the displayed
fundamental strip. The low-`X` polynomial removes every real pole `s=j/2`,
`j>=2`, and the reciprocal-zeta zero removes `s=1/2`. The Landau implication
therefore applies under its fixed-object, finite-abscissa and local
integrability hypotheses.

The source proves eventual positivity SUFFICIENT for RH. Its negative-mass
criterion is also NECESSARY, as follows. Put
`B(z)=(1-67^(-z))/zeta(z)` and assume RH's classical consequence
`sum_(n<=x)beta(n)=O_epsilon(x^(1/2+epsilon))`. Abel summation gives
`sum beta(n)/n=B(1)=0`, and the exact source splitting is

```
C_m(X)/4^m = m sqrt(X) sum_(n<=X) beta(n)/n
            -sum_(n<=X) beta(n)/sqrt(n)
            +sum_(j=2)^m (-1)^j binom(m,j) X^(j/2)
                sum_(n>X) beta(n)/n^((j+1)/2).
```

Each term is `O_(m,epsilon)(X^epsilon)` (choose the input exponent smaller
first). Consequently the logarithmic negative mass is subpower. The
converse is the reviewed Landau argument, so that negative-mass criterion
is RH-equivalent. Eventual sign has not thereby been shown necessary.
The quadratic envelope identity `C_2=16B(3/2)X-G_2` is an identity, not a
third independent proved positivity theorem. Split these roles in any
canonical use of the combined source range '.7–.9'.

## R18 — exact extraction contracts for surviving components

**P79:** S26's interval of equation numbers '.2–.8' contains the separate
positivity claim '.4'. Retain exact equations '.2,.3,.5,.6,.7,.8' and the
score-minus-target identity '.10' only as algebra. Exclude '.4' unless its
separate primitive proof is paid. The already rejected Hall/surplus and
positive-splice conclusions are not restored by the Euler split.

**Vaughan:** S15/S16 prove, by finite Dirichlet convolution,
`a_U=b_U*1` and `a_U*a_U*mu=b_U*a_U=b_U*b_U*1`. Combined with
`eta*eta=1`, this is `h_U*h_U`. The two ratio-four kernel factors are genuine
Mellin convolutions. Endpoints of the step kernels matter in literal finite
point evaluations; they are irrelevant only almost everywhere in the
integral identities. Keep the first-pass finite truncation before the
full-line Hardy estimate and the coupled squarefree gcd constraints.

**Volterra:** S10 requires `a>0`, local absolute continuity of `f`, a BV
representative of `f'`, and the declared right boundary derivative. The
Green derivative jumps by `t^(-3/2)`, exactly compensating the coefficient
`t^(3/2)` of `df'`. Both homogeneous modes and all knot atoms are essential.

**Native Y4:** use row/column indices `q>=2`; the `q=1` diagonal of the carry
matrix is zero. The full triangular inverse, its top two entries and the
radial null-support statement survive. None supplies nonnegative,
source-owned global feasibility.

**Julia:** the actual `a=4` mass proof is valid. The monotone-integrand
argument for the generic prime bound is justified when `c>=1/log 2`, in
particular at `c=9/2`; no all-`c>1` monotonicity is needed. For a generic
finite measure with `W(t)=0`, conditional-mean maps use the subspace
`L2({W>0})` and zero conventions. For the actual unbounded prime support,
`W(t)>0`. The six-term algebraic negative-mass cap and the existing corrected
reserve `21587/38416` are reconstructed; the identification with the full
critical completed source remains open.

**Finite cubature:** finite positive measure and integrable finite-dimensional
coordinates permit a finite real atomic cubature; this is an existence
statement, not a guarantee of rational nodes or a symbolic implementation.
The unsupported literal score assignment excluded in the first release
remains excluded. Finite positive Pick boxes remain conditional on their
specified primitive rectangles; the midpoint-radius lemma cannot validate
those primitives.
