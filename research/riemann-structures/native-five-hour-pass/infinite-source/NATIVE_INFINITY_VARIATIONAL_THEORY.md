# Infinite-source variational certificate in the original observation

Status: new proof and acquisition interface; no optimizer acquisition is
asserted in this version. Scope: the literal source on the fixed primes
`2,3,5`, all continuous coordinatewise monotone paths, and the unchanged
Mellin measure. The local-product truncation below approximates the
infinite operator; it is not a physical-product horizon.

The contribution is an explicit finite algebra and tail interface for a
global infinite-horizon optimizer or an actual legal descent. It does not
repeat the already proved coefficient-frame theorem and does not identify
the post-renewal retained-gamma family or imply RH.

## 1. Exact dependencies and normalization

The following files are read at native head
`9421846721cd788ab01615c8b6d459d9de849df7`, under
`research/riemann-structures/native-six-hour/`:

| File | Exact Git blob |
|---|---|
| `ALL_HORIZON_THREE_PRIME_SOURCE_MOMENTS.md` | `2113ce2bef593e19ca647c12c4fbb3c0728572a2` |
| `EIGHT_QUADRATIC_LAST_ACTIVATION_CONE.md` | `b74e3bab62a60ef73ae269f634ffb1e9656e9e3f` |
| `NATIVE_EARLY_ACTIVATION_DESCENT.md` | `cafc01c4025ee670a52bb47890a771ea4b91c6f5` |
| `FIXED_PRIME_INFINITE_HORIZON_COMPLETION.md` | `851e4331c12d9f3f073ab73dca26baa33bd5e548` |
| `INFINITE_NATIVE_PHYSICAL_FAITHFULNESS.md` | `f7c42135e276a34d4da00279110666b0f4636080` |
| `NATIVE_OPTIMAL_PATH_GEOMETRY.md` | `dfc772647bcee407c174cbf4312acfc1ad8dd737` |

The primitive L-102707 is at
`ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`, blob
`6810bcece309b0c54ae6c8fc84b314990004549c`; L-102880 has blob
`d7330d114ebba1a7a16e22fa9ba6aa6b5eb7cdd6` at the same commit.
PR783 is imported at `9497db89e34669e2167c632c918c491bf6ee73ab`:
`research/exploratory/prs-765-766-770-781-proof-review/SOURCE_OBSERVATION_AND_EPSTEIN_WALL.md`,
blob `c271fb11e729c0c629500f46e47bb4d0d818eff7`. Its G.1--G.11 already
give the product-observation rank criterion, eventual Euclidean row frame,
and explicit inverse preconditioning. Those are not an original-measure
Gram computation or a claim that all tensor coordinates are attainable.

Put

\[
A(z)=\sqrt{1-z^2},\quad D(z)=\sqrt{1-z}-A(z),\quad
z_p(t)=p^{-1/2+it},\quad
S(t,x)=\prod_p(A(z_p)+x_pD(z_p)).
\]

Every root is its analytic power-series branch at zero. The current is

\[
F_\infty(t;\gamma)=2\int_\gamma\overline S\,dS,
\qquad E_\infty(\gamma)=\|F_\infty(\cdot;\gamma)\|_{L^2(\nu)}^2,
\qquad d\nu=|\widehat\kappa(t)|^2dt/(2\pi).
\tag{1}
\]

Thus the differentiated arithmetic index has phase `+it log n`.
The original ordered records, factor two, physical weights and all
equal-ratio aliases are unchanged. The exact positive measure mass is

\[
\nu_0=128(3+\sqrt2)\log2-288.
\tag{2}
\]

## 2. Finite algebra for the infinite Gram

For `a in {0,1}^3`, define
\(\phi_a=\prod_p A(z_p)^{1-a_p}D(z_p)^{a_p}\).
The inherited monomial decoder is an exact real integer array
`d[j,a,b]`, where `j=0` denotes the constant and `j=1,...,20` the
ordered moments in the source note. It satisfies

