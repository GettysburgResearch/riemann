# Removing the explicit sixth-power Euler denominator

**Status:** proposed, fully written elementary normalization lemma and source-dependent Mellin consequence. No improved bound for the signed transformed probe is proved. No independent mathematical review or Lean formalization of this note has been performed. This is an analysis of the pinned formal source, not a claim of priority for Euler-factor extraction.

The purpose is to turn a vague suggestion to improve the imported theorem into one specific signed analytic target. A holomorphic numerator can be constructed on the whole desired open half-plane; controlling its corresponding physical transform remains the missing estimate.

## 1. Exact source, not a guessed correction

The copied [EulerCorrectionAlgebra.lean](upstream/DedekindZetaZeroFree/Moments/Principal/EulerCorrectionAlgebra.lean) defines

\[
 C(r,A,B)=\frac{(1-r^2)(1-(1-r)A-rB)}{(1-B)(1-A)}. \tag{1}
\]

The copied [NormalizedProbeArithmeticData.lean](upstream/DedekindZetaZeroFree/Nonvanishing/Mellin/NormalizedProbeArithmeticData.lean) substitutes, at a good prime ideal of norm q,

\[
 r=q^{-1},\qquad A_p(s)=a_pq^{-s},\qquad
 B_p(s)=b_pq^{3-6s}, \tag{2}
\]

where a_p is the target ray character and b_p is the sixth power of the actual theta phase at the prescribed generator. The source's `local_phases` proof gives modulus one outside the exclusions. The lemma below even permits modulus at most one. No assertion that b_p defines a finite-order Hecke character is needed.

Fix a number field F of degree d, a finite excluded set S, and prime-indexed complex constants |a_p|,|b_p|<=1. Primes mean prime ideals; equal norms do not identify conjugate ideals. All complex powers use real log q.

## 2. A numerator product on Re(s)>1/2

Define, first algebraically,

\[
 \widetilde C_p(s)=(1-B_p(s))C(q^{-1},A_p(s),B_p(s)).
\]

The cancellation has the exact form

\[
 \boxed{\widetilde C_p(s)
 =(1-q^{-2})\left(1+
 \frac{q^{-1}(A_p(s)-B_p(s))}{1-A_p(s)}\right).} \tag{3}
\]

### Proposition 1

The product

\[
 \widetilde H(s)=\prod_{p\notin S}\widetilde C_p(s) \tag{4}
\]

converges normally, is holomorphic, and is nonzero on Re(s)>1/2. For every fixed delta>0 there is an explicit C_delta, independent of F, S, and the phases, such that

\[
 e^{-C_\delta d}\le |\widetilde H(s)|\le e^{C_\delta d}
 \quad\text{when }\Re s\ge1/2+\delta. \tag{5}
\]

**Proof.** Put sigma0=1/2+delta. In this region |A_p|<=q^(-sigma0)<1 and |B_p|<=q^(3-6sigma0)<1. The numerator in (1) is nonzero because

\[
 |(1-r)A_p+rB_p|
 \le(1-r)|A_p|+r|B_p|<1,
\]

with 0<r<1. The factor 1-r^2 and the denominator 1-A_p are also nonzero. Thus each factor (3) is holomorphic and nonzero. This reuses exactly the convex-combination mechanism already proved in the upstream local nonvanishing lemma; local nonvanishing is not a new discovery here.

The new useful accounting is

\[
 \widetilde C_p-1
 =-q^{-2}+(1-q^{-2})
      \frac{q^{-1}(A_p-B_p)}{1-A_p},
\]

so, with a=2^(-sigma0),

\[
 |\widetilde C_p-1|
 \le q^{-2}+\frac{q^{-1-\sigma_0}+q^{2-6\sigma_0}}{1-a}.
 \tag{6}
\]

Every prime sum on the right converges: 1+sigma0>1 and 6sigma0-2=1+6delta>1. The Weierstrass product criterion gives normal convergence on closed sub-half-planes.

For explicit control of the inverse, let b=2^(3-6sigma0), c=1-max(a,b)>0, and

\[
 m_\delta=\frac{3c}{4(1+a)}>0.
\]

