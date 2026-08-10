# Xi-cardinal Gram capture — session report

Date: 2026-08-11  
Branch: `research/gpt56-pro/364-xi-cardinal-gram-capture`  
Base: PR #364 head `afa9ee2145b04749fe55c1607c2fbe0ffc802e96`  
Status: **NEW ANALYTIC THEOREM; RH UNPROVED**

## 1. Question attacked

PR #364 reduced finite off-line isolation to the capture scalar

```text
C_Z(t)=t* K_Z^(-1)t
```

or, equivalently, the target-pair Schur complement of the zero-evaluation Gram.
A fixed support can be arbitrarily ill-conditioned, so the open question was
whether a cofinal localisation hierarchy could keep this target quantity under
control while the finite zero packet grows.

## 2. Main theorem

Fix a hypothetical nonreal centered zero `omega` of multiplicity `m`.  Let

```text
L_omega(z)=Xi(z)/[a_omega (z-omega)^m]
```

be its exact Xi-cardinal function and put

```text
h=L_omega-L_(conj omega).
```

Using Riemann's theta-kernel Fourier representation and a zero-resolvent
identity, the inverse Fourier source `q` of `h` is proved to decay faster than
every Gaussian.  Consequently, for every `a>1/2`,

```text
M_(omega,a)=int |q(u)|^2 exp(2a|u|)du < infinity.
```

In the strip RKHS with kernel

```text
kappa_a(z,w)=4a/[4a^2+(z-conj(w))^2],
```

the same source is an exact interpolant with values

```text
(+1,-1,0,0,...)
```

at **every** finite zero packet containing the target pair.  Therefore

```text
C_a(Z,t)<=M_(omega,a)
```

uniformly in the number, spacing, and internal conditioning of nuisance zeros.

Compact smooth exact interpolants and the complete critical modulation lattice
then give finite Gabor Grams `K_j` with support lengths `L_j` satisfying

```text
C_(Z_j)(t)<= [M_(omega,a)+o(1)]/L_j.
```

If `S_j` is the target-pair Schur complement,

```text
S_j >= [L_j/(M_(omega,a)+o(1))] t t*.
```

Thus the target Schur complement cannot collapse along an adaptively growing
complete-kernel hierarchy; it has a protected rank-one component growing
linearly in the support length.

## 3. Why division by a zero improves, rather than destroys, localisation

The key lemma is elementary but easy to miss.  If `f` is super-Gaussian and
`fhat(omega)=0`, then

```text
R_omega f(u)
 =-i exp(-i omega u) int_(-infinity)^u exp(i omega t)f(t)dt
```

also equals the upper-tail integral because the total integral is zero.  The
lower-tail expression controls one end and the upper-tail expression controls
the other.  Hence `R_omega f` remains super-Gaussian and

```text
(R_omega f)^hat(z)=fhat(z)/(z-omega).
```

The multiplicity of the Xi zero allows this operation to be iterated exactly.
This supplies the form-domain statement that earlier kernel branches had to
leave as an inherited Xi-cardinal hypothesis.

## 4. Full Weil-form capture

The construction is diagonalised in the seminorm

```text
P(f)=int exp(|u|/2)(|f|+|f''|).
```

For every centered zero `zeta`, two integrations by parts give

```text
|fhat(zeta)| <= C P(f)/(1+|zeta|^2).
```

Since the zeta zero count implies summability of `(1+|zeta|)^(-4)`, the complete
Weil form is continuous in this seminorm.  The compact exact interpolants can
therefore be chosen so that

```text
Q_W(f_j,f_j)->-2m.
```

This removes the possible circularity between support length, packet radius,
and unseen-zero tail: the actual vectors converge directly to the global
cardinal difference in the complete form topology.

## 5. Adversarial scope checks

### Fixed support

A fixed-support uniform bound over arbitrary finite point configurations is
false.  PR #364's clustered synthetic example is retained.  The theorem permits
support and mode count to grow after each finite packet is chosen.

### Zero separation

No lower bound for gaps between zeta zeros is assumed.  The uniform competitor
is one global Xi-cardinal source that already vanishes at every nuisance zero.

### Multiplicity

Multiplicity is handled by iterating the zero-resolvent exactly `m` times.  The
finite interpolation packet contains distinct coordinates; the Weil value of
the target pair is `-2m`.

### Finite dimensionality

The compact interpolant first lives in the complete critical lattice.  Nested
finite consecutive mode blocks have Grams increasing to the complete Gram;
once the complete Gram is positive definite, inverse capture costs converge
monotonically.  A finite block therefore attains the same bound up to an
arbitrarily small error.

### No hidden RH input

The theorem assumes a hypothetical off-line zero and constructs the negative
direction it would force.  It uses the classical Xi Fourier kernel, not any
positivity statement equivalent to RH.

## 6. Exact regression

```text
experiments/X-zeta23-xi-cardinal-capture/
```

uses the planted-zero toy entire function

```text
F(z)=P(z) sqrt(pi) exp(-z^2/4).
```

The retained run verifies:

```text
PASS_XI_CARDINAL_GRAM_CAPTURE
```

with:

```text
cardinal error                         4.94e-15
nested strip costs                    5.775, 6.130, 11.475, 13.149, 14.864
weighted source norm                  23504.084
rank-one Schur residual minimum       0.120379
local pair Weil value                 -2.0000000000000036
```

Compact exponential-window kernel errors decrease monotonically from about
`1.045` at radius two to `0.00298` at radius ten.

## 7. Corrected frontier

The Gram-capture obstruction from PR #364 is closed at cofinal-hierarchy scope.
Combined with PR #199, a hypothetical off-line pair now forces a fixed negative
moat in every complete corrected-kernel hierarchy.

The remaining conclusion-producing theorem is solely the arithmetic lower
floor for the complete corrected Weil kernel:

```text
B_ker,j-Z_ker,j* C_j^(-1)Z_ker,j >= -epsilon_j G_ker,j,
epsilon_j->0.
```

Under false RH, the theorem in this branch proves that such a floor must fail.
No unconditional proof of that floor, and hence no proof of RH, is claimed.
