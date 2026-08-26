# Review specification — least-discrepancy rough-tail L-family repair

Review PR #751 after the `T-106090` checkpoint.

## Required reconstruction order

1. lock parent PR #719 at
   `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`;
2. verify that `L-102953`, `L-102955`, `L-102957--L-102959` and
   `L-102962--L-102963` have the scopes claimed in `T-106090`;
3. start from a clean common-core pair
   \[
   N=Pg^2c^2,\quad M=Qg^2d^2,\quad c,d>1,\quad(c,d)=1;
   \]
4. prove uniqueness of the orientation by
   \(\min(P^-(c),P^-(d))\);
5. verify that the selected prime divides exactly one physical product and
   that the opposite reduced core is strictly rough;
6. reconstruct the nonzero Ramanujan identity;
7. derive the exact local Gauss transform and the even-character energy
   identity;
8. verify the fixed-fibre coefficient normalization
   \(z_d=\delta_d/(g d\sqrt Q)v_d\);
9. use \(P^-(d)>\ell\) to check the uniform long-core bound;
10. reconstruct the Mellin amplitudes with fixed \(g,\ell,Q,\sigma\);
11. verify that the anchor sum is formed inside
    \(Z_{g,\ell,Q,\sigma,h}\) before squaring;
12. derive the exact amplified Gauss identity;
13. verify the natural weight \(g^2\ell Q\) and the dual summability
    \(\sum(g^2\ell Q)^{-1}=Y^{o(1)}\);
14. reconstruct the same-anchor diagonal payment in `L-106094`;
15. identify every remaining distinct-anchor cross term;
16. verify the coherence counterfixture `R-106090`;
17. inspect the direct target `LDART106090` and the two distinct-anchor
    moments `LDRPCX106090`, `LDRNEX106090`;
18. do not invoke the fixed Mellin consumer until `BCI102990` has genuinely
    been closed.

## Mandatory firewalls

A proposed proof fails if it:

```text
uses one fixed-fibre estimate and sums anchors absolutely;
drops the anchor-dependent coprimality mask;
counts the same opposite rough tail once for every anchor before forming Z;
omits the fixed g or Q indices while claiming the source-dual weight;
uses the nonprincipal family moment to infer the principal member for free;
reintroduces the minimum-owner star/cycle current after the equal-pair bypass;
claims the finite replay proves the distinct-anchor moment, BCI102990 or RH.
```

## Current classification

```text
L-106090 least-discrepancy normal form       accepted internally;
L-106091 exact even-character family         accepted internally;
L-106092 fixed-fibre long-core bound         accepted internally;
L-106093 amplified Mellin--Gauss form        accepted internally;
L-106094 same-anchor diagonal                accepted internally;
R-106090 coherence firewall                  accepted internally;
LDART106090                                  open;
LDRPCX106090 / LDRNEX106090                  open sufficient conjunction;
BCI102990                                    open;
RH                                           unproved.
```
