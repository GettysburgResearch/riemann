# Review specification — corrected T-106150 Wick half-source square

Review in this order:

1. Verify `L-106133` in the Boolean algebra:
   \[
   b_U=f_U\star f_U,
   \qquad
   \mathfrak B_U^{\rm eq}
   =\int_0^1(1-\theta)
      \mathfrak G_{U,\theta}^{\star2}d\theta.
   \]
2. Reconstruct the canonical pair coefficient
   \[
   2\int_0^1(1-\theta)\theta^{k-2}d\theta
   =\binom{k}{2}^{-1}.
   \]
3. Read `R-106150` before using any scalar self-convolution. Test the
   one-label fixture
   \[
   x_p\star x_p=0,
   \qquad x_p^2\ne0.
   \]
4. Derive the exact Wick--Mellin field `J_U^diamond` by imposing disjoint
   prime-label supports.
5. Verify
   \[
   J_U=J_U^\diamond+C_U
   \]
   and classify every contraction label as owner/owner, owner/core, or
   core/core, with exponent `2`, `3`, or `4`.
6. Check that the parent `T-102990` closed ledger genuinely applies to the
   fixed differential observation of those contraction fields.
7. Verify
   \[
   \Phi_*=2(D-1/2)A*_MA
   \]
   and
   \[
   \mathcal O_{\Phi_*}[B_U^{eq}]
   =(2D-1)J_U^\diamond.
   \]
8. Confirm the factor `2D-1`. Do not use the false product-rule formula
   `D(f*g)=Df*g+f*Dg` for convolution.
9. Reconstruct the derivative/outer multiplier
   \[
   \frac12D(D-1)(5D+3/2)(2D-1).
   \]
10. Verify that the reflection signature belongs to the **ordinary**
    convolution and enters the live source only modulo the closed contraction
    field.
11. For characters, verify the normal-ordered analytic square
    \[
    \int(1-\theta):\!\widehat F_\chi^2\!:_B d\theta.
    \]
12. Decide whether any existing theorem proves `WKSFSC106150`,
    `SFSC106150`, `REFEV106150`, or `REFOD106150`.

Mandatory firewalls:

```text
Do not identify Boolean star with ordinary source multiplication.
Do not omit shared-label contractions.
Do not call the Wick square an autocorrelation or modulus square.
Do not infer physical near-collision control from the source diagonal.
Do not take conductor-fibre absolute values before connected/Wick centering.
Do not claim the exact replay proves a one-sided estimate or RH.
```

Current status:

```text
Boolean/Beta equal-pair source square       exact;
ordinary = Wick + contractions              exact;
contractions                                inherited closed after observation;
common-mother Wick differential image       exact;
reflection model modulo contractions        exact sufficient coordinate;
WKSFSC / SFSC / REFEV / REFOD               open;
BCI102990 / RH                              open.
```
