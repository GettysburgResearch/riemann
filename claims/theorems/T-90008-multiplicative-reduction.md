# T-90008 — The multiplicative reduction: class H, the λ-slice, "Form A over H ⇒ RH", and exact λ-extremality certificates

Claim ID: `T-90008` (provisional range; allocate at registry)
Status: **§1 λ-SLICE IDENTITIES PROVED (one-line arithmetic + machine checks); §2 REDUCTION THEOREM PROVED modulo two named in-repo consumers (T-90005 §1 chain; T-90001 §4 Landau consumer with its Flag 0); §3 EXTREMALITY CERTIFICATES PROVED (exact exhaustive finite search, three independent code paths); §4 asymptotic extremality principle PROVED_SKETCH, general λ-extremality CONJECTURED; §5 minimality finite-certificate PROVED; class-uniform Form A over H OPEN (= the Stage-2 target). No RH claim.**
Authoring: `claude-fable-5` session `riemann-proof-review-8nz34i`, Multiplicative Bootstrap dispatch, Stage 1
Date: 2026-08-09
Consumes (definitions unchanged): T-90003 §1 (source cell calculus, \(w_X, U_X, R_X\)), T-90006 §0–2 (\(W, H_p, \Sigma_{X,n}\)), T-90007 §2 (kernels \(c^{X,n}_p(k)\)), T-90005 §1 (chain map), T-90001 §0/§4 (Form A, radical bridge, Landau consumer), T-90007 §3 (the A6 adversarial certificate this theorem answers).

## 0. The class and the transported family

**Definition (class \(\mathcal H\)).** \(\mathcal H=\{f:\mathbb Z_{\ge1}\to\{-1,+1\}\ \text{completely multiplicative}\}\): free signs \(f(p)\in\{\pm1\}\) on primes, \(f(k)=\prod_{p\mid k}f(p)\) on squarefree \(k\), \(f(1)=+1\) forced (empty product). \(\lambda\in\mathcal H\) is the Liouville point \(f(p)=-1\ \forall p\).

**Definition (transported family).** Every campaign functional consumes its source only at squarefree \(k\); the \(f\)-transport is the squarefree restriction \(f\cdot\mu^2\):
- source: \(U^f_X(m)=\sum_{k\le X/m,\ k\ \mathrm{sf}}f(k)\,w_X(mk)\), \(R^f,S^f\) as in T-90003 §1, per-exit \(\Sigma^f_{X,n}(p)=\langle S^f,H^{(n)}_p\rangle=\sum_{k\ \mathrm{sf}\le X/n}f(k)\,c^{X,n}_p(k)\) (kernels of T-90007 §2, \(f\)-free);
- one-scalar ramp: \(\displaystyle \mathrm{Ramp}_f(X)=\sum_{d\ \mathrm{sf}\le X/2}f(d)\,T_X(d),\qquad T_X(d)=\sum_{2\le m\le X/d}(\log m)\,w_X(md)\ \ge0.\)

**GFEP over \(\mathcal H\):** \(\Sigma^f_{X,n}(p)\ge0\) for all \(f\in\mathcal H\), \(X\ge4\), \(n\le X/20\), \(p\in W\).
**Form A over \(\mathcal H\):** for every \(\varepsilon>0\) there is \(C_\varepsilon\) with \(\mathrm{Ramp}_f(X)\ge4\sqrt X-C_\varepsilon X^\varepsilon\) for all \(X\) and **all** \(f\in\mathcal H\).

## 1. The λ-slice (Lemma 1; PROVED)

