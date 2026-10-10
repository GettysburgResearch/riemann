# Independent review of the spectral mean and shifted Gauss continuation

**Reviewer:** scale_covariance_attack. **Date:** 2026-10-10.
This is an independent analytic reconstruction of the two specified
notes. The reviewer did not author either note. It is an AI-agent
review, not a Lean verification or external human peer review.

**Verdict:** the spectral theorem, the exact standard-face cube
summation, the shifted-variable continuation, and its stated
mean-square implication pass at their declared source-conditional
scope. They do not prove a fourth or generalized inverse moment.

## 1. Reviewed contents and scope

| File | SHA-256 of reviewed contents | Bytes |
|---|---|---:|
| `SPECTRAL_ROW_MEAN.md` | `5154dc7d0502555f9a198eed386b9926bf1769ac61ae6b7c6fa319eadec7ace1` | 11136 |
| `SECOND_REFLECTION_BOOTSTRAP.md` | `e1db605878eb805a3d21f908ea1c73f5869d56c112a3c3e91e67d9b715b16fd0` | 18957 |

The first file was reviewed in full. For the second, the review covers
Sections 1--4, the conditional mean-square deduction in Section 6,
the exact requirements listed in Section 7, and the physical exponent
comparison in Section 8. Section 5's elementary
inactive-frequency identity and displayed norm exponent were checked,
but its narrative assertion about restoration of every involution
phase is not a load-bearing input to the reviewed theorem and is not
separately certified here.

