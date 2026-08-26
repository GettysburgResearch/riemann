# Review specification — corrected T-106150 Wick square and reflection gate

Review in this order:

1. Verify the Boolean half-source and canonical pair identity in `L-106133`.
2. Read `R-106150` and test `x_p star x_p=0` versus `x_p^2!=0`.
3. Derive the exact Wick--Mellin field `J_U^diamond` by imposing disjoint
   source supports.
4. Verify `J_U=J_U^diamond+C_U` and classify every contraction as
   owner/owner, owner/core, or core/core, with prime exponent `2`, `3`, or `4`.
5. Verify that parent `T-102990` closes the fixed differential observation of
   those contraction fields.
6. Check
   \[
   \mathcal O_{\Phi_*}[B_U^{eq}]=(2D-1)J_U^\diamond
   \]
   and the complete `D_out` multiplier. Do not use a product rule for
   convolution.
7. Verify `L-106135`:
   \[
   E_U+O_U=N_U,
   \quad
   J_U=E_U-O_U,
   \quad
   D_{out}J_U=2D_{out}E_U=-2D_{out}O_U.
   \]
8. Check the pointwise negative-part equality and the mismatch-energy formula.
9. Verify the normal-ordered analytic character square; do not insert a complex
   conjugate or restore shared-label contractions.
10. Decide whether any existing theorem proves `WKSFSC106150`,
    `SFSC106150`, or the equivalent `REFSIG106150`.

Mandatory firewalls:

```text
Do not identify Boolean star with ordinary multiplication.
Do not omit shared-label contractions.
Do not call the Wick square an autocorrelation or modulus square.
Do not treat reflection-even and reflection-odd energies as independent gates.
Do not infer physical near-collision control from the source diagonal.
Do not take conductor-fibre absolute values before connected/Wick centering.
Do not claim the replays prove an open gate or RH.
```

Current status:

```text
Boolean/Beta equal-pair source square       exact;
ordinary = Wick + contractions              exact;
contractions after observation              inherited closed;
common-mother Wick differential image       exact;
reflection complementarity                  exact;
WKSFSC / SFSC / REFSIG                      open;
BCI102990 / RH                              open.
```