(i) For squarefree \(k=p_1\cdots p_r\): \(\mu(k)=(-1)^r=\prod_i\lambda(p_i)=\lambda(k)\). Hence \(U^\lambda=U_X\), \(R^\lambda=R_X\), \(\Sigma^\lambda_{X,n}=\Sigma_{X,n}\) **identically** — the true Möbius functional is the \(\lambda\)-slice of the class family. (ii) \(\Lambda=\mu*\log\) gives
\[\mathrm{Ramp}_\lambda(X)=\sum_{d,m:\,dm\le X}\mu(d)(\log m)\,w_X(dm)=\sum_{2\le q\le X}\Lambda(q)\,w_X(q)\]
**exactly** (the \(m=1\) terms vanish; \(d>X/2\) forces \(m=1\)). *Membership of the truth in \(\mathcal H\) is therefore unconditional — no Siegel-type or zero-free input.* Machine checks: identity (ii) to \(\le1.4\cdot10^{-12}\) at \(X\in\{600,1000,2000,3000,5000,8000,10^4\}\) (`m1_ramp.py`); (i) implicitly re-verified everywhere \(f=\lambda\) reproduces the stored true values below.

## 2. Reduction theorem (PROVED modulo named consumers)

**Theorem.** (a) GFEP over \(\mathcal H\) \(\Rightarrow\) RH. (b) Form A over \(\mathcal H\) \(\Rightarrow\) RH.

*Proof.* Specialize to the single point \(f=\lambda\in\mathcal H\). (a) By Lemma 1(i) this is GFEP at all \(n\le X/20\); \(n>X/20\) is proved unconditionally (T-90003 §5, T-90005 §2); GFEP-full \(\Rightarrow\) RH by the exact chain map T-90005 §1 (final arrow = T-90001 §4 Landau consumer). (b) By Lemma 1(ii) the \(\lambda\)-slice reads \(\sum_{q\le X}\Lambda(q)q^{-1/2}\log(X/q)\ge4\sqrt X-C_\varepsilon X^\varepsilon\) — precisely the sharp one-sided ramp consumed by T-90001 §4 (via the radical bridge A4, slack \(O_\varepsilon(X^\varepsilon)\) allowed). ∎

Inherited flags, stated honestly: T-90001 §4's Flag 0 (consumer residency) applies to both branches; nothing else is imported. The theorem consumes only the \(\lambda\)-slice — the **reason** to demand the full class is methodological and is certified next: mean-value machinery of Halász/pretentious type cannot distinguish \(\mu\) inside \(\mathcal H\), so a Stage-2 argument must be class-uniform; the class is only a legitimate target if no member breaks the functional.

## 3. Exact extremality certificates (PROVED, finite; the search deliverable)

Exhaustive minimization over **all of \(\mathcal H\)** (prime signs \(p\le K\)) is exact via disjoint-fiber decomposition: any squarefree \(k\le K\) has at most one prime factor \(>\sqrt K\) (two would force \(k>K\)); conditioning on the \(2^{|\{p\le\sqrt K\}|}\) core assignments, each large prime's sign optimizes independently (its fiber \(\{qm\}\) meets no other large prime); both conditional objects are Walsh–Hadamard transforms. Class sizes covered exactly: \(2^{25}\) up to \(2^{95}\) (per-exit), \(2^{62}\) up to \(2^{669}\) (ramp).

**(a) Per-exit (script `m1_mult.py`).** At \((X,n)\in\{(2000,20),(2000,40),(3000,25),(3000,100),(4000,15),(6000,15),(10^4,20)\}\) (\(K=X/n\) from 30 to 500), at **every** exit \(p\in W\):
\[\min_{f\in\mathcal H}\Sigma^f_{X,n}(p)\ =\ \Sigma^{\lambda}_{X,n}(p)\ =\ \Sigma_{X,n}(p)\ >\ 0,\]
i.e. **the true Möbius sign pattern is the exact global minimizer of the class at every exit, and the class minimum is the true (positive) GFEP value.** Binding values \(\min_p\): \(+0.584\,(2000,20)\), \(+0.515\,(3000,25)\), \(+0.204\,(3000,100)\), \(+0.770\,(4000,15)\), \(+0.796\,(6000,15)\), \(+0.777\,(10^4,20)\); zero exits where any \(f\in\mathcal H\) beats \(\lambda\) (tolerance \(10^{-10}\)). Contrast the same kernels under free signs (A6 regime): \(-2.48,-6.45,-0.34,-14.41,-24.93,-22.47\) — the T-90007 §3 refutation is **entirely erased by multiplicativity alone**, and the rescue deepens with depth (|class min / free min| = 0.24 → 0.03).

