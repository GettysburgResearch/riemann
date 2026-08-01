# Continuation report — exact source completion below the square-root barrier

Agent: `gpt56-08`  
Date: 2026-08-01  
Branch: `agent/gpt56-pro-09-d/156-capacity-saturation`  
Primary claims: `L-15628`, `L-15629`, `T-15605`  
Status: strongest conditional completion pushed; RH not claimed proved

## Executive result

The former missing object was phrased as an exact source/profile frame for the
actual complete dangerous complement with

```text
B_T=o(sqrt(T/log T)).
```

The new construction separates exactness from positivity.

1. The global-anchor/prolate frame remains the **core**. It supplies the
   uniformly positive omitted-tail Gram and the radial/endpoint/alias profile
   theorem.
2. A new zero-avoiding finite Fourier–Mellin inverse repairs only the difference
   between that core and the actual finite complement.
3. The exact inverse costs only

   ```text
   R^(1/4+o(1)),
   ```

   far below the square-root barrier.
4. Therefore an approximation angle

   ```text
   eta_R=O(R^(-1/4-epsilon))
   ```

   is enough to preserve the positive Gram and produce an exact complete frame.

The existing uniform Dunster/prolate error is

```text
R^(-2/3) polylog R,
```

which is already stronger. The remaining issue is not source interpolation or
PSWF accuracy; it is proving that the **actual complete dangerous complement**
has that power-saving angle to the constructed prolate core.

## New finite Fourier source inverse

Let `L=log R` and retain `N=O(L^2)` Fourier modes. Select a support length in
each unit logarithmic interval so that every grid point

```text
2 pi k/L, |k|<=N,
```

stays at least `L^-4` from every zeta-zero ordinate in the relevant height
range. Riemann–von Mangoldt shows that the total excluded length is
`O(L^-2 log L)`.

The standard local zeta product then gives

```text
max_k |zeta(1/2+i 2pi k/L)|^-1
 <= exp(C(log L)^2)=R^o(1),
```

with the same subexponential bound for the logarithmic support derivative.

A box-cardinal Mellin column has exact Kronecker samples on the finite grid. One
extra guard mode has zero target samples and is used to impose the source
integral condition exactly. Therefore

```text
C_L y
 =sum_k y_k/zeta(1/2+i 2pi k/L) * corrected_cardinal_k
```

is an exact source right inverse on the complete finite Fourier space.

After transport from logarithmic to symmetric multiplicative coordinates, its
fixed-order profile cost is

```text
R^(1/4+o(1)).
```

The local product and exact Mellin normalization require independent review.

## Core-plus-correction theorem

Let `F_R^0` be the prolate core and let

```text
Delta_R=exact_complement-localized_image(F_R^0).
```

Define

```text
F_R=F_R^0+C_R Delta_R.
```

Then the localized image of `F_R` is exactly the actual complete complement.
If the core tail Gram lies between `cG` and `CG`, then

```text
complete tail Gram
 >=(sqrt(c)-||C_R|| ||Delta_R||)^2 G.
```

Consequently

```text
R^(1/4+o(1)) ||Delta_R|| ->0
```

preserves the Gram and the sub-square-root profile envelope.

For the selected-real-zero graph kernel of `L-20302`,

```text
||Delta_R|| <= sqrt(epsilon_R)/sigma_R,
```

so the exact scalar gate is

```text
R^(1/4+o(1)) sqrt(epsilon_R)/sigma_R ->0.
```

This is the sharpest current bridge between the old radical packet, the full
line-zero complement frame, and the exact Möbius/Fourier source machinery.

## Composition to the spectral trace

Under the quarter-power angle, `L-15627` produces a cofinal complement
compression floor of order `log R`. `L-15626` then gives

```text
Tr Q(Gamma-A)_+Q
 <=d beta^2/[4(gamma-Gamma)]
 =o(Gamma-t)
```

from the already-established packet-cross rate.

## Exact blocker

The remaining statement is one of the equivalent quantitative forms

```text
||(I-Pi_prol,R)J_R||_(production/profile)
 =O(R^(-1/4-epsilon)),
```

or

```text
R^(1/4+epsilon+o(1)) sqrt(epsilon_R)/sigma_R ->0.
```

Existing PSWF asymptotics prove the needed rate between the declared prolate
columns and their Hermite models. They do not prove that the actual complete
zeta-dangerous complement is captured at that angle.

Under false RH an off-line Xi-cardinal direction can force this angle or the
positive tail Gram to fail. Thus this is a genuine RH-bearing structural gate,
but it is substantially narrower than an arbitrary complete-source right
inverse theorem.

## Review priorities

1. Audit the local zeta-product lower bound in `L-15628`.
2. Audit the box-cardinal Mellin normalization and guard source constraint.
3. Check the `R^(1/4)` logarithmic-to-multiplicative profile transport against
   the endpoint ledger.
4. Identify the exact production metric in which the actual complement/prolate
   angle should be estimated.
5. Attempt the graph specialization using the radical evaluation endpoint and
   the simple-line frame floor from PR #191.
