# Source transpose, endpoint projection, and the twenty primitive directions

This is a proof-only statement about the fixed-prime half-source and its
original observation. The transpose is an honest involution of the ambient
source tensor. It is not, in general, an operation on admissible source
paths. The difference is visible before taking any norm.

The source convention is L-102707 at
ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc, blob
6810bcece309b0c54ae6c8fc84b314990004549c. The completed field and its
faithfulness are the separate proof packet
822646ffea23d906c385f0273a8c45693e982c4d:

| Theorem | Git blob |
| --- | --- |
| FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md | 851e4331c12d9f3f073ab73dca26baa33bd5e548 |
| INFINITE_NATIVE_PHYSICAL_FAITHFULNESS.md | f7c42135e276a34d4da00279110666b0f4636080 |

No new numerical acquisition, all-prime limit, or Boolean/Walsh
identification is asserted.

## 1. An actual finite-dimensional source carrier

For \(r\) independent prime schedules, let
\[
 V=\operatorname{span}_{\mathbb R}\{f_a(u)=u^a:a\in\{0,1\}^r\},
 \qquad f_0=1.
\]
These are polynomials on the continuous cube, not functions in a quotient
where \(u_i^2=u_i\). Every actual supported source coefficient has a unique
expansion
\[
                       a_n(u)=\sum_a v_{n,a}f_a(u).
\]
For an admissible continuous monotone path from \(\mathbf0\) to
\(\mathbf1\), define its monomial current matrix
\[
                       M_{a,b}(\gamma)=2\int_\gamma f_b\,df_a. \tag{1.1}
\]
Then the literal ordered current is exactly
\[
                  B_{n,m}(\gamma)=v_n^{\,t}M(\gamma)v_m.       \tag{1.2}
\]
The original factor two and derivative-side convention are unchanged.
The squarefree source coefficients are nonzero scalar multiples of all
the \(f_a\), so this matrix is a faithful carrier of the complete labelled
current. It is not a list of independently adjustable path parameters.

On the ambient real matrix space define
\[
 J(M)=M^t,\qquad P_\pm M=\frac{M\pm M^t}{2}.
\]
Thus \(J^2=1\), and \(P_+\), \(P_-\) are complementary projections.
Under (1.2), transpose swaps \(B_{n,m}\) and \(B_{m,n}\).

## 2. The symmetric part is exactly an endpoint matrix

The continuous BV product rule gives
\[
 M_{a,b}+M_{b,a}=2[f_af_b]_{\mathbf0}^{\mathbf1}=2E_{a,b},
 \qquad
              E_{a,b}=1-\mathbf1_{a=0}\mathbf1_{b=0}.         \tag{2.1}
\]
Consequently every actual current has the form
\[
                         M(\gamma)=E+A(\gamma),\qquad A^t=-A.
                                                                    \tag{2.2}
\]
The matrix \(E\) is fixed, and
\[
 A_{a,b}(\gamma)=\int_\gamma(f_b\,df_a-f_a\,df_b).             \tag{2.3}
\]
In particular, for every nonconstant monomial,
\[
 M_{0,a}=0,\quad M_{a,0}=2,\quad
 E_{0,a}=1,\quad A_{0,a}=-1.                                 \tag{2.4}
\]
These endpoint constraints will matter for admissibility.

For a real ambient matrix \(N\), let \(T_H(N)\) denote the original
physical observation
\[
 T_H(N)(t)=\sum_{nm\le H}
       \frac{v_n^{\,t}Nv_m}{\sqrt{nm}}e^{it\log(n/m)}.
\]
Its absolutely convergent infinite version is the operator in the frozen
faithfulness theorem. The symmetric cutoff and real coefficient vectors
give, at every finite horizon and at infinity,
\[
 T_H(N^t)(t)=T_H(N)(-t)=\overline{T_H(N)(t)}.                 \tag{2.5}
\]
Therefore
\[
 T_H(P_+N)=\operatorname{Re}T_H(N),\qquad
 T_H(P_-N)=i\operatorname{Im}T_H(N).                         \tag{2.6}
\]
The first field is real and even; the second is imaginary and odd.
These statements are for real matrices. Transpose alone is not complex
conjugation on an arbitrary complex coefficient matrix.

