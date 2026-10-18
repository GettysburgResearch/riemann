# Independent scoped review of the all-order budget theorem

Reviewer: the native Newton/amplitude track, separate from the author of the
critical proof. Review is read-only; no critical-author file was edited.

Reviewed file: `research_pass2/critical/ALL_ORDER_BARRIER.md`.

Reviewed SHA-256:
`024145421147a157d59c8e5ef2bba4ca20555e63119dd6112be465e5a516d595`.

**Finding:** no substantive mathematical defect found in the claimed
fixed-order moment deduction, the positive-budget supporting planes or the
`100/111` method floor, within the declared imported family and physical
contracts. The result is an obstruction to deductions from a specified list
of upper estimates. It is not a lower bound for any actual family, integral
or zero set, and it does not assert that the floor is attainable.

## Sources actually checked

- Freshly read the family definitions and Theorem 1.1 in
  [de Faveri, arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1), including
  the distinction between sixth-power-free rows ordered by their full ideal
  norm and ordering by inducing conductor. Also read the concluding detector
  budget in Section 9.
- Fetched and read the shifted rowwise detector in #971 at commit
  `3f1d2a07631eb6cca1f2716be01f64e874667639`, file
  [SHIFTED_DETECTOR.md](https://github.com/GettysburgResearch/riemann/blob/3f1d2a07631eb6cca1f2716be01f64e874667639/standalone/2026-10-18-ramified-shifted-detector/SHIFTED_DETECTOR.md),
  Git blob `2d1afc3cf3040909f70f2a21d6e28d75fe1c99fe`. The actual prefix
  polynomial and the unchanged Type-II terms agree with the new proof.
- Matched the Mellin monomial in the local pinned `05-poisson.tex`. The
  two-term physical norm is the #965 reflected estimate and additive norm
  carried into #974's `FOURTH_MEAN_EXTENSION.md`, Section 3. That favorable
  norm is an explicit contract of the reviewed architecture; it is not the
  numerical `probe-low` estimate printed in `05-poisson.tex` itself.

This pass did not reprove the imported de Faveri theorem, reconstruct the
classical Hecke AFE from first principles, or re-audit every physical adapter
in #965 and #974. It reviews the new deductions from those stated inputs.

## Full columns, actual conductors and arbitrary fixed order

The complete-column adapter is sound. For `n=c d^6`, the squared coefficient
mass on a product dyad is `V^(1-2s0+eta)/(Nd)^6`. Applying the sieve on the
positive row restriction `(a,d)=1` and then Minkowski costs the convergent
sum of `(Nd)^(-3+eta)`. A coprimality condition between `c` and `d` would be
wrong; none is imposed. The finite twist factor `psi(d)^6` and all nonunit
zeros are retained. Equal-norm ideals remain different columns.

The main AFE piece gives the four displayed affine exponents. The dual piece
is especially important: its squared prefactor is the actual
`Q0^(r(1-2sigma))`, and combining it with its endpoint length produces
`Q0^(r(1/2-sigma)) K(U,Q0^(r/2))`. Negative conductor exponents are bounded
at small conductor instead of silently replacing them by powers of `U`.
The resulting maximum is correct. For `r>=4` the two hybrid terms lie below
`r(1-sigma)`, giving the asserted simplification. Fixed finite interpolation
between the four vertices is compatible with the exponent coordinates.
No limit requiring constants uniform in growing moment order is taken.

## Whole-family estimates versus zero-selected sets

The proof uses the same selected set before Hölder and interpolation. It
does not need statistical independence from the denominator zeros. The
current file explicitly caps a count budget at `nu<=1` and proves the
invariant `e>=nu*t`, where `t=1/p`; hence the selected first-mean budget
`m=nu*(1-t)+e` is at least `nu`.

The positive weights `24,34,8` on the three reflected affine estimates
give exactly `66e-55t+45y>=27`. This survives complex interpolation and
intermediate selected-set norm changes, since their cost changes the
left side by `(66nu-55) Delta t>=0` for `nu>=5/6`. It follows that
`66m+45y>=82` for every allowed selected first-mean estimate. Thus the
certificate constrains the whole declared sequence of operations, not
only a final application of Hölder to an otherwise unrestricted estimate.

For the separate `9/10` escape threshold, the weights `9,14,4` correctly
give `27e-22t+18y>=11`. The analogous intermediate-norm closure is
`(27nu-22) Delta t>=0` for `nu>=22/27`; this supplies the same scope at that
smaller count exponent. An explicit sentence recording this closure was
recommended to the author, as a clarity improvement. The numerical
consequences `1/54` and `1/72` are correct strict necessary savings.

## Forced class and asymmetric scales

At `sigma=2/3`, one retained Type-II endpoint equals `5/6` independently
of both support exponents and all first-term moment choices. In a complete
finite threshold partition, either the full good class is already placed
at or beyond `2/3`, or the first class whose upper placement reaches that
point is counted from a lower threshold at most `2/3`. Its available count
budget is therefore at least `5/6`. This argument is about what the retained
estimates must cover; it does not assert that the class is nonempty.

At the unavoidable frequency scale `U=Z^(1-alpha)`, the displayed Mellin
exponent is correct. For balanced scales, the supporting plane is exactly
the obstruction at `a=15/37`, hence boundary `100/111`. Smaller balanced
scales make this class more expensive. At a fixed proposed boundary, moving
either asymmetric case toward its balanced endpoint only decreases the
class's budget. In the `beta>=alpha` case the derivative is precisely
`-1/2-m+(2/3)y<0`. If the proposed boundary is below the floor, this path
stays inside short support. The added long-support comparison from the
same physical norm has minimum `11/12`, and cannot provide an escape.

## Literal polynomial and remaining scope

The polynomial in Section 6 really is the tail from the finite product
`L(s)M_A(s)-1`: its coefficients are
`c_A(n)=sum_(d|n,Nd<=A) mu_F(d)`. They vanish for `1<Nn<=A`.
The sieve applied to its complete columns at real part `2/3` pays

    V^(-1/3) K(U,V)
       = V^(2/3) + U V^(-1/3) + U^(1/3)V^(1/2) + U^(5/6).

The last term is the actual unchanged exponent responsible for the
barrier. Literal caps, the source convolution, the sixth-power masks and
the exponential tail remain in scope. A source-specific improvement of
that term is open, and the proof correctly says that it would still leave
the other detector and physical budgets to be checked.

No numerical optimizer, historical proposed global zero-free fraction,
finite moment-order sweep or finite checker is a premise of this review's
infinite supporting-plane conclusion. The new critical checker's execution
and artifact provenance are outside this scoped mathematical review.

## Final-byte addendum

The final proof bytes were read back at SHA-256
`18ef9e2f04a6bc5a49fad26768916ca05152a6e513ae56bd12fabed5f4650191`.
Relative to the reviewed version above, Section 6 now explicitly closes the
`27e-22t+18y>=11` certificate under every allowed selected-norm operation at
`nu>=22/27`, including the cost `(27nu-22) Delta t`. This is the recommended
clarification, and its algebra and scope are correct. The finding of no
substantive defect applies to these final bytes. The earlier hash is retained
as review history; this addendum supplies the final reviewed identity.