The review read the imported October 5 `paper2.tex`, especially the
exact definitions `eq:T`, `eq:completed-twist`, and the statement
`prop:R` at lines 1317--1329 in the retained source. Its underlying
automorphy, all-row proof, and classical sextic sieve remain declared
analytic inputs. The fixed source is OpenAI/math commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`; no changing upstream version
is substituted.

The all-cusp coefficient adapter has separate authorship by this
reviewer, so this report does not represent an independent review of
that adapter. The actual finite-ray covariance must also receive its
own review before the standard-face theorem is promoted to the
complete reflected object. Its role is identified below.

## 2. Spectral theorem: exact family and physical block estimates

The canonical coefficient is `bar-alpha(n) gamma_2(n) xi(n)`, with
finite `xi`. The auxiliary twist `chi_n(d)^4` forces the squarefree
column to avoid `d`. On the cube index its twelfth power is the
coprimality indicator, giving the literal omission of `d` in
`L_(S,kd)(3u-1/2, bar-alpha^3 xi^3 chi_k^3)`.
No positive valuation at a deleted prime has been converted to one.

The physical block in spectral equation (2.1) follows from the source
definition with `V_*(y)=sqrt(y) W(y)`: the source denominator and this
factor leave precisely `X^(-1/2) sqrt(Nb)`. There is no
`(n,b)=1` condition. At fixed `b`, rewriting the block as a normalized
squarefree polynomial of length `L_b=X/(Nb)^3` gives an exterior
factor of modulus at most `1/Nb`, as stated.

The source's completed mean square applies uniformly even as `X`
tends to infinity: choose its reference parameter
`D=max(2Q,F,X,2)` and its fixed ceiling exponent `C_0=1`.
Then all source parameters lie below that ceiling, and the source
derivative order depends only on the chosen small exponent, not on
`X,Q,F`. Its loss is at most `(2QFX)^epsilon`. Restricting its
nonnegative all-row sum to the specified squarefree rows is valid,
including if a further `(k,d)=1` condition is imposed.

For the alternative block estimate, the squarefree sextic sieve sees
only arbitrary bounded column coefficients, with the `d` mask kept
inside them. The normalized coefficient mass is bounded on every
nonempty scale, including a fixed bounded range below one. Weighted
Cauchy over `b` gives one harmonic factor. Summing the three sieve
terms with the additional weight `1/Nb` yields the powers
`(Nb)^(-1)`, `(Nb)^(-4)`, and `(Nb)^(-3)` respectively.
The logarithms are absorbed into a small power; no orthogonality
between cube indices is presumed.

## 3. Spectral theorem: holomorphy and conductor exponents

The smooth dyadic identity reconstructs the completed Dirichlet
coefficient exactly:

\[
X^{1/2-u}X^{-1/2}
\left(\frac{Nn(Nb)^3}{X}\right)^{-u}\sqrt{Nb}
=(Nn)^{-u}(Nb)^{-3u+1/2}.
\tag{3.1}
\]

Every individual smooth block is finite and entire in `u`. On a
compact subset of `Re(u)>1/2`, the source estimate bounds its dyadic
tail by a summable geometric series after choosing a sufficiently
small preliminary exponent. This is normal convergence in a finite
row Hilbert space; it neither presumes the unknown tail bound nor
uses an exchange of conditionally convergent Euler products.

The cube reciprocal is an absolutely convergent Euler product there,
because `Re(3u-1/2)>1`. Its uniform bound survives all moving
omissions. This proves the continued `G` and the transfer of its
norm bound without a zero-free hypothesis.

The minimum of the two block bounds can be split as in spectral
equation (4.1). The first crossover solves `X=Q^2F/X`, giving
`X_1=Q sqrt(F)` and total norm contribution
`Q^(1-a) F^((1-a)/2)`.

The second crossover solves `(QX)^(2/3)=Q^2F/X`, giving
`X_2=Q^(4/5)F^(3/5)`. With `a=Re(u)<5/6`, the two dyadic sides
both give

\[
Q^{1-4a/5}F^{1/2-3a/5}.
\tag{3.2}
\]

For `a>5/6`, the lower range is bounded by `Q^(1/3)` and the
upper endpoint is no larger. At `a=5/6` the retained logarithm
gives uniform control across that value. The comparisons

\[
1-4a/5<1/2\quad(a>5/8),
\qquad
1/2-3a/5\le(1-a)/2
\tag{3.3}
\]

verify the claimed conductor mean on every strict strip above
`5/8`. The first minimum, the base `sqrt(Q)` term, and the
`Q^(1/3)` term are all covered as well. Small source exponents
can be retained throughout and absorbed using the strict margins;
the Fourier parameter enters only through the polynomial smooth
seminorms of `y^(-u)W_0(y)`.

## 4. Bootstrap: local identities and the exact shifted family

The cube-law hypothesis `varrho^3=bar-rho^3`, together with
`kappa=eta rho^3`, gives `K_p y_p=x_p` exactly at good primes.
At omitted primes all sums have only their constant term; the proof
does not divide by a zero character value there.

The two cases of the local cube sum, according as `p` divides `n`,
produce the denominator `(1-x)(1-y)`, with numerator one or
`1-x+K`. Thus the exterior reciprocal `1/L(w,chi^-)` cancels
precisely the full product of `(1-x)^(-1)`. This cancellation
requires the unrestricted cube valuations and includes the case
`p` dividing both indices.

Factoring `K` from every squarefree prime of `n` changes its norm
power from `t=1-s` to `u=v-s`, and changes its finite character by
the factor `kappa`. The remaining divisor coefficient is
`h_p=K_p^(-1)-y_p`. Gauss CRT then gives the conditioned series
`G_(k,d)(u)` with the exact fourth-power character, hence its
moving coprimality mask.

Its completed series has canonical angular parameter zero, source
local exponents one at `k` and four at `d` on the disjoint set in
use. The conditioned-theta interpolation argument applies with the
same absolute local majorants as the cited source. Division by its
cube factor is justified at `Re(u)>1/2` solely by its absolutely
convergent Euler product. In particular the individual bound in
bootstrap (3.4) does not borrow an angular reciprocal estimate from
a larger half-plane.

The bootstrap uses reciprocal row notation `chi_k(n)`, while the
spectral statement uses `chi_n(k)`. The inherited sextic reciprocity
decomposes their ratio into finitely many fixed primary ray classes.
On each row class it can be absorbed into the fixed finite
coefficient character. The spectral theorem is uniform over that
finite family. This conversion preserves all nonunit zeros and
does not alter its conductor exponents.

## 5. Bootstrap: domain, row mean, and interpretation

Put `a=Re(u)` and `delta=1-Re(v)>0`. The cube factor is absolutely
convergent on the claimed chamber. The remainder has the uniform
bound `|h(d)| << (Nd)^(-delta+epsilon)`. With the individual or
spectral Gauss bound, the norm exponent of a `d` summand is

\[
-a-\delta+(1-a)/2.
\tag{5.1}
\]

The ideal sum converges precisely under the stated sufficient
condition

\[
\frac32a+\delta>\frac32,
\qquad\text{equivalently}\qquad
3a-2\Re(v)>1.
\tag{5.2}
\]

For `a>=1`, the simpler defining bound gives convergence from
`a+delta>1`. The chamber is connected and overlaps the initial
absolute definition. Local normal convergence gives holomorphic
continuation of that same function. It is not merely a new series
defined on a disjoint region.

For the row mean, a coefficient depending on `k` is not assumed to
be independent of the row: `tilde-a_k(d)` is used as a contraction
and `h(d)` is bounded by its uniform row majorant. Minkowski then
applies to the finite partial sums, followed by norm convergence.
The spectral theorem supplies exactly the uniform auxiliary loss
needed in (5.1).

The balanced scalar exponent is `2a-Re(v)`. At the upper chamber
boundary `Re(v)=(3a-1)/2`, its infimum is `(1+a)/2`. Inserting
the proved strict spectral threshold `a>5/8` gives the limiting
scalar value `13/16`, approached at `v=7/16` and `s=-3/16`.
This lies to the right of the stated standalone kernel pole
`s=-1/3`. All these boundaries are strict. The number `13/16`
is not a zeta zero-free bound, an original-moment exponent, or
evidence that the required full-row covariance has been controlled.

Section 8 correctly compares the candidate physical energy
`Q D^(13/8)` with the existing minimum. Writing `Q=D^h`, the
classical physical exponent is `2` for `0<=h<=1`,
`(2h+4)/3` for `1<=h<=4`, and `h` thereafter. The candidate
improves it only for `h<3/8`. In that range the inherited
factorwise bound `D(Q+Q^2)` is already smaller: it dominates
the candidate whenever `h<=5/8`. These ranges cover all
nonnegative `h`. The direct inequalities in bootstrap (8.3)
verify the same conclusion without a power parametrization. Thus
even if the indicated contour composition is supplied, this scalar
improvement does not improve the available physical covariance bound
at any row scale. The comparison makes no claim that the required
contour composition has been independently established here.

## 6. Review boundaries

The continuation and conductor-mean deductions are valid at their
explicit assumptions. Applying them to every term of the actual
reflected object still requires the independently reviewed finite-ray
cube covariance and the all-cusp coefficient adapter. Their
composition, including ramified and bad-prime summation, is a
separate load-bearing step.

The review did not run a numerical moment experiment or a Lean
build. It did not substitute a quadratic row for the surviving
sextic row in the bootstrap. It did not identify a residue with a
moment diagonal. The original all-row higher-moment problem and its
long dual covariance remain open.
