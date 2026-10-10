# Correction-dependent cube cutoffs preserve the raw A2 saving

**Status:** proposed source-conditional theorem. The short-row saving
previously established for a raw two-factor Gauss polynomial transfers
to the full arithmetic A2 completion, uniformly in its moving inner
exclusion and fourth-power auxiliary. The transfer includes every
nonzero row. It does not prove the centered two-column covariance or
the generalized inverse-Mobius moment.

**Authorship:** root. An independent review must bind the final source.

**Exact dependencies:** the mixed completed estimate and exact A2 child
identities in [MOVING_AUXILIARY_ADAPTER.md](MOVING_AUXILIARY_ADAPTER.md);
PR #918, commit `cfa102748b26f840ccc4b963a660711424db0ec3`,
`standalone/2026-10-10-sextic-joint-core/INTERFACE_COMPARISON.md`,
equations (2.4), (3.1)--(3.5), and (3.10)--(3.12); and the refined
all-row sextic sieve in PR #913, commit
`6498d6cc2eded03159c7332b25fd224ad07f89c1`,
`REFINED_ALL_ROW_SIEVE.md`, Theorem 3.4. The short/long method is the
one in PR #923, commit `1a1152008706f7e24fa1efe4990588f8f99c5d8d`,
`ALL_ROW_COMPLETION_AND_RAW_GAIN.md`, Section 6. The new points here
are the mixed family, arbitrary rectangles, and a different cutoff
in each A2 correction child. The analytic input is explicitly
conditional on the imported October 5 theta framework and the stated
angular estimate; those foundations are not independently rebuilt.

## 1. Objects, scales, and statement

Use the Eisenstein field, primary generators, fixed bad set S, fixed
finite ray character xi, and literal character zeros of the sources.
Write

\[
a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n),\qquad
\lambda(n)=\overline{\alpha(n)}\xi(n).
\tag{1.1}
\]

Here lambda is a multiplicative coefficient, not the ramified-prime
generator. Every physical ideal index avoids S. For squarefree q,f,
with their overlap permitted, let

\[
P_q(A,B;k,f)=
\sum_{\substack{an\ {\rm squarefree}\\(an,qS)=1}}
a_\xi(an)\chi_{an}(k)\chi_{an}(f)^4
W_1(Na/A)W_2(Nn/B),
\quad \mathcal P_q=\frac{P_q}{\sqrt{AB}}.
\tag{1.2}
\]

The weights are fixed smooth functions supported on fixed compact
positive intervals. The A2 polynomial Q_q is the exact arithmetic
completion in PR #914, with the same tensor test, and
\(\mathcal Q_q=Q_q/\sqrt{AB}\). Its unambiguous finite definition
through P is recalled in Section 3.

Set

\[
r=\frac q{(q,f)},\qquad F=Nf,\quad R_q=Nr,\quad
\ell=R_qF=N\operatorname{lcm}(q,f),\qquad
m=R_q^{1/3}F^{2/3},\qquad X=\sqrt{AB}.
\tag{1.3}
\]

The letters r and R_q concern the exclusion. The positive real
number U below is the independent cube cutoff. Let \(\mathfrak D\ge2\)
be a reference parameter; A,B,H,Nq,Nf and all chosen cutoffs are
bounded by fixed powers of \(\mathfrak D\), allowing reciprocal
powers for subunit cutoffs. Initially A,B,H are at least one.
The row norm is

\[
\|F\|_H^2=\sum_{0<Nk\le H}|F(k)|^2.
\tag{1.4}
\]

Thus units, sixth powers, arbitrary good-prime valuations, and
fixed bad-prime factors are included. Define

\[
\begin{split}
\mathcal B(H,X;\ell,m,U)={}&HX
 +\ell H^2X^{5/12}U^{7/4}
 +m H^{4/3}X^{2/3}U^2\\
&+H^{1/6}X^2U^{-3}
 +H^{2/3}X^{4/3}U^{-2}.
\end{split}
\tag{1.5}
\]

### Theorem 1.1

Under the mixed completed input of the companion, for every
\(\epsilon>0\) and every such \(U>0\),

\[
\boxed{
\|\mathcal P_q(A,B;\cdot,f)\|_H^2
 +\|\mathcal Q_q(A,B;\cdot,f)\|_H^2
\ll \mathfrak D^\epsilon\,
\mathcal B(H,\sqrt{AB};\ell,m,U).
}
\tag{1.6}
\]

The implicit constant depends on the fixed supports, a finite number
of smooth seminorms, the fixed ray data, scale ceiling, and epsilon.
It is independent of the moving exclusions, auxiliaries, and rows.
The term \(H^{1/6}X^2U^{-3}\) retains the repeated-row cost from the
all-row sieve. There is no squarefree-row substitution.

