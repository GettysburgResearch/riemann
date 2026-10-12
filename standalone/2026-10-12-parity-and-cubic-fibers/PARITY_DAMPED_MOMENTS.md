# Parity damping, quadratic–cubic separation, and the cofinal norm obstruction

**Status:** proved algebraic and probabilistic reductions, a conditional estimate for an exactly specified damped arithmetic moment, and a method-specific obstruction. The undamped generalized moment remains open. The pointwise input below is an explicit premise when its exponent is less than one; no imported zero-free theorem is independently certified here.

The main positive result is the following. Give each good prime ideal an independent sign with mean `-(Np)^(-t)`, and leave the actual sextic coefficients, row set, column tests, and exclusions in place. Under the native uniform pointwise premise `PW_b`, the resulting positive `2k`-moment is

\[
 \mathcal F_{k,t}(D,H)
 \ll_{k,t,\epsilon} HD^{\,k\max\{1,2b-2t\}+\epsilon}.
 \tag{0.1}
\]

Thus the entire damped hierarchy is of diagonal size when `t >= b-1/2`. Counting alone gives the unconditional endpoint `t=1/2`. The separately assumed `b=7/8` gives `t=3/8`. This is an estimate for an exact signed parity-weighted sum in the original arithmetic moment, as well as for its probabilistic representation. It is not a bound for the undamped moment.

If the separately stated native second moment is also supplied, the stronger whole-family bound is

\[
 \mathcal F_{k,t}(D,H)
 \ll HD^{\,k+(k-1)(2b-2t-1)_++\epsilon},
 \qquad (x)_+=\max\{x,0\}.
 \tag{0.2}
\]

At `t=0` it returns the existing native second-moment/pointwise loss, and at `t=b-1/2` it reaches the same diagonal damped endpoint.

The damping variable acts on the product of the primes of **odd total tuple multiplicity**. It therefore acts on the fully singleton sector left by the recent graph and cubic-overlap theorems. An exact quadratic–cubic Walsh decomposition identifies what must cancel when the damping is removed. A common-spike model then proves that even all fixed integer-product sextic sieve inequalities, combined by arbitrary valid norm manipulations, cannot make the undamped excess sublinear in the moment order at cofinal row heights.

## 1. Source boundary and native data

The comparison sources are pinned as follows; their exact bytes, Git blobs, and SHA-256 identities are recorded in `sources/repository_sources.json`.

* PR #927, commit `f9939c957f5aac6b2099b591e4988991700a152b`, packet `standalone/2026-10-10-sextic-signed-reunion/`: `HIGHER_CUBIC_POOLS.md`, `MIXED_CUBIC_REPLICATION.md`, and `SMALL_W_CORE_AUDIT.md`. The last file's equation (1.5) returns the complete signed auxiliary sum to the original native centered energy. The other two files leave the all-singleton balanced core unchanged.
* PR #928, commit `ab98878279cd5614fe79bb94aa916e97c9ee50b4`, packet `standalone/2026-10-10-signed-graph-and-joint-descent/`: `ARBITRARY_GRAPH_SECTORS.md` and `DENSE_CROSS_GCD_SECTORS.md`. Their selectors depend on shared incidence ideals. When those ideals are all one, their charge is zero.
* PR #923, commit `1a1152008706f7e24fa1efe4990588f8f99c5d8d`, `standalone/2026-10-10-sextic-separated-cores/SUBSET_PRODUCT_INCIDENCE.md`, Lemma 2.1: the whole physical-product sextic bound used in Section 8. Its source is PR #913, commit `6498d6cc2eded03159c7332b25fd224ad07f89c1`, `standalone/2026-10-10-sextic-moment-descent/REFINED_ALL_ROW_SIEVE.md`.

Fix `K=Q(sqrt(-3))`, its good-prime primary-generator convention, a finite bad set `S`, and a fixed finite-order Hecke datum `nu`, unramified outside `S`. At a good squarefree ideal `n`, put

\[
 \xi_u(n)=\nu(n)\chi_n(u),\qquad
 \chi_n(u)=\left(\frac un\right)_6.
 \tag{1.1}
\]

All symbols retain their literal zero at a nonunit. On nonsquarefree correction ideals they are extended completely multiplicatively, with the same zeros. The value at the unit ideal is one. Every nonzero element row is retained, including all six units and every repeated prime-power row. A good-prime column exclusion is the exact condition `(n,qS)=1`, where `Nq <= D^B` for a fixed `B`; `q` need not be squarefree.

Let `W` be a fixed smooth compactly supported function on `(0,infinity)`, with support contained in `[alpha,beta]`, `alpha>0`. Put

\[
 A_u^{(q)}(X;W)=
 \sum_{(n,qS)=1}\mu_K(n)\xi_u(n)W(Nn/X).
 \tag{1.2}
\]

Use an ambient parameter `D>=2`. The pointwise premise is required at **every nonempty shorter scale in the same physical row range**:

\[
 |A_u^{(1)}(X;V)|
 \ll_{\epsilon,B_0}D^\epsilon X^b\|V\|_{C^{J_b}},
 \quad 0<Nu\le D^{B_0},\quad c\le X\le C D,
 \qquad \frac12\le b\le1.
 \tag{PW_b}
\]

Here the compact support range of `V`, the positive lower bound `c` for nonempty scales, and `C,B_0` are fixed; the finite seminorm exponent is uniform over the displayed test family. The constants may depend on these fixed data, `S,nu,b`, and the requested loss, not arbitrarily on `u,X`, or an exclusion. The case `b=1` follows from ideal counting. The smaller exponents are separate analytic premises. Section 4 proves the precise moving-exclusion adapter needed below from this unmasked premise.

