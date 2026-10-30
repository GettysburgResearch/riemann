# Arithmetic attack: sparse reciprocal detectors and positive residue propagation

Status: **EXPLORATION — exact lemmas proved below; the analytic cancellation gate remains open.**  
Scope: ordinary zeta and finite Dirichlet character families. No new zero-free boundary is claimed.  
Sources/dependencies: finite character orthogonality; Dirichlet L-function Euler products and continuation; nonvanishing of nonprincipal L-functions at 1; the totient divisor identity. Repository overlap: [issue #740](https://github.com/GettysburgResearch/riemann/issues/740), [PROGRAMMES.md](https://github.com/GettysburgResearch/riemann/blob/f99d9e3908dde4865377c75d9ca051c1f545bf4f/PROGRAMMES.md), and the [30 October source map](https://github.com/GettysburgResearch/riemann/blob/56c62d6e63a0111074c9837aaef30112792abb72/standalone/2026-10-30-literature-pass/REPO_MAP.md).  
What was run: exact integer Euler-factor expansions through 20,000 for nine moduli; 78,125 finite Fourier examples; finite totient/conductor identities.  
Smallest remaining gap: obtain a genuine arithmetic upper bound for the contour statistic in Section 5, without discarding its principal-conductor contribution.

## 1. The attack and what survives

Three mechanisms were developed, rather than another scalar retuning:

| Mechanism | Exact outcome | Remaining issue |
|---|---|---|
| Build a nonnegative Dirichlet series whose poles detect zeta zeros, then use Landau's theorem | A sharp finite-character sign obstruction; a stronger positive-mixture obstruction including the real pole at 1 | A successful detector must escape this finite positive-mixture class |
| Multiply all reciprocal character L-functions to hide the early arithmetic coefficients | An explicit reciprocal detector supported only on integers congruent to 1 modulo q, retaining every zeta zero as a pole | Its long coefficient gap costs growing degree and conductor; the gap alone gives no continuation below 1 |
| Take logarithmic derivatives and average over moduli | Every inherited zero has a positive residue of fixed size; an exact shifted-zeta/totient identity and finite-tail identity | Control the full contour statistic, including imprimitive repetitions and the large-divisor complement |

The third construction removes a weakness of reciprocal-product arguments: the residue of a product reciprocal can be exponentially small in the family degree, whereas the logarithmic derivative retains an integer multiplicity. It also provides an exact arithmetic expression for the statistic whose upper bound is missing.

These are fresh derivations in this pass, not certified claims of worldwide novelty. The basic Euler-product and character identities are classical. The contribution is their precise combination, the quantitative sign obstruction, the uniqueness statement, and the resulting reviewable detector contract. A broad novelty search could not be completed because the web search tool returned empty errors; GitHub repository sources were available. The existing propagation programme is acknowledged, not renamed as a new programme.

## 2. A sharp sign obstruction to finite Euler-product positivity

Let G=(Z/qZ)^×, h=|G|, and let χ run over its full character group. Write χ₀ for the principal character. Consider

$$
F(s)=\prod_\chi L_q(s,\chi)^{e_\chi},\qquad e_\chi\in\mathbb Z,
$$

where all L-functions use modulus q, including imprimitive Euler factors. Assume eχ=eχ̄, so the coefficients are real. The Euler product is absolutely convergent for Re s>1. For a prime p not dividing q, its first Dirichlet coefficient is

$$
a(p)=f(p\bmod q),\qquad f(g)=\sum_\chi e_\chi\chi(g).
$$

Finite character orthogonality gives

$$
\mathbb E_G f=e_{\chi_0},\qquad
\mathbb E_G|f|^2=\sum_\chi |e_\chi|^2.
$$

### Proposition A: negative-prime-class density

If eχ₀=−r<0 and δ is the fraction of residue classes on which f<0, then

$$
\boxed{\displaystyle
\delta\ge \frac{r^2}{\sum_\chi |e_\chi|^2}.}
$$

In particular, F cannot have all its Dirichlet coefficients nonnegative. By the prime number theorem in arithmetic progressions, the same δ is the relative natural density, among primes, of the negative prime coefficients. The finite-group inequality itself does not require that analytic density theorem.

**Proof.** Put f₋=max(−f,0). Since E f=−r, E f₋≥r. Cauchy–Schwarz gives

$$
r\le\mathbb E f_-\le\sqrt{\delta\,\mathbb E|f|^2}.
$$

Squaring proves the assertion. Every reduced residue class contains primes, so a negative class already contradicts coefficientwise nonnegativity. ∎

**Sharpness.** Take eχ=−r for every χ. Then f(1)=−rh and f(g)=0 elsewhere. Thus δ=1/h and Σ|eχ|²=hr²: equality holds. Sparse negativity has a precise coefficient-energy cost; it has not disappeared.

**Extension.** The same finite-group proof applies to products of finite-image Artin Euler factors, with irreducible characters in place of abelian characters and uniform probability on the finite Galois group. Conjugacy classes receive their group-size weights. This is an Euler-coefficient statement and does not assume the Artin holomorphy conjecture. It prevents finite field lifts from evading the principal-character sign obstruction merely by using higher-dimensional representations.

### Proposition B: positive mixtures cannot remove both obstructions

Consider a finite positive mixture

$$
H(s)=\sum_{j=1}^{J}c_j\prod_\chi L_q(s,\chi)^{e_{j,\chi}},
\qquad c_j>0,\quad\sum_jc_j=1,
$$

with integer, conjugation-symmetric exponents. Suppose H is regular at s=1 and some term has e_{j,χ₀}<0. Then H has negative prime coefficients.

**Proof.** Every conjugate pair contributes a positive real quantity as real s tends to 1 from the right. The real nonprincipal Dirichlet L-values at 1 are positive, and the principal factor has positive pole coefficient. Therefore the terms with the largest positive principal exponent, if present, have positive leading Laurent coefficients and cannot cancel in a positive mixture. Regularity at 1 forces every e_{j,χ₀}≤0.

The prime coefficient of H is the character polynomial with averaged exponents ēχ=Σ_j c_j e_{j,χ}. Its group mean is ēχ₀<0 because at least one principal exponent is negative. Proposition A's proof applies to these real averaged exponents. ∎

This is a scoped impossibility statement: within this finite positive-mixture class, retaining a reciprocal principal term, removing the pole at 1, and making every Dirichlet coefficient nonnegative are incompatible.

**Necessary qualification.** The function ζ+1/ζ has coefficients 1+μ(n)≥0 and retains reciprocal-zeta poles. It is not a counterexample to Proposition B: it has an unavoidable pole at 1. Landau's theorem then sees that rightmost real singularity and does not exclude poles farther left. Negative mixture weights, infinitely many factors, continuum corrections, or genuinely non-Euler constructions are outside Proposition B; each requires a new sign argument.

## 3. A reciprocal detector with an exact arithmetic gap

Define

$$
A_q(s)=\prod_{\chi\bmod q}L_q(s,\chi)^{-1},\qquad q\ge2.
$$

For p not dividing q let f_p be the multiplicative order of p modulo q. Each f_p-th root of unity occurs h/f_p times among χ(p). Consequently

$$
\boxed{\displaystyle
A_q(s)=\prod_{p\nmid q}(1-p^{-f_ps})^{h/f_p}
=\sum_{n\ge1}a_q(n)n^{-s},\quad \Re s>1.}
$$

Every local exponent is an integer. Every nonconstant local monomial has index p^{f_pj}≡1 mod q. Multiplying the local polynomials proves

$$
a_q(1)=1,\qquad a_q(n)=0\quad(n\not\equiv1\pmod q),
\qquad a_q(n)=0\quad(2\le n\le q).
$$

For a prime p≡1 mod q, a_q(p)=−h. Thus this is a genuine sparse reciprocal detector, not a nonnegative one.

### Proposition C: the pole is retained without a nonprincipal nonvanishing assumption

Every nontrivial zeta zero ρ is a pole of A_q of order at least its zeta multiplicity.

**Proof.** The principal factor is

$$
L_q(s,\chi_0)=\zeta(s)\prod_{p\mid q}(1-p^{-s}).
$$

The finite factors do not vanish for Re s>0. Every nonprincipal L_q is holomorphic there. A zero of another L_q increases the reciprocal product's pole order; it cannot cancel it. The only pole of an individual factor is the principal pole at 1, which is not ρ. ∎

### Proposition D: uniqueness of exact prime isolation

Suppose a monomial F as in Section 2 has principal exponent −r and its prime coefficient f(g) vanishes for every g≠1. Then eχ=−r for every χ, so F=A_q^r.

**Proof.** The group mean fixes f(1)=−rh. Fourier inversion then gives eχ=h⁻¹f(1)χ̄(1)=−r. ∎

Therefore the full inverse character product is forced if one wants a fixed reciprocal principal power and exact isolation of the completely split prime class. There is no cheaper monomial with the same prime-level specification.

### What the gap actually buys

For σ=Re s>1,

$$
\log A_q(s)=-h\sum_{p^k\equiv1\ (q)}\frac{p^{-ks}}{k},
$$

using the logarithm fixed by the Euler product. Hence

$$
|\log A_q(s)|\le h\sum_{m\ge1}(mq+1)^{-\sigma}
\le hq^{-\sigma}\zeta(\sigma),
$$

and

$$
|A_q(s)-1|\le\exp\{hq^{-\sigma}\zeta(\sigma)\}-1.
$$

In particular A_q→1 uniformly on Re s≥1+ε. This argument stops at 1. The absolute Dirichlet series cannot converge at σ≤1: the prime terms in the class 1 alone have magnitudes h p^{−σ}, whose sum diverges there. The early coefficient gap is not an analytic continuation theorem.

For prime q, the product has degree q−1, and the product of the primitive conductors is q^{q−2}: the q−2 nonprincipal characters have conductor q. A gap on the scale q therefore costs log conductor of order q log q. Also, a simple zeta pole in A_q has residue proportional to the reciprocal product of nonprincipal L-values at ρ; its size need not be stable as q grows. This is the reason for changing to logarithmic derivatives next.

## 4. Positive residue propagation and a shifted-zeta identity

Set

$$
D_q(s)=-\frac{A_q'(s)}{A_q(s)}
=\sum_{\chi\bmod q}\frac{L_q'}{L_q}(s,\chi).
$$

For Re s>1 character orthogonality gives

$$
\boxed{\displaystyle
D_q(s)=-\varphi(q)\sum_{n\equiv1\ (q)}\Lambda(n)n^{-s}.}
$$

At a nontrivial zeta zero, D_q has positive integer residue at least its zeta multiplicity. Other character zeros only add positive residues. This statement has no nonprincipal-value denominator and no uncontrolled residue normalization.

For Re s>2, absolute convergence permits summing over all q. Since Σ_{q|m}φ(q)=m,

$$
\sum_{q\ge1}D_q(s)
=-\sum_{n\ge2}\Lambda(n)(n-1)n^{-s}
=\frac{\zeta'}{\zeta}(s-1)-\frac{\zeta'}{\zeta}(s).
$$

Here q=1 means D₁=ζ'/ζ. Thus

$$
\boxed{\displaystyle
\sum_{q\ge2}D_q(s)
=\frac{\zeta'}{\zeta}(s-1)-2\frac{\zeta'}{\zeta}(s),
\qquad \Re s>2.}
$$

This identity is useful precisely because its convergence domain is explicit. Continuing the right-hand side does **not** continue the infinite sum term by term with positivity preserved. At a zeta zero ρ, the right-hand side has negative residue −2m, whereas every summand has positive residue at least m. The discrepancy is a failure of local convergence, not a contradiction to the existence of ρ. At ρ+1, a shifted-zeta pole can appear even though every individual Dirichlet factor is zero-free to the right of 1; it again comes from the infinite-modulus limit.

### Exact finite complement

For integer Q≥2 put

$$
R_Q(m)=m-\sum_{\substack{q\mid m\\q\le Q}}\varphi(q)\ge0,
\qquad
H_Q(s)=\sum_{n\ge2}\Lambda(n)R_Q(n-1)n^{-s}.
$$

Then H_Q has nonnegative Dirichlet coefficients, vanishes through n≤Q+1, and for Re s>2

$$
\boxed{\displaystyle
\sum_{q=2}^Q D_q(s)
=\frac{\zeta'}{\zeta}(s-1)-2\frac{\zeta'}{\zeta}(s)+H_Q(s).}
$$

The finite sum is meromorphic by the ordinary finite L-function theory, so this equation supplies a meromorphic continuation of H_Q. Its sparse, positive initial Dirichlet representation cannot be used outside its convergence domain. The large-divisor complement H_Q is an explicit location of the missing arithmetic cancellation; deleting it would delete the inherited pole information.

## 5. The contour criterion and its exact conductor accounting

Normalize by the number of moduli:

$$
T_Q(s)=\frac{1}{Q-1}\sum_{q=2}^{Q}D_q(s).
$$

On every half-plane Re s≥2+ε, T_Q=Oε(1/Q), directly from the absolutely convergent full sum. Nevertheless its residue at every zeta zero is at least the zeta multiplicity for every Q.

Let U be a bounded Jordan domain whose closure lies in Re s>θ>0, excludes 1, and whose boundary avoids all the character zeros under consideration. Count zeros with multiplicity. The argument principle gives the exact, nonnegative statistic

$$
Z_Q(U)=\frac{1}{2\pi i}\int_{\partial U}T_Q(s)\,ds
=\frac{1}{Q-1}\sum_{q=2}^{Q}\sum_{\chi\bmod q}N_\chi(U)
\ge N_\zeta(U).
$$

This is a genuine propagation theorem: a zeta zero forces a fixed amount of positive family mass. It does not yet supply the upper bound.

### A precise sufficient analytic gate

Choose in advance a countable collection of such domains covering the half-plane Re s>θ away from 1. If for every domain one proves, along unbounded Q with admissible boundaries,

$$
\boxed{\displaystyle \liminf_{Q\to\infty} Z_Q(U)<1,}
$$

then ζ has no zeros in Re s>θ. A stronger sufficient estimate is liminf_Q ∮|T_Q(s)| |ds|<2π. No boundary sequence may be chosen after seeing a hypothetical zero in a way that excludes it. A standard generic choice of boundaries avoids the countable collection of zero locations.

The challenge is to prove this from the explicit shifted-prime-power/divisor formula, not from a zero-free assumption. It allows nonprincipal zeros provided their weighted mass stays below the integer threshold; it does not assume GRH for the rest of the family.

### Why an ordinary primitive-family density theorem is insufficient

Let N_d^*(U) count zeros over primitive characters of exact conductor d, with N₁^*=Nζ. Imprimitive Euler corrections have zeros only on Re s=0, outside U. Regrouping the finite family by primitive conductor gives

$$
\boxed{\displaystyle
Z_Q(U)=N_\zeta(U)
+\sum_{d=2}^{Q}\frac{\lfloor Q/d\rfloor}{Q-1}\,N_d^*(U).}
$$

The principal contribution has coefficient exactly 1. A bound on the primitive high-conductor tail cannot delete this term. In a range where a primitive cumulative bound Σ_{d≤x}N_d^*(U)=O(x^κ) with κ<1 is available, summation by parts only yields convergence of the nonprincipal harmonic sum; the limit is

$$
N_\zeta(U)+\sum_{d\ge2}\frac{N_d^*(U)}d,
$$

not zero. Conversely, normalizing by the total number of characters, of order Q², makes the principal zero contribution disappear at order 1/Q. That recovers a density statement while losing the desired individual conclusion.

## 6. Four-part ledger and research decision

**LOCAL POLE/DEFECT THEOREM — proved:** A_q retains every zeta zero; D_q has residue at least its multiplicity, independent of nonprincipal L-values.

**FAMILY PROPAGATION THEOREM — proved:** Z_Q(U)≥Nζ(U), with exact conductor weights and finite Euler corrections accounted for.

**UNCONDITIONAL UPPER BOUND — only in the safe region:** T_Q=O(1/Q) for Re s≥2+ε. The required contour estimate in the target strip is not proved. Existing primitive density information cannot pay for its principal term.

**CONTRADICTION AND FINAL SCOPE — conditional:** the boxed contour estimate would exclude zeta zeros in the selected half-plane. This pass does not establish that estimate or improve the current zero-free boundary.

The useful next attack is specific: study the smoothed Mellin transform of H_Q, or an equivalent large-divisor statistic on prime powers, with the exact shifted-zeta cancellation retained. Any proposed replacement must be checked against the conductor identity and the positive-mixture obstruction. This is substantially more constrained than asking an unspecified family average to amplify an exceptional member.

## 7. Exact computation and provenance

Run `python replay.py > replay.json` using the Python standard library. The script checks the local Euler identities and sparse support for q=3,4,5,7,8,11,16,31,101 through n=20,000. It checks the sign inequality for all 5^7 exponent vectors on (Z/2Z)^3 with principal exponent −1 and other exponents in [−2,2], including sharp equality examples. It also checks the finite totient-complement and primitive-conductor counting identities.

These computations are exact integer replays of finite algebra. They do not locate hypothetical zeros, certify analytic continuation, or provide the missing contour estimate. The proofs above carry the infinite statements; the computation checks conventions and boundary terms.
