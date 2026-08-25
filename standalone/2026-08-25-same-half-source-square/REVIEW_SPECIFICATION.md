# Review specification — T-106150 same-half-source square

Review in this order:

1. Verify the Boolean half-source identity `b_U=f_U star f_U` from `L-106132`.
2. In `L-106133`, reconstruct the coefficient of one full labelled support
   `S` and one unordered owner pair `{p,q}`. Check
   \[
   2\int_0^1(1-\theta)\theta^{|S|-2}d\theta
   =\binom{|S|}{2}^{-1}.
   \]
3. Verify that Boolean restriction away from owner labels commutes with the
   half-source and the depth dilation.
4. Check that `(p,a)->p a^2` is injective and that the stated source diagonal
   is subpower. Do not confuse this with the physical near-collision Gram.
5. Reconstruct the kernel identity
   \[
   \Phi_*=2(D-1/2)A*_M A.
   \]
6. Verify the convolution derivative rule
   \[
   D(f*_M g)=(Df)*_Mg=f*_M(Dg)
   \]
   and therefore the factor `2D-1` in `L-106134.7`.
7. Reconstruct the CV, XD, outer and derivative-outer differential images,
   especially
   \[
   \frac12D(D-1)(5D+3/2)(2D-1)\mathcal J_U.
   \]
8. Verify the reflection-signature formula and the elementary conjunction
   inequality in `T-106150.7`.
9. Check that character twisting produces an analytic square with no
   conjugation. Reject any replacement by a positive norm square unless the
   Wick-centered correction `R-106131 / T-106140` is retained.
10. Decide whether `SFSC106150`, `REFEV106150`, or `REFOD106150` follows from an
    existing source-specific variation or half-divisor theorem.

Mandatory firewalls:

```text
Do not replace a convolution square by an autocorrelation square.
Do not use D(f*g)=Df*g+f*Dg; that inserts a false factor two.
Do not declare the source diagonal to control physical near-collisions.
Do not discard owner, core, incidence, marked-67 or carrier labels.
Do not claim the exact replay proves any one-sided estimate or RH.
```

Current status:

```text
equal-pair Beta half-source square             exact;
common-mother differential self-convolution    exact;
reflection signature                           exact;
SFSC / REFEV / REFOD                           open;
BCI102990 / RH                                 open.
```
