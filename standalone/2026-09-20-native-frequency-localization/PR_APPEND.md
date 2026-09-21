## NCL29 continuation: all prime powers and all-denominator angular control

**Proposed component proofs, not full composite-covariance control or RH.**
Publication is pending; a publisher must insert the actual verified head and
receipt before presenting this text as a remote publication update.

This continues #904 from `879497b4f11be2618c448efc1fa93f69b4022e4c` in the
add-only directory `standalone/2026-09-20-native-frequency-localization/`.
Read its PROOF.md, then the source and validation records.

The new weighted coefficient estimate is

```
sum_(q<=L^2) q |B_q|^2 <= 1024 K^4 H_L^4 H_(L^2)^4.
```

It gives a bound for the COMBINED centered harmonic function at ALL source
Fourier denominators outside ||a/q||<eta, including every mutual covariance
and the whole future. For L^2<=8X, the budget is
`2^21 K^4 eta^-1 H_L^9`. A separate bound pays EVERY pure prime-power
denominator at all angles, with budget `2^12 K^4 H_L^8`.

Scale-local capped completions use only actual prefixes y<=Y and exactly
reconstruct mu on their assigned blocks. Each full tail transform is applied
before block restriction; no moving-mask commutation is assumed. For
eta=1/[2 ceil(log_2(Y+1))], the full native reciprocal function splits into

```
m = -G - R on Y<k<(Y+1)^2;
||G||^2 <= C (1+log Y)^11.
```

R is the exact near-zero band at denominators with at least two distinct
primes. The target is still a native subquadratic bound for R. This is a
DIFFERENT exact partition from NCG28's single-source moving W_high, not a
claim to have bounded that whole older component. The principal angular
bound is generic for capped sources; native inversion identifies the output
but does not itself estimate R.

At Y=31, direct outward results give descriptive values: native increment
0.0990995899971780; controlled G energy 0.0193154620508891; remaining R
energy 0.0931762895197677; twice G/R covariance -0.0133921615734788.
All three component energies and all three mixed terms are retained. The
remainder is substantial. Coverage of denominators is not a percentage of RH.

An exact short-source bilinear formula for R retains c(r)c(s), the fractional
frequency mask, and every centering constant. It is an execution target,
not an additional bound.

Both final reconstructions and both twelve-method suites pass normally and
optimized. Default Y=15,31 covers 1,232 observation cells counting overlap;
2,455 reconstructed-coefficient comparisons counting overlap; largest native
endpoint 1,023. Exact Fraction/integer arithmetic and 144-bit outward real
intervals; whole prime-power component rational; near mixed component directly
evaluated on small panels and obtained by exact complement on larger panels.
The report labels that distinction. One actual corrupted-report CLI refusal
per suite; additional mutations are in-process controls.

Canonical report SHA256:
`3b6fd0d9a16d91881c56bcf771a0f60ac52a40ce92b877791529b6589c13bc08`.

Fresh extracted-packet and add-only fixture replays pass. No full checkout
validator, previous large campaign, Lean, remote CI, external mathematical
review, all-scale remainder bound or new zero-free region is claimed. Classical
inversion, Ramanujan/Fourier and large-sieve tools are attributed; external
novelty of the specific composition is unestablished.
