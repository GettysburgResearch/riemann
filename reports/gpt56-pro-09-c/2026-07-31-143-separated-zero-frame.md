# Separated certified zeros give a dimension-stable Hardy frame

Agent: `gpt56-pro-09-c`  
Date: 2026-07-31  
Issues: #160 and #166  
Draft PR: #168

## Result

The zero-frame conditioning left implicit in `L-14319` is now explicit.
For the reciprocal Hardy weight

```text
W_tau(t)=2 cosh(2 tau t),
```

Fourier evaluation at a real ordinate `gamma` has representer

```text
k_gamma(t)=exp(i gamma t)/W_tau(t).
```

Their full-line Gram is exactly

```text
<k_gamma,k_eta>
 = pi/(4 tau) sech(pi(gamma-eta)/(4 tau)).
```

Thus a `D`-separated finite set has a dimension-independent Riesz lower bound

```text
pi/(4 tau) [1-2 sum_(n>=1) sech(pi D n/(4 tau))].
```

A simple sufficient gap is

```text
D > (4 tau/pi) log 5.
```

This is a closed weighted Ingham inequality for the certified-zero exponentials.
It is also the finite unconditional shadow of the Clark/de Branges kernel
coordinates suggested by the Weil Hilbert-space literature.

## Finite support

Restricting to `[-L,L]` changes each Gram entry by at most

```text
exp(-2 tau L)/tau.
```

For `m` selected zeros,

```text
lambda_min(H_L)
 >= pi/(4 tau)(1-r_(tau,D))
    -m exp(-2 tau L)/tau.
```

Hence the frame remains uniformly conditioned whenever

```text
m_L exp(-2 tau L) -> 0.
```

The logarithmic/near-logarithmic plunge dimensions isolated on PR #163 easily
satisfy this scale for fixed `tau>0`.

## Consequence for the positive path

The number of selected certified zeros may grow without destroying frame
conditioning. Combined with `L-14319`, the remaining visible-block data reduce
to:

```text
principal-angle/visibility threshold delta^2,
corrected zero-representer block floor b,
complete complement floor gamma,
residual lower floor after the positive zero channels are removed.
```

The frame-conditioning term is no longer a cofinal blocker.

## Exact checker

`X-14313` verifies the rational composition

```text
sigma^2=d_lower(1-r_upper)-m epsilon_upper.
```

The synthetic packet certifies `147/100`; six tests and all six checksum rows
pass. Proof-object SHA-256:

```text
389a7322bf34aec23e1035d199b3d421511b31ad0f06296a7cc50f77272ad4e4
```

## Remaining boundary

No production separated-zero frame has been assembled, and no cofinal residual
floor is proved. RH is not claimed.
