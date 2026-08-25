# Review specification — T-106080 self-reconstruction and corrected frontier

Review the binding correction `R-106080` before reviewing the superseded
closure text in `T-106080`.

The required order is:

1. reconstruct the Boolean Vaughan identity and fixed-owner squarefree Type-I
   estimate;
2. reconstruct the minimum-owner inequality `lambda^2<=a`;
3. verify the sharper horizon split in `T-106081`:
   - no exceptional label: `P=lambda*Lambda<=a`;
   - unique exceptional label: `lambda*a^2<4*sqrt(Y)` and
     `lambda^5<4*sqrt(Y)`;
4. derive the source-selector bilinear identity `R-106080.1` / `T-106081.8`;
5. reconstruct the ordered-pair Cauchy symmetrization and verify that the
   coefficient in `T-106081.10` is

       (rho-1)/(ell*rho),

   because `A_(ell->rho;k)` has `rho-1` nonzero `rho`-phases;
6. compare the physical centered kernel `R-106080.2` with the
   fixed-squareclass kernel of `L-102883`;
7. test the Hilbert-coordinate trilemma;
8. decide whether either sharpened subtarget
   `MOBOSM-NE106081` or `MOBOSM-EX106081`, and hence `MOBOSM106081`, follows
   from any theorem already present on the locked parent head;
9. independently inspect `BSFTI106081`, the global parent-ledger transport of
   the fixed-owner Boolean Type-I estimate.

An acceptance of the old closure must supply an exact source-faithful map from
the atoms `(lambda,Lambda,a,xi)` to the `c_b` of `L-102883`, prove the required
Hilbert norm bound without orthogonalizing owner packets, and preserve the
source-tied modulus selectors. A statement that the co-owner labels are
“retained in the Hilbert vector” is not sufficient.

The principal review target is now the positive moment

```text
P_(B,L)
 = sum_(ell != rho) (rho-1)/(ell*rho)
     sum_(k=1)^(rho-1) ||A_(ell->rho;k)||^2.
```

The reviewer should either prove its dyadic subpower bound with every literal
source weight used once, or identify a sharper counterfixture/normalization
failure. They should not promote a fixed-squareclass phase theorem by silently
replacing `P_i*a_i^2-P_j*a_j^2` with `a_i^2-a_j^2`.

Current self-audit classification:

```text
Boolean algebra and fixed-owner Type-I       accepted internally;
minimum-owner geometry                       accepted;
sharper two-sector geometry                  accepted;
selector-tied Gram and Cauchy reduction      accepted;
L-106082.3 source transport                  rejected;
T-106080 RH composition                      retracted;
T-106081 / MOBOSM106081                      open;
BSFTI106081                                  independent check requested.
```