An empty rectangle is zero. The same proof applies when a nonempty
A or B lies in its fixed support-dependent interval below one; all
displayed powers then remain comparable to their versions with that
scale replaced by one. This bounded extension is used for children.

## 2. The raw mixed polynomial with an arbitrary positive cutoff

The exact finite cube inverse is

\[
\mathcal P_q(A,B;k,f)
=\sum_{\substack{h\ {\rm squarefree}\\(h,qfS)=1}}
\frac{\mu_K(h)\lambda(h)^3\chi_h(k)^3}{Nh}
\mathcal C_{q,v_h}\left(A,\frac B{(Nh)^3};k,f\right),
\quad v_h(a)=\mathbf1_{(a,h)=1}.
\tag{2.1}
\]

The companion proves the completed estimate, with
\(T=\min(A,\sqrt B)\),

\[
\|\mathcal C_{q,v_h}(A,B;\cdot,f)\|_H^2
\ll\mathfrak D^\epsilon
\left[HA+\ell\frac{H^2A}{B}T^{5/6}
 +m\left(\frac{H^2A^2}{B}\right)^{2/3}\right].
\tag{2.2}
\]

The arbitrary h in its outer mask is permitted, but no arbitrary
outer coefficient is silently placed into its angular scalar input.

Because (1.2) is symmetric under interchange of the two axes and
their weights, orient the raw polynomial so that A is at most B.
Write the terms in (2.1) with \(Nh\le U\) as \(\mathcal S_U\).
Weighted Cauchy with weight \((Nh)^{-1}\), followed by (2.2), gives

\[
\|\mathcal S_U\|_H^2
\ll\mathfrak D^\epsilon
\left[HA+\ell H^2 A B^{-7/12}U^{7/4}
 +m H^{4/3}A^{4/3}B^{-2/3}U^2\right].
\tag{2.3}
\]

Indeed, on substituting \(B/(Nh)^3\), use
\(T\le\sqrt B/(Nh)^{3/2}\). The second and third terms of (2.2)
then have h powers \(7/4\) and 2. Ideal counting gives
\(\sum_{Nh\le U}(Nh)^{b-1}\ll_b U^b\) for b positive and U at
least one. The first term uses only the reciprocal-norm logarithm.
The sums are finite on physical support, so every logarithm is
absorbed into \(\mathfrak D^\epsilon\). If U is below one, the short
sum is empty and (2.3) remains true. No smooth scalar estimate in h
is applied to a sharp h cutoff.

For A at most B and X equal to \(\sqrt{AB}\),

\[
A\le X,\qquad
AB^{-7/12}=X^{5/12}(A/B)^{19/24}\le X^{5/12},\qquad
A^{4/3}B^{-2/3}=X^{2/3}(A/B)\le X^{2/3}.
\tag{2.4}
\]

Thus (2.3) is bounded by the first three terms in (1.5).

### 2.1 Regroup the long inverse before bounding it

Expand the physical cube variable b in the terms with \(Nh>U\),
and group by d=hb. Then

\[
\mathcal L_U(k)=
\sum_{\substack{Nd>U\\(d,qfS)=1}}
\frac{c_U(d)\lambda(d)^3\chi_d(k)^3}{Nd}
\frac{P_q^{[d]}(A,B/(Nd)^3;k,f)}
 {\sqrt{AB/(Nd)^3}},
\quad
c_U(d)=\sum_{\substack{h\mid d\\Nh>U}}\mu_K(h).
\tag{2.5}
\]

Here \(P_q^{[d]}\) includes exactly the extra outer mask
\((a,d)=1\). Its inner squarefree index can meet d. The unrestricted
d can have repeated prime factors; h and b need not be coprime.
The coefficient \(c_U\) is the signed divisor sum in (2.5), with
\(|c_U(d)|\le\tau_K(d)\). For U below one it equals
\(\mathbf1_{d=1}\), so (2.5) is still exact.

For fixed d, combine the two squarefree factors a,n into their
squarefree product. Its coefficients include all q,f,d masks and
are independent of k. The fixed-order divisor bound and ideal
counting give normalized squared coefficient mass
\(O(\mathfrak D^\epsilon)\). The all-row sieve therefore gives

\[
\left\|
\frac{P_q^{[d]}(A,B/(Nd)^3;\cdot,f)}
 {\sqrt{AB/(Nd)^3}}
\right\|_H^2
\ll\mathfrak D^\epsilon
\left[H+H^{1/6}\frac{X^2}{(Nd)^3}
 +H^{2/3}\frac{X^{4/3}}{(Nd)^2}\right].
\tag{2.6}
\]

