# Exact Kreĭn–Langer source/critical/port decomposition

## Status

```text
branch: research/gpt56-pro/91008-cauchy-square-clark-jordan
claim:  L-91034
control:R-91005
replay: X-91025
RH:     UNPROVED
```

## Main result

In the shifted half-plane `H={Re z>0}`, put

```text
Theta_a(z)=xi(1/2-a+z)/xi(1/2+a+z).
```

Let `B_a` be the Blaschke product of the genuine poles of `Theta_a` in `H`;
these are exactly the uncancelled zeros of depth `d>a`. Let

```text
Delta_a=b_a^2 b_(2a)^2 b_(4a)^2
```

be the six-state deterministic Cauchy inner factor. The symmetric Hadamard
product proves

```text
A_a=B_a Theta_a       analytic inner,
I_a=Delta_a B_a Theta_a  inner.
```

For

```text
K_F(z,w)=[1-F(z)conj(F(w))]/[z+conj(w)],
```

the product rule is

```text
K_(FG)=K_F+F conj(F) K_G.
```

Applying it twice gives exactly

```text
K_(I_a)/(Delta_a B_a conj(Delta_a B_a))
 =K_(Theta_a)
  +K_(Delta_a)/(Delta_a B_a conj(Delta_a B_a))
  +K_(B_a)/(B_a conj(B_a)).
```

Thus, at the meromorphic-inner/model-space level,

```text
safe positive pole-removed source Gram
 =critical scattering Gram
  +deterministic stable ports
  +crossed zero ports.
```

The source, stable, and zero-port kernels are positive semidefinite. The
critical kernel may have negative squares.

## Explicit zero ports

For one simple crossed pole `p`,

```text
K_(b_p)/(b_p conj(b_p))
 =2 Re(p)/[(z-p)(conj(w)-conj(p))].
```

It is one positive rank-one output port. Conjugate poles realify into the
expanding/contracting two-state hyperbolic block. Under RH the pole Blaschke
factor is constant and the entire zero-port kernel vanishes.

Conversely, any off-line zero of depth `d>0` produces a nonzero port for every
generic scale `0<a<d`. Therefore

```text
RH
<=> crossed zero-port kernel is identically zero for every a>0.
```

## Exact firewall

Take `Theta=1/b_p`. The pole-removed inner function is the constant one, so the
safe source kernel is identically zero, but

```text
K_Theta=-K_(b_p)/(b_p conj(b_p)).
```

A nonzero positive pole port exactly cancels a negative critical kernel.
Therefore positivity and energy conservation do not force the port to vanish.
An exhaustion theorem is indispensable.

## Important correction

The identity above is a de Branges--Rovnyak/model-space identity. It is not yet
the full arithmetic CJHI identity.

The positive source of `L-91031` has Hankel form

```text
S_a(z+conj(w)),
```

whereas the pole-removed source here is genuinely two-variable. Likewise the
Cauchy-Weil filter in `T-91006` is a translation-invariant Hardy/convolution
map, not pointwise multiplication by the rational transfer in the analytic
variable.

A common linear filter preserves the exact four-term identity, but the actual
Cauchy filter must first be constructed on the common model-space domain. The
remaining theorem is therefore:

```text
construct an explicit arithmetic coisometry
from the L-91031 Stinespring space
onto the L-91034 pole-removed source space,
intertwining the actual Cauchy Hardy filter,
and prove that critical + deterministic outputs exhaust its norm.
```

Only then would the zero output be forced to vanish.

## Verification

The standard-library rational-complex replay returns

```text
PASS_KREIN_LANGER_CAUCHY_PORT_DECOMPOSITION
checks: 80
```

It checks the full kernel identity, product rule, simple rank-one pole formula,
Takenaka--Malmquist port expansion, and the one-pole cancellation firewall.
It proves finite algebra only.

## Honest frontier

```text
meromorphic-inner four-term kernel identity       EXACT
inner factorization from symmetric xi product     PROPOSED COMPLETE
stable and crossed-pole feature formulas          EXACT
RH <=> absence of crossed ports at all scales     PROPOSED COMPLETE
source positivity alone deletes ports             FALSE
arithmetic Hankel -> model-space coisometry        OPEN
actual Cauchy-Weil filter intertwining             OPEN
zero-port exhaustion/absence                      OPEN / RH-EQUIVALENT
Riemann Hypothesis                                 UNPROVED
```