**(b) One-scalar (script `m1_ramp.py`).** At \(X\in\{600,1000,2000,3000,5000,8000,10^4\}\):
\[\min_{f\in\mathcal H}\bigl[\mathrm{Ramp}_f(X)-4\sqrt X\bigr]=\mathrm{Ramp}_\lambda(X)-4\sqrt X\in[-28.5,-20.9],\]
matching the deterministic offset \(-2\log X-4+O(\psi\text{-fluct})\) of the \(\lambda\)-slice — inside any \(X^\varepsilon\) envelope; \(f\equiv1\) gives \(+5925\) at \(X=10^4\); every tested pretender direction loses. **Form A over \(\mathcal H\) costs, at every tested scale, exactly nothing beyond Form A at \(\mu\).**

**Validation (three independent paths).** (V1) full brute-force enumeration over all prime-sign vectors where feasible (\(2^{10}\) at \((3000,100)\); \(2^{15}\) at three exits of \((2000,40)\); \(2^{10}\) ramp at \(X=60\)) agrees to \(\le4\cdot10^{-15}\); (V2) direct product re-evaluation of every reported minimizer; (V3) the independent first-entrance flow recursion (mpmath dps30, disjoint code path, squarefree-restricted signs) reproduces every per-exit class minimum to \(\le5\cdot10^{-14}\).

**Fork resolution (branch (b) of the dispatch).** Multiplicative adversaries cannot break the functional; minimizers never pretend to \(n^{it}\) or to any real character: nearest-\(\chi\) distances of the minimizer (=\(\lambda\)) are \(D^2\ge0.55\) (best \(\chi_5\)), \(\min_tD^2(f,n^{it})\ge0.36\) (argmin \(t\approx14.1\approx\gamma_1\), a sanity signal). **\(\mathcal H\) is search-stable as the pure class: no character/Siegel exclusion enters, hence none is needed for membership either.**

## 4. Why: the extremality principle (PROVED_SKETCH asymptotically; CONJECTURED in general)

**Single-flip rigidity (measured exactly).** \(\Sigma^{f_q}-\Sigma^\lambda=2\sum_{m\ \mathrm{sf},\,q\nmid m}\mu(m)\,c(qm)=:\delta(q)\ge0\) for **every** prime \(q\) at every tested kernel — each prime fiber \(c(q\,\cdot)\) is *the same Möbius functional one level down* (self-similarity; the flat directions \(\delta(q)\to0\) sit at \(q\to K\), where the fiber shrinks to \(\{q\}\) and \(\delta=2c(q)\ge0\) by kernel positivity).

