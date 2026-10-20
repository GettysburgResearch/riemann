# Conditional left-line bounds in shrinking smooth angular sectors

20 October 2026. **Status: proposed conditional consequence, with an
explicit common unitary Hecke zero-free premise.** This is a consumer
of the cubic mean, not a new zero-free boundary or a prime-counting
theorem.

Dependencies:

* ANGULAR_UNIFORMITY.md, SHA256
  9735a9cf2a7c75495a86da9c80ff9ddb7e2efb1e19bb6acad226aaec00b99385;
* ../uniform/UNIFORM_INVERSE_AND_STRIPPING.md, SHA256
  fcee7547018c62c5a54c273501b7f2032a93b3633b5b04b3cdce90fdc1015c12;
* the exact Type-I multiplicativity and squarefree/common-prime
  conventions in ../average/ANGULAR_SELF_ABSORPTION.md, SHA256
  0c195c93ef2548a81197e21d0eca58f1632f25e9339d0f078fa185f8605d59e8.

## 1. Actual family premise and the stripped left-line estimate

Fix \(\beta\in[1/2,1)\). Suppose the actual unitary Hecke characters
over \(E=\mathbb Q(\omega)\) that occur below all have
\[
                  L_E(z,\chi)\ne0\qquad(\Re z>\beta).
\tag{S1}
\]
A common zero-free half-plane for the full unitary family is a
sufficient premise. A theorem restricted to a different set of
infinity types is not substituted for (S1).
Choose a fixed
\[
        \frac{2\beta+1}{6}<p<\frac12.
\tag{S2}
\]
In particular \(p>1/4\), so the reflected mean (U2) is available.

For \(\ell\ne0\), retain the source notation
\[
 Q_{r,\ell}(s)=Z_r(3s-\tfrac12,3\ell)\,
       \mathcal R_{r,\ell}(s).
\]
There is no moving quadratic conductor: \(S=1\).
The Hecke factor in the cube completion, without archimedean
gamma factors, has fixed finite conductor, depending
only on the source's fixed ramified conventions, and angular
degree \(3\ell\). Its analytic conductor at the argument
\(3p-\tfrac12+3it\) is
\[
             \mathcal C\ll(1+|\ell|+|t|)^2.
\tag{S3}
\]
The strict gap \(3p-\tfrac12-\beta>0\), Proposition 1 of the
uniform reciprocal note, and restoration of deleted primes imply
\[
 |Z_r(3p-\tfrac12+3it,3\ell)^{-1}|
       \ll_{p,\beta,\epsilon}(Nr)^\epsilon
                    (1+|\ell|+|t|)^\epsilon.
\tag{S4}
\]
The same statement holds for each fixed number of derivatives,
after allocating the conductor exponent in Proposition 1
sufficiently small. The inverse is continued holomorphically at
any principal pole. No angular differentiation of the test weight
is used to obtain uniformity.

The reflected complete mean and (S4) therefore give
\[
 \sum_{Nr\le B}^{*}|\mathcal R_{r,\ell}(p+it)|^2
 \ll_{p,\beta,\epsilon}
       B^{2-2p+\epsilon}(1+|\ell|+|t|)^{4-4p+\epsilon}.
\tag{S5}
\]
All four finite ramified profiles are covered; their cubic
characters do not change the cube factor. The sum keeps all
natural common-prime zeros.

Let \(W_A,W_B\) be fixed smooth compactly supported radial weights,
and let \(|b_v|\le1\). Define the actual free-column Type-I form
\[
 T_\ell(A,B)=\sum_{u,v} b_v\,\widetilde g(uv)\alpha(uv)^\ell
                       W_A(Nu/A)W_B(Nv/B),
 \qquad A,B\ge1.
\tag{S6}
\]
The inner variable \(u\) is unrestricted apart from the source
primary and squarefree Gauss support. In particular a prime-only
inner sum is not asserted to satisfy the same statement.
Exact Gauss multiplicativity, Mellin inversion in \(u\), and
Cauchy--Schwarz over \(v\) yield
\[
 |T_\ell(A,B)|\ll_{p,\beta,\epsilon,W}
   (AB)^\epsilon A^pB^{3/2-p}
                  (1+|\ell|)^{2-2p+\epsilon}.
\tag{S7}
\]
Rapid Mellin decay uses a fixed number of radial derivatives,
independent of \(\ell,A,B\). The gap in (S2) is fixed while the
estimate is proved; the implicit constant may depend on that gap.

## 2. Smooth angular localization with the exact zero mode