Let `w_H(u)>=0` be any finite row weight supported in this physical row range and satisfying

\[
 \sum_{u\ne0}w_H(u)\ll H.
 \tag{1.3}
\]

A sharp norm ball or a fixed nonnegative compact smooth profile at height `H` has this property. Nonnegative Schwartz profiles can be used whenever the premise is supplied on their row annuli with the usual uniform reference-scale bounds; that extension is not needed for the statements here. Define

\[
 M_{2k}^{(q)}(D,H;W)
 =\sum_{u\ne0}w_H(u)|A_u^{(q)}(D;W)|^{2k}.
 \tag{1.4}
\]

Every moment order, damping parameter, conductor exponent, and test is fixed independently of `D`. No estimate uniform in a moment order growing with `D` is asserted.

Only the optional refinement uses the additional weighted native premise

\[
 \sum_u w_H(u)|A_u^{(1)}(X;V)|^2
 \ll_\epsilon HD^\epsilon X\|V\|_{C^{J_2}}^2
 \tag{NM2_w}
\]

at every nonempty shorter scale in the same physical row range. This is a separate assumption on the chosen row weight. It does not follow for arbitrary weighted rows merely from their total mass (1.3). A bounded nonnegative weight on a row ball is covered whenever the corresponding sharp native second moment is supplied. The pinned native height restrictions are retained whenever this input is invoked.

## 2. The exact quadratic–cubic Walsh remainder

For each good prime define

\[
 Q_p(u)=\chi_p(u)^3\in\{0,-1,1\},\qquad
 C_p(u)=\chi_p(u)^4\in\{0\}\cup\mu_3.
 \tag{2.1}
\]

The identity `chi_p = Q_p C_p` is literal at zero as well as on the sixth roots of unity. Use their multiplicative extensions on squarefree ideals.

For a fixed `D`, only finitely many primes occur in the supported column ideals. Let `mathcal P_D` be this finite set. For independent uniform signs `epsilon_p` on those primes, write `epsilon(n)=product_{p|n}epsilon_p` and form the **cubic-coefficient** polynomial

\[
 P_u(\boldsymbol\epsilon)
 =\sum_{(n,qS)=1}\mu_K(n)^2\nu(n)C_n(u)
 W(Nn/D)\epsilon(n).
 \tag{2.2}
\]

Its nonnegative `2k`-th power has a unique Walsh expansion

\[
 |P_u(\boldsymbol\epsilon)|^{2k}
 =\sum_{r\mid\prod_{p\in\mathcal P_D}p}
       \mathcal C_{k,r}(u)\epsilon(r),\qquad
 \mathcal C_{k,r}(u)
 =\mathbb E_{\epsilon}|P_u(\epsilon)|^{2k}\epsilon(r).
 \tag{2.3}
\]

These coefficients are real. They depend on the row only through the cubic characters and their literal masks, as well as the fixed data.

For an ordered Hermitian tuple `n_1,...,n_k;m_1,...,m_k`, define

\[
 r=\operatorname{rad}_2\!\left(\prod_i n_i\prod_jm_j\right),
 \tag{2.4}
\]

where `rad_2` is the product of primes whose exponent is odd. Expanding (2.2) gives the exact coefficient formula

\[
 \mathcal C_{k,r}(u)=
 \sum_{\operatorname{rad}_2(\prod_i n_i\prod_jm_j)=r}
 \prod_i\nu(n_i)C_{n_i}(u)W(Nn_i/D)
 \prod_j\overline{\nu(m_j)C_{m_j}(u)W(Nm_j/D)}.
 \tag{2.5}
\]

All columns in this formula are good squarefree ideals obeying their original exclusions and supports. The entire tuple Möbius sign is

\[
 \prod_i\mu_K(n_i)\prod_j\mu_K(m_j)=\mu_K(r).
 \tag{2.6}
\]

### Theorem 2.1. Literal parity decomposition

\[
 \boxed{
 |A_u^{(q)}(D;W)|^{2k}
 =\sum_r\mu_K(r)Q_r(u)\mathcal C_{k,r}(u).
 }
 \tag{2.7}
\]

**Proof.** If `p` divides `u`, every nonzero column involving `p` in (2.2) vanishes. Hence the polynomial and its Walsh expansion are independent of `epsilon_p`, and `mathcal C_{k,r}(u)=0` whenever `p|r`. On the other, active primes, substitute `epsilon_p=-Q_p(u)`, which is an actual sign. The resulting polynomial is exactly (1.2). Values assigned on the inactive primes are immaterial. The surviving Walsh value at `r` is `mu_K(r)Q_r(u)`. This proves (2.7) without evaluating a non-multilinear identity at an illicit zero sign. Equivalently, one can check each tuple using (2.6); its even quadratic powers are the principal masks already retained by its cubic factors. QED.

Write

\[
 \mathcal B_k=\sum_u w_H(u)\mathcal C_{k,1}(u),\qquad
 \mathcal R_k=
 \sum_{r\ne1}\mu_K(r)\sum_u w_H(u)Q_r(u)\mathcal C_{k,r}(u).
 \tag{2.8}
\]

Then `M_(2k)=mathcal B_k+mathcal R_k`. The baseline is positive. It contains all tuples of even total prime multiplicity, including some nonprincipal cubic correlations; it is **not** just the complete-residue principal-character part. If all `2k` long columns are pairwise coprime, (2.4) is their full product. Thus the fully singleton tuples occur in the nonempty remainder, at parity scale comparable to `D^(2k)`.

## 3. Elementary hypercontractivity and quantitative Walsh coefficients

### Lemma 3.1. A finite sign inequality

