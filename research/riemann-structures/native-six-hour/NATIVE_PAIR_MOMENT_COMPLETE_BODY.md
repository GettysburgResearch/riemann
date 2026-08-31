# The complete three-moment body of a single monotone pair path

For a continuous coordinatewise monotone path from (0,0) to (1,1), put

\[
 A=\int v\,du,\qquad B=\int uv\,du,\qquad C=\int v^2\,du.
\]

This note gives the exact upper envelope of C at fixed (A,B), classifies
all its equality profiles, and combines it with the previously proved
lower envelope to determine the complete attainable three-moment body.
These are the original source occupations. The result does not optimize
the physical Gamma-weighted energy or identify a retained-gamma decoder.

The threshold-law correspondence and the exact lower envelope are frozen
at `8522f5a8854c29c755314bf4d86b2bc42464da71`:

- `NATIVE_THRESHOLD_LAW_AND_CONVEXIFICATION.md`, blob
  `a4f189a6f12cd189be7b711a4d0ac5f36bbc613d`;
- `NATIVE_PAIR_MOMENT_LOWER_ENVELOPE.md`, blob
  `a8b3d8448aef58f7c0c1b2105302e03e973d91d1`.

The argument uses standard compact moment-set geometry and convexity,
with the reductions proved below rather than imported as a claim that
two-point laws automatically extremize every two-moment problem. No
priority claim for these general methods or numerical discovery is made.

## 1. Statement of the complete body

The feasible first two moments are exactly

\[
 0\le A\le1,\qquad \frac A2\le B\le A-\frac{A^2}{2}.       \tag{1}
\]

At A=0 the only triple is (0,0,0), and at A=1 it is (1,1/2,1).
For 0<A<1 define

\[
 \boxed{\displaystyle
 C_{\max}(A,B)=
 \begin{cases}
 2A-1+\dfrac{(1-A)^3}{1-2B},&A\le\tfrac12,\\[6pt]
 \dfrac{A^3}{2(A-B)},&A\ge\tfrac12.
 \end{cases}}                                             \tag{2}
\]

The two formulas agree at A=1/2. Their denominators are positive on
the stated interior ranges. The complete body is

\[
 \boxed{\quad (A,B)\text{ satisfies (1)},\qquad
              C_{\min}(A,B)\le C\le C_{\max}(A,B).\quad}   \tag{3}
\]

Here C_min is the frozen lower envelope. For clarity its full formula
is recalled. Set

\[
 d=B-A/2,\quad B_{\max}=A-A^2/2,\quad
 B_0=A/2+\min(A,1-A)/6,
\]
\[
 B_1=\begin{cases}A-2A^2/3,&A\le1/2,\\
                  1/2-2(1-A)^2/3,&A\ge1/2.
       \end{cases}
\]

| Range | Exact C_min |
|---|---|
| A/2 <= B <= B_0 | A^2 + 12(B-A/2)^2 |
| A<1/2 and B_0 <= B <= B_1 | 4A^3/[9(A-B)] |
| A>1/2 and B_0 <= B <= B_1 | 2A-1+4(1-A)^3/[9(1/2-B)] |
| B_1 <= B <= B_max | A-sqrt((2A-A^2-2B)/3) |

The neighboring lower formulas agree at transitions. At A=1/2 the
one-clip interval has zero length. Both envelopes equal A^2 when B=A/2
and equal A when B=B_max. Every intermediate C in (3) is attained by
one actual monotone path, not merely by a mixture of different currents.

## 2. Threshold laws and the Gini problem

In u-time the path has a nondecreasing profile f:[0,1]->[0,1] almost
everywhere. Its completed graph includes all vertical segments, which
have zero du mass. There is a unique probability law mu on [0,1] whose
CDF is this profile almost everywhere: the initial height supplies an
atom at zero and the final missing height supplies an atom at one.
Conversely every such CDF has a completed monotone graph.

Let T,S be independent with law mu, and write

\[
 m=\mathbb ET=1-A,\qquad s=\mathbb ET^2=1-2B,\qquad
 V=s-m^2=2A-A^2-2B.                                      \tag{4}
\]

The moment range is m^2<=s<=m. Tonelli's theorem gives

\[
 G(\mu):=\mathbb E|T-S|=2\int_0^1 f(u)(1-f(u))\,du,
 \qquad C=A-\frac{G(\mu)}2.                              \tag{5}
\]

Thus maximizing C is precisely minimizing the Gini mean difference
under two fixed moments. This auxiliary probability law does not change
the original primitive 2ds or physical Mellin measure.

## 3. A minimizing law has at most three atoms

The set of probability laws on the compact interval with fixed first
and second moments is weakly compact and nonempty. The moments are
continuous for weak convergence. The functional G is also continuous:
CDFs converge at every continuity point of the limiting CDF, hence
almost everywhere, and the bounded integrands in (5) permit dominated
convergence. Therefore a minimum exists.

Moreover G is strictly concave as a function of the law. If mu and nu
have distinct CDFs f and g and 0<t<1, then

\[
 G(t\mu+(1-t)\nu)-tG(\mu)-(1-t)G(\nu)
       =2t(1-t)\int_0^1(f-g)^2\,du>0.                   \tag{6}
\]

