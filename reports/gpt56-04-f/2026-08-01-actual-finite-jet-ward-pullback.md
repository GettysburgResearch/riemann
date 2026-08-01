# Actual Riemann finite-jet audit and nonlinear Ward repair

## Objective

Attack the manuscript's actual central finite-jet theorem, first by attempting to prove that the jet range is a two-sided seam radical and scalar-probe invisible, and then—if that route fails—by constructing the missing nonlinear Ward pullback.

## Actual-definition verdict

The clean radical route does not follow from the manuscript's contour definitions.

The central finite-jet subtraction is realized through the finite contour coordinate, seam transpose, comparison trace, LCI map, and projection into `mathcal K_R`. The manuscript's Section 4 cancellation theorem kills only the regular area-type boundary form. It explicitly retains the singular boundary trace on the zero-area seam, and the finite-window weights are carried by the corresponding singular boundary distributions.

Therefore regular-trace cancellation is not a theorem that the jet range is orthogonal for the signed seam involution. The actual operator correction contains three channels:

```text
D = R_raw* S C + C* S R_raw - C* S C.
```

The clean route would have to prove all three vanish, plus annihilation by the fixed scalar probe. Those statements are absent and are not consequences of the displayed boundary cancellation.

## Constructive repair

For the actual finite raw and renormalized comparison operators

```text
A = R_raw* S R_raw,
K = (R_raw-C)* S (R_raw-C),
D = A-K,
```

define the relative determinant Ward functional

```text
W(w) = d/dw log[det_2(I+iwA)/det_2(I+iwK)].
```

Its order-`ell` coefficient is exactly

```text
q_rel(ell)=Tr(A^ell)-Tr(K^ell)=-P_ell(A,D),
```

where `P_ell` is the complete nonempty contact polynomial.

Let

```text
delta_raw(ell)=raw_one_contour(ell)-Tr(A^ell).
```

The complete nonlinear Ward counterterm is

```text
q_Ward(ell)=delta_raw(ell)+q_rel(ell)
           =delta_raw(ell)-P_ell(A,D).
```

Then the Ward-renormalized scalar coefficient satisfies identically

```text
raw_one_contour(ell)-q_Ward(ell)=Tr(K^ell)
```

for every order and every finite window/readout.

At order four,

```text
q_Ward(4)=delta_raw(4)
 +4 Tr(A^3D)-4 Tr(A^2D^2)-2 Tr(ADAD)
 +4 Tr(AD^3)-Tr(D^4).
```

## Majorant

If both raw and renormalized finite operators have Hilbert--Schmidt norm at most `C`, then

```text
|q_rel(ell)| <= 2 C^ell,
sum_(ell>=2) |q_rel(ell)| r^(ell-1)
 <= 2 C^2 r/(1-Cr).
```

Including a raw diagonal defect with the same two-sided coefficient bound gives `4 C^2 r/(1-Cr)`. No new limit theorem is needed.

## Exact control

`X-15117` checks a genuinely noncommuting rational example through order eight. Eleven adversarial tests pass. The certificate digest is

```text
41de875cdbc6f4d1c61430a66a4d3c870a7f2d4c401625a53f2eafc1cfc4b628
```

## Honest boundary

This repairs the finite algebra by a canonical nonlinear counterterm. It does not prove that the manuscript's existing linear finite-jet scalar coefficient already equals the Ward counterterm. Nor does it prove that the Ward-amended classical ledger still converges to `xi'/xi`.

The remaining target-preservation theorem is therefore exact:

```text
q_linear(ell,M)=q_Ward(ell,M,N)
```

for every order/readout, or an independent Guinand--Weil replay for the amended ledger. A discrepancy beginning at order four cannot be absorbed into the two central exponential constants.
