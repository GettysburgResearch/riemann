# The spherical cubic residue: exact divisibility law and marked cancellation

Date: 20 October 2026.

Status: proposed source-dependent analytic component. The residue formula is
imported from Dunn--Radziwill; the exact divisor law, coherent-mark adapter,
and sparse-row estimates below are proved here. They do not constitute a new
zero-free boundary or removal of the resonant exceptions in PR #1009.

Scope: the Eisenstein field, the actual normalized cubic Gauss coefficients,
arbitrary finite squarefree divisibility/coprimality filters, and a smooth
short Mobius mark. The marked saving uses a stated zero-free input. None of
the arguments assume GRH or an unproved mixed-moment estimate.

Exact sources: Dunn and Radziwill, *Bias in cubic Gauss sums: Patterson's
conjecture*, [arXiv:2109.07463v3](https://arxiv.org/html/2109.07463v3),
equations (2.2)--(2.3), Proposition 5.2 and its residue formula.
The source version is dated 14 May 2024. The zero-free premise may be supplied
by the source-dependent Liu input recorded in the preceding packet, but is
kept as a parameter below. No GRH-dependent theorem from Section 8 of
Dunn--Radziwill is used.

What was run: the companion exact-rational checker verifies the local
divisibility/filter identities and the sparse-row exponent calculations.
It does not check the imported analytic theorem or certify a numerical
zero-free region.

Smallest remaining gap: inserting this residue into **every** labeled,
reflected, and selected inverse-moment state in Liu's induction with its
original normalizations. A favorable bound for the unmarked residue alone
does not perform that insertion.

## 1. Normalization and the imported residue

Let \(E=\mathbb Q(\omega)\), \(\omega^2+\omega+1=0\), and use primary
generators \(a\equiv1\pmod3\). They identify integral ideals coprime to
3 with generators. All sums below are over these generators, or equivalently
these ideals. Put \(q_a=Na\), and write \(g(a)\) and

\[
 \widetilde g(a)=g(a)/\sqrt{q_a}
\]

for the source cubic Gauss sum and its normalization. It vanishes unless
\(a\) is squarefree, has absolute value one on squarefree \(a\), and satisfies

\[
 \widetilde g(ab)=\widetilde g(a)\widetilde g(b)
                  \overline{\left(\frac ab\right)_3}
 \qquad ((a,b)=1).
 \tag{1.1}
\]

Here the reciprocity conventions are those of the source. In particular,
the two primary cubic symbols in the usual Gauss-product identity are
equal, and their product is their conjugate.

For squarefree primary \(r\), including \(r=1\), set

\[
 \psi_r(c)=\overline{\left(\frac cr\right)_3},\qquad
 G_r(s)=\sum_c\widetilde g(c)\psi_r(c)q_c^{-s}.
 \tag{1.2}
\]

The character has its natural zero at a common prime. Initially
\(\Re s>1\). Write

\[
 Z_3(z)=\zeta_E^{(3)}(z),\qquad
 C_E=\frac{(2\pi)^{5/3}}
          {3^{7/2}\Gamma(2/3)Z_3(2)}>0.
 \tag{1.3}
\]

Proposition 5.2 of the cited source gives a simple pole at \(s=5/6\)
and its residue. Dividing its displayed residue by
\(\zeta_E^{(3r)}(2)=Z_3(2)\prod_{p\mid r}(1-q_p^{-2})\) gives exactly

\[
 \boxed{R_r:=\mathop{\rm Res}_{s=5/6}G_r(s)
 =C_E\overline{\widetilde g(r)}q_r^{-1/6}
                    \prod_{p\mid r}\frac{q_p}{q_p+1}.}
 \tag{1.4}
\]

This is nonzero. In particular \( |R_r|\le C_Eq_r^{-1/6}\).
This calculation does not assert that \(G_r\) has no other poles away
from \(5/6\); zeros of the ordinary factor divided out in the source
identity matter to that separate question.

## 2. Exact residue under native divisibility and coprimality filters

Put

\[
 w(a)=\prod_{p\mid a}(q_p+1)^{-1}
\]

for squarefree \(a\), with \(w(1)=1\).

**Proposition 2.1.** If \(a\) is squarefree and \((a,r)=1\), then

\[
 \mathop{\rm Res}_{s=5/6}
   \sum_{a\mid c}\widetilde g(c)\psi_r(c)q_c^{-s}
       =R_r w(a).
 \tag{2.1}
\]

If \((a,r)>1\), the series is identically zero. More generally, if
\(a,b\) are squarefree, \((a,b)=(a,r)=1\), then

\[
 \mathop{\rm Res}_{s=5/6}
   \sum_{\substack{a\mid c\\(c,b)=1}}
        \widetilde g(c)\psi_r(c)q_c^{-s}
   =R_r\prod_{p\mid a}\frac1{q_p+1}
          \prod_{\substack{p\mid b\\p\nmid r}}\frac{q_p}{q_p+1}.
 \tag{2.2}
\]

The last product automatically ignores exclusions already enforced by
the zero extension of \(\psi_r\). No assumption of an Euler product
for \(G_r\) is made.

**Proof.** Squarefree support and (1.1), first on \(\Re s>1\), give

\[
 \sum_{a\mid c}\widetilde g(c)\psi_r(c)q_c^{-s}
   =\widetilde g(a)\psi_r(a)q_a^{-s}G_{ra}(s).
 \tag{2.3}
\]

The new zero extension enforces \((c/a,a)=1\), as required. The exact
phase identity following from (1.1) and cubic reciprocity is

\[
 \widetilde g(a)\psi_r(a)
        \overline{\widetilde g(ra)}
             =\overline{\widetilde g(r)}.
 \tag{2.4}
\]

Take residues in (2.3) and insert (1.4). The remaining norm factor is
\(q_a^{-5/6-1/6}=q_a^{-1}\), which multiplied by
\(\prod_{p\mid a}q_p/(q_p+1)\) is \(w(a)\). This proves (2.1).
Inclusion--exclusion over the primes of \(b\) proves (2.2), since
\(1-(q_p+1)^{-1}=q_p/(q_p+1)\). All sums used in this last step are
finite. Meromorphic continuation of the finite identities licenses
taking their residues. \(\square\)

Thus the *residue functional*, despite the absence of a scalar Euler
product for the Gauss coefficients, has the exact independent prime
divisibility weights \(1/(q_p+1)\). This distinction is essential.

### The completed theta index has the even simpler weight \(1/q_p\)

Keep the unrestricted cube factor in the actual theta coefficient and put

\[
 T_r(s)=G_r(s)Z_3^{(r)}(3s-1/2)
       =\sum_{c,b}\widetilde g(c)\psi_r(cb^3)q_b^{1/2}
                        (q_cq_b^3)^{-s}.
 \tag{2.5}
\]

The superscript means omission of the primes of \(r\). Its residue is

\[
 R_r^\theta=R_rZ_3^{(r)}(2)
   =\frac{(2\pi)^{5/3}}{3^{7/2}\Gamma(2/3)}
       \overline{\widetilde g(r)}q_r^{-1/6}
                 \prod_{p\mid r}(1-q_p^{-1}).
 \tag{2.6}
\]

For a prime \(p\nmid3r\), requiring \(p\nmid cb^3\) multiplies this
residue by

\[
 \frac{q_p}{q_p+1}(1-q_p^{-2})=1-q_p^{-1}.
 \tag{2.7}
\]

The first factor is the proved squarefree-column exclusion; the second
comes from the absolutely convergent cube Euler factor at the pole.
Consequently requiring \(p\mid cb^3\) multiplies the residue by exactly
\(q_p^{-1}\). For a squarefree \(a\) coprime to \(r\), requiring
\(a\mid cb^3\) multiplies it by \(q_a^{-1}\); arbitrary disjoint
coprimality filters multiply it by \(\prod(1-q_p^{-1})\). These statements
follow by finite inclusion--exclusion and concern the full theta index.

For disjoint selected prime lists \(\mathcal P_i\), supported on fixed-ratio
annuli and with bounded separate coefficients \(b_i(p)\), the residue
multiplier of the full-index mark
\(\prod_i\sum_{p\in\mathcal P_i}b_i(p)1_{p\mid cb^3}\) is therefore

\[
 \prod_i\sum_{\substack{p\in\mathcal P_i\\p\nmid r}}
                         \frac{b_i(p)}{q_p}.
 \tag{2.8}
\]

Its absolute value is bounded uniformly in the annular lengths, for a
fixed number of positions: elementary ideal counting gives
\(\sum_{P\le q_p\le CP}q_p^{-1}=O_{E,C}(1)\).
No row-independent lower bound for this multiplier is claimed.

## 3. A coherent Mobius mark has a reciprocal-zeta saving

Fix \(1/2<\beta<1\). Assume

\[
 Z_3(z)\ne0\quad(\Re z>\beta).
 \tag{3.1}
\]

The pole at \(z=1\) is permitted, and becomes a zero of \(1/Z_3\).
For the smoothed estimate below use also the standard consequence
that \(1/Z_3(z)\) has polynomial growth on each fixed vertical line
strictly to the right of \(\beta\). It follows, for this fixed field,
from the ordinary finite-order/growth bounds and zero-freeness by
Borel--Caratheodory. Alternatively it can be retained as an explicit
analytic input; the claimed saving uses it only for Mellin shifting.

For squarefree \(r\), \(B\ge1\), and fixed
\(W\in C_c^\infty((0,\infty))\), define the actual divisor functional

\[
 A_{r,W}(B)=\sum_{(a,r)=1}\mu_E(a)w(a)W(q_a/B).
 \tag{3.2}
\]

Here \(w\) need only be evaluated on squarefree arguments since
\(\mu_E\) vanishes on the others.

**Theorem 3.1.** Under (3.1), for every \(\epsilon>0\),

\[
 \boxed{A_{r,W}(B)\ll_{E,\beta,\epsilon,W}
                       q_r^\epsilon B^{\beta-1+\epsilon}.}
 \tag{3.3}
\]

The constant is uniform in squarefree \(r\) and \(B\ge1\). In
particular, the residue produced by a coherent short Mobius mark
has a power saving; taking absolute values of the mark would lose it.
For tests on a fixed annulus the constant uses only finitely many
derivatives. Replacing \(W(x)\) by \(W(x)x^{it}\) has a polynomial
cost in \(1+|t|\), by the same Mellin integration-by-parts proof.

**Proof.** For \(\Re s>0\), the relevant Dirichlet series is

\[
 A_r(s)=\sum_{(a,r)=1}\mu_E(a)w(a)q_a^{-s}
       =\prod_{p\nmid3r}\left(1-\frac{q_p^{-s}}{q_p+1}\right).
 \tag{3.4}
\]

It factors as

\[
 A_r(s)=\frac{K(s)}{Z_3(s+1)}
      \prod_{p\mid r}\left(1-\frac{q_p^{-s}}{q_p+1}\right)^{-1},
 \quad
 K(s)=\prod_{p\nmid3}
  \frac{1-q_p^{-s}/(q_p+1)}{1-q_p^{-(s+1)}}.
 \tag{3.5}
\]

The Euler product \(K\) is a holomorphic unit throughout \(\Re s>-1\).
Indeed, on \(\Re s\ge-1+\delta\), each local ratio is

\[
 1+\frac{q_p^{-(s+1)}}{(q_p+1)(1-q_p^{-(s+1)})}
       =1+O_\delta(q_p^{-1-\delta}).
 \tag{3.6}
\]

Both numerator and denominator are nonzero there. Normal convergence
of the logarithms outside finitely many primes proves the assertion;
it also bounds \(K\) uniformly in height on smaller closed half-planes.

On any fixed line \(\Re s=\beta-1+\epsilon_0>-1\), the finite product
over \(p\mid r\) is \(O_{\epsilon_0,\epsilon}(q_r^\epsilon)\).
For sufficiently large primes every factor is at most \(q_p^\epsilon\),
and the remaining finite prime set contributes one fixed constant.
This estimate is uniform in \(\Im s\).

Write \(\widehat W(s)=\int_0^\infty W(x)x^{s-1}\,dx\).
Mellin inversion initially on a positive line gives

\[
 A_{r,W}(B)=\frac1{2\pi i}\int\widehat W(s)B^sA_r(s)\,ds.
\]

Shift to \(\Re s=\beta-1+\epsilon_0\), with sufficiently small
\(\epsilon_0>0\). The integrand has no pole in the crossed strip:
the pole of \(Z_3\) gives a zero, and (3.1) excludes reciprocal poles.
Repeated integration by parts gives rapid vertical decay of
\(\widehat W\), while (3.5) gives polynomial vertical growth with the
stated \(q_r^\epsilon\) cost. The shifted integral is (3.3), after
allocating the small losses within the requested \(\epsilon\).
\(\square\)

### The exact coherent mark used in a mixed block

For smooth compactly supported \(W_M,W_S\), consider the finite sum

\[
 \sum_c\widetilde g(c)\psi_r(c)
   \sum_{a\mid c}\mu_E(a)W_S(q_a/N)W_M(q_c/(Dq_a)).
 \tag{3.7}
\]

There is no replacement of its divisor sum by the complete
\(\mu*1\) identity. Define its \(5/6\)-residue contribution by the
finite sum of residues obtained after Mellin inversion of \(W_M\).
Proposition 2.1 gives this contribution exactly as

\[
 \mathcal R_r(D,N)=R_rD^{5/6}\widehat W_M(5/6)
      \sum_{(a,r)=1}\mu_E(a)w(a)q_a^{5/6}W_S(q_a/N).
 \tag{3.8}
\]

Apply Theorem 3.1 to \(x^{5/6}W_S(x)\). With \(Y=DN\),

\[
 \boxed{|\mathcal R_r(D,N)|
 \ll_{\epsilon,W_M,W_S}
 q_r^{-1/6+\epsilon}Y^{5/6}N^{\beta-1+\epsilon}.}
 \tag{3.9}
\]

For the candidate input \(\beta=B_\flat\), the saving in the marked
length is \(N^{-0.125113352960035\ldots+\epsilon}\). This numerical
specialization has the status of that source-dependent input.

Equation (3.9) bounds a **specified residue contribution** of (3.7).
The remaining contour and dual sum must still be controlled; this is
not a bound of (3.7) itself, and it is not the complete mixed mean.

## 4. Sparse sextic lifts of the residue

The residue estimate can also be averaged before taking absolute
values of an entire theta reflection. Let \(\kappa=2\) or \(4\), and
index the explicit family by

\[
 u=r^\kappa b^6,\qquad r\text{ squarefree},\quad b\text{ arbitrary}.
 \tag{4.1}
\]

This decomposition is unique in its indicated family; common primes
of \(r,b\) are allowed. The associated cubic row is \(\psi_r\), with
the additional zero extension \((c,b)=1\). Write its residue as
\(R_{r;b}\). Proposition 2.1 gives

\[
 R_{r;b}=R_r\prod_{\substack{p\mid b\\p\nmid r}}
                      \frac{q_p}{q_p+1},\qquad
 |R_{r;b}|\le C_Eq_r^{-1/6}.
 \tag{4.2}
\]

For \(H\ge2\), elementary ideal counting in the fixed quadratic field
therefore proves

\[
 \boxed{
 \sum_{q_{r^2b^6}\le H}|R_{r;b}|^2\ll_E H^{1/3},\qquad
 \sum_{q_{r^4b^6}\le H}|R_{r;b}|^2\ll_E H^{1/6}\log(2H).}
 \tag{4.3}
\]

Indeed the number of \(b\) of norm at most \(T\) is \(O_E(T)\) for
\(T\ge1\). The left side for general \(\kappa\) is at most a constant
times

\[
 H^{1/6}\sum_{q_r\le H^{1/\kappa}}
                       q_r^{-(\kappa+2)/6}.
 \tag{4.4}
\]

Partial summation of the same ideal-counting bound gives respectively
\(O(H^{1/6}H^{1/6})\) and \(O(H^{1/6}\log(2H))\). Dropping
squarefreeness in this upper bound is harmless.

For a normalized smoothed cubic block \(X^{-1/2}\sum_c\cdots W(q_c/X)\),
the residue is \(X^{1/3}\widehat W(5/6)R_{r;b}\). Its contribution to
the two squared means is consequently

\[
 \ll_W X^{2/3}H^{1/3},\qquad
 \ll_W X^{2/3}H^{1/6}\log(2H).
 \tag{4.5}
\]

The weaker first bound is already at most \(H\) when \(X\le H\), and
at most \(X\) when \(H\le X\). Thus a resonant residue is not, merely
by being nonzero, an obstruction to the size of an unmarked inverse
second moment. Its sparse row support and conductor decay matter.

The choice between the two lifts in a particular sextic source depends
on that source's cubic/sextic orientation. Formula (4.3) proves both
explicit families; it does not silently identify all of Liu's labeled
row states with either one.

## 5. What this advances, and what it does not

The previous angular continuation removes a constant term by a nonzero
angular or balanced radial phase. That mechanism fails at the spherical
resonance. The result here retains the spherical residue, proves its
exact native divisor law, and gives two quantitative ways to control it:
sparse-row averaging and a power saving under the actual short Mobius
mark. The latter uses exactly the reciprocal-zeta zero-free information
already available as an input; no new nonvanishing hypothesis is hidden
in a positive surrogate.

To extend the complete unitary theorem one still has to derive the
corresponding all-field residue, with the finite \(S\)-profiles, unit
sectors, labels, active selected primes, and every reflection state, then
insert it through the source norm induction and detector continuation.
To improve the universal boundary or prove RH one must additionally
improve the binding mixed/long-inverse estimates. These obligations are
not discharged by (3.9) or (4.5).
