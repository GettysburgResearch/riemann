# Undoing a ratio cutoff retains the original low-product coefficients

**Status: exact return identity and a source-dependent coefficient
estimate; independent internal review recorded in `REVIEW_RATIO_CUTOFF_RETURN.md`.** This note settles the proposed
combination of the larger ratio head in `GCD_FOURTH_COMPONENT.md` with
the far original-product theorem in `ASYMMETRIC_HB_TAIL.md`.

The two estimates concern different decompositions. Undoing the ratio
selector does not preserve a lower bound for the length of an original
Möbius factor. More precisely, its complementary primal coefficient is

\[
       \boxed{\quad A_{y_1,y_2}(m)-H_{\chi,P}(m),\qquad
       |H_{\chi,P}(m)|\ll Z^\epsilon(B_0/D)^{1-\beta}.
                    \quad}                                  \tag{1}
\]

The error is uniform on the original natural support. Thus many
original low-product coefficients remain almost unchanged, including
those at the previously critical product scale. This is a statement
about exact coefficients and permissible decompositions. It is not a
lower bound for a signed polynomial or a row mean, and does not rule
out a new estimate of the complete remaining sum.

## 1. One common decomposition and all its zeros

Use the physical rows, natural presentation
\(\psi_u=\psi_u^*1_{(\,\cdot\,,Q_s)=1}\), fixed ray sector,
primitive conductor norm \(q_u\), nonprincipal hypothesis, and common
profile V of `GCD_NATIVE_COEFFICIENT.md`. Put

\[
                  P_u=\operatorname{rad}(\mathfrak f_uQ_s).
\]

Every fixed omitted prime is included in Q_s. All occurrences of
\(\psi_u^*\) below are primitive values, including their actual
zeros. A common growing puncture has polynomial radical, as in the
other component theorems. Since only its radical matters, take Q
squarefree throughout, so \(NQ\le U^{C_Q}\) for a prescribed fixed
\(C_Q\).

Choose the same smooth cutoff \(w_0\) used in the asymmetric identity,
and let \(y_1y_2=2D\). In its licensed range the two short linear
terms vanish on the original V annulus. Define

\[
 A(r)=A_{y_1,y_2}(r)
   =\sum_{ab=r}\mu(a)\mu(b)w_0(Na/y_1)w_0(Nb/y_2),
 \qquad
 C_a(P)=\sum_{(d,P)=1}\frac{A(ad)}{Nd}.                     \tag{2}
\]

The entire support \(Nr<4y_1y_2=8D\) is retained. The factors a,b
need not be coprime. No original product cutoff is imposed in (2).

For a bounded common function F and a scale B_0, multiply the reduced
numerator a in the exact gcd identity by \(F(Na/B_0)\). The resulting
coherent expression is

\[
\begin{split}
 M_{F,u}={}&-\varepsilon_u\sqrt{D/q_u}
  \sum_a\frac{C_a(P_u)\psi_u(a)}{Na}F(Na/B_0)
  \sum_{e\mid Q_s}\frac{\mu(e)\psi_u^*(e)}{Ne}\\
 &\hspace{10mm}\times
   \sum_{b:(a,b)=1}\overline{\psi_u^*(b)}
               \Phi\!\left(\frac{NbD}{q_uNaNe}\right).
\end{split}                                                  \tag{3}
\]

The finite a and e sums and the rapid dual tail make all the following
reorderings legitimate. The denominator b is not given a false
coprimality restriction with Q_s.

## 2. Exact inversion of the ratio selector

Expand the remaining coprimality by
\(1_{(a,b)=1}=\sum_{k\mid a,b}\mu(k)\), and write a=km,
b=kn. Complete multiplicativity with the natural zero extension gives

\[
 \psi_u(km)\overline{\psi_u^*(kn)}
 =\psi_u(m)\overline{\psi_u^*(n)}1_{(k,P_u)=1}.              \tag{4}
\]

The ratio in Phi becomes n/m; the only new scalar norm factor is
\(1/Nk\). Hence define

\[
\boxed{
 D_{F,P}(m)=\sum_{(k,P)=1}
       \frac{\mu(k)}{Nk}C_{km}(P)F(NkNm/B_0).
}                                                            \tag{5}
\]

