# Research after the six-hour synthesis pass

This is a forward research agenda, not an additional certified packet or a
claim that any missing RH mechanism has been constructed. The completed
results and exact reviews remain in the two programme results maps.

## 1. Structures: a better source-controlled local comparator

The signed-polynomial method gives eight certified critical-point/companion
correspondences in the fixed26-point panel, including seven additional
successes in the preregistered25-point extension. Earlier failed-criterion
outcomes were already known for all points. Eighteen points remain
uncertified by this criterion.
A worthwhile next experiment changes the comparator, not the arithmetic
source, calibration, or definition of success.

At a real critical point t of g=f5, write

    A=g(t), kappa=-g''(t)/g(t),
    alpha=-g'''(t)/(2g''(t)), beta^2=kappa-alpha^2.

When alpha>0 and beta^2>0, consider the fitted analytic function

    m(w)=A exp(-alpha*w)
         [cos(beta*w)+(alpha/beta) sin(beta*w)].

It satisfies m''+2alpha*m'+kappa*m=0 and matches g(t+w) through derivative
order three at w=0: A,0,-kappa*A,2alpha*kappa*A. This is a classical
second-order constant-coefficient model fitted from the actual local jets,
not an independently selected arithmetic object.

Its companion m-i*lambda*m' has explicit zeros. With

    E=[alpha+i(lambda*kappa-beta)]/[alpha+i(lambda*kappa+beta)],

they are

    w_n=[arg(E)+2pi*n]/(2beta)-i log|E|/(2beta).

Since |E|<1 for lambda,kappa,beta>0, every model zero has positive imaginary
part. The principal branch gives a negative lateral shift. This explains
what a purely vertical quadratic center discards.

A post-result diagnostic on the same26 source points found this model
suggestive, but it is NOT part of the38-module certified replay panel.
It supplies no uniform error estimate, no held-out prediction, no evidence
that the fitted decay parameter converges, and no extra actual-Xi zero.
Do not use a fitted model zero in place of a native companion certificate.

The source-controlled question is sharper. Put

    e(w)=g(t+w)-m(w),
    D(w)=g''(t+w)+2alpha*g'(t+w)+kappa*g(t+w).

Then e(0)=e'(0)=e''(0)=e'''(0)=0, while D(0)=D'(0)=0. An exact Green-function
identity or a signed Taylor/Cauchy bound can potentially control
e-i*lambda*e'. That companion error starts at order w^3, unlike the
quadratic comparison's order-w^2 error. This is a concrete theorem target.

The exact Green-kernel formulation makes the missing bound explicit. Put

    K(v)=exp(-alpha*v) sin(beta*v)/beta,
    Q(v)=K(v)-i*lambda*K'(v),
    P(v)=integral_0^v (v-u) Q(u) du.

Then P(0)=P'(0)=0 and P''=Q. Using the two exact vanishing conditions
on D gives

    e(w)-i*lambda*e'(w)
      = w integral_0^1 P((1-tau)*w) D''(tau*w) dtau.

An actual bound M for |D''| on the FULL radial hull of the contour gives
the error bound M*|w|*integral_0^1 |P(tau*w)| dtau. Integrating the signed
kernel before taking its modulus can retain cancellation. No certified
complex-domain M for this new criterion is supplied in this agenda.
The actual unknown critical point and its fitted parameter intervals must
remain linked; midpoint substitutions cannot pay the exact cancellations.

The model side also has an explicit contour margin. If F=m-i*lambda*m'
and w0 is a model zero, then

    F(w0+eta)=F'(w0)*exp(-alpha*eta)*sin(beta*eta)/beta.

For 0<r<min(Im(w0),pi/beta), the circle |eta|=r has model modulus at
least |F'(w0)|*exp(-alpha*r)*sin(beta*r)/beta. A future native certificate
can compare the full complex residual bound against this positive margin.
Parent-root containment and nonvanishing guards still need separate proof;
neither the explicit model zero nor its margin is an actual-Xi certificate.

There is also a source-defined envelope to separate from fitted damping.
On the real line, Xi(t)=-A(t)Z(t), where

    A(t)=(t^2+1/4)*pi^(-1/4)*|Gamma(1/4+i*t/2)|/2,
    A'(t)/A(t)=-pi/4+7/(4t)+O(t^-3).