For a multilinear polynomial `F(epsilon)=sum_I a_I epsilon(I)` and an integer `k>=1`,

\[
 \boxed{
 \|F\|_{L^{2k}(\epsilon)}^2
 \le\sum_I(2k-1)^{|I|}|a_I|^2.
 }
 \tag{3.1}
\]

**Proof.** For complex numbers `a,b`, symmetry and `|Re(a conjugate(b))|<=|a||b|` give

\[
 \mathbb E_{\epsilon=\pm1}|a+\epsilon b|^{2k}
 \le\sum_{j=0}^k\binom{2k}{2j}|a|^{2k-2j}|b|^{2j}
 \le\bigl(|a|^2+(2k-1)|b|^2\bigr)^k.
 \tag{3.2}
\]

For the last inequality, the coefficient ratio is

\[
 \frac{\binom{2k}{2j}}{\binom{k}{j}}
 =\prod_{\ell=0}^{j-1}\frac{2k-2\ell-1}{2j-2\ell-1}
 \le(2k-1)^j.
\]

Separate the last sign, writing `F=G+epsilon_p J`. Equation (3.2), followed by the triangle inequality in `L^k` on the remaining signs, gives

\[
 \|F\|_{2k}^2\le\|G\|_{2k}^2+(2k-1)\|J\|_{2k}^2.
\]

Induction on the finite number of signs proves (3.1). QED.

For every fixed integer `m>=1`, elementary ideal counting and convolution give

\[
 \sum_{Nn\le X}\mu_K(n)^2m^{\omega(n)}
 \le\sum_{Nn\le X}d_{m,K}(n)
 \ll_{K,m}X(\log(2X))^{m-1},\qquad X\ge1.
 \tag{3.3}
\]

Indeed the summand inequality follows prime by prime, and the convolution estimate follows inductively from `#{Nn<=X}=O_K(X)` and the ideal harmonic sum `sum_(Nn<=X)1/Nn=O_K(log(2X))`. Both latter facts also follow directly from lattice counting in this fixed imaginary quadratic field.

Applying (3.1) to (2.2) and then (3.3) proves, uniformly in the actual row and every retained column mask,

\[
 0\le\mathcal C_{k,1}(u)
 \ll_{k,W}D^k(\log(2D))^{k(2k-2)}.
 \tag{3.4}
\]

Only `|nu(n)C_n(u)|<=1` was used. In particular,

\[
 0\le\mathcal B_k\ll_\epsilon HD^{k+\epsilon},
 \qquad \mathcal R_k\ge-\mathcal B_k.
 \tag{3.5}
\]

The second inequality follows from the nonnegative full moment, not from positivity of the individual Walsh coefficients. A bound on `mathcal R_k` from above would suffice; an absolute-value bound is unnecessary.

Walsh coefficient domination and Parseval give two further uniform facts:

\[
 |\mathcal C_{k,r}(u)|\le\mathcal C_{k,1}(u),\qquad
 \sum_r|\mathcal C_{k,r}(u)|^2
 =\mathbb E_\epsilon|P_u(\epsilon)|^{4k}
 \ll_\epsilon D^{2k+\epsilon}.
 \tag{3.6}
\]

### Lemma 3.2. Decay in the parity ideal

For every supported `r`,

\[
 \boxed{
 |\mathcal C_{k,r}(u)|
 \ll_{k,W,\epsilon}\frac{D^{k+\epsilon}}{\sqrt{Nr}}.
 }
 \tag{3.7}
\]

**Proof.** The product of the `2k` squarefree columns in (2.5) has the unique form `r g^2`. Its norm is at most `(beta D)^(2k)`, so `Ng <= (beta D)^k/sqrt(Nr)`. At any fixed product the number of ordered factorizations into `2k` ideals is at most the fixed-order divisor function, which is `O_(k,epsilon)(D^epsilon)` on this support. Counting `g` proves (3.7). If the upper bound for `Ng` is below one, the coefficient is zero. This count retains all incidence configurations; it is not a multiplicativity assertion about their test weights. QED.

Consequently the complete small-parity part of the actual remainder obeys the unconditional estimate

\[
 \left|\sum_{1<Nr\le R}\mu_K(r)
       \sum_u w_H(u)Q_r(u)\mathcal C_{k,r}(u)\right|
 \ll_\epsilon HD^{k+\epsilon}\sqrt R,
 \qquad R\ge1.
 \tag{3.8}
\]

Unlike a native norm contraction, this uses an absolute tuple count only after the parity restriction has been imposed. Thus no inadmissible deletion of free singleton terms is involved. The exponent cost for `R=D^rho` is `rho/2`, independent of `k`. It does not control the fully singleton range `R` comparable to `D^(2k)`.

## 4. Recovering moving exclusions from the unmasked pointwise premise

For an ideal `Q`, write `ell|Q^infinity` when every prime of `ell` divides `Q`. The exact finite convolution identity is

\[
 A_u^{(Q)}(Y;V)
 =\sum_{\ell\mid Q^\infty}
       \xi_u(\ell)A_u^{(1)}(Y/N\ell;V).
 \tag{4.1}
\]

Only `Nell<=beta_V Y` contributes. At a prime of `Q` the local inverse factor `(1-x)^(-1)` multiplies the Möbius factor `1-x` to one; at other primes the original factor remains. This also proves the identity when `xi_u(p)=0`: no symbol is divided out, and every affected nonconstant term is zero.

Apply `PW_b` at the same ambient `D` and the same rows to every nonempty shorter scale. Then

\[
 |A_u^{(Q)}(Y;V)|
 \ll D^\epsilon Y^b\|V\|_{C^{J_b}}
       \prod_{p\mid Q,\ p\notin S}(1-(Np)^{-b})^{-1}.
 \tag{4.2}
\]