For a nonempty subunit scale the fixed support constants give the
same estimate. Formula (2.6) needs no extra conductor factor in q,f:
their characters and masks are part of arbitrary column coefficients.

Apply Minkowski to (2.5). The height term costs a reciprocal-norm
logarithm. The other two square-root terms use

\[
\sum_{Nd>U}(Nd)^{-5/2}\ll U^{-3/2},\qquad
\sum_{Nd>U}(Nd)^{-2}\ll U^{-1}.
\tag{2.7}
\]

These inequalities hold also for U below one, with a larger fixed
constant. All divisor bounds are absorbed with smaller preliminary
epsilon losses on the polynomial support. Squaring yields

\[
\|\mathcal L_U\|_H^2
\ll\mathfrak D^\epsilon
\left[H+H^{1/6}X^2U^{-3}
 +H^{2/3}X^{4/3}U^{-2}\right].
\tag{2.8}
\]

Since X is at least one initially, and is bounded below by a fixed
positive support constant in every nonempty child, its first term
is absorbed into HX with a fixed constant. The
triangle inequality between the exact short and long pieces proves
the P assertion of Theorem 1.1 for every positive U. In particular
there is no requirement \(U\le X^{1/3}\) in this inequality. Such a
requirement is only useful when choosing an optimizing cutoff.

## 3. A different cutoff for each exact A2 correction

For pairwise-coprime squarefree c,d,e, with \((cde,qfS)=1\), write

\[
C=Nc,\quad J=Nd,\quad E=Ne,
\]

and define the child labels

\[
\begin{gathered}
A_t=A/(CJ^2E^2),\qquad B_t=B/(C^2JE^2),\\
q_t=qcde,\qquad f_t=ef,\qquad
X_t=\frac{X}{(CJ)^{3/2}E^2},\\
\ell_t=\ell CJE,\qquad
m_t=m(CJ)^{1/3}E^{2/3}.
\end{gathered}
\tag{3.1}
\]

The last two formulas use \(q_t/(q_t,f_t)=rcd\); the overlap at e
is retained. The exact A2 coefficient is

\[
\Omega_t(k,f)=\sqrt{CJE}\,\lambda(cde)^3a_\xi(e)
\chi_{cd}(k)^3\chi_e(k)^4\chi_e(f)^4,
\quad \omega_t=\Omega_t/\sqrt{CJE}.
\tag{3.2}
\]

With all literal zeros, \(|\omega_t|\le1\). The finite forward
projection is

\[
\boxed{
\mathcal Q_q(A,B;k,f)
=\sum_t\frac{\omega_t(k,f)}{CJE^{3/2}}
\mathcal P_{q_t}(A_t,B_t;k,f_t).
}
\tag{3.3}
\]

Every nonempty child has both factor scales bounded below by fixed
positive support constants. Empty children may be omitted. The same
weights W_1,W_2 are evaluated at the displayed child scales.

Choose the child cutoff to be

\[
\boxed{U_t=U/(CJ)^{1/2}.}
\tag{3.4}
\]

This choice can be below one. Section 2 was deliberately proved for
that case. Each child's cube inverse is exact at its own cutoff;
there is no requirement that distinct children have the same cutoff.
Orient each child separately with its shorter axis first when applying
the raw bound. Its product scale is still X_t and its q_t,f_t do not
change under that interchange.

### Lemma 3.1. Every correction norm sum converges

For each of the five terms in \(\mathcal B\), multiply the square
root of its child version by \(1/(CJE^{3/2})\), substitute (3.1) and
(3.4), and factor out the square root of the parent term. The exact
remaining norm weights are:

| Parent energy term | C power in the denominator | J power | E power |
|---|---:|---:|---:|
| \(HX\) | \(7/4\) | \(7/4\) | \(5/2\) |
| \(\ell H^2X^{5/12}U^{7/4}\) | \(5/4\) | \(5/4\) | \(17/12\) |
| \(mH^{4/3}X^{2/3}U^2\) | \(11/6\) | \(11/6\) | \(11/6\) |
| \(H^{1/6}X^2U^{-3}\) | \(7/4\) | \(7/4\) | \(7/2\) |
| \(H^{2/3}X^{4/3}U^{-2}\) | \(3/2\) | \(3/2\) | \(17/6\) |

For example the second row follows from

\[
\frac1{CJE^{3/2}}
(CJE)^{1/2}
\big((CJ)^{-3/2}E^{-2}\big)^{5/24}
\big((CJ)^{-1/2}\big)^{7/8}
=(CJ)^{-5/4}E^{-17/12}.
\tag{3.5}
\]

