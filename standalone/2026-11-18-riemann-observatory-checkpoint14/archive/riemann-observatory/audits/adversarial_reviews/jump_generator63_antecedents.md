# Primary antecedents for the logarithmic factorial RH criterion

The closest verified antecedent is Michel Balazard's Proposition 11, which gives the closed-span obstruction on the same discrete Hilbert space and explicitly treats all zero multiplicities. Applying it to the jump series \(\eta'\) proves the logarithmic factorial criterion. Manzur–Noor's Theorem 5.1 supplies the related fixed-time, single-member criterion. Bober, Borisov and Báez-Duarte's work on Vasyunin's correction use the same parity seed and central binomial family. I located no explicit statement of the logarithmic factorial target membership in the bounded set of primary texts inspected here. [Balazard, arXiv:1812.04309v1](../../sources/jump_generator63_antecedents/balazard_1812.04309.pdf) · [Manzur–Noor, arXiv:2610.03568v1](../../sources/jump_generator63_antecedents/manzur_noor_2610.03568v1.pdf)

## The direct antecedent and its specialization

Let \(S\) be the space of integer unit-cell functions with norm squared \(\sum_n |b_n|^2/[n(n+1)]\), and put \(b_0=0\). Write \(f_k(x)=k\lfloor x/k\rfloor-\lfloor x\rfloor\) and \(W_\zeta=\overline{\operatorname{span}}\{f_k:k\ge2\}\). Balazard's \(D_0\) is exactly \(S\), and his \(B_0\) is the finite span of \(r_k(x)=\{x/k\}-\{x\}/k=-f_k(x)/k\). Thus \(\overline{B_0}=W_\zeta\). Proposition 8 identifies \(F(s)=\sum (b_n-b_{n-1})n^{-s}\) with \(s\int_1^\infty b(x)x^{-s-1}dx\) to the right of \(1/2\) by analytic continuation. Proposition 10 gives RH iff \(W_\zeta=S\), crediting Báez-Duarte for the strong closure theorem. Proposition 11 states that membership forces \(F/\zeta\) holomorphic on this half-plane. Its proof passes each vanishing zero jet to the norm limit in (11), including all derivative orders below the multiplicity. This is the same obstruction needed for the proposed criterion, including its discrete geometry. Balazard asks the general reverse implication in Question 2 in §6. The specialization below uses only the necessary implication and the RH direction of Proposition 10. [Balazard §§1,3–4,6](../../sources/jump_generator63_antecedents/balazard_1812.04309.pdf) · [Published chapter record](https://doi.org/10.1007/978-3-030-61887-2_3) · [Bagchi Theorem 1](../../sources/prefix_skeptic62_criteria2/bagchi.pdf)

For each fixed integer \(k\ge2\), define
\[
 a^{(k)}_n=\sum_{j\le n}(\log j)(k1_{k\mid j}-1)
 =k\log(q!)+kq\log k-\log(n!),\qquad q=\lfloor n/k\rfloor .
\]
Since the partial sums of \(k1_{k\mid j}-1\) equal \(f_k(n)\) and are bounded, summation by parts gives \(a^{(k)}_n=O_k(1+\log n)\). Hence \(a^{(k)}\in S\). The jump group multiplies jump \(j\) by \(j^{i\tau}\). On this vector the difference quotient converges strongly to \(i a^{(k)}\). Summation by parts bounds each quotient by \(2\|f_k\|_\infty\log n\), square summable in the step norm, and finite cell sums give the pointwise limit. Thus \(Gf_k=i a^{(k)}\), with no need for a spectral description of \(G\). [Manzur–Noor equations (13)–(14)](../../sources/jump_generator63_antecedents/manzur_noor_2610.03568v1.pdf) · [Independent generator-domain proof](jump_generator63_skeptic.md)

