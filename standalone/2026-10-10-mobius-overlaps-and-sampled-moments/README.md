# Möbius overlaps, grouped cubic factors, and sampled moments

**Status: proposed research, 10 October 2026.** This continuation proves four component estimates and reductions toward the generalized inverse-moment program. The numerical overlap improvements use an explicit uniform pointwise or reciprocal-L premise. The reflected-family applications retain the pinned theta identities and local coefficient adapters. The sampling inequalities themselves require neither a zero-free theorem nor Möbius cancellation.

**The full short-row fourth moment, generalized diagonal moment hierarchy, and RH remain unproved. No new zero-free region or external novelty claim is made.** The results below are new contributions to this research packet, with their analytic dependencies stated separately.

The exact parent is PR [#917](https://github.com/GettysburgResearch/riemann/pull/917), commit `6b4723042b3d250024eef45cb1924f88f28e902c`. Newer sibling branches are used only at the immutable commits named in the proofs and [PROVENANCE.json](PROVENANCE.json). They are not merged into this branch.

## The question being attacked

For the actual Eisenstein inverse polynomial, with its literal nonunit zeros,

$$
A_u(D;W)=\sum_{(n,S)=1}\mu_K(n)\nu(n)(u/n)_6W(Nn/D),
\qquad
M_{2k}(D,H;W)=\sum_{0<Nu\le H}|A_u(D;W)|^{2k},
$$

the desired short-row bound is $M_{2k}(D,D^h)\ll_\epsilon D^{h+k+\epsilon}$, or a sufficiently strong averaged version. More generally, a cofinal sequence of fixed orders with height and excess $h_k,e_k=o(k)$ would suffice in the exact moment-to-zero reduction. The arithmetic estimate for those full moments is the missing premise, rather than a consequence of a finite computation.

This pass makes the overlap estimates stronger, proves a new bound for every fixed quadratic product, reduces how many scale observations the criterion needs, and improves a genuine reflected block even after all repeated-prime rows are included.

| Component | Proved statement in this packet | Analytic scope |
| --- | --- | --- |
| [Möbius overlap tails](MOBIUS_OVERLAP_TAILS.md) | All-degree designated-factor bounds; sharper sharp fourth-moment cutoff; grouped cubic double-triangle sectors in every fixed higher moment | Classical character sieves plus the displayed uniform pointwise premise; a sharper degree-three sharp tail additionally uses the interval/reciprocal premise |
| [Quadratic inverse products](QUADRATIC_INVERSE_PRODUCTS.md) | Every fixed product length, every nonzero row: $\min\{HR^2,HP+\sqrt HPR\}$ | Classical squarefree quadratic sieve plus uniform pointwise cancellation; no native sextic second moment |
| [Sampled moment criterion](SAMPLED_MOMENT_CRITERION.md) | Full lower-height averaged moments recovered from distributed apertures or a sparse finite grid, without a power loss | Sampling is unconditional; moment-to-zero conclusions retain an unproved sampled arithmetic estimate and the parent's exact moving-mask inversion |
| [Joint reflected blocks](JOINT_REFLECTED_BLOCKS.md) | Three-variable squarefree-row sieve and a separate physical all-row block theorem; energy $D^{5/2-\theta+\epsilon}$ in a specified long-dual block | The sieve uses classical inputs; the physical adapter uses the pinned source theta identities and coefficient structure |

## 1. Stronger common-factor tails without discarding the residual signs

The useful pointwise premise is uniform smooth-test cancellation with exponent $b>1/2$. It covers the indicated finite-order twists, polynomially growing rows and exclusions, and a fixed finite number of test seminorms. The value $b=7/8$ is a source-qualified input here; this packet does not independently prove that zero-free claim.

Let $T_{\ge C}$ be the exact portion of $A_u(D)^2$ whose two original column ideals have common-factor norm at least $C$. The new bound is

$$
\|T_{\ge C}\|_2^2
\ll_\epsilon D^{4b+\epsilon}
\left[HC^{1-4b}+H^{1/3}C^{2-4b}
+H^{2/3}C^{5/3-4b}\right].
$$

The proof leaves the common factor as an oscillating cubic sum and retains Möbius cancellation in both residual inverse factors. An exact forward Euler correction restores every disjointness condition. Its nonconstant terms always involve at least two coordinates, which makes the required weighted correction summable. The sharp gcd indicator remains on the arbitrary-coefficient cubic axis; no unsupported sharp-test pointwise theorem is used.

At $b=7/8$, $H=D^h$, and $1<h\le11/10$, this reaches the fourth-moment diagonal scale $HD^{2+\epsilon}$ when

$$
\boxed{C\ge D^{(9-2h)/11}.}
$$

The parent cutoff was $D^{(6-h)/7}$. Their exponent difference is $3(1+h)/77$. At $h=21/20$, the cutoff decreases from $99/140$ to $69/110$; as $h\downarrow1$, it decreases from $5/7$ to $7/11$.

The same exact correction works for every fixed polynomial degree and for designated prime-incidence ideals, including ordinary subset gcds. For a designated incidence of multiplicity $m$, total original length $\mathcal P$, and resulting character order $r=3$ or $6$, the general bound is

$$
\|F_{I,\ge C}\|_2^2\ll_\epsilon
D^\epsilon\mathcal P^{2b}
\left[HC^{1-2mb}+H^{1/r}C^{2-2mb}
+H^{2/3}C^{5/3-2mb}\right].
$$

The proof separately states the quadratic and principal-mask cases and the nonempty support restrictions. These are estimates for exact polynomial portions, not a positive partition of the full moment.

## 2. An all-order quadratic component and a sharper degree-three tail

For a fixed product of inverse quadratic columns of lengths $L_i$, assume uniform pointwise exponents $b_i>1/2$. Set

$$
P=\prod_iL_i,\qquad R=\prod_iL_i^{b_i}.
$$

[Theorem 4.1](QUADRATIC_INVERSE_PRODUCTS.md) proves

$$
\boxed{
\sum_{0<Nu\le H}\left|\prod_iB_{i,u}(L_i;q_i)\right|^2
\ll_\epsilon D^\epsilon\min\{HR^2,HP+\sqrt HPR\}.
}
$$

The proof first handles all internal collisions of a physical product on squarefree rows. It then writes every row as $u=\varepsilon v^2a$, allowing the square base $v$ to overlap the squarefree remainder $a$. On each $v$-dyad it takes the smaller of the valid sieve and pointwise bounds, before summing the dyads. Every moving exclusion by $v$ is retained.

For one factor, the second term improves from the classical $\sqrt H L^2$ to $\sqrt H L^{1+b}$. At $b=7/8$, the diagonal scale $HL$ is reached for $H\ge L^{7/4}$, compared with the classical sufficient height $L^2$.

For $j$ identical factors this gives every fixed quadratic $2j$-th moment:

$$
\sum_{0<Nu\le H}|B_u(L;q)|^{2j}
\ll_{j,\epsilon}D^\epsilon
\min\{HL^{2jb},HL^j+\sqrt H L^{j(1+b)}\}.
$$

These are the quadratic components with net sextic exponent three. They are not the original sextic inverse moments with net exponent one.

Applying this estimate to the common factor of a degree-three polynomial gives

$$
\|G_{\ge C}^{(3)}\|_2^2
\ll_\epsilon D^{6b+\epsilon}
\left[HC^{1-6b}+\sqrt H C^{1-5b}\right].
$$

The sharp cutoff in this application uses an explicit reciprocal-L premise, from which the companion note proves uniform interval cancellation by truncated Perron. At $b=7/8$ and $1<h\le11/10$, the sufficient cutoff is $C\ge D^{9/17}$. A smooth pointwise estimate alone is not promoted to this sharp interval statement.

## 3. Grouping cubic factors reaches a larger low-overlap sector

In a sixth-moment expansion, take three unbarred and three barred positions. Let the repeated-prime ideals on each side form a triangle:

$$
q_{12},q_{13},q_{23},q_{45},q_{46},q_{56}\asymp R=D^r,
\qquad X=D/R^2,
$$

with all other repeated incidence ideals equal to one and six singleton lengths $X$. The pair coefficients are positive $\mu^2$, but their characters are cubic and remain oscillatory.

Grouping the three cubic factors on each side, and applying row Cauchy between the two entire groups, gives the complete signed-block bound

$$
\boxed{
|S_R|\ll_\epsilon HD^\epsilon X^{6b}
\left[R^3+H^{-2/3}R^6+H^{-1/3}R^5\right].
}
$$

The proof accounts for collisions inside each independent grouped product and then restores the original incidence disjointness with a mixed-sign correction. It does not estimate an arbitrarily deleted subcollection of signed tuples by monotonicity.

For $b=7/8$ and $h=21/20$, the diagonal target $HD^3$ follows at $r\ge19/55$. The comparison is for this exact matched configuration:

| Estimate | Sufficient lower exponent of $R$ |
| --- | ---: |
| PR #921, two singleton inverse axes | $1/2$ |
| PR #923, one-sided subset-product selector | $33/80$ |
| Present estimate, two individual cubic axes | $9/22$ |
| Present estimate, two whole cubic groups | $19/55$ |

The grouped gain over $33/80$ is $59/880$. The proof gives its full piecewise range for $1<h\le11/10$, with the switch at $h=27/26$.

These blocks have common gcd one on each side and no cross-side shared prime. They are not already covered by a nontrivial common-triple or global Hermitian gcd tail. Adding $k-3$ matched cross pairs embeds the same result in every fixed $2k$-th moment, $k\ge3$, with bound

$$
|S_R^{(k)}|\ll_\epsilon
HD^{k-3+\epsilon}X^{6b}
\left[R^3+H^{-2/3}R^6+H^{-1/3}R^5\right].
$$

This is an all-order theorem for a specified incidence family. It does not cover the full moment.

## 4. The moment criterion needs many fewer scale observations

For the parent's fixed universal test $W_*$, its infinite-convolution construction gives a uniform explicit bound at every derivative order:

$$
\sup_t\left|\frac{d^m}{dt^m}A_u(Xe^t;W_*)\right|
\le X B^{m+1}(m!)^2.
$$

This permits interpolation degree $m=o(\log X)$ with a controlled remainder. No derivative-moment conjecture is used.

There are two ways to supply the arithmetic data on $[X,2X]$:

* Retain a measurable set occupying a fixed positive fraction of every logarithmic cell of length at most $\ell_X$, where $\ell_X\log X\to0$. The retained fraction may even tend to zero under the quantitative condition proved in the note; for example, $\ell_X=(\log X)^{-1-\delta}$ and retained fraction $(\log\log X)^{-A}$ work for fixed $\delta,A>0$.
* Use an equally spaced logarithmic grid of $N_X=\lceil(\log X)^2\omega(X)\rceil$ intervals, where $\omega(X)\to\infty$ arbitrarily slowly. With $D_j=X\exp(j\log2/N_X)$ and $\Delta_X=\log2/N_X$, it suffices to bound the positively weighted sum $\Delta_X\sum_jM_{2k}(D_j,D_j^h;W_*)$.

Either kind of sampled bound with exponent $h+k+e$ recovers

$$
\int_X^{2X}M_{2k}(D,X^h;W_*)\,\frac{dD}{D}
\ll_\epsilon X^{h+k+e+\epsilon},
$$

with no power loss. The recovered height is fixed at $X^h$ throughout the dyad. Its stepwise envelope is comparable to $D^h$, which is sufficient for the exact sixth-power replica inversion. The resulting conditional zero-free boundary for the fixed twist family is

$$
\boxed{\Re s>\frac12+\frac{5h}{12k}+\frac e{2k}.}
$$

The sampled arithmetic bound remains unproved. The theorem reduces the amount of arithmetic information needed; it does not supply that information.

The note also constructs different fixed Mellin detectors with slower derivative growth. One permits a grid of order

$$
\log X\,\log\log X\,(\log\log\log X)^{1+\delta}\omega(X).
$$

Each test is fixed before $X$ varies, and its Mellin transform is nonzero on $\Re s>0$. An arithmetic estimate for one detector is not silently transferred to another. Existing real signed-remainder inequalities can be sampled with positive weights directly; an upper bound for the signed average suffices, without an inserted absolute value.

Finally, a separate unconditional modulation theorem gives

$$
\frac1{2T}\int_{-T}^{T}M_{2k}(D,H;y^{i\tau}W)\,d\tau
\ll_{k,\epsilon}HD^{k+\epsilon}(1+D^k/T).
$$

Its growing aperture does not yield the fixed-test estimate: restricting it by positivity to a fixed modulation interval restores a power cost at least linear in $k$. The proof and this limitation are both retained.

## 5. A reflected-block gain survives all repeated-prime rows

The new three-variable sieve averages the negative allocation $g$ jointly with the quadratic product column $gn$. It handles the actual common divisor $(g,n)$ and the moving row mask $(k,e)=1$ before applying any sieve.

For the physical family, a separate local adapter uses the source conductor shortening when $k=s v^2$. Its reflected length is

$$
U_v\asymp U_0\frac{R_v^2}{(Nt)^2(Nv)^4},
\qquad U_0=\frac{H^2EG^2}{BFC^3}.
$$

The row-prime Ramanujan amplitude at valuation two is the limiting local term. An absolutely convergent Euler sum with exponent strictly below $1/3$, followed by a fixed positive margin absorbed into $D^\epsilon$, proves the physical block estimate

$$
\sum_{0<Nk\asymp H}|\mathcal C^\psi_{E,F,G,C}(k)|^2
\ll_\epsilon D^\epsilon
\left[
\frac{HE}{G}\Lambda+\frac HG+
\frac{HE^{2/3}}G\Lambda+E\sqrt H+U_0+(EU_0)^{2/3}
\right],
\quad \Lambda=\min\{1,(G/U_0)^{1/3}\}.
$$

Here $\psi$ is a fixed smooth cutoff on a compact positive annulus of the actual transformed-weight argument. It is inserted after the valid complete-group pruning. The theorem includes every nonzero row, all square factors and sixth-power copies, all fixed bad-prime parts, and all source cusps. It is a theorem for this specified reflected component, not an arbitrary-coefficient all-row extension of the squarefree-row sieve.

For $A=B=D$, $H=D^{3-\theta}$, $E=G=D^{1/2}$, $F=1$, $C=D^{3/2-2\theta/3}$, and $0\le\theta<1/2$, one has $U_0=D^2$ and

$$
\sum_{0<Nk\asymp D^{3-\theta}}|\mathcal C^\psi(k)|^2
\ll_\epsilon D^{5/2-\theta+\epsilon}.
$$

The preceding angular two-axis estimate for the squarefree-row block gave $D^{35/12-\theta+\epsilon}$; the new exponent is lower by $5/12$ and remains valid for the indicated physical component over all rows. The new sieve step does not need angular reciprocal cancellation. Its use of the physical coefficient identity remains source-conditional.

The high-frequency blocks with small cube index still contain the unsaved terms $U+(EU)^{2/3}$. No sum over those blocks or over all small transformed-weight ratios has been shown to meet the required full moment bound.

## 6. A concrete next arithmetic target

Under the stated $b=7/8$ pointwise premise, fix $1<h\le11/10$ and put $\gamma=(9-2h)/11$. Write the exact polynomial identity

$$
A_u(D;W_*)^2=T_{\ge D^\gamma}(u;D)+T_{<D^\gamma}(u;D).
$$

The first term now has a proved diagonal row-energy bound. On the grid from Section 4, the following is a sufficient remaining fourth-order estimate:

$$
\boxed{
\Delta_X\sum_{j=0}^{N_X}
\sum_{0<Nu\le D_j^h}
|T_{<D_j^\gamma}(u;D_j)|^2
\ll_\epsilon X^{h+2+\epsilon}.
}
$$

This is still open. It would supply the full sampled fourth moment by the positive inequality for the two polynomial pieces. Sampling is then applied to the original smooth fixed-row function $A_u$, not to a moving sharp-cutoff remainder. The resulting conditional boundary is $1/2+5h/24$; obtaining these estimates for heights arbitrarily close to one would reach the proposed $17/24$ target.

For a result approaching the full hypothesis, the corresponding arithmetic excess must be sublinear along cofinal fixed moment orders. On the fully singleton sector, the two-native-moments-plus-pointwise architecture still gives excess $(2b-1)(k-1)$, which is linear in $k$. At $b=7/8$, it is $3(k-1)/4$ and its extracted limit returns to $7/8$. The new overlap and reflected-block bounds do not remove that surviving singleton contribution. A new signed arithmetic cancellation estimate there is the smallest material gap.

## Review and reproducibility

The four complete proofs identify hypotheses, strict domains, row and character conventions, normalization, imported inputs, and what remains open. Exact finite diagnostics exercise primitive character zeros, local corrections, interpolation and endpoint geometry, square-part decompositions, and rational exponent comparisons. They do not prove the large sieves, pointwise cancellation, theta automorphy, an infinite moment estimate, or a zero-free statement.

The full intended mathematical source is frozen before exact-commit review. [REVIEW.md](REVIEW.md) records the resulting scoped nonauthor agent audits and the frozen source identity; [VALIDATION.md](VALIDATION.md) gives replay commands, acceptance rules and finite coverage. [PROVENANCE.json](PROVENANCE.json) binds the proof/checker bytes and immutable source files. Review and publication receipts may be appended without rewriting the frozen mathematical source. No human acceptance or Lean formalization is claimed.

