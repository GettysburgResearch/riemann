# Positive coefficient tail for the original physical horizon

Registered before acquisition. Scope: primes 2,3,5 and the original affine
twenty-moment observation, not a new measure or a coefficient-frame metric.

For A_e=[z^e]sqrt(1-z^2), D_e=[z^e](sqrt(1-z)-sqrt(1-z^2)), put
`w_e=|A_e|+|D_e|` and `u_e=sum_(i=0)^e w_i w_(e-i)`.
The exact sum W(q)=sum w_e q^e is
`2+sqrt(1+q)-2sqrt(1-q^2)`. Every affine decoder coefficient has
absolute value at most two. Hence each true physical field tail obeys

    |Z_infinity,j-Z_H,j| <= P_H
    P_H=2{ product_p W(p^-1/2)^2
             - sum_(2^a3^b5^c<=H) u_a u_b u_c / sqrt(2^a3^b5^c) }.

The positive omitted sum decreases with H, so a strict certificate at one
H proves the same bound at all larger horizons. Prefix enumeration is
complete, not sampled. The registered panel is H=2^32,2^40,2^48,2^56,2^61,
evaluated at 192-bit Arb precision, with at most 100000 smooth products.
No threshold between panel values is declared optimal.

The inherited independently certified infinite Gram lower bound is
`c=1/12000000`. Acceptance of `20 nu_0 P_H^2 < c/4` implies
the original physical norm lower bound `c/4=1/48000000` at EVERY horizon
at least H, by the operator triangle inequality. Failure of this sufficient
test is retained and implies no rank failure.

The producer binds the same primitive sources as physical_infinity.py,
reconstructs all exact binomial coefficients, and records the full prefix
digest and count. Independent controls compare direct ordered-pair
enumeration at small horizons with convolution-prefix enumeration.

Post-acquisition input-binding refinement, with the original panel and acceptance
predicate unchanged: authenticate `physical_infinity.py` before import at LF
SHA256 `9eaad7aac963f0ad13d2d4a2656258bf172e61fc51fbb5af74a0aff7f1b13207`,
and the already independently replayed L96/192 capture at SHA256
`e828069e8898a464741553a44f53a13bb11d93c5c27ed5475130656a99749757`.
The consumer verifies the original primitive manifest, coordinate normalization,
all twenty positive LDL pivots, and the certified lower endpoint exceeding
`1/12000000`. It does not claim to recompute the full Gram inside the small
tail replay. The separate `physical_infinity.py --check 96` does that.
