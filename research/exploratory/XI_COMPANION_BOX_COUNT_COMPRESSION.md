# Complete Xi companion box counts and finite physical compression

Status: PROPOSED SOURCE-BOUND FINITE THEOREM; independent exact-SHA review required.
Authoring base: 134a55016b4f3ea970dc8e5f03505d4e97afff07 (OA).
Scope: three fixed boxes; conditional finite-input, GLOBAL-output Hardy projections.
All frozen parents remain unchanged. RH remains open.

## 1. Exact statement

Keep the actual, unrescaled entire function and the exact constant scales
from OA1--3 and frozen L-106610/L-106620:
\[
 f(z)=\xi_{\rm R}(1/2+iz),\quad
 \xi_{\rm R}(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),
 \qquad
 \lambda_a=\left[\tfrac12\Re\psi(1/4+ia/2)-\tfrac12\log\pi\right]^{-1},
 \quad a\in\{32,64,128\}.                                      \tag{BC1}
\]
Each lambda is certified positive. It is fixed throughout its box; it is
neither a function of z nor the leading approximation 2/log(a/(2pi)).
These anchors are explicitly selected, not identified with a pre-existing
physical partition or a historical sufficiently-high threshold.
Put R_k=f^(k)-i lambda_a f^(k+1), C_k=f^(k)+i lambda_a f^(k+1),
Theta_k=R_k/C_k, and W=f f^(6)-f' f^(5).

**Unconditional finite theorem, under the pinned ball enclosure contract.**
On the complete boundaries of
\[
 \mathcal R_a=(a-6,a+6)+i(0,1)                               \tag{BC2}
\]
R5 never vanishes. The numbers of its zeros in these OPEN boxes, counted
with complex multiplicity, are respectively 3, 5, and 6. All fourteen are
individually enclosed in disjoint disks of radius 2^-120, are simple,
and satisfy C5 R0 C0 f6 W !=0. Thus all are genuine simple Theta5 zeros,
none is a Theta0 zero or pole, and all are genuine simple poles of the
native quotient R0*C5/(C0*R5). There is NO omitted strip at y=0:
the closed bottom edges themselves are certified zero-free.

Exact centers are the integers in DISKS divided by 2^180; decimals below
are only a readable index. Nine centers are inherited unchanged from OA.

| a | real parts of the complete root list, approximately |
|---|---|
| 32 | 27.42896148, 31.74349328, 35.84197025 |
| 64 | 58.23626889, 61.13482127, 63.83969145, 66.56110290, 69.35187959 |
| 128 | 122.88975741, 124.96551599, 126.99738772, 129.13759927, 131.30283449, 133.32267367 |

The five new roots have, in the corresponding order among the new nodes,
strict raw |Theta0| corridors (m/1000,(m+1)/1000), with m equal to
593,472,366,544,194. The last is NOT greater than 1/4. This packet makes
no claim that OA's nine-node >1/4 bound extends to every node.

**Conditional finite physical theorem.** Separately for each lambda_a,
assume Theta0 and Theta5 are inner in C+. Write
\[
 \Theta_0=\Gamma U,\qquad \Theta_5=\Gamma B               \tag{BC3}
\]
after their maximal common inner divisor is removed. Then all the listed
nodes survive as simple B zeros. In the boundary-dx Hardy norm, let
P_U project onto U H^2, let P_B project onto K_B=H^2 ominus B H^2,
and let E_a be the span of the fourteen-list's 3/5/6 kernels for this a.
The following strict bounds hold:

| a | global finite-input squared HS norm ||P_U P_Ea||_HS^2 | global operator norm ||P_U P_Ea|| |
|---|---:|---:|
| 32 | >1193/1000 | >748/1000 |
| 64 | >1551/1000 | >816/1000 |
| 128 | >1343/1000 | >747/1000 |

These also lower-bound the corresponding quantities for P_U P_B, where
the full squared HS norm is allowed to be infinite. They do NOT prove
that it is infinite. No decision that lambda_a lies outside GC's global
exceptional set is needed. No Fourier-band lower bound is asserted.

