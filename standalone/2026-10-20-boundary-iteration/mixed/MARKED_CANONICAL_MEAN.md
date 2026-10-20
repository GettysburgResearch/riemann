# A divisor-marked canonical sextic mean

Date: 2026-10-20. Status: proposed source-dependent deduction, with its
analytic imports isolated below. This is a bound for prescribed arithmetic
coefficients. It is not a new arbitrary-coefficient sieve, an improved global
zero-free half-plane, or a proof of RH.

The latest inherited repository state is PR #1009, commit
`7f6ff9dae8d3473a5835a5cbe7308148b8b3c1a0`. Nothing in this note modifies an
inherited theorem. The new point is to retain prime-divisor marks through
sextic Poisson, instead of estimating each marked prime separately.

## 1. Imports and scope

Work over the Eisenstein integers, with good primary ideals avoiding a fixed
finite set of primes containing those above 6. Write \(q_a=Na\), and use the
literal zero extension of sextic residue symbols \(\chi_n(u)\), including
their sixth powers. All implied constants can depend on fixed annular test
supports, their finitely many smooth seminorms, the number of prime lists,
fixed finite ray data, and an arbitrarily small power loss.

The analytic input is the selected inverse estimate of Baiying Liu,
[Theorem 11.2, arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1), in the
normalization recorded in
`../../2026-10-20-angular-hecke-continuation/ANGULAR_THETA_AND_INVERSE.md`,
Section 7.2. Its needed content is precisely this:

Let

\[
 M_u(D;W)=\sum_n\frac{\mu(n)\nu(n)\chi_n(u)^{-1}}{\sqrt{q_n}}
                    W(q_n/D),
\quad
 Q_u=\prod_{i=1}^j
       \sum_{p\in\mathcal P_i}\frac{b_i(p)\chi_p(u)^{-1}}{\sqrt{q_p}}.
 \tag{1.1}
\]

The lists \(\mathcal P_i\) are fixed during the row sum, each in a fixed
norm annulus \(q_p\asymp P_i\); their bounded coefficients are independent
of the row. They may be arbitrary subsets. Put \(P=\prod_iP_i\), with
\(P=1\) for the empty product. For a fixed positive margin, the source
asserts

\[
 \sum_{0<q_u\le H}|M_u(D;W)Q_u|^2\ll H(HD P)^\epsilon
 \tag{1.2}
\]

when \(DP^2\) and \(D^{2/3}P^{8/3}\) are smaller than \(H\) by that
margin in logarithmic length. The estimate has the uniform fixed-seminorm
and norm-twist dependence needed for a common smooth profile. Conjugating
gives the opposite orientation. Replacing the source's \(D^{-1/2}\)
normalization by \(q_n^{-1/2}\) only changes its annular test.

This note assumes (1.2), not the source's final zero-free theorem. A growing
puncture is not included silently in (1.2): Section 3 below proves the
required extension by an exact Euler identity.

For the canonical consequence, the finite Gauss and masked Poisson
calculation is the one in Sections 10.2--10.3 of
[Structured cubic and sextic means for angular Gauss coefficients,
v3, 17 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/5).
We state the specific root, masks, frequency fibre and profile again in
Section 5. Only its finite algebra and masked Poisson reduction are used;
its all-length unmarked conclusion is not an input to the new proof.

All lengths are at least one. To impose strict source margins, use a common
base \(Z=\max(2,U,D,P,q_Q)\) and enlarge row bounds by \(Z^\eta\), choosing
\(\eta>0\) after the desired final \(\epsilon\). This keeps the source
logarithmic parameters in a fixed bounded range. Nonempty bounded subunit
column scales can be covered by a constant number of fixed windows.

## 2. An all-length selected inverse estimate

For sixth-power-free rows, (1.2) implies

\[
 \boxed{
 \sum_{0<q_u\le U}^{\mathrm{sixth\ power\ free}}
       |M_u(D)Q_u|^2
 \ll(UDP)^\epsilon U^{1/6}
       \max\{U,DP^2,D^{2/3}P^{8/3}\}^{5/6}.}
 \tag{2.1}
\]

Here and below a positive sum can be restricted to any fixed subset of its
rows. In particular a ball estimate gives an annular estimate.

