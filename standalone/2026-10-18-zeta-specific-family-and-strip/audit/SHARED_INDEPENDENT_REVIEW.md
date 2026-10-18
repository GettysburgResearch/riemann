# Independent review of the shared-factor quadratic-family route

Reviewer: a separate research agent (`/root/field_audit`) from the author of
the shared-factor route. Review date: 2026-10-18.

Verdict: **the component deductions pass this review at the exact hashes
below**. I independently checked the arguments and replayed the finite exact
checker under optimized Python. No substantive mathematical defect remains
in the reviewed proof. This is an independent agent review, not external
referee approval or proof-assistant verification.

The result is an arithmetic extraction theorem, an exact residual
decomposition, and two explicit critical-energy reductions. The missing
ordinary cancellation estimate and strict-below-one full residual estimate
have not been proved. The actual-L-value adapter on `Re s>3/4` is a moment
convergence theorem; it does not establish a zero-free region there.

## 1. Exact reviewed identity

Paths are relative to the parent research packet. SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `shared/PROOF.md` | `7953ae0232d95db445ed665c9ef5b80e9489fa9e98403833f7943e104f763e47` |
| `shared/check_shared_factor.py` | `6c83977930f037c8589cbd93faab31ecc0f3e0b52749d028f198ab8ffc686176` |
| `shared/check_report.json` | `500bbd490fea7dd07a8a3ff61081f65d7ec9b9a80826f3b6cc229b6292d1403b` |

Later changes to these files require a new review identity. Editorial
summaries are not additional mathematical premises of this review.

The author clarified three details raised during review: `g` is defined on
all positive odd integers, the weighted square main term retains the average
of its conductor-dependent weight, and the fixed-mollifier square-pair sum
has an explicit summable majorant. These clarifications agree with the proof
already intended. The signed-mean-first corollary was included before the
hashes above were frozen and was separately checked below.

## 2. The actual family and uniform character average

Every `d=-8u`, with `u` positive, odd and squarefree, is a negative
fundamental discriminant. Its quadratic character is primitive and odd, has
conductor `8u`, and vanishes at 2. The density constant `4/pi^2` for odd
squarefree integers is correct.

The uniform estimate (2.1) correctly retains ramification:

\[
\mathbb E_Q\chi_u(n)
=\mathbf1_{n=\square}g(\operatorname{rad}n)
 +O(Q^{-1/2}n^{1/4}\log(2n))
\]

for positive odd `n`, and is exactly zero for even `n`.

For a square index, the squarefree coprimality count gives the stated main
term and error `O(sqrt(Y) 2^{omega(a)})` with `n=a^2`. The bound
`2^{omega(a)} << sqrt(a)` is valid for odd `a`; only the prime 3 contributes
a fixed factor larger than one. Normalizing by the actual family size does
not enlarge the claimed error.

For a nonsquare index, the Jacobi symbol has a nonprincipal primitive part
on its odd-exponent prime kernel. Inclusion-exclusion handles the additional
zero restrictions from even-exponent primes. Its total cost is bounded by
`sqrt(n) log(2n)`, as claimed. Restriction of the summation variable to odd
integers is harmless by subtracting the even-index sum.

Inserting the squarefree-divisor expansion and splitting at `A` gives
`A sqrt(n) log(2n)+Y/A`. The stated choice of `A`, or the trivial estimate
when that choice is below one, gives the required uniform bound. The prefix
version also proves the bounded-variation weighted estimate by partial
summation. No distribution theorem under GRH is used.

These finite mixed-character moments determine the three-state independent
limiting prime law, including its mass `1/(p+1)` at zero. Independence is
asserted only in the limit, not for the finite discriminant family.

## 3. The native inverse source and complete critical energy

The coefficients `a_u=mu*(mu chi_u)` are the full coefficients of
`1/[zeta(s)L(s,chi_u)]`. Their local factors are correct in all three odd
prime states and at the permanently ramified prime 2. The finite convolution
identity for `A_u(x)` includes every coefficient.

For the mean and covariance, the two inverse-character indices are odd and
squarefree. Their product is a square precisely when the indices agree.
This gives exactly the retained positive diagonal in (3.4), without omitting
a ramified or shared-prime term. The elementary bound

\[
\sum_{m\le x}m^{1/4}|M(x/m)|\ll x^{5/4}
\]