The original measure \(d\nu=|\widehat\kappa(t)|^2dt/(2\pi)\) is even.
Reflection \(f(t)\mapsto f(-t)\) is consequently a unitary involution
on the original complex Hilbert space, with orthogonal even and odd
projections. Thus (2.5) intertwines actual source and observation
involutions, and
\[
 \|T_H(E+A)\|_\nu^2=\|T_H(E)\|_\nu^2+\|T_H(A)\|_\nu^2.       \tag{2.7}
\]
No diagonalization of the frequency Gram form or deletion of ratio
aliases is involved.

## 3. The fixed endpoint energy is positive at infinity

With \(z_p(t)=p^{-1/2+it}\), the completion theorem identifies
\[
 R(t):=T_\infty(E)(t)
   =\prod_p|1-z_p(t)|-\prod_p|1-z_p(t)^2|.                  \tag{3.1}
\]
In particular
\[
 R(0)=\prod_p(1-p^{-1/2})-\prod_p(1-p^{-1})<0
                                                                    \tag{3.2}
\]
for every nonempty finite prime panel. The continuous function \(R\)
is nonzero on an interval about zero. The original nonzero compactly
supported kernel has an entire nonzero Fourier transform, whose real
zeros are isolated. Its zero at \(t=0\), coming from the zero kernel
moment, does not make its density vanish on that interval.
It follows that
\[
             \|R\|_\nu^2>0,\qquad
             m_\infty\ge\|R\|_\nu^2.                       \tag{3.3}
\]
Here \(m_\infty\) is the minimum over actual monotone paths, whose
existence is established in the completion theorem.

## 4. Exactly eight fixed constraints in three variables

Now specialize to \(r=3\), with variables \(u,v,w\).
The ambient skew matrix space has dimension \(\binom82=28\).
It is naturally the dual of \(\Lambda^2 V\). Define the source curvature
map
\[
 \mathcal K:\Lambda^2 V\longrightarrow\Omega^2_{\rm poly},
                   \qquad f\wedge g\longmapsto2\,df\wedge dg. \tag{4.1}
\]
The one-form in (2.3) has negative exterior derivative
\(\mathcal K(f\wedge g)\).

Its kernel is exactly
\[
 \boxed{\displaystyle
 \ker\mathcal K=
   (1\wedge\operatorname{span}\{u,v,w,uv,uw,vw,uvw\})
   \ \oplus\
   \mathbb R\,(u\wedge vw+v\wedge uw+w\wedge uv).}             \tag{4.2}
\]
The first seven directions clearly have zero curvature. For the eighth,
\[
 du\wedge d(vw)+dv\wedge d(uw)+dw\wedge d(uv)=0.              \tag{4.3}
\]
There are no further kernel directions. Here is a finite source
calculation proving completeness without a rank extrapolation. After
removing the seven constant wedges, the 21 remaining monomial wedges
split by their total multidegree as follows:

| Multidegree pattern | Number of degrees | Wedges per degree | Curvature rank per degree |
| --- | ---: | ---: | ---: |
| permutations of \((1,1,0)\) | 3 | 1 | 1 |
| permutations of \((2,1,0)\) | 6 | 1 | 1 |
| \((1,1,1)\) | 1 | 3 | 2 |
| permutations of \((2,1,1)\) | 3 | 2 | 2 |
| permutations of \((2,2,1)\) | 3 | 1 | 1 |

Each single wedge in the table has nonzero curvature. At degree
\((1,1,1)\), the three wedges in (4.3) have exactly their displayed
relation: the first two forms are linearly independent. At degree
\((2,1,1)\), representatives \(u\wedge uvw\) and \(uv\wedge uw\)
have independent curvatures, because the latter has a nonzero
\(dv\wedge dw\) coefficient and the former has none. Coordinate
permutations handle the other two such degrees. Different multidegrees
are independent. Thus the total rank is
\(3+6+2+6+3=20\), proving (4.2).

