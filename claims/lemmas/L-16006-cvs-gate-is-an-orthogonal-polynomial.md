# L-16006 — The CvS finite gate is an orthogonal-polynomial extremal problem; its kernel polynomial detects the poles of the source

Claim ID: `L-16006`
Title: $t^{*}=\min\{\|P\|^{2}:P$ monic of degree $2N\}$, and $P_\xi$ is the monic orthogonal polynomial
Status: `PROPOSED` — parts (a)–(c) are short exact proofs; part (d) is measurement. Offered for checking, not as settled.
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `T-16001` (the CvS coordinate map is a linear bijection onto $\mathcal P_{2N}$); `L-16004` (Loewner closed form); CvS arXiv:2511.23257 Thm 5.6, Prop 4.1
Scope: finite special matrices at $2N+1$ distinct real nodes
Related counterexample candidates: none

---

## 0. What this is for

`O-16004` recorded, as a surprise, that the roots of the CvS kernel polynomial of the arithmetic Weil form land on the zeta zeros. This note gives what I believe is the mechanism, and the mechanism is elementary. If it is right, then the observation is a consequence of positivity rather than evidence for it, and several other features of the finite picture — the real-rootedness, the $1/N$ decay of the critical scalar, the roots sitting *outside* the node interval, the fact that only the lowest few zeros are resolved — all fall out of the same statement.

I want to be careful about the register. (a)–(c) below are two-line arguments and I have checked them numerically to working precision; I would still like someone to read them. (d) is a measurement with an explicit failure in it.

## 1. Setup

Nodes $\lambda_{-N}<\dots<\lambda_{N}$ distinct and real ($\lambda_j=j$ in the CvS/Weil setting), $\dim=2N+1$. Write

$$\Omega(s)=\prod_{k=-N}^{N}(\lambda_k-s),\qquad \ell(s)_j=\frac{1}{\lambda_j-s},\qquad P_x(s)=\sum_{j}x_j\prod_{k\neq j}(\lambda_k-s),$$

$\eta=(1,\dots,1)^{\mathsf T}$, and let $Q$ be a special matrix in the sense of CvS Prop 4.1. `T-16001` records that $x\mapsto P_x$ is a linear bijection $\mathbb R^{2N+1}\to\mathcal P_{2N}$.

## 2. Statement

**(a) [EXACT]** $\displaystyle P_x(s)=\Omega(s)\,\langle x,\ell(s)\rangle$, and the coefficient of $s^{2N}$ in $P_x$ is exactly $\eta^{\mathsf T}x$.

*Proof.* $\prod_{k\neq j}(\lambda_k-s)=\Omega(s)/(\lambda_j-s)$. For the leading coefficient, $\Omega$ has degree $2N+1$ with leading coefficient $(-1)^{2N+1}$, so $\Omega(s)/(\lambda_j-s)$ is monic of degree $2N$ for every $j$, and the coefficients add. $\square$

So **the CvS normalisation $\eta^{\mathsf T}x=1$ says precisely "$P_x$ is monic of degree $2N$."** That reading is worth having on its own; it is what makes (b) an extremal problem over a natural set.

**(b) [EXACT]** Let $Q\succ0$ and define the inner product $\langle P,R\rangle_Q:=\Phi^{-1}(P)^{\mathsf T}Q\,\Phi^{-1}(R)$ transported through the bijection $\Phi:x\mapsto P_x$. Then

$$t^{*}:=\frac{1}{\eta^{\mathsf T}Q^{-1}\eta}=\min\big\{\langle P,P\rangle_Q\;:\;P\ \text{monic},\ \deg P=2N\big\},$$

and the unique minimiser is $P_\xi$ with $\xi=Q^{-1}\eta/(\eta^{\mathsf T}Q^{-1}\eta)$ — the CvS kernel vector. Equivalently: **$P_\xi$ is the monic degree-$2N$ orthogonal polynomial of $\langle\cdot,\cdot\rangle_Q$.**

*Proof.* $\min\{x^{\mathsf T}Qx:\eta^{\mathsf T}x=1\}=1/(\eta^{\mathsf T}Q^{-1}\eta)$ with minimiser $Q^{-1}\eta/(\eta^{\mathsf T}Q^{-1}\eta)$ (Cauchy–Schwarz in the $Q$ metric). Transport by (a). Monic minus monic is lower degree, so the minimiser is characterised by orthogonality to $\mathcal P_{2N-1}$, which is the definition of the orthogonal polynomial. $\square$

