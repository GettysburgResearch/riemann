# Affine averaging with the projectors retained: an exact dirty-fibre obstruction

**Status: proved finite operator identities and a scoped obstruction to one
proposed transfer.** Fixed endpoint projectors preserve the complete
affine variance gain when the comparison operator is centered correctly.
The actual local condition of a dirty edge is different: it fixes a
projective line and leaves a noncontracting determinant-incidence channel.
Arbitrary high-density good-state projectors do not remove that channel.

These statements neither lower-bound the full arithmetic dirty operator
nor disprove cancellation of its actual Möbius coefficients. The full
operator has additional list weights, prime averages, Fock weights and
archimedean restrictions. The conclusion is precise: the complete affine
variance identity and one-variable cancellation bounds do not by themselves
give a power contraction on each dirty fibre after its fixed-line
condition. A further conditional averaging or coefficient-specific estimate
is needed.

## 1. The positive projection lemma

Let `H=L^2(F_p)` use normalized counting measure. Let `Jf=E f` be the
constant projection, let `Pi=I-J`, and define

\[
 (U_{q,h}g)(x)=g(qx+h),\qquad q\ne0,
 \qquad K_{q,h}=U_{q,h}-J.
\]

Let `P,Q` be any two fixed multiplication projectors, and let `f,g` be
arbitrary. Then

\[
 \boxed{\quad
 \mathbb E_{q\ne0,h}
    |\langle f,P K_{q,h}Q g\rangle|^2
   =\frac{\operatorname{Var}(Pf)\operatorname{Var}(Qg)}{p-1}.
 \quad}                                                    \tag{1}
\]

Indeed `U_{q,h}` preserves constants, so the integrand is
`|<Pi Pf,U_(q,h) Pi Qg>|^2`. The affine action takes each ordered pair
of distinct points exactly once through all ordered distinct pairs.
Expanding the square gives (1), including for complex functions.
In particular its root mean square is at most
`||Pf||_2 ||Qg||_2/sqrt(p-1)`. No projector is discarded and no
exceptional-measure estimate is needed.

The same conclusion holds after conditioning on a label `lambda` if the
conditional affine law is uniform and the projectors and test vectors are
fixed after that conditioning. Average the right side of (1) over the
label. A conditional density bounded by `C` relative to uniform changes
the upper bound by at most the factor `C` in the squared estimate.

Correct centering matters. Without `J` the exact extra term is
`|E(Pf)|^2 |E(Qg)|^2`; mean-zero inputs need not stay mean zero after
multiplication. But that observation alone is not an obstruction to a
correctly centered operator. Formula (1) retains `P J Q`, exactly where
the comparison term belongs.

For an actual family `A_(q,h)`, still with fixed `P,Q`, (1) also gives the
useful comparison-error inequality

\[
\begin{split}
 &\left(\mathbb E|\langle f,P A_{q,h}Q g\rangle|^2\right)^{1/2}\\
 &\quad\le
 \frac{\|Pf\|_2\|Qg\|_2}{\sqrt{p-1}}
 +\|f\|_2\|g\|_2
   \left(\mathbb E\|P(A_{q,h}-K_{q,h})Q\|_{\rm op}^2\right)^{1/2}.
\end{split}                                                \tag{2}
\]

It is necessary to prove the second term small for the actual comparison
kernel. Replacing a major-arc integral by `J` without that verification
is not licensed by (1).

## 2. The fixed line in the actual dirty equation