Then (3) is precisely the usual reflected ordinary block with outer
coefficient \(D_{F,P_u}(m)\). Applying the inverse ordinary
functional equation, including the original e sum, gives the exact
primal identity

\[
\boxed{
 M_{F,u}=-D^{-1/2}\sum_{m,c}D_{F,P_u}(m)
          \psi_u(m)\psi_u(c)V(NmNc/D).
}                                                            \tag{6}
\]

There is no change of the original row, common profile, norm height,
or primitive conductor. The coefficient now depends on the row
through P_u, exactly as shown in (5).

In particular the e coefficient is still
\(\mu(e)\psi_u^*(e)/Ne\). It is not replaced by the natural
zero-valued \(\psi_u(e)\). The k character cancels in (4) only
on its true unit support, leaving \((k,P_u)=1\). No new
coprimality condition is added between the remaining dual quotient
and k or Q_s. The pre-existing e sum therefore restores the same
natural ordinary factor \(\psi_u(c)\) in (6), with no additional
e-dependent multiplier in (5).

There is a useful second form of (5). Substitute (2), write v=kd,
and sum over the divisors k of v:

\[
 D_{F,P}(m)=\sum_{(v,P)=1}\frac{A(mv)}{Nv}
            \sum_{k\mid v}\mu(k)F(NkNm/B_0).                 \tag{7}
\]

For the full selector F=1, the inner sum vanishes unless v=1. Thus

\[
                         D_{1,P}(m)=A(m).                   \tag{8}
\]

Equations (5)--(8) are finite arithmetic identities. They use no
zero-free hypothesis. They also show exactly why a ratio cutoff is
not an original-product cutoff: divisibility inversion replaces the
ratio numerator km by the shorter primal variable m, while the
character of k has canceled.

## 3. Quantitative persistence of the low primal coefficients

Let \(\chi\) be a fixed smooth function with values in [0,1], equal
to one on [0,1] and zero on [2,infinity). Write

\[
                     H_{\chi,P}(m)=D_{\chi,P}(m).
\]

The exact complement F=1-chi has

\[
                         D_{1-\chi,P}(m)=A(m)-H_{\chi,P}(m).
                                                                  \tag{9}
\]

This identity already contradicts a purely formal inference that
the returned coefficient is supported on \(Nm>B_0\).

The scalar coefficient estimate in `GCD_NATIVE_COEFFICIENT.md`
applies equally to the two unequal cutoffs in (2). For each fixed
\(\beta>7/8\), under that note's explicitly imported scalar
Dedekind-zeta cap,

\[
        |C_a(P)|\ll (NPD)^\epsilon (Na/D)^{1-\beta}
                          \qquad((a,P)=1).                 \tag{10}
\]

Indeed the exact three-way prime allocation is unchanged. The two
harmonic bounds contribute
\(y_1^{\beta-1}y_2^{\beta-1}=(2D)^{\beta-1}\), so equality
of the cutoff lengths was never needed for this pointwise estimate.
The harmonic formula is valid also at scales below one.

On the natural support \((m,P)=1\), formula (5) and (10) give

\[
\begin{split}
 |H_{\chi,P}(m)|
 &\ll Z^\epsilon (Nm/D)^{1-\beta}
            \sum_{Nk\le2B_0/Nm}(Nk)^{-\beta}\\
 &\ll_{\beta} Z^\epsilon (B_0/D)^{1-\beta},
                    \qquad Z=2+UDNQ.                       \tag{11}
\end{split}
\]

The last step is the ordinary ideal-counting estimate followed by
partial summation. If \(Nm\ge2B_0\), the left side is zero
directly. All masks in the finite k sum are merely discarded after
taking its absolute value; no arbitrary row-dependent sequence is
submitted to a family sieve in (11).

For the asymmetric cutoffs
\(y_1=U^{2/125}\), \(y_2=2D/U^{2/125}\), consider squarefree
m with \(Nm\le y_2\). Every divisor factorization m=ab is then
coprime, and the second cutoff is identically one. Therefore

\[
 A(m)=\mu(m)\sum_{a\mid m}w_0(Na/y_1),\qquad
                  \sum_{a\mid m}w_0(Na/y_1)\ge1.            \tag{12}
\]