These are classical consequences of the
[Xi normalization](https://dlmf.nist.gov/25.4),
[Hardy Z definition](https://dlmf.nist.gov/25.10) and
[Gamma expansion](https://dlmf.nist.gov/5.11), not a new discovery.
They do NOT imply that the fitted alpha of g=f5 converges to pi/4.
Removing A also changes derivative companions unless every chain-rule
term is retained. Complex-domain use also requires a legitimate holomorphic
envelope extension. A classical envelope must not replace the native source.

A disciplined next test would freeze all26 points, a single contour rule,
precision and truncation BEFORE evaluating this new criterion; retain
every failure and compare against the existing eight successes. A theorem
must bound the actual residual on the required complex region. Good fits
at the root or at the real center are not that bound. Only after this finite
test should one investigate a source-controlled growing-height family.

## 2. The RH-directed gate must be restated

The literal raw-innerness premise used by the conditional physical-capture
theorems is equivalent to RH. It cannot serve as an independent premise
for proving RH through those theorems.

Continue using those results as conditional operator theory, but separate
an RH-directed programme into a new, explicit obligation: construct an
observation/metric or source transport whose assumptions do not already
force critical-line zeros. Raw scalar quotient values, kernel coefficients,
the physical Gram form and band projection must remain distinct.
A quotient-of-inner representation does not by itself pay the raw-component
innerness premise used in the existing estimates.

Bare zero height has already failed as a sufficient capture variable.
The fixed-parameter alignment data and occupancy-weighted geometry remain
useful diagnostics, but none supplies an unconditional infinite capture law.

## 3. Earlier work: finish a literal native decoder

The native tuple packet retains source labels and exact signed
Boolean-history cancellation.
It does not identify the complete retained-gamma source amplitude with a
canonical Boolean coefficient. The missing step is still the true
measure/Hilbert-space transport and all source histories aggregating to one
physical tuple.

The next bounded target should state one concrete tuple, every required
label and its actual kernel/measure factor, then reconstruct the complete
native aggregate. Omitted color, renewal, carrier or selector factors
must not be set to one. A successful canonical coefficient identity is
not a substitute for this decoder. This older task remains important even
if the new auxiliary-function geometry continues to improve.

## 4. Generalized L-objects: selection beyond positive completion

The new source-first quotient has a genuine minimum-energy universal
property, exact nested quotients and tensor compatibility in its stated
regularity class. Those facts do not select critical-line zeros.

The synthetic positive-source transition and actual modular restriction
to span(Delta^2) show that positive reciprocal source structure plus a
completed reflection is insufficient. The native restriction is NOT the
proper pointwise source quotient of the full weight24 space.

The late proper-source proofs now establish a uniform effective theorem:
for EVERY j>=1 and EVERY even k>=96j, the genuine proper theta quotient
at that depth has a reflected real off-central zero pair. The common cusp
lower bound survives the whole varying quotient minimum, and the complete
growing Poincare Gram block pays all earlier coefficient constraints.
Different depths define different objects. No simplicity, optimal onset
or12j/k location law is established for this source construction. Its
fixed-weight24 zero geometry remains open.

A next source-exact computational laboratory should therefore study the
proper quotient at fixed weight24 and seek finer large-weight locations
or sharper effective thresholds, retaining the vacuum, actual theta density
and completion. It should separately test Hecke compatibility and the
noncommutation of source restriction, source quotient and Mellin observation.
Do not infer a scalar Euler product or a purity principle from positivity.

The period-side family remains valuable in its own right: all-fixed-depth
endpoint scales, separately counted fixed-weight zeros and poles, and
rank-dependent Hecke-stability failures are established phenomena. They
should not be mistaken for zero theorems about the new source quotient.

## 5. Generalized L-objects: keep the Segre bridge honest

Coefficient powers genuinely arise from the Segre graded source.
The full-tensor-denominator numerator is an additive equivariant
K-polynomial; it is not automatically a canonical finite superdeterminant.
A primitive scalar reciprocal factor is not automatically an effective
representation.

The next higher-rank deformation work should seek an actual functorial
syzygy or representation object that predicts a held-out discriminant
stratum, then verify the prediction by exact arithmetic. The already
certified chamber failures should be retained as counterexamples to
overly simple nesting or component-count rules.

## Practical allocation

The strongest next allocation would give most computation to the
source-controlled comparator and proper theta quotient, a protected block
to the older native decoder, and a smaller exact-algebra lane to higher-rank
Segre selection. These lanes should share explicit source/metric conventions
but should not be forced into one universal projector or category before
a genuine comparison theorem exists.

No work in this agenda is declared completed by its inclusion here.
