# O-16001 — The Connes–van Suijlekom finite coordinates are Fourier *coefficients*; the finite target is the sampled Ξ

Claim ID: `O-16001`
Title: Identification of the finite CvS target vector as $\xi_j=(-1)^{j}\,\Xi(2\pi\alpha j)$, and a documented trap
Status: `PROPOSED`
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: Connes–van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action*, arXiv:2511.23257 v1, Lemmas 5.1/5.7, **Proposition 5.5 eq. (19)**, Theorem 5.6, Prop. 5.10 (all quoted); `L-16001` (identification $K=\Phi/4$); Poisson summation / Whittaker–Shannon sampling
Scope: the interface between the repository's continuum targets (`L-15101`, `T-15102`) and the finite CvS matrix theorem
Related counterexample candidates: none directly; supplies the object censused in `R-16001`

---

## Statement

**(a) The coordinates.** In Connes–van Suijlekom (CvS) the finite vector $\xi=(\xi_j)_{j=-N}^{N}$ is the vector of **Fourier coefficients** of an element of $L^{2}[0,L]$ in the eigenbasis $U_n(x)=L^{-1/2}e^{2\pi inx/L}$ of the circle Dirac operator, **not** a vector of point samples of a function. The boundary vector is verbatim $\eta=\sum_j e_j$, the all-ones vector in that eigenbasis (CvS Lemma 5.1(ii), Lemma 5.7(ii)). The parity involution is $\gamma(e_j)=e_{-j}$, i.e. on functions the symmetry $x\mapsto L-x$ of $[0,L]$.

**(b) The finite transform.** CvS Theorem 5.6(ii) attaches to $\xi$ the function $\xi(x)=\sum_k\xi_ke^{2\pi ikx}$ on $[0,1]$, **extended by zero off $[0,1]$**, and its Fourier transform

$$\widehat\xi(z)=2\,e^{-iz/2}\sin(z/2)\sum_{j=-N}^{N}\frac{\xi_j}{z-2\pi j}. \tag{O-16001.1}$$

This is a **truncated Whittaker–Shannon cardinal series**, and it satisfies the interpolation property $\widehat\xi(2\pi j)=\xi_j$. It is **not** the exponential sum $\sum_j\xi_je^{ijz}$.

**(c) The target.** Let $\Phi=4K$ be the Riemann–Pólya function of `L-16001`, $\Xi(w)=\int_{\mathbb R}\Phi(t)e^{iwt}dt$. Fix a scale $\alpha>0$, put $G(x)=\alpha^{-1}\Phi(x/\alpha)$ for $|x|\le\tfrac12$ and $G=0$ outside, and let $F(z)=\int_{-1/2}^{1/2}G(x)e^{izx}dx$. Then $F$ is real and even, $F(z)\approx\Xi(\alpha z)$ with error controlled by $\int_{|t|>1/(2\alpha)}\Phi$, and after transporting the window $[-\tfrac12,\tfrac12]$ to $[0,1]$ the CvS coefficients are

$$\boxed{\;\xi_j=(-1)^{j}\,F(2\pi j)\;\approx\;(-1)^{j}\,\Xi(2\pi\alpha j)\;} \tag{O-16001.2}$$

so that **the finite CvS target is, up to the centering sign $(-1)^{j}$, the vector of samples of $\Xi$ itself on an arithmetic progression.** It is automatically even ($\xi_{-j}=\xi_j$), as CvS requires.

**(d) Sign pattern.** Consequently $\xi$ is **strongly mixed in sign**: it alternates at every step where $\Xi$ does not change sign, and fails to alternate exactly where $\Xi$ changes sign between consecutive samples. In particular $n_-\approx n/2$, never $0$.

**(e) The trap (recorded deliberately).** Pólya's $\Phi>0$ is positivity of **values**. It does **not** make the CvS coordinates positive. The inference

> "$\Phi>0$, so the finite target $p$ is strictly positive, so by `L-16002` the Finsler isotropic cone is empty and the working note's remaining cofinal task is vacuous"

is **FALSE**, and is refuted precisely by (a)–(d). It was actually made and pursued during this session before the primary source was read, and is recorded here so that no later agent repeats it.

