# L-16003 — Gap parity: the CvS finite criterion is a sign-pattern condition on the target

Claim ID: `L-16003`
Title: Gap-parity lower bound for the real roots of the CvS interpolation polynomial, and the exact one-signed characterization
Status: `PROPOSED`
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: elementary real analysis only. Uses the definition of the CvS interpolation polynomial (Connes–van Suijlekom Theorem 5.6(i) / Prop. 5.10, eq. (21)/(24)), and `L-15108` for the translation "real-rooted $\Leftrightarrow$ a PSD special completion exists"
Scope: every finite level, every real target vector with no zero coordinate
Related counterexample candidates: none directly; supplies the counting mechanism used by `R-16001`

---

## Statement

Let $\lambda_{-N}<\lambda_{-N+1}<\dots<\lambda_{N}$ be distinct reals, let $\xi\in\mathbb R^{2N+1}$ have **no zero coordinate**, and set

$$P(s)=\sum_{j}\xi_j\prod_{k\neq j}(\lambda_k-s)=\Omega(s)\,R(s),\qquad \Omega(s)=\prod_k(\lambda_k-s),\qquad R(s)=\sum_j\frac{\xi_j}{\lambda_j-s},$$

so $\deg P=2N$ (the leading coefficient is $(-1)^{2N}\sum_j\xi_j$, nonzero under the CvS normalization $\eta^{\mathsf T}\xi=1$).

**(i) Gap parity.** For each $j$ with $-N\le j\le N-1$ let $I_j=(\lambda_j,\lambda_{j+1})$. Then the number of roots of $P$ in $I_j$, counted with multiplicity, is

- **odd** if $\xi_j\xi_{j+1}>0$;
- **even** (possibly zero) if $\xi_j\xi_{j+1}<0$.

**(ii) Lower bound.** Let

$$S(\xi)=\#\{j:\ \xi_j\xi_{j+1}>0\}\qquad\text{(the number of \emph{same-sign} adjacent pairs)}.$$

Then $P$ has at least $S(\xi)$ real roots, one in each same-sign gap.

**(iii) Exact characterization of the criterion in the one-signed case.** If all $\xi_j$ have the same sign then $S(\xi)=2N=\deg P$, so $P$ has exactly one simple root in each of the $2N$ gaps and **no others**: $P$ is real-rooted with roots strictly interlacing the nodes. Combining with `L-15108`, a PSD special completion with $\ker=\mathbb R\xi$ therefore **always** exists for a one-signed target. (This is the polynomial-side counterpart of `L-16002`.)

**(iv) The criterion as a sign condition — CORRECTED.**

> **Erratum (2026-07-31, prompted by audit `O-15104` point 4).** The first version of (iv) asserted that a real-rooted $P$ has every same-sign gap carrying exactly one root, every sign-change gap exactly two, **and the two outer rays none**. The outer-ray clause is **false**. Exact counterexample: nodes $(-1,0,1)$, $\xi=(-1,3,-1)$ (so $\eta^{\mathsf T}\xi=1$), giving $P(s)=s^{2}-3$ with roots $\pm\sqrt3\approx\pm1.732$ — **both roots lie on the outer rays and both interior gaps are empty**. The statement of (iv) was stronger than its own proof, which had correctly hedged "when no roots lie on the outer rays".

The correct bookkeeping adds an outer-ray parity rule. As $s\to\lambda_N^{+}$, $R(s)\to-\infty\cdot\operatorname{sign}(\xi_N)$; as $s\to+\infty$, $R(s)\sim-(\eta^{\mathsf T}\xi)/s\to0$ with sign $-\operatorname{sign}(\eta^{\mathsf T}\xi)$. Hence

$$\#\{\text{roots in }(\lambda_N,\infty)\}\ \text{is odd}\iff \xi_N\,(\eta^{\mathsf T}\xi)<0,$$

and symmetrically on $(-\infty,\lambda_{-N})$ with $\xi_{-N}$. The complete statement is therefore:

$$P\ \text{real-rooted}\iff\ \text{the }2N+2\ \text{region counts sum to }2N\ \text{subject to: interior gap }(j,j{+}1)\ \text{odd}\iff\xi_j\xi_{j+1}>0,\ \text{each outer ray odd}\iff\xi_{\pm N}(\eta^{\mathsf T}\xi)<0 .$$

Correspondingly the lower bound (ii) improves to

$$\#\{\text{real roots}\}\ \ge\ S(\xi)+\#\{\text{outer rays with odd parity}\},$$

which for an even target is $S(\xi)+2\cdot\mathbf 1[\xi_N(\eta^{\mathsf T}\xi)<0]$. On the counterexample this reads $2\ge0+2$ — sharp. Parts (i)–(iii) are unaffected; only (iv)'s outer-ray clause was wrong.

**(v) Transport to the sampled-$\Xi$ target.** With the CvS coordinates of `O-16001`, $\xi_j=(-1)^{j}a_j$ where $a_j=F(2\pi j)\approx\Xi(2\pi\alpha j)$. Then

$$\xi_j\xi_{j+1}>0\iff a_ja_{j+1}<0,$$

so $S(\xi)$ is exactly the number of **sign changes of the sampled $\Xi$ sequence**, which (generically) counts the sample gaps containing an odd number of zeros of $\Xi$. Hence:

$$\#\{\text{real roots of }P\}\ \ge\ \#\{\text{sign changes of }(\Xi(2\pi\alpha j))_{j=-N}^{N}\}.$$

**Consequently the finite criterion can only pass if the sampling resolves the zeros of $\Xi$**: a pair of $\Xi$-zeros falling inside a single sample gap of width $2\pi\alpha$ produces no sign change and forfeits the corresponding real roots. **The failure mode of the criterion is exactly Lehmer's phenomenon at the sampling scale.**

---

## Definitions

- *Same-sign pair*: an index $j$ with $\xi_j\xi_{j+1}>0$. *Sign change*: $\xi_j\xi_{j+1}<0$.
- All root counts are with multiplicity unless stated otherwise.
- $\eta^{\mathsf T}\xi=\sum_j\xi_j=1$ is the CvS normalization (derivable from their hypotheses, not assumed).

## Motivation

The working note's finite gate is a positivity condition on a matrix pencil, and its Bézoutian reformulation (note §5) is a set of threshold inequalities. Both are analytically opaque: they say nothing about *why* a given target passes or fails.

This lemma replaces both by a **combinatorial** statement about the sign pattern of the target vector, which is immediately readable, immediately computable, and — crucially — immediately interpretable in terms of $\Xi$: via `O-16001` the sign pattern of $\xi$ is the sign pattern of the sampled $\Xi$, so the criterion becomes a statement about how well the sampling resolves the zeros of $\Xi$. That is the first time in this program that the finite condition has been connected to a recognizable analytic property of $\zeta$.

It also explains, rather than merely records, two facts previously known only as computations: why one-signed targets are trivial (`L-16002`), and why the observed real-root counts track the number of $\Xi$-zeros in the sampled window (`R-16001`).

## Proof

**(i).** Fix $j$ and let $s\to\lambda_j^{+}$ from inside $I_j$. In $R(s)=\sum_k\xi_k/(\lambda_k-s)$ every term stays bounded except the $k=j$ term, and $\lambda_j-s\to0^{-}$, so

$$R(s)\longrightarrow -\infty\cdot\operatorname{sign}(\xi_j)\qquad (s\to\lambda_j^{+}).$$

Similarly, as $s\to\lambda_{j+1}^{-}$ the singular term is $k=j+1$ with $\lambda_{j+1}-s\to0^{+}$, so

$$R(s)\longrightarrow +\infty\cdot\operatorname{sign}(\xi_{j+1})\qquad (s\to\lambda_{j+1}^{-}).$$