Every exponent is strictly greater than one. After removing
coprimality restrictions only in this nonnegative accounting sum,
each weight is summable by the absolutely convergent ideal zeta
series. These convergent factors are independent of every moving
scale and auxiliary. This proves the lemma.

Apply Minkowski to (3.3), keep its row phases as contractions, apply
the raw bound at U_t, and use
\(\sqrt{x_1+\cdots+x_5}\le\sum_i\sqrt{x_i}\).
Lemma 3.1 bounds the result by a constant times
\(\mathfrak D^{\epsilon/2}\sum_i\sqrt{\mathcal B_i}\).
Squaring and redistributing preliminary epsilon losses proves the Q
assertion of (1.6). This completes Theorem 1.1.

### Why the child cutoff matters

A common U in all children would leave the second row's C and J
exponents equal to \(13/16\), whose ideal sums do not converge.
The choice (3.4) changes them to \(5/4\) while leaving every long-tail
exponent greater than one. This is a convergence statement about the
actual correction series, not an assumption that its coefficients
are independent or random.

More generally \(U_t=U/(CJ)^\eta\) works for every fixed
\(3/14<\eta<1\). The lower endpoint comes from
\(13/16+7\eta/8>1\); the upper one comes from the long-tail
denominator powers \(5/2-3\eta/2>1\) and \(2-\eta>1\).
The choice one half gives the table above with comfortable strict
margins.

## 4. Explicit unramified-auxiliary range for the full A2 polynomial

Put q=f=1 and A=B=D. Then X=D and \(\ell=m=1\). The same
optimization as in PR #923 now applies to Q itself, by Theorem 1.1.

For \(1\le H\le D^{38/87}\), choose

\[
U=D^{4/15}H^{-7/30}.
\tag{4.1}
\]

The third and fourth terms of (1.5) are
\(D^{6/5}H^{13/15}\). The second is
\(D^{53/60}H^{191/120}\), at most that common value precisely in
the displayed range. The first and fifth terms are smaller there.
Consequently

\[
\boxed{
\|Q_1(D,D;\cdot,1)/D\|_H^2
\ll D^{6/5+\epsilon}H^{13/15},
\qquad 1\le H\le D^{38/87}.
}
\tag{4.2}
\]

For \(D^{38/87}\le H\le D^{19/22}\), choose

\[
U=D^{1/3}H^{-22/57}.
\tag{4.3}
\]

The second and fourth terms are \(D H^{151/114}\).
The third is \(D^{4/3}H^{32/57}\), no larger exactly above the
displayed lower junction. The first and fifth are also smaller.
The cutoff is at least one up to the displayed upper endpoint.
It follows that

\[
\boxed{
\|Q_1(D,D;\cdot,1)/D\|_H^2
\ll D^{1+\epsilon}H^{151/114},
\qquad D^{38/87}\le H\le D^{19/22}.
}
\tag{4.4}
\]

The two bounds agree at \(H=D^{38/87}\). In particular,

\[
\boxed{
\|Q_1(D,D;\cdot,1)/D\|_H^2\ll D^{2+\epsilon}
\quad(1\le H\le D^{114/151}).
}
\tag{4.5}
\]

At \(H=D^{1/2}\), (4.3) gives \(U=D^{8/57}\), and

\[
\boxed{
\|Q_1(D,D;\cdot,1)/D\|_{D^{1/2}}^2
\ll D^{379/228+\epsilon}.
}
\tag{4.6}
\]

The prior classical envelope at this height is
\(D^{25/12+\epsilon}\). The exponent difference is \(8/19\).
PR #923 already proved (4.6) for P. The new conclusion is its transfer
to the full arithmetic Q, with the moving mixed family and all A2
correction children quantitatively covered.

## 5. Exact boundary of this gain

This theorem estimates a positive row norm of the A2 completion and
its raw face. It can be used for complete mixed children at smaller
rectangles without an unstated positive conductor gap. The fixed
finite-prime exclusions, growing q,f, their overlap, and arbitrary
row valuations are part of the theorem.

The fourth-moment sufficient target in PR #914, equation (6.9), is
a different object: the signed b,f sum of strict off-diagonal
correlations with its common row-dependent kernel. Applying an A2
projection to both columns gives two independently corrected labels.
For t=(c,d,e), the reconstructed product column includes
\(s_t=c^3d^3e^4\), so the removed equality is
\(s_ta n=s_{t'}a'n'\). The positive norm (1.6) does not estimate that
centered sesquilinear form at the required scale.

At the longest balanced fourth-moment core, the initial dual height
is of order \(D^{3-\theta}\), while (4.5) reaches only
\(D^{114/151}\). No iteration closing that gap is proved here.
Therefore this transfer does not establish the full fourth moment,
the \(17/24\) boundary, the generalized diagonal hierarchy, or RH.