For an actual path, evaluation of (2.3) on the seven constant wedges
is \(-1\), as already recorded in (2.4). The remaining kernel one-form
is exact:
\[
 \begin{aligned}
 &(vw\,du-u\,d(vw))+(uw\,dv-v\,d(uw))+(uv\,dw-w\,d(uv))\\
 &\hspace{35mm}=-d(uvw).
 \end{aligned}
\]
Hence the eighth constraint is
\[
                  A_{u,vw}+A_{v,uw}+A_{w,uv}=-1.             \tag{4.4}
\]
There are therefore eight independent fixed affine constraints on the
28 skew entries. Differences between actual paths satisfy the
corresponding eight homogeneous equations.

These equations describe exactly the affine hull of actual skew
currents; they do not describe every individually attainable current.
For completeness, actual monotone rectangles prove that there is no
further linear constraint. Compare two paths with a common monotone
prefix and suffix and opposite axis orders around an interior rational
coordinate rectangle. Their evaluations on \(f\wedge g\) differ, up to
orientation, by the rectangle integral of \(2df\wedge dg\).
If such an integral vanishes for every rational coordinate rectangle,
shrinking rectangles and continuity force every coefficient of the
polynomial two-form to vanish. These actual differences therefore span
the dual of \(\operatorname{im}\mathcal K\), of dimension 20.

Thus the ambient antisymmetric carrier has dimension 28, whereas the
actual primitive source family has affine variation dimension 20.
The eight missing directions are fixed endpoint/exact-form constraints,
not eight directions lost by the infinite physical observation.

## 5. A projector on carriers need not act on paths

For any actual path, transpose has
\((M^t)_{0,a}=2\), the symmetric projection has \(E_{0,a}=1\), and
the skew projection has \(A_{0,a}=-1\). Every actual path instead has
\(M_{0,a}=0\). Therefore none of these three matrices is an admissible
literal current when the panel is nonempty:
\[
             M^t\notin\{M(\gamma)\},\quad
             E\notin\{M(\gamma)\},\quad
             A\notin\{M(\gamma)\}.                          \tag{5.1}
\]
In particular extracting the imaginary field is an ambient source and
Hilbert projection; it is not a demonstrated legal deformation of the
primitive path.

The frozen infinite faithfulness theorem strengthens this distinction.
It says that \(T_\infty\) is injective on the entire matrix carrier.
Thus no different admissible path can secretly realize \(T_\infty(E)\),
\(T_\infty(A)\), or \(T_\infty(M^t)\) while having a different literal
matrix. This last assertion is about the infinite observation. No
unmeasured finite-horizon injectivity is assumed.

## 6. Faithfulness also gives a strict primitive energy gap

There is a qualitative improvement of (3.3), with no new numerical
constant. Use exactly the monomial basis
\(1,u,v,w,uv,uw,vw,uvw\) to give real skew matrices their Frobenius norm,
and let
\[
 s_-=\min_{\substack{N^t=-N\\\|N\|_{\rm F}=1}}
                            \|T_\infty(N)\|_\nu>0.          \tag{6.1}
\]
Positivity follows from finite dimensionality and the separate
faithfulness theorem. The seven unit constraints contribute 14 to
\(\|A\|_{\rm F}^2\). The three distinct remaining entries in (4.4)
have sum \(-1\), so their squares sum to at least \(1/3\); their
transposed entries contribute the same amount. Consequently
\[
 \|A(\gamma)\|_{\rm F}^2\ge\frac{44}{3},\qquad
 \boxed{\displaystyle
 m_\infty\ge\|R\|_\nu^2+\frac{44}{3}s_-^2>\|R\|_\nu^2>0.}    \tag{6.2}
\]
In particular the imaginary current cannot vanish for any admissible
path in this three-prime source. This does not compute \(s_-\), the
infinite optimizer, or the numerical size of the strict gap.

The transpose splitting is consequently a precise bridge between the
ambient tensor carrier, the endpoint part, and actual primitive
variation. Its source and observation projections are classical linear
operations. Their admissibility obstruction, the eight exact source
constraints, and the strict-gap deduction retain the specified current
and observation. They are not an identification with Boolean Walsh
projectors, a change of primitive normalization, or a principal-member
theorem for a larger retained family.

