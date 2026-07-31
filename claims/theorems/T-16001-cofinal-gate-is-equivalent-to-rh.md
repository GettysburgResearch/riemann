# T-16001 — The cofinal gate is satisfiable, and satisfiability is exactly equivalent to RH

Claim ID: `T-16001`
Title: The level-$N$ admissible set is an $(N{+}1)$-parameter family with freely prescribable real zeros; an explicit satisfying sequence exists; and satisfiability of the working note's hypotheses is equivalent to RH
Status: `PROPOSED`
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `L-15108` (Reading A of the gate); `O-16001`; Connes–van Suijlekom Theorem 5.6; Laguerre–Pólya theory (Laguerre; Pólya–Schur 1914; Levin, *Distribution of Zeros of Entire Functions*, Ch. VIII); Hadamard factorization of $\xi$
Scope: **Reading A** of hypothesis (9) — see §0. Reading B is explicitly *not* settled.
Related counterexample candidates: none

---

## 0. The reading, stated first because everything depends on it

Hypothesis (9) of the working note (`T-15104.7`) admits two inequivalent readings, and the repository has been using them interchangeably.

- **Reading A (arbitrary special completion).** *Some* special PSD matrix $Q$ with $\ker Q=\mathbb R p$ exists. By `L-15108` this is equivalent to $P$ being real-rooted with simple roots. **This is what `L-16003`, `R-16001`, `X-16002` and this theorem decide.**
- **Reading B (the one-scalar arithmetic pencil).** The *given arithmetic* $Q_j$ is fixed and only the scalar $c$ may be chosen, as literally written in `T-15104.4`. `L-15108` §6 states this subfamily is **strictly smaller**, and that this is the entire point: *"a noncircular sufficient test that can, in principle, be proved from arithmetic structure without first knowing the target polynomial is real-rooted."*

Everything below is **Reading A**. §5 states exactly what does and does not carry over.

## Statement

**(i) The gate is a free-zero condition.** Fix nodes $\lambda_{-N}<\dots<\lambda_N$. The map

$$\xi\ \longmapsto\ P_\xi(s)=\sum_{j}\xi_j\prod_{k\neq j}(\lambda_k-s)$$

is a **linear bijection** $\mathbb R^{2N+1}\to\mathbb R_{\le 2N}[s]$, with inverse the Lagrange formula

$$\xi_i=\frac{P(\lambda_i)}{\prod_{k\neq i}(\lambda_k-\lambda_i)} .$$

It restricts to a bijection $\{\text{even }\xi\}\to\{\text{even polynomials of degree}\le 2N\}$. Consequently **the $2N$ roots of $P$ may be prescribed arbitrarily on $\mathbb R$**, and every real-rooted even $P$ arises from an admissible even target. Reading A of the gate therefore imposes **no restriction whatever** beyond "choose $2N$ real numbers".

**(ii) Parameterisation of the admissible transforms.** The real even level-$N$ CvS transforms having only real zeros are exactly

$$F(z)=C\prod_{i\le N}\Bigl(1-\frac{z^{2}}{u_i^{2}}\Bigr)\prod_{m>N}\Bigl(1-\frac{z^{2}}{4\pi^{2}m^{2}}\Bigr),\qquad \xi_j=(-1)^{j}F(2\pi j),$$

with $C$ and $u_1,\dots,u_N$ free real parameters — an $(N{+}1)$-parameter family, matching the dimension count. The second product is the **sinc skeleton**, the zeros at $2\pi m$, $|m|>N$, that CvS Theorem 5.6(ii) leaves in place; the $u_i$ are free.

**(iii) An explicit satisfying sequence (the zero-matched target).** Let $\gamma_n$ be the ordinates of the zeros of $\Xi$ and set

$$F_N(z)=\Xi(0)\prod_{n\le N}\Bigl(1-\frac{z^{2}}{\gamma_n^{2}}\Bigr)\prod_{m>N}\Bigl(1-\frac{z^{2}}{4\pi^{2}m^{2}}\Bigr),\qquad \xi_j=(-1)^{j}F_N(2\pi j).$$

Then hypothesis (9) holds at **every** level by construction, and hypothesis (8) holds — $F_N\to\Xi$ locally uniformly on all of $\mathbb C$ — because $\sum\gamma_n^{-2}<\infty$ makes the $\Xi$-tail product tend to $1$, and $\bigl|\log\prod_{m>N}(1-z^{2}/4\pi^{2}m^{2})\bigr|\le R^{2}/(2\pi^{2}N)\to0$ on $|z|\le R$.

**So the hypotheses of the working note's Theorem 3.1 are SATISFIABLE, and the theorem is not vacuous.**

**(iv) But satisfiability is exactly RH.** The following are equivalent:

1. RH;
2. $\Xi\in$ the Laguerre–Pólya class;
3. some sequence of real-rooted real polynomials converges to $\Xi$ locally uniformly on $\mathbb C$;
4. some sequence of real-rooted real entire functions converges to $\Xi$ locally uniformly on $S_{1/2}$;
5. hypotheses (8) and (9-Reading A) are jointly satisfiable.

**(v) Consequence.** The working note's Theorem 3.1 is a **reformulation of RH, not a reduction**. No purely structural or soft-analytic proof of its cofinal gate can exist: by (i) the admissible set at each level is a full $(N{+}1)$-parameter family with *free* real zeros, and the correct member is the one whose free zeros are the $\gamma_n$ — so knowing that those are real **is** RH. Positivity of $\Phi$, Cauchy–Schwarz, interlacing, Nyquist density and tapering are all insensitive to the truth of RH and cannot discriminate.

**(vi) A rate.** Since $|z|<2\pi(N{+}1)$ contains no forced (skeleton) zeros, matching $\Xi$'s zeros up to height $R$ requires $2N\ge(R/\pi)\log(R/2\pi e)$, i.e. $R\lesssim 2\pi N/\log N$. The zero-matched construction attains this exactly.

---

## Motivation

`R-16001` showed that the repository's actual target sequence fails the gate. That left the decisive question open: is the failure a defect of *that* construction, or is the gate unsatisfiable in principle — in which case Theorem 3.1 would be vacuously true and the entire positive route dead?

This theorem answers it, and the answer reframes the programme. The gate is satisfiable, easily; what it is *not* is informative. Recording this prevents two opposite errors: concluding from `R-16001` that the route is dead, and hoping that some cleverer structural argument will establish the gate.

## Proof sketch

**(i).** Both spaces have dimension $2N+1$. Evaluating $P_\xi$ at $\lambda_i$ kills every term but the $i$-th, giving $P_\xi(\lambda_i)=\xi_i\prod_{k\ne i}(\lambda_k-\lambda_i)$, which is the stated inverse and shows injectivity, hence bijectivity. Symmetric nodes and $\gamma$-evenness match up on both sides. Prescribing $2N$ real roots (and a leading coefficient) determines $P$, hence $\xi$.

**(ii).** By CvS Theorem 5.6(ii) the zeros of $\widehat\xi$ are the skeleton $2\pi m$, $|m|>N$, together with the $2N$ roots of $P$; realness of the latter is the gate. Writing the Hadamard product of the resulting even function of exponential type $\tfrac12$ gives the displayed form, with $u_i$ the free roots and $C$ the normalization; the parameter count is $N+1$, matching $\dim\{\text{even }\xi\}=N+1$.

**(iii).** Hypothesis (9) is immediate from (i)–(ii). For (8): $\prod_{n\le N}(1-z^2/\gamma_n^2)\to\prod_{n}(1-z^2/\gamma_n^2)=\Xi(z)/\Xi(0)$ by Hadamard (genus 1, $\sum\gamma_n^{-2}<\infty$), and the skeleton tail tends to $1$ locally uniformly by the displayed logarithmic bound.

**(iv).** $1\Leftrightarrow2$ is the definition of LP together with $\Xi$ real entire of order 1, genus 1: under RH the Hadamard product $\Xi(0)\prod(1-z^2/\gamma_n^2)$ is literally in LP normal form ($a=b=m=0$). $2\Leftrightarrow3$ is the Laguerre–Pólya theorem: LP is *exactly* the locally uniform closure of real-rooted real polynomials. $3\Rightarrow4$ trivially; $4\Rightarrow1$ by Hurwitz on each half-strip, using $\Xi\not\equiv0$ (e.g. $\xi_{\mathrm R}(2)=\pi/6\ne0$). $1\Rightarrow5$ is (iii); $5\Rightarrow4$ is immediate since the finite transforms are real-rooted real entire functions.

**(v),(vi).** Immediate from (i) and from the Riemann–von Mangoldt count against the skeleton-free window.

## Analytic domain audit

$\Xi$ is entire of order 1, genus 1, **maximal** type, with $\log|\Xi(iy)|=(|y|/2)\log|y|(1+o(1))$ by Stirling. Each $\widehat\xi$ is entire of exponential type $L/2$ ($=\tfrac12$ for $L=1$). All convergence statements are locally uniform; no contour or branch choice occurs. The Hadamard product for $\Xi$ converges absolutely because $\sum\gamma_n^{-2}<\infty$.

