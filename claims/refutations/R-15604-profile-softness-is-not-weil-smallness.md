# R-15604 — Profile softness does not imply Weil-form smallness

Claim ID: `R-15604`  
Title: A vanishing ordinary tail/profile Gram can coexist with a fixed negative localized form  
Status: `EXACT ABSTRACT REFUTATION`  
Authoring agent: `gpt56-08`  
Created: 2026-08-01  
Targets: unqualified soft-tail absorption in the first draft of `L-15630`  
Related counterexample candidates: none

## 1. Exact family

For integers `j>=1`, put

\[
 R_j=16^j,
 \qquad
 M_j=R_j^{1/4}=2^j,
 \qquad
 \tau_j={M_j\over\sqrt{R_j}}=2^{-j}.
 \tag{R-15604.1}
\]

On `H=C^2`, take

\[
 G_j=I_2,
 \qquad
 D_j=\operatorname{diag}(\tau_j^2,1),
 \qquad
 K_j=I_2,
 \tag{R-15604.2}
\]

and the self-adjoint localized form

\[
 A_j=\operatorname{diag}(-1,1).
 \tag{R-15604.3}
\]

Then

\[
 K_j\preceq M_j^2G_j
 \tag{R-15604.4}
\]

and

\[
 {M_j\log R_j\over\sqrt{R_j}}
 =2^{-j}j\log16\longrightarrow0.
 \tag{R-15604.5}
\]

The regularized conditioning theorem therefore applies.

## 2. Soft sector

The first coordinate belongs to the soft spectral sector because

\[
 \tau_j^2\le\tau_j.
 \tag{R-15604.6}
\]

Its ordinary profile mass tends rapidly to zero:

\[
 \langle D_je_1,e_1\rangle
 =\tau_j^2\longrightarrow0,
 \tag{R-15604.7}
\]

and even

\[
 (\log R_j)\langle D_je_1,e_1\rangle
 =j\log16\,4^{-j}\longrightarrow0.
 \tag{R-15604.8}
\]

Nevertheless its localized form is fixed and negative:

\[
 \boxed{
 \langle A_je_1,e_1\rangle=-1
 \quad\text{for every }j.}
 \tag{R-15604.9}
\]

Thus no estimate involving only the ordinary profile Gram `D_j`, its trace, or
the regularized conditioning inequality can promote the soft coordinate into a
near-radical packet.

## 3. Zeta interpretation

The exact Xi-cardinal obstruction has precisely this logical shape. A localized
off-line cardinal direction can have a profile component that escapes every
high-frequency/local-Weyl frame while retaining a fixed negative Weil value at
one nonreal zero coordinate.

The example does not assert that the synthetic matrices arise from the Suzuki
operator. It proves the abstract implication

```text
small ordinary tail/profile mass
    => small localized Weil form
```

is false without a theorem controlling the finite zero/local signature block.

## 4. Corrected consequence

The valid output of `L-15630` is therefore:

1. a complete exact frame with sub-square-root **regularized** conditioning;
2. an actual-profile hard complement with sub-square-root actual conditioning;
3. a finite soft-signature block whose ordinary profile trace tends to zero.

The remaining positive obligation is the explicit finite form estimate

\[
 \left\|
 \left[
 G_{S,j}^{-1/2}\mathscr S_{S,j}G_{S,j}^{-1/2}
 \right]_{-}
 \right\|\to0,
 \tag{R-15604.10}
\]

or another theorem excluding the off-line-cardinal signature on the soft
sector.

## 5. Proof boundary

All identities in the synthetic family are exact. This is a scope refutation,
not a zeta computation and not evidence for or against RH.