produces the uniform mean and second-moment errors used in the proof.
Integration against `x^{-2 sigma} dx/x` gives the exponent
`5/2-2 sigma` in (3.7), uniformly for `1/2<=sigma<=1`.

The substitution `x=my` correctly gives the dilation energy
`m^{-2 sigma} E_sigma(M;T/m)`. The `m=1` term supplies the lower bound.
Monotonicity of the ordinary energy and the retained positive coefficients
supply the upper bound. At the critical exponent the multiplier is at most
`1+log(T)`; above it the Euler multiplier converges.

Consequently `Q(T)>=T^{3+delta}` makes the discrepancy in the **average of
individual critical energies** tend to zero. The resulting all-epsilon
subpower criterion is equivalent to the ordinary critical Möbius energy
criterion, with the logarithmic multiplier absorbed into epsilon.

The later signed-mean-first result is also correct. Squaring the deterministic
mean error and then integrating gives

\[
E_\sigma(\mathbb E_Q A_u-M;T)
\ll Q^{-1}T^{5/2-2\sigma}(\log(2T))^2.
\]

At `sigma=1/2`, `Q(T)>=T^{3/2+delta}` makes this discrepancy energy vanish.
The triangle inequality for its square root proves (3.12) in both directions.
The family is fixed throughout each integral on `[1,T]`; the proof does not
replace it by a different family at each `x`. This smaller conductor
requirement concerns energy of the signed average, and is not claimed for
the average of individual energies.

The Mellin consumer is valid. Cauchy--Schwarz with the critical energy gives
absolute convergence on every half-plane `Re s>1/2`, so the identity
`integral M(x)x^{-s} dx/x=1/[s zeta(s)]` continues holomorphically there.
The converse uses the classical RH-to-Mertens theorem as explicitly stated.
Neither direction assumes GRH for any additional quadratic L-function.

## 4. Complete residual and square aliases

The independent Euler model exists in each fixed finite `L^k` on
`Re s>1/2`: the normalized prime factors form a bounded product martingale,
and the absolute moment increments are summable. The majorant

\[
\sum_{nm=\square}(nm)^{-\sigma}\le\zeta(2\sigma)^3
\]

also justifies the Dirichlet-series `L^2` convergence. The corresponding
locally uniform analytic interpretation follows on smaller compact sets
from the same uniform bounds and analytic mean-value estimates.

I independently derived the local orthogonal decomposition using the basis
`1`, `X_p/sqrt(g_p)`, and
`(X_p^2-g_p)/sqrt(g_p(1-g_p))`. It gives exactly the stated `C_p`, `t_p`,
and `v_p`. In particular, the identity

\[
X_p x_p\frac{(1-X_p x_p)^{-1}}{C_p}=t_p+Z_p
\]

is valid in all three states. Products indexed by distinct squarefree prime
sets are orthogonal. Their coefficients are the displayed `S_{X,r}`, and
their squared norms are `v(r)`. For fixed `X` the coefficients take only
finitely many values, while `sum_r v(r)<infinity`. Parseval therefore proves
the complete positive variance formula, not just its constant term.

The square aliases in the mean are retained correctly. For an inverse index
`n`, the full L-series index must be `n a^2`, with local survival probability
`g(rad(na))`. The resulting Euler product is exactly the correction stated
after (4.8). The permanently ramified prime 2 is excluded from this auxiliary
Euler product and remains in the ordinary Möbius polynomial.

The common scalar can be any complex `z` in the probabilistic identity.
Taking `z=zeta(s)` leaves that scalar in both the squared bias and every
variance term. At a zeta zero the residual is exactly one. This argument
neither divides by zeta nor silently normalizes away a shared zero.

## 5. Causal inversion and the corrected analytic mollifier

The identity `product_p(1-t_p)=C^{-1}`, local bounds `|t_p|<1`, and
absolute summability give the forward and inverse dilation kernels in (5.2).
For every `0<=eta<2 sigma-1`, their additional `b^eta` coefficient masses
converge, including the geometric inverse at each prime. The finite-horizon
norm calculation is correct and the constants are independent of the
observation horizon.

The residual is defined as minus one below cutoff 1. This is essential:
including that initial region makes (5.4) exact and prevents a missing
constant. The claimed equivalence of **signed bias decay** with ordinary
Möbius residual decay follows with the stated exponent range. It does not
assert an equivalence for the complete residual with its positive variance.