## 2. Complete boundary certification, not an argument sample

Traverse the rectangle counterclockwise starting at a-6. Divide every
edge into exact segments of length 1/16: 192 on each horizontal edge,
16 on each vertical edge, hence 416 segments including closure. The
explicit boundary() list fixes this coverage without a floating mesh.

For a segment midpoint c put h=1/32, rho=1/8, and R=1/4. The segment
is contained in |z-c|<=h. Let M be an outward upper bound on |f| on
the full rectangle [Re c-R,Re c+R]+i[Im c-R,Im c+R]. Scalar ball evaluation
of BC1 provides it. This rectangle contains the closed disk of radius R.
All these regions have 20<Re z<150 and -1<Im z<2. Consequently Im s=Re z
stays away from zero: neither Gamma(s/2) nor zeta(s) meets a pole, and
BC1's product is analytic on a neighborhood without removable-pole tricks.

If |w-c|<=rho, the circle |z-w|=rho remains in the R disk. Cauchy's
derivative estimate therefore gives |f^(j)(w)|<=j! M rho^-j. For F=R5,
\[
 \sup_{|w-c|\le\rho}|F(w)|
 \le M_F:=M(120\,8^5+\lambda_a720\,8^6).                  \tag{BC4}
\]
Writing F(c+z)=sum A_n z^n, a second application of Cauchy's estimate
gives |A_n|<=M_F rho^-n. Thus the analytic tail, not merely a formal
series truncation, satisfies
\[
 \left|F(c+z)-\sum_{n=0}^{31}A_n z^n\right|
 \le M_F\frac{(8h)^{32}}{1-8h},\quad |z|\le h.           \tag{BC5}
\]
The point series f(c+X)=sum v_j X^j is computed to cap39, and
\[
 A_n={(n+5)!\over n!}v_{n+5}
       -i\lambda_a{(n+6)!\over n!}v_{n+6}.                \tag{BC6}
\]
All needed indices are at most37. Horner evaluation on the exact
axis-aligned displacement ball encloses the degree31 polynomial over
the WHOLE segment. Adding the BC5 outward error radius to both real
and imaginary parts encloses F on the whole segment.

Separately evaluate F at every exact endpoint, and choose its complex
ball midpoint as an exact Gaussian rational vertex v_j. Enlarge each
segment image rectangle to include v_j and v_(j+1). Strict exact endpoint
comparisons show that this convex hull excludes zero: at least one of
its real or imaginary intervals has a strict sign. The fixture records
every such hull, scalar M, error bound and rational polygon vertex.

For each segment the actual image path and the straight rational polygon
edge lie in the same convex zero-free rectangle. Their straight-line
homotopy is continuous at shared vertices, avoids zero, and closes.
Hence the image F(boundary R_a) and the rational polygon have the SAME
winding number about zero. This is why a finite point plot alone would
not suffice and why our interval arc enclosure is load-bearing.

The polygon winding is computed with exact Fraction arithmetic. For an
oriented edge p->q put cross=p_x q_y-p_y q_x. Add1 if p_y<=0<q_y and
cross>0; subtract1 if q_y<=0<p_y and cross<0. Otherwise add0. This is
the positive-real-ray crossing rule with half-open endpoint convention.
Edges through zero are rejected; all hull guards already exclude them.
It returns exactly 3,5,6. The argument principle applies since F is entire
and the certified closed boundary is zero-free. There are no poles to
subtract and no rounding of a floating argument integral.

## 3. Individual roots and exhaustion of each box

All fourteen frozen dyadic centers are verified afresh, including the nine
from OA. At radius r=2^-120 enclose A=|F(c)| above, D=|F'(c)| below and
M2=sup|F''| above using the uniform rectangle jet through derivative8.
The exact rational inequality
\[
 (A+M2 r^2/2)2^{50}<Dr                                  \tag{BC7}
\]
implies Rouché's one-zero statement by comparison with F'(c)(z-c), as
proved in OA4--5. Thus each disk has exactly one simple zero. Reflected
xi_R(1-s) rectangular jets overlap the direct jets, including the correct
derivative signs. Nonzero C5,R0,C0,f6,W,F' guards are uniform on each
containing rectangle, as are all raw Theta0 modulus corridors.