The same convex-combination bound gives |widetilde C_p|>=m_delta uniformly in p and s. For a positive real x>=m_delta, the mean-value theorem gives |log x|<=max(1,m_delta^(-1))|x-1|. Apply this to x=|widetilde C_p|, using ||widetilde C_p|-1|<=|widetilde C_p-1|.

For any t>1, each rational prime has at most d primes above it, of norm at least that prime. Consequently

\[
 \sum_{p\text{ prime ideal}}(Np)^{-t}
 \le d\sum_{\ell\text{ rational prime}}\ell^{-t}
 \le d(\zeta(t)-1).
\]

One permissible choice is

\[
 C_\delta=\max(1,m_\delta^{-1})
 \left[\zeta(2)-1+
 \frac{\zeta(1+\sigma_0)-1+\zeta(6\sigma_0-2)-1}{1-a}\right]. \tag{7}
\]

Summing the logarithm bound and passing from finite products to the normally convergent product proves (5), including its strictly positive lower bound. The use of the ordinary zeta series here is entirely in its absolute-convergence half-plane, not an assumption about its zeros. QED.

The original product's displayed majorant contains q^(3-6sigma), requiring sigma>2/3. Formula (3) changes that term to q^(2-6sigma), requiring only sigma>1/2. This is a weighted arithmetic calculation, not an inference from formal polynomial degree alone.

## 3. Exact extraction and the phase caveat

Extend b_p completely multiplicatively to good integral ideals, denoting the extension b(d). Define only in its convergence region

\[
 E_b(w)=\sum_{(\mathfrak d,S)=1}
       \mu_F(\mathfrak d)b(\mathfrak d)(N\mathfrak d)^{-w}
       =\prod_{p\notin S}(1-b_p(Np)^{-w}),\qquad \Re w>1.
\]

Then the source product H and (4) satisfy

\[
 \widetilde H(s)=E_b(6s-3)H(s),\qquad \Re s>2/3. \tag{8}
\]

Both sides are genuinely convergent products there. If b happens to be an appropriate Hecke character, E_b(w)=1/L^S(w,b) on Re(w)>1. **No such identification or continuation is required in this note.** In particular the new finite-order Hecke theorem is not silently applied to an angular theta phase.

Equation (8) does not say that either factor on its right independently continues without poles to Re(s)>1/2. It supplies a normally convergent product for their reunited left side.

## 4. The corresponding signed physical operation

We state the analytic consequence with all its hypotheses. Let beta>2/3. Suppose a continuous complex function g on (0,infinity) satisfies:

- for every A>0, g(Z)=O_A(Z^A) as Z decreases to zero;
- for every epsilon>0, g(Z)=O_epsilon(Z^(beta+epsilon)) as Z tends to infinity.

Write T(s)=integral_0^infinity g(Z)Z^(-s)dZ/Z, initially Re(s)>beta. Define

\[
 \boxed{\widetilde g(Z)=
 \sum_{(\mathfrak d,S)=1}
 \mu_F(\mathfrak d)b(\mathfrak d)(N\mathfrak d)^3
 g\!\left(\frac{Z}{(N\mathfrak d)^6}\right).} \tag{9}
\]

There is no added coprimality condition between d and any coefficient index inside g. The exponents are **3 and 6**, not an unweighted dilation and not a square-norm rescaling.

### Proposition 2

The sum (9) converges locally uniformly and absolutely. It is continuous, flat at zero to every positive power, and has the same available growth beta+epsilon. Its Mellin transform obeys

\[
 \widetilde T(s)=E_b(6s-3)T(s),\qquad \Re s>\beta. \tag{10}
\]

**Proof.** For every fixed a>beta there is a global bound |g(Z)|<=C_a Z^a, using its hypotheses and continuity on compact intervals. Choose a>beta>2/3. The absolute majorant for (9) is

\[
 C_aZ^a\sum_{\mathfrak d}(N\mathfrak d)^{3-6a}<\infty.
\]

This proves local uniform convergence and the available growth estimate. For Z<=1 and any desired power A, use the zero-side hypothesis with an exponent B>max(A,2/3). All arguments Z/(Nd)^6 are at most one, and the sum is O(Z^B), hence O(Z^A).

