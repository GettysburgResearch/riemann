# L-16004 — Closed form for the special completion: the Loewner matrix of `-P'/P`, and automatic parity

Claim ID: `L-16004`
Title: The CvS special positive completion is the Loewner matrix of `-P'/P`; positivity and parity are both automatic consequences of the root structure
Status: `PROPOSED`
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `L-15108` (the converse this lemma makes explicit); Connes–van Suijlekom Theorem 5.6, form (11); `O-16001` for notation
Scope: every finite level with `P` squarefree and non-vanishing at the nodes
Related counterexample candidates: none

---

## Statement

Let $\lambda_{-N}<\dots<\lambda_N$ be the nodes, let $\xi$ be a target with $\eta^{\mathsf T}\xi\neq0$, and let

$$P(s)=\sum_j\xi_j\prod_{k\neq j}(\lambda_k-s)=A\prod_{m=1}^{2N}(\mu_m-s),\qquad A=\eta^{\mathsf T}\xi\ne0,$$

be the CvS interpolation polynomial, assumed squarefree with $P(\lambda_i)\neq0$ for every $i$ (both automatic when every $\xi_i\neq0$). Define

$$g(s):=-\frac{P'(s)}{P(s)}=\sum_{m=1}^{2N}\frac{1}{\mu_m-s},$$

and let $Q$ be the **Loewner (divided-difference) matrix of $g$ at the nodes**:

$$\boxed{\;Q_{ij}=\frac{g(\lambda_i)-g(\lambda_j)}{\lambda_i-\lambda_j}\ \ (i\neq j),\qquad Q_{ii}=g'(\lambda_i).\;}$$

Equivalently, with $b_i=g(\lambda_i)=-P'(\lambda_i)/P(\lambda_i)$ and $a_i=g'(\lambda_i)=\bigl(P'(\lambda_i)^2-P(\lambda_i)P''(\lambda_i)\bigr)/P(\lambda_i)^2$, $Q$ is exactly the special matrix of CvS form (11) with source $b$ and diagonal $a$. Then:

**(i) Rank-one decomposition.** Writing $\ell(\mu)\in\mathbb C^{2N+1}$ for the vector $\ell(\mu)_j=1/(\lambda_j-\mu)$,

$$Q=\sum_{m=1}^{2N}\ell(\mu_m)\,\ell(\mu_m)^{\mathsf T}.$$

**(ii) Positivity is exactly real-rootedness.** If every $\mu_m$ is real then $Q\succeq0$, and since the $2N$ vectors $\ell(\mu_m)$ are linearly independent (a Cauchy-matrix argument, the $\mu_m$ being distinct and distinct from the nodes), $\operatorname{rank}Q=2N$, i.e. $\ker Q$ is exactly one-dimensional. Conversely a nonreal conjugate pair $\mu,\bar\mu$ contributes $2\operatorname{Re}\bigl(\ell(\mu)\ell(\mu)^{\mathsf T}\bigr)$, which has signature $(1,1)$ on its two-dimensional range; so each nonreal pair forces a negative eigenvalue and $Q\not\succeq0$.

**(iii) The kernel is the target.** $\ker Q=\mathbb R\xi$.

**(iv) Parity is automatic.** If the node set is symmetric ($\lambda_{-i}=-\lambda_i$) and $\xi$ is even, then the root multiset $\{\mu_m\}$ is symmetric under $\mu\mapsto-\mu$, hence $g$ is **odd**; therefore the source $b_i=g(\lambda_i)$ is odd and the diagonal $a_i=g'(\lambda_i)$ is even, which is exactly CvS form (11). Consequently **the parity constraints of Theorem 5.6 are satisfied automatically, with no freedom to be chosen and no obstruction to check**, and $Q\gamma=\gamma Q$.

**(v) Consequence.** `L-15108`'s converse becomes explicit and constructive: the special PSD completion with prescribed kernel, when it exists, may be written down in closed form directly from $P$, with no eigen-decomposition, no choice of metric weights, and no parity repair.

---

## Motivation

`L-15108` establishes that a special PSD completion with $\ker=\mathbb R\xi$ exists iff the target polynomial is real-rooted, but its proof of the existence direction is non-constructive: it diagonalizes the quotient operator, *chooses* positive metric weights on a real eigenbasis, and pulls back. Its §5 then argues that the weights can be chosen to respect parity, and its own gap audit (item 3) flags that "parity must be built into the quotient metric; it is not automatic from an arbitrary eigenbasis".

This lemma removes all of that. There is a canonical choice — the Loewner matrix of $-P'/P$ — for which positivity is a one-line consequence of a rank-one decomposition and parity is automatic. It converts the most delicate remaining hypothesis of the whole finite programme into a triviality, and it supplies a certificate that a verifier can check in exact arithmetic without ever computing a root.

## Proof

**(i).** Partial fractions give $g(s)=\sum_m(\mu_m-s)^{-1}$ directly from $P=A\prod_m(\mu_m-s)$. Then for $i\neq j$,

$$\frac{g(\lambda_i)-g(\lambda_j)}{\lambda_i-\lambda_j}=\frac{1}{\lambda_i-\lambda_j}\sum_m\left[\frac1{\mu_m-\lambda_i}-\frac1{\mu_m-\lambda_j}\right]=\frac{1}{\lambda_i-\lambda_j}\sum_m\frac{\lambda_i-\lambda_j}{(\mu_m-\lambda_i)(\mu_m-\lambda_j)}=\sum_m\frac{1}{(\mu_m-\lambda_i)(\mu_m-\lambda_j)},$$

which is $\sum_m\ell(\mu_m)_i\ell(\mu_m)_j$. For $i=j$ the confluent limit gives $g'(\lambda_i)=\sum_m(\mu_m-\lambda_i)^{-2}=\sum_m\ell(\mu_m)_i^2$. So (i) holds entrywise, including the diagonal.

**(ii).** With all $\mu_m$ real, each summand is a real rank-one PSD matrix, so $Q\succeq0$. Independence of $\{\ell(\mu_m)\}_{m=1}^{2N}$: the $(2N+1)\times 2N$ matrix with entries $1/(\lambda_j-\mu_m)$ is a Cauchy matrix in the $\lambda$'s and $\mu$'s; any $2N\times2N$ minor is a Cauchy determinant $\prod_{p<q}(\lambda_p-\lambda_q)(\mu_q-\mu_p)/\prod_{p,q}(\lambda_p-\mu_q)$, nonzero because the $\lambda$'s are distinct, the $\mu$'s are distinct ($P$ squarefree) and no $\mu$ equals a node ($P(\lambda_i)\neq0$). Hence $\operatorname{rank}Q=2N$ and $\dim\ker Q=1$. For a nonreal pair, $\ell(\bar\mu)=\overline{\ell(\mu)}$, and on the real two-plane spanned by $\operatorname{Re}\ell(\mu),\operatorname{Im}\ell(\mu)$ the form $2\operatorname{Re}(\ell\ell^{\mathsf T})$ acts as $2(uu^{\mathsf T}-vv^{\mathsf T})$ with $u=\operatorname{Re}\ell$, $v=\operatorname{Im}\ell$, of signature $(1,1)$; so it contributes a negative direction.

**(iii).** $Q\xi=0$ is equivalent to $\langle\ell(\mu_m),\xi\rangle=0$ for every $m$ when $Q\succeq0$. Now $\langle\ell(\mu),\xi\rangle=\sum_j\xi_j/(\lambda_j-\mu)=P(\mu)/\Omega(\mu)$ with $\Omega(s)=\prod_j(\lambda_j-s)$, which vanishes exactly when $P(\mu)=0$. So each $\ell(\mu_m)\perp\xi$ and $Q\xi=0$; combined with $\dim\ker Q=1$ this gives $\ker Q=\mathbb R\xi$. (In the indefinite case the same computation shows $Q\xi=0$ still holds.)

**(iv).** With symmetric nodes and even $\xi$, $\Omega$ has the parity of $s\mapsto\Omega(-s)$ up to sign and $P(-s)=\pm P(s)$; in either case the root multiset is invariant under $\mu\mapsto-\mu$. Then $g(-s)=\sum_m(\mu_m+s)^{-1}=\sum_m(-\mu_m+s)^{-1}$ after reindexing $\mu\mapsto-\mu$, which is $-g(s)$. So $g$ is odd, $b_i=g(\lambda_i)$ is odd, and $a_i=g'(\lambda_i)$ is even since the derivative of an odd function is even. That $Q$ then commutes with $\gamma$ is immediate from $Q_{-i,-j}=Q_{ij}$. ∎

## Analytic domain audit

Finite-dimensional and rational throughout. $g$ is a real rational function with simple poles exactly at the roots of $P$; it is evaluated only at the nodes, where $P\neq0$ by hypothesis, so no singularity is encountered. When all $\mu_m$ are real, $g$ is a Herglotz–Nevanlinna function of $s$ and $Q$ is its Loewner matrix; the positivity in (ii) is the finite-dimensional shadow of Loewner's theorem on matrix-monotone functions, though the direct rank-one proof given above is self-contained and does not invoke it.

## Dependency audit

- Partial fractions and the Cauchy determinant — elementary, used in (i) and (ii).
- CvS form (11) — used only to observe that $(b,a)$ is exactly the required shape.
- `L-15108` — **not used**; this lemma reproves its existence direction constructively and removes its §5 parity caveat.

## SCOPE CAUTION (added 2026-07-31) — (ii) is true here and false if lifted

(ii)'s sentence *"each nonreal pair forces a negative eigenvalue and $Q\not\succeq0$"* is correct **in this lemma's setting**, where there are exactly $2N$ poles in dimension $2N+1$: the PSD part contributed by the real poles then has rank at most $2N-2k$ for $k$ nonreal pairs, its kernel has dimension at least $2k+1$, and the rank count leaves a negative direction that nothing can cover. The proof above uses that.

**Lifted out of that setting to an over-determined form — many more poles than nodes — the sentence is false.** Verified independently (`experiments/X-16003-source-atlas/overdet.py`, mpmath dps 120): with a uniform real ladder $\mu_k=k\pi/2$, $k=1..20$, plus **one** nonreal quadruple at $\pm\mu_*\pm id$, the inertia stays $(\dim,0,0)$ — positive definite — over wide ranges of $d$:

| $N$ | dim | $\mu_*$ | $\mu_*/N$ | $d=0.1$ | $d=1$ | $d=10$ |
|---|---|---|---|---|---|---|
| 4 | 9 | 7.854 | 1.96 | $(9,0,0)$ | $(9,0,0)$ | $(9,0,0)$ |
| 4 | 9 | 31.416 | 7.85 | $(9,0,0)$ | $(9,0,0)$ | $(9,0,0)$ |
| 6 | 13 | 12.566 | 2.09 | $(13,0,0)$ | $(13,0,0)$ | $(13,0,0)$ |
| 8 | 17 | 31.416 | 3.93 | $(17,0,0)$ | $(17,0,0)$ | $(17,0,0)$ |
| 8 | 17 | 1.571 | 0.20 | $(15,2,0)$ | $(15,2,0)$ | $(15,2,0)$ |

The pattern is that the nonreal quadruple is only *seen* when it sits near or inside the node band — roughly $\mu_*/N\lesssim1.5$ here — and is essentially invisible outside it, moving $\lambda_{\min}$ by under $1\%$.

**Why this matters for the programme.** The arithmetic source $\psi_W$ has poles at all the zeta zeros sampled at finitely many nodes, i.e. it is squarely in the **over-determined** regime, not this lemma's. So **"a single off-line zero must break positivity of a finite Weil matrix" does not follow from (ii)** and needs its own argument. Anyone building a counterexample search on that implication should stop and re-derive it. The credit for spotting this is to a parallel detectability study run this session; I have re-verified it independently rather than taking it on report.

## Gap audit

1. **Squarefreeness and $P(\lambda_i)\neq0$ are hypotheses.** A repeated root of $P$ breaks the rank count in (ii) and the kernel is then larger than one-dimensional, so the CvS one-dimensional-kernel hypothesis genuinely fails. This is the same repeated-root caveat as working-note Remark 5.5.
2. (iv) assumes the root multiset is symmetric, which follows from symmetric nodes and even $\xi$. A target that is not exactly even loses the conclusion.
3. This lemma says **nothing** about whether $P$ is real-rooted for any particular target. It converts that question into positivity of $Q$ and back; it does not answer it. In particular it does not bear on `R-16001`, whose content is that $P$ is *not* real-rooted for the programme's targets below $\alpha_c$.
4. The construction requires knowing $P$, not its roots — $b_i$ and $a_i$ are computed from $P,P',P''$ at the nodes by exact rational arithmetic. But *verifying* $Q\succeq0$ still requires an exact inertia computation; the rank-one form is a proof device, not a shortcut for the checker.

## Adversarial tests

Exact rational arithmetic, targets $\xi_j=(-1)^j\Xi(2\pi\alpha j)$ rationalized to 100 significant digits, inertia by exact symmetric congruence:

| $\alpha$, $N$ | exact #real roots of $P$ | inertia of $Q$ | $Q\succeq0$? | $b$ odd? | $a$ even? |
|---|---|---|---|---|---|
| $1.1,\ 6$ | $12$ of $12$ (**PASS**) | $(12,0,1)$ | **yes** | yes | yes |
| $1.0,\ 6$ | $8$ of $12$ (fail) | $(10,2,1)$ | no | yes | yes |
| $0.9,\ 6$ | $8$ of $12$ (fail) | $(10,2,1)$ | no | yes | yes |

Exactly as (ii) and (iv) predict: the number of negative eigenvalues equals the number of nonreal conjugate pairs ($4$ nonreal roots $\to 2$ negative directions), the kernel is one-dimensional in every case, and **parity holds whether or not the level passes** — confirming that parity is structural and independent of positivity. Stability re-verified at rationalization precisions 20/30/40/60/80.

**A methodological warning recorded from this test.** An earlier automated certificate reported "all CvS hypotheses satisfied" at $\alpha=1.0$, $N=6$ on the strength of a *leading principal minors all positive* test. That test is **not** a valid positive-semidefiniteness check for a singular matrix: $Q$ there has inertia $(10,2,1)$ and is indefinite. Sylvester's criterion in leading-minor form characterizes positive *definiteness*; for a matrix with a kernel one must use all principal minors, or an exact congruence/inertia computation. Any checker in this repository that gates on leading minors should be corrected.

## Remaining uncertainty

The algebra is elementary and was verified exactly. The author is confident in (i)–(iv). The main risk is hypothesis creep: (iv) requires exact evenness of the target, and any production pipeline that only approximately symmetrizes will not inherit the conclusion.

## Suggested next attack

1. Add the closed form to the exact checker as the canonical completion, replacing any eigen-decomposition route; it needs only $P,P',P''$ at the nodes.
2. Audit every existing certificate in the repository that uses a leading-principal-minor test for semidefiniteness.
3. Use (ii) quantitatively: the number of negative eigenvalues of $Q$ equals the number of nonreal conjugate pairs of $P$, so the inertia of the Loewner matrix is an alternative, root-free measurement of the deficit studied in `R-16001` — potentially much cheaper than root isolation at large $N$.
