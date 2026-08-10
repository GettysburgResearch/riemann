# Continuation report: pole-null Cauchy kernel, exact index-two shift, and heat amplification

Date: 2026-08-11  
Proposed stack: Fredholm-Pontryagin PR on top of PR #365  
Status: theorem packet and finite replay; RH unproved

## 1. Why continue past the first Fredholm packet

The first packet produced a trace-class Weil operator whose Fredholm determinant has one positive root per off-line pair. Two features remained unnecessarily opaque:

1. its evaluation kernel was only estimated, not explicit;
2. the positive pole term obscured the physical prime/gamma competition.

Both can be removed exactly.

## 2. Explicit Cauchy-Sobolev metric

Reverse the order of confinement and Sobolev smoothing:

```text
J=(c^2-d^2)^(-1) M_(exp(-a|u|)),  1/2<a<c.
```

Then

```text
K(z,w)
 =4a/[(c^2+z^2)(c^2+conj(w)^2)
      (4a^2+(z-conj(w))^2)].
```

The diagonal is `O((1+|Re z|^2)^-2)`, so the complete zero form is trace class. The prime-shift nuclear norm is bounded by

```text
C_(a,c) exp(-a|y|)(|y|+1/a),
```

which again makes the all-prime series summable.

This supplies a concrete rational kernel for exact finite determinants and interpolation experiments.

## 3. Pole cardinals and exact index two

The two functions

```text
E_+=Xi(z)(1-2iz),
E_-=Xi(z)(1+2iz)
```

are exact cardinals at the pole coordinates `+i/2,-i/2` and vanish at all nontrivial zeros. For `Q=W-P`, they form a negative identity block.

Correct every off-line Xi-cardinal by subtracting its two pole values against `E_+,E_-`. The corrected cardinal stays super-Gaussian, keeps its pair values, and becomes pole-null.

This proves

```text
n_-(Q)=q+2,
n_-(W restricted to pole-null tests)=q,
```

where `q` is the number of off-line reflected pairs.

Thus RH is exactly the fixed-index statement `n_-(Q)=2`.

## 4. Exact Lévy-prime form

The gamma multiplier has the Lévy representation

```text
mu(t)-mu(0)
 =1/pi int exp(-y/2)/(1-exp(-2y)) [1-cos(ty)]dy.
```

On pole-null tests, Weil's form is therefore

```text
positive continuum jump energy
+ negative constant mass
- discrete prime-power adjacency.
```

The pole-free form satisfies `Q(|f|)<=Q(f)`. The remaining constraint is genuinely only the two pole moments, already removed in the projected operator.

## 5. Entire heat amplifier

For the pole-null trace-class operator `A0`, define

```text
Theta(beta)=tr(exp(-beta A0)-I).
```

Then

```text
RH <=> Theta(beta)<=0 for every beta>0.
```

A single negative eigenvalue makes `Theta(beta)` positive and exponentially large for large beta. Its all-order prime-word expansion has factorial damping and converges globally, unlike the local logarithmic determinant series.

## 6. New frontier

```text
explicit Cauchy-Sobolev trace metric       PROPOSED COMPLETE
exact two pole cardinals                   PROPOSED COMPLETE
pole-free index = off-line pairs + 2       PROPOSED COMPLETE
pole-null index = off-line pairs           PROPOSED COMPLETE
gamma Lévy jump representation             PROPOSED COMPLETE
pole-free diamagnetic inequality            PROPOSED COMPLETE
entire heat-trace RH criterion              PROPOSED COMPLETE
index(Q)<=2                                 OPEN / RH-EQUIVALENT
Theta(beta)<=0                              OPEN / RH-EQUIVALENT
Feynman-Kac/polymer domination              OPEN
Riemann Hypothesis                          UNPROVEN
```

The strongest conceptual target is now a Pontryagin-index-two theorem for an explicit Lévy operator perturbed by the prime-power adjacency.
