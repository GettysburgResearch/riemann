# Complete prime-divisor marks: exact transfer and the remaining exponent

Date: 2026-10-20. This is a source-dependent marked-polynomial adapter.
It does not prove a smaller zero-free boundary.

## 1. Analytic input and conventions

The abstract input is a uniform selected inverse estimate, with exact
natural zeros, a common-profile convention and finite height seminorms.
In logarithmic lengths its two strict inequalities are
\[
r+2z<m,\qquad 2r+8z<3m.                 \tag{1.1}
\]
It bounds the squared mean of a central inverse polynomial of length
\(Z^r\) times a product of prime polynomials of total length \(Z^z\),
over all nonzero rows of norm at most \(Z^m\), by \(Z^{m+\epsilon}\).
The prime coefficients can be bounded fixed coefficients, independent
of the row and other columns. The number of positions is fixed.

The family must also have the source's exact sixth-power presentation
law
\[
\psi_{ua^6}(n)=\psi_u(n)\mathbf1_{(n,a)=1}.
\]
The row parametrization retains finite unit sectors and bounded
multiplicity, and its common scale-supremum/profile measures must support
the sixth-power amplification used in §3, uniformly under fixed
punctures and surviving prime sublists. These are explicit analytic
hypotheses; multiplicativity alone does not prove a selected inverse
estimate.

For fixed fields \(F\supseteq\mu_{12}\), the coefficient families proved
in the preceding packet supply these hypotheses: see
[ANGULAR_THETA_AND_INVERSE.md, §7](../2026-10-20-angular-hecke-continuation/ANGULAR_THETA_AND_INVERSE.md)
and its stated source inputs. Thus §§2–3 give a source-dependent theorem
for those families.

The Eisenstein field \(E=\mathbb Q(\omega)\) in rStation paper 5 does
not contain \(\mu_{12}\). That paper's unmarked angular inverse theorem
does not by itself supply the selected estimate (1.1) over \(E\).
Its local angular reflection is compatible with the proposed extension,
but the selected recursion, finite ray reciprocity and uniform common
measures still require a separate proof there. We do not assert this
field bridge. The Eisenstein Gauss consumer in §4 is consequently
conditional on the same selected-M1 and amplification hypotheses being
proved over \(E\); it is not a completed solution of rStation §13.

Write
\[
M_u(Y;W)=\sum_n\frac{\mu(n)\psi_u(n)}{\sqrt{Nn}}W(Nn/Y).
\]
This differs from a normalization \(Y^{-1/2}\sum\mu\psi W\) only by the
fixed annular test factor \(x^{-1/2}\). Every zero extension is literal.

Let \(\mathcal P_i\) be disjoint fixed-ratio prime windows of norm length
\(P_i\), with fixed bounded coefficients \(\eta_i(p)\). Set
\[
A_i(n)=\sum_{\substack{p\in\mathcal P_i\\p\mid n}}\eta_i(p),
\quad L=\prod_iP_i,
\quad \mathcal A(n)=\prod_i(A_i(n)+c_i),                  \tag{1.2}
\]
where the constants are bounded by subsidiary powers of the common
polynomial-size parameters, with the power allocated within the
requested \(\epsilon\) loss (for example, fixed divisor bounds).
The assertions below also allow all
surviving sublists. No mark is allowed to depend on the varying row
except through a separately expanded bounded row multiplier.

## 2. Exact extraction of every mixed term

For a subset \(J\) of positions, the identity is
\[
\begin{split}
&\sum_n\frac{\mu(n)\psi_u(n)}{\sqrt{Nn}}
       \prod_{i\in J}A_i(n)W(Nn/Y)\\
&\quad=(-1)^{|J|}\sum_{\substack{p_i\in\mathcal P_i\\r_i\ge1\ (i\in J)}}
 \left(\prod_{i\in J}
       \frac{\eta_i(p_i)\psi_u(p_i)^{r_i}}{(Np_i)^{r_i/2}}\right)
 M_u\left(Y/\prod_{i\in J}(Np_i)^{r_i};W\right).          \tag{2.1}
\end{split}
\]
The character in the last inverse polynomial is the original character;
its column is not falsely punctured at \(p_i\). Those repeated-prime
terms are exactly what restores the squarefree Möbius coefficient.

To prove (2.1), at a selected prime set \(x=\psi_u(p)(Np)^{-s}\).
Multiplication of the inverse Euler factor \(1-x\) by a prime-divisor
mark replaces it by \(-\eta(p)x\). Their quotient is
\(-\eta(p)x/(1-x)\). Expand it geometrically. Disjoint prime windows
make the selected primes distinct, so multiplication gives (2.1).
If \(\psi_u(p)=0\), the entire marked contribution at that prime is zero
on both sides. Annular support makes the identity finite for each row.