Formula (5.5) is a finite, explicit analytic combination at each cutoff. Its
coefficients have no poles in `Re s>1/2`, since the correction Euler product
is nonzero there. It removes the auxiliary square-alias correction from the
mean. The proof explicitly distinguishes this analytic mollifier from a
Dirichlet polynomial with coefficients constant in `s`. At a hypothetical
zeta zero both the original and corrected finite residuals remain one.

## 6. Actual full L-values: the adapter and its domain

The approximate functional equation has the correct parity, conductor scale,
gamma quotient, root number, and dual power for the family `d=-8u`. The
completed nonprincipal L-function is entire, so its contour shift has only
the intended residue from the integration kernel. The Gaussian kernel
justifies the shifts, and the weights have the stated small-argument limits
and arbitrarily rapid large-argument decay on the fixed compact range
`3/4<sigma_0<=Re s<=sigma_1<5/4`.

Dependence of the weights on `q=8u` is handled correctly. After removing the
absolute size of the dual prefactor, their supremum and total variation on
`[Q,2Q]` are uniformly bounded in the summation indices. Truncation at
`N=Q^{1/2+delta}` therefore permits the weighted character estimate, and its
tails are negligible by ordinary absolute bounds.

There are two essential diagonal details:

1. For a square character index `k` with a conductor-dependent weight `W_u`,
   the main term is `g(rad k) E_Q W_u`. It is not replaced at finite `Q`
   by the unweighted constant. Each fixed-pair weight tends to one as `Q`
   grows.
2. Multiplication by a fixed polynomial in the characters changes the square
   condition to `n m k` being a square. This condition is retained, including
   the zeros caused by ramification. Its absolute sum is at most
   `k^sigma zeta(2 sigma)^3`, by substituting `n'=nk` and enlarging the
   positive square-pair sum. Thus fixed character twists do not invalidate
   dominated convergence, but their constants depend on the fixed cutoff.

The primary off-diagonal error is exactly of size
`Q^{3/4-sigma+delta(5/2-2 sigma)}` up to logarithms. The dual diagonal
is bounded by `Q^{1/2-sigma+delta(2 sigma-1)}` up to a logarithm; writing
`n=ra^2,m=rb^2` gives the remaining harmonic `r` sum. The dual
off-diagonal error is `Q^{3/4-sigma+delta(2 sigma+1/2)}` up to logarithms.
For the stated compact set a single sufficiently small positive `delta`
makes all three errors vanish. Cauchy--Schwarz removes the primary/dual
cross term. The fixed mollifier is bounded uniformly in the character and
does not change disappearance of the dual part.

These steps prove convergence of the required first and second moments for
each **fixed cutoff** on `Re s>3/4`. Absolute convergence supplies the
overlap and points farther to the right. The full residual excludes `s=1`
because of the common zeta pole. There is no assertion of uniformity for
an arbitrary growing mollifier, no transfer of the random-model domain down
to `Re s>1/2`, and no auxiliary GRH input.

## 7. Exact finite replay and boundaries of the verdict

I independently ran, from the shared directory,

```text
python -O check_shared_factor.py --output /tmp/shared_factor_independent.json
```

The process exited successfully. The independently written report is
byte-for-byte identical to `check_report.json` at the hash in Section 1.
Acceptance uses explicit exceptions rather than `assert`, so optimization
does not erase its predicates.

The finite checks include all inverse indices through 240 in ten actual
fields, with split, inert, and ramified local behavior. They enumerate all
27 states of the three-prime model with exact ramification probabilities.
They verify source means, covariance, a complete critical-energy integral,
the retained dilation multiplier, all eight orthogonal components of the
three-prime full residual, a zero common scalar, and both directions of the
correction operator. The residual checks use exact complex rational Euler
variables and exact rational probabilities; this is an algebraic fixture,
not a numerical sample of the infinite analytic theorem.

The actual-discriminant table is appropriately labeled as finite observations.
It is not used to certify an asymptotic rate. The checker explicitly excludes
the infinite products, analytic family limits, approximate functional
equation, all-horizon cancellation, a zero-free strip, and RH from its
machine-certified scope.

The imported Pólya--Vinogradov estimate, primitive quadratic functional
equation, and RH-to-Mertens implication were not independently reproved in
this review. Their exact required forms and uses were checked. Proposed
quasi-RH results elsewhere in the repository are not premises. The positive
verdict covers the stated component proofs and finite replay; it supplies
neither of the missing global cancellation estimates.