Every disk is strictly inside its box; pairwise real intervals are
disjoint. Their counts add to 3,5,6, equal to Section2's complete counts.
There are therefore no additional R5 zeros anywhere in the open boxes.
This is not a global companion census, a count of Xi zeros, or a statement
about growing boxes, varying parameters, or the critical line.

## 4. Correct physical Gram and common-factor monotonicity

We personally rechecked CP2, CP6, CP9, CP11 and CP15. Use the unitary
Fourier convention f(z)=(2pi)^(-1/2)integral_0^infinity h(t)e^(izt)dt
and conjugate-linear-first inner products. For b_j=x_j+i y_j define the
UNnormalized inverse kernel v_j(t)=exp[-(y_j+i x_j)t]. Up to one common
nonzero phase and a positive scale these are reproducing kernels, so
\[
 G_{ij}=\langle v_i,v_j\rangle
 ={1\over y_i+y_j+i(x_j-x_i)}.                            \tag{BC8}
\]
For distinct C+ nodes G is positive definite: a linear combination of
these distinct exponentials vanishing in L2 vanishes analytically, and
its first n derivatives at zero give an invertible Vandermonde system.
Equivalently the Cauchy determinant is
\[
 \det G=\prod_j{1\over2y_j}
  \prod_{i<j}{|b_i-b_j|^2\over|b_i-\bar b_j|^2}>0.          \tag{BC9}
\]
Both matrix determinant and product are enclosed and crosschecked.

For any inner J, evaluation gives M_J^*v_j=overline(J(b_j))v_j and
P_(JH2)=M_J M_J^*. Since M_J is an isometry,
\[
 H_J:=(\langle P_{JH2}v_i,P_{JH2}v_j\rangle)_{ij}
       =V_J G V_J^*,\quad V_J=diag(J(b_j)).               \tag{BC10}
\]
The orientation is V G V*, NOT V* G V, with our convention. These are
projection values, not the numerator-transmitted operator M_J alone.

Under BC3 the local nonzero Theta0(b_j) guards imply Gamma(b_j)!=0,
so every node remains a B zero and E_a subset K_B. Moreover
Theta0 H2=Gamma U H2 is a subspace of U H2; both are closed. Their
orthogonal projections therefore satisfy
\[
 P_{UH2}-P_{\Theta_0 H2}\succeq0,
 \qquad H_U-H_{\Theta_0}\succeq0.                         \tag{BC11}
\]
An equivalent matrix proof, with V_Theta=V_U V_Gamma, is
\[
 H_U-H_{\Theta_0}
 =V_U(G-V_\Gamma G V_\Gamma^*)V_U^*\succeq0,              \tag{BC12}
\]
because the middle matrix is the Gram of projections onto K_Gamma.
This does not require Gamma constant, a globally zero-free raw numerator,
purity of the factors, or lambda outside any exceptional set.

Let T synthesize the finite v_j family. Then T* T=G and
Q=T G^(-1/2) is an isometry onto E_a. Finite matrix cyclicity yields
\[
 \|P_{UH2}P_{E_a}\|_{HS}^2
  =tr(G^{-1}H_U)\ge tr(G^{-1}H_{\Theta_0}).                \tag{BC13}
\]
For any nonzero Gaussian-rational coefficient vector c,
\[
 \|P_{UH2}P_{E_a}\|^2
 \ge {c^*H_Uc\over c^*Gc}
 \ge {c^*H_{\Theta_0}c\over c^*Gc}.                       \tag{BC14}
\]
The last expressions use ONLY raw Theta0 at actual surviving roots.
They are not claiming the raw and reduced matrices are equal. Their
upper enclosures are NOT upper bounds on the reduced quantities.

## 5. Certified compression arithmetic and boundaries

