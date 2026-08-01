# L-16230 — Source-derived radial, derivative, and endpoint placeholders decay on an adaptive cofinal diagonal

Claim ID: `L-16230`  
Status: **PROVED DIAGONAL EMITTER THEOREM; COMPLETE ARITHMETIC ALIAS GRAM SEPARATE**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Depends on: exact leakage normalization `L-16217`; fixed-mode CCM/Dunster convergence; `L-16221`

## Statement

Let `gamma_j -> infinity`. At each level take the exact two-constraint repaired
source packet in modes `0,4,8,12`. Let `s_(n,j)>0` be the exact positive-ray
leakage amplitudes and let `a_(n,j,k)` be the directed angular Legendre
coefficients.

For every prescribed `epsilon_j>0`, finite angular cutoffs may be chosen so that
the normalized coefficient-tail synthesis errors satisfy

```text
sum_source epsilon_rad,j <= epsilon_j/gamma_j,
```

and consequently

```text
sum_source epsilon_drad,j <= epsilon_j.
```

The horizontal-strip coefficient-tail error is `O(epsilon_j/gamma_j)`.

For the fixed mode packet, the repaired physical sources converge in fixed
Sobolev order to finite Hermite combinations. Hence

```text
sup_j ||f_j^(4)||_1 < infinity.
```

With `lambda_j^2=gamma_j/(2pi)`, the p=4 Poisson endpoint ledger therefore has

```text
point charge       = O(gamma_j^-2),
L2 squared charge  = O(gamma_j^(-7/2)).
```

Choosing, for example, `epsilon_j=2^-j` proves that the radial, frequency,
horizontal, endpoint, and their directly reconstructed deterministic-error
fields all tend to zero.

## Proof

For one fixed block, the directed Legendre coefficient sequence is square
summable. Since `s_(n,j)>0`, its normalized tail tends to zero as the finite
cutoff tends to infinity. Increase the cutoff until the displayed source-packet
bound is met. Differentiating the finite Fourier kernel with respect to its
scaled radial frequency multiplies the omitted source by at most `gamma_j`,
because `|t|<=1` on the angular support. This proves the radial and derivative
statements. Evaluation in a horizontal strip of half-width `1/(2gamma_j)` costs
only a fixed exponential factor.

Fixed-mode Dunster convergence, including any fixed derivative order on compact
physical coordinates and the Gaussian exterior envelope, gives convergence in
`W^{4,1}` to the repaired Hermite packet. Thus the fourth-derivative norms are
uniformly bounded. Insert this bound in the exact `p=4` ledger

```text
(zeta(4)-1)||f^(4)||_1/(2pi lambda)^4
```

and its squared L2 analogue with denominator proportional to `lambda^7`.
Because `lambda^2` is proportional to `gamma`, the stated powers follow.

Every bound is checked separately at each finite level; no complexity estimate
for the adaptive cutoff is required. QED.

## Production boundary

This theorem closes the decay of the fields that previously appeared as

```text
t2=1,
t2_derivative=4,
||f^(4)||_1<=10^100.
```

It does not identify the complete arithmetic tail Gram with the first Poisson
sample. A production profile-Gram floor still requires a directed enclosure of
the complete cross-alias operator. `X-16207` makes that field mandatory and
fails closed when it is absent.
