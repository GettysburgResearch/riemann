## Purpose

Stack on PR #642 at exact head
`07aa0d4838458a1b2d3af9e5bc96616baa6b4767`, reconstruct its remaining source
interfaces, and move the conclusion to one scalar factor-67 Harnack state.

**RH remains unproved.**

## Single idea: scalarize before composing

PR #642 proves

```text
Q_Y(j) = integral T(Y/t) kappa_j(t) dt/t,
kappa_j(t)>0,
```

and hence `c_X(j)=integral Psi(X/t) kappa_j(t) dt/t`.

Instead of carrying every row through the global common-parent tree, define

```text
H67(x)=Psi(x)-Psi(x/67)/sqrt(67).
```

Global `H67>=0` implies RH directly from

```text
Mellin(H67)(s)
 = (1-67^(-(s+1/2)))(s+3/2)
   / [s(s-1/2) zeta(s+1/2)].
```

The 67 factor cannot cancel a zero with real part greater than `1/2`.

## Exact source repair

A smaller endpoint is not a raw cutoff of the SHARP kernel measure. The exact
one-parent child map is

```text
R_(Z|Y)(t)=1_(t<=Z) T(Z/t)/T(Y/t).
```

This ratio lies in `[0,1]`. It simultaneously proves normalized-profile
monotonicity, positive Hall edge sources, and disjoint random-key child
ownership. The raw-cutoff counterexample `Y=16,Z=4,t=4` is retained.

## Exact finite result

The defect has local 67-adic coefficients `(1,-2,1)`. A segmented `2^50`
producer proves

```text
H67(x)>0 for every real 1<=x<100,000,001.
```

The directed minimum occurs at `x=201^-`:

```text
1626923303441334483980962730376 / 2^100
 <= min H67 <=
1626923303449543135335825015140 / 2^100.
```

The lower endpoint is greater than `1.28341618987788997`.

## Exact remaining line

```text
H67(x)>=0 for every x>=100000001    OPEN / RH-BEARING
Riemann Hypothesis                  UNPROVED
```

## Removed conclusion interfaces

```text
score and all-column capacity;
second-order Volterra anchors and knot ledger;
finite/continuum equality frame;
global vector-valued common-parent composition;
row-specific large-j noncancellation;
terminal and prime-square ports.
```

## Replay

```bash
cd experiments/X-99250-sharp-harnack
python3 verify.py
./replay.sh --full
```
