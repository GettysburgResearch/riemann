# An estimated overlap and an exact remaining corner

**Status: source-dependent overlap theorem and exact reduction.** This
note proves an estimate for an intersection of the original-product and
reduced-ratio decompositions. It does not infer an intersection estimate
from two bounds for its larger sets. Together with `MIDDLE_JOINT.md`, it
leaves a specified coherent corner. That corner remains unestimated.
Consequently no new unconditional zero-free region or RH proof is claimed.

Write

\[
 D=U^r,\qquad 29/25\le r\le117/100,\qquad
 e_0(r)=\frac{1+5r}{6}.
\]

Use the exact asymmetric smooth identity from the third pass, with
\(y_1=U^{2/125}\), \(y_2=2D/U^{2/125}\). In its full reflected
expression, let \(R\) denote the norm of the original outer product and
\(a\) the numerator after reducing the ratio of the original outer ideal
and the ordinary dual ideal. Thus \(Na\le R\) on every individual term.

For one fixed nonincreasing smooth cutoff \(\chi\), equal to one
through one and zero from two onward, the overlap treated here is

\[
             G(R)=1-\chi(R/U),\qquad
             K(a)=\chi(Na/U^{17/20}).
\]

Its coherent squared row norm satisfies

\[
 \boxed{\quad
 \sum_u w_U(u)|M_{KG,u}|^2
 \ll_\epsilon U^{\mathcal E(r)-3/80+\epsilon}
                     (1+|t|)^A p_J(W)^2,
 \qquad
 \mathcal E(r)=\frac83+\frac{5r}{2}
                         -\frac{10}{\sqrt6}\sqrt r.
 \quad}                                                     \tag{1}
\]

The saving over \(e_0(r)\), throughout the displayed interval, is at
least

\[
 \boxed{\quad
 \sqrt{\frac{58}{3}}-\frac{211}{48}
    =0.00113531942430639031\ldots >\frac1{1000}.
 \quad}                                                     \tag{2}
\]

All original outer products up to their true smooth support \(8D\) are
retained in this overlap, including those that vanished only after the
complete ordinary sum in the primal expression. Those terms cannot be
discarded after inserting the ratio selector.

## 1. Scope, sources, and exact expressions

Use the physical sixth-power-free Eisenstein rows, including their
nonsquarefree members; finite ray presentations; either common sextic
orientation; nonprincipal primitive inducing characters; and a common
puncture of polynomial radical from `third-pass/GCD_FOURTH_COMPONENT.md`.
The permitted twists are finite-order ray twists and norm heights. There
is no assertion for nonzero angular twists from a scalar cap.

