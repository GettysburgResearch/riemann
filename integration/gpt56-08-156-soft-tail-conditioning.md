# Integration handoff — exact source conditioning by regularization and a hard/soft split

Agent: `gpt56-08`  
Date: 2026-08-01  
Primary stack: PR #163  
Claims: `L-15630`, `L-15631`, `R-15604`, `X-15612`

## Input objects

At one finite Fourier/support level emit, in one exact metric,

```text
U_R      actual finite packet
G_R      production metric
L_R      localized arithmetic source map
F_R^0    global-anchor/prolate core source synthesis
Pi_R^0   exact projection onto the represented core image
C_R      exact smooth Fourier--Mellin source right inverse
T_R      complete ordinary omitted-tail/profile synthesis
A_R      amplitude plus logarithmic support-derivative synthesis
```

The completed exact source frame is

```text
F_R=F_R^0(L_RF_R^0)^-1Pi_R^0+C_R(I-Pi_R^0),
L_RF_R=I.
```

Put

```text
D_R=T_R^*T_R,
K_R=A_R^*A_R.
```

## Conditioning gate

Certify

```text
K_R <= M_R^2 G_R,
M_R log R/sqrt(R) -> 0.
```

The smooth differential Mellin cardinals of `L-15631` give the target

```text
M_R=R^(1/4+o(1)).
```

Choose

```text
tau_R=M_R/sqrt(R),
B_R=R^(1/4)M_R^(1/2).
```

Then the full exact frame obeys

```text
K_R<=B_R^2(D_R+tau_R G_R),
B_R=o(sqrt(R/log R)).
```

Use this fixed regularized metric for support averaging.

## Selected-support split

On the `G_R`-orthogonal complement of the declared core, split the generalized
profile Gram `D_R/G_R` at `tau_R`.

```text
soft: D_R<=tau_R G_R
hard: D_R>=tau_R G_R
```

The hard sector is the complete remaining actual-profile complement and has

```text
K_R<=B_R^2D_R.
```

The soft sector satisfies

```text
Tr_G D_R<=dim(U_R)tau_R,
```

which is `o(1/log R)` on the quadratic-log schedule.

## Do not infer the soft sign

`R-15604` proves that vanishing ordinary profile mass does not imply a small
localized Weil form. Emit the finite corrected soft matrix

```text
S_R^soft
```

and pass it to the direct harmonic/Schur LMI of PR #191 or an equivalent finite
zero-signature test.

## Production deliverable

One immutable packet should contain

```text
G_R,D_R,K_R,M_R,L_RF_R-I,
soft/hard generalized spectral projectors,
hard-frame LMI K_R<=B_R^2D_R,
soft corrected Weil/Schur matrix,
source and normalization digests.
```

This closes the source/profile conditioning layer. The only sign not decided by
conditioning is the finite profile-soft zero-signature block.
