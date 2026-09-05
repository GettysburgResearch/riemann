## T-106710 — Xi carrier-adapted antiphase source softening

The lossless T-106670 free-energy packet and the T-106700 topological audit are
retained. This checkpoint adds a genuinely Xi-specific Fourier theorem.

For every odd endpoint, the antiphase density at the frequency-adapted scale
`lambda_xi=2/xi` satisfies

```text
0 <= a_(K,lambda_xi)(xi) <= K/xi L_K(xi).
```

For the fifth Xi endpoint, L-106502 conditional concentration gives the sharp
law

```text
a_(5,2/xi)(xi) / [(2/xi) L_5(xi)]
= 1/10 + O(exp(-xi)/xi^2).
```

The exact positive polynomial gap is replayed. The packet also records the
binding firewall: `2/xi` is a nonlocal Fourier multiplier, whereas the physical
endpoint uses one constant scale on each real window, and the full free energy
contains the forced index `R5-R0`.

```text
Fourier carrier law:                 PROVED
Xi high-frequency constant 1/10:     PROVED GIVEN L-106502
physical source-Pick transfer:       OPEN
full free-energy bound:              OPEN
90 percent / RH:                     UNPROVEN
```