**Corollary.** In the CvS pencil $Q-t\,\eta\eta^{\mathsf T}$, the critical scalar is the *orthogonal-polynomial norm* and the kernel vector is the *orthogonal polynomial*. Hence **CvS Theorem 5.6's conclusion — that the kernel polynomial is real-rooted — is, in this situation, the classical fact that orthogonal polynomials of a positive inner product on $\mathbb R$ have real simple roots.** I do not claim this reproves their theorem; I claim it is what the theorem is asserting once the coordinates are read this way, and that this is why confirming real-rootedness numerically was never going to be informative.

**(c) [EXACT, given `L-16004`]** If moreover $\psi(x)=\sum_{\mu\in M}\dfrac{a_\mu}{\mu-x}$ with $M\subset\mathbb R$ finite, $\mu\notin\{\lambda_j\}$, $a_\mu>0$, and $Q=\operatorname{Loewner}(\psi)$, then $Q=\sum_\mu a_\mu\,\ell(\mu)\ell(\mu)^{\mathsf T}$ and

$$\langle P,R\rangle_Q=\sum_{\mu\in M}\frac{a_\mu}{\Omega(\mu)^{2}}\,P(\mu)R(\mu)=\int PR\,d\nu,\qquad \boxed{\ \nu:=\sum_{\mu\in M}\frac{a_\mu}{\Omega(\mu)^{2}}\,\delta_\mu\ }$$

a **positive discrete measure supported on the poles of the source.** Consequently:

1. $P_\xi$ is the monic degree-$2N$ orthogonal polynomial of $\nu$; its $2N$ roots are the **$2N$-point Gauss quadrature nodes** of $\nu$. They are real, simple, and lie strictly inside $(\min M,\max M)$ — *not* inside the node interval. (This is why the roots observed in `O-16004` sit far outside $[-N,N]$, and why $P_\xi$ has constant sign at every node.)
2. If $\#M=2N$ exactly, then $\nu$ has $2N$ atoms, $\mathcal P_{2N-1}$ is all of $L^2(\nu)$, and $P_\xi=\prod_{\mu}(s-\mu)$ **exactly**, with $t^{*}=0$. The gate then recovers the poles of the source with no error at all.
3. The atom weights carry the factor $\Omega(\mu)^{-2}$. Since $|\Omega(\mu)|\sim|\mu|^{2N+1}$ for $|\mu|$ large, **the mass falls off like $|\mu|^{-2(2N+1)}$**: the measure is overwhelmingly concentrated on the lowest poles, and increasingly so as $N$ grows.
4. $t^{*}(N)$ is non-increasing in $N$ (the feasible set of monic polynomials grows richer relative to a fixed $\nu$ after rescaling), and vanishes once $2N\ge\#M$.

**(d) [MEASURED]** See §3–§4.

## 3. Evidence

All HIGH-PRECISION FLOAT (mpmath, dps 60–80). Code: `experiments/X-16003-source-atlas/{mech.py, mech2.py, arith_op.py, resolve.py}`.

**(a) identity.** Worst relative discrepancy between $P_x(s)$ and $\Omega(s)\langle x,\ell(s)\rangle$ over random integer $x$ and six random rational $s$, $N=5$, dps 60: $2.8\times10^{-61}$.