For fixed `b>0` and every `eta>0`, the finite product is `O_(b,eta)((NQ)^eta)`: at sufficiently large primes its logarithm is at most `eta log Np`, and the finitely many remaining local factors are finite constants. All of those small primes are retained. Hence if `NQ<=D^B`, reallocating the small losses gives

\[
 |A_u^{(Q)}(Y;V)|\ll_{\epsilon,B}D^\epsilon Y^b\|V\|_{C^{J_b}}.
 \tag{4.3}
\]

There is no arbitrary column coefficient in this adapter. Its applicability relies on the exact Euler-product coprimality exclusion. Nonempty scales below one lie in a fixed compact interval and change only support-dependent constants.

If `NM2_w` is supplied, the same identity (4.1) and the triangle inequality in the fixed weighted row `L^2` norm give

\[
 \|A^{(Q)}(Y;V)\|_{2,w}
 \ll D^\epsilon\sqrt{HY}\|V\|_{C^{J_2}}
       \prod_{p\mid Q,\ p\notin S}(1-(Np)^{-1/2})^{-1}.
\]

The same finite-product argument absorbs this last product into `D^epsilon`. Thus the moving-mask version of `NM2_w` needed below is derived from its unmasked shorter-scale version; an arbitrary masked-coefficient large sieve has not been substituted for the native estimate.

## 5. A positive semigroup on the exact parity kernel

Fix `t>=0`. On the finite set `mathcal P_D`, take independent signs `e_p` with

\[
 \mathbb P(e_p=1)=\frac{1-(Np)^{-t}}2,
 \qquad
 \mathbb P(e_p=-1)=\frac{1+(Np)^{-t}}2.
 \tag{5.1}
\]

The marginal mean is `-(Np)^(-t)`. These distributions are consistent as the finite prime set increases, but every polynomial and every expectation here uses only finitely many coordinates. No exchange of an infinite random series is required. At `t=0` the signs are deterministically minus one.

Define the biased-sign physical polynomial with the **original sextic phase** by

\[
 Z_{u,t}^{(q)}(D;W)
 =\sum_{(n,qS)=1}\mu_K(n)^2\xi_u(n)W(Nn/D)e(n),
\]
\[
 \mathcal F_{k,t}^{(q)}(D,H;W)
 =\sum_u w_H(u)\mathbb E_e|Z_{u,t}^{(q)}(D;W)|^{2k}.
 \tag{5.2}
\]

This is nonnegative, and `mathcal F_(k,0)=M_(2k)`. Equations (2.3) and (2.7) give the exact identity

\[
 \boxed{
 \mathcal F_{k,t}^{(q)}
 =\mathcal B_k+
 \sum_{r\ne1}\frac{\mu_K(r)}{(Nr)^t}
        \sum_u w_H(u)Q_r(u)\mathcal C_{k,r}(u).
 }
 \tag{5.3}
\]

Indeed the Walsh coefficient for the sextic rather than cubic polynomial is `Q_r(u) mathcal C_(k,r)(u)`, with the same argument at inactive primes as in Theorem 2.1, and `E e(r)=mu_K(r)(Nr)^(-t)`.

For completeness, if `T_t` is the product sign-noise operator whose Walsh multiplier at `r` is `(Nr)^(-t)`, then `T_s T_t=T_(s+t)`, and the right side of (5.3) is `T_t` of the nonnegative moment function evaluated at the all-minus sign vector. This is a finite-dimensional identity. It implies positivity, but not monotonicity in `t` at that vector.

The coefficient estimate (3.7) already gives `mathcal F_(k,t) << HD^(k+epsilon)` for `t>=1/2`, by absolute summation (with a harmonic logarithm at equality). The next theorem improves the permitted damping using the actual inverse Möbius coefficients.

## 6. The damped hierarchy from native pointwise cancellation

### Lemma 6.1. Centered bounded prime signs

Let `e_p` be arbitrary independent signs, `m_p=E e_p`, and `z_p=e_p-m_p`. For any finite multilinear coefficient array `B_d` indexed by squarefree ideals,

\[
 \boxed{
 \left\|\sum_d B_d\prod_{p\mid d}z_p\right\|_{2k}^2
 \le\sum_d[4(2k-1)]^{\omega(d)}|B_d|^2.
 }
 \tag{6.1}
\]

**Proof.** Introduce an independent copy `e'_p`. Conditional expectation over that copy sends `product_(p|d)(e_p-e'_p)` to `product_(p|d)z_p`. Jensen therefore bounds the displayed `L^(2k)` norm by the norm with `z_p` replaced by `e_p-e'_p`. These differences are independent, symmetric variables taking values in `{0,-2,2}`. Conditional on their magnitudes, write them as independent uniform signs times magnitudes at most two. Apply Lemma 3.1, then bound each squared magnitude product by `4^(omega(d))`. The resulting bound is independent of the conditioned magnitudes, so averaging completes the proof. Degenerate differences, including those at `t=0`, cause no exception. QED.

### Theorem 6.2. Full parity-damped moment bound

Assume `PW_b` in the precise form of Section 1. For every fixed integer `k>=1`, every fixed `t>=0`, and every polynomially bounded coprimality exclusion `q`,

\[
 \boxed{
 \mathbb E_e|Z_{u,t}^{(q)}(X;W)|^{2k}
 \ll_{k,t,\epsilon}D^\epsilon
        X^{\,k\max\{1,2b-2t\}}
 }
 \tag{6.2}
\]

uniformly on every nonempty shorter scale `c<=X<=CD` and on the same physical rows as the premise. In particular,

