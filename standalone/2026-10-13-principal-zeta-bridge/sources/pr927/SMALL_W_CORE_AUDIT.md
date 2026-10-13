# Bounded small-w audit: the exact native return and the remaining positive-norm barrier

**Status:** an exact consequence and a source-qualified adapter, followed by a
method-specific optimization diagnosis. No new full moment theorem is asserted.
The adapter is an application of the already available two-native-axis
machinery; it is not presented as a new native mean-square input. This audit
does not alter any frozen proof.

## Sources and the two different scalar exponents

- `pass2_signed_auxiliary.md`, SHA256
  `6b8277e64adb1121704fbf7dc4553aeda31b598c65e0279d80316a35d66d38bf`,
  especially (3.6), (3.7), Lemma 5.1, and Theorem 6.1.
- PR #921, commit `4e6d4aa57ae4cb04d76b2b31279ac367951b469a`,
  `HERMITIAN_INCIDENCE.md`, SHA256
  `5c1844409097959a772916e1658ec61dfa747da857dd48321869d0a38cbc66e9`:
  the smaller-scale, moving-exclusion native M2, its finite smooth seminorm
  dependence, the critical disjointness correction, and the Schwartz adapter.
- `MOVING_COLUMN_MASKS.md`, SHA256
  `068c7c993bdf09e17c2c06182ca8bc631e6ed34d8df6ccf29c46e1f2333ae0ee`.
- `A2_MOVING_MEAN_SQUARE.md`, SHA256
  `6eed5695c672dab92620763f8df5b63f60dc416754367ed541cb854bf06854ba`.
- `HYBRID_CUBE_INVERSE.md`, SHA256
  `d4c5dad1b5c719043ac7118c5f468b3d5c398e2bbd5c4470a1983f64139f066a`.

Write beta for the finite-order inverse pointwise exponent of the signed
reunion note, and write kappa for the angular scalar exponent of the hybrid
cube theorem. These are different premises. Counting gives either exponent
one; beta=7/8 and kappa=11/12 retain their separate source conditions.
All native M2 statements below retain their imported canonical premise.

## 1. A final exact divisor reunion returns the native covariance

In the exact native formula (3.6), put g=bw and s=wr. Multiplication by the
chosen primary generator of w is a bijection from nonzero element rows r to
the nonzero rows s divisible by w. Its norm identity is

\[
Nw\,Nr=Ns.
\tag{1.1}
\]

For fixed g, the primitive columns z1,z2, their exclusions, the two values
v(gz_i), the finite-ray scalar, and the new row character are all independent
of the divisor w of g. Thus the remaining signed divisor factor is exactly

\[
\sum_{w\mid g}\mu(w)\mathbf1_{w\mid s}
=\prod_{p\mid g}(1-\mathbf1_{p\mid s})
=\mathbf1_{(s,g)=1}.
\tag{1.2}
\]

This is a complete divisor sum; imposing a cutoff on w changes it to a
truncated divisor weight, not to the indicator in (1.2). All the column sums
are finite and the row sums are absolutely convergent against the fixed
Schwartz profile, so the regrouping is legitimate.

Consequently the complete signed expression is exactly

\[
\begin{split}
\mathcal O_\xi[v]=\frac1L\sum_{g\ {\rm sf}}
\sum_{\substack{z_1,z_2\ {\rm sf},\ (z_1,z_2)=1\\
 (z_1z_2,gS)=1,\ (z_1,z_2)\ne(1,1)}}
&\mu(z_1)\mu(z_2)\xi(z_1)\overline{\xi(z_2)}
G(z_1z_2^{-1})\overline{v(gz_1)}v(gz_2)\\
&\cdot\sum_{s\ne0}\mathbf1_{(s,g)=1}
\overline{\chi_{z_1}(s)}\chi_{z_2}(s)\Phi(Ns/H).
\end{split}
\tag{1.3}
\]

Every original column exclusion remains in v. In particular a moving q0
restricts g,z1,z2 exactly as in the signed theorem.

Expand the fixed function G as G(x)=sum_eta c_eta eta(x), and set

\[
B_{\nu,v}(s)=
\sum_{n\ {\rm sf}}\mu(n)\overline{\nu(n)}\chi_n(s)v(n),
\qquad
\Delta_v(s)=\sum_{n\ {\rm sf}}|v(n)|^2\mathbf1_{(n,s)=1}.
\tag{1.4}
\]

All columns in these sums retain their fixed and moving exclusions. The
bijection n1=gz1, n2=gz2 identifies (1.3) with

\[
\boxed{
\mathcal O_\xi[v]
=\frac1L\sum_\eta c_\eta
\sum_{s\ne0}\Phi(Ns/H)
\bigl(|B_{\xi\eta,v}(s)|^2-\Delta_v(s)\bigr).
}
\tag{1.5}
\]

