# Variable-geometry principal contour for Hu's unitary probe

**Status:** Proposed source-conditional principal-row theorem, not a zero-free theorem. The proof below reconstructs the two scalar residue shifts, rather than importing Xu–Sang's finite-order principal theorem wholesale. Hu's physical identity and local factors remain explicit inputs and have not been independently proved here.

**Source inputs:** Hu, [unitary Weil preprint](https://hexagonmath.org/2610.00216v1), (6.2), (6.5), (6.9), (6.11)–(6.16); the independently checked [principal-tube bounds](../2026-10-28-hu-principal-region/README.md); standard Hecke continuation, functional equation and fixed-field prime-ideal theorem. We assume the source's common Mellin formula and that its `M(z)` is holomorphic on `Re(z)>0` with the vertical strip/trace decay needed for the integrals below, as furnished by the source test-function construction. No source claim stated only for `beta>7/8` is used as an input here.

## Statement

Fix Hu's field `K` containing `mu_12`, a fixed oriented unitary Hecke target `psi`, its finite bad set `S`, and Hu's test functions with `M(1/6)!=0`. Fix `b,ell` and a finite disjoint system of prime windows as in [the variable-low note](../2026-10-28-hu-variable-low/README.md), with `l_x=(1-b-ell)/2`, `l_y=(1+b-ell)/2`, `h=1-l_x+ell`, and `l_y,h>0`. Let `beta` be any real upper bound for the real parts of all zeros of the particular `L_K(s,psi)`, with `87/100<beta<=7/8`, and choose a fixed `e>0` so small that `beta+e<1`, `1/6+e` is inside the common Mellin domain, and both `l_y/20-(1+h)e` and `h/600-e` are positive.

Let `P_psi(Z)` denote `(-1)^J` times the **principal row of Hu's same finite compensated probe** (6.9), where `J` is the number of slots, now with `X=Z^l_x`, `Y=Z^l_y` and slot lengths summing to `ell`. Write `A(Z)=Z^(-ell/6) product_i S_i(Z)`, where `S_i(Z)=sum_p W_i(Np/P_i)(Np)^(-5/6)`, and let `c_psi!=0` be Hu's scalar product of the two zeta residues and the two test values. With `C_b(s)=s-(4+b)/6` and `H_psi^S(s)=H_(1,psi)(s,1,1/6)`, define

    f_psi(Z) = (1/2pi i) integral_(Re s=2)
                  Z^C_b(s) exp((s-5/6)^2) H_psi^S(s)/L_K^S(s,psi) ds.

For every fixed `0<mu<(87/100) min_i ell_i` and `epsilon>0`,

    P_psi(Z)/(c_psi A(Z)) - f_psi(Z)
       <<_(psi,e,epsilon) Z^(C_b(beta)+(1+h)e-l_y/20+epsilon)
        + Z^(C_b(beta)+e-h/600+epsilon)
        + Z^(C_b(beta)+e-mu+epsilon).

The implicit constant can depend on the fixed target and slot system; the three displayed margins do not depend on the later finite-order target twist. This is a principal-row result only.

## Reciprocal and Mellin bounds

On every fixed line `Re(s)=beta+e`, `1/L_K^S(s,psi)` has at most polynomial growth in the height, with a finite degree allowed to depend on `psi,e`. One direct proof is as follows. If `L_K(s,psi)` is a norm-character zeta shift with pole `s0`, put `F(s)=(s-s0)L_K(s,psi)`; otherwise put `F=L_K(s,psi)`. In either case `F` is entire and zero-free in `Re(s)>beta`. In a fixed-width vertical strip, standard Hecke functional-equation bounds give `|F(s)| << (1+|Im(s)|)^A`, and the Euler product gives `|F(3+it)| >> 1`. For each height `t`, choose a holomorphic logarithm on a rectangle `beta+e/2<Re(s)<4`, `|Im(s)-t|<2`. A positive harmonic majorant for `Re(log F)` and a fixed Harnack chain from `3+it` to `beta+e+it` give `|F(beta+e+it)|^(-1) << (1+|t|)^(A_e)`. Restoring `s-s0` and deleting the fixed finite `S` Euler factors cost at most another polynomial: the deleted factors are bounded away from zero on `Re(s)>=beta+e>0`. This argument applies separately to each fixed target and does not claim uniformity in its finite conductor.

The fixed-field zeta function has polynomial vertical growth on each bounded real strip away from its pole. The Gaussian `exp((s+z-1)^2)`, the source Mellin decay for `M(z)` and the compactly supported window transform `W1hat(w)` absorb every fixed polynomial height factor. The same estimates justify the large-height joins in the following shifts. Their exact strip and trace form is an input from Hu's test construction, retained explicitly in the header.

## Local correction and slot normalization

By the principal case of the linked tube bound, the full unselected product `H_(1,psi)(s,w,z)` is absolutely and uniformly convergent after one fixed prime cutoff on `Re(s)>=87/100`, `Re(w)>=19/20`, `Re(z)>=33/200`; each selected local factor `G_p/H_p` is uniformly bounded there. Therefore the principal selected correction is holomorphic in that tube and has the all-height bound

    H_(1,psi,Z)(s,w,z) << Z^(ell Re(z)),

with a constant depending on the fixed slot count and windows. This is obtained by factoring the same full `H_(1,psi)` from every selected tuple and applying the fixed-field ideal count to each disjoint window.

At `w=1,z=1/6`, Hu (6.16) gives `G_p/H_p=-1+O((Np)^(-87/100))` uniformly on `Re(s)=beta+e`. Hence, with the overall `(-1)^J` absorbed in the source normalization,

    H_(1,psi,Z)(s,1,1/6)
       = H_psi^S(s) Z^(ell/6) A(Z) [1+O(Z^(-mu))].

The nonnegative windows make the relative error bounded by a sum of their individual cutoff errors. The fixed-field prime-ideal theorem gives each `S_i(Z)` a positive main term of order `P_i^(1/6)/log P_i`; thus `A(Z)^(-1) <<_epsilon Z^epsilon`. These assertions use the **same** slot system as the physical probe.

## Two residues and the variable exponents

For the principal row, (6.5) has scalar factor `zeta_K^S(6z) zeta_K^S(w)/L_K^S(s,psi)` times the selected correction above. Move from the absolute contours to `Re(s)=beta+e`, `Re(w)=1+e`, `Re(z)=1/6+e`, keeping the reciprocal on a zero-free global `s`-line. Then move `w` to `19/20`, crossing only its zeta pole at 1. In that residue move `z` to `33/200=1/6-1/600`, crossing only the pole of `zeta_K^S(6z)` at `1/6`. The reciprocal remains on `Re(s)=beta+e`; a possible norm-character pole of `L(s,psi)` gives a zero of its reciprocal, not an extra pole. The correction has no pole on this tube, and `M(z)` is holomorphic for positive real part. All height joins are justified by the preceding polynomial and trace bounds.

After factoring `A(Z)` and using the selected-correction majorant, the real outside exponent is

    l_x/2 + Re(s)-1 + h Re(z) + l_y(Re(w)-1).

At the double residue this is `C_b(Re(s))`; the scalar residues are precisely `c_psi!=0`. The unresidued `w` integral has exponent `C_b(beta)+(1+h)e-l_y/20`, while the remaining `z` integral after the `w` residue has exponent `C_b(beta)+e-h/600`. The local slot approximation supplies the error with exponent `C_b(beta)+e-mu`. Finally, move the main double-residue integral from `Re(s)=beta+e` to `Re(s)=2`; `H_psi^S(s)` is holomorphic there by Hu Lemma 6.1, the reciprocal is holomorphic throughout `Re(s)>beta`, and the Gaussian controls the joins. This gives `f_psi(Z)` and the stated estimate.

## Remaining boundary

This establishes neither the nonprincipal-row detector nor an averaged numerator estimate. To infer a zero-free region, one still needs a single target-uniform positive power saving for **all** nonprincipal rows in this same variable-geometry probe, the source's common-height and slot-mesh order, the low-side estimate, and the Mellin continuation argument. The present proof assumes, rather than reproves, Hu's finite-place identities, Mellin trace estimates and prime-window calibration.
