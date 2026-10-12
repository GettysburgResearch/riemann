# A fixed-order guard search and its exact cofinal condition

Status: complete conditional algorithm theorem. No unbounded algorithm is
implemented or run here. No actual cofinal progress or time bound is proved.
Scope: actual Xi, its complete paired product and classical strip A1/2,
positive theta's imaginary-axis exclusion, and convergent directed
evaluation of its real values and one fixed logarithmic coefficient.
The complete shifted identity is the one already proved in
`HAUSDORFF_LOG_MOMENT_CRITERION.md`, SHA
`4f72ef0b7685bd0346f9c0d61b54819a2c7462de78d9620473cf07383ec9c54f`.
The global acute-sector projection is the one already reviewed in
`COFINAL_MOMENT_OBSTRUCTION.md`, SHA
`7588200870a048a52a9da84cb884e3062808d0e36f9b25a978d449340b3e8d35`.
Simplicity is essential to the cofinal condition below. This is not a
finite decision procedure for RH or for its truth with simplicity.

## FG1. One fixed moment suffices for a sound finite packet

Fix t1 and k1 throughout. Every source occurrence rho=x+iy with x>0 and
|y|<=1/2 has `D=rho^2+1` in the sector
`|arg D|<=arcsin(1/2)=pi/6`. Thus every Re(D^-1) is strictly positive.
If x<=H, then `|D|<=H^2+5/4` and

\[
 \Re(\rho^2+1)^{-1}
  \ge\frac{\sqrt3/2}{H^2+5/4}
  >p_H:=\frac{7}{9(H^2+5/4)}>0.
\tag{FG1}
\]

The last strict comparison is rational after squaring:3/4>49/81.
Conjugate grouping preserves the complete real moment

\[
 M=C_1(1)=\sum_{\Re\rho>0}m_\rho(\rho^2+1)^{-1}
         =-[w]\log\frac{\Xi(i\sqrt{1-w})}{\Xi(i)}.
\tag{FG2}
\]

Take any finite family of pairwise disjoint positive rational intervals
[a_i,b_i] with strict opposite signs of actual Xi at their endpoints.
Each selects ONE actual real occurrence gamma_i, without initially
assuming uniqueness, completeness or simplicity. For a directed upper
endpoint M_up>=M put

\[
                   U=M_{\rm up}-\sum_i\frac1{b_i^2+1}.
\tag{FG3}
\]

Since gamma_i<=b_i, each subtraction is a lower bound on its full selected
inverse-square contribution. U is therefore an upper bound on the complete
remaining real projected moment, including every unknown complex
occurrence and all extra multiplicities. Its terms are positive by FG1.
If U<p_H, there can be no remaining occurrence with real part at or below H.

If, in addition, every selected bracket lies wholly below or wholly above H,
the brackets below H contain exactly one SIMPLE real zero each, and they
constitute the complete source census through H. Any additional occurrence
in such a bracket would remain after selecting one and contradict the
guard. A complex occurrence cannot be selected by a real sign crossing and
is excluded by the same argument. No historical count or candidate list is
used in this finite certificate.

## FG2. A countable partial search

Enumerate all finite rational packets consisting of a positive rational H,
a finite family of disjoint positive rational intervals not straddling H,
and a directed precision. The empty family is permitted. Dovetail their
finite evaluations: retain a packet only when all endpoint enclosures have
strict opposite signs and its full directed FG3 upper bound is less than
the exact rational FG1 price. Emit the resulting complete SIMPLE census.

This specifies a computable schedule under the stated convergent directed
evaluation hypothesis. The source has actual real values, and the coefficient
in FG2 is a fixed local completed-zeta coefficient at real s3/2. Only that
one coefficient is needed. The theorem does not claim a particular native
implementation or convergence rate. Each emitted packet is sound without
RH, by FG1–FG3.

The emitted heights are cofinal if and only if EVERY source zero is real
and SIMPLE. Cofinality implies that assertion because every source zero
has a finite positive real part, and some emitted complete SIMPLE census
must extend past it. Purely imaginary source zeros have already been
excluded by positive theta.

Conversely, suppose RH and simplicity hold. Fix any H>0 that is not a
real source zero. Every finite set of real roots then has pairwise disjoint
rational strict sign brackets, since each root is simple. The complete
inverse-square sum is absolutely convergent. Select a finite real head
whose remaining shifted inverse-square sum is less than p_H/3. Refine its
finitely many brackets so that they do not straddle H and the total
subtraction error in FG3 is less than p_H/3. Increase precision until
M_up-M<p_H/3. The resulting finite packet has U<p_H and will appear in
the exhaustive search. There are root-free rational H arbitrarily large,
by source discreteness. Therefore the emitted heights are cofinal.

The argument requires no upper bound on the number of roots below the
selected head and no ability to recognize that the head is complete before
the guard succeeds. Enumeration eventually includes the finite witness
that exists under the assumed real simple spectrum.

## FG3. What is and is not uniform progress

The enumeration schedule is explicit and unconditional; cofinal SUCCESS
is conditional on RH and simplicity. The theorem gives no unconditional
lower bound on how far it progresses for actual Xi, no bound on runtime,
and no finite point at which an observer can conclude that it will remain
cofinal. Higher moments may greatly improve practical finite guards, but
an all-order hierarchy is not necessary for this qualitative conditional
cofinal search.

If an off-real source zero or any multiple real zero exists, every emitted
height is below its positive real part. For an odd multiple real zero,
one strict sign interval removes only one occurrence and the extra
multiplicity remains in the positive residual. For an even multiple root,
no strict crossing can remove all its occurrences either. This is precisely
the occurrence obstruction established by the fixed-source triple-root
positive-Fourier model in `COFINAL_RESIDUAL_SCALAR_CRITERION.md`.

Neither scalar positivity of the complete source nor the existence of
arbitrarily many sign crossings proves the missing cofinal success. This
partial search makes the logical condition and the fixed-order mechanism
concrete while preserving that actual-source gap.