For sigma>beta, T is absolutely convergent. Substitution Z=(Nd)^6 x gives

\[
 \int_0^\infty (Nd)^3g(Z/(Nd)^6)Z^{-s}\,\frac{dZ}{Z}
 =(Nd)^{3-6s}T(s).
\]

The analogous integral of absolute values factors into a finite absolute Mellin integral times sum_d (Nd)^(3-6sigma). Fubini is therefore valid. Summing proves (10). Holomorphy of both Mellin transforms follows by compact-substrip domination, with logarithmic derivatives absorbed by strict exponent margins. QED.

For the pinned source take beta=31/32 and

\[
 g(Z)=Z^{61/100}\,\mathrm{Spectral.f}(Z).
\]

The relevant source inputs are `Growth.g_growth`, `Flatness` as used by `Holomorphy`, and `AxisIdentity`. This is the **Quantitative** spectral function, not an unexamined substitution of the older `ActualRecipe.I` scale parameters.

## 5. A precisely stated full-proof target

Suppose the imported source provides the identity

\[
 L^S(s)T(s)=e^{(s-5/6)^2}H(s) \tag{11}
\]

on a right half-plane, for its actual target continuation and phase data. Combining (8)--(10) gives

\[
 \boxed{L^S(s)\widetilde T(s)
       =e^{(s-5/6)^2}\widetilde H(s)} \tag{12}
\]

in the initial region. The numerator on the right now has a proved holomorphic, nonvanishing product on **all Re(s)>1/2**.

**Conditional criterion.** A bound

\[
 \widetilde g(Z)\ll_\epsilon Z^{1/2+\epsilon}
 \quad\text{for every fixed }\epsilon>0 \tag{OPEN-R}
\]

for the actual source in (9) would imply that its target L^S has no zeros in Re(s)>1/2, away from the principal pole at one.

**Proof of the implication.** Proposition 2 already gives continuity and flatness at zero. OPEN-R makes its Mellin integral holomorphic in Re(s)>1/2. The target L^S is the actual meromorphic continuation. Analytic uniqueness extends (12) through the connected half-plane punctured at one. A zero of L^S there makes the left side zero, contradicting Proposition 1 and the nonvanishing exponential. Finite excluded Euler factors have no zeros in this positive-real-part region and can be restored. For the totally complex mu_12-containing auxiliary field, the imported abelian descent then gives the corresponding conclusion for the original number field. QED.

This is a sufficient signed-probe criterion, **not a proof of OPEN-R**. The implication relies on the imported actual-source identity, its flatness, and its continuation semantics, not merely on a formal Euler product. No equality between (9) and the original native 2k-th moment is asserted.

## 6. Where the difficulty moved

The uniform absolute-value/Minkowski majorant at weight alpha (equal to the absolute coefficient mass for unit phases) is

\[
 \sum_{(\mathfrak d,S)=1}\mu_F(\mathfrak d)^2
                 (N\mathfrak d)^{3-6\alpha}. \tag{13}
\]

It converges only for alpha>2/3. Indeed, on its convergence half-plane the squarefree ideal series is zeta_F^S(w)/zeta_F^S(2w), with w=6alpha-3; the pole at w=1 makes the positive series divergent there, and monotonicity gives divergence for smaller real w. At alpha=1/2 the weight is identically one. This is an **absolute-sum cost**, not a claimed optimal norm theorem for a signed operator over arbitrary number fields.

Thus the normalization does not give a free critical-line bound. It proves the numerator can be kept nonzero while exposing the precise weighted Möbius cancellation that must replace (13). No improvement to the imported 31/32 bound follows from Propositions 1--2 alone.

This is the useful connection to the repository's signed cube-reunion and compensated-Euler work: preserve the full signed divisor operation before taking a norm. It is also the warning from the freezing and coherent-row packets: a large positive intermediate reference can be real and still need compensating cancellation. The practical next question is whether the actual theta representation of g turns (9) into a controllable joint signed period. That identity and its power-saving estimate remain research tasks, not established adapters.