Its jump series and quotient on the far right are
\[
\begin{split}
 F_k^{\mathrm{log}}(s)&=-\frac{d}{ds}\bigl[(k^{1-s}-1)\zeta(s)\bigr],\\
 \frac{F_k^{\mathrm{log}}(s)}{\zeta(s)}
   &=(1-k^{1-s})\frac{\zeta'(s)}{\zeta(s)}+k^{1-s}\log k .
\end{split}
\]
At any zero \(\rho\) in the right half of the open critical strip with order \(m\), the latter expression has a simple pole of residue \(m(1-k^{1-\rho})\ne0\). The modulus of \(k^{1-\rho}\) is greater than 1. Balazard's Proposition 11 now implies that membership rules out every such zero, and reflection excludes all left-hand exceptions. Conversely RH gives all of \(S\). Equivalently the \((m-1)\)-st Mellin derivative separates the logarithmic vector from the span because \(F_k^{\mathrm{log}}\) vanishes to precisely order \(m-1\). This uses no zero-density estimate and makes no simplicity assumption. The conclusion is for each individual fixed \(k\), including \(k=2\). [Explicit jet calculation and norm bound](jump_generator63_single_member_skeptic.md) · [Balazard Proposition 11](../../sources/jump_generator63_antecedents/balazard_1812.04309.pdf)

For \(k=2\) the jump series is exactly \(\eta'(s)\), where \(\eta(s)=(1-2^{1-s})\zeta(s)\). The target has cell values
\[
 a_{2q}=\log\frac{(2q)!!}{(2q-1)!!}
 =\log\frac{4^q}{\binom{2q}{q}},\qquad
 a_{2q+1}=\log\frac{(2q)!!}{(2q+1)!!}.
\]
Stirling gives \(a_n=\frac12(-1)^n\log n+\frac12\log(\pi/2)+O(1/n)\). The adjacent-value sum tends to the logarithm of the Wallis product, \(\log(\pi/2)\). The closure criterion refers to the full alternating sequence in the stated norm.

## Closely matching antecedents and their scope

- **Manzur–Noor v1, Theorems 4.1 and 5.1.** At each fixed real \(\tau\ne0\), membership of \(T_\tau h_k\) for some integer \(k\ge2\) is equivalent to RH. Equation (22) and its iteration propagate an off-line zero through a vertical arithmetic progression. Ingham's fixed-threshold density bound excludes that progression. For an order-\(m\) zero ordinary evaluation has a zero of order \(m\) in \(\tau\) at 0. The first infinitesimal obstruction at a multiple zero therefore uses the higher evaluation jet from Balazard's Proposition 11. The source supplies the group and the fixed-time criterion. [Primary source, pp. 4–5](../../sources/jump_generator63_antecedents/manzur_noor_2610.03568v1.pdf)
- **Bober and Borisov.** Bober's Theorem 1.1 (2) with parameters \(a=b=1\) is exactly \(-f_2\), and Theorem 1.2 (7) with the same parameters is \(\binom{2n}{n}\). Their link is the classical floor formula for factorial valuations used in the Landau classification, and §1.1 puts the balanced floor sums in the Nyman–Beurling space. Borisov §3 and Theorem 14 likewise link balanced floor sums with factorial ratios, and explicitly use \(\eta(s)=(1-2^{1-s})\zeta(s)\) and the summation-by-parts zero witness \(n^{-\rho}-(n+1)^{-\rho}\) for the constant target. These are exact antecedents to the seed and the basic zero witness. The logarithmic factorial target evaluates the log-weighted jumps of the seed. [Bober preprint](../../sources/jump_generator63_antecedents/bober_0709.1977.pdf) · [Published article](https://doi.org/10.1112/jlms/jdn078) · [Borisov §3](../../sources/jump_generator63_antecedents/borisov.pdf)
- **Báez-Duarte's logarithmic continuous target.** In arXiv:math/0011254v1 §1.2, equations (1.10)–(1.11) and Theorem 1.2 use \(\lambda(t)=\mathbf1_{(0,1]}(t)\log t\), with real dilations. The ordinary real-dilation difference quotient recovers the constant. The Mellin transform of this continuous logarithm is \(-1/s^2\), whereas the step target here has transform \(\eta'(s)/s\) for \(k=2\). The publisher abstract for the related 2002 paper likewise uses \(\lambda\). Direct PDF routes for that journal manifestation did not yield the text in this check. [Primary arXiv preprint, §1.2](../../sources/logarithmic_riesz_priority_skeptic_round4/baez_arithmetical2000.pdf) · [2002 publisher abstract](https://doi.org/10.1155/S0161171202013248)
- **Operators and multiplicities.** Burnol's §5 uses real dilation contractions on a continuous Hardy-space model and discusses derivative-based zero witnesses, including critical-line jets for a quantitative lower bound. The integer composition semigroup \(W_n\) in Manzur–Noor–Santos is indexed by the multiplicative integers, with normalized isometries and a cyclicity problem. It differs from the real-time jump phase transport. The rStation paper 1 v11 §8 juxtaposes integer dilation invariance and the Manzur–Noor fixed-time criterion. I used that portion as a contemporary pointer to the two operator settings. [Burnol §5](../../sources/jump_generator63_antecedents/burnol_math_0112254.pdf) · [Manzur–Noor–Santos §§1,3](../../sources/ratio62_semigroup/manzur_noor_santos.pdf) · [rStation paper 1 v11](https://rstation.ai/problems/riemann_hypothesis/papers/1/v11)

## The exact von Mangoldt coefficients and a failed direct truncation

Balazard's coefficient map is \(w=\mu*u\), where \(u\) is the jump sequence. For the logarithmic target \(-\zeta'/\zeta=\sum\Lambda(n)n^{-s}\) in \(\Re s>1\) gives exactly
\[
 w_k(n)=k1_{k\mid n}\Lambda(n/k)-\Lambda(n)+k\log k\,1_{n=k},
\]
with the first summand treated as zero if \(k\nmid n\). For \(k=2\) this equals \(\log2\) at powers of two, \(-\log p\) at powers of odd primes \(p\), \(2\log p\) at twice such odd prime powers, and zero elsewhere. This identifies the explicit target's arithmetic coefficients within the existing Vasyunin–Balazard coordinate system. [Balazard §§1–3, Propositions 4 and 7](../../sources/jump_generator63_antecedents/balazard_1812.04309.pdf)

An exact coefficient version follows by the same projection argument Balazard credits to Weingartner for the constant target. Write \(P_N a^{(k)}=\sum_{j=2}^N b_{j,N}r_j\) for the orthogonal projection onto the usual finite span. The coefficient \(w(j)\) in the jump-series quotient is \(-b_{j,N}\) for \(j\ge2\), since the quotient for \(r_j\) is \(1/j-j^{-s}\). The projections converge strongly to \(P_{W_\zeta}a^{(k)}\). Each \(w(j)\) is a finite linear combination of continuous cell evaluations, so \(\lim_N b_{j,N}=-w_k(j)\) for every \(j\ge2\) if the target lies in the span closure. Conversely those identities force the difference between the target and its projection to have arithmetic coefficient supported only at 1. Its cell values would be a constant times \(\lfloor x\rfloor\), which is in \(S\) only for zero constant. Thus these coefficient limits are another exact version of the same criterion. Yang's 2026 publisher abstract generalizes Weingartner's constant-target setting to \(L^p\). The subscription full text was outside this check. [Balazard Propositions 12–13](../../sources/jump_generator63_antecedents/balazard_1812.04309.pdf) · [Weingartner publisher record](https://doi.org/10.1016/j.aim.2006.04.003) · [Yang publisher abstract](https://doi.org/10.1007/s00013-026-02256-9)

A pointwise finite identity follows from \(\log n=\sum_{d\mid n}\Lambda(d)\):
\[
 a^{(k)}(x)=k\log k\lfloor x/k\rfloor+
              \sum_{d\le x}\Lambda(d)f_k(x/d).
\]
Here \(a^{(k)}(x)=a^{(k)}_{\lfloor x\rfloor}\). The dilated seed belongs to the finite span, since \(d f_k(x/d)=f_{kd}(x)-f_d(x)\), with \(f_1=0\). A natural attempt is
\[
 A_M(x)=\log k\,[f_k(x)-f_M(x)]
          +\sum_{d\le M}\Lambda(d)f_k(x/d),\qquad M\ge2.
\]
It is an actual finite-span element and agrees with the target for \(1\le x<M\). It diverges in the step norm as an approximating sequence. To see this, for \(M\le x<2M\) every omitted \(f_k(x/d)\) with \(M<d\le x\) is \(-1\), so
\[
 A_M(x)-a^{(k)}(x)=\psi(x)-\psi(M)-M\log k .
\]
On an interval of length \(c_k M/\log M\) to the right of \(M\), the elementary bound \(\Lambda(n)\le\log n\) makes the first two terms together at most \(\tfrac12 M\log k\) for sufficiently small fixed \(c_k>0\). The squared norm of the defect is \(\gg_k M/\log M\). Báez-Duarte's 2005 note already uses \(-f_2(x/d)\) as (2.1), and shows divergence of Vasyunin's correction to the constant. The explicit defect here applies to the displayed von Mangoldt truncation for the logarithmic target. [Báez-Duarte 2005, §2](../../sources/jump_generator63_antecedents/baez_vasyunin_0506318.pdf)

## Bounded search record

The searches combined Nyman–Beurling and Báez-Duarte with logarithmic factorial, gamma, central binomial, Wallis, von Mangoldt, eta derivative, jump, generator, differentiation, and fixed-time membership, including French terms and citation trails from the identified primary papers. I read the pinned passages detailed above. The related 2002 and 2026 journal manifestations noted above were inspected at abstract level. This identifies the exact general obstruction in Balazard's preprint, its published counterpart, and the specialization to the explicit logarithmic target. It leaves historical priority for that particular specialization open. [Pinned PDF digests](../../sources/jump_generator63_antecedents/SHA256SUMS)