\[
 \boxed{
 \mathcal F_{k,t}^{(q)}(D,H;W)
 \ll_{k,t,\epsilon}HD^{\,k\max\{1,2b-2t\}+\epsilon}.
 }
 \tag{6.3}
\]

Constants may be chosen uniformly for `t` in any specified compact subinterval of `[0,infinity)`, at the cost of its fixed support/seminorm constants.

**Proof.** Work at a shorter column scale `X`. In (5.1), `m_p=-(Np)^(-t)`. Expanding `e_p=m_p+z_p` in each squarefree column gives the exact finite identity

\[
 Z_{u,t}^{(q)}(X;W)
 =\sum_{\substack{d\ \mathrm{sf}\\(d,qS)=1}}
      B_d(u)\prod_{p\mid d}z_p,
 \tag{6.4}
\]

where, with `Y=X/Nd`,

\[
 \begin{split}
 B_d(u)
 &=\xi_u(d)
   \sum_{(m,dqS)=1}\mu_K(m)\xi_u(m)(Nm)^{-t}W(Nm/Y)\\
 &=\xi_u(d)Y^{-t}A_u^{(dq)}(Y;V_t),
 \qquad V_t(x)=x^{-t}W(x).
 \end{split}
 \tag{6.5}
\]

The original squarefree condition is exactly the coprimality `(m,d)=1`. No shared-prime contribution is lost. The row factor `xi_u(d)` is a contraction, retaining its zero. Only `Nd<=beta X` contributes, so `N(dq)` remains bounded by a fixed power of the ambient `D`. All tests `V_t` have the same compact support; their required finite seminorms are bounded for fixed `t`, uniformly on compact `t` ranges.

The adapter (4.3), at the same physical row range, gives

\[
 |B_d(u)|\ll D^\epsilon (X/Nd)^{b-t}.
 \tag{6.6}
\]

This remains valid if `b-t` is negative: every realized `Y` is bounded below by `1/beta`, and (6.5) is the exact identity `Y^(-t) A(Y;V_t)`. No estimate is applied at a vanishing scale.

Let `gamma=2(b-t)` and `c_k=4(2k-1)`. Lemma 6.1 bounds the squared norm by

\[
 D^\epsilon X^\gamma
 \sum_{Nd\le\beta X}\mu_K(d)^2c_k^{\omega(d)}(Nd)^{-\gamma}.
 \tag{6.7}
\]

Partial summation of (3.3), or the ideal divisor bound followed by a dyadic sum, yields, for every prescribed small loss,

\[
 \sum_{Nd\le\beta X}\mu_K(d)^2c_k^{\omega(d)}(Nd)^{-\gamma}
 \ll_{k,t,\epsilon}X^{\max\{0,1-\gamma\}+\epsilon}.
 \tag{6.8}
\]

At `gamma=1` the extra factor is only a fixed logarithmic power. For negative `gamma` the same formula counts the larger ideals with their positive weight; it does not replace them by one. Nonempty bounded `X<1` changes only a fixed support constant. The estimate with a positive loss is uniform for `gamma` in a fixed compact interval.

Combining (6.7)–(6.8) gives squared norm `<< D^epsilon X^(max(1,gamma))`. Raise it to the fixed power `k` and reallocate the preliminary losses to obtain (6.2). Sum the nonnegative row weights using (1.3) to obtain (6.3). QED.

### Theorem 6.3. Refinement with the native second moment

If `NM2_w` is supplied in addition to `PW_b`, then for every fixed `k,t` and every nonempty shorter scale `X`,

\[
 \boxed{
 \mathcal F_{k,t}^{(q)}(X,H;W)
 \ll_{k,t,\epsilon}HD^\epsilon
       X^{\,k+(k-1)(2b-2t-1)_+}.
 }
 \tag{6.9}
\]

**Proof.** Keep the actual shorter native coefficient `B_d(u)` from (6.5), and define the nonnegative function

\[
 \mathcal Q_{k,t}(u)=
 \sum_{Nd\le\beta X}[4(2k-1)]^{\omega(d)}|B_d(u)|^2.
 \tag{6.10}
\]

The squarefree and exclusion conditions from (6.4) remain in this sum. The proof above gives both

\[
 \mathbb E_e|Z_{u,t}^{(q)}|^{2k}\le\mathcal Q_{k,t}(u)^k,
 \qquad
 \sup_u\mathcal Q_{k,t}(u)\ll D^\epsilon X^m,
 \quad m=\max\{1,2b-2t\}.
 \tag{6.11}
\]

The moving-mask native second moment established after (4.3), applied to `V_t`, gives

\[
 \sum_u w_H(u)|B_d(u)|^2
 \ll HD^\epsilon (X/Nd)^{1-2t}.
 \tag{6.12}
\]

All row phases are contractions, and no coefficient outside the declared native family has been inserted in this estimate. Sum (6.12) with the nonnegative weights in (6.10). The same ideal divisor sum used in (6.8), now at exponent `1-2t<=1`, yields

\[
 \sum_u w_H(u)\mathcal Q_{k,t}(u)
 \ll HD^\epsilon X.
 \tag{6.13}
\]

At `t=0` the ideal sum is harmonic; its fixed logarithmic power is absorbed in the loss. For positive `t`, including `t>1/2`, the formula continues to count its weighted large ideals correctly. Consequently

\[
 \sum_u w_H(u)\mathcal Q_{k,t}(u)^k
 \le(\sup_u\mathcal Q_{k,t}(u))^{k-1}
       \sum_u w_H(u)\mathcal Q_{k,t}(u)
 \ll HD^\epsilon X^{1+(k-1)m}.
\]

This is (6.9), after reallocating the fixed-order losses. QED.

### Consequences and exact scope