**Proof.** Let \(H_0\) be the maximum in (2.1), put
\(H=Z^\eta H_0\), and take an amplifier prime \(a\) of norm comparable
to \(A=(H/U)^{1/6}\). We require that \(a\) lie outside all the prime
lists. This does not lose a power: choose \(j+1\) sufficiently separated
constant multiples of the \(A\)-annulus. Each of the \(j\) fixed-width
list annuli can intersect at most one of them. One amplifier annulus is
therefore disjoint from every list, and has \(\gg A/\log(2A)\) good
primes once \(A\) is large. The constants depend only on the fixed number
and widths of the lists. Enlarging \(H\) by its fixed annular constant is
harmless.

Complete zero extension gives the exact identity

\[
 M_u(D)=M_{ua^6}(D)
       -\frac{\nu(a)\chi_a(u)^{-1}}{\sqrt{q_a}}
                         M_{ua^6}(D/q_a).
 \tag{2.2}
\]

It remains valid if \(a\mid u\), when the second term vanishes. Because
the amplifier prime is outside the lists, \(Q_{ua^6}=Q_u\), with every
old common-prime zero unchanged. Multiply (2.2) by this same \(Q_u\),
square, and sum over \(u,a\). The map \((u,a)\mapsto ua^6\) is
injective on sixth-power-free \(u\): prime valuations modulo six recover
\(u\), and their quotients recover \(a\). No coprimality between \(u\)
and \(a\) is used.

The first term is bounded by (1.2) at row length \(O(H)\). In the second,
\(D/q_a\) lies in one fixed-width scale interval around \(D/A\), and
\(q_a^{-1}\ll A^{-1}\). Separate its common smooth profile, or apply
one-dimensional Sobolev to the scale and its Euler derivative. Equation
(1.2) applies uniformly at every such shortened scale and to the derivative
test. This bounds the second term by \(O(H)\) as well, with only the
permitted seminorm and small-power losses. Dividing by the number of
amplifier primes gives
\(U^{1/6}H^{5/6}\) up to logarithms. Allocate \(\eta\) and preliminary
losses below the final \(\epsilon\). This proves (2.1). \(\square\)

The construction is useful even when \(H_0=U\), because the slight
inflation supplies both the fixed source margin and a growing amplifier
annulus. It never requires a prime list to contain all primes in its
annulus.

## 3. Punctures and unrestricted rows

Let \(\psi_u(n)=\nu(n)\chi_n(u)^{-1}\). This is completely
multiplicative with its literal zeros. For a puncture \(Q\) fixed during
the row sum, Euler convolution gives

\[
 M_{u,Q}(D)
 =\sum_{\operatorname{rad}(e)\mid Q}
       \frac{\psi_u(e)}{\sqrt{q_e}}M_u(D/q_e).
 \tag{3.1}
\]

All supported prime powers \(e\), not merely squarefree ones, occur.
The identity follows coefficientwise from
\(\prod_{p\mid Q}(1-\psi_u(p)p^{-s})^{-1}\).
The common annular support truncates every actual sum. Its absolute
coefficient mass satisfies

\[
 \sum_{\operatorname{rad}(e)\mid Q}q_e^{-1/2}
 =\prod_{p\mid Q}(1-q_p^{-1/2})^{-1}
 \ll_\epsilon q_Q^\epsilon.
 \tag{3.2}
\]

Minkowski, contraction by \(\psi_u(e)\), and the monotonicity of the
right side of (2.1) under shortening \(D\) prove its punctured version
with a factor \(q_Q^\epsilon\). In this step the selected prime lists
and their coefficients stay fixed. Row-dependent choices of the puncture
are not asserted.

Every nonzero element row is uniquely \(u=vt^6\), where \(v\) is
sixth-power-free and the unit is retained in \(v\). There is no
condition \((v,t)=1\). At fixed \(t\), both \(M\) and \(Q\) acquire
their literal zeros at the primes of \(t\): the former has puncture
\(Qt\), and the latter has the same lists with primes dividing \(t\)
deleted. These are permissible fixed lists for that invocation. Expand
(2.1) into the sum of its three branches and sum over \(t\), using

\[
 \sum_tq_t^{-6}<\infty,
 \qquad \sum_{q_t\ll U^{1/6}}q_t^{-1}\ll\log(2U).
 \tag{3.3}
\]

After choosing the preliminary puncture and divisor losses sufficiently
small, (2.1) therefore holds on **all nonzero rows**, with the additional
factor \(q_Q^\epsilon\). This includes principal sixth-power rows.

## 4. Extracting prime-divisor marks

Let \(\mathcal P_i\) now be pairwise disjoint prime lists and put