Expanding \(\mathcal A(n)\) in (1.2) over all subsets \(J\) proves the
complete product identity, including every constant/mark mixed term.
It is not enough to keep only the product of the nonconstant marks.

When \(r_i=1\) at each surviving position, one common smooth separation
in \(Nn/(Y/L_J)\) and \(Np_i/P_i\), made before fixing the tuple, gives
the selected inverse product with lengths
\[
D=Y/L_J,\qquad \prod_{i\in J}P_i=L_J.
\]
Here the profile and the central roots are separated together. This
retains the actual scale \(Y/\prod Np_i\), rather than replacing a
tuple-dependent sharp selector by a new arithmetic coefficient.

For a position with \(r_i\ge2\), the absolute outside mass is bounded:
\[
\sum_{p\in\mathcal P_i}\sum_{r\ge2}(Np)^{-r/2}
 \ll P_i^\epsilon.                                      \tag{2.2}
\]
The original ideal/prime count and a geometric series prove this. Freeze
these primes and powers before applying Minkowski. Their row phases are
contractions and their column scales are shorter. Removing a position
with \(r_i\ge2\) decreases both expressions in (1.1), so the all-first-
power, full-subset term has the worst inequalities.

Consequently the full marked inverse polynomial has squared mean
\(T^{1+\epsilon}\) whenever, with fixed positive logarithmic margins,
\[
T>YL,\qquad T^3>Y^2L^6.                                 \tag{2.3}
\]
Common smooth profiles have fixed finite seminorm costs throughout.

## 3. Fixed punctures and exact sixth-power restoration

A fixed puncture \(Q\), independent of the row during the invocation,
can be removed before applying the preceding estimate. For the
unmarked inverse use the full supported-prime-power identity
\[
M^Q_u(Y)=\sum_{e:\,\operatorname{rad}e\mid Q}
 \frac{\psi_u(e)}{\sqrt{Ne}}M_u(Y/Ne),
\quad
\sum_e(Ne)^{-1/2}
=\prod_{p\mid Q}(1-(Np)^{-1/2})^{-1}\ll Q^\epsilon.      \tag{3.1}
\]
In the prime polynomial retain its original \((p,Q)=1\) restriction
in its bounded prime coefficient. This proves the required fixed-
puncture estimate by Minkowski; it does not reclassify a support moving
with the current row as fixed.

For sixth-power amplification there is also a *finite* restoration
identity. For a fixed amplification ideal \(a\), the original inverse
variable has the unique split \(n=dn_0\), with \(d\mid\operatorname{rad}a\)
squarefree and \((n_0,a)=1\). Hence
\[
\begin{split}
M_u^{\mathcal A}(Y)
={}&\sum_{d\mid\operatorname{rad}a}
 \frac{\mu(d)\psi_u(d)}{\sqrt{Nd}}\sum_{J\subseteq I}
       \left(\prod_{i\notin J}A_i(d)\right)\\
&\hspace{12mm}\cdot
 M_{ua^6}^{\prod_{i\in J}(A_i+c_i)}(Y/Nd).               \tag{3.2}
\end{split}
\]
This uses \(A_i(dn_0)=A_i(d)+A_i(n_0)\) on the actual disjoint support.
All original common masks are retained. In particular the expansion
also restores prime factors that meet the amplification ideal; they
cannot simply be omitted.

For fixed position count, \(A_i(d)\) is divisor bounded, and
\(\sum_{d\mid a}(Nd)^{-1/2}\prod_i(1+|A_i(d)|)\ll a^\epsilon\).
Thus (3.2) has subpower absolute coefficient mass. The shortened scale
is handled by the same common scale-supremum measure as in the source
inverse amplification, not by multiplying separately averaged suprema.

Put
\[
H_0=\max\{YL,Y^{2/3}L^2\}.                              \tag{3.3}
\]
Choose a slightly larger power \(H\ge\max(2T,H_0^{1+c})\) so that (2.3)
has fixed strict margins at row width \(H\), and average (3.2) over
\(Na\ll(H/T)^{1/6}\). For sixth-power-free original rows the map
\((u,a)\mapsto ua^6\) has bounded multiplicity with the original finite
unit sectors retained. The averaging density is \((T/H)^{1/6}\).
The common divisor and scale measures cost only subsidiary powers.
Applying (2.3), and then taking \(c\) small within the requested loss,
gives
\[
\boxed{\quad
\sum_{\substack{u\ {\rm sixth\text{-}power\text{-}free}\\Nu\le T}}
 |M_u^{\mathcal A}(Y)|^2
\ll (TYLQ)^\epsilon
 \left[T+T^{1/6}\max\{YL,Y^{2/3}L^2\}^{5/6}\right].
\quad}                                                   \tag{3.4}
\]

