# Signed finite-ray descent and conductor means

**Status: proposed standalone research, with source-conditional proofs.**
This pass cancels the apparent divisor pole in the actual reflected
series, proves closure of its complete cusp coefficient family, and
extends that series into a larger analytic domain with a conductor
mean estimate. It also obtains an all-cusp bound after exact support
pruning. The full generalized `2k`-th moment, its fourth-moment case,
and RH remain open. None of the new bounds improves the best existing
physical estimate at the critical moment scales.

This packet continues [PR #920](https://github.com/GettysburgResearch/riemann/pull/920),
whose final head is `2edc467ef4dea4aa685219ac6a558a158b88768d` and
whose mathematical source is
`6aceafc1729ca0962eb12519b407b69c3b5a4d5f`. All inherited proofs and
their recorded qualifications remain intact. The analytic foundation
is the October 5 OpenAI/math manuscript at
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`; the new deductions
assume its stated theta interfaces. The conductor mean additionally
uses its completed mean square and the classical squarefree sextic
sieve. No new Lean verification or independent acceptance of the
imported foundation is claimed.

## 1. The requested moment and the present boundary

In the Eisenstein field, with the inherited primary convention,
literal nonunit zeros, fixed bad set S, and a fixed finite character
nu, put

\[
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D).
\]

The target is, for every fixed integer `k>=1`, every arbitrarily
small fixed `theta>0`, and every epsilon greater than zero,

\[
\boxed{
\sum_{0<Nu\le H}|A_u(D;W)|^{2k}
\ll_{k,\theta,\epsilon,\nu,S,W}H D^{k+\epsilon},
\qquad H=D^{1+\theta}.
}
\tag{1.1}
\]

The sum is over **all** nonzero element rows, including sixth powers
and imprimitive rows. Smooth seminorms can be stated explicitly as in
the inherited transfer. The previously derived sixth-power extraction
would give the fixed-character limiting boundary

\[
\frac12+\frac{5}{12k}.
\tag{1.2}
\]

For k=2 this is 17/24; cofinally unbounded fixed orders would approach
1/2. This is an implication from the moment hypothesis, not an
unconditional consequence of this packet. See the exact quantifiers
and family-strength discussion in
[GENERAL_MOMENT_ATTACK.md](../2026-10-10-sextic-moment-descent/GENERAL_MOMENT_ATTACK.md)
and [MOMENT_OBSTRUCTIONS.md](../2026-10-10-sextic-moment-descent/MOMENT_OBSTRUCTIONS.md).

The present attack concerns a specific joint Dirichlet series exposed
by coupled theta reflection. Its rows are squarefree in the new
conductor mean. That distinction matters when returning to (1.1).

## 2. The apparent pole cancels in the actual finite data

PR #920 continued the reunited standard-face series meromorphically
through v=1. Its unresolved finite character expansion allowed a
possible principal pole and additional reciprocal poles. The new
calculation evaluates the actual finite Fourier data before expanding
them into unrelated character labels.

With row r, `Q=Nr`, and fixed eta,rho, write

\[
\kappa=\eta\rho^3,\quad
v=w+3s-\tfrac32,\quad
x_p=\chi^-_r(p)(Np)^{-w},\quad
z_p=\kappa(p)(Np)^{-v},\quad D_p=1-x_p+z_p.
\]

The true fixed multiplier is `phi_rho(x)=rho(x)` on primary units
at the bad modulus, and zero elsewhere. For every good primary d,
its finite Fourier transform satisfies

\[
\widehat\phi_\rho(d^{-2}h)=\rho(d)^2\widehat\phi_\rho(h).
\tag{2.1}
\]

Reindexing the **whole** Fourier sum by this permutation preserves
the cusp and its additive phase. The exact bad Kubota factor changes
by `chi_d(c0)^(-2)`. Its conjugate cancels the supplementary character
left over from the good-prime reflection, so the complete divisor
phase is precisely `eta(d)rho(d)^3=kappa(d)`.

The resulting local cancellation is elementary but decisive:

\[
D_p+z_p\bigl(-1+Np\,\mathbf1_{p\mid m}\bigr)
=\begin{cases}
1-x_p,&p\nmid m,\\
1-x_p+Np\,z_p,&p\mid m.
\end{cases}
\tag{2.2}
\]

The infinite reciprocal in v disappears from the complete function.
Only the finite frequency-divisor weight remains:

\[
\prod_{\substack{p\mid m\\p\nmid rS}}
\left(1+\frac{\kappa(p)(Np)^{1-v}}{1-x_p}\right).
\tag{2.3}
\]

[FINITE_RAY_REUNION.md](FINITE_RAY_REUNION.md) proves that the full
reunited object is holomorphic on

\[
\Re s<0,\qquad \Re s<\Re v-1,
\tag{2.4}
\]

with no separate lower bound on Re(v) and no zero-free assumption.
In particular the complete v=1 residue from PR #920 is zero; the
other possible finite-character poles are removable on the overlap.
This assertion concerns the actual complete data, not arbitrary
individual terms of the earlier redundant character expansion.

## 3. The output closes under the next cube completion

The second exact Fourier reindexing, `h -> b^3 h`, gives

\[
F_{\sigma,c_0}(b^3m)=\overline{\rho(b)}^{\,3}
F_{\sigma,c_0}(m).
\tag{3.1}
\]

[FINITE_CUBE_HOMOGENEITY.md](FINITE_CUBE_HOMOGENEITY.md) checks
this at all three cusp types, including the ramified middle Kubota
case. The actual output ray characters therefore have the prescribed
cube

\[
\varrho^3=\overline\rho^{\,3},
\qquad \varrho=\overline\rho\,\xi,\quad\xi^3=1.
\tag{3.2}
\]

The companion
[ALL_CUSP_COEFFICIENT_ADAPTER.md](ALL_CUSP_COEFFICIENT_ADAPTER.md)
derives every supported coefficient from the explicit cusp formulas,
with the source's additive-character normalization and complex
conjugation. It proves

\[
d_\sigma(b^3\ell)=\sqrt{Nb}\,d_\sigma(\ell)
\quad\text{for }\sigma=0,+,-.
\tag{3.3}
\]

No extra coprimality between b and the squarefree part is required.
The nonstandard cusps' intrinsic additive phases stay fixed because
primary b satisfies `b^3=1 mod lambda^4`. Bad squarefree parts,
bad cube parts, ramified exponents and zero sectors are retained.
Consequently the full reflected coefficient system, after its
specified norm and angular factors are extracted, is a finite ray
combination of the canonical Gauss family needed for the next step.

## 4. A shifted variable and a proved conductor mean

Set

\[
t=1-s,\quad u=v-s,\quad
K_p=\kappa(p)(Np)^{1-v},\quad
y_p=\overline\alpha(p)^3\varrho(p)^3\chi_r(p)^3
             (Np)^{-(3t-1/2)}.
\]

The prescribed cube in (3.2) gives `K_p y_p=x_p`. Sum every cube
valuation before extracting the dominant squarefree factor. The local
identity then becomes

\[
1-x_p+K_p=K_p(1+K_p^{-1}-y_p).
\tag{4.1}
\]

Pulling K out of the squarefree index changes its Dirichlet variable
from t to **u=v-s**. Conditioning on the remaining divisors gives a
normally convergent sum of canonical Gauss Dirichlet series, with
perturbation `h(p)=K_p^(-1)-y_p`.

For `a=Re(u)` between 1/2 and 1, the individual Gauss bound costs
`Q^(1-a)(Nd)^((1-a)/2)` up to small powers and a vertical polynomial.
The new divisor sum converges under the sufficient strict
condition

\[
\tfrac32a+1-\Re v>\tfrac32,
\quad\text{equivalently}\quad
\Re s<\frac{\Re v-1}{3}.
\tag{4.2}
\]

This improves the former condition `Re(s)<Re(v)-1`.
[SECOND_REFLECTION_BOOTSTRAP.md](SECOND_REFLECTION_BOOTSTRAP.md)
proves the exact rearrangement, analytic domain and vertical bounds.
It also checks that simply applying the same theta involution twice
does not supply an independent second reflection.

The new [SPECTRAL_ROW_MEAN.md](SPECTRAL_ROW_MEAN.md) proves, for
the exact canonical Gauss family and squarefree rows of norm Q,

\[
\boxed{
\sum_{r\sim Q}^{*}|G_{r,d}(a+iT)|^2
\ll Q^{1+\epsilon}(Nd)^{1-a+\epsilon}(2+|T|)^M,
\qquad \frac58<a<1.
}
\tag{4.3}
\]

Its two inputs are the smooth completed block bounds

\[
Q+Q^2Nd/X,
\qquad Q+X+(QX)^{2/3}.
\tag{4.4}
\]

Mellin reconstruction is locally normally convergent for Re(u)>1/2.
The crossover at `X=Q^(4/5)(Nd)^(3/5)` yields the threshold 5/8.
The cube reciprocal lies in its absolute Euler half-plane, so this
argument does not use a zero-free theorem.

Finally [FULL_CUSP_DESCENT.md](FULL_CUSP_DESCENT.md) composes the
identities and estimates, summing all the actual bad and ramified
labels. Write the original reunited series as
`R_r(w,s)=H(s)Q^(1-2s)Y_r(s,v)`, with H its explicit gamma factor.
The complete continued domain is

\[
\boxed{
a=\Re(v-s)>\frac12,\qquad
\tau=\Re v<\min\left(a,\frac{3a-1}{2}\right).
}
\tag{4.5}
\]

For `5/8<a<1` and `tau<(3a-1)/2`, strictly inside this domain,

\[
\boxed{
\sum_{r\sim Q}^{*}|Y_r(s,v)|^2
\ll Q^{1+\epsilon}
(2+|\Im s|+|\Im v|)^M.
}
\tag{4.6}
\]

All cross terms in the actual cusp sum are controlled. Its finite
decomposition is not treated as an orthogonal one.

## 5. What the new estimates do at the physical scales

At balanced lengths `A=B=D`, the residual Mellin scalar is
`D^(v-2s)`. Under the new bounds its exponent approaches 13/16
from above. That is a scalar exponent for this analytic argument;
it is neither a zeta zero-free boundary nor a generalized moment
exponent.

Even granting a valid passage of that estimate to a corresponding
smoothed physical completion, the resulting energy
`Q D^(13/8+epsilon)` does not beat the minimum of two older bounds:

\[
D^\epsilon D(Q+Q^2),\qquad
D^\epsilon\left[Q+D^2+(QD^2)^{2/3}\right].
\tag{5.1}
\]

For `Q=D^h`, the new exponent is `h+13/8`. It is smaller than the
classical envelope only when h<3/8, while the factorwise bound is
already smaller throughout that range. It beats the factorwise
bound only when h>5/8, where the classical envelope is already
smaller. This is a complete exponent comparison, not merely a test
at a few numerical scales.

The same comparison would hold if this method's spectral threshold
were lowered from 5/8 all the way to 1/2. The full-cusp note proves
this for every putative threshold `1/2<=a0<1`. Improving that one
threshold alone is therefore insufficient; a further saving in the
joint covariance or a different use of the continued series is needed.

There is a separate quantitative deduction in
[SUPPORT_PRUNED_COVARIANCE.md](SUPPORT_PRUNED_COVARIANCE.md).
Remove the exact vanishing groups `Ng>C_S sqrt(B)` **before**
splitting their theta sums and applying norms. The all-cusp adapter
then extends the required quadratic–cubic coefficient calculation.
For the specified coupled completion with squarefree rows,

\[
\sum_{r\sim H}^{*}|\mathcal C_{A,B}(r)|^2
\ll D^\epsilon\left[
HA+\frac{H^2A\min(A,\sqrt B)}B
 +\left(\frac{H^2A^2}B\right)^{2/3}\right].
\tag{5.2}
\]

This gives a real quantitative improvement for short rows. At balanced
scales and `H=D^h`, its exponent is `h+1` for `0<=h<=1/2`, and
`2h+1/2` for `h>=1/2`. It beats the minimum in (5.1) for every
fixed `0<h<3/4`; at `H=sqrt(D)` it saves a factor `sqrt(D)`.
It does not enlarge the previously available range for an energy
bound of order D squared. It remains too large in the difficult fourth-moment
initialization, where product columns have length about D squared
and dual rows extend to about `D^(3-theta)`. It does not establish a
new range for the full original moment.

The pinned [PR #919](https://github.com/GettysburgResearch/riemann/pull/919)
at `9b04a887e171b3104a66cf57296ce5b0b2920d78` supplies a useful
constraint on attempted signed scale averaging: its exact residual
S already satisfies `S(D)>=-O(D^(h+2+epsilon))`. Thus a target-size
upper bound for its signed integral is equivalent, at the exponent
level, to the same bound for its absolute integral. Excess positive
mass cannot be canceled by negative mass of a larger power. The new
calculation records this implication without assuming the missing
average itself.

## 6. Proofs and finite verification

| Result | Proof | Precise scope |
|---|---|---|
| Actual finite-ray pole cancellation | [Reunion](FINITE_RAY_REUNION.md) | Source-conditional exact identity and holomorphic continuation |
| Prescribed reflected cube character | [Cube homogeneity](FINITE_CUBE_HOMOGENEITY.md) | Every actual cusp and finite bad-ray branch |
| Complete good-prime coefficient class | [Cusp adapter](ALL_CUSP_COEFFICIENT_ADAPTER.md) | Exact source coefficients, units, bad parts and intrinsic phases |
| Shifted Gauss variable and new divisor domain | [Bootstrap](SECOND_REFLECTION_BOOTSTRAP.md) | Exact canonical family with the proved cube interface |
| Conductor mean in Re(u)>5/8 | [Spectral mean](SPECTRAL_ROW_MEAN.md) | Squarefree rows, moving d, uniform finite ray family |
| Composition for the complete reflected object | [Complete descent](FULL_CUSP_DESCENT.md) | Entire second-reflection cusp sum of the original standard-face series |
| Support-pruned covariance | [Covariance bound](SUPPORT_PRUNED_COVARIANCE.md) and adapter Section 5 | Specified full coupled completion; no growing auxiliary extension |

The reproducible finite diagnostic is

~~~bash
python3 standalone/2026-10-10-signed-covariance-descent/checks/check_descent_algebra.py \
  --output standalone/2026-10-10-signed-covariance-descent/results/descent_algebra_checks.json
~~~

It uses exact arithmetic for the local cancellation, cube summation,
finite Fourier covariance, prescribed character support, primary-cube
congruence and exponent comparisons. Deliberately wrong signs,
characters or masks must fail the corresponding predicates. These
checks concern finite algebra; infinite convergence, automorphy and
moment estimates are established only by the written proofs under
their stated inputs.

Scoped independent AI-agent reconstructions are recorded separately
from authorship. They do not constitute external human acceptance or
formal proof certification. The frozen source and follow-up validation
records bind the actual contents used in those reviews.

## 7. The next missing theorem

The remaining target is a bound for the **actual signed small-gcd,
large-conductor covariance**, or its permitted scale average, with
the original balanced divisor coefficients and every moving auxiliary
and exclusion mask. It must survive passage back from the completed
theta expressions to the Möbius polynomial and must cover all element
rows. Repeating the present absolute bounds, the same theta involution,
or a finite-character decomposition does not furnish this estimate.

This pass removes two genuine obstructions to pursuing that theorem:
the apparent pole and the unverified character-family closure. It
also measures the remaining conductor cost explicitly. The required
quantitative cancellation, already unresolved at the full fourth
moment, is still the step that would advance the generalized hierarchy
toward the full hypothesis.
