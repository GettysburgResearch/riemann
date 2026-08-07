# Full-problem breakthrough — field-separated pole pinning

Author: `gpt56-pro-09-n`  
Date: 2026-08-07  
Branch: `agent/gpt56-pro-09-n/202-haar-renormalization`  
Status: **PROPOSED; RH remains unproved and undisproved**

## 1. Problem exposed by the audit

The branch had two incompatible filter classes:

1. positive mixtures of `r`-adic defects, with a robust multiplicity-descent
   proof but half-knot debt at least `1/4`;
2. endpoint Fejer filters, with optimal `O(N^-2)` debt but no positive
   multiplicity maximum principle.

`R-20202` also refuted a signed terminal-flat shortcut that appeared to combine
their advantages only because its RH sign was reversed.

## 2. Resolution of the exposure conflict

Let `P_0>=0` have algebraic coefficients in a number field `K`. Choose one exact
positive `eta notin K` and put

```text
P_eta=P_0+eta(1-cos x).
```

At any off-line zero of multiplicity `m`, the filtered logarithmic-derivative
residue is

```text
m eta + A,
A in K.
```

It cannot vanish. Therefore the filter is RH-complete through the same
Landau/pole argument even when its remaining coefficients have arbitrary signs.

For the endpoint family, take

```text
K_N=Q(zeta_(4(N+1))),
eta=2^-B sqrt(p),
p=1 mod 4,
p does not divide 4(N+1).
```

Then `sqrt(p) notin K_N` by conductor inclusion. This is exact algebraic field
separation; transcendence is unnecessary.

## 3. Conditioning retained

The pinned half-knot ratio is

```text
[(N+1) sin^2(pi/[2(N+1)]) + eta/2]
/
[N+1+eta].
```

With `eta<=2^-3N`, this remains

```text
pi^2/(4N^2)+O(N^-3).
```

At the critical mesh `t=2log(n)/N`:

```text
algebraic endpoint support  q<=n^2
pin-only support            q<=n^(2/N).
```

Thus the analytic exposure mechanism costs only a tiny oldest-prime-prefix
correction.

## 4. Exact artifacts

- `T-20206`: transcendental special case;
- `T-20207`: exact quadratic-field pin;
- `L-20213`: prime-prefix localization;
- `L-20214`: generic number-field statement;
- `M-20204`: fixed-degree production protocol;
- `X-20204`: symbolic residue/ramp/support checker with eight mutation tests.

The exact checker treats the pin as an independent symbol and does not replace
the field-theoretic or Landau proofs.

## 5. Reconnaissance

An ordinary complete-prime-power scan tested degrees `N=2,...,12` and all
critical levels `n=2,...,3162`, using every prime power through `n^2<=10^7`.
All 34,771 values were positive.

This is scheduling evidence only: binary64 prime prefix accumulation and
nondirected special-function arithmetic were used.

## 6. Remaining theorem

Choose one sufficiently large **fixed** degree and exact pin. Prove either

```text
E_N(2log(n)/N)>=0 eventually
```

or

```text
(-E_N(2log(n)/N))_+=n^o(1).
```

The preferred arithmetic mechanisms are:

1. centered terminal-prime/pole transport;
2. Selberg log-convolution square;
3. prime-polygon convex dual margin;
4. real-axis Stieltjes continued fraction.

The filter may now be optimized in the full algebraic Fejer cone; pole exposure
no longer constrains it to positive `r`-adic mixtures.