\[
2\int x^b\,d(x^a)=d_{0,a,b}+\sum_{j=1}^{20}d_{j,a,b}M_j(\gamma).
\tag{3}
\]

Here is a complete construction. Put `m=a+b`, `s=a-b`,
`I={i:m_i=1}` and `J={i:m_i=2}`. When `m=0` everything is zero.
When `J` is nonempty the constant is one and the coefficient on
`integral x^(m-e_i) dx_i` is `s_i` for each `i in I`.
When `J` is empty and `I` is nonempty, let `r=max I`: the constant
is `1+s_r`, and each retained `i!=r` coefficient is `s_i-s_r`.
When `I` is empty and `m!=0`, only the constant one remains.
Every coefficient has absolute value at most two.

Consequently, with `x=(1,M_1,...,M_20)`,

\[
F_\infty=\sum_{j=0}^{20}x_j Z_j,
\qquad Z_j=\sum_{a,b}d_{j,a,b}\phi_a\overline{\phi_b}.
\tag{4}
\]

Absolute convergence of the primitive weighted coefficient sums justifies
the finite algebra and all integrals. The complete moment dependence has
not grown at infinity. The actual twenty variation fields are independent
in the original Hilbert space by the imported faithfulness theorem.

Define the three holomorphic local products

\[
Q_0=A^2=1-z^2,\quad Q_1=AD=g-(1-z^2),\quad
Q_2=D^2=2-z-z^2-2g,\qquad g=(1-z)\sqrt{1+z}.
\tag{5}
\]

For `alpha in {0,1,2}^3`, put
\(U_\alpha(t)=\prod_p Q_{\alpha_p}(z_p(t))\) and
\(K_{\alpha,\beta}=\int U_\alpha\overline{U_\beta}\,d\nu\).
The original affine Gram is exactly

\[
\mathcal G_{jk}=\operatorname{Re}\sum_{a,b,c,d}
d_{j,a,b}d_{k,c,d}K_{a+d,b+c}.
\tag{6}
\]

This index order follows from `Z_j conjugate(Z_k)`; transposing it
without tracking the differentiated factor would change the interface.
All covariance entries are real because the coefficients are real,
`U_alpha(-t)=conjugate(U_alpha(t))`, and the original measure is even.
Thus 27 holomorphic products suffice; no 64-by-64 numerical source
inverse or new Fourier measure is required.

## 3. Explicit local-product truncation tails

Let `c_n=[z^n]sqrt(1-z)`. Then `c_0=1`, `c_n<0` for `n>=1`, and
`|c_n|` decreases. For `n>=2`,

\[
|[z^n]g|=|c_n|+|c_{n-1}|.
\tag{7}
\]

Indeed `sqrt(1+z)` has coefficient `(-1)^n c_n`; consecutive
coefficients have opposite signs from index one onward. The low terms
are `g=1-z/2-5z^2/8+3z^3/16-13z^4/128+...`.
For `0<q<1` and every integer `L>=2`, define

\[
T_L(q)=\frac{(|c_L|+|c_{L+1}|)q^{L+1}}{1-q}.
\tag{8}
\]

If `Q_i,L` retains exponents `0,...,L`, its omitted coefficient-q-norm
is at most `tau_0=0`, `tau_1=T_L(q)`, `tau_2=2T_L(q)`.
These bounds use the actual decreasing coefficients, not a replacement
unit bound. The exact full coefficient-q-norms are

\[
\begin{aligned}
m_0(q)&=1+q^2,\\
m_1(q)&=1+q-(1+q)\sqrt{1-q}-q^2/4,\\
m_2(q)&=2+q-q^2-2(1+q)\sqrt{1-q}.
\end{aligned}
\tag{9}
\]

To verify (9), the absolute series of `g` is
`2+q-(1+q)sqrt(1-q)`. In `AD`, the constant disappears and the
absolute quadratic coefficient changes from `5/8` to `3/8`.
In `DD`, the constant and linear terms disappear, the quadratic
absolute coefficient becomes `1/4`, and every coefficient from degree
three onward has twice the absolute size in `g`. This gives (9),
including all low-degree corrections.