Let \(\phi\in C_c^\infty(\mathbb R)\). For \(0<\Delta\le1\),
periodize \(\phi((\theta-\theta_0)/\Delta)\) on
\(\mathbb R/\mathbb Z\), and denote the result by
\(\phi_{\Delta,\theta_0}\).
Insert this function of \(\arg\alpha(uv)/(2\pi)\) in (S6), using
the same \(b_v\) for every Fourier mode, to obtain
\(T_{\phi_{\Delta,\theta_0}}\).
Its zero Fourier coefficient is exactly
\(\Delta\int_{\mathbb R}\phi\).
The remaining coefficients satisfy
\[
 \sum_{k\ne0}(1+|k|)^{2-2p+\epsilon}
              |\widehat{\phi_{\Delta,\theta_0}}(k)|
       \ll_{\phi,p,\epsilon}\Delta^{-2+2p-\epsilon}.
\tag{S8}
\]
Thus
\[
 \left|T_{\phi_{\Delta,\theta_0}}
       -\Delta\!\left(\int\phi\right)T_0\right|
 \ll (AB)^\epsilon A^pB^{3/2-p}
                       \Delta^{-2+2p-\epsilon}.
\tag{S9}
\]
The unconditional bound from (U16) remains available, so one may
take the smaller of the right side of (S9) and
\((AB)^\epsilon A^{1/2}B\Delta^{-1-\epsilon}\).
Ignoring the arbitrarily small losses, the conditional bound is
stronger precisely when
\[
                            A\Delta^2>B.
\tag{S10}
\]

The zero-angular term in (S9) has not been estimated or discarded.
For example, when \(B=1\), the spherical Gauss sum can have an
\(A^{5/6}\) main term. Formula (S9) is a weighted discrepancy from
the actual zero-angular average, not a bound asserting that this
average or its residue vanishes.

## 3. Width exponents on the full Type-I range

Write \(X=AB\), \(A=X^a\), \(B=X^{1-a}\), with the complete range
\(0\le a\le1\). For fixed \(p\) in (S2), the right side of (S9)
is smaller by a power than the natural absolute scale \(X\Delta\)
if \(\Delta\ge X^{-\xi_p(a)+\eta}\), where \(\eta>0\) is fixed
and
\[
 \xi_p(a)=
       \frac{p-\tfrac12+(\tfrac32-2p)a}{3-2p}.
\tag{S11}
\]
Letting \(p\) approach \((2\beta+1)/6\) from the right, while
keeping a fixed positive gap appropriate to \(\eta\), gives
\[
 \boxed{\displaystyle
 \xi_\beta(a)=
       \frac{(7-4\beta)a-2(1-\beta)}{4(4-\beta)}.}
\tag{S12}
\]
More precisely, for fixed \(a,\eta\) with
\(\xi_\beta(a)>\eta>0\), choose \(p\) in (S2) sufficiently close
to its lower endpoint, then all small losses sufficiently small.
Uniformly for
\(\Delta\ge X^{-\xi_\beta(a)+\eta}\), (S9) is
\(O(X^{1-c}\Delta)\) for some \(c>0\) depending on these choices.
No uniform constant as \(p\) reaches the endpoint is claimed.

The conditional width exponent is positive exactly when
\[
                   a>\frac{2(1-\beta)}{7-4\beta}.
\tag{S13}
\]
For other \(a\), this particular conditional expression gives no
shrinking-sector saving. The unconditional exponent is \(a/4\).
Their exact difference is
\[
           \xi_\beta(a)-\frac a4
                =\frac{(1-\beta)(3a-2)}{4(4-\beta)}.
\tag{S14}
\]
Consequently the conditional expression improves the
unconditional width only for \(a>2/3\), agrees at \(a=2/3\),
and is weaker for \(a<2/3\).
Both estimates are valid on the whole range; the usable exponent
is their maximum. In particular the balanced case still gives
the unconditional exponent \(1/8\).

At \(a=1\),
\[
                 \xi_\beta(1)=\frac{5-2\beta}{4(4-\beta)}.
\tag{S15}
\]
For illustration, substituting the candidate
\(\beta=B_\flat\approx0.874886647039964\) gives approximately
\(0.2600\), instead of \(1/4\). This numerical substitution is
conditional on (S1); it does not itself establish that premise.
The conclusion concerns smooth weighted sectors and an
unrestricted Type-I column. It supplies no sharp-sector prime
asymptotic, no improved numerical zero-free boundary, and no RH
claim.