\[
 A_i(n)=\sum_{p\in\mathcal P_i}\eta_i(p)\mathbf1_{p\mid n},
 \quad A(n)=\prod_{i=1}^j A_i(n),
 \quad |\eta_i(p)|\le1,
 \quad P=\prod_iP_i.
 \tag{4.1}
\]

The number \(j\) is fixed. Each \(A_i(n)\) is divisor-bounded; this is
not an arbitrary column coefficient. Define

\[
 \mathcal I_A(U,Y;Q)=
 \sum_{0<q_u\le U}
 \left|\sum_{(n,Q)=1}
   \frac{\mu(n)\nu(n)\chi_n(u)^{-1}A(n)}{\sqrt{q_n}}W(q_n/Y)
 \right|^2.
 \tag{4.2}
\]

Then

\[
 \boxed{\mathcal I_A(U,Y;Q)\ll(UYPq_Q)^\epsilon
 \left\{U+U^{1/6}Y^{5/6}P^{5/6}
           +U^{1/6}Y^{5/9}P^{5/3}\right\}.}
 \tag{4.3}
\]

To see the exact extraction, for one prime use the Dirichlet-series
identity

\[
 \sum_n\mu(n)\psi(n)\mathbf1_{p\mid n}(q_n)^{-s}
 =-\frac{\psi(p)q_p^{-s}}{1-\psi(p)q_p^{-s}}
                       \sum_n\mu(n)\psi(n)(q_n)^{-s}.
 \tag{4.4}
\]

Mellin inversion consequently gives a sum over **all** \(a\ge1\),
with coefficient \(-\psi(p)^a/q_p^{a/2}\) and inverse length
\(Y/q_p^a\). It is incorrect to replace (4.4) by just its first term.
For distinct lists the identities multiply without collision, since the
selected primes are distinct.

The terms with \(a=1\) in a set of slots form the selected prime product
in (1.1), while shortening the inverse length by the product of their
prime lengths. Separate the bounded prime norm ratios in one common
smooth profile before applying (2.1). For each slot with \(a\ge2\),
sum the coefficient absolutely; over one prime annulus

\[
 \sum_{p\in\mathcal P_i}\sum_{a\ge2}q_p^{-a/2}\ll1
 \tag{4.5}
\]

with a fixed constant. These terms only shorten the inverse length
further. If \(P_J\) is the product of the slots with first powers,
equation (2.1) uses

\[
 \max\{U,(Y/P_J)P_J^2,(Y/P_J)^{2/3}P_J^{8/3}\}
 =\max\{U,YP_J,Y^{2/3}P_J^2\}.
 \tag{4.6}
\]

Since \(P_J\le P\), this is bounded by the same expression with
\(P\). Minkowski and the fixed number of slot assignments prove (4.3).
For a puncture, first remove primes dividing \(Q\) from the lists, as
their original marked terms vanish. Apply (3.1) afterward; all its
supported prime powers are then disjoint from the surviving lists, so
\(A(en)=A(n)\) whenever \(\operatorname{rad}(e)\mid Q\). This
justifies the puncture loss without altering the mark.

The same bound holds for a fixed finite linear combination of products
over subsets of these slots, including a constant term. It also holds
after adding fixed outer divisor-bounded scalars. It does not allow
arbitrary row-dependent choices of \(\eta_i(p)\).

## 5. Canonical sextic consequence

Use the normalized Gauss sum \(\gamma_{-1}(n)\) with the source's
additive-character convention and define the prescribed coefficient

\[
 c(n)=\mu(n)\gamma_{-1}(n)\nu(n).
 \tag{5.1}
\]

The finite Gauss identity converts this to
\(C_{-1}(n)=\overline{\alpha(n)}\gamma_2(n)\), times a fixed finite
ray function. Thus this is the physical angular mode needed in the
source; no new angular inverse theorem is needed here.

For a positive normalized average of squarefree labels \(q_f\asymp F\),
let \(w(f)\ll\tau(f)^C\) be independent of the row and column. Put

\[
 \mathcal J_A(K,D,F;Q)=\frac1F\sum_{f\asymp F}w(f)
 \sum_{0<q_z\le K}
 \left|\sum_{\substack{n\ \mathrm{squarefree}\\(n,Q)=1}}
 \frac{c(n)A(n)}{\sqrt{q_n}}
         \chi_n(z)\chi_n(f)^4W(q_n/D)\right|^2.
 \tag{5.2}
\]