For `t>=b-1/2`, (6.3) is `O(HD^(k+epsilon))` at every fixed order. Thus (5.3) proves an upper bound of that size for the **entire damped signed remainder**, and its lower bound is `-mathcal B_k`. Individual `r` ranges need not have either sign, and their absolute values are not bounded by positivity of the whole.

At `b=1`, the theorem is unconditional and agrees with the counting threshold `t=1/2`. At the separately assumed `b=7/8`, it lowers the threshold to `3/8`. Absolute coefficient counting at that smaller damping would allow a full-range loss `D^(k/4+epsilon)` beyond the diagonal scale. Theorem 6.2 removes that loss for the complete damped functional by using the shorter inverse sums in (6.5). It does not remove the remaining damping.

## 7. What damping removal would have to add

The biased expectation of the physical polynomial is

\[
 \mathbb E_e Z_{u,t}^{(q)}(D;V)
 =D^{-t}A_u^{(q)}(D;x^{-t}V(x)).
 \tag{7.1}
\]

Choose `V(x)=x^t W(x)` and apply Jensen. This gives the exact adapter

\[
 \boxed{
 M_{2k}^{(q)}(D,H;W)
 \le D^{2kt}\mathcal F_{k,t}^{(q)}(D,H;x^tW).
 }
 \tag{7.2}
\]

At the proved threshold `t=b-1/2`, the cost is `D^((2b-1)k)`. With the separately supplied native second moment, ordinary interpolation improves the constant part of this loss to `(2b-1)(k-1)`. Neither cost is sublinear in `k` when `b>1/2` is fixed.

There is also a precise pointwise equivalence. Fix `0<=t<=1/2`, put `b=1/2+t`, and keep the same ambient, shorter-scale, row, and test quantifiers. The pointwise-in-row randomized **second** moment bound

\[
 \mathbb E_e|Z_{u,t}^{(q)}(X;V)|^2\ll_\epsilon D^\epsilon X
 \tag{7.3}
\]

for every test `V` in the declared fixed-support family implies `PW_b`, by (7.1) and Jensen with `V=x^tW`. Conversely `PW_b` implies (7.3), including the moving exclusions, by Theorem 6.2. The full pointwise randomized hierarchy follows from that same premise. This equivalence concerns the displayed pointwise randomization and its uniformity; it is not an assertion that the imported ordinary native second moment already supplies (7.3).

For a sharp full row ball `Nu<=D^h`, an averaged diagonal bound on `mathcal F_(k,t)` at every fixed `k` would likewise imply the top-scale pointwise exponent `1/2+t` with arbitrary positive losses: apply (7.2) to an individual retained row and choose a fixed sufficiently large `k` relative to `h` and the desired loss. At a single fixed height exponent this does not automatically supply the stronger same-height, all-shorter-scale premise. That additional quantifier must be retained when an equivalence for the full family is claimed.

The noise operators do not possess a generic reverse estimate with a sublinear-in-`k` exponent cost. For example, take the bounded squarefree coefficient array `a_n=mu_K(n)W(Nn/D)`, with a fixed nonnegative annular `W` that is positive on an interval, and form `P(e)=sum a_n e(n)`. At the all-minus vector, `P(-1)=sum mu_K(n)^2W(Nn/D) >> D`. For `0<=t<=1/2`, the same centered-sign proof, using the counting bound for its cofactor sums, gives

\[
 \mathbb E_t|P(e)|^{2k}\ll D^{2k(1-t)+\epsilon}.
 \tag{7.4}
\]

Its expectation is `sum mu_K(n)^2(Nn)^(-t)W(Nn/D) >> D^(1-t)`, so Jensen gives the matching power lower bound. Therefore the power `2kt` in the reverse comparison is attained, up to arbitrary small losses, in this class of coefficient arrays. The squarefree ideal count in an annulus has positive density; it follows from the convergent square-divisor exclusion sum and fixed-field ideal counting. This array is not being identified with a fixed finite-order Hecke row in the native family. It rules out a universal reverse-noise argument that ignores that arithmetic distinction.

Thus Theorem 6.2 supplies a controlled path toward the native moment, but its endpoint is exactly tied to the supplied pointwise exponent. A signed native estimate removing a fixed positive amount of the parity damping would be genuinely new information. Neither positivity nor the semigroup law supplies it.

## 8. A cofinal obstruction to all integer-product norm compositions

The physical sextic-product bound in the pinned #923 Lemma 2.1 gives, for any fixed integer monomial in equal-scale native factors, of total degree `j>=1`,

\[
 \frac1H\left\|\prod_i A_i(D)^{e_i}\right\|_{2,H}^2
 \ll_\epsilon D^\epsilon
       \left[D^j+D^{2j-5h/6}+D^{5j/3-h/3}\right],
 \qquad j=\sum_i e_i,\quad H=D^h.
 \tag{8.1}
\]

Repeated integer copies are literal physical products and are covered by the same fixed-order incidence proof. The bound also applies to their absolute product when factors are conjugated. Grant in addition the native `L^2` bounds `H^(-1)||A_i||_2^2 << D` and `PW_b`. This grants every integer degree at once, with its own fixed-degree constant.

Set

\[
 a=2b-1,\qquad
 F_h(x)=\max\{x,\ 2x-5h/6,\ 5x/3-h/3\}.
 \tag{8.2}
\]

For `x>=0`, its exact three branches are

\[
 F_h(x)=
 \begin{cases}
 x,&0\le x\le h/2,\\
 5x/3-h/3,&h/2\le x\le3h/2,\\
 2x-5h/6,&x\ge3h/2.
 \end{cases}
 \tag{8.3}
\]

Consequently