To check the diagonal exactly, n1=n2 is equivalent to the primitive unit
pair. The common character has squared modulus 1_(s,g)=1, and the fixed
character at g cancels with its conjugate. The sum of the diagonal Fourier
coefficients is G(1), as also obtained directly from the quotient scalar.
There is no assumption that the c_eta are positive, or that Phi is positive.

Equation (1.5) shows what the complete signed auxiliary reconstruction has
accomplished. It removes the artificial divisor multiplicity and recovers
the actual native centered product-column energy. It does not produce a
second independent source of cancellation after the original native
covariance has been reconstructed.

## 2. A valid ambient-height adapter for every w

Assume the native input at H=D^h, h=1+theta, with the original smaller-scale
range X<=C D and polynomial moving exclusions. Let beta>1/2 be the optional
finite-order pointwise exponent, set a=2 beta-1, and fix k>=2. Write

\[
L=D^k,\qquad Nb\asymp B,\qquad Nw\asymp W,
\qquad Z=\frac L{BW}.
\tag{2.1}
\]

Nonempty bounded subunit scales are replaced by one only up to fixed support
constants. Define O_(B,W) by restricting the full signed expression to these
b,w ranges, while keeping its complete primitive-column sum and original
row kernel. Sharp b,w norm annuli are allowed.

For a fixed b,w and their g=bw allocation matrix, the 2k singleton axes have
lengths X1,...,Xk,Y1,...,Yk, each at most C D, with

\[
\prod_i X_i=\prod_i Y_i=\frac L{Ng}\asymp Z.
\tag{2.2}
\]

Use s=wr, but do not enlarge the original row scale H. The selected-row
weight is 1_(w|s) Phi(Ns/H), dominated by the original Schwartz majorant.
The native second moment and row Cauchy therefore apply at height H to two
chosen axes. This does not assert a native bound at H/Nw with the moving
twist chi_n(w).

Let Q1>=Q2 be the two largest singleton lengths. Their product is at least
a fixed constant times Z^(2/k). With pointwise estimates on the other axes,
the resulting complete disjoint product has row L1 bound

\[
\begin{split}
D^\epsilon H(Q_1Q_2)^{1/2}
\prod_{i\ne1,2}Q_i^\beta
&=D^\epsilon H Z^{2\beta}(Q_1Q_2)^{-a/2}\\
&\ll D^\epsilon H Z^{1+a(1-1/k)}.
\end{split}
\tag{2.3}
\]

This calculation is first made after the exact disjointness correction.
The two selected axes are selected before its shifts. Their weights are
1/2, and the others have weight beta. The sole critical pair is handled by
the finite-horizon D^epsilon estimate in the pinned Hermitian lemma; all
other pairs have weight sum greater than one. All moving exclusions and
literal zeros survive. Mellin separation of the original coupled smooth
tests has a fixed finite seminorm loss. The Schwartz annular adapter changes
only the reference parameter, retaining the original column scales.

There are at most D^epsilon allocations for each g and O(BW) choices of b,w
in the norm block. Dividing (2.3) by L therefore gives

\[
\boxed{
|\mathcal O_{B,W}|
\ll D^\epsilon H Z^{a(1-1/k)}.
}
\tag{2.4}
\]

The excluded primitive unit pair costs O(D^epsilon H) only at Z comparable
to one. It obeys the same estimate. Taking the minimum with the existing
pointwise block estimate yields the valid combined bound

\[
\boxed{
|\mathcal O_{B,W}|
\ll D^\epsilon H
\min\left\{Z^{a(1-1/k)},\frac{Z^a}{W}\right\}.
}
\tag{2.5}
\]

The first alternative improves the second precisely when
W<Z^(a/k), apart from fixed constants. At w=1 this is the cross-pair
incidence face already controlled by the two-axis machinery: every shared
prime appears once on each Hermitian side and has signed character exponent
zero. The nonprincipal cubic pools do not act on those shared primes.

Summing the first alternative gives, for the sharp w tail R>=1,

\[
|\mathcal O_{\ge R}|
\ll D^\epsilon H (L/R)^{a(1-1/k)}.
\tag{2.6}
\]

This is useful below the crossover with the pointwise-only tail, but it
reaches diagonal size only when R is comparable to L. It does not improve
the diagonal-size threshold of the already proved sharp auxiliary tail.

The loss of row density in (2.3) is explicit: the native theorem bounds the
rows w|s by the energy of all rows at H. Its cost relative to a hypothetical
twisted M2 at H/Nw is Nw. The moving-mask theorem, which changes an original
column exclusion into a literal sixth-power twist, does not remove this
first-power row twist.