In [Lü--Wang--Wu, arXiv:2610.20242](https://arxiv.org/pdf/2610.20242),
Section 4.4, equation (4.47), an incoming dirty prime `p=p_*` comes from
a recorded Fock coordinate `(p,ell)`. The incoming unshared product `a`
is divisible by `p`, while the complete departing product `P_full` is
not. Therefore the raw edge has, modulo `p`,

\[
          \det(z,z')=c\ne0,\qquad [z']_p=\ell,
          \qquad c=P_{\rm full}\pmod p.                   \tag{3}
\]

These are the retained local constraints, not an enlarged affine
average. Assume `p>=3`, as holds for the HLC prime ranges. Choose a
nonzero representative `v` of `ell`. Every allowed
target point is `z'=t v`, `t in F_p^*`, and (3) forces

\[
            z'=\frac{c}{\det(z,v)}v.                       \tag{4}
\]

Thus the source cannot lie on `ell`. Put

\[
 X=\mathbb F_p^2\setminus\ell,\qquad
 Y=\ell\setminus\{0\},\qquad
 \phi(z)=c v/\det(z,v).
\]

Equip `X,Y` with their uniform probability measures. Each target `t v`
has exactly `p` preimages: the nonzero linear functional `det(z,v)` is
prescribed to equal `c/t`. These fibres are disjoint and partition `X`.
Consequently the pullback

\[
                    Tg(z)=g(\phi(z))                       \tag{5}
\]

is an **isometry** from `L^2(Y)` to `L^2(X)`. It also preserves means.
Subtracting the constant map `J_(X,Y)g=E_Y g` leaves norm one on
mean-zero inputs. There is no factor `p^(-1/2)` on this conditioned
channel.

This calculation explains the difference from the complete affine action.
The dirty record fixes a line; it does not independently average the two
affine parameters. The source's separation condition then limits the
admissible omitted-list choices. That list-selection gain is not an
additional finite-field mixing factor.

## 3. Arbitrary endpoint good-state projectors retain the channel

Let `P=1_A` on `X` and `Q=1_B` on `Y`, with no restriction on how the
sets were defined. Any complete endpoint conditions represented on this
local model are retained, rather than reduced to the conditions along a
realized path. This does not assert that the integer source projector
factors through one residue class modulo `p`. Write

\[
 \delta_X=1-|A|/|X|,\qquad
 \alpha_Y=|B|/|Y|>0,
 \qquad r_y=|A\cap\phi^{-1}(y)|/p.
\]

Directly from the disjoint fibres,

\[
       (PTQ)^*(PTQ)=Q\,\operatorname{diag}(r_y)\,Q,
       \qquad \frac1{|Y|}\sum_y(1-r_y)=\delta_X.
                                                               \tag{6}
\]

Hence

\[
 \boxed{\quad
  \|PTQ\|_{\rm op}^2
    =\max_{y\in B}r_y
    \ge\max\{0,1-\delta_X/\alpha_Y\}.
 \quad}                                                       \tag{7}
\]

The same lower bound is available on mean-zero inputs supported in `B`
when `|B|>=2`. To see this, select the two points of `B` with largest
`r_y`. A function taking opposite values on those two points and zero
elsewhere has mean zero, and its squared norm ratio is their average.
That average is at least the average of all `r_y` on `B`, which is at
least `1-delta_X/alpha_Y`. Thus

\[
 \left\|P(T-J_{X,Y})Q\right\|_{
   \{g:Qg=g,\ E_Yg=0\}\to L^2(X)}^2
       \ge\max\{0,1-\delta_X/\alpha_Y\}.                    \tag{8}
\]

This retains every part of the endpoint projectors. If both exceptional
densities tend to zero, the lower bound tends to one. If their
conditional densities are unknown, a global exceptional-measure estimate
does not supply them. Neither alternative gives a small local operator
norm merely by appealing to complete affine variance.

The normalizations in (5)--(8) are probability normalizations of the local
incidence channel. They do not assert that its scalar coefficient in the
full HLC operator is one. The source's harmonic prime measures,
symmetrization and Fock damping must still multiply and combine these
channels. In particular (7) is not a lower bound for the full sum of raw
and comparison operators.

One related normalization can be checked in the source itself. In its
Section 4.4 the recorded-pair measure is `lambda_i(p,ell)=nu_i(p)`, and
an active prime entry also has measure `nu_i(p)`. Transferring an existing
recorded pair to an active list introduces no new prime or line draw.
The line probability was already accounted for when that coordinate
entered the expansion. A fresh `1/(p+1)` factor cannot therefore be
charged again at every dirty transfer to manufacture an extra contraction.

## 4. Strong one-variable cancellation does not remove the incidence

There is also a bounded explicit test pair for this local channel. Let
`p>=5`, `k=floor(sqrt(p))`, and parametrize `Y` by `t in F_p^*`. Put

\[
 g(t v)=\frac{(p-1)e_p(kt)+1}{p},\qquad
 f(z)=g(\phi(z)).                                          \tag{9}
\]

Both functions have mean zero, absolute value at most one, and squared
norm `1-2/p`. Their unprojected pairing is exactly
`<f,Tg>=1-2/p`. For arbitrary projectors as above, with
`delta_Y=1-alpha_Y`, removing the two exceptional sets and retaining the
centered comparison gives

\[
 \operatorname{Re}\langle Pf,(T-J_{X,Y})Qg\rangle
 \ge1-\frac2p-\delta_X-\delta_Y-\delta_X\delta_Y.           \tag{10}
\]

Indeed the `T` term is the average of
`1_A(z)1_B(phi(z))|f(z)|^2`. The deleted mass is at most
`delta_X+delta_Y`. Since both original means vanish, the magnitude of
the remaining `J` term is at most `delta_X delta_Y`.

In the determinant coordinate `s=det(z,v)`, the source test is the
reciprocal phase `((p-1)e_p(kc/s)+1)/p`. Both this function and the
target function in (9) have square-root bounds for interval sums twisted
by any multiplicative character modulo `p`:

\[
 \sup_{I,\chi\bmod p}
 \left|\sum_{n\in I}\chi(n)F(n)\right|
       \ll\sqrt p\log(2p),                                \tag{11}
\]

where `I` is an interval of residues and `F` is either test extended by
zero at zero. For the reciprocal test, complete the interval and use
the twisted Kloosterman bound
`|sum_(x!=0) chi(x)e_p(ax+b/x)|<=2sqrt(p)` when `ab!=0`;
the degenerate terms are Gauss sums. For the target test, Gauss sums
handle nonprincipal characters. For the principal character use the
geometric-series bound `O(p/k)=O(sqrt(p))`; the constant correction
costs at most one.

The finite-field input in this supplementary claim is the classical
twisted Kloosterman bound; see Keith Conrad,
[On Weil's proof of the bound for Kloosterman sums](https://kconrad.math.uconn.edu/articles/kloosterman.pdf),
*Journal of Number Theory* 97 (2002), 439--446, and the explicit bound
in Theorem 1 of
[Sungjin Kim's proof](https://www.csun.edu/~sungjin/WeilBound-CharacterTwistedSum.pdf).
No such input is needed for (1)--(8).

One can also test the finite arrays against ordinary small-modulus
Dirichlet characters. Split an interval into residue classes modulo
`q`, with `q<=p/(2k)`. For the target phase, each progression is a
geometric series, giving `O(p/k)` after summing its `q` classes.
For the reciprocal phase, completing each progression modulo `p` gives
`O(q sqrt(p) log(2p))`. Consequently all moduli
`q<=p^(1/8)` satisfy a bound `O(p^(5/8) log(2p))`, stronger than the
one-scale `p^(7/8+epsilon)` cap estimate in this modulus range.

These are explicit finite-scale cancellation tests. They are not a
construction of a global multiplicative sequence satisfying every
Dirichlet cap, and the tests are not asserted to be Möbius. They show why
using only such one-variable estimates to control a deterministic
reciprocal incidence loses essential two-variable information. The
pairing (10) remains of constant size despite (11).

## 5. A quantitative error bound when projectors vary with the average

For completeness, if `P_gamma,Q_gamma` vary with the affine parameter,
write their exceptional masses as `d_P(gamma),d_Q(gamma)`. The exact
decomposition

\[
 P_\gamma K_\gamma Q_\gamma-K_\gamma
    =(P_\gamma-I)K_\gamma Q_\gamma
                         +K_\gamma(Q_\gamma-I)
\]

and the permutation-plus-constant form of `K_gamma` give, for bounded
test vectors,

\[
\begin{split}
 &\left(\mathbb E_\gamma
    |\langle f,P_\gamma K_\gamma Q_\gamma g\rangle|^2\right)^{1/2}\\
 &\quad\le\frac{\sqrt{\operatorname{Var}(f)
                             \operatorname{Var}(g)}}{\sqrt{p-1}}
  +2\|f\|_\infty\|g\|_\infty
       \left(\mathbb E_\gamma(d_P(\gamma)+d_Q(\gamma))^2\right)^{1/2}.
\end{split}                                                 \tag{12}
\]

Each of the two error pairings is bounded by twice its exceptional mass
times the two sup norms. Thus (12) is a proved projection-error
inequality, not an informal permission to drop the projectors. A small
unconditional exceptional measure alone does not make its error a
fixed power or prove the conditional uniformity used in (1).

For the HLC application, a sufficient genuinely stronger input would
therefore establish a centered conditional affine law, with a small
comparison error as in (2), **after fixing the complete endpoint lists
and recorded line coordinates**. The raw dirty relation (3)--(8) shows
that such a law cannot be supplied by a single fixed-line channel. An
alternative is to estimate the coherent average over distinct line
labels or the actual signed coefficients before taking a norm. Neither
has been proved here. The precise gain from this attempt is the usable
fixed-projector identity (1), the explicit error inequality (12), and
the local obstruction (7)--(10) to the proposed unrestricted transfer.

## 6. Verification boundary

`check_projected_affine_operator.py` independently exercises the exact
centered affine identity with nontrivial fixed endpoint projectors,
the fixed-line fibre count, the compressed Gram matrix and its
mean-zero lower bound, and the two-term projector-error estimate.
Its arithmetic is rational and every acceptance remains active under
`python -O`. The finite checker does not certify the Kloosterman bound,
the HLC source's global estimates, or any new Möbius correlation.
