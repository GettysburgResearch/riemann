## Purpose

Continue PR #664 and attack its ratio-67 Möbius-window frontier by an independent native-source renormalization.

**RH remains unproved.**

## New global theorem

With

```text
beta(n)=mu(n)-1_(67|n)mu(n/67),
S(y)=4(sqrt(y)-1)_+,
G_m(X)=sum_n beta(n)n^(-1/2)S(X/n)^m,
```

this packet proves

```text
G_m(X)>0 for every real X>1 and every real m>=2.
```

The proof uses the literal labelled Euler source, including two labelled copies of `67`, and a strict exponent-`3/2` prime-label mass below one.

## Euler–Taylor renormalization

An exact positive Taylor-remainder cone removes every Euler layer whose effective prime exponent is greater than one. The process stops exactly at the prime-harmonic boundary.

For every integer `m>=2`, the last remainder is

```text
C_m(X)=sum_n beta(n)n^(-1/2)K_m(X/n),
```

where `K_m>=0` is explicit and has a rational Mellin multiplier with no zeros. After the exact compact correction, its Mellin transform is analytic at every positive real point and retains every translated off-line zeta pole.

Hence subpower logarithmic negative mass of `C_m` implies RH.

## Minimal member

For `m=2`,

```text
C_2(X)
 = 16(1-67^(-3/2))/zeta(3/2) * X
   - G_2(X).
```

The native quadratic scalar `G_2` is globally nonnegative. The sole remaining theorem is its sharp upper envelope, or merely subpower logarithmic mass of the excess.

## Firewall

Positivity of all `m>=2` powers does not imply the last critical sign. Exact pole-lowering gives positive B-spline convolutions down to the quadratic level; the final step is a positive smoothing of the unknown critical linear source. A nonnegative primitive can have a negative final window.

## Replay

```bash
cd experiments/X-99930-critical-taylor
./replay.sh
```

Expected verdict:

```text
PASS_T99930_CRITICAL_TAYLOR_RENORMALIZATION
```

## Boundary

```text
activation-zero powers m>=2                  PROVED GLOBALLY
subcritical Taylor/Euler remainders           PROVED POSITIVE
all absolutely convergent layers              REMOVED EXACTLY
critical kernel and Mellin consumer            PROVED EXACT
critical envelope / negative-mass theorem      OPEN / RH-BEARING
Riemann Hypothesis                             UNPROVED
```