**(c1) synthetic pole recovery, exactly-determined regime ($\#M=2N$).** Source $\psi(x)=\sum_k a_k[(\mu_k-x)^{-1}+(-\mu_k-x)^{-1}]$, unit weights, nodes $-6..6$:

| pole set (positive half) | recovered positive roots | relative error |
|---|---|---|
| $11,19,27,35,43,51$ | $11,19,27,35,43,51$ | $6\times10^{-48}$ … $6\times10^{-35}$ |
| $14,21,35,49,77,91$ | $14,21,35,49,77,91$ | $3\times10^{-45}$ … $1\times10^{-31}$ |

These pole sets have nothing to do with zeta. The gate returns them to working precision. Independent check: the L-16004 assembly $\sum_\mu a_\mu\ell\ell^{\mathsf T}$ agrees with the Prop 4.1 divided-difference assembly to $5\times10^{-81}$ at dps 80.

**(c) orthogonality, over-determined regime.** Poles at the first 20 zeta ordinates (as a *synthetic* pole set, $\Delta=1$, unit weights), dps 80:

| $N$ | $t^{*}$ | $\xi^{\mathsf T}Q\xi$ vs $t^{*}$ | $\max_{k<2N}$ orthogonality residual | $\|P_\xi\|^2_\nu$ vs $t^{*}$ |
|---|---|---|---|---|
| 3 | $1.890027\times10^{-3}$ | $6.7\times10^{-68}$ | $2.0\times10^{-67}$ | $2.5\times10^{-67}$ |
| 4 | $6.590430\times10^{-4}$ | $5.6\times10^{-63}$ | $2.6\times10^{-63}$ | $6.7\times10^{-63}$ |
| 6 | $3.980868\times10^{-5}$ | $1.4\times10^{-55}$ | $2.1\times10^{-55}$ | $1.4\times10^{-54}$ |

Residuals at the level of the working precision, i.e. consistent with the identity being exact.

**(c3) the mass collapse.** Mass fractions of $\nu$ by pole index, same synthetic source:

| $N$ | $\mu_1$ | $\mu_2$ | $\mu_3$ | $\mu_4$ | $\mu_5$ | $\mu_6$ |
|---|---|---|---|---|---|---|
| 3 | 0.996 | $3.55\times10^{-3}$ | $3.06\times10^{-4}$ | $1.94\times10^{-5}$ | $6.37\times10^{-6}$ | $9.97\times10^{-7}$ |
| 6 | $1.000$ | $1.90\times10^{-5}$ | $1.83\times10^{-7}$ | $1.02\times10^{-9}$ | $1.26\times10^{-10}$ | $3.89\times10^{-12}$ |

and for the **arithmetic** $\Omega$ at cutoff 2000: at $N=6$ the fractions are $1,\;2.3\times10^{-5},\;2.3\times10^{-7},\;1.3\times10^{-9},\dots$; at $N=10$ they are $1,\;1.0\times10^{-8},\;4.7\times10^{-12},\;9.3\times10^{-16},\dots$. This is the quantitative form of "only the lowest zeros are resolved", and it says the situation gets *worse* with $N$, not better, in the sense that the higher poles are weighted ever more faintly.

## 4. The part that failed — but read §4a first, because I got part of it wrong

> **ERRATUM, same day, and it is substantial.** The orthogonality residuals in the table below are computed as $\max_k$ over $k=0,\dots,2N-1$. **The odd $k$ are vacuous**: the source is odd, so the atoms come in $\pm\mu$ pairs and $P_\xi$ is even, and every term of $\sum_\mu w_\mu P_\xi(\mu)\mu^{k}$ cancels identically against its partner for odd $k$. My normalisation divides by $\sum_\mu|w_\mu P_\xi(\mu)\mu^k|$, so on the odd $k$ I computed $0/0$ and reported floating-point noise as a defect. The maxima quoted below (0.83, 0.47, 0.35, 0.36) are those noise values.
>
> Redone over **even $k$ only**: 0.62 (cutoff 2000, $N=4$), 0.36 ($N=6$), 0.44 ($N=8$), 0.83 (cutoff 500, $N=6$). **So the conclusion of §4 survives** — the residual against the *unit-residue* $\nu_\zeta$ really is order one — but it survives for a weaker reason than I claimed, and the specific numbers below should not be quoted. §4a replaces this section's diagnosis with a sharper one.

## 4a. Redone twice — and the second redo removes the arithmetic content entirely

> **ERRATUM 2 (from the PR #173 second-pass review, verified here).** §4a below reported the Hankel property of the transported Gram matrix as *evidence* that the arithmetic form has a representing measure. **It is not evidence of anything arithmetic: the identity is universal for Loewner matrices.**
>
> The reviewer's proof: with barycentric weights $w_i=1/\prod_{k\ne i}(\lambda_i-\lambda_k)$ one has $\sum_i w_i\lambda_i^{r}=0$ for $r<n$, and the divided-difference identity then gives $H_{a+1,b}-H_{a,b+1}=0$ identically. Equivalently, via $\psi[x,y]=\frac1{2\pi i}\oint\frac{\psi(t)\,dt}{(t-x)(t-y)}$ and $\sum_i w_i\lambda_i^{a}/(t-\lambda_i)=t^{a}/\tilde\Omega(t)$ for $a\le n$, $M_{ab}=\frac1{2\pi i}\oint\psi(t)t^{a+b}\tilde\Omega(t)^{-2}dt$ — manifestly a function of $a+b$ alone.
>
> Verified across ten sources at dps 80 — $x$, $x^2$, $x^3$, $x^5-2x$, $\sin x$, $\arctan(x/20)$, $x/(1+x^2)$, $1/(x-30.5)$, $\log(x+40)$, $e^{x/9}$ — odd, even and neither, polynomial, oscillatory, Pick, rational and transcendental. **Every one has Hankel defect $\sim10^{-81}$.** So the $10^{-105}$–$10^{-198}$ figures below are roundoff around a universal identity, exactly as the reviewer says.
>
> **And I initially disputed this, wrongly, by the same $0/0$ mistake for the fourth time.** My first re-test normalised each comparison by $\max(|H_{a+1,b}|,|H_{a,b+1}|)$; for a symmetric source both are *structurally* zero on half the entries, so it returned $O(1)$ noise and appeared to give counterexamples ($x^3$, $\sin$, $\arctan$ all "failing"). Normalising by the global matrix scale, they all pass. The recurring failure mode — reading a structurally-zero quantity as a measurement — is now four for four in this session and is recorded as such in `O-16008`§5.
>
> **A second correction, where I could not confirm the reviewer either.** The review states that the extracted Gauss rule represents the *critical pencil*, $Q-t^{*}\eta\eta^{\mathsf T}=\sum_kA_k\ell(r_k)\ell(r_k)^{\mathsf T}$. Checked entrywise at $(c,N)=(2000,4),(2000,6),(20000,6)$: relative error **0.74, 0.84, 0.86** — it does not hold as written. Nor does it reconstruct $Q$ (relative error 1.0). The closest true statement I could find is $R\approx Q-\kappa\eta\eta^{\mathsf T}$ — $Q-R$ is constant to within 3–7% of its scale — with $\kappa/t^{*}=3.80,\,6.15,\,6.98$, growing roughly like $N$. **So the precise relation between the extracted rule and $Q$ is unresolved** and I adopt neither story. What the review is unambiguously right about is the negative part: the extracted rule is **one** representing object, not "the measure $Q$ carries", and §4a's framing overstated it.
>
> **What survives.** The residue match $A_k\approx a_c(\gamma_k)$ is the one substantive observation, and it is now *explained* rather than measured — see `T-16002`§1.

## 4a. [superseded framing retained below] Redone: the form has a representing measure; it is the *residues* that are wrong

Applying the same even/odd discipline to a stronger test changes the picture, and in the programme's favour.

$\Phi$ inverts in closed form: from $P_x(s)=\Omega(s)\langle x,\ell(s)\rangle$ and $\Omega(\lambda_j)=0$ one gets $x_j=P(\lambda_j)\,w_j$ with $w_j=1/\prod_{k\ne j}(\lambda_k-\lambda_j)$. Hence with $\tilde Q_{ij}=w_iQ_{ij}w_j$,

$$\langle P,R\rangle_Q=\sum_{i,j}P(\lambda_i)\,\tilde Q_{ij}\,R(\lambda_j),\qquad M_{ab}:=\langle s^a,s^b\rangle_Q .$$

The form is a **moment functional** — equivalently it has a representing measure on $\mathbb R$ — exactly when $M_{ab}$ depends only on $a+b$, i.e. when $M$ is Hankel. This is *not* automatic for a positive definite form. Measured, on the even antidiagonals (the odd ones vanish identically, as above):

| cutoff | $N$ | dps | worst **even**-antidiagonal relative Hankel defect | odd-antidiagonal scale vs even |
|---|---|---|---|---|
| 2000 | 4 | 120 | $6.6\times10^{-105}$ | $1.5\times10^{-123}$ vs $8.6\times10^{-6}$ |
| 2000 | 6 | 160 | $1.1\times10^{-141}$ | $5.6\times10^{-163}$ vs $1.1\times10^{-5}$ |
| 2000 | 8 | 220 | $9.8\times10^{-198}$ | $1.1\times10^{-219}$ vs $1.8\times10^{-5}$ |
| 500 | 6 | 160 | $1.9\times10^{-142}$ | — |

**The defect tracks the working precision across three settings of dps**, which is the signature of an exact identity. So the arithmetic Weil form's induced inner product **is** a moment functional, and since $Q_W\succ0$ the functional is positive definite and Hamburger gives a representing positive measure on $\mathbb R$, symmetric about $0$. That is the object §5(1)'s "suggested next attack" asked for, and it exists.

This also looks like a **general** property of Loewner matrices rather than an arithmetic accident: the same test on synthetic pole-sum sources returns even-antidiagonal defects of $10^{-150}$, and for $\psi(x)=x^3$ one can check by hand that the three surviving contributions all land on the antidiagonal $a+b=4N-2$ with equal values. I state that as a conjecture, not a result: **for any source $\psi$, $\langle P,R\rangle_{\operatorname{Loewner}(\psi)}$ depends only on the product $PR$.** If true it explains *why* orthogonal polynomials appear at all in (b) — the CvS gate is a moment problem — and it would make CvS Theorem 5.6 read "a positive-definite moment functional has a representing measure on $\mathbb R$, so its orthogonal polynomials are real-rooted".

**Where the measure puts its mass.** Extracting the form's own $2N$-point Gauss rule (nodes = roots of $P_\xi$, weights = Christoffel numbers from $\sum_iW_ir_i^k=\mu_k$), cutoff 2000, $N=8$, dps 220:

| $w=2\pi r/L$ | rel. err vs nearest $\gamma$ | Christoffel $W_i$ | implied residue $a_i=W_i\Omega(r_i)^2$ |
|---|---|---|---|
| 14.1347251417 | $2.9\times10^{-15}$ | $3.93\times10^{-43}$ | **0.072233228** |
| 21.0220398103 | $8.2\times10^{-9}$ | $2.33\times10^{-48}$ | 0.73431165 |
| 25.0111337074 | $1.1\times10^{-5}$ | $2.84\times10^{-51}$ | 0.40011649 |
| 30.6381529707 | $7.0\times10^{-3}$ | $1.96\times10^{-54}$ | 0.31958202 |
| 36.8182225511 | $2.0\times10^{-2}$ | $1.01\times10^{-56}$ | 0.93212564 |
| 43.4765270376 | $3.4\times10^{-3}$ | $6.51\times10^{-59}$ | 1.8245615 |
| 67.7720189732 | 0.56 | $4.38\times10^{-65}$ | 4.81 |
| 132.000887936 | 2.05 | $3.76\times10^{-74}$ | 30.2 |

**Every Christoffel weight is positive**, at every $(c,N)$ tried — consistent with a genuine positive measure. The nodes are the zeta zeros, sharply for the low ones and degrading exactly where §1's resolution law says they should.

**And here is the sharp form of §4's failure.** If the pure pole model $\psi_W\approx\sum_\rho(s-\rho)^{-1}$ held, the implied residue would be $a_i=1$ at every recovered zero. It is not. Moreover $a_1$ is remarkably **stable in $N$** and **not stable in $c$**:

| cutoff | $a_1$ at $N=4$ | $N=6$ | $N=8$ |
|---|---|---|---|
| 2000 | 0.072265122 | 0.07223323 | 0.072233228 |
| 500 | — | 0.0023715094 | — |

Six significant figures of agreement across $N$ at fixed cutoff, and a factor of 30 change between cutoffs. So the finite Weil form assigns each zero a well-defined effective residue, that residue is a **function of the cutoff alone**, and at $c=2000$ it is about $1/14$ rather than $1$. That is a much more informative statement than "the pole model fails", and it is what a corrected §4 should say.

I expected the arithmetic Weil form to be well modelled by the pure pole sum $\sum_\rho 1/(s-\rho)$, i.e. that its induced inner product would be close to $L^2(\nu_\zeta)$ with $\nu_\zeta$ the zeta-zero measure of (c). **It is not.** Using X-0001's $Q_W$ and the exact kernel vector, dps 60:

| cutoff | $N$ | $t^{*}$ | $\xi^{\mathsf T}Q_W\xi$ vs $t^{*}$ | $\|P_\xi\|^{2}_{\nu_\zeta}$ | orthogonality residual vs $\nu_\zeta$ | best of 400 random monic competitors |
|---|---|---|---|---|---|---|
| 500 | 6 | $2.420477\times10^{-3}$ | $1.6\times10^{-36}$ | $7.96\times10^{-4}$ | **0.83** | $1.154\times10^{-2}$ |
| 2000 | 6 | $2.054256\times10^{-3}$ | $1.4\times10^{-34}$ | $4.76\times10^{-4}$ | **0.47** | $1.132\times10^{-2}$ |
| 2000 | 8 | $1.529400\times10^{-3}$ | $2.4\times10^{-26}$ | $3.26\times10^{-4}$ | **0.35** | $1.123\times10^{-2}$ |
| 2000 | 10 | $1.203284\times10^{-3}$ | $1.9\times10^{-19}$ | $1.85\times10^{-4}$ | **0.36** | $9.552\times10^{-3}$ |

The variational identity (b) holds to working precision, and the minimality is visible (every random monic competitor is 5–9 times worse). But the orthogonality residual against $\nu_\zeta$ is **order one**, and $\|P_\xi\|^2_{\nu_\zeta}$ is off from $t^{*}$ by a factor of about 3–6.

So $\psi_W$ is *not* a pole sum over the zeta zeros in any quantitative sense — which one should have expected, since $\psi_W(x)=\frac1\pi\int_0^L\sin(2\pi x(1-y/L))D(y)\,dy$ is **entire in $x$** and has no poles at all. What it has is a smoothed, finite-cutoff imitation of that pole structure, and the smoothing is not a small perturbation of the measure.

**The honest conclusion is therefore split in two.** (b) is representation-free and applies to $Q_W$ exactly: the arithmetic kernel polynomial *is* the monic orthogonal polynomial of the Weil form's own inner product, and $t^{*}$ *is* its norm. (c) is a model, it explains the *qualitative* pole-detection cleanly and the synthetic case exactly, and it is **quantitatively wrong** for $\psi_W$. Anyone tempted to substitute $\psi_W\approx\sum_\rho 1/(s-\rho)$ and reason from there should not, on this evidence.

## 5. What follows for the programme

1. **`O-16004`§2 is explained, and downgraded accordingly.** The gate is a pole/spectral detector for whatever source it is fed. Feeding it the Weil source returns the zeta zeros because the Weil source imitates $\sum_\rho(s-\rho)^{-1}$; that is the explicit formula, and the ten-digit agreement is a very good regression test and nothing more. It is not independent evidence about zeta.
2. **Real-rootedness was never going to be informative.** By (b) it is the orthogonal-polynomial fact, conditional only on $Q\succ0$. This sharpens `O-16004`§4 and the e2 finding into something provable: given positivity, the rest of the CvS conclusion is automatic. The entire arithmetic content of Reading B sits in $Q_W\succeq0$, i.e. in finite Weil positivity.
3. **The $1/N$ decay of $t^{*}$ is not a defect.** By (b), $t^{*}(N)=\min\{x^{\mathsf T}Q_Wx:\sum_jx_j=1\}$ is the minimum of the truncated Weil functional over normalised test vectors. Its decay to $0$ is the statement that **Weil positivity is sharp** — exactly what one expects — rather than a sign that the pencil parameter is being squeezed out. (The e2 report reads the decay as a loss of freedom; on this reading it is instead a measurement of how close to degenerate the Weil functional is at level $N$, which is a quantity worth tabulating in its own right.)
4. **A cheap one-sided diagnostic.** $t^{*}<0$ implies $\eta^{\mathsf T}Q^{-1}\eta<0$, which is impossible for $Q\succeq0$ invertible. So **$t^{*}<0\Rightarrow Q\not\succeq0$**, detected by one linear solve rather than a congruence — much cheaper on these ill-conditioned matrices, though it inherits the same precision requirement.

> **Correction 2 (PR #173 review, verified).** I then wrote "$t^{*}<0\Rightarrow Q$ is **indefinite**". Also wrong, and weaker than stated: $t^{*}<0$ gives only "**not PSD**". Elementary counterexample $Q=-I_n$, for which $\eta^{\mathsf T}Q^{-1}\eta=-n$ and $t^{*}=-1/n<0$ while $Q$ is **negative definite**, not indefinite. Verified at $n=3,5,9$. Corrected above.
>
> **Correction 1, earlier the same day.** I first wrote that $t^{*}<0$ is *equivalent* to a positivity violation. **That is false**, and I have a counterexample from my own run. The implication holds in one direction only: $t^{*}>0$ does **not** imply $Q\succeq0$, because when $Q$ is indefinite the quantity $1/(\eta^{\mathsf T}Q^{-1}\eta)$ is a *saddle* value of $x^{\mathsf T}Qx$ on $\{\eta^{\mathsf T}x=1\}$, not a minimum — the constrained infimum is then $-\infty$. Measured instances (from the sign scan of `O-16005`, cutoff 200, $N=6$): the pattern $(-1,-1,-1)$ has inertia $(12,1,0)$ with $t^{*}=+3.4387\times10^{-3}$, and $(1,1,-1)$ has inertia $(11,2,0)$ with $t^{*}=+6.5800\times10^{-3}$. Both are indefinite with a **positive** $t^{*}$. The variational statement in (b) is fine as written — it assumes $Q\succ0$ — but the screen derived from it is one-sided and must be used as such.

## 6. Feasibility of the one-scalar gate, exactly

Everything above assumed $Q\succ0$. The prior question — *for which $Q$ does a usable scalar exist at all?* — has a clean answer, and it is sharper than the "$n_-$ changes by at most one" bound recorded in `O-16004`§4.

Since $\operatorname{Loewner}(\lambda)=J=\eta\eta^{\mathsf T}$ (off-diagonal $(i-j)/(i-j)=1$, diagonal $\lambda'\equiv1$), the one-scalar family is $Q-cJ$, and $J$ acts trivially on $\eta^{\perp}$.

**(e) [EXACT]**
- *Necessary.* If $Q-c\eta\eta^{\mathsf T}\succeq0$ for some real $c$, then $Q|_{\eta^{\perp}}\succeq0$. (For $x\perp\eta$, $x^{\mathsf T}(Q-c\eta\eta^{\mathsf T})x=x^{\mathsf T}Qx$.)
- *Sufficient.* If $Q|_{\eta^{\perp}}\succ0$ strictly, such a $c$ exists; the extremal one is unique and the kernel there is one-dimensional.

So **the one scalar buys exactly one direction, and only a direction that $\eta$ can see.** $Q$ itself may have a negative eigenvalue and the gate still passes — but only that one, and only if its eigenvector is not $\eta$-orthogonal.

**Corollary (parity).** $\eta$ is even and the parity involution is $e_j\mapsto e_{-j}$, so **the entire odd sector lies inside $\eta^{\perp}$.** Hence:

$$\text{Reading B feasible}\ \Longrightarrow\ Q_W|_{\text{odd}}\succeq0\ \text{ outright.}$$

No choice of the scalar can repair a single negative direction in the odd sector. That is a genuine necessary condition on the arithmetic form which the CvS apparatus cannot supply, and it is the sharp form of the observation (made independently in a parallel report) that the pencil "cannot touch the odd sector".

**Evidence.** EXACT rational congruence throughout (`experiments/X-16003-source-atlas/feas.py`).

- *Necessity*, 300 random rational symmetric matrices, $n=5,6,7$, minimising $n_-(Q-cJ)$ over a 13-point grid in $c$ spanning $\pm10^{6}$: **0 violations**.
- *Sufficiency*: the random test was **vacuous** — not one of the 300 had $Q|_{\eta^{\perp}}$ strictly positive definite, so it tested nothing, and I record that rather than quoting "0 violations" as if it were evidence. Redone on 30 designed instances $Q=M-s\eta\eta^{\mathsf T}$ with $M=G^{\mathsf T}G+I\succ0$ and $s\in\{0,1,10,100,10^{4}\}$, which satisfy the hypothesis by construction: in every case $\min_c n_-(Q-cJ)=0$, **including the 22 instances where $Q$ itself had inertia $(n-1,1,0)$.** So the pencil does repair the single negative eigenvalue exactly when the theory says it should.
- *The gate is strictly stronger than "$t^{*}>0$"*, confirmed on X-0001 at cutoff 200, $N=6$ (dps 60):

| block signs | inertia $Q$ | $t^{*}$ | inertia $Q-t^{*}J$ | PSD with 1-dim kernel? |
|---|---|---|---|---|
| $(+,-,-)$ | $(13,0,0)$ | $+2.8510\times10^{-3}$ | $(12,0,1)$ | **yes** |
| $(-,-,-)$ | $(12,1,0)$ | $+3.4387\times10^{-3}$ | $(11,1,1)$ | no |
| $(+,+,-)$ | $(11,2,0)$ | $+6.5800\times10^{-3}$ | $(10,2,1)$ | no |

The two indefinite rows have **positive** $t^{*}$ and are nevertheless correctly rejected by the actual gate test, which is the behaviour the correction in §5(4) predicts.

## 7. Two pencils, which must not be conflated

Flagged in review and I agree. The **self-nominated** pencil studied throughout this claim is $Q-t\,\eta\eta^{\mathsf T}$, where the target $\xi=Q^{-1}\eta/(\eta^{\mathsf T}Q^{-1}\eta)$ is produced *by* the form. The **Reading-B** pencil of the working note is $T_p(c)=A_p+cB_p$ with a *prescribed* target $p$ — a different object with a different question attached. Results about one do not transfer to the other, and `O-16004`§4's discussion of "Reading B" should be read with that distinction in mind.

## Gap audit

1. (a)–(c) are short arguments I wrote and checked numerically; they have not been reviewed. The one place I would look hardest is the claim in (c) that $\{\ell(\mu)\}_{\mu\in M}$ is linearly independent when $\#M\le 2N+1$ — I used it implicitly in (c2) and verified it only through the numerical rank, not by the Cauchy-matrix argument.
2. (b) requires $Q\succ0$ for the minimum to be attained and positive. For $Q$ merely PSD with a kernel the statement degenerates to $t^{*}=0$; I did not work through the boundary case carefully.
3. All numbers are HIGH-PRECISION FLOAT. Nothing here is certified. The X-0001 rows inherit that experiment's own uncertified archimedean truncation.
4. §4's failure is measured against **one** candidate measure, $\nu_\zeta$ with unit weights at $\mu=\gamma\Delta$. A different normalisation of the source, or a smoothing kernel applied to the atoms, might do much better. I did not search for one; "the pole model is quantitatively wrong" should be read as "this pole model is", not as "no pole model is".
5. The claim in §5(1) that the ten-digit agreement is "nothing more" than a regression test is a judgement, not a theorem. Someone who believes the finite gate extracts more than the explicit formula already gives should say what more, concretely.
6. §6's sufficiency direction needs $Q|_{\eta^{\perp}}$ **strictly** positive definite; the PSD-but-singular boundary case is not settled here, and I expect it to fail in general (a kernel vector of $Q|_{\eta^{\perp}}$ that is not $Q$-orthogonal to $\eta$ should break it). I did not construct that counterexample.
7. §6's evidence uses a finite grid in $c$ (13 points, $\pm10^{8}$). A feasible $c$ outside the grid or between grid points would be missed, so "min over the grid" is an upper bound on feasibility, not a decision procedure. The designed-instance rows are unaffected, since there feasibility was confirmed positively.

## Suggested next attack

1. Prove or refute (c) for a genuine measure attached to $\psi_W$: find the positive measure $\nu_W$ with $\langle P,R\rangle_{Q_W}=\int PR\,d\nu_W$, if one exists. Since $Q_W\succ0$ it exists as a *bilinear form*; the question is whether it is a measure on $\mathbb R$ of Herglotz type, and if so where its support is. That support is the honest answer to "what does the finite Weil form think the zeros are".
2. Because $t^{*}$ is a minimum of the Weil functional, tabulate $t^{*}(N,c)$ as a **sharpness measure for Weil positivity** and compare it against the known extremal-test-function literature. If someone has an asymptotic for the minimum of the Weil functional over degree-$2N$ normalised test vectors, it predicts $t^{*}$ and that is a real check on the whole pipeline.
3. The $\Omega(\mu)^{-2}$ weighting suggests changing the nodes. Nodes $\lambda_j=j$ put the Gauss weight where it decays like $\mu^{-2(2N+1)}$; nodes spread over the range of interest would flatten $\nu$ and could resolve many more zeros at the same $N$. Whether CvS Thm 5.6 survives non-integer nodes is the prerequisite question.