Use `q_p=p^(-1/2)`. For a three-prime feature let

\[
M_\alpha=\prod_p m_{\alpha_p}(q_p),\qquad
\eta_\alpha=\sum_p\tau_{\alpha_p}(q_p)
                       \prod_{r\ne p}m_{\alpha_r}(q_r).
\tag{10}
\]

Telescoping the product proves
`sup_t |U_alpha-U_alpha,L|<=eta_alpha`. The prefix mass
\(m_{\alpha,L}=\prod_p\sum_{e=0}^L|[z^e]Q_{\alpha_p}|q_p^e\)
is a separately computable upper bound on `sup|U_alpha,L|`.
Hence the covariance error is bounded entrywise by

\[
\epsilon_{\alpha\beta}
=\nu_0\bigl(\eta_\alpha m_{\beta,L}
           +m_{\alpha,L}\eta_\beta+\eta_\alpha\eta_\beta\bigr).
\tag{11}
\]

This is the expansion into two cross terms and one tail-tail term.
Replacing prefix masses by full masses is valid but less sharp.
All roots, powers and (2) in this interface require outward arithmetic.
An upper bound in (8) is not an observed signed error.

The finite covariance can be evaluated in the original kernel without
time quadrature:

\[
K^{(L)}_{\alpha\beta}
=\sum_{e,f\in\{0,...,L\}^3}
\left(\prod_p [z^{e_p}]Q_{\alpha_p}[z^{f_p}]Q_{\beta_p}
                    p^{-(e_p+f_p)/2}\right)
\Gamma\!\left(\sum_p(e_p-f_p)\log p\right),
\tag{12}
\]

where `Gamma(v)=integral exp(itv)dnu(t)` is the unchanged kernel
autocorrelation. Local signed difference-frequency correlations may
reorganize (12), provided every term, including zero differences, is
retained. This rectangular local-exponent cutoff is not `nm<=H`.

Contract (11) with the absolute coefficients in (6), after any exact
integer aggregation, and add the directed error from (12). This supplies
an enclosure of every true `mathcal G_jk`, and therefore of all twenty
half-gradient components at every moment vector in a declared box.
For a simple uniform entry bound `epsilon`, the unaggregated multiplier
is `(sum_ab|d_jab|)(sum_cd|d_kcd|)`; source-sensitive aggregation is
preferable. An entry-radius matrix `E>=0` also gives the spectral
error bound `sqrt(||E||_1 ||E||_infinity)`.

Although `K^(L)` is a covariance matrix, its reshuffling in (6) need not
be the Gram of a common truncated primitive: separate product truncation
does not preserve multiplication identities. Do not assume that the
resulting approximate `mathcal G^(L)` is positive semidefinite or is an
actual finite-horizon energy. The true infinite Gram is positive
semidefinite by (1); spectral signs must be certified against its error
enclosure. No projection of negative approximate eigenvalues is allowed.

## 4. A global infinite-horizon optimizer certificate

For a candidate moment vector `x_*=(1,M_*)`, put
`theta_j=(mathcal G x_*)_j`, `j=1,...,20`.
These are the full source half-gradient components. For every actual
competing path the exact Hilbert identity is

\[
E_\infty(\gamma)-E_\infty(\gamma_*)
=2\sum_j\theta_j(M_j(\gamma)-M_j(\gamma_*))
 +\|F_\infty(\gamma)-F_\infty(\gamma_*)\|^2.
\tag{13}
\]

Consider `v=f(u)=clip(lambda+mu*u,0,1)`, with `mu>0`, completed by
its required endpoint vertical segments. Keep `w=0` until `(u,v)=(1,1)`
and then raise `w` to one. This is an actual monotone path. Write
`A=integral f`, `B=integral u f`, `C=integral f^2`. Its only nonzero
moments are

\[
M_1=A,\ M_7=C,\ M_{10}=1-2B,\quad
M_{12}=M_{13}=M_{14}=M_{18}=M_{20}=1.
\tag{14}
\]

Suppose the true infinite coefficients obey

\[
c:=\theta_7>0,\qquad
2c\lambda+\theta_1=0,\qquad
2c\mu-2\theta_{10}=0.
\tag{15}
\]

These are self-consistency equations, not a fit to finite horizons.
They make `f` the pointwise minimizer on `[0,1]` of
`c v^2+(theta_1-2theta_10 u)v`. Strict clipping regimes must be
verified when differentiating the moment formulas.

Form all eight quadratics from the inherited cone with `c_j=theta_j`:

\[
\begin{aligned}
p_{\sigma\tau}(z)&=(\theta_2-2\sigma\theta_{13}+\tau\theta_6)
 +(\theta_4-2\sigma\theta_{20}+\tau\theta_{15})z
 +(\theta_{17}-\theta_{18}-2\sigma\theta_{14}+\tau\theta_8)z^2,\\
q_{\sigma\tau}(z)&=(\theta_3-2\sigma\theta_{12}+\tau\theta_9)
 +(\theta_5-2\sigma\theta_{18}+\tau\theta_{16})z
 +(\theta_{19}-\theta_{20}-2\sigma\theta_{14}+\tau\theta_{11})z^2,
\qquad \sigma,\tau\in\{0,1\}.
\end{aligned}
\tag{16}
\]

**Certificate theorem.** If (15) holds and every polynomial in (16)
is nonnegative throughout `[0,1]`, the candidate is a global minimizer
of the complete infinite energy over all actual monotone three-coordinate
paths. No convexification of the source path set is required.

If all eight minima are at least `delta>0`, then, putting
`I=integral |v-f(u)|^2 du` and `J=integral w(du+dv)`,

\[
E_\infty(\gamma)-E_\infty(\gamma_*)
\ge 2c I+2\delta J+
\|F_\infty(\gamma)-F_\infty(\gamma_*)\|^2.
\tag{17}
\]

For the proof, remove the exact potential `w R(u,v)` of the source
one-form, with `R` as in the inherited coefficient map. The remaining
`w` cost is at least `delta w(du+dv)`, because the affine-in-`w`
coefficients interpolate between the corresponding endpoint polynomials
in (16). The planar projection identity gives at least `c I`.
Insert these two lower bounds in (13). All operations are valid for
continuous BV paths; endpoint vertical contributions remain in the
exact potential.

When `c,delta>0`, equality forces `J=I=0`. Monotonicity then forces
`w` to activate only after `u=v=1`, and the planar path to have exactly
the completed graph of the continuous clipped profile. Thus the oriented
image is unique, allowing pauses and weak reparametrizations. For a
both-clipped profile the imported Hausdorff estimate and its sharp
one-third exponent apply with this same infinite energy gap.

## 5. Required numerical acceptance interface

A successful acquisition must enclose the true infinite Gram, not simply
the matrix in (12). It must retain:

1. the literal decoder (3), local coefficients, complete correlation
   contraction and all outward tail bounds (8)--(12);
2. every declared candidate start and its outcome;
3. a two-parameter root box for (15), with strict clipping inequalities;
4. an interval Jacobian and an inward Krawczyk or equivalent existence
   certificate for the actual infinite equations;
5. positive `c` and nonnegative minima of all eight true quadratics,
   including endpoint and interior-vertex cases;
6. the complete original-energy enclosure and any strict `delta`.

For Krawczyk evaluation, use the actual outward-rounded box displacement
from its chosen center. A nominal radius must not omit any portion added
by rounding. Gram uncertainty is part of every function and derivative
enclosure. Existence and uniqueness inside the box are distinct from the
global path conclusion, which comes from (13)--(17).

For `h(z)=az^2+bz+c`, retain endpoints and also the value
`c-b^2/(4a)` when `a>0` and `-2a<b<0`. Interval lower-envelope
nonnegativity is a valid sufficient certificate. A negative upper-envelope
minimum refutes this cone; an uncertain lower-envelope sign is UNKNOWN.
Failure of the sufficient cone does not refute the candidate minimum.

## 6. Legal three-dimensional descent if the cone does not close

The imported early-activation construction extends to (1) because every
source field in (4) lies in the original Hilbert space. Fix the candidate
planar graph, mark a point `s0` in its `s=u+v` parametrization, activate
`w` from zero to `epsilon` there, continue the planar graph at that height,
then complete `w` to one at the endpoint. This is one legal path, not an
average of paths. The exact gauged field gives

\[
F_\infty(\gamma_\epsilon)-F_\infty(\gamma_0)
=\epsilon L(s_0)+\epsilon^2 Q(s_0),
\tag{18}
\]

where `L` is the tail integral of the vector `P1 du+Q1 dv`, and `Q`
the tail integral of `P2 du+Q2 dv`. Every component is a rational
polynomial integral on the finitely many clipped-profile segments.
Its energy difference is exactly

\[
2a\epsilon+(2b+\|L\|^2)\epsilon^2
 +2\operatorname{Re}\langle L,Q\rangle\epsilon^3
 +\|Q\|^2\epsilon^4,
\quad a=\operatorname{Re}\langle L,F_*\rangle,
\ b=\operatorname{Re}\langle Q,F_*\rangle.
\tag{19}
\]

If a directed upper bound `a_bar<0` is found, take any certified
`M_bar>=2|b|+(||L||+||Q||)^2`, `M_bar>0`. A positive rational
`epsilon<=min(1,-a_bar/M_bar)` then gives a strict energy decrease
of at most `epsilon*a_bar`. This is an actual infinite-source result
once its Gram errors are included. The complete rational path and its
source coefficients must be retained.

The scalar tail `a(s0)` is exactly the integral of the true half-gradient
`P1 du+Q1 dv`. Its nonnegativity for every mark is equivalent to absence
of any infinitesimal early-`w` descent on this fixed planar path.
Negative coefficients away from the graph are not a substitute.
If these tails are nonnegative, finite activations may still require
the quartic test, and general planar changes remain a separate problem.
The signed quadratic source term is never discarded. An interval merely
containing zero cannot be used as an exact first-order cancellation.

## 7. What success or failure establishes

All algebra and tails above are source theorems. The candidate optimum
is conditional until an actual directed root-and-support certificate
is supplied. A strict descent is an alternative positive result: it
exhibits a legal better path and rejects the proposed shape at infinity.
If neither predicate closes, the remaining numerical or support gap
must be recorded explicitly.

No all-prime uniform frame, arbitrary path-attainability of moment
vectors, common symmetry projector, or full retained-gamma decoder is
imported. PR783's Euclidean coefficient recovery and this original-measure
variational problem remain distinct. The whole calculation is finite in
source dimension but infinite in arithmetic exponents, with the latter
controlled by the declared analytic tail rather than a finite ladder.

## 8. Terminal-plateau obstruction and an exact two-coordinate repair

The following sharper fallback is suggested by a preliminary finite-product
calculation, but the theorem below is independent of that calculation.
No numerical sign is asserted here. Suppose the candidate has a nonempty
terminal plateau `v=1`, and choose a fixed `s<1` strictly inside it.
Put `l=1-s` and use the following actual infinite fields:

\[
X=Z_2+Z_4+Z_{17}-Z_{18},\qquad
Y=Z_6+Z_8+Z_{15},\qquad
Z=Z_{13}+Z_{14}+Z_{20}.
\tag{20}
\]

Raise `w` to `epsilon` at `(u,v)=(s,1)`, continue `u` to one with
`v=1,w=epsilon`, then finish `w`. Formula (18) becomes the explicit
identity

\[
L_s=l[X-(1+s)Z],\qquad Q_s=lY,\qquad
\Delta F=\epsilon L_s+\epsilon^2Q_s.
\tag{21}
\]

There are no integrations of the unknown candidate profile in these two
variation vectors. Their coefficients are rational whenever `s` is
rational. The candidate itself enters only through its true half gradient.
Define

\[
p=\theta_2+\theta_4+\theta_{17}-\theta_{18},\qquad
q=2(\theta_{13}+\theta_{14}+\theta_{20}).
\]

The first-order half-energy coefficient is

\[
a_s=l[p-q(1+s)/2].
\tag{22}
\]

**Terminal obstruction.** If the candidate has a nonempty terminal
plateau and `p-q<0`, it is not even a local minimum in the full legal
path class. Continuity makes (22) negative for every `s` sufficiently
close to one inside that plateau; (19) then gives a strict improving
path for a sufficiently small positive rational `epsilon`. A directed
certificate may instead choose one preregistered rational `s` and check
both plateau membership and `a_s<0` directly. A floating sign of `p-q`
does not discharge either gate.

More generally keep the entire prefix up to `(s,1,0)` fixed and replace
the remaining tail by ANY monotone path from `(s,0)` to `(1,1)` in
the `(u,w)` plane, still with `v=1`. Normalize `u=s+l xi` and put

\[
A=\int w\,d\xi,\qquad B=\int\xi w\,d\xi,\qquad
C=\int w^2\,d\xi.
\]

Relative to the original tail with `w` last, its field is exactly

\[
\Delta F=lA(X-2sZ)-2l^2BZ+lCY.
\tag{23}
\]

For a direct check, the changes of source moments are
`Delta M2=Delta M4=Delta M17=l A`, `Delta M18=-l A`,
`Delta M13=Delta M14=Delta M20=-2l(sA+lB)`, and
`Delta M6=Delta M8=Delta M15=l C`; all other moments are unchanged.
These follow from the endpoint identities
`integral u dw=1-l A` and `integral u^2 dw=1-2l(sA+lB)`.
Thus (23) retains the vertical activations and their exact weights.
The special profile `w=epsilon` almost everywhere gives
`(A,B,C)=(epsilon,epsilon/2,epsilon^2)` and recovers (21).

The attainable triples in (23) are exactly the complete pair body in
`NATIVE_PAIR_MOMENT_COMPLETE_BODY.md` at
`6aa24e9c81c5a618ae7b740872f48266a5a86892`, blob
`c81751156911e984a62e0664ef3a1312eab7c3bc`:
`0<=A<=1`, `A/2<=B<=A-A^2/2`, and
`C_min(A,B)<=C<=C_max(A,B)`. Every allowed triple has an actual
completed monotone graph. Therefore minimizing the original quadratic
energy obtained from (23) over this three-dimensional body gives the
exact best terminal repair for this fixed prefix, not a relaxation or
a finite-staircase ansatz.

A useful sufficient certificate is again two-parameter. Set
`U=l(X-2sZ)`, `V=-2l^2Z`, `W=lY`. At a proposed terminal field
`F=F_*+AU+BV+CW`, let
`a=Re<U,F>`, `b=Re<V,F>`, `c=Re<W,F>`.
If `c>0`, `mu>0`, and
`2c lambda+a=0`, `2c mu+b=0`, then the terminal profile
`w=clip(lambda+mu xi,0,1)` globally minimizes the original energy
among ALL repairs of this fixed prefix. The pointwise planar projection
gives support domination over every legal pair graph, and the squared
field remainder gives the exact quadratic comparison. This assertion
does not require the full three-coordinate cone (16).

This terminal optimum is a conditional subproblem optimum, not yet a
global three-coordinate optimum: moving the marked switch or changing
the prefix may lower the energy further. Its scientific value is a
source-defined repair with an exact admissible body and original metric,
and, when (22) is certified negative at a restricted-family minimizer,
a rigorous rejection of the last-activation shape at infinity.