The labels, prime lists, puncture, and their coefficients are fixed
during their respective stated averages. The unlabelled case is
\(F=1,f=1,w(1)=1\). Then the proposed deduction is

\[
 \boxed{\begin{aligned}
 \mathcal J_A(K,D,F;Q)\ll(KDFPq_Q)^\epsilon\bigl\{
  &K+DF\\
  &+K^{5/6}D^{1/6}F^{-2/3}P^{5/6}\\
  &+K^{5/6}D^{-1/9}F^{-2/3}P^{5/3}\bigr\}.
 \end{aligned}}
 \tag{5.3}
\]

Here is the complete change to the finite Poisson reduction. Open the
square and write \(n_1=ga,n_2=gb\), with \(g,a,b\) squarefree and
pairwise coprime. Except for \(a=b=1\), the primitive row character is
\(\chi_a\overline{\chi_b}\), of conductor \(ab\). Its residual mask
is \((z,g)=1\). Masked Poisson introduces \(d\mid g\), a frequency
\(h\ne0\), and the new row

\[
 k=hf^2g^2/d=hf^2d(g/d)^2.
 \tag{5.4}
\]

The exact Gauss phase cancels both Gauss coefficients and leaves
\(\mu(a)\nu(a)\overline{\chi_a(k)}\) and its conjugate at \(b\),
times a fixed finite ray factor. This is an identity of zero-extended
functions: \(gf\mid(k)\), so their column zeros already remain in the
new characters. The real root, including the original normalization, is

\[
 \frac{K\mu(d)w(f)}{Fq_gq_dq_aq_b}.
 \tag{5.5}
\]

The original marks are still exactly \(A(ga)\overline{A(gb)}\).
Insert the complete projector
\(\mathbf1_{(a,b)=1}=\sum_{s\mid a,b}\mu(s)\), then set
\(a=sx,b=sy\). The resulting \(x,y\) are squarefree, punctured by
\(Qs\), but need not be mutually coprime. The zero \((s,k)=1\)
remains in the outer sum. The root splits as

\[
 \frac K{Fq_gq_dq_s^2q_xq_y}
 =\frac K{FDq_dq_s}
   \frac D{q_gq_s\sqrt{q_xq_y}}
   \frac1{\sqrt{q_xq_y}}.
 \tag{5.6}
\]

The middle factor is bounded and smooth on the actual windows. For each
slot, coprimality on that support gives the exact decomposition

\[
 A_i(gsx)=A_i(g)+A_i(s)+A_i(x).
 \tag{5.7}
\]

Expand the fixed product of slots. Outer factors depending on \(g,s\)
are divisor-bounded. Each residual column is an inverse polynomial
carrying a product of a subset of the original prime marks, so (4.3)
applies with the original total \(P\) as an upper bound. Different
subsets on the two sides are handled by Cauchy after the common profile
has been separated. The finite ray expansion changes only the fixed
characters of those two inverse polynomials.

On dyads \(q_g\asymp G,q_s\asymp S,q_k\asymp T\), put

\[
 Y=D/(GS),\qquad T_0=D^2F^2/K.
 \tag{5.8}
\]

Retain both old column windows, the middle factor in (5.6), and the full
Fourier kernel in one compact logarithmic profile, with independent
coordinates for \(f,g,s,k,x,y\). Its weighted Fourier norm is
\(\ll_A\min\{1,(T/T_0)^{-A}\}\). This follows directly from
Schwartz decay and integration by parts; there is no sharp selector
depending on the column.

For each \(k\ne0\), the number of structural preimages in (5.4) is
at most \(\tau((k))^3\), because \(f,d,g/d\) are divisors of
\((k)\) and \(h\) is determined. The original weight \(w(f)\) and
the new outer marks at \(g\) are also divisor-bounded in \(k\).
There is no additional count of the \(f\) or \(g\) range. Apply
weighted Cauchy to the entire outer sum before enlarging the positive
\(k\)-sum to a complete annulus. Discarding \((s,k)=1\) now is
legitimate. Also \(q_d^{-1}\le1\) and
\(\sum_{q_s\asymp S}q_s^{-1}\ll1\). The marks at \(s\), and
the puncture \(Qs\), cost only small powers. Thus the block is bounded
by

\[
 (KDFPTq_Q)^\epsilon\frac K{FD}
 \min\{1,(T/T_0)^{-A}\}
 \left\{T+T^{1/6}Y^{5/6}P^{5/6}
          +T^{1/6}Y^{5/9}P^{5/3}\right\}.
 \tag{5.9}
\]