The imported analytic premises are the finite-order family and scalar
\(7/8\) caps from
`openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`,
Git blob `268c4e3206d460c617d3d2129742a72b831b3def`, its native inverse
moment and ordinary functional equation calculus, and the buffered
physical-row counts of Xu--Sang,
[arXiv:2610.17675v2](https://arxiv.org/html/2610.17675v2), Lemma 6.2
and Proposition 6.3. The complete external framework is not independently
certified in this deduction. `MIDDLE_JOINT.md` proves the same-bin
coefficient/ordinary-block estimate used in Section 4 below.

Set

\[
 A(r_0)=\sum_{h_1h_2=r_0}\mu_E(h_1)\mu_E(h_2)
         w_0(Nh_1/y_1)w_0(Nh_2/y_2),\qquad y_1y_2=2D.       \tag{3}
\]

The two factors need not be coprime. In particular their repeated-prime
contributions are included. The original coefficient is supported on
\(Nr_0<8D\), and this complete support is retained below.

Write \(\psi_u^*\) for the primitive inducing character, \(q_u\) for
its conductor scale, and \(Q_s\) for the common deleted radical in a
fixed bad-place sector, including every redundant natural zero. Put
\(P_u=\operatorname{rad}(\mathfrak f_uQ_s)\). For a common original
outer weight \(J(R)\), define

\[
 C^J_a(P)=\sum_{(d,P)=1}\frac{A(ad)}{Nd}J(NaNd).             \tag{4}
\]

For a common reduced-ratio weight \(F\), the exact component is

\[
\begin{split}
 M_{FJ,u}={}&-\varepsilon_u\sqrt{D/q_u}
 \sum_a\frac{\psi_u(a)C^J_a(P_u)}{Na}F(Na)
 \sum_{e\mid Q_s}\frac{\mu_E(e)\psi_u^*(e)}{Ne}\\
 &\qquad\times
 \sum_{b:(a,b)=1}\overline{\psi_u^*(b)}
       \Phi_t\!\left(\frac{NbD}{q_uNaNe}\right).
\end{split}                                                 \tag{5}
\]

The same phase cancellation as in the third pass proves (5): for
\(r_0=da,n=db,(a,b)=1\),
\(\psi_u(da)\overline{\psi_u^*(db)}
=\psi_u(a)\overline{\psi_u^*(b)}1_{(d,P_u)=1}\).
In particular \(b\) is not given a false \(Q_s\) mask, and the e
coefficient in (5) uses the primitive value, which need not vanish.
All sums over a, d and e are finite, and the ordinary dual tail is
absolutely convergent.

The unweighted expression is the native inverse: \(M_{1,1,u}=M_u\).
The original far piece is \(M_{1,G,u}\). The overlap in (1) is
\(M_{K,G,u}\). Formula (5) defines the actual intersection before a
norm is taken; it is not a product of norm estimates.

## 2. A common three-variable Mellin representation

We prove a general coefficient estimate with
\(G_T(R)=1-\chi(R/T)\), where T is a prescribed bounded power of U.
Let \(7/8<\beta<1\), \(\theta=1-\beta\), and choose a small fixed
\(\eta>0\). Write

\[
 F_P(v)=\zeta_E(v)^{-1}
             \prod_{p\mid P}(1-(Np)^{-v})^{-1}.              \tag{6}
\]

The scalar cap and the logarithmic reciprocal argument from
`third-pass/GCD_NATIVE_COEFFICIENT.md`, Section 4, give

\[
 |F_P(\beta+i\tau)|\ll_{\beta,\epsilon}
                 (NP(3+|\tau|))^\epsilon.                  \tag{7}
\]

Let \(\mathfrak b_a(s,z)\) be exactly the common multiplicative
coefficient from that note and `GCD_FOURTH_COMPONENT.md`, not a new
arbitrary sequence. It is cubefree-supported. At a prime of norm q,
with \(x=q^{-s},y=q^{-z},\Delta=(1-x/q)(1-y/q)\),

\[
 \mathfrak b_1=1,\qquad
 \mathfrak b_p=-\frac{x+y-xy/q}{\Delta},\qquad
 \mathfrak b_{p^2}=\frac{xy}{\Delta}.                        \tag{8}
\]

Every prime in a is coprime to P on the true natural support. For
\((a,P)=1\), one has the exact common-contour formula

\[
\boxed{
\begin{split}
 C^{G_T}_a(P)=\frac1{(2\pi i)^3}
 \int_{(\eta)}\!\int_{(\eta)}\!\int_{(-\theta-\eta)}
 &\widehat w_0(s)\widehat w_0(z)\widehat G(h)
       y_1^s y_2^z T^h\\
 &\times F_P(1+s+h)F_P(1+z+h)
              \mathfrak b_a(s+h,z+h)\,dh\,dz\,ds,
\end{split}}                                                 \tag{9}
\]

where \(G(x)=1-\chi(x)\) and \(\widehat G(h)\) is its Mellin
transform on \(\Re h<0\). This transform is holomorphic there and
rapidly decreasing on fixed vertical lines. Indeed
\(\widehat G(h)=-\widehat\chi(h)\) on that half-plane, with the
continued transform of the low cutoff. Its possible pole is at zero,
outside the shifted h contours.

To verify (9), start with \(\Re s=\Re z=1\) and
\(\Re h=-\eta/2\), taking \(\eta<1\). Mellin inversion of the
three original cutoffs is then absolutely convergent. The factor
\((Nr_0)^{-h}\) shifts *both* convolution variables: if
\(A_{s,z}(r_0)=\sum_{h_1h_2=r_0}\mu(h_1)\mu(h_2)
(Nh_1)^{-s}(Nh_2)^{-z}\), then

\[
             (Nr_0)^{-h}A_{s,z}(r_0)=A_{s+h,z+h}(r_0).       \tag{10}
\]

The original scalar harmonic identity therefore gives exactly the
two factors F and \(\mathfrak b_a\) in (9). No additional power of
Na remains outside \(\mathfrak b_a\). Equivalently, in the explicit
three-way prime allocation, replacing the gcd weight by
\((Nd)^{-1-h}\) multiplies its local coefficient by
\((Na)^h\); this cancels the separately introduced \((Na)^{-h}\).
For a prime and a prime square this is precisely (8) with
\(x,y\) replaced by \(xq^{-h},yq^{-h}\).

First move s and z to \(\Re s=\Re z=\eta\), keeping
\(\Re h=-\eta/2\). Their real parts stay positive, so neither
cutoff pole at zero is crossed. Next move h to
\(-\theta-\eta\). The two reciprocal arguments then have real
part beta; they remain in the scalar zero-free region throughout.
The h path remains strictly negative. The finite Euler denominators
in \(\mathfrak b_a\) are nonzero because their arguments have
positive real part. The reciprocal's zero at its scalar zeta pole
causes no singularity. Thus no residue is crossed in these moves.

Rapid decay of all three cutoff transforms, (7), and the finite
Euler-factor bounds justify horizontal limits and absolute convergence.
Here \(\eta,\beta\) are fixed before the scale limit. Their small
power costs are reserved inside the final epsilon.

On the contours of (9),
\(\Re(s+h)=\Re(z+h)=-\theta\), exactly the lines of the old
coefficient theorem. Moreover,

\[
 |y_1^sy_2^zT^h|=(2D)^\eta T^{-\theta-\eta},\qquad
 |\mathfrak b_a(s+h,z+h)|\ll d_E(a)^C(Na)^\theta.           \tag{11}
\]

Consequently

\[
 \boxed{\quad
 |C^{G_T}_a(P)|\ll (2+UDNQ)^\epsilon
                         (Na/T)^{1-\beta}.
 \quad}                                                     \tag{12}
\]

More importantly, (9) separates its row mask. All P-dependence is in
the bounded row scalars \(F_P(1+s+h)F_P(1+z+h)\). The same common
column coefficient \(\mathfrak b_a\) as in the complete gcd theorem
remains. Formula (12) alone would not justify a family moment.

## 3. The exact k weight and the bin estimate

Insert a common smooth dyadic window \(Na\asymp B\) in (5), with
\(J=G_T\), and invert its remaining coprimality exactly:

\[
 1_{(a,b)=1}=\sum_{k\mid a,b}\mu_E(k),\qquad a=kA,\ b=kB'.
\]

The fixed-k term has weight
\(\mu_E(k)(Nk)^{-1}1_{(k,P_u)=1}\), the coefficient
\(C^{G_T}_{kA}(P_u)\), and the ordinary dual scale
\(q_uNA\,Ne/D\). There is no additional k in that scale.
These are the exact normalizations of equation (8) in
`third-pass/GCD_FOURTH_COMPONENT.md`. The weight is \(1/Nk\),
not \(1/\sqrt{Nk}\).

Let \(R_1=B/Nk\). Substitution of (9) into the fixed-k outer block
uses the identical local factors
\(\mathfrak b_p+\mathfrak b_{p^2}\psi_u(p)(Np)^{-w}\) for
\(p\mid k\) and
\(1+\mathfrak b_p\psi_u(p)(Np)^{-w}
+\mathfrak b_{p^2}\psi_u(p)^2(Np)^{-2w}\) otherwise.
No possibly vanishing \(\mathfrak b_p\) or correction polynomial
is inverted. The same absolutely convergent correction and incomplete
ordinary reciprocals as in that theorem therefore apply.

On a buffered bin with \(\delta=2a_\circ-1\), its coefficient
argument gives

\[
 \left|R_1^{-1/2}\sum_A C^{G_T}_{kA}(P_u)\psi_u(A)
                                  V(NA/R_1)\right|
 \ll (B/T)^\theta R_1^{\delta/2}
                   (Nk)^\epsilon U^\epsilon\,\mathcal P,   \tag{13}
\]

where \(\mathcal P\) denotes fixed profile seminorms and polynomial
norm-height costs. The only change from the old proof is the real
scalar factor: \(D^{-\theta}\) is replaced by
\((2D)^\eta T^{-\theta-\eta}\). Its k local factors still cost
\((Nk)^{\theta+\epsilon}\), and its R_1 Mellin shift costs
\(R_1^{\theta+\delta/2}\), giving (13).

All three Mellin frequencies in (9) use one shared buffered height.
In particular the actual reciprocal arguments contain s+h and z+h;
one must not spend independent full buffers on s,z,h. First truncate
their joint absolute values and the profile frequencies inside one
fixed fraction of the licensed buffer. Keep the scalar s,z,h variables
on the already established contours (9). Bound their complementary
large-frequency tails using the finite outer polynomial and the trivial
bound for \(\mathfrak b_a\), with the family's own w integral on its
absolute line. The scalar cutoff transforms decay rapidly there and
(7) is global in height. Choose those external decay orders after the
fixed source and moment orders. Only the remaining low-frequency
family w integral undergoes the buffered shift. No deformation of a
frequency-truncated scalar integral is asserted, and the family
zero-free rectangle is not extended to greater heights.

## 4. Same-bin overlap bound

The exact inverse ordinary functional equation in the fixed-k term
returns the original natural ordinary block at scale \(D/R_1\),
with every e factor retained. Common profile separation, the coefficient
bound (13), and the ordinary pointwise estimate on the **same** buffered
bin give

\[
 |\hbox{fixed-k component}|\ll
 (Nk)^{-1+\epsilon}(B/T)^\theta
 R_1^{\delta/2}(D/R_1)^{\delta/2}
 U^\epsilon\,\mathcal P
 = (Nk)^{-1+\epsilon}(B/T)^\theta
 D^{\delta/2}U^\epsilon\,\mathcal P .                       \tag{14}
\]

This uses the same-bin mechanism proved in `MIDDLE_JOINT.md`; the
ordinary factor has its actual scale \(D/R_1\), so its length and
the inverse length add to r. Nonempty k satisfy \(Nk\ll B\).
The harmonic k sum costs only a logarithm and the reserved subpower.

Above-floor bins have count
\(U^{\mathcal R(\delta)+\epsilon}\), where
\(\mathcal R(\delta)=(15-16\delta)/(15-6\delta)\) and
\(0\le\delta\le3/4\). The bottom bin contributes
\(U^{1+r/50+\epsilon}\). Therefore the coherent dyadic overlap
obeys

\[
 \boxed{\quad
 J^{G_T}_B\ll (B/T)^{1/4}
       U^{\mathcal E_{.51}(r)+\epsilon}\mathcal P^2,
 \quad}                                                     \tag{15}
\]

by taking beta sufficiently close to \(7/8\). The small losses
are absorbed after the bounded scale ranges have been fixed. The
envelope and its printed \(.51\) floor are exactly those of the
third pass; no adjustable floor is needed.

For \(29/25\le r\le117/100\), the displayed radical branch in
(1) dominates the bottom-bin line. Indeed this interval lies in
\([2/3,200/147]\); \(\mathcal E\) is increasing there, and
\(\mathcal E(29/25)>16/15>1+(117/100)/50\).
Apply (15) with T=U and sum smooth dyadic **norms** through
\(B\ll U^{17/20}\). The positive B exponent makes the sum
geometric up to fixed endpoint factors. This proves (1) for the
coherent smooth selector, including its transition.

For completeness, the gap is increasing in r on this interval:

\[
 \frac{d}{dr}\{e_0(r)-\mathcal E(r)+3/80\}
      =-\frac53+\frac5{\sqrt{6r}}>0\qquad(r<3/2).
\]

At r=29/25 it equals the radical in (2). Its comparison with
\(1/1000\) is exact:

\[
 \frac{58}{3}-\left(\frac{26381}{6000}\right)^2
                         =\frac{42839}{36000000}>0.         \tag{16}
\]

The two compared square roots are positive, and
\(26381/6000=211/48+1/1000\).

## 5. One complete remaining corner and its consumer

Set

\[
 H(a)=\chi(Na/(2U)),\qquad
 K(a)=\chi(Na/U^{17/20}),\qquad G(R)=1-\chi(R/U).            \tag{17}
\]

On every individual reflected term, \(Na\le R\). If \(1-G(R)\)
is nonzero then \(R<2U\), and hence \(H(a)=1\). Therefore

\[
 (1-H(a))(1-G(R))=0,\qquad 0\le K(a)\le H(a)\le1.          \tag{18}
\]

The exact algebraic identity

\[
 1=H+G-HG=H+G-KG-(H-K)G
\]

now gives the **coherent identity**

\[
 \boxed{\qquad
 M_u=M_{H,1,u}+M_{1,G,u}-M_{K,G,u}-M_{H-K,G,u}.
 \qquad}                                                   \tag{19}
\]

Every summand in (19) is defined by the same complete reflected
expression (5), so all masks, primitive conductors, profiles, signs,
and otherwise primal-zero outer products agree. No Hilbert-space
orthogonality is asserted or needed for this identity.

The first term has the general same-bin full-ratio-head bound proved in
`MIDDLE_JOINT.md`, with cutoff \(2U\). The fixed factor two changes
only its profile constant. Its exponent is
\(\mathcal E(r)+(1-r)/4\le\mathcal E(r)-1/25\), which is
smaller than the overlap exponent in (1). The second has the
\(1/750\) saving of `third-pass/ASYMMETRIC_HB_TAIL.md`. The third
has the strictly greater than \(1/1000\) saving (1)--(2). Thus the
only new estimate needed in this decomposition is

\[
 \sum_u w_U(u)|M_{\mathrm{corner},u}|^2
  \ll_\epsilon U^{e_0(r)-1/1000+\epsilon}
                         (1+|t|)^A p_J(W)^2,\qquad
 M_{\mathrm{corner},u}=M_{H-K,G,u}.                          \tag{C}
\]

Its support is precisely constrained by

\[
       R>U,\qquad U^{17/20}<Na<4U,\qquad Na\le R,
                                                               \tag{20}
\]

with the smooth weights (17), the original asymmetric short-factor
cutoffs, and the full support \(R<8D\) retained. This is an
intersection near the ratio threshold, not the original middle band.

**Hypothesis (C) remains open.** If it holds, the triangle inequality
in (19) gives the complete native \(1/1000\) saving. The unchanged
certified consumer in `third-pass/CONDITIONAL_CONSUMER.md` then gives
the conditional boundary \(\operatorname{Re}s>0.8748856\), within
its stated finite-order Eisenstein framework and its base-change
consequences. No new arithmetic claim is inserted into that consumer.
Conversely, the complete native saving and the three proved component
bounds imply the same saving for this corner by (19). Thus the corner
is an exact sufficient target, and is equivalent at this exponent
modulo the three established terms.

### Exact return of the corner coefficient

The newly estimated overlap also permits a quantitative check of what
is left. For any weights F,J define the returned primal coefficient

\[
 D_{F,J,P}(m)=\sum_{(k,P)=1}\frac{\mu_E(k)}{Nk}
                         C^J_{km}(P)F(NkNm).               \tag{21}
\]

The same inverse ordinary functional equation as in the third pass
returns (5) with this coefficient and the original natural ordinary
factor. In particular,

\[
             D_{1,J,P}(m)=A(m)J(Nm),                       \tag{22}
\]

because substitution of (4) groups \(v=kd\) and leaves
\(\sum_{k\mid v}\mu_E(k)=1_{v=1}\). All sums are finite and the
true \((k d,P)=1\) condition remains.

By (19), the exact returned corner coefficient is consequently

\[
 \boxed{\quad
 D_{H-K,G,P}(m)=D_{H,1,P}(m)-D_{K,G,P}(m)
                              -A(m)\chi(Nm/U).
 \quad}                                                     \tag{23}
\]

The complete coefficient bound from the third pass and (12), followed
by harmonic ideal counting in (21), give on \((m,P)=1\)

\[
 |D_{H,1,P}(m)|\ll Z^\epsilon(2U/D)^\theta,\qquad
 |D_{K,G,P}(m)|\ll Z^\epsilon(U^{17/20}/U)^\theta,
 \quad Z=2+UDNQ.                                          \tag{24}
\]

For example, choose \(\beta=22/25\), \(\theta=3/25\), and then
choose the small losses after the prescribed puncture-radical range.
The two bare exponents are at most \(-12/625\) and \(-9/500\),
respectively. Since both are strictly below \(-1/60\), (23) gives

\[
 \boxed{\quad
 D_{H-K,G,P_u}(m)=-A(m)\chi(Nm/U)+O(U^{-1/60}).
 \quad}                                                     \tag{25}
\]

For squarefree m with \(Nm\le\min(U,y_2)\),
\(A(m)=\mu_E(m)\sum_{a\mid m}w_0(Na/y_1)\), whose divisor
sum is at least one. Thus the old critical primal coefficients at
exponent \(.7456999427\ldots\) occur in the returned corner with
their opposite sign, up to the small error (25). This is a coefficient
identity and estimate, not a lower bound for the subsequent signed sum
or a claim of actual moment saturation.

In particular, (20) does not imply that the returned primal inverse
variable has norm greater than U. The corner has genuine remaining
content despite its restricted support in the two original reflected
variables. Any argument using the stronger primal support claim would
need a further estimate.

## 6. Checks and limits

`check_coherent_identity.py` checks the exact local Mellin shift (10),
the original harmonic Euler allocation with nontrivial prime masks,
finite gcd grouping with the original natural and primitive characters,
the coherent identity (19), and the returned coefficient (23). It checks the exact rational radical
margin (16) and interval conditions. Negative controls delete the
overlap term or remove the gcd's natural coprimality mask.

The tests are finite algebra in a free-prime/integer model and exact
exponent comparisons. They do not prove the external analytic premises,
the Mellin shifts, the uniform buffered argument, or (C). The theorem
proved here is the actual overlap estimate (1), with the common
three-Mellin representation that licenses its family use, and the
exact remaining-corner reduction (19).