---

## Definitions

- $\Xi(w)=\xi_{\mathrm R}(\tfrac12+iw)$ with $\xi_{\mathrm R}(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$.
- $\alpha>0$: the *scale*. The sample spacing in the $\Xi$ variable $w$ is $2\pi\alpha$; the effective window in $t=\log u$ is $|t|\le 1/(2\alpha)$.
- $N$: the *level*; the finite space has dimension $2N+1$ and $\deg P=2N$.
- $P(s)=\sum_{j=-N}^{N}\xi_j\prod_{k\neq j}(k-s)=\Omega(s)\sum_j\frac{\xi_j}{j-s}$, $\Omega(s)=\prod_j(j-s)$ — the CvS interpolation polynomial of Theorem 5.6(i).

## Motivation

The repository's positive route describes its targets as localized *functions* ($p_\lambda(u)=\chi(\log u)k(u)$ in `L-15101`), while the finite theorem consumes *coefficient vectors*. Nothing in PR #158 or in the working note states which of the two the symbol $p$ denotes, and the note's phrase "target-pinned" is neutral between them. That ambiguity is not cosmetic: the two readings differ by a discrete Fourier transform and have **opposite sign structure**, and one of them makes the entire criterion vacuous.

Fixing the interface does three things at once:

1. it closes the trap in (e);
2. it makes the finite target **directly computable from $\Xi$**, with no Weil matrix, no prolate operator, and no radical machinery — an enormous practical simplification, since $\Xi$ can be evaluated to arbitrary precision by standard means;
3. it exhibits the finite condition as a statement about the **sampled zero structure of $\Xi$**, which is what `L-16003` and `R-16001` then exploit.

## Derivation

CvS Theorem 5.6(ii) forms $\xi(x)=\sum_k\xi_ke^{2\pi ikx}$ on $[0,1]$ and zero outside, so $\xi_j$ is by definition the $j$-th Fourier coefficient of $\xi(\cdot)$ on $[0,1]$; equivalently $\xi_j=\widehat\xi(2\pi j)$ where $\widehat\xi(z)=\int_0^1\xi(x)e^{-izx}dx$. That is (a) and the interpolation property in (b). Formula (O-16001.1) is CvS's own, obtained from $\int_0^1e^{2\pi ikx}e^{-isx}dx=2e^{-is/2}\sin(s/2)/(s-2\pi k)$.

For $\widehat\xi$ to approximate the even real function $\Xi$ one needs $\xi(\cdot)$ symmetric about $x=\tfrac12$, which is exactly CvS's parity $\gamma$. Writing $G(x)=\xi(x+\tfrac12)$ on $[-\tfrac12,\tfrac12]$ and $F(z)=e^{iz/2}\widehat\xi(z)=\int_{-1/2}^{1/2}G(x)e^{izx}dx$, the coefficients of $G$ over $[-\tfrac12,\tfrac12]$ are $F(2\pi j)$, and the translation by $\tfrac12$ multiplies the $j$-th coefficient by $e^{-i\pi j}=(-1)^{j}$. This gives (O-16001.2).

**This centering dictionary is not merely a reconstruction — it is stated in the primary source.** Connes–van Suijlekom **Proposition 5.5, equation (19)** reads, verbatim: *let $f\in L^{2}([0,L])$ and $f_\sigma(x):=f(x+\tfrac L2)$ for $|x|\le\tfrac L2$, extended by $0$ on $\mathbb R$; then the restriction of the Fourier transform of $f_\sigma$ to $\tfrac{2\pi}{L}\mathbb Z$ is given by the Fourier transform $\widehat f$ of $f\in L^{2}(\mathbb R/L\mathbb Z)$ as*

$$\mathcal F(f_\sigma)\!\left(\frac{2\pi}{L}n\right)=(-1)^{n}\,\widehat f(n).$$

That is exactly (O-16001.2) with $\widehat f(n)=\xi_n$: the $(-1)^{n}$ is CvS's own factor, and the identification of the coordinates as Fourier coefficients sampled against the transform is theirs, not this agent's. Statement (a) is therefore `QUOTED`, not `DERIVED`.

Finally, taking $G(x)=\alpha^{-1}\Phi(x/\alpha)\big|_{|x|\le1/2}$ gives $F(z)=\int_{|t|\le1/(2\alpha)}\Phi(t)e^{i\alpha zt}dt$, so

$$F(z)-\Xi(\alpha z)=-\int_{|t|>1/(2\alpha)}\Phi(t)e^{i\alpha zt}\,dt,\qquad |F(z)-\Xi(\alpha z)|\le 2\int_{1/(2\alpha)}^{\infty}\Phi \ \ (z\in\mathbb R),$$

and the tail is **doubly exponentially small** because $\Phi(t)\asymp e^{-\pi e^{2t}}$ (`L-16001`(e)). Substituting $\alpha^{-1}\Phi(x/\alpha)$ for $G$ and $\Xi(\alpha j\cdot 2\pi)$ for $F(2\pi j)$ up to that error gives the boxed approximation. Statement (d) is immediate from $\Xi$ real with real zeros interlacing sign changes.

## Analytic domain audit

- $\Phi$ is real-analytic, even, strictly positive, and doubly-exponentially decaying on $\mathbb R$; $G$ is bounded with compact support, so $F$ is entire of exponential type $\tfrac12$ and $\widehat\xi$ likewise.
- $\Xi$ is entire; no poles, no branch cuts, no contours occur.
- (O-16001.1) has removable singularities at $z=2\pi j$; the zeros of $\sin(z/2)$ cancel the poles where $\xi_j\neq0$ and survive as zeros of $\widehat\xi$ where $\xi_j=0$. This is CvS's own bookkeeping and is reproduced here without change.
- The approximation bound displayed above is stated for **real** $z$. Off the real axis the sinc kernel grows like $e^{|{\rm Im}\,z|/2}$ and the bound must be multiplied accordingly; the honest strip statement is left to the error-budget work flagged below.

## Dependency audit

- CvS Lemmas 5.1(ii)/5.7(ii) for $\eta=\sum_je_j$ — used in (a).
- CvS Theorem 5.6(ii) and its proof for (O-16001.1) — used in (b).
- `L-16001`(e),(f) for $K=\Phi/4$, positivity and the decay rate — used in (c).
- Translation property of Fourier coefficients — used in (O-16001.2). Elementary.

## Gap audit

1. **This is the *natural* target, not necessarily the *production* target.** The repository's chain (`L-15101` → `L-15102` → `L-15103` "two-sign prolate radical repair" → `T-15102`) applies further "repairs". Whether the production coefficient vector equals (O-16001.2) has **not** been verified. Everything downstream (`L-16003`, `R-16001`) is therefore scoped to the naive sampled target and must be labelled so.
2. The approximation in (O-16001.2) replaces $F(2\pi j)$ by $\Xi(2\pi\alpha j)$; the difference is the aliasing/truncation tail. For any *quantitative* claim the exact $F(2\pi j)$ should be used, not $\Xi$.
3. The strip version of the error bound (needed for Hurwitz, which lives on $|{\rm Im}\,z|<1/2$) is not derived here.
4. CvS Theorem 5.6(ii) is stated only for the integer node set $\lambda_j=j$; Proposition 5.10 covers general simple symmetric nodes but gives **only** the polynomial statement, with **no** transform statement. Any "finite transform" attached to non-integer nodes is the working note's own construction and is outside CvS. This is a scope point the working note does not make.
5. CvS state **no converse** to 5.6 or 5.10; the converse used by the program is the note's own `L-15108`, which was independently checked this session and found correct.

## Adversarial tests

Numerical, at 80–150 decimal digits (**EMPIRICAL** confirmation of a derivation):

| test | result |
|---|---|
| truncated cardinal series $F$ vs $\Xi(\alpha z)$ at $z=1.3,4.7,9.1,20$, $\alpha=0.5$, $N=8/16/30$ | max error $6.7\!\cdot\!10^{-9}$ / $2.9\!\cdot\!10^{-9}$ / $2.9\!\cdot\!10^{-9}$ (aliasing floor) |
| same, $\alpha=0.3$, $N=8/16/30$ | $6.9\!\cdot\!10^{-6}$ / $2.4\!\cdot\!10^{-11}$ / $3.0\!\cdot\!10^{-20}$ (converging) |
| evenness $\xi_{-j}=\xi_j$ | exact, by construction |

So the sampled target **does** satisfy hypothesis (8) of the working note's Theorem 3.1 (local uniform convergence to $\Xi$) in the required sense, and the decrease of the error with $\alpha$ confirms the aliasing interpretation.

A direct refutation of the trap (e), in exact rational arithmetic: CvS Appendix B.1 decides $p=(1,x,1)$ at nodes $(-1,0,1)$, giving real-rootedness iff $x(x+2)\ge0$. The two regimes with an *empty* isotropic cone ($x>0$ and $x<-2$) are exactly the real-rooted ones, and the *nonempty*-cone regime $-2<x<0$ is exactly the failing one. So `L-16002` is correct and consistent with CvS — it simply does not apply to a mixed-sign target.

## Adjudication: `T-15104` is **not** refuted by the three-node example

Two independent audits this session reached opposite conclusions about whether the instance $\lambda=(-1,0,1)$, $p=(1/10,8/10,1/10)$ refutes the programme. The disagreement is resolved by reading the exact wording, and the resolution is worth recording because the same confusion will recur.

The instance satisfies every hypothesis of Connes–van Suijlekom Theorem 5.6: with $b=(1,0,-1)$ (odd) and diagonal $a=(9,\tfrac14,9)$ (even),

$$Q=\begin{pmatrix}9&-1&-1\\-1&\tfrac14&-1\\-1&-1&9\end{pmatrix}$$

is of form (11), $Qp=0$ exactly, $Q\succeq0$ of rank 2 (principal minors $9,\tfrac14,9$; $\tfrac54,80,\tfrac54$; $\det=0$), and $\ker Q=\mathbb Rp$ is one-dimensional and $\gamma$-even. Verified in exact rational arithmetic.

- The **exponential sum** $\sum_jp_je^{ij z}=\tfrac8{10}+\tfrac2{10}\cos z$ has **only nonreal** zeros ($\cos z=-4$).
- The **CvS transform** $\widehat p(z)=2e^{-iz/2}\sin(z/2)\bigl[\tfrac{0.1}{z+2\pi}+\tfrac{0.8}{z}+\tfrac{0.1}{z-2\pi}\bigr]$ has **only real** zeros: $2\pi\mathbb Z\setminus\{0,\pm2\pi\}$, together with the roots of $P(z/2\pi)$, i.e. $z=\pm2\pi\sqrt{4/5}$. And $P(s)=s^{2}-\tfrac45$ is real-rooted, as Theorem 5.6(i) asserts.

So the example refutes only the **unwindowed** reading. `T-15104` says verbatim *"the Fourier transform of the corresponding **compactly supported** finite Fourier sum"*, and the working note's Theorem 3.1 says *"the Fourier transform of its compactly supported finite Fourier sum"*. Both use the correct object. **`T-15104` and the note's Theorem 3.1 stand; Connes–van Suijlekom stands; the three-node example refutes neither.** Any audit reporting otherwise has substituted $\sum_jp_je^{i\lambda_jz}$ for the windowed transform.

The residual criticism that *is* fair: neither the note nor `T-15104` writes the transform down explicitly, so a reader must go to the primary source to learn which object is meant. Displaying (O-16001.1) once in the claim file would remove the ambiguity permanently.

## Remaining uncertainty

The identification (a),(b) is quoted from the primary source and is certain. The identification (c),(d) of the *program's* target is a reconstruction: it is the natural one, it satisfies the convergence hypothesis, and it is what a reader of `L-15101` would build — but it has not been checked against the production "repaired" vectors. That check is the single most important follow-up.

## Suggested next attack

1. Verify against branch `agent/gpt56-pro-10/151-radical-hermite-bridge` whether the production repaired target is (O-16001.2) or something else; in particular determine what `L-15103`'s "two-sign" repair does to the sign pattern.
2. Derive the strip form of the approximation bound, with explicit constants, so Hurwitz can be applied rigorously.
3. Add a one-line screening test to the exact checker: if the coefficient vector is one-signed, the Finsler condition is vacuous (`L-16002`) and the level carries no information.