$R$ is continuous on the open interval $I_j$ (no other node lies in it), so the number of sign changes of $R$ on $I_j$ — hence, by continuity, the number of zeros of $R$ in $I_j$ counted with multiplicity — has the parity of the change of sign between the two endpoints. If $\operatorname{sign}(\xi_j)=\operatorname{sign}(\xi_{j+1})=\sigma$, the endpoint limits are $-\infty\sigma$ and $+\infty\sigma$: opposite signs, so an odd number of zeros. If the signs are opposite, both limits have the same sign, so an even number of zeros. Since $\Omega$ has no zero in the open interval $I_j$, zeros of $R$ in $I_j$ are exactly zeros of $P$ in $I_j$, with the same multiplicities.

**(ii).** Immediate from (i): every same-sign gap contributes at least one root, and the gaps are pairwise disjoint.

**(iii).** If all $\xi_j$ share a sign then every one of the $2N$ gaps is same-sign, so by (i) each contains at least one root; that already accounts for $2N=\deg P$ roots, so each gap contains exactly one, it is simple, and there are no roots elsewhere (in particular none on the outer rays and none nonreal). The interlacing statement is the assertion that the unique root of each gap separates consecutive nodes, which is what was just proved. The final sentence follows from `L-15108`, whose equivalence "positive special completion exists $\Leftrightarrow$ the target polynomial is real-rooted with simple roots" applies verbatim.

*Remark.* (iii) is the classical Nevanlinna/Cauchy-transform argument in disguise: for one-signed $\xi$, $\pm R$ is a Herglotz function of $s$, strictly increasing between consecutive poles, hence with exactly one zero per gap.

**(iv).** The gaps and the two outer rays $(-\infty,\lambda_{-N})$, $(\lambda_N,+\infty)$ partition $\mathbb R\setminus\{\text{nodes}\}$, and $P(\lambda_j)=\xi_j\prod_{k\ne j}(\lambda_k-\lambda_j)\ne0$, so no root is a node. The interior parities are (i). For the outer ray $(\lambda_N,\infty)$: the only singular term as $s\to\lambda_N^{+}$ is $k=N$ with $\lambda_N-s\to0^{-}$, giving $R\to-\infty\cdot\operatorname{sign}(\xi_N)$; and as $s\to+\infty$, $R(s)=\sum_k\xi_k/(\lambda_k-s)=-(\eta^{\mathsf T}\xi)/s+O(s^{-2})$, so $R\to0$ from the side $-\operatorname{sign}(\eta^{\mathsf T}\xi)$. The count is odd iff those two signs differ, i.e. iff $\xi_N(\eta^{\mathsf T}\xi)<0$. The lower ray is symmetric. $P$ is real-rooted iff the $2N+2$ region counts sum to $2N$ subject to all these parities.

**(v).** $\xi_j\xi_{j+1}=(-1)^{j}a_j\cdot(-1)^{j+1}a_{j+1}=-a_ja_{j+1}$, giving the displayed equivalence. If $\Xi$ has an odd number of zeros in the sample gap $(2\pi\alpha j,2\pi\alpha(j+1))$ then $a_j,a_{j+1}$ have opposite signs and the gap contributes; if it has an even number (in particular two, or none) it does not. ∎

## Analytic domain audit

Entirely real, finite-dimensional and elementary. $R$ is a real rational function with simple poles exactly at the nodes; $\Omega$ is a real polynomial with simple zeros exactly at the nodes; $P=\Omega R$ is a polynomial of degree $2N$. No analytic continuation, contour, or branch choice occurs. The hypothesis $\xi_j\ne0$ for all $j$ is essential: a vanishing coordinate removes a pole (CvS Lemma 5.9(ii) covers that degenerate case, where $\lambda_j$ itself becomes a root) and both the parity bookkeeping and the degree count change.

## Dependency audit

