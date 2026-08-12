# Integration addendum — exact delayed form core and compressed Hardy delay dilation

## Freeze

```text
parent PR:      #400
parent head:    7dc9fec9eb5fab4ee9340ddbc5a52e36a6ab617e
parent branch:  research/gpt56-pro/91028-levy-fock-hardy-completion
session date:   2026-08-13
RH:             unproved
```

Read the child branch head from GitHub after publication.

## Chosen path

This addendum attacks the delayed two-sided Hardy geometry surrounding
`T-91008`, `L-91316`, and correction `R-91011`.  It does not rename the
RH-equivalent arithmetic domination.  It closes three antecedent geometric
obligations exactly.

## New exact claims

### `L-91320` — delayed carrier completeness

A generic distribution theorem proves that translates of any nonzero analytic
causal mother with sufficient exponential decay have exactly one weighted
half-line defect: the integral functional.  The proof makes the delicate step
fully legitimate by writing the multiplier of `DH` as `D(L1)-L1`, invoking
Fourier injectivity on tempered distributions, and using a full-measure delay
to avoid every isolated zero.

Applied to the branch Cauchy impulse, this upgrades

```text
L-91034.12  PROPOSED -> PROVED.
```

The hidden jump in `R-91008` is genuinely removed by the delay fibre.

### `L-91321` — canonical bridge

The two half-line integral defects have explicit Riesz vectors.  Their global
mean-zero coupling is the orthogonal one-dimensional channel

```text
b_eta(t)
 = eta exp(-eta t) 1_(t>0)
   - eta exp(eta t) 1_(t<0),
```

with norm squared `2 eta` and transform

```text
-2 i eta u / (eta^2+u^2).
```

Together with `L-91320`, this upgrades the Hilbert-space core statement

```text
L-91034.13  PROPOSED -> PROVED,
```

while leaving its arithmetic bridge row/column unsigned.

### `L-91322` — compressed-delay dilation

For every inner `Theta`, the model space `K_Theta` is invariant under the
adjoint upper-Hardy shift semigroup.  Therefore the raw boundary delay has the
exact decomposition

```text
exp(-i tau dot) g
 = T_(Theta,tau) g + L_(Theta,tau) g,
```

where `T` remains in `K_Theta` and `L` is the escaped negative-Hardy prefix.
Every finite cross-delay Gram matrix splits exactly into the resident Gram plus
the leakage Gram.  The leakage satisfies a conservative cocycle.

This is the precise repair of `R-91011`: raw delays need not preserve the
Suzuki model space, because their canonical compression plus explicit leakage
is already an isometric dilation.

The same claim sharpens `L-91316`: its score observation is a coisometry, so the
Fisher-Hankel source decomposes orthogonally into the Suzuki tangent and the
score-orthogonal reserve.  Composing this with `T/L` gives a fixed observation
for every same-orientation delay packet, on the declared form domain.

## Verification

```text
experiments/X-91320-compressed-delay-dilation/
PASS_COMPRESSED_DELAY_DILATION
```

The verifier uses exact Gaussian integers in the finite model
`K_(z^m)`.  It checks 25 pairwise cross-Gram identities, 245 semigroup
identities, and one five-vector packet Pythagorean identity without floating
point.

## Corrected route state

```text
scalar undelayed form core                         REFUTED
vector delayed half-line form core                 PROVED
canonical global bridge geometry                   PROVED
raw delay invariance of Suzuki model space         FALSE
compressed delay + Hardy leakage dilation          PROVED
all same-orientation cross-delay L2 Gram entries   PROVED
Fisher score / orthogonal-reserve splitting        PROVED
physical Cauchy test -> resident base vector        OPEN
A_a-domain stability under compressed shifts       OPEN
mixed-orientation and bridge arithmetic entries    OPEN
source arithmetic >= Fisher-Hankel resident norm   OPEN / RH-BEARING
Riemann Hypothesis                                 UNPROVED
```

## Remaining highest-leverage theorem

After the present geometry, the conclusion-producing resident inequality is
still

```text
C_a^(Jordan+gamma+pole)
 >= 2 a^2 Var_a(Y) A_a* A_a.
```

To use it for the exact delayed Cauchy packet, the next attack must also pin the
undelayed physical-to-model-space base map and prove stability of the chosen
Fisher-Hankel form domain under `T_(Theta_a,tau)`.  Once those are established,
same-orientation delay polarization is automatic; no independent delay
invariance theorem remains.

The mixed Hardy orientation and the explicit bridge row/column should then be
handled as one finite block extension, not by scalar diagonal estimates.

## Integration recommendation

Stack this child PR on #400.  Integrate it as an exact geometric advance and
normative correction.  Do not present it as the arithmetic domination or as a
proof of RH.