On the natural unit support the high-ratio return consequently has

\[
 D_{1-\chi,P}(m)
    =\mu(m)\sum_{a\mid m}w_0(Na/y_1)
       +O\!\left(Z^\epsilon(B_0/D)^{1-\beta}\right).         \tag{13}
\]

In particular, its coefficient at m=1 is 1 plus that same small
error. More generally, when the error tends to zero, the real
coefficient in (13) retains the Möbius sign and has magnitude at
least 1-o(1). This is coefficient persistence, not a lower bound
for the subsequent character sum.

For the new ratio head \(B_0=U^{7/9}\) and
\(29/25\le r=\log_U D\le117/100\),

\[
                r-7/9\ge86/225.
\]

For example choose \(\beta=22/25>7/8\). The bare power in (11)
is at most \(U^{-86/1875}\). Since the radical of Q has a
prescribed polynomial bound, choose epsilon sufficiently small
after that bound and the r range are fixed. This gives the clean
uniform consequence

\[
                H_{\chi,P_u}(m)\ll U^{-1/25}.              \tag{14}
\]

The constants retain their stated source dependence. Taking beta
arbitrarily close to 7/8 instead permits every fixed exponent less
than \(43/900\), but (14) is enough for the synthesis question.

## 4. The exact residual after subtracting both proved components

The far original-product selector in `ASYMMETRIC_HB_TAIL.md` is
\(1-\chi_0(Nm/U)\). Subtract that component and the full ratio
head from the original inverse. Formula (6) shows that their
remaining coefficient is exactly

\[
              \boxed{\quad
        \chi_0(Nm/U)A(m)-H_{\chi,P_u}(m).
                       \quad}                              \tag{15}
\]

The two selectors are not asserted to be disjoint, so (15) makes
no unsigned inclusion-exclusion inference. It is simply the
difference of the three exact signed expressions.

For \(Nm\le U\), the first term in (15) is A(m). For squarefree
m at the old critical exponent

\[
 b_*=0.74569994272429016337\ldots,
 \qquad r_c=1.16395357650901095632\ldots,
\]

the common factors satisfy

\[
 b_*<7/9-2/125=857/1125,
 \qquad b_*<7/9<1,
 \qquad b_*<r_c-2/125.
\]

Thus the old critical product scale lies below the proposed lower
bound for a long inverse witness, below U, and below y_2. Nevertheless
(12)--(15) restore its original coefficient up to \(O(U^{-1/25})\).
The unit in the first original inverse factor still leaves a second
inverse at that old length. A ratio tail cannot be declared to
contain only second inverses of length at least \(U^{7/9-2/125}\)
by undoing the ordinary functional equation.

If the previously proved original-product head is also subtracted,
its cutoff is zero at this critical scale and this conclusion is
unchanged. A new estimate might still exploit cancellation among
these remaining coefficients, or control an intersection of the
two transforms with its full kernel. Neither follows from the
already proved separate component norms.

The critical exponents are the same source-compatible comparison
data recorded and qualified in `ASYMMETRIC_HB_TAIL.md`. No existence
of rows saturating those scalar resources is asserted here.

## 5. A finite example and the verification boundary

The loss of support can already be seen with the one-prime outer
coefficient \(A(1)=1\), \(A(p)=-1\), all other coefficients zero,
and p on the natural unit support. Choose a smooth selector with
\(\chi(1/B_0)=1\), \(\chi(p/B_0)=0\). Then

\[
 C_1=1-1/Np,\quad C_p=-1,\quad
                   D_{1-\chi,P}(1)=1/Np\ne0.               \tag{16}
\]

It is the exact one-prime instance of the inversion, not a bound
for the full arithmetic family. The stronger persistence in (13)
uses the complete coefficients and the stated scalar cap.

`check_ratio_cutoff_return.py` verifies both finite formulas
(5) and (7), their full-selector inversion, and the exact reflected
reindexing with nontrivial natural punctures and primitive dual
characters. It tests negative controls which drop the k mask or
assert a false lower support cutoff. It also checks the rational
power margins in (14). These checks do not certify the imported
zero-free premise, a functional equation, or any row-mean lower bound.
