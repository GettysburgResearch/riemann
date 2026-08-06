# O-20806 — Shrinking-strip tilted-prime reconnaissance

Claim ID: `O-20806`  
Title: The canonical `P^-2` shifted statistic retains a positive margin at the global record-low prefix through `10^7`  
Status: `EMPIRICAL — HIGH-PRECISION SELECTED PREFIXES; NOT DIRECTED OR COFINAL`  
Authoring agent: `gpt56-03-v`  
Created: 2026-08-07  
Dependencies: `T-20803`; the exact prime-power manifest of `X-20806`  
Scope: numerical calibration of the new shrinking-strip criterion

## 1. Quantities replayed

At a prefix define

\[
 \omega=P^{-2},
 \qquad
 \mathcal P(\omega)
 =\sum_{q\le X}{\Lambda(q)\over q^{1/2+\omega}},
 \tag{O-20806.1}
\]

\[
 \mathcal L={P\over\omega}\log{P\over\mathcal P(\omega)},
 \qquad
 \widetilde M=\mathcal L-A_+^*(P),
 \tag{O-20806.2}
\]

and

\[
 J=Q-\mathcal L,
 \qquad
 \eta={\log^2(X/2)\over8P}.
 \tag{O-20806.3}
\]

`T-20803` proves exactly

\[
 0\le J=M-\widetilde M\le\eta.
 \tag{O-20806.4}
\]

The computations below test normalization and scale only.

## 2. Small prefix where the tolerance is necessary

At the prefix ending in `q=13`, a 60-decimal-place same-formula replay gives

```text
P              4.97188439807019393782867570475
Q              8.97918479208130913224176319291
omega          0.0404536726181638142811396666412
shifted P      4.62294226286679086703444302265
A*(P)          8.94811611597559893249700031087
L              8.94336428483443432741456324695
M              0.0310686761057101997447628820348
J              0.0358205072468748048271999459605
tilde M       -0.00475183114116460508243706392569
eta            0.0880864051971284266798476325859
```

Thus the stronger strict test `tilde M>=0` fails at this harmless positive
prefix, while the RH-equivalent tolerant test

```text
tilde M + eta > 0
```

passes comfortably. This validates the logical role of the deterministic
Hoeffding tolerance.

## 3. Global record-low prefix through `10^7`

`X-20806` found the smallest ordinary Fenchel margin through `10^7` at the
prefix ending in

```text
q=3089, next prime-power knot 3109.
```

An 80-decimal-place replay gives

```text
P
108.66398251759350930756836727932323947004248065147912251551037078326627161839366

Q
676.17838616926309283865606843285236116086699122485844823655284510936130252214515

omega
0.0000846893431266150302112153304405747002367732675174374856607491720039644231481533

shifted P
108.60673351253942793406378814008922930782590971019175362013049336959859136825603

Fenchel minimizer
8.03906375949627172246869983072710245036752162084941001603146905439733658897811

A*(P)
676.15086559590947203383565385778322737816949696894209569438654119743753706127287

L
676.16643247208335696114830833636642496351294095492119915809103184180575945822466

exact margin M
0.0275205733536208048204145750691337826974942559163525421663039119237654608722740

tilt variance defect J
0.0119536971797358775077600964859361973540502699372490784618132675555430639204804

tilted margin tilde M
0.0155668761738849273126544785831975853434439859791034637044906443682223969517936

Hoeffding tolerance eta
0.0620164700643069875665941071430353127006195359710194328168290153090069025100430
```

The canonical shifted statistic therefore remains strictly positive at the
hardest prefix found by the independent physical-cell and Fenchel scans.

The exact cumulant defect is about `43%` of the final reserve here. It is not a
negligible decoration at modest scale, but it is already much smaller than the
universal tolerance.

## 4. Final prefix through `10^7`

At the last retained prime power `q=9,999,991`, an ordinary extended-precision
replay gives

```text
P                    6321.4118493684645728
omega                2.5024869859975238261e-8
shifted P            6321.4096149722227915
L                    89287.04321636091622
tilde M              0.0376359204761200772
exact M              0.03794421051861718
tilt defect J        0.0003082900424971058
Hoeffding eta        0.0047048233294057629
```

The actual tilt defect is now below `3.1e-4`, while the theorem's inexpensive
range-only tolerance is below `4.8e-3`. Both tend to zero on the proved
cofinal scale.

The final calculation uses extended ordinary arithmetic, not outward intervals;
it is retained only to show the scale of the new criterion.

## 5. Interpretation

The computation supports three practical conclusions:

1. the shifted sum is numerically stable when evaluated through
   `-log1p(-(P-mathcal P)/P)` rather than by subtracting two nearly equal
   logarithms;
2. the exact variance defect should be emitted when available, while `eta`
   remains the fail-closed theorem bound;
3. after a short initial range, the stronger strict tilted margin appears
   positive through the whole tested frontier, including the existing global
   record low.

None of these finite facts proves the cofinal inequality in `T-20803`.

## 6. Proof boundary

- Prime-power enumeration is inherited from the exact integer manifest of
  `X-20806`.
- The `q=13` and `q=3089` replays use ordinary arbitrary precision, not directed
  balls.
- The `10^7` endpoint uses extended ordinary arithmetic.
- No claim is made that the strict tilted margin remains positive forever.
- The theorem-level contribution is `T-20803`; this file is only an indicative
  normalization and scale check.