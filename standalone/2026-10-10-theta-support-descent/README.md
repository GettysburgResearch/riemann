# Theta support descent and fixed angular second moments

**Status: proposed standalone research, with source-conditional analytic proofs and scoped independent AI-agent reviews.** This packet proves exact support cancellation in the coupled completion, extends the imported second-moment argument to fixed angular types, enlarges the domain of a reunited Euler factor, and continues the complete reunited standard-face series meromorphically across its former \(v=1\) boundary. The full fourth moment, the generalized diagonal moment hierarchy, and RH remain open.

The base is PR [#915](https://github.com/GettysburgResearch/riemann/pull/915), frozen at 9959364671f89b86f3992ec5ed5e19f804eb607b. The underlying analytic source is the October 5 manuscript from OpenAI/math, frozen at adc7f1241b42e322a6451854ab7e4b4c146bf78a and physically retained in the October 7 import. The new proofs use its theta automorphy and cusp expansions; the angular moment also uses its arithmetic, sieve, and finite-descent inputs. This packet does not claim a new independent verification of that imported foundation, a Lean build, or integration into the accepted results.

## 1. The question being attacked

Over \(K=\mathbb Q(\omega)\), put

\[
A_u(D;W)=
\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D),
\qquad \chi_n(u)=(u/n)_6,
\]

with the inherited primary-generator convention, fixed finite-order \(\nu\), fixed bad set \(S\), and the literal zero extension at nonunits. The requested result is

\[
\boxed{\quad
\sum_{0<Nu\le H}|A_u(D;W)|^{2k}
\ll_{k,\theta,\epsilon,\nu,S,W}HD^{k+\epsilon},
\qquad H=D^{1+\theta}.
\quad}                                                    \tag{1.1}
\]

This is required for every fixed integer \(k\ge1\) and every arbitrarily small fixed \(\theta>0\). Rows are all nonzero elements; sixth powers and imprimitive rows cannot be deleted.

The extraction argument in [the earlier moment packet](../2026-10-10-sextic-moment-descent/GENERAL_MOMENT_ATTACK.md) sends (1.1) to the limiting fixed-character boundary

\[
\beta_k=\frac12+\frac{5}{12k}.
\]

In particular \(k=2\) would give \(17/24\), and unbounded fixed orders would approach \(1/2\). The [exact hierarchy discussion](../2026-10-10-sextic-moment-descent/MOMENT_OBSTRUCTIONS.md) shows that the unrestricted hierarchy has the strength of GRH for the represented sextic row-twist family. Here \(H\) is an arithmetic norm cutoff; it is not the height of a zeta zero.

The new results below address specific obstacles in that proof route. They do not establish (1.1) for \(k=2\) or higher.

## 2. Exact support cancellation at every source cusp

The first coupled reflection has the local Ramanujan factor

\[
R_p(x)=-1+Np\,\mathbf1_{p\mid x}.
\]

For squarefree \(a\), retain its positive divisibility condition intact:

\[
\prod_{p\mid a}R_p(x)
=\sum_{dg=a}\mu_K(g)Nd\,\mathbf1_{d\mid x}.                 \tag{2.1}
\]

The prior three-way allocation is recovered only after expanding
\(\mathbf1_{d\mid nb}=\sum_{ef=d}\mathbf1_{e\mid n}
\mathbf1_{f\mid b}\mathbf1_{(f,n)=1}\).
Keeping the full projected theta sum in (2.1) allows a second transformation before taking its absolute value.

Let \(V^\sharp\) be the exact inherited transform of a compact smooth \(V\), with \(\operatorname{supp}V\subset[u,R]\). The opposite horizontal derivative has the same gamma kernel and the opposite angular phase. In raw Fourier-norm coordinates its second transform is exactly

\[
\mathscr H_0[V^\sharp](x)=V(27x).                          \tag{2.2}
\]

The factor 27 is retained explicitly. The resulting support identity is proved in [OPPOSITE_DERIVATIVE_REFLECTION.md](OPPOSITE_DERIVATIVE_REFLECTION.md).

[ALL_CUSP_REFLECTION.md](ALL_CUSP_REFLECTION.md) proves the necessary extension to every source cusp. For a translation \(\beta=a/c\), it constructs a matrix with the **original** denominator \(c\), even after transforming the cusp representative. The construction reduces to exactly the three supplied cusp expansions and preserves \(Nc\le Nq\) for a multiplier of period \(q\). No additional cusp expansion is assumed.

Since every nonzero frequency has \(N\ell\ge1/81\), the completed sum

\[
\mathcal S_{\sigma,F}(X)=
\sum_{\ell\ne0}\frac{d_\sigma(\ell)F(\lambda^4\ell)\alpha(\ell)}
{\sqrt{N\ell}}V^\sharp(N\ell/X)
\]

satisfies

\[
\boxed{\quad X>3R(Nq)^2
\quad\Longrightarrow\quad
\mathcal S_{\sigma,F}(X)=0.\quad}                         \tag{2.3}
\]

For the projected allocation \(a=dg\), its period is \(q=Mkd\), whereas its initial raw scale is
\(X=(Nc_0)^2(Nk)^2(Na)^2/B\).
The row norm cancels from (2.3). Consequently every complete grouped contribution with

\[
\boxed{\quad Ng>C_S\sqrt B\quad}                          \tag{2.4}
\]

vanishes, uniformly in the row \(k\), at every source cusp. The constants are explicit in the proof. In standard-face coordinates the condition is
\((Ng)^2>81cR(NM)^2B\); in raw coordinates it is
\((Ng)^2>3R(NM)^2B/(Nc_0)^2\).

At balanced lengths \(A=B=D\), the complete all-negative contribution \(d=1,\ g=a\asymp D\) is therefore exactly zero once \(D\) is sufficiently large. Every surviving group has \(Nd\gg D^{1/2}\).

[RAMANUJAN_SUPPORT_PRUNING.md](RAMANUJAN_SUPPORT_PRUNING.md) gives the exact arithmetic consequence and the necessary order of operations. The squarefree-index, cube-index, and ramified sums must remain complete for the fixed group. An individual dyadic piece need not vanish. Multiplying a group by any additional coefficient of its outer ideal \(a\) preserves its pointwise zero, but does not create a new higher-moment completion theorem.

### Why this does not yet close the fourth moment

The normalized additive Fourier transform satisfies

| Local function | Frequency \(h=0\) | Frequency \(h\ne0\) |
|---|---:|---:|
| \(-1\) | \(-1\) | \(0\) |
| \(q\mathbf1_{x=0}\) | \(1\) | \(1\) |
| \(-1+q\mathbf1_{x=0}\) | \(0\) | \(1\) |

Thus summing the complete Ramanujan factor restores activity at every original divisor prime. Its full conductor contains \(ka\) again. The vanishing of a projected component is real, but the second reflection of the whole expression can reconstruct the original completion. A signed covariance estimate and removal of cube completion remain necessary.

## 3. A proved extension to fixed angular characters

[HIGHER_ANGULAR_SECOND_MOMENT.md](HIGHER_ANGULAR_SECOND_MOMENT.md) extends the source argument to

\[
\nu_{r,\rho}(n)=\alpha(n)^r\rho(n),
\qquad \alpha(n)=n/|n|,
\]

where \(r\) is a fixed integer and \(\rho\) is a fixed finite ray character. The angular factor is not treated as periodic.

The key identity is that a pure \(m\)-th horizontal derivative at a rational cusp has no lower-order or height-derivative terms:

\[
\partial_z^m F(g^{-1}(z+\beta,v))\big|_{z=0}
=\left(-\frac1{\bar c^2v^2}\right)^m
\partial_{\bar z'}^mF\!\left(-\frac{\delta'}c,\frac1{Nc\,v}\right).
\]

For \(m\ge1\) it kills every constant mode. Its Mellin functional equation keeps the same conductor exponent \(1-2s\); only a unit angular phase and fixed gamma parameters change. The proof checks the finite local transforms, the all-row mean square, cube inversion, both Poisson steps, and finite descent in the enlarged family. It also retains the finite smooth seminorms needed for the final Dirichlet-series continuation.

The actual inverse second moment is

\[
\boxed{\quad
\sum_{0<Nu\le D^{1+\theta}}
|A_{u,r,\rho}(D;W)|^2
\ll D^{2+\theta+\epsilon}\|W\|_{C^J}^2,
\qquad r\ne-1.
\quad}                                                    \tag{3.1}
\]

The exception is stated precisely. The canonical Gauss family excludes its angular parameter \(+1\), and the initial inverse Poisson calculation sends the inverse type \(r\) to the canonical type \(-r\). For inverse type \(-1\), this proof does not give the full-row second moment. Its fixed-row bound nevertheless follows by conjugating the covered inverse type \(+1\).

Sixth-power extraction therefore gives, for **every fixed integer \(r\)**,

\[
A_{1,r,\rho}(D;W)\ll D^{11/12+\epsilon}\|W\|_{C^{J_1}},
\]

and a source-conditional zero-free half-plane \(\Re s>11/12\) for the corresponding fixed angular Hecke \(L\)-function. This enlarges the character class. It does not strengthen the numerical zeta boundary already available in the inherited research, nor import the separate stronger \(7/8\) argument into this extension.

For the needed types \(r=\pm3\), the proof also establishes conductor uniformity:

\[
\boxed{\quad
|L(\sigma+it,\alpha^{\pm3}\rho)^{-1}|
\ll_{\delta,\epsilon}
[N\mathfrak q(2+|t|)]^\epsilon,
\qquad \sigma\ge11/12+\delta .
\quad}                                                    \tag{3.2}
\]

The proof supplies its own uniform polynomial growth estimate using cancellation of the odd finite part in Eisenstein lattice cells, then applies the analytic-logarithm argument. Every moving Euler mask is retained in \(\mathfrak q\). Thus (3.2) resolves the previously missing uniform angular reciprocal interface on this fixed interior half-plane. It does not control that reciprocal near \(1/2\).

## 4. A larger domain for the scalar Euler factor

[EULER_DOMAIN_EXTENSION.md](EULER_DOMAIN_EXTENSION.md) concerns the exact reunited Ramanujan Euler product at a **fixed theta index \(n\)**. Set \(v=w+r-1\), and at a prime put

\[
x=\chi^-_k(p)(Np)^{-w},\qquad
z=\kappa_k(p)(Np)^{-v}.
\]

The local identity

\[
\frac{(1-x+z)(1-z)}{1-x}
=\frac{1-z^2}{1-xz}
\left(1+\frac{x^2z-xz^2}{(1-x)(1+z)}\right)
\]

extracts an angular numerator \(L(w+v,\chi^-_k\kappa_k)\) and the finite-order reciprocal \(L(2v,\kappa_k^2)^{-1}\). The new remainder converges normally in

\[
\Re w>0,\quad \Re v>0,\quad
2\Re w+\Re v>1,\quad \Re w+2\Re v>1.                      \tag{4.1}
\]

The full local factors at primes dividing \(n\) remain present, and their uniform norm bound is
\((Nn)^{\max(0,1-\Re w)+\epsilon}\).
Extracting every finite initial collection of terms linear in \(z\) also continues the old remainder holomorphically throughout
\(\Re w>0,\ \Re v>1/2\).

The new reciprocal has fixed finite-order primitive character; it does not introduce another uncontrolled angular reciprocal. When \(\kappa^2\) is principal and \(\Re w>1/4\), there is a precise fixed-index zero at \(v=1/2\), after multiplication by the original angular denominator. A possibly divergent theta-index sum cannot be interchanged with that zero.

The note accounts for both angular numerator conductor costs in prospective coupled contour directions. These comparisons are not legal contour shifts for the full deformed theta series. Its continuation and bounds must be established separately.

## 5. Continuation of the full reunited series

The separate-factor restriction can be improved by keeping the cube completion intact. [DEFORMED_GAUSS_CONTINUATION.md](DEFORMED_GAUSS_CONTINUATION.md) conditions the squarefree theta index on a divisor \(d\), rather than bounding its deformation by its largest coefficient.

The relative divisor factor and the literal cube-mask quotient cancel exactly:

\[
h(p)=\frac{qx(1-y)}{1-x+z},
\qquad
\frac{L_{S,k}(r,\chi^+_k)}{L_{S,kd}(r,\chi^+_k)}
=\prod_{p\mid d}(1-y_p)^{-1},
\qquad
j(p)=\frac{qx}{1-x+z}.
\]

Consequently the complete reunited object is a sum of **entire completed theta series** \(\mathcal T_{k,d}(s)\). It has no remaining reciprocal of the cube \(L\)-function. The proof supplies the uniform moving-divisor estimate

\[
|\mathcal T_{k,d}(\sigma+it)|
\ll (Nk)^{A(\sigma)+\epsilon}(Nd)^{B(\sigma)+\epsilon}
(2+|t|)^M,
\]

where \(A=\max(0,1-\sigma,1-2\sigma)\) and
\(B=\max(0,(1-\sigma)/2,1/2-2\sigma)\).
The factor \( (Nd)^{-1/2}\) on the left boundary comes from the actual Ramanujan divisibility weights in the absolutely convergent dual theta series. It is retained before interpolation.

Writing \(\omega=\Re w\) and \(v=w+3s-3/2\), the full series continues holomorphically to the convex tube

\[
\omega>1,\quad \omega+\sigma>2,\quad
\omega+\tfrac32\sigma>\tfrac52,\quad
\omega+3\sigma>\tfrac52 .
\]

For \(\sigma\le0\), this reaches every \(\Re v>1\). The raw deformed Gauss series without its global cube factor has a separate, smaller continuation furnished by the angular reciprocal theorem: \(17/36<\sigma<1\) and \(\omega+\frac32\sigma>\frac52\).

The main continuation theorem uses the source theta inputs, with no zero-free assumption. Its conductor comparison is also explicit: on \(\sigma\le0\), the theta factor \((Nk)^{1-2\sigma}\) exactly cancels the negative row power in the literal Mellin scalar. At \(A=B=D\) the resulting size is \(D^{\Re v-2\sigma}(Nk)^\epsilon\). This gives analytic continuation but no saving in the long row range.

### 5.1 Crossing \(v=1\) while keeping the Möbius sign

[POST_REFLECTION_EULER_CONTINUATION.md](POST_REFLECTION_EULER_CONTINUATION.md) supplies a further reflection of that conditioned divisor series. The exact exponent-3/exponent-4 calculation cancels its angular and cubic Gauss factors. Its remaining divisor phase belongs to a finite family of fixed finite-order characters \(\zeta_b\). The negative Ramanujan term remains negative.

For a dual frequency index \(m\), its local divisor factor is

\[
1+\frac{u_p(-1+Np\,\mathbf1_{p\mid m})}{1-x_p+z_p},
\qquad u_p=\zeta_b(p)(Np)^{-v}.
\]

Extracting \(1-u_p\) gives the reciprocal \(L_{S,k}(v,\zeta_b)^{-1}\), with a normally convergent remainder. The dual cusp sum then converges normally under

\[
\boxed{\quad
\Re v>\tfrac12,\qquad
\Re s<\min(0,\Re v-1).
\quad}
\]

This proves a **meromorphic continuation of the full reunited standard-face object across \(v=1\)**. Its possible poles are the original principal-character divisor at \(v=1\) and zeros of a finite family of fixed Hecke \(L\)-functions. An inherited finite-order zero-free boundary \(1/2<\beta<1\) removes the latter in \(\Re v>\beta\). The conservative choice \(\beta=11/12\) is available from the same imported method. In that region the proof also gives uniform polynomial vertical bounds after removing the possible principal pole.

The possible residue at \(v=1\) is written explicitly as a normally convergent finite sum of cusp series. It may vanish. A reflected principal divisor character contributes a reciprocal zero, not an additional pole. The proof does not identify this residue with the signed initial Poisson diagonal.

This continuation still does not yield the desired moment estimate. Below \(v=1\), its absolute bound requires \(\Re s<\Re v-1\), so the balanced exponent satisfies
\(\Re v-2\Re s>2-\Re v\ge1\).
The gained analytic domain is therefore accompanied by an insufficient bound. The missing quantitative cancellation remains visible after the continuation has been proved.

## 6. Proofs, verification, and the next missing statement

| Item | Proof or evidence | Scope |
|---|---|---|
| Opposite derivative and exact \(V(27x)\) return | [Opposite reflection](OPPOSITE_DERIVATIVE_REFLECTION.md) | Source theta inputs; full standard completion |
| Denominator-preserving all-cusp reflection | [All-cusp proof](ALL_CUSP_REFLECTION.md) | Exactly the three source cusp sequences |
| Projected divisor cutoff and Fourier restoration | [Ramanujan pruning](RAMANUJAN_SUPPORT_PRUNING.md) | All-cusp completed groups, with row zeros |
| Fixed angular moments and moving reciprocal bounds | [Angular proof](HIGHER_ANGULAR_SECOND_MOMENT.md) | Source arithmetic and analytic inputs; explicit exceptional full-row type |
| Larger fixed-index Euler domain | [Euler proof](EULER_DOMAIN_EXTENSION.md) | Scalar factor; full theta continuation separate |
| Full reunited-series continuation | [Conditioned theta proof](DEFORMED_GAUSS_CONTINUATION.md) | Exact cube cancellation; uniform moving-divisor bounds |
| Continuation across the former \(v=1\) boundary | [Reflected divisor proof](POST_REFLECTION_EULER_CONTINUATION.md) | Meromorphic continuation, explicit possible residue, and finite-order pole control |
| Independent derivative and angular reconstruction | [Theta review](INDEPENDENT_THETA_REVIEW.md) | Exact file hashes; reviewer distinct from author |
| Independent all-cusp reconstruction | [All-cusp review](ALL_CUSP_INDEPENDENT_REVIEW.md) | Exact file hash; reviewer distinct from author |
| Independent support and finite-checker reconstruction | [Pruning review](PRUNING_AND_CHECKER_REVIEW.md) | Proof and explicitly bounded finite cases |
| Independent Euler and joint-series reconstruction | [Joint-series review](INDEPENDENT_JOINT_SERIES_REVIEW.md) | Separate exact-hash scopes for the Euler and continued series |
| Independent post-reflection reconstruction | [Arithmetic review](POST_REFLECTION_INDEPENDENT_REVIEW.md) and [separate full-series review](INDEPENDENT_POST_REFLECTION_REVIEW.md) | Two distinct reviewers; exact scalar, signs, domain, poles, and remaining exponent loss |

The finite diagnostics are reproducible:

~~~bash
python3 standalone/2026-10-10-theta-support-descent/checks/check_support_algebra.py \
  --output standalone/2026-10-10-theta-support-descent/checks/support_algebra_report.json
python3 standalone/2026-10-10-theta-support-descent/checks/check_euler_factors.py \
  --output standalone/2026-10-10-theta-support-descent/results/euler_factor_checks.json
~~~

The support checker uses exact Eisenstein integer arithmetic, cyclotomic coefficient identities, and rational scale calculations. It checks 1,350 cusp constructions, 1,554 divisor identities, 22,620 positive-divisibility projections, 192 Fourier equalities, and 96 scale cases. It includes cases where the transformed cusp denominator has a different norm or is zero, as well as counterexamples to an extra negative-branch coprimality restriction.

The Euler checker clears three polynomial identities, verifies linear extraction through order 12, tests 64 exact rational local cases including literal zero masks, and checks six conductor-exponent comparisons plus nine completed-domain cases. Both normal and optimized Python retain the explicit acceptance checks. These are finite algebra diagnostics. The analytic assertions require the written proofs and their stated source inputs; no finite calculation certifies RH or an infinite moment bound.

The next missing statement is quantitative cancellation for the **signed, long-dual, divisor-weighted covariance**, with a valid passage between the original Möbius polynomial and the completed theta expression. In the first unresolved fourth-moment initialization, product columns have length about \(D^2\) and dual rows extend to norm about \(D^{3-\theta}\). The source canonical descent does not enter this range. The present angular enlargement leaves those scales unchanged, and the support identity does not remove the full conductor after all allocations are summed.

This packet narrows the analytic work still required and removes specific incorrect majorants. It does not supply that missing covariance theorem.
