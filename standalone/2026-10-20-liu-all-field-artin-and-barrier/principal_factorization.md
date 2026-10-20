# The angular Hecke factor in Liu's principal residue

Date: 2026-10-20.

Status: proposed complete algebraic and analytic component proof, conditional only on identification with the explicit local correction in the pinned source. No new zero-free boundary or native moment estimate is claimed.

Source: Baiying Liu, [arXiv:2610.26835v1](https://arxiv.org/abs/2610.26835v1), Section 13.3, pp. 94-97, equation (13.9), and Lemma 4.2, pp. 28-29. The source PDF SHA-256 is `5d0fd10274c8444c789b0b7925a1cd3419017fe760be3219b6be51d7fbed9bd5`. The calculations here concern the actual principal residue \((w,z)=(1,1/6)\). They use the displayed local formula as an auditable starting point; they do not reprove its exceptional-theta origin.

## 1. Exact local identity

Fix a number field \(F\supseteq\mu_{12}\), its finite excluded set \(S\), and a finite-order target Hecke character \(\eta\). All products below run over prime ideals of \(F\) outside \(S\). For \(q=N\mathfrak p\), let

\[
 D=\eta(\mathfrak p)q^{-s},\qquad
 \nu=(\overline\Lambda\eta)^6,\qquad
 R=\nu(\mathfrak p)q^{3-6s},\qquad v=q^{-1}.
\]

Here \(\Lambda\) is the unitary theta coefficient character from source Lemma 4.2. It has complex angular types \(\pm1\). Thus \(\nu\) has complex angular types \(\pm6\), and in particular is nonprincipal and of infinite order. Both \(\eta\) and \(\Lambda\) are unramified outside the chosen \(S\).

At the principal frequency, source Section 13.3 has \(j=0,\rho=1\). Specialize its independent variables to \(w=1,z=1/6\), so that \(Y_0=V=v\). Its local series then simplifies to

\[
 P_0^*=\frac{(1+v)(R-D)}{1-R},\qquad
 P_0=\frac{1+v}{1-v}+P_0^*.
\]

Indeed, the term involving \((q-1)Y_0V/(1-V)\) becomes \(v\); retaining that term is essential. Equation (13.9) now gives

\[
 \boxed{
 H_{\eta,\mathfrak p}(s,1,1/6;1)
 =\frac{(1-q^{-2})\{1-(1-q^{-1})D-q^{-1}R\}}
        {(1-D)(1-R)}.}
 \tag{1.1}
\]

Define the residual factor

\[
 K_{\eta,\mathfrak p}(s)
 =(1-R)H_{\eta,\mathfrak p}(s,1,1/6;1)
 =(1-q^{-2})\left(1+\frac{q^{-1}(D-R)}{1-D}\right).
 \tag{1.2}
\]

Consequently, in the initial region of absolute convergence,

\[
 \boxed{
 H_\eta(s)=L_F^S(6s-3,\nu)K_\eta(s),\qquad
 K_\eta(s)=\prod_{\mathfrak p\notin S}K_{\eta,\mathfrak p}(s).}
 \tag{1.3}
\]

The power six retains the full target character \(\eta^6\). No order-six assumption on the target has been made. The extracted factor is an angular Hecke function, not a finite-order Hecke function and not generally a Dedekind zeta function.

## 2. The residual product is a holomorphic unit for \(\operatorname{Re}s>1/2\)

### Proposition

The product \(K_\eta\) converges normally and is holomorphic and nowhere zero on \(\operatorname{Re}s>1/2\). On every closed sub-half-plane \(\operatorname{Re}s\geq1/2+\epsilon\), its modulus and inverse modulus are bounded uniformly in the imaginary part and in all unitary local target/theta phases. The bounds may depend on \(F\) and \(\epsilon\).

### Proof: local nonvanishing

Write \(\sigma=\operatorname{Re}s>1/2\). Since the local phases have modulus one,

\[
 |D|=q^{-\sigma}<q^{-1/2},\qquad
 |R|=q^{3-6\sigma}<1.
\]

The numerator \(N=1-(1-q^{-1})D-q^{-1}R\) satisfies

\[
 |N|\geq1-(1-q^{-1})q^{-\sigma}-q^{-1}q^{3-6\sigma}
 >(1-q^{-1})(1-q^{-1/2})>0.
 \tag{2.1}
\]

The other numerator factor \(1-q^{-2}\) is positive, and the denominator \(1-D\) never vanishes. Thus every \(K_{\eta,\mathfrak p}\) is holomorphic and nonzero there. The same estimates give the uniform local lower bound

\[
 |K_{\eta,\mathfrak p}(s)|
 \geq\frac{(1-q^{-2})(1-q^{-1})(1-q^{-1/2})}{1+q^{-1/2}}
 \geq c_*>0\qquad(q\geq2),
 \tag{2.2}
\]

where one may take
\(c_*=(3/8)(1-2^{-1/2})/(1+2^{-1/2})\).
All factors in the middle expression increase as \(q\) increases, so the value at \(q=2\) is a valid lower bound.

### Proof: normal convergence and global nonvanishing

Equation (1.2) gives

\[
 K_{\eta,\mathfrak p}-1
 =-q^{-2}+(1-q^{-2})\frac{q^{-1}(D-R)}{1-D}.
\]

On \(\sigma\geq1/2+\epsilon\), the denominator has a uniform positive lower bound, and therefore

\[
 |K_{\eta,\mathfrak p}-1|
 \ll q^{-2}+q^{-3/2-\epsilon}+q^{-1-6\epsilon}.
 \tag{2.3}
\]

All three prime-ideal sums converge. Their bounds are independent of imaginary parts and local phases. Normal convergence follows on every compact subset of \(\sigma>1/2\); the nonzero local factors and summable deviations imply that their product is nonzero. Equation (2.2) also bounds the absolute value of each real logarithm of the local modulus by a fixed multiple of \(|K_{\eta,\mathfrak p}-1|\), giving the stated product and reciprocal bounds.

For example, if \(0<\epsilon\leq1/2\) and \(n_F=[F:\mathbb Q]\), the comparison with rational primes (at most \(n_F\) prime ideals above each rational prime) and then with integers gives the crude explicit shape

\[
 |K_\eta(s)|+|K_\eta(s)|^{-1}
 \leq2\exp\{C n_F(1+\epsilon^{-1})\},
 \qquad \sigma\geq1/2+\epsilon,
 \tag{2.4}
\]

for an absolute constant \(C\). No discriminant-uniform bound for the extracted Hecke function is inferred from (2.4). \(\square\)

## 3. Continuation and the exact source of possible zeros

The unitary Hecke character \(\nu\) has nonzero infinity type, so its primitive Hecke function is entire. The finite factors omitted in \(L_F^S\) are entire as well. Identity (1.3) therefore continues the principal correction holomorphically to

\[
 \operatorname{Re}s>1/2.
\]

Within this half-plane, the omitted Euler factors cannot vanish: their arguments \(6s-3\) have positive real part, whereas a factor \(1-\nu(\mathfrak p)q^{-u}\) vanishes only on \(\operatorname{Re}u=0\). The residual product also cannot vanish. Hence the zeros of the continued \(H_\eta\), with multiplicity, are exactly

\[
 \boxed{s=(\rho+3)/6,
 \quad L_F(\rho,\nu)=0,\quad \operatorname{Re}\rho>0.}
 \tag{3.1}
\]

In particular \(H_\eta\) is automatically nonzero for \(\operatorname{Re}s>2/3\), by the ordinary Euler-product half-plane \(\operatorname{Re}(6s-3)>1\). Thus the source's convenient principal box \(\operatorname{Re}s\geq437/500\) is not an intrinsic nonvanishing boundary for this residue correction.

At a zero of the target \(L_F(s,\eta)\) with \(\operatorname{Re}s>2/3\), the ratio \(H_\eta(s)/L_F(s,\eta)\) retains the target pole with its full multiplicity. Below that line, any possible cancellation is explicitly reduced to the simultaneous-zero condition

\[
 L_F(s,\eta)=0,
 \qquad L_F(6s-3,(\overline\Lambda\eta)^6)=0.
\]

This is an exact localization of a potential obstruction, not an assertion that the simultaneous condition occurs or cannot occur. A proven bound \(\operatorname{Re}\rho\leq B_\nu\) for this infinite-order angular function would give nonvanishing of \(H_\eta\) for \(\operatorname{Re}s>(3+B_\nu)/6\). The universal finite-order theorem in Liu's paper does not establish that premise for \(\nu\).

## 4. Relation to the inspected repository work

The full proof in [PR #975](https://github.com/GettysburgResearch/riemann/pull/975), pinned at [edbc27b61208ccc7ee1fa99fa3f4e861f5a03452](https://github.com/GettysburgResearch/riemann/blob/edbc27b61208ccc7ee1fa99fa3f4e861f5a03452/standalone/2026-10-18-resonant-transverse-jet/PROOF.md), was inspected. It extracts the mixed factor \(\zeta_F^S(s+w)\) and proves a nonvanishing normalizer on \(w=1-s\), with \(\operatorname{Re}z>1\). The calculation here instead specializes to Liu's principal residues \(w=1,z=1/6\), extracts the angular factor at \(6s-3\), and proves that the remaining product is a unit for \(\operatorname{Re}s>1/2\). No literature-wide priority claim is made.

The original compensated average, its direct estimate, all nonprincipal rows, and the justified movement of the original contours still require their own estimates. An improved domain for this principal residue does not move those contours or improve the zero-free boundary on its own.

## 5. Exact coefficientwise removal, and the cost of taking absolute values

The extracted angular factor can be removed by an exact Mellin convolution. This also identifies the extra estimate that such a removal would need before it could improve the theta argument.

Use the source normalization \(C(s)=s-c_0\), where \(c_0=(4+b)/6\), and retain its original Gaussian. Equation (13.13) is

\[
 f_\eta(Z)=\frac1{2\pi i}\int_{(2)}
     Z^{s-c_0}e^{(s-5/6)^2}\frac{H_\eta(s)}{L_F^S(s,\eta)}\,ds.
 \tag{5.1}
\]

Write \(\mu_F(\mathfrak a)\) for the ideal Möbius function, and sum only over ideals coprime to \(S\). Define

\[
 (T_\nu f_\eta)(Z)
 =\sum_{(\mathfrak a,S)=1}
   \mu_F(\mathfrak a)\nu(\mathfrak a)
   (N\mathfrak a)^{3-6c_0}
   f_\eta\!\left(\frac{Z}{(N\mathfrak a)^6}\right).
 \tag{5.2}
\]

The reciprocal Euler series

\[
 \frac1{L_F^S(6s-3,\nu)}
 =\sum_{(\mathfrak a,S)=1}
       \mu_F(\mathfrak a)\nu(\mathfrak a)(N\mathfrak a)^{3-6s}
\]

converges absolutely on \(\operatorname{Re}s>2/3\). Substitution in (5.1), with absolute interchange on the original line \(\operatorname{Re}s=2\), gives exactly

\[
 (T_\nu f_\eta)(Z)=\frac1{2\pi i}\int_{(2)}
     Z^{s-c_0}e^{(s-5/6)^2}\frac{K_\eta(s)}{L_F^S(s,\eta)}\,ds.
 \tag{5.3}
\]

The shifted argument in (5.2) and the exponent \(3-6c_0\) are both necessary: together they recover \((N\mathfrak a)^{3-6s}\). This is an identity for the principal Mellin transform; it does not assert that the transformed function has a new theta interpretation or satisfies the original mixed moment estimates.

Here is a precise bound for the direct absolute-value route. Suppose that, for some real \(B\),

\[
 |f_\eta(Y)|\ll Y^{B-c_0}\quad(Y\geq1),
 \qquad
 |f_\eta(Y)|\ll_A Y^A\quad(0<Y\leq1)
 \quad\text{for every }A>0.
 \tag{5.4}
\]

The source establishes the second estimate by moving the original principal integral right (Section 13.6, p. 106); the first is the kind of estimate its compensated average seeks to prove. The fixed-field estimate \(\#\{\mathfrak a:N\mathfrak a\leq Y\}\ll_F Y\) and partial summation imply

\[
 |T_\nu f_\eta(Z)|\ll
 \begin{cases}
  Z^{B-c_0},&B>2/3,\\
  Z^{2/3-c_0}\log(2Z),&B=2/3,\\
  Z^{2/3-c_0},&B<2/3,
 \end{cases}
 \qquad Z\geq2.
 \tag{5.5}
\]

For completeness, the ideals of norm at most \(Z^{1/6}\) contribute at most

\[
 Z^{B-c_0}\sum_{N\mathfrak a\leq Z^{1/6}}
                 (N\mathfrak a)^{3-6B}.
\]

This sum is bounded, logarithmic, or of order at most \(Z^{2/3-B}\), according as \(B>2/3\), \(B=2/3\), or \(B<2/3\). For the remaining ideals, choose \(A>\max\{0,2/3-c_0\}\) in (5.4). Their contribution is at most

\[
 Z^A\sum_{N\mathfrak a>Z^{1/6}}
       (N\mathfrak a)^{3-6c_0-6A}
 \ll Z^{2/3-c_0}.
\]

This proves (5.5) and also shows that the series (5.2) converges absolutely at each positive \(Z\). The logarithm at equality can be absorbed into an arbitrarily small exponent loss.

Thus removing the angular factor is algebraically possible, but the direct estimate preserves the original exponent only above \(2/3\). Below \(2/3\), this route supplies only the \(2/3\) exponent. Improvement there would require a further estimate, such as cancellation in the relevant angular Möbius convolution, together with control of the transformed theta averages and their coupled variables. Liu's finite-order theorem alone does not provide that angular cancellation.