The actual b_j is only known to lie in its certified disk. We therefore
insert its full containing rectangular ball into every occurrence in
BC8 and insert the UNIFORM raw Theta0 ball into BC10. Dependency between
the unknown node and its function value is retained by inclusion: treating
these enclosures independently enlarges the result, never narrows it.
We do not evaluate the metric at the rational center and call it the root.

FLINT ball matrix inversion encloses G^-1. A second explicit Gauss--Jordan
row route gives overlapping trace bounds. BC9 supplies a separate positive
determinant product. The three enclosed RAW traces are approximately
1.19379484407755, 1.55139869173258 and 1.34315260013381. For BC14, RAYS is
an explicit Gaussian-INTEGER vector per anchor; no eigenvalue solver runs
in acceptance. The exact outward rational lower endpoints exceed respectively
(748/1000)^2, (816/1000)^2 and (747/1000)^2. The initial eigenvector search
was only a scout for these fixed integer inputs, not a proof step.

The test also reconstructs G, H, their inverse trace and the Rayleigh form
from the rational root rectangles and raw-value bounds using an independent
Fraction interval implementation. Every arithmetic operation rounds outward
to the dyadic grid 2^-160; reciprocals reject zero-containing intervals.
This route uses no FLINT matrix operations and independently proves the
same strict rational floors. It still depends on the special-function
enclosures supplying the node/value intervals; it is not a second Xi library.

The global-output qualifier is essential. From P_U>=P_Theta it does NOT
follow in general that ||Pi_I P_U v||>=||Pi_I P_Theta v|| for a prescribed
Fourier output band I. Inserting a noncommuting output projection destroys
this simple comparison. Nor is multiplication by U substituted for P_U.
No native outer-weight change is included here. CP remains an explicit
counterexample to infinite-height/coprimality implying global HS divergence.
Our finite lower bounds neither conflict with CP nor imply a cofinal floor.

The exact fixed-box census and the conditional global compression are
different conclusions: the former uses no innerness or RH hypothesis;
the latter explicitly uses innerness. Neither proves RH, high-T capture,
parameter stability, a growing-box census, or infinite Hilbert--Schmidt norm.

## 6. Replay and audit contract

The runtime and all44 native-file aggregate pins are inherited from OA:
python-flint0.9.0, FLINT3.6.0, CPython3.12.10, WindowsAMD64, 256-bit balls.
The new point Taylor evaluator uses cap39; local root jets use cap9.
Public caps are 192--512 precision bits, at most64 series coefficients,
matrix order6, polygon vertices500, 4096-bit rational components,
12,000,000 JSON bytes, 300,000 JSON nodes, and depth24.
Booleans cannot substitute for typed integers; floats, nonfinite JSON
numbers, duplicate keys, noncanonical rational pairs and cap breaches fail.

Eight direct frozen bindings authenticate all five OA files, CP's proof,
and both native phase/gauge notes by Git blob and LF SHA256. The actually
loaded five OA files must also match their frozen bytes; OA's own helper
authenticates its six transitive sources and native runtime before replay.
The new proof, producer, manifest and test have artifact locks, and the
fixture has a canonical payload seal. Acceptance reconstructs every arc,
every root, every matrix and every conclusion from fixed primitive inputs.
Resealing an edited fixture is not an acceptable substitute for replay.

The [official matrix API](https://python-flint.readthedocs.io/en/latest/acb_mat.html)
documents the inverse and matrix arithmetic; no approx-mode solver is used.
OA cites the official scalar/series enclosure contract and pinned FLINT
series documentation. We rely on that implementation contract, not on a
formal verification or an independent reimplementation of FLINT. Exact
rational winding and synthetic projection controls independently exercise
the finite algebra, not the correctness of special-function internals.

Smallest result-invalidating burdens: BC4--6's uniform analytic arc bound,
correct polygon orientation/coverage, BC10's conjugation convention, or
BC11's restriction to global output. All are explicitly proved above.
The next substantive burden is source-specific band/outer-metric capture
or a controlled varying-window family, not extrapolation of this finite table.