## 3. Why the supplied positive hybrid estimates do not close the balanced core

Here specialize to k=2 and write H=D^h. The original covariance target is
O(H D^epsilon). To compare with the positive two-axis Gauss bounds, undo the
second Poisson transform. At b=w=1 the literal columns have two physical
axes of length D, and their dual row height is

\[
Y=\frac{D^4}{H}=D^{4-h}.
\tag{3.1}
\]

Even if one grants a loss-free treatment of the primitive-pair restriction
and the coupled smooth kernel, the Cauchy benchmark for a normalized literal
energy E(Y;D,D) carries the factor H/D^2. Both the supplied hybrid and full
A2 positive estimates contain the term YD, independently of their cutoffs.
That term becomes

\[
\frac H{D^2}\,YD=D^3.
\tag{3.2}
\]

Thus these displayed positive inequalities cannot certify the desired
O(H D^epsilon) bound when h<3. In the intended range 1<h<2 they do not even
improve the existing two-axis/pointwise leading-core estimate
H D^(2 beta-1) at beta=1 or beta=7/8. Increasing either truncation does not
change (3.2). This statement is about the right-hand sides of the supplied
inequalities; it is not a lower bound for the actual arithmetic energy.

The b exclusion causes a second, separate difficulty. Consider an admissible
balanced residual allocation at w=1 with Nb comparable to B. Put

\[
Z=D^2/B,\qquad m=M=\sqrt Z,\qquad Y=Z^2/H.
\tag{3.3}
\]

The original exclusion is q0=b and the fourth-power auxiliary is one, so
the new adapter has exactly J=B and K=B^(1/3). The two positive column norms
have normalizer sqrt(Z). After counting the B choices of b, the optimistic
conversion factor is H B/D^2=H/Z. Again this benchmark grants zero additional
loss for the primitive-pair correction, so it isolates a difficulty present
before that correction is estimated.

By the general-rectangle hybrid bound, its second short term is

\[
B Y^2 Z^{\kappa/2-1/4} R^{5/2-\kappa},\qquad R\ge1.
\tag{3.4}
\]

After multiplication by H/Z, its ratio to the target H is at least

\[
\frac{D^2}{H^2}Z^{7/4+\kappa/2}.
\tag{3.5}
\]

The compact dual row support is empty when Y is sufficiently small. Whenever
it contains a nonzero element, Y is bounded below by a fixed positive
constant, hence Z is at least a fixed constant times sqrt(H). Therefore
(3.5) is at least a fixed constant times

\[
D^2 H^{-9/8+\kappa/4}.
\tag{3.6}
\]

At kappa=11/12 this is D^2 H^(-43/48). For every 1/2<kappa<=1 it exceeds a
fixed power of D throughout 1<h<2. The R power in (3.4) is positive; the
additional T power in the full A2 hybrid is also positive. Thus no choice
of the allowed cutoffs eliminates this particular obstruction on the
balanced residual blocks. Treating the q0 exclusion as a contraction of
the theta norm would erase the factor B and would be an invalid change of
the proven theorem.

This does not rule out cancellation in b, between A2 corrections, or within
the signed covariance before Cauchy. Such cancellation would be additional
arithmetic information. Nor does it claim that every unbalanced residual
block is beyond every existing incidence estimate. It locates a family of
balanced admissible scales on which the supplied positive bounds do not
settle the remaining core.

## 4. The minimal missing gain identified by this audit

At b=w=1, the exact remaining primitive pair consists of 2k disjoint native
inverse axes of length D, with the original coupled smooth tests and fixed
finite-ray coefficient G. Its unnormalized row sum needs a bound of size

\[
H D^{k+\epsilon}.
\tag{4.1}
\]

The two-axis inputs give only H D^(1+2(k-1) beta+epsilon). The missing saving
for this specified primitive family is therefore

\[
D^{(k-1)(2\beta-1)}.
\tag{4.2}
\]

For k=2 this is D at the counting pointwise exponent and D^(3/4) at the
source-conditional beta=7/8. A theorem supplying that saving for the actual
primitive multilinear coefficients would address the leading sector.
A theorem uniform over the required shifted physical axes and retained
row masks would also provide the interface for the adjoining sectors.
An arbitrary-coefficient moment claim is unnecessary, and a positive norm
for the differently normalized short-row A2 family does not supply (4.1).

For w>1, a genuinely shorter-row native theorem with the actual moving
first-power twist chi_n(w), an explicit useful dependence on Nw, and the
same exclusions would strengthen (2.5). It would not by itself remove the
balanced w=1 obstruction in (4.2). The bounded attack therefore yields the
exact reconstruction (1.5) and the legitimate adapter (2.5), while leaving
this named arithmetic cancellation problem open.