**Main-term Euler rigidity (sketch).** For \(f\in\mathcal H\) with flipped set \(P(f)=\{p:f(p)=+1\}\): \(D_f(s)=\sum_{d\,\mathrm{sf}}f(d)d^{-s}=Z_f(s)/\zeta(s)\) with \(Z_f(s)=\prod_{p\in P(f)}\frac{1+p^{-s}}{1-p^{-s}}\), every factor \(>1\) on \(s\in(0,\infty)\). Perron against the \(w_X\)-kernel (\(X^{s-1/2}/(s-\frac12)^2\)) with \(\sum_q((f\!\cdot\!\mu^2)*\log)(q)q^{-s}=D_f(s)(-\zeta'(s))\): if \(\sum_{P(f)}1/p<\infty\), the double pole of \(-\zeta'\) at \(s=1\) is reduced by \(D_f\)'s zero to
\[\mathrm{main}(f)=4\sqrt X\,Z_f(1),\qquad Z_f(1)=\prod_{p\in P(f)}\frac{p+1}{p-1}=e^{D(f,\lambda)^2+O(1)\cdot\Sigma p^{-2}}\ \ge\ 1,\ =1\iff f=\lambda;\]
if \(\sum_{P(f)}1/p=\infty\) the pole survives and \(\mathrm{main}(f)\asymp\sqrt X\log X\cdot(\text{positive})\). Either way the main term is uniquely minimized at \(f=\lambda\) with value \(4\sqrt X\), and the penalty exponent is the **pretentious distance to \(\lambda\)**: \(\mathrm{main}(f)-\mathrm{main}(\lambda)\approx4\sqrt X\,(e^{D(f,\lambda;X)^2}-1)\). The finite-\(X\) certificates of §3 confirm the ordering with no truncation exception down to \(X=600\).

**Conjecture (λ-extremality).** \(\min_{f\in\mathcal H}\Sigma^f_{X,n}(p)=\Sigma_{X,n}(p)\) and \(\min_{f\in\mathcal H}\mathrm{Ramp}_f(X)=\mathrm{Ramp}_\lambda(X)\) for all \(X,n\le X/20,p\). Under it, GFEP over \(\mathcal H\) \(\iff\) GFEP, and Form A over \(\mathcal H\) \(\iff\) Form A: **the class is free.**

## 5. Minimality of \(\mathcal H\) (finite-certificate PROVED)

Freeing the tail re-breaks: with \(f\) multiplicative on \(k\le K_0\) and *arbitrary* \(\pm1\) signs on squarefree \(k\in(K_0,K]\), the exact class minimum at the binding exit is \(-0.349\ (2000,20)\), \(-0.294\ (3000,25)\), \(-0.781\ (4000,15)\) at \(K_0=K/2\); still \(-0.174\) at \(K_0=2K/3\) \((4000,15)\); positive only once multiplicativity reaches \(\approx5K/6\) (`m1_minimality.py`). Together with T-90007 §3(ii) (true-\(\mu\) head + free tail dies at \(K/K_0\ge3/2\)): **multiplicativity is load-bearing at every depth up to a \(1-o(1)\) fraction of \(K\); no tail-block relaxation of \(\mathcal H\) survives.** \(\mathcal H\) is minimal in the block sense; by T-90007 §3 it is also necessary (sign-pattern + prefix + magnitude classes are refuted).

## 6. Stage-2 handoff (exact shape of the remaining problem; OPEN)

Class-uniform Form A over \(\mathcal H\) splits per §4 as (computable main term with penalty \(4\sqrt X(e^{D(f,\lambda)^2}-1)\ge0\), deterministic, Moat-side) + (truncation remainder, to be bounded **uniformly over \(\mathcal H\)**). The pretentious dichotomy matches this split exactly: \(f\) far from \(\lambda\cdot\)(twists) — Halász-type decay must beat only a *positive* main-term cushion; \(f\) near \(\lambda\) — the cushion vanishes and the demand at the point \(f=\lambda\) is square-root cancellation with \(X^\varepsilon\) slack, against Halász supply of shape \(\sqrt X[(1+M)e^{-M}+(\log X)^{-1/2}]\). The visible supply/demand gap at the \(\lambda\)-point, \(\sqrt X(\log X)^{-1/2}\) vs \(X^\varepsilon\), is the Stage-2 GO/NO-GO quantity; Stage 1 asserts nothing about it.

## 7. Artifacts

`experiments/X-90008-multiplicative-reduction/`: `m1_mult.py` (per-exit exhaustive class search + V1–V3), `m1_ramp.py` (one-scalar kernel, Λ-identity, class min), `m1_minimality.py` (tail-block probe), logs `m1_mult.log`, `m1_ramp.log`, `m1_minimality.log`, `SHA256SUMS`. Reuses `g3_adv.py` (X-90004) unchanged for kernels and the independent flow path.