Distinct laws have CDFs differing on a set of positive length; values
at individual jump points do not affect this assertion. A minimizing
law must consequently be an extreme point of the fixed-moment set.

Here is the needed support bound without a general extremal-measure
theorem. If a law has at least four support points, choose four disjoint
measurable neighborhoods E_i of positive mass. The three homogeneous
equations

\[
 \sum_{i=1}^4 c_i\int_{E_i}t^j\,d\mu(t)=0,
                           \qquad j=0,1,2
\]

have a nonzero real solution. Scale it so that |c_i|<=1, put
h=sum_i c_i 1_{E_i}, and take the distinct laws (1+h)mu and (1-h)mu.
They are nonnegative probability measures with the same two moments
and have midpoint mu. This contradicts extremality. Every minimizing
law therefore has at most three atoms.

This argument does not yet reduce three atoms to two. That extra step,
which is special to the present objective, is proved next.

## 4. Three interior atoms cannot minimize

Suppose a minimizer has three distinct atoms a<b<c with positive weights
p,q,r, where p+q+r=1. Keep these weights fixed and write x=b-a>0 and
y=c-b>0. The mean condition fixes

\[
 a=m-(1-p)x-r y,\qquad c=m+p x+(1-r)y.
\]

The variance and half-Gini are

\[
 V=p(1-p)x^2+2prxy+r(1-r)y^2,                             \tag{7}
\]
\[
 G/2=p(1-p)x+r(1-r)y.                                    \tag{8}
\]

Set alpha=p(1-p), beta=pr, gamma=r(1-r). The quadratic form in (7)
is positive definite because alpha*gamma-beta^2=pqr>0. On its positive
branch, locally regard y as a function of x. Implicit differentiation
gives

\[
 y'=-\frac{\alpha x+\beta y}{\beta x+\gamma y},\qquad
 y''=-\frac{\alpha+2\beta y'+\gamma(y')^2}
                {\beta x+\gamma y}<0.                   \tag{9}
\]

The numerator is positive by positive definiteness and the denominator
is positive. Consequently (8) is strictly concave in this local x
coordinate. If 0<a<c<1, both signs of a sufficiently small change in x
remain feasible: y stays positive and a,c remain strictly inside the
unit interval. Strict concavity then contradicts local minimality.

A three-atom minimizer must therefore contain zero or one as an outer
atom. A collapsed gap or a zero weight already gives at most two atoms.

## 5. The boundary three-atom case also reduces to two

Consider a law supported on {0,b,c}, with 0<b<c<=1 and all three
weights positive. Its nonzero-location weights are forced by m,s:

\[
 q=\frac{mc-s}{b(c-b)},\qquad
 r=\frac{s-mb}{c(c-b)},\qquad
 p=\frac{bc-m(b+c)+s}{bc}.                               \tag{10}
\]

In the nondegenerate case V>0, c>=s/m>m. For a fixed such c, the full
feasible interval for b is

\[
 \frac{mc-s}{c-m}\le b\le\frac{s}{m}.                    \tag{11}
\]

If c=s/m the law already has q=0. Otherwise the interval is nonempty
and has positive length; positivity of all three weights means b is
strictly inside it. Direct substitution into G/2 yields

\[
 \frac G2=m-\frac{m^2}{c}
              -\frac{(mc-s)^2}{b c(c-b)}.                \tag{12}
\]

The coefficient (mc-s)^2 is positive. To minimize (12) at fixed c,
one must minimize b(c-b). This last function is strictly concave, so
its minimum on the interval (11) occurs at an endpoint, and every
interior value is strictly greater than the smaller endpoint value.
At the left endpoint p=0; at the right endpoint r=0. Both give
two-atom laws with the same prescribed moments and a strictly smaller
G than an interior three-atom law.

Reflection T->1-T treats a law with outer atom one. Thus no minimizing
law has three distinct atoms of positive weight. Every minimizer has
at most two atoms; the conclusion uses both reductions, not the
support bound alone.

## 6. Optimizing the two-atom separation

Assume 0<m<1 and 0<V<m(1-m). For a two-atom law at a<b, set
x=m-a>0 and y=b-m>0. The weights are y/(x+y) and x/(x+y), and

\[
 xy=V,\qquad \frac G2=\frac{V}{x+y},\qquad
 \frac{V}{1-m}\le x\le m.                              \tag{13}
\]

The function x+V/x is strictly convex, so its maximum is at an endpoint
of this interval. The two endpoint laws and their separations are

\[
 \{0,s/m\},\qquad d_0=m+V/m=s/m,
\]
\[
 \{(m-s)/(1-m),1\},\qquad
 d_1=(1-m)+V/(1-m)=\frac{1-2m+s}{1-m}.                  \tag{14}
\]

Their difference is

\[
 d_0-d_1=(2m-1)\left(1-\frac{V}{m(1-m)}\right).          \tag{15}
\]

The first law is the unique minimizer if m>1/2, the second if m<1/2,
and both are minimizers if m=1/2. Strict convexity excludes any other
two-atom support in the nondegenerate case. Combining (5), (13) and
(14) gives the symmetric expression