\[
 \sup_{x\ge0}\{2bx-F_h(x)\}=h\,c(b),\qquad
 c(b)=
 \begin{cases}
 b-1/2,&1/2<b\le5/6,\\
 3b-13/6,&5/6\le b\le1.
 \end{cases}
 \tag{8.4}
\]

For `b<=5/6` the maximum is at `x=h/2`; for `b>=5/6` it is at `x=3h/2`, with a constant final branch allowed at `b=1`. This proves the formula for all real `x`, hence for every integer degree.

### Theorem 8.1. Simultaneous common-spike witness

For fixed `h>1` and `1/2<b<=1`, put

\[
 \delta=\delta_{\mathbb Z}(h,b)
 =\max\left\{a,\sup_{j\in\mathbb N}
                     (2bj-F_h(j))\right\}
 \le\Delta(h,b):=\max\{a,hc(b)\}.
 \tag{8.5}
\]

This is an explicit finite optimization: the integer supremum is attained among `1` and the positive integers immediately below and above `h/2` and `3h/2`. On each intervening interval its objective is affine, and its final slope is `2b-2<=0`. At `b=1` the final constant branch is attained already at `ceil(3h/2)`.

There is a mean-zero finite row model satisfying `PW_b`, native `L^2`, and **every** bound (8.1), in which

\[
 \frac1H\left\|\prod_{i=1}^k A_i(D)\right\|_{2,H}^2
 \asymp D^{2bk-\delta}.
 \tag{8.6}
\]

**Proof.** On a probability space take an event of mass `p=D^(-delta)`, an independent uniform sign `sigma`, and put every long-scale factor equal to `A_i=D^b sigma 1_E`. The factors have mean zero and pointwise size at most `D^b`. Their normalized second moments are `D^(2b-delta)<=D`, because `delta>=a`. A degree-`j` integer monomial has squared moment

\[
 \mathbb E\left|\prod_i A_i^{e_i}\right|^2
 =D^{2bj-\delta}\le D^{F_h(j)},
 \tag{8.7}
\]

by (8.4)–(8.5). Thus all the stated physical-product upper bounds are satisfied simultaneously, without even an epsilon loss.

If a literal finite row set is desired, let `N=floor(D^h)`, place equal positive and negative values on `2 floor(N D^(-delta)/2)` rows, and set the other values to zero. Since `delta<=Delta`, `c(b)<=5/6`, and `a<=1<h`, one has `delta<h`; the occupied count tends to infinity and its density is comparable to `D^(-delta)`. The floors preserve all upper bounds, with only fixed normalization constants, and preserve the power lower bound in (8.6). QED.

This is a countermodel to **deduction from the specified norm data**, not a counterexample to the arithmetic Möbius conjecture. It does not assert that these vectors arise from the literal Hecke coefficients or satisfy every exact arithmetic identity. It proves that Hölder, Cauchy, interpolation, tensor norm manipulations, arbitrary fixed integer monomial replications, and any correctly justified fractional-cover inequality using only those norm inputs cannot force an upper bound smaller than (8.6). An independence-based fractional-cover assertion is additional information and does not hold for this shared-spike model.

For any claimed normalized whole-product bound `D^(k+e_k+epsilon)` from this norm data, the witness requires

\[
 \boxed{e_k\ge(2b-1)k-\delta.}
 \tag{8.8}
\]

In particular, if `h_k=o(k)` with `h_k>1`, then `delta_k<=Delta(h_k,b)=O_b(1+h_k)=o(k)`. Therefore

\[
 \boxed{\liminf_{k\to\infty}\frac{e_k}{k}\ge2b-1.}
 \tag{8.9}
\]

This remains true even though all integer-product norm bounds, of unbounded fixed degree, were granted. It is stronger than a comparison of a finite list of subset choices.

The finite envelope is also attained by an available upper bound whenever `k>=ceil(3h/2)`. If its maximum is `a`, apply the native second moment on one factor and `PW_b` on the other `k-1`. Otherwise choose a maximizing degree `j_0<=ceil(3h/2)`, use (8.1) on any `j_0` factors, and use `PW_b` on the rest. The resulting exponent is exactly `2bk-delta`, up to the allowed losses. Thus in this range the ordinary subset method already attains the optimum of **all** valid norm compositions based on the granted inputs; mixed higher integer replications cannot improve it.

When `delta=a`, the witness attains the elementary native second-moment/pointwise upper bound `D^(k+a(k-1))` for every `k>=1`, and that bound is exactly optimal within these norm data. The continuous condition `hc(b)<=a` suffices. At `b=7/8`,

\[
 c(b)=11/24,\qquad
 \Delta(h,b)=\max\{3/4,11h/24\}.
\]

The exact integer envelope improves that sufficient range: `delta=3/4` for every `1<h<=7/4`. To check this directly, `j=1` is covered by the native term. For `h<=4/3`, the maximum among `j>=2` is `5h/6-1/2<=3/4`. For `4/3<=h<=7/4`, the `j=2` value is `1/6+h/3<=3/4`, and every `j>=3` is on the decreasing final branch with maximum `5h/6-3/4<3/4`. Just above `7/4` the `j=2` value exceeds `3/4`, so this endpoint is exact. At the counting value `b=1`, `delta=max{1,5h/6}`, and the corresponding exact sharp range is `1<h<=6/5`.

### Connected cumulants do not remove the witness

For the mean-zero scalar spike `A=D^b sigma 1_E`, every odd moment is zero and every positive even moment is `pD^(mb)`. The joint-cumulant partition formula gives, for each fixed even `m>=2`,

\[
 \kappa_m(A)=D^{mb}\bigl(p+O_m(p^2)\bigr).
 \tag{8.10}
\]

