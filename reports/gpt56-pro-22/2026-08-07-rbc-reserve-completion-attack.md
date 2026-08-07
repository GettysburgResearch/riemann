# RBC reserve-completion attack

Date: 2026-08-07  
Agent: `gpt56-pro-22`  
Issue: #256  
Frozen parent: PR #250 head `f179ab93e7e0dc748e0e9fb9e5a6800b80b6d224`

## Objective

The parent proposal deliberately left two arithmetic obligations open:

```text
actual top-corner reflected Schur reserve;
actual bounded simultaneous boundary charge.
```

This pass attempted to prove both.  It incorporated the two-frequency physical
block correction of PR #241 and tested five possible closure mechanisms:

1. aggregate reflected positivity;
2. an exact finite matrix depth lift;
3. far-right residual contraction;
4. a different finite-resolvent parametrization;
5. cyclic root-of-unity polarization.

## Result in one paragraph

The source-map problem and finite-depth bookkeeping can be closed exactly.  A
nilpotent matrix inverse reconstructs the complete `-zeta'/zeta` source through
the endpoint and retains every two-frequency reflected cross term.  All
reciprocal-free depth differences form a finite ledger, while the nontrivial
meromorphic quotient has rank one per side.  However, the aggregate reflected
Gram has zero Schur reserve, absolute contraction on a far-right line is exactly
critical after deweighting, and a resolvent that kills the terminal pole moves
the same pole into its base row.  The rank-one surviving charge is a **full-scale
fixed-ratio Mertens shell**, not one `V=X^(1/K)` coordinate.  Its subexponential
block energy is precisely the RH-bearing theorem.

## 1. Exact reserve obstruction

For packet fields `q_1,...,q_m` in the physical block Hilbert space, the exact
two-frequency identity controls

\[
\left\|\sum_rq_r\right\|^2.
\]

Its packet Gram is the all-ones block matrix.  It has kernel

\[
\sum_rq_r=0,
\]

and the two-block Schur complement is exactly zero.  Therefore reflection
creates the correct Hermitian orientation but no strict packet reserve.

This is recorded in `R-25601`.

## 2. Exact matrix depth lift

Let

\[
R=1-\zeta M_V,
\]

and let `S_K` be the nilpotent forward depth shift.  The matrices

\[
\mathbf A=M_V^{-1}(I-RS_K),
\qquad
\mathbf B=M_V\sum_{j<K}R^jS_K^j
\]

satisfy

\[
\mathbf A\mathbf B=I.
\]

Their logarithmic derivative is

