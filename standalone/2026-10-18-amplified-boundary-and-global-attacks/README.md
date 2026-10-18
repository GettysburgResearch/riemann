# A global parameter corollary and attempts to go substantially farther

**Result:** under the analytic hypotheses explicitly stipulated by Xu--Sang v2,

\[
\boxed{\zeta(s)\ne0\quad\text{for}\quad
       \operatorname{Re}s>\frac{43744333}{50000000}=0.87488666.}
\]

The same consequence holds for every finite-order Hecke \(L\)-function over
\(\mathbb Q(\sqrt{-3})\) and every Dirichlet \(L\)-function. Principal poles
are allowed. This is a statement at every height and conductor.

**The improvement is only \(4\times10^{-8}\) over Xu--Sang's reported
\(0.8748867\).** It is a new exact parameter deduction from their framework,
with its upstream assumptions preserved. This packet does not establish
those imported analytic inputs, a substantially wider zero-free region,
or RH. It makes no claim of worldwide priority for the new decimal.

Start with the [theorem and complete certificate proof](correlated/UNIFORM_BOUNDARY.md).
The arithmetic uses exact rational numbers throughout. A separately written
bivariate polynomial checker reproduces every coefficient and every scalar
margin. Two additional agents reviewed the analytic interface and the
global quantifiers; these are reviews within the same AI session.

## What changed relative to the preceding packets