The one-block partition contributes `p`; every other nonzero partition has at least two blocks and contributes a constant times at least `p^2`. Thus the connected cumulant itself carries the leading rare-event power. Reorganizing the same estimates into connected cumulants cannot supply the missing saving without a new estimate on those connected arithmetic terms.

## 9. What independence is true, and what the finite rows do not supply

For a good prime, a uniform nonzero residue has its sextic symbol uniform on `mu_6`. The map `z -> (z^3,z^4)` is a bijection from `mu_6` to `mu_2 x mu_3`. Under complete uniform CRT residues, the local quadratic signs are therefore independent fair signs after all cubic values are fixed. At a zero cubic value the corresponding column terms vanish, so there is no missing zero-mask case. It follows, conditionally on the entire cubic environment, that every nonempty term `Q_r mathcal C_(k,r)` has complete-residue average zero.

This exact conditional cancellation explains why the Walsh decomposition is natural. It does not establish the same assertion for the short physical row ball. The coefficients `mathcal C_(k,r)(u)` vary with the row through all their cubic phases; replacing them by fixed coefficients in a quadratic large sieve would change the problem.

There is also an elementary obstruction to importing the ordinary CRT-coordinate heat-bath chain. Let `mathfrak Q` be a product of good primes, and suppose `N(mathfrak Q/p)>4H` for every prime `p|mathfrak Q`. On rows `0<Nu<=H`, the residues modulo all primes except `p` determine the row uniquely: if `u,v` share those residues, then `mathfrak Q/p` divides `u-v`, while

\[
 N(u-v)\le(\sqrt{Nu}+\sqrt{Nv})^2\le4H.
\]

Thus `u=v`. Every one-coordinate conditional resampling operator on these **full residue coordinates** is the identity. Its Dirichlet form is zero, so it cannot yield a nontrivial product-measure Poincaré or logarithmic-Sobolev inequality for the conditioned short-row distribution. This argument is specifically about residue-coordinate resampling; it does not rule out every possible chain on the coarser character values.

The new arithmetic target is now explicit: cancel enough of

\[
 \sum_{r\ne1}\mu_K(r)
       \sum_u w_H(u)Q_r(u)\mathcal C_{k,r}(u)
 \tag{9.1}
\]

to remove a positive part of the known parity damping, with the actual cubic coefficients and the same rows. Theorem 6.2 proves that this coupled kernel is controlled after damping at `b-1/2`; Theorem 8.1 explains why another positive norm composition cannot remove that fixed damping at cofinal orders. No undamped cancellation estimate is claimed here.

## 10. Literature and validation boundary

The surviving Möbius parity sign is an established ingredient of this repository program. [PR #914, `CONDUCTOR_SECTORS.md`, Section 9](https://github.com/GettysburgResearch/riemann/blob/0cc0428fedbbfc340044c7451b3d392c1da9a103/standalone/2026-10-10-sextic-moment-conductor-core/CONDUCTOR_SECTORS.md) proves `mu_K(f_1 f_3 f_5)` for the odd residual conductor classes, including the high-order principal zero masks. Its Sections 7–10 already isolate the genuine singleton remainder. The same packet's [interaction-graph calculation](https://github.com/GettysburgResearch/riemann/blob/0cc0428fedbbfc340044c7451b3d392c1da9a103/standalone/2026-10-10-sextic-moment-conductor-core/INTERACTION_GRAPH.md) also records why separate factor-axis phases cannot erase the coupled cubic edges. None of those facts is claimed as new here.

[PR #911, `GENERALIZED_MOMENT_ATTACK.md`](https://github.com/GettysburgResearch/riemann/blob/2f8b6a3898a722d0602a91dea73bac344a3bb7dd/research/exploratory/2026-10-10-four-hour-wave/literature/GENERALIZED_MOMENT_ATTACK.md), develops the inherited signed remainder, collision Euler factors, and lower-moment lifting. Its [prime-slot route status](https://github.com/GettysburgResearch/riemann/blob/2f8b6a3898a722d0602a91dea73bac344a3bb7dd/research/exploratory/2026-10-10-two-hour-continuation/literature/PRIME_SLOT_ROUTE_STATUS.md) proves decay on a shrinking multivariate Mellin tube and explicitly leaves its complementary `CT1` estimate open. The present note does not promote that tube to a full moment. Its additional results are the exact **purely cubic coefficient / quadratic Walsh** separation, the full positive parity-damped family with its quantified shorter-scale adapters, the parity-ideal coefficient decay, and the simultaneous **all-integer-degree** norm obstruction with its exact integer envelope. These four precedent files have also been fetched at the displayed immutable commits and included in the source manifest.

The random-sign weighted norm inequality is classical in the theory of random multiplicative functions. A directly relevant primary reference is Adam J. Harper, *Moments of random multiplicative functions, II: High moments*, arXiv:1804.04114v1 (11 April 2018), Section 2.2, Probability Result 1, which states the Rademacher inequality with divisor weight `d_(2 ceil(q)-1)`. See <https://arxiv.org/pdf/1804.04114v1>. The integer inequality needed here is proved from the one-sign identity in Section 3, and the biased-sign extension is proved separately in Section 6. No probabilistic independence of the arithmetic rows is imported from that literature.

The external sieve inequalities and optional native `PW_b` input are exactly the source-qualified interfaces above. The main parity identities, the bias expansion, the finite exclusion adapter, and the common-spike obstruction are proved here. Finite checks can verify primitive sixth-root/zero arithmetic, Walsh identities, the rational exponent envelope, and the finite symmetrization formulas. Such checks do not establish `PW_b`, an infinite sieve, a full native moment, a zero-free region, or RH.
