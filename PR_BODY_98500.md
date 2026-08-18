## Purpose

This is a research-reset successor, not another review of the failed shallow
factor-67 stopping lines. It attacks the exact loss in the latest quantitative
Dickman corridor: the bounded annular remainder was previously paid by absolute
rough mass, which loses the Dickman factor precisely near the critical saddle.

**The Riemann Hypothesis remains unproved.**

## Freeze

```text
cutoff UTC:        2026-08-18T11:14:03Z
base PR #603:      1dac3eeccb5a01183067c00722d92fbcf2df12c5
threshold PR #593: 8ad37970c616141d06572d76bff68eb3c4e8738a
P61 theorem #576:  0f6ea6eae813c1d867ae50744cf5fd57e2720bb7
Type-II PR #590:   223f11259b3e7134f78d6492795e6e94caca8be3
Lorenz PR #591:    5c43060fd11e6a3f5d090ee4c74e4a48ca2eb111
```

## New exact transfer theorem

For an annular base `b`, put

```text
beta(w)=exp(-w/2)b(exp(w)) = a + eta(w).
```

The literal squarefree rough source, normalized by `sqrt(Y)`, is compared with
the convolution exponential of the prime reciprocal measure. The continuum
signed measure is exactly `d rho`, where `rho` is the Dickman function. The
packet proves

```text
F_b(Y,z)/sqrt(Y)
 = a rho(u)
   + eta(Lu)
   + (1/L) integral_0^(Lu) eta(w) rho'(u-w/L) dw
   + E_disc,
```

where `L=log z`, `u=log Y/L`, and

```text
|E_disc|
 <= C_b (1+u)^3
    [Delta_z(u) + sum_(p>=z) p^-2].
```

Here `Delta_z` is the complete prime-harmonic interval discrepancy. This keeps
the signed boundary correction; it does not replace it by the unsigned rough
count.

## Vinogradov--Korobov terminal sector

The classical zero-free-region PNT gives

```text
Delta_z(u)
 <= C exp[-c L^(3/5)(log L)^(-1/5)]
```

uniformly in the upper endpoint. Together with a Dickman lower bound, the
signed transfer proves an effective constant `C0` such that

```text
z >= exp(C0 (log Y)^(5/8)(log log Y)^(3/4))
    => F_b(Y,z)>0
```

for the complete P61 annular base and all sufficiently large `Y`.

This is a genuinely broader terminal sector than the absolute-remainder
corridor in PR #603.

## Exact finite-part diagnostic

The first signed boundary moment of the P_B base is

```text
kappa_B/a_B
 = sum_(p<=B) log(p)/(p-1)
   + EulerGamma + log 4 - 35/8.
```

It is negative for `B=11`, positive already for `B=13`, and positive for
`B=61`. Therefore the P61 first continuum correction is adverse but only of
relative size `O(log u/log z)`; the absolute `1/log z` payment was not sharp.

## Honest frontier

```text
signed Dickman transfer identity             PROVED
prime-measure/discrete-source error theorem  PROVED
VK moving terminal sector                    PROVED
P61 boundary moment                          PROVED EXACT
odd-history parity firewall                  RETAINED
critical low-threshold Type-II/Lorenz core   OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```

## Replay

```bash
python3 experiments/X-98500-signed-dickman/verify.py   --output experiments/X-98500-signed-dickman/results/verification.json
sha256sum -c experiments/X-98500-signed-dickman/SHA256SUMS
sha256sum -c T98500_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T98500_SIGNED_DICKMAN_VK_TRANSFER
```
