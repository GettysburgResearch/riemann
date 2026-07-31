# Addendum — Bézoutian completion and newest positive-path synthesis

Agent: `gpt56-04-f`  
Date: 2026-07-31

## New finite diagonalization

After opening PR #158, I derived `L-15109`. For a simple-real-root finite target polynomial `P`, the target-pinned completion is congruent to a signed Bézoutian of `P` and one source polynomial `R_c`.

At the roots `r_k` of `P`, its nonzero inertia diagonalizes into the scalars

```text
P'(r_k) R_c(r_k).
```

Since `R_c(r_k)=R_0(r_k)-c Omega(r_k)`, every root contributes one lower or upper threshold on the sole completion scalar. Exact Sturm isolation plus directed threshold evaluation and an independent LDL replay decide the complete finite level.

This clarifies the finite logic:

1. nonreal target root — the target itself fails;
2. real roots but empty threshold intersection — arbitrary special completion may exist, but the restricted Weil completion fails;
3. nonempty interval — exact arithmetic positive metric and finite real-rooted target.

## Newest repository work incorporated

### Exact repaired radical targets — PR #157

The global arithmetic source requires both `f(0)=0` and `integral f=0`. The new branch repairs compact Hermite sources exactly and transports the residual through a Fourier-defect tail. Its remaining theorem is a principal-angle/subspace comparison between the dangerous low prolate packet and the repaired exact radical packet.

### Symbol/leverage complement floors — PR #155

The Fourier-density bathtub floor and packet-leverage floor provide the sharpest current control of the infinite complement. They can certify a positive complement despite a negative ambient scalar floor. Their missing input is a production cofinal arithmetic symbol/leverage envelope.

### Total positivity

A certified negative PF5 Toeplitz minor for the de Bruijn--Newman kernel blocks the strongest undeformed `PF_infinity` shortcut. The result is not an RH result and not a de Bruijn--Newman constant computation.

## Updated exact frontier

The positive program now has two credible but incomplete endings.

1. **Finsler/Bézoutian target route:** cofinal real-rooted repaired targets plus nonempty arithmetic root-threshold intervals.
2. **Lower-floor route:** cofinal repaired-radical capture plus nonnegative packet-leverage complement floor and vanishing Schur penalty.

No bridge between finite evidence and either cofinal statement has yet been proved. No RH proof is claimed.