\[
-\mathbf A'\mathbf A^{-1}
={M_V'\over M_V}I
+\sum_{j=1}^{K-1}R'R^{j-1}S_K^j.
\]

For the declared forward shift, the last-row anchor and the all-column vector
synthesize `-zeta'/zeta` coefficientwise through `X`.  Tensoring two independent
frequencies gives the exact physical reflected source map of `L-9518` and all
depth cross terms.

This closes a real gap in earlier packetwise uses of the scalar Selberg identity.
It is `L-25601`.

## 3. Far-right contraction is neutral

On the weighted space with `sigma=alpha+1/2>1`, the residual convolution has
absolute norm

\[
\sum_n{|r_V(n)|\over n^\sigma}
\ll_\sigma V^{1-\sigma}\log V.
\]

At depth `K` this appears strongly contracting.  But recovering the physical
block costs `X^alpha`, and

\[
X^{1-\sigma}X^{\sigma-1/2}=X^{1/2}.
\]

The vertical line cancels out.  This method gives only the unsigned
square-root barrier.  It is formalized in `R-25602`.

## 4. Meromorphic charge cannot be deleted

Every finite resolvent satisfies

\[
{1\over\zeta}
=M\sum_{j<K}R^j+{R^K\over\zeta},
\qquad
1-R=\zeta M.
\]

If `M` is holomorphic at a zeta zero, the terminal residual has the complete
principal part of `1/zeta`.  If `R` vanishes there strongly enough to kill the
terminal residual, then `M=(1-R)/zeta` has the full pole instead.

Thus finite inverse design can move the charge but not remove it.  A
complete-tail control demonstrating the second alternative is included in
`L-25602`.

## 5. Rank-one charge versus full logarithmic scale

Modulo functions holomorphic at every nontrivial zero, all finite inverse
residuals have one quotient class.  The reflected quotient therefore has
analytic rank one.  Every fixed-ratio shell

\[
Q_c(t)=e^{-t/2}[M(e^t)-M(ce^t)]
\]

represents that class, and the causal filters of `L-23008` identify all fixed
ratios.

But the anchor occupies

\[
ce^J<n\le e^J,
\]

which is a full `X`-scale shell.  Rank one is not a `1/K` exponent.  This exact
scope correction is `L-25603`.

## 6. Cyclic phase lift

Root-of-unity colors

\[
A_\omega=M_V^{-1}(1-\omega R)
\]

produce an exact positive finite depth frame.  Fourier orthogonality gives

\[
\sum_{\omega^K=1}
\left\|\sum_j\omega^jf_j\right\|^2
=K\sum_j\|f_j\|^2.
\]

Each color has its own two-frequency reflected Selberg identity.  This closes
the abstract depth-kernel issue and diagonalizes unequal depths, but the
`omega=1` color is zeta itself.  Estimating its forcing still requires the
fixed-ratio anchor theorem.  This is `L-25604`.

## 7. Exact completion boundary

For fixed `c` and `B`, put

\[
E_{c,B}(J)=\int_J^{J+B}|Q_c(t)|^2dt.
\]

The surviving theorem is

\[
E_{c,B}(J)=e^{o(J)}.
\]

Its Laplace transform contains

\[
{1-c^{z+1/2}\over(z+1/2)\zeta(z+1/2)},
\]

so the numerator does not cancel an off-line zero.  The fixed-ratio shell
criterion gives

\[
E_{c,B}(J)=e^{o(J)}\iff RH.
\]

Any valid RBC family projects to this scalar theorem.  Conversely the scalar
theorem already completes RH without the rest of RBC.  This classification is
`T-25601`.

## 8. Cross-route conclusion

The result explains why the strongest live proposals now meet at one object.

```text
reflected RBC:
    one full-scale Möbius anchor needs coercivity;

balanced Type II:
    the same anchor needs signed lower-scale contraction;

carry/Gamma:
    a positive finite minorant must pay the same anchor without losing the
    critical mass;

parabolic carry transport:
    positive defect must be transported into equally macroscopic signed slack.
```

The signed constraint-dipole route of PR #254 is the most concrete current
attempt to prove a positive projection of this anchor.  It is not imported as a
proved theorem here.

## 9. Exact regression

`X-25601` checks:

```text
matrix inverse and derivative            exact
forward-shift last-row synthesis         exact
finite endpoint tail                     1/45
aggregate Schur reserve                   0
nonzero packet-kernel control             98/121
color/depth Parseval energy               11936689/1587600
meromorphic quotient rank                 1
far-right physical exponent               1/2
mutation tests                            8/8 PASS
proof-object SHA-256
f9804f4155ea5f88754f6bafc8b988542f3472b9570188269d283d876092a3be
```

The experiment is exact synthetic algebra only.

## Final status

```text
superorder non-top purge                   retained proposed
physical two-frequency reflected block     retained proposed exact
matrix packet/global source map             proposed exact
all depth cross terms                       proposed exact
bounded local depth incidence               proposed exact
aggregate reflected reserve                 refuted: Schur complement zero
far-right absolute contraction              refuted as subcritical mechanism
finite-resolvent pole deletion              refuted by charge conservation
analytic charge rank                         one
charge support scale                         full X scale
fixed-ratio anchor estimate                  open / RH-bearing
Riemann Hypothesis                           unproved
```

The pass did not produce a proof of RH.  It did prove that the remaining RBC
obligations cannot be completed by the advertised finite bookkeeping alone and
reduced every unresolved part to one explicit scalar anchor theorem.