All nonempty windows have \(Y\ll D\). Sum the logarithmically many
\(G,S\) dyads, and the full frequency tail with \(A\) sufficiently
large. When \(T_0\ge1\), substitute \(T=T_0\) in the braces.
When \(T_0<1\), nonzero lattice norms are bounded below and arbitrary
Schwartz decay gives the same upper bound. The three resulting terms are
exactly the last three terms of (5.3).

The original principal diagonal costs \(K\) times a small power,
since \(A(n)\) is divisor-bounded. The separate principal restoration
in the nonzero-frequency expression costs a small power as well; the
same divisor bound on the mark suffices there. Adding both proves (5.3),
conditional only on the imports stated in Section 1. Every cube or
reflection step beyond this canonical core is outside this theorem.

## 6. A strict gain and the remaining boundary obstruction

Take \(D=K\), \(F=1\), and \(1\le P\le K^{1/3}\). Then (5.3)
simplifies to

\[
 \mathcal J_A(K,K,1;Q)\ll(KPq_Q)^\epsilon K P^{5/6}.
 \tag{6.1}
\]

The last term is no larger than \(KP^{5/6}\), since this comparison
is precisely \(P^{5/6}\le K^{5/18}\). The elementary treatment
which extracts a marked prime and applies Cauchy over its label range
costs \(KP\), even if an unmarked row-scale estimate is granted. Thus
(6.1) saves \(P^{1/6}\) in this genuine, prescribed marked canonical
norm. It does not claim an optimal exponent.

It is essential not to turn this local gain into an unsupported
zero-free-boundary claim. In logarithmic variables \(D=U^r,P=U^z\),
the all-length inverse estimate (2.1) has exponent

\[
 E(r,z)=\frac{1+5\max\{1,r+2z,(2r+8z)/3\}}6.
 \tag{6.2}
\]

On the source detector class with thresholds \(\delta r\) and
\(2gz\), the count exponent is \(E(r,z)-\delta r-2gz\).
On its two overlong branches its derivative in \(z\) is respectively

\[
 5/3-2g,\qquad 20/9-2g.
 \tag{6.3}
\]

Both are positive throughout the relevant source range
\(0\le2g\le\delta\le5/6\). Therefore permitting these overlong
selected lengths does not improve the optimized count: a minimum occurs
on the old row-scale admissible edge, and for \(r\ge1\) at \(z=0\).
This is an exact monotonicity obstruction, not a numerical failure to
find better parameters.

There is an even more direct check at the canonical interface. Set the
positive label length to one and write \(K=Z^k,D=Z^d,P=Z^z\).
Requiring the right side of (5.3) to be at most \(Z^{d+\epsilon}\)
gives, besides \(k\le d\), exactly

\[
 d\ge k+z,\qquad 4d\ge3k+6z.
 \tag{6.4}
\]

These are the inherited selected canonical terminal margins. The new
quantitative estimate does not enlarge this admission region. Feeding it
back into the original selected inverse induction therefore does not
improve (1.2); treating it as a new admissible boundary would count the
same input twice.

An application to the actual mixed detector still must transport its
joint prime mark, puncture, complete cube variable, and common reflection
kernel into (5.2), at the real lengths. Merely substituting (6.1) into an
unmarked scalar inequality is invalid. In particular (5.3) does not
establish the full \(U^{6/5+\epsilon}\) inverse/plain mixed polygon
requested in the earlier repository route. The unmarked edge
\(r=3/2,m=0\) still has inherited exponent \(17/12\), a gap
\(13/60\) above \(6/5\).

## 7. Verification checklist for independent review

The analytic review should focus on these explicit points:

1. The exact scope and uniform seminorm dependence of source Theorem 11.2
   used in (1.2), including arbitrary fixed prime subsets and both
   orientations. No full-annulus prime input is used here.
2. Sixth-power injection, the two-term identity (2.2), and amplifiers
   avoiding every selected list, without imposing \((u,a)=1\).
3. All supported prime powers in (3.1) and (4.4), followed by Minkowski
   before any positive row enlargement.
4. The exact Gauss convention and zero masks in (5.4)--(5.7), and the
   divisor fibre before applying the inverse norm.
5. One common smooth profile before separation, including the prime
   norm ratios and the row-dependent Poisson kernel.

The companion `check_marked_exponents.py` checks the rational exponent
identities, the strict gain range, and the detector monotonicity. Such
checks do not prove the imported analytic estimates.