\[
 C_{\max}=A-V\min\left\{\frac{m}{s},
                   \frac{1-m}{1-2m+s}\right\},           \tag{16}
\]

which simplifies to (2).

All degenerate cases are explicit. If V=0, the only law is delta_m,
the profile is 1_{u>=1-A}, and C=A. If V=m(1-m), the identity
E[T(1-T)]=0 forces the unique endpoint law with masses 1-m and m;
the profile is the constant A and C=A^2. If m=0 or m=1 the law is
the corresponding single endpoint mass and the profile is respectively
one or zero. These conventions resolve any indeterminate fraction in
(16); no division by a zero variance is used.

## 7. Every upper equality profile

For 0<A<1 and A/2<B<B_max, put m=1-A, s=1-2B and V=s-m^2.

If A<1/2, the unique upper profile almost everywhere is

\[
 c=s/m,\qquad \rho=V/s,\qquad
 f_+(u)=\begin{cases}\rho,&0\le u<c,\\1,&c<u\le1.
                         \end{cases}                   \tag{17}
\]

Its law has masses rho at zero and m^2/s at c. The completed graph
first activates v to rho, then advances u to c, activates v to one,
and finishes u.

If A>1/2, the unique upper profile almost everywhere is

\[
 a=\frac{2B-A}{A},\qquad h=\frac{A^2}{2(A-B)},\qquad
 f_+(u)=\begin{cases}0,&0\le u<a,\\h,&a<u<1.
                         \end{cases}                   \tag{18}
\]

Its law has mass h at a and mass 1-h at one. Its graph advances u to
a, activates v to h, finishes u, and then completes v at u=1.

At A=1/2 and interior B there are exactly two upper equality profiles,
(17) and (18), interchanged by f(u)->1-f(1-u). They are distinct.
At B=A/2 both reduce to the same constant profile; at B=B_max both
reduce to the same threshold. These, together with A=0,1, are all
equalities. Values assigned at isolated jump points are immaterial;
completed oriented graphs are unique for a specified profile, up to
pauses and weak monotone reparametrization.

The classification follows from the strict reductions above. In
particular an average of the two distinct upper profiles at A=1/2
does not produce an additional upper equality case: strict concavity
of G, equivalently strict convexity of the squared profile norm, rules
that out.

## 8. Attainment of the entire vertical section

Fix a feasible (A,B). Let f_- be the frozen explicit lower-envelope
profile and choose the upper profile f_+ above; to make the construction
single-valued at A=1/2, choose (17). Put

\[
 J=\int_0^1(f_+-f_-)^2\,du,\qquad
 I=\int_0^1 f_-(f_+-f_-)\,du\ge0.                        \tag{19}
\]

The inequality follows from the frozen boxed projection/KKT proof for
the lower minimizer. In the terminal threshold and degenerate cases,
the profiles coincide and I=J=0. Both integrals in (19) are explicitly
computable from the finitely many affine pieces and jumps. Every

\[
 f_t=(1-t)f_-+t f_+,\qquad 0\le t\le1,
\]

is nondecreasing, lies in [0,1], and has the same A and B. Its last moment
is exactly

\[
 C(t)=C_{\min}+2It+Jt^2.                                 \tag{20}
\]

For J>0 and any desired C between the two envelopes, choose

\[
 \boxed{\displaystyle
 t=\frac{\sqrt{I^2+J(C-C_{\min})}-I}{J}\in[0,1].}         \tag{21}
\]

At C=C_min this is zero; at C=C_max it is one because
C_max-C_min=2I+J. Monotonicity of (20) proves the claimed range and
the required equality C(t)=C. If J=0, the only permitted C is their
common value and the unique profile is already known. Thus (21) is a
constructive realization, not only an appeal to connectedness.

The resulting profiles are piecewise affine with finitely many jumps,
so their completed graphs are actual continuous monotone paths with
finitely many segments. No mixture of separately observed paths is
substituted for this single graph.

Conversely every path obeys both sharp envelopes. This proves (3).
For an interior feasible pair the two envelopes are distinct: the
unique lower minimizer has a nonconstant affine ramp, whereas every
upper equality profile has the two-level form just classified. At
the two B-boundaries they coincide in the unique constant or threshold
profile.

For the two-coordinate multilinear source V=span{1,u,v,uv}, these are
also complete current coordinates. After an exact endpoint potential
is removed, every one-form g df-f dg is a linear combination of
du,v du,v^2 du,dv,u dv,u^2 dv. Their integrals are respectively
1,A,C,1,1-A,1-2B. Hence (21) realizes the entire specified pair current,
including the endpoint constants, whenever its three coordinates obey
(3). This statement does not infer a retained-gamma or full native
arithmetic decoder.

This is the complete body of these three moments for one pair of
coordinates. It is not a classification of all higher-arity source
compatibilities, the convex hull of all native currents, or a physical
energy optimum. Additional coordinates can be completed to obtain any
one chosen pair projection, but simultaneous pair assignments need
not be compatible with one common higher-dimensional path. No new
scientific job, numerical test panel or change of source measure is
required for this proof-only result.