**A correction to an earlier statement of this session.** It was asserted (in `NOTATION.md` §1 and `L-16001`'s audit) that "a locally uniform limit of functions of exponential type $\le\tau$ has type $\le\tau$, so any sequence converging to $\Xi$ must have type $\to\infty$." **That is false.** Real polynomials have type $0$ and are dense — e.g. the Taylor sections of $e^{z^2}$, and even real-rooted ones since $(\sin(\varepsilon z)/\varepsilon)^n\to z^n$. Type is *not* lower semicontinuous under locally uniform convergence. Independently, hypothesis (8) only demands convergence on $S_{1/2}$, where $\Xi$ is bounded and type is invisible. The correct statement is a **conditioning** one: if $|F_\nu|\le C_\nu e^{\tau|z|}$ with $\tau$ **fixed** and $F_\nu\to f$ of maximal type, then $C_\nu\to\infty$. Observed: $\sum_j\xi_j$ runs $0.0136\to6182.8$ and the coordinate dynamic range $2.4\times10^{4}\to3.05\times10^{16}$ over $N=4..24$. That is a numerical-conditioning warning, **not** an obstruction.

## Dependency audit

- `L-15108` supplies Reading A ⇔ real-rootedness; used throughout.
- CvS Theorem 5.6(ii) supplies the skeleton; used in (ii).
- Hadamard factorization of $\xi$ and $\sum\gamma_n^{-2}<\infty$; used in (iii),(iv).
- Laguerre–Pólya theorem (LP = closure of real-rooted real polynomials); used in (iv). **Imported**, not reproved.
- Riemann–von Mangoldt; used only in (vi).

## Gap audit

1. **Reading B is not settled.** (8)+(9-strict) satisfiable $\Rightarrow$ RH is proved; whether RH $\Rightarrow$ (8)+(9-strict) satisfiable is **open**. If Reading B turned out unsatisfiable, Theorem 3.1 would be vacuously true and the programme dead — **but that would carry no implication about RH**, since the implication runs one way only. This asymmetry must not be misread.
2. (iii) uses the $\gamma_n$ as input. That is the whole point of (v), but it means the construction is not an algorithm for anything.
3. The Laguerre–Pólya theorem is imported. It is classical and standard, but it is the load-bearing import.
4. (ii)'s parameterisation is stated for the integer node set, where CvS Theorem 5.6(ii) applies. For general nodes there is no CvS transform statement (only Prop. 5.10's polynomial statement), so (ii) does not transfer.
5. Nothing here says anything about the truth of RH.

## Adversarial tests

Exact rational arithmetic; roots counted by exact Sturm sequences over $\mathbb Q$.

- **The bijection (i), stress-tested with deliberately wild data.** At $N=5$ (nodes $-5..5$) with prescribed roots $\{\pm1,\pm2,\pm13,\pm4321,\pm77777\}$: the Lagrange round-trip reproduced the prescribed $P$ **exactly**, the recovered $\xi$ was even, $\eta^{\mathsf T}\xi=1$ automatically (the prescribed $P$ being monic), and exact Sturm gave $10$ real roots of $10$, deficit $\mathbf 0$. Roots four orders of magnitude outside the node range are no obstacle — confirming that the gate constrains nothing.
- **The zero-matched target (iii).** Prescribing roots at $\pm\gamma_n/2\pi$: deficit $\mathbf 0$ at $N=4,6,8$ (degrees $8,12,16$), $\xi$ even and $\eta^{\mathsf T}\xi\neq0$ in every case. An independent run reports the same at $N=10,14,20,24$ with roots matching $\pm\gamma_n/(2\pi)$ to $10^{-98}$.
- **Direct contrast with `R-16001`:** at the very same levels the sampled-$\Xi$ target has deficit $4$. Two admissible targets, both converging to $\Xi$, opposite verdicts — which is exactly what (i) predicts and what makes the gate uninformative.

## Remaining uncertainty

(i) and (iv) are elementary/classical and independently verified; the author is confident. (ii)'s parameter count and (iii)'s convergence estimate were taken from an independent agent's derivation and re-checked only at the level of the exact Sturm census, not line by line. Reading B (gap audit 1) is the substantive unknown.

## Suggested next attack

1. **Test Reading B.** Take the zero-matched $\xi$ at $N=6$, build the arithmetic $Q_6$, and decide whether a scalar $c$ exists with $T(c)\succeq0$, $\ker T(c)=\mathbb R\xi$. An $11\times11$ exact-rational problem, and the single most informative experiment available — it tests the only part of the programme that could still be non-circular.
2. **First settle whether the arithmetic Weil matrix is even of CvS divided-difference form** in these coordinates (`OPEN_PROBLEMS` P-5). If it is not, `L-15107` does not apply to it and Reading B is ill-posed as stated.
3. Retire, throughout the repository, any argument that hopes to establish the cofinal gate by structural means alone.