The preceding [#1003](https://github.com/GettysburgResearch/riemann/pull/1003)
contains finite theta constructions and quadratic-family estimates, while
leaving their global zero-exclusion premises open. This continuation
changes the working analytic comparison by using the newer
[Xu--Sang manuscript, arXiv:2610.15291v2](https://arxiv.org/html/2610.15291v2).
Credit for that manuscript's numerator estimate belongs to its authors.
Our new contribution to that route is the parameter choice and its exact
certificate, not the numerator theorem.

The exact comparison is

| Result | Right boundary | Status in this packet |
|---|---:|---|
| Xu--Sang's final stated value | \(0.8748867\) | Imported, with its explicit analytic assumptions |
| This parameter corollary | \(0.87488666\) | Complete exact admissibility proof and application of the imported closure criterion |
| Fixed-\(\kappa\) limit of the unchanged endpoint | \(0.8748866496166314191\ldots\) | Exact necessary condition, expressed algebraically |
| \(5/6\) or \(1/2\) | \(0.833333\ldots\) or \(0.5\) | Not obtained |

The limit in the third row is not a bound on zeta zeros. It is a limit on
this particular sufficient estimate. It explains why further searches for
nearby parameters cannot supply a substantial advance.

## 1. The global proof

The selected tuple is

\[
b=\frac{173}{2000},\qquad
\ell=\frac{6267001}{37500000},\qquad
\kappa=\frac{29991}{40000}.
\]

The moment license comes from Xu--Sang's established first stage,
\((1+\kappa)/2=69991/80000\), before our candidate boundary is invoked.
After clearing a positive denominator, the endpoint condition becomes

\[
Q=A(y)\delta^2+B_q(y)\delta+C(y)>0,\qquad y=1/2-x\ge0.
\]

All coefficients of \(A\) and \(4AC-B_q^2\) are positive rationals.
The identity

\[
4AQ=(2A\delta+B_q)^2+(4AC-B_q^2)
\]

therefore proves the inequality over the entire continuous parameter
rectangle. The other source conditions, including the small-row,
floor, prime-supply and positive error margins, are also checked exactly.
The source's general licensed-parameter closure lemma then gives the
global half-plane. No inference from a finite zero census is used.

The [fixed-\(\kappa\) limit](correlated/XU_FIXED_KAPPA_LIMIT.md) is a separate
exact proof: at a specified algebraic \(\delta_*\), the coefficient of the
geometric parameter \(b\) vanishes. The remaining inequality forces the
limiting boundary shown above, even if \(b\) is allowed to vary freely.

A stronger design constraint appears in the
[direct-estimate floor](correlated/DIRECT_ESTIMATE_FLOOR.md). For Liu's
complete free-geometry direct recipe, an exact decomposition into
nonnegative terms proves

\[
B_{\rm low}\ge\frac{13}{15}+\frac{17k}{60}\ge\frac{13}{15}.
\]

This is independent of every high-side moment or row-count estimate.
Even perfect bounds on that side would not reach \(5/6\) through the same
direct formula. With the principal exponent unchanged, a new direct bound
must save at least \(1/30\) to reach \(5/6\), or \(11/30\) to reach RH.
These are necessary budgets for that recipe, not estimates already proved.

## 2. A direct attack on the Möbius coefficients

The [native calculation](native/MOBIUS_CLOSURE_ATTEMPT.md) uses the actual
Möbius function and its full convolution inverse. It retains every old
product and the complete strict square-step interval. The exact harmonic
remainder becomes

\[
Z_Y(x)=\frac{S_Y(x)}x-\int_x^\infty\frac{S_Y(t)}{t^2}\,dt,\qquad
S_Y(t)=\sum_{a,b\le Y}\mu(a)\mu(b)
          \left(\frac12-\left\{\frac{t}{ab}\right\}\right).
\]

The native sign-crossing condition controls the balance vector only on
its specified cofinal set. It is not promoted to an all-\(Y\) estimate.
In the critical box, low reciprocal harmonics have only bounded phase
variation. Applying the available Möbius bound there reproduces the old
energy exponent. It does not pay the extra power required for the proposed
contraction. The exact inverse identity also preserves a hypothetical
zero's singularity after canceling its extra multiplicity.

Recombining all products before using the crossing condition gives a
further exact result. On \(s=1/2+it\), put
\(A_Y^{\rm old}(s)=\int_1^Y m(x)x^{-s}\,dx\). The two boundary terms in
\(\zeta(s)G_Y(s)^2/(s-1)\) can be removed with squared frequency error

\[
\ll_\varepsilon Y^{-45/71+\varepsilon}F_Y+Y^{-2}
\]

at \(T=Y^{84/71}\), on the literal crossing set. The remaining term is
\((s-1)\zeta(s)(A_Y^{\rm old}(s))^2\), with its physical window retained.
The small endpoint value \(m(Y)\) does not multiply this interior term.

The [joint numerator comparison](native/JOINT_NUMERATOR_CLOSURE.md) pursues
the correlated-moment alternative. Its proposed twist-safe improvement
has an exact excess over the existing estimate:

\[
J-K=\frac{P_m-R}{4}
       +\frac q2\,|z(m)-z(v)|\ge0.
\]

Allowing all intermediate numerator contours, including reflection and
outside Mellin costs, likewise reduces to the two already known contour
choices. At the critical short-witness subdivision, the controlling
numerator block has exactly the length of the plain detector already
known to be large. A new signed inverse/plain estimate remains necessary.

## 3. A quadratic replacement for the sextic detector

The [quadratic probe theorem](field/QUADRATIC_PROBES.md) constructs an exact
local Möbius detector using quadratic characters:

\[
\sum_{x\bmod q}\chi_q(x(x+1))e_q(hx)
 =e_q(-h/2)\operatorname{Kl}_q(1,h^2/16),
\]

for odd squarefree \(q\), with inverses interpreted modulo \(q\).
At \(h=0\), the value is \(\mu(q)\).

The obstacle is explicit: the target occurs at a degenerate frequency.
For large primes \(p\), exact recovery from nonzero frequencies with
coefficients in any fixed number field has a unique solution, using every
frequency with coefficient \(-1\). Its coefficient norm is \(p-1\).
This does not rule out a different or growing coefficient class, but it
prevents a cheap fixed-field cancellation scheme of this form.

The proposed inert-prime restriction also has an exact square-root branch
at \(s=1\). An uncentered summatory bound with any fixed exponent below one
would contradict its local zero order. The note proves this obstruction
without assuming any new zero-free theorem.

## 4. A quartic detector with every Möbius sign retained

The [principal and quartic calculation](field/PRINCIPAL_CORRELATIONS_AND_QUARTIC.md)
goes beyond replacing one character order by another. Over
\(F=\mathbb Q(i)\), with the ramified prime removed, it derives the exact
identity

\[
\widetilde g_4(c)^2=\mu_F(c)\epsilon(c),\qquad
\epsilon(c)=\left(\frac{-1}{c}\right)_4\frac{c}{|c|},
\]

for every primary generator \(c\), including inert primes and
nonsquarefree moduli. Consequently

\[
\sum_{c\ {\rm primary}}
\frac{\widetilde g_4(c)^2\epsilon(c)^{-1}}{N(c)^s}
=\frac1{\zeta_F^S(s)},\qquad \Re s>1.
\]

This uses the classical quartic Gauss identities with their exact
normalization. It does not claim that the resulting reciprocal series
has acquired a new analytic continuation.

The note then implements Suzuki's actual two-residue-class square-index
formula, including its matrix sign. The required object becomes a
bilinear tensor of two equal square-index theta coefficients. A usual
Hermitian norm replaces \(\mu_F\) by \(\mu_F^2\); a simple square of theta
selects an additive convolution; a linear square-index pairing supplies
only one Gauss factor. These operations therefore do not provide the
needed signed diagonal.

The elementary quartic/quadratic pairing also has a central-character
mismatch. A compensating genuine Eisenstein factor removes that mismatch,
so a compensated period remains open. Its convergence, cusps, second
Gauss factor and complete uniform estimate still need to be constructed.
The source's completed functional equation carries a zeta denominator
and the square-index conductor cost; neither is canceled without a
licensed argument.

The same note tests a coupled principal-target Mellin operation. Its
diagonal functional-equation cancellation is exact, but the new Cauchy
pole meets an existing zeta pole. The resulting double-pole residue
contains \(L'_u/L_u\) with an explicit coefficient. Its transverse
contour also pays a conductor-to-length cost. Both contributions remain
in the stated next estimate.

## 5. Global theta and heat attempts

Three analytic results test the proposed path from finite moment matching
to a global narrow band:

- [Kernel instability](theta/KERNEL_STRIP_INSTABILITY.md): arbitrarily close
  positive, strongly log-concave perturbations of the actual theta kernel
  can preserve any fixed finite set of its normalized moments exactly
  while acquiring zeros at any prescribed off-real height and arbitrarily
  large real part. The perturbations do not retain the exact modular
  identity.
- [Reverse heat obstruction](theta/NO_REVERSE_HEAT_STRIP.md): a three-spin
  construction has fixed variance and an arbitrarily small positive heat
  threshold, yet any prescribed initial Fourier zero band. A threshold
  estimate alone cannot be run backwards into a narrow original strip.
- [Modular positivity transfer](theta/MODULAR_POSITIVITY_TRANSFER.md): the
  exact positive gamma-convolution representation controls a Laplace
  transform. Its positivity does not by itself establish the required
  Stieltjes property for the logarithmic Mellin transform. A related shape
  parameter already has forced off-line Mellin zeros.

These are proved identities or obstructions to specified inference steps.
They do not exclude a theta construction preserving additional exact
arithmetic structure.

## Does dropping “all number fields” help?

The global corollary already works over one auxiliary field,
\(\mathbb Q(\sqrt{-3})\). Ordinary zeta is retained because
\(\zeta_F=\zeta L(\,\cdot\,,\chi_{-3})\), and the nonprincipal factor is
entire. No theorem for every number field is required.

The family of auxiliary characters plays a different role: it licenses the
moment estimate and the common displacement in the closure argument.
Dropping that family while keeping the same proof would remove a premise.
A principal-target improvement must change an actual binding estimate or
construct a new zero-preserving observable.

## Reproduction and review

Run from this packet directory:

    python -S -B verify_packet.py --replay

The [validation record](VALIDATION.md) identifies the acceptance semantics,
independent reviews and limitations. The manifest covers all packet files
except itself. The main mathematical files and exact certificate are
individually bound by SHA-256 in the independent reports.

This is an additive proposed packet stacked on frozen #1003 at commit
669b6a01f4d4858ae1ef806b07547be95c08c935. Inherited research and integrated
status are not revised by these standalone claims.