As usual, first take dyadic original rows, then sum the row dyads.
Decomposing a general nonzero row as \(vt^6\), keeping its full puncture
at \(t\), extends the same bound to all nonzero rows. The two resulting
sums use \(\sum_t(Nt)^{-6}<\infty\) and
\(\sum_{Nt\ll T^{1/6}}(Nt)^{-1}\ll\log(2T)\).

This proves a global bound, not only the cone (2.3). It gives no better
exponent than the unmarked bound and can be worse when \(L>1\).

## 4. Conditional Eisenstein consumer: the full marked sextic-Gauss image

In this section additionally assume that the analytic hypotheses of
§1 have been proved over the Eisenstein field for the inverse angular
modes appearing in rStation paper 5. Under that unproved bridge, use
the paper's §§10.2–10.3, with column coefficient
\(c_j(n)=\mu(n)\alpha(n)^j\gamma_{-1}(n)\nu(n)\) multiplied by
\(\mathcal A(n)\). The two squarefree gcd decompositions give
\[
A_i(gsx)=A_i(g)+A_i(s)+A_i(x),
\]
on their genuine pairwise coprime support. The complete product
therefore leaves precisely the marked inverse family in (1.2), with
new constants \(A_i(g)+A_i(s)+c_i\). These constants are divisor
bounded. All mixed terms are retained by §2.

Retain all the source's coefficient restrictions, in particular its
fixed \(j\ne1\); only modes satisfying both those restrictions and the
additional selected inverse hypothesis are covered. Take \(D,F\ge1\),
as usual up to bounded nonempty subunit scales.

The exact frequency is still \(k=hf^2d(g/d)^2\); the Gauss cancellation,
all natural zeros, and the divisor bound for its fibre are unchanged.
The surviving inverse column has length at most \(D\), the row scale is
\(T_0=D^2F^2/K\), and the outside normalization is \(K/(FD)\).
Inserting (3.4) gives the following first Poisson bound for the
normalized positive label average:
\[
\boxed{\quad
\mathcal J^{\mathcal A}_j(K,D,F;Q)
\ll (KDFLQ)^\epsilon\left[
K+DF+K^{5/6}F^{-2/3}
 \max\{D^{1/6}L^{5/6},D^{-1/9}L^{5/3}\}
\right].\quad}                                           \tag{4.1}
\]
The original diagonal is \(K\) up to small powers, because fixed
prime-divisor products are divisor bounded. Kernel tails and fixed
finite ray expansions are handled before the positive frequency
enlargement exactly as in the cited proof. If \(L=1\), (4.1) reduces to
the existing \(K+DF\) short estimate.

The complementary unmarked completed estimate in rStation §11 cannot
be inserted with an arbitrary marked coefficient. Its marks would
have to be retained through cube completion, their shared primes and
the reflected local factors. Formula (4.1) does not silently assert
such an unrestricted complementary theorem.

Source: https://rstation.ai/problems/riemann_hypothesis/papers/5

## 5. Exact native exponent substitutions

For a native inverse-times-prime product, let
\(D=U^r\), \(L=U^m\); its corresponding marked inverse column has length
\(Y=DL\). Formula (3.4), or the direct selected amplification with the
same full restoration, gives
\[
e_{\rm mark}(r,m)=
\max\left\{1,\frac{1+5\max\{r+2m,(2r+8m)/3\}}6\right\}. \tag{5.1}
\]

For every \(r\ge0\), the entire unmarked edge reduces exactly to
\[
e_{\rm mark}(r,0)=\max\{1,(1+5r)/6\},
\]
the previous pure inverse exponent. There is no positive saving anywhere
on this edge; all mark positions are absent.

At the illustrative nearby short inverse/plain scale \((r,m)=(0.746,0.418)\), even
the prime-supported subcase has
\[
r+2m=1.582,\qquad (2r+8m)/3=1.612,
\quad e_{\rm mark}=1.51.                                \tag{5.2}
\]
The already available general mixed Hölder exponent at that point is
\[
\min\{1+\kappa m,(2+\kappa r)/2\}
=1.279665438\ldots,
\qquad \kappa=2B_\flat-1.
\]
Thus (5.1) does not improve even this prime subcase at the relevant
lengths.

The native ordinary short factor has a coherent *arbitrary squarefree
divisor* weight, not a fixed finite product of the prime-divisor weights
in (1.2). Treating it as such would additionally require a complete
factorization and every resulting norm range. A single rough prime
divisor already has length \(U^m\) and exhibits the unfavorable
inequalities (5.2). Small-prime factorizable pieces do not cover that
complement.

Accordingly the selected angular inverse input closes the full
prime-divisor-polynomial transfer with the explicit loss (3.4) in
the families where §1 is available, including the cited
\(F\supseteq\mu_{12}\) families. Its exponent supplies no fixed gain
on the native long inverse edge or at the cited short prime subcase.
The full ordinary mixed estimate and the Eisenstein selected-M1 bridge
are separate missing inputs. The conditional Gauss calculation does
not remove either obligation.