- (i)–(iv): self-contained.
- (iii) invokes `L-15108` only for the final sentence translating real-rootedness into existence of a special PSD completion; the polynomial statement itself does not depend on it.
- (v) invokes `O-16001`(c) for $\xi_j=(-1)^{j}a_j$, which is a reconstruction of the program's target and is scoped accordingly.

## Gap audit

1. **(ii) is only a lower bound.** The bound is attained exactly in some families and strictly exceeded in others; see the adversarial tests. Nothing here proves the excess roots are nonreal, so **(ii) cannot be used to prove that a level FAILS** unless one separately knows the sign-change gaps carry no roots. Any claim of the form "$P$ has exactly $S(\xi)$ real roots" is at present **EMPIRICAL**, not proved.
2. The degree count $\deg P=2N$ uses $\sum_j\xi_j\ne0$. Under the CvS normalization this holds, but a construction that normalizes differently must recheck it.
3. Multiplicities: (i) counts with multiplicity, so a double root inside a same-sign gap would violate the odd count — it cannot occur there, but double roots in sign-change gaps are permitted and would break the simplicity that CvS's one-dimensional-kernel hypothesis requires. Simplicity must be certified separately.
4. (v)'s phrase "generically" hides the case where a zero of $\Xi$ falls exactly on a sample point, i.e. $a_j=0$; then $\xi_j=0$ and gap audit item 1 above applies.
5. This lemma says nothing about whether a passing level yields a matrix meeting CvS's **parity** constraints (source odd, diagonal even). That is a separate obligation.

## Adversarial tests

Exact rational arithmetic; real-root counts by Sturm sequences over $\mathbb Q$ on targets rationalized to 100 significant digits, with the counts verified stable under rationalization at 20/30/40/50/60 digits. Full data in `experiments/X-16002-cvs-sampled-target-census/`.

- **Bound (ii) held in 26 of 26 cases** across three families (sampled $\Xi$ at $\alpha\in\{0.3,0.5,0.6,0.8,0.9,1.0\}$; sampled $\operatorname{sinc}$; one-signed targets), $N\in\{5,\dots,10\}$.
- **The bound is attained exactly** ($\#\text{real}=S(\xi)$) in all 8 one-signed and band-limited $\operatorname{sinc}$ cases, confirming (iii) and showing (ii) is sharp.
- **The bound is strictly exceeded** for the sampled-$\Xi$ target in 13 of 18 cases, by 2 to 12 roots. So extra pairs of real roots do appear in sign-change gaps for that family, and the naive "equality" strengthening of (ii) is **false**. Recorded to prevent it being assumed.
- (iii) independently re-verified in exact arithmetic on seven positive targets at $n=3,5,7$ including strongly peaked ones, with one root per node gap in every case (`experiments/X-16001-finsler-cone-collapse`, proposition P5).

## Remaining uncertainty

Parts (i)–(iv) are elementary and the author is confident in them. Part (v) inherits the scope caveat of `O-16001`: it describes the naive sampled target, which may not be the repository's production "repaired" target. The most likely error would be a mis-transported sign convention in $(-1)^{j}$; that factor was derived twice, independently, and checked numerically against the interpolation property $\widehat\xi(2\pi j)=\xi_j$.

## Suggested next attack

1. Prove or refute the converse half: that the roots *not* forced by (ii) are nonreal. An argument-principle or Jensen count on the entire function $\widehat\xi$ (which has exponential type $\tfrac12$, so linear zero density) is the natural route. This is the missing ingredient that would turn the empirical census of `R-16001` into a theorem.
2. Quantify (v): given the sample spacing $2\pi\alpha$, count how many $\Xi$-zero pairs in $|w|\le2\pi\alpha N$ are unresolved. Relate to known lower bounds on zeta zero gaps and to the Lehmer pairs used by Rodgers–Tao in proving $\Lambda\ge0$. A cofinal schedule must resolve *every* pair eventually, which is a strong and interesting requirement in its own right.
3. Use (iii) contrapositively as a cheap screening test in the exact checker.
