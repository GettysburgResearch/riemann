## T-105320 continuation — exact first-chaos cancellation

The direct T-105310 Cauchy-model comparison has a binding arithmetic defect:
after the natural low-order normalization, the degree-one von Mangoldt packet
has asymptotic energy `1/2` on each one-sided safe-line source. It cannot be a
one-percent perturbation of the archimedean carrier.

This checkpoint repairs that defect by a source-fixed, zero-free Wick
congruence. If

```text
A_X(s)=sum_(n<=X) Lambda(n)n^(-s),
W_(L,X)(s)=exp[-A_X(s)/(2L)],
```

then

```text
L W_(L,X)^2/(L-A_X)
 = exp(-A_X/L)/(1-A_X/L)
 = 1 + sum_(m>=2) c_m (A_X/L)^m.
```

The complete linear prime packet is absent. The reciprocal coefficient family
is also exactly the frozen-parameter derivative of the formal xi-prime
coefficient family:

```text
-log(N) b_L(N) = partial_L C(N;L).
```

Differentiating the pinned xi-prime re-expansion also gives entry-dependent reciprocal error `O((log T)^-1/2)` in H3. Using PNT and unique factorization, the one-sided normalized coefficient
energy tends to

```text
D_W=sum_(m>=2)c_m^2 m!/(2m)! < 7/320.
```

The corresponding two-sided stationary model has effective rank at least
`160/167`. Even one-percent trace/HS transfer leaves `0.920515...`, which would
imply `0.676831...` of zeta zeros on the line, counted with multiplicity, after
the T-105310 nuisance ledger.

```text
coefficient derivative bridge             PROVED EXACT
entry-dependent reciprocal freezing       PROVED IN H1/H2/H3 NORMS
zero-free first-chaos Wick cancellation    PROVED EXACT
one-sided Wick energy < 7/320              PROVED FROM PNT
two-sided model effective rank >160/167    PROVED
raw one-percent model comparison            REFUTED
WXFER105320 actual-Xi transfer              OPEN / RECORD-BEARING
new zero proportion / RH                    UNPROVED
```
