# L-16001 — The exact Weil-radical target is Pólya's Φ, and the transform normalization carries a factor 1/4

Claim ID: `L-16001`
Title: Identification of the L-15101 radical target with the classical Riemann–Pólya function, and correction of the transform normalization
Status: `PROPOSED`
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `L-15101` (statement only — this lemma re-derives its analytic content from scratch and does **not** import it); classical Poisson summation; the standard Mellin representation of `ξ`
Scope: the canonical positive-route target before localization
Related counterexample candidates: none directly; supplies the object used by `O-16001`, `R-16001`, `C-16001`

---

## Statement

Let

$$h(x)=\frac{\pi}{2}\,x^{2}\bigl(2\pi x^{2}-3\bigr)e^{-\pi x^{2}},\qquad x\in\mathbb R,$$

and let

$$k(u)=u^{1/2}\sum_{n\ge 1}h(nu),\qquad u>0,\qquad K(t):=k(e^{t}).$$

Then all of the following hold.

**(a) Hermite decomposition.** With $\psi_m(x)=H_m\!\bigl(\sqrt{2\pi}\,x\bigr)e^{-\pi x^{2}}$ ($H_m$ the physicists' Hermite polynomials, so that $\widehat{\psi_m}=(-i)^{m}\psi_m$ under $\widehat f(y)=\int f(x)e^{-2\pi ixy}dx$),

$$h=\tfrac{1}{64}\,\psi_{4}-\tfrac{3}{16}\,\psi_{0}.$$

Consequently $\widehat h=h$, and $h(0)=\widehat h(0)=0$.

**(b) Mellin transform.** For $\operatorname{Re}s>0$,

$$\int_{0}^{\infty}h(v)\,v^{s-1}\,dv=\frac{s(s-1)}{8}\,\pi^{-s/2}\,\Gamma\!\left(\frac{s}{2}\right).$$

**(c) Transform normalization — corrected.** With $\displaystyle \widehat k(z)=\int_{0}^{\infty}k(u)\,u^{-iz}\,\frac{du}{u}$ and $\Xi(z)=\xi\!\left(\tfrac12+iz\right)$, $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$,

$$\boxed{\;\widehat k(z)=\tfrac14\,\Xi(z)\;}$$

for all $z$ in the strip of absolute convergence, hence for all $z\in\mathbb C$ by analytic continuation.
Claim `L-15101` equation (L-15101.7) asserts $\widehat k=\Xi$ **without** the factor $\tfrac14$. The factor is harmless for every zero-location statement, but it is wrong as an identity and must be corrected wherever `L-15101.7` is used quantitatively (for example inside any explicit error budget that compares $\|\widehat{p_\lambda}-\Xi\|$ against a bound derived from $\|k\|$).

**(d) Inversion symmetry and evenness.** $k(1/u)=k(u)$ for all $u>0$; equivalently $K(-t)=K(t)$.

**(e) Identification with Pólya's function — with the scaling stated exactly.** Define

$$\Phi(t):=4K(t)=\sum_{n\ge1}\bigl(4\pi^{2}n^{4}e^{9t/2}-6\pi n^{2}e^{5t/2}\bigr)e^{-\pi n^{2}e^{2t}},$$

so that, by (c) and (d), $\Xi(z)=\int_{\mathbb R}\Phi(t)e^{izt}\,dt$. This $\Phi$ is the Riemann–Pólya kernel **in the normalization of this note**.

The classical literature (Titchmarsh §2.16, and the de Bruijn–Newman literature) overwhelmingly uses a variable scaled by $2$:

$$\Phi_{\mathrm{cl}}(u)=\sum_{n\ge1}\bigl(2\pi^{2}n^{4}e^{9u}-3\pi n^{2}e^{5u}\bigr)e^{-\pi n^{2}e^{4u}},\qquad \Xi\!\left(\tfrac{z}{2}\right)=2\int_{0}^{\infty}\Phi_{\mathrm{cl}}(u)\cos(zu)\,du .$$

**The exact dictionary is**

$$\boxed{\ \Phi_{\mathrm{cl}}(u)=2\,K(2u)=\tfrac12\,\Phi(2u),\qquad\text{equivalently}\qquad K(t)=\tfrac12\,\Phi_{\mathrm{cl}}(t/2).\ }$$

So it is **wrong** to say "$K=\Phi_{\mathrm{cl}}/4$": that is off by a factor $2$ *and* misses the argument rescaling $t\mapsto t/2$. Any import from the classical literature — in particular the de Bruijn–Newman flow $H_{\tau}(z)=\int e^{\tau u^{2}}\Phi_{\mathrm{cl}}(u)e^{izu}du$, whose $\tau$ is calibrated to $\Phi_{\mathrm{cl}}$, not to $\Phi$ — must be transported through this dictionary. This is exactly the kind of interface slip §8 of the working note warns about, and it was made and caught during this session.

**(f) Positivity.** $K(t)>0$ for every real $t$. (Classical for $\Phi$; see the dependency audit.)

**(g) Theta form.** With $\theta(w)=\sum_{n\ge1}e^{-\pi n^{2}w}$,

$$k(u)=u^{1/2}\Bigl(w^{2}\theta''(w)+\tfrac32 w\,\theta'(w)\Bigr)\Big|_{w=u^{2}}.$$

---

## Definitions

- $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$, entire of order 1.
- $\Xi(z)=\xi(\tfrac12+iz)$; $\Xi$ is entire, real on $\mathbb R$, even.
- Fourier convention on $\mathbb R$: $\widehat f(y)=\int_{\mathbb R}f(x)e^{-2\pi ixy}\,dx$.
- Multiplicative Fourier–Mellin convention: $\widehat k(z)=\int_{0}^{\infty}k(u)u^{-iz}\,d^{*}u$, $d^{*}u=du/u$. Under $u=e^{t}$ this is the ordinary Fourier transform $\int_{\mathbb R}K(t)e^{-izt}\,dt$.
- RH is equivalent to: every zero of $\Xi$ in $S_{1/2}=\{|\operatorname{Im}z|<1/2\}$ is real.

---

## Motivation

The repository's positive route (`L-15101`, `T-15102`, `T-15104`, PR #158) is built on a target $k$ described as an "exact global Weil-radical vector" obtained from the Connes–Consani $E$-map, with its transform identified as $\Xi$ by an **imported** normalization that `L-15101` explicitly leaves conditional on an audit.

This lemma discharges that audit by elementary means, and in doing so removes the import entirely: $k$ is, up to the factor $4$, exactly the function Riemann and Pólya used a century ago. That identification is not a deflation — it is the single most useful structural fact available about the target, because it connects the repository's finite program to the whole classical corpus on $\Phi$: Pólya's positivity and monotonicity results, the Laguerre–Pólya class, the de Bruijn–Newman flow, Rodgers–Tao's $\Lambda\ge0$, and the Jensen/Turán moment inequalities. Every one of those becomes available as a tool or as an obstruction. In particular, positivity (f) is the hypothesis that drives the collapse proved in `R-16001`.

---

## Proof

**(a).** $H_0(y)=1$ and $H_4(y)=16y^{4}-48y^{2}+12$. Substituting $y=\sqrt{2\pi}\,x$,

$$\psi_{0}(x)=e^{-\pi x^{2}},\qquad \psi_{4}(x)=\bigl(64\pi^{2}x^{4}-96\pi x^{2}+12\bigr)e^{-\pi x^{2}}.$$

Hence

$$\tfrac{1}{64}\psi_{4}-\tfrac{3}{16}\psi_{0}=\Bigl(\pi^{2}x^{4}-\tfrac{3\pi}{2}x^{2}+\tfrac{3}{16}-\tfrac{3}{16}\Bigr)e^{-\pi x^{2}}=\Bigl(\pi^{2}x^{4}-\tfrac{3\pi}{2}x^{2}\Bigr)e^{-\pi x^{2}},$$

which is exactly $h(x)=\tfrac{\pi}{2}x^{2}(2\pi x^{2}-3)e^{-\pi x^{2}}$. Since $\widehat{\psi_m}=(-i)^m\psi_m$ and $(-i)^{0}=(-i)^{4}=1$, both summands are Fourier eigenfunctions with eigenvalue $+1$, so $\widehat h=h$. The constant terms cancel by construction, giving $h(0)=0$; and $\widehat h(0)=h(0)=0$, i.e. $\int_{\mathbb R}h=0$.

**(b).** For $a>-1$, $\int_{0}^{\infty}v^{a}e^{-\pi v^{2}}dv=\tfrac12\pi^{-(a+1)/2}\Gamma\!\bigl(\tfrac{a+1}{2}\bigr)$. Therefore

$$\int_{0}^{\infty}h(v)v^{s-1}dv=\pi^{2}\cdot\tfrac12\pi^{-\frac{s+4}{2}}\Gamma\!\Bigl(\tfrac{s}{2}+2\Bigr)-\tfrac{3\pi}{2}\cdot\tfrac12\pi^{-\frac{s+2}{2}}\Gamma\!\Bigl(\tfrac{s}{2}+1\Bigr)
=\tfrac12\pi^{-s/2}\Bigl[\Gamma\!\bigl(\tfrac s2+2\bigr)-\tfrac32\Gamma\!\bigl(\tfrac s2+1\bigr)\Bigr].$$

Using $\Gamma(\tfrac s2+1)=\tfrac s2\Gamma(\tfrac s2)$ and $\Gamma(\tfrac s2+2)=\tfrac s2\bigl(\tfrac s2+1\bigr)\Gamma(\tfrac s2)$,

$$\Gamma\!\bigl(\tfrac s2+2\bigr)-\tfrac32\Gamma\!\bigl(\tfrac s2+1\bigr)=\Gamma\!\bigl(\tfrac s2\bigr)\cdot\tfrac s2\Bigl[\tfrac s2+1-\tfrac32\Bigr]=\Gamma\!\bigl(\tfrac s2\bigr)\cdot\frac{s(s-1)}{4},$$

which gives (b).

**(c).** For $\operatorname{Re}(\tfrac12-iz)>1$ the double sum converges absolutely, so with $s=\tfrac12-iz$,

$$\widehat k(z)=\int_{0}^{\infty}u^{s}\sum_{n\ge1}h(nu)\,\frac{du}{u}=\sum_{n\ge1}n^{-s}\int_{0}^{\infty}v^{s}h(v)\,\frac{dv}{v}=\zeta(s)\cdot\frac{s(s-1)}{8}\pi^{-s/2}\Gamma\!\left(\frac s2\right)=\frac{\xi(s)}{4}.$$

Finally $\xi(s)=\xi(1-s)$ and $1-(\tfrac12-iz)=\tfrac12+iz$, so $\widehat k(z)=\tfrac14\xi(\tfrac12+iz)=\tfrac14\Xi(z)$. Both sides are entire in $z$ (the left by the super-Gaussian decay established in (e)), so the identity extends to all $z\in\mathbb C$.

**(d).** Poisson summation for the even Schwartz function $h$ gives $\sum_{n\in\mathbb Z}h(nu)=u^{-1}\sum_{n\in\mathbb Z}\widehat h(n/u)$. Since $h$ is even and $h(0)=\widehat h(0)=0$, this reads $2\sum_{n\ge1}h(nu)=2u^{-1}\sum_{n\ge1}\widehat h(n/u)=2u^{-1}\sum_{n\ge1}h(n/u)$, using $\widehat h=h$. Multiplying by $\tfrac12 u^{1/2}$ gives $k(u)=u^{-1/2}\sum_{n\ge1}h(n/u)=k(1/u)$.

**(e).** Substituting $u=e^{t}$ into $k(u)=u^{1/2}\sum_n h(nu)$ with $h(x)=\bigl(\pi^{2}x^{4}-\tfrac{3\pi}{2}x^{2}\bigr)e^{-\pi x^{2}}$:

$$K(t)=e^{t/2}\sum_{n\ge1}\Bigl(\pi^{2}n^{4}e^{4t}-\tfrac{3\pi}{2}n^{2}e^{2t}\Bigr)e^{-\pi n^{2}e^{2t}}=\sum_{n\ge1}\Bigl(\pi^{2}n^{4}e^{9t/2}-\tfrac{3\pi}{2}n^{2}e^{5t/2}\Bigr)e^{-\pi n^{2}e^{2t}},$$

which is $\Phi(t)/4$ for the $\Phi$ displayed above. That this $\Phi$ is the classical one is exactly the statement $\int_{\mathbb R}\Phi(t)e^{izt}dt=\Xi(z)$, which follows from (c) and (d): $\int K(t)e^{-izt}dt=\widehat k(z)=\tfrac14\Xi(z)$, and $K$ even makes the sign of $z$ immaterial.

**(f).** As $t\to+\infty$ the $n=1$ term dominates and is positive; $K$ is even by (d). The full statement $\Phi>0$ on $\mathbb R$ is classical (see dependency audit). It is also directly checkable: $\Phi(t)=4K(t)$ and $K$ is a strictly positive, strictly log-concave-looking, super-Gaussian bump; see the adversarial tests.

**(g).** With $w=u^{2}$ and $\theta(w)=\sum_{n\ge1}e^{-\pi n^{2}w}$ one has $\sum_n n^{2}e^{-\pi n^{2}w}=-\pi^{-1}\theta'(w)$ and $\sum_n n^{4}e^{-\pi n^{2}w}=\pi^{-2}\theta''(w)$. Substituting into (e) gives (g). ∎

---

## Analytic domain audit

- $h$ is Schwartz on $\mathbb R$; every interchange of $\sum$ and $\int$ above is justified by absolute convergence, which holds for $\operatorname{Re}s>1$ and is then propagated by analytic continuation of $\xi$.
- $k$ is real-analytic on $(0,\infty)$; $K$ is real-analytic on $\mathbb R$ and satisfies $0<K(t)\le C(1+|t|)^{N}e^{-\pi e^{2|t|}}$-type super-Gaussian decay, so $\widehat k$ is entire of order 1 and **infinite** (maximal) type. In particular $\widehat k$ is **not** of exponential type; this is essential and is used in `C-16001`.
- $\Xi$ is entire; $\xi$ has no poles (the pole of $\zeta$ at $s=1$ is cancelled by the factor $s-1$, the trivial zeros by $\Gamma(s/2)$). No contour, branch cut, or multivalued function occurs anywhere in this lemma.
- The identity in (c) is between two entire functions of $z$; it is proved on a half-plane of absolute convergence and extended by the identity theorem.

## Dependency audit

- Poisson summation for Schwartz functions — used once, in (d).
- $\widehat{\psi_m}=(-i)^{m}\psi_m$ for Hermite functions — used in (a).
- $\zeta(s)$ Dirichlet series for $\operatorname{Re}s>1$ and the functional equation $\xi(s)=\xi(1-s)$ — used in (c).
- Positivity of $\Phi$ in (f) is **imported** as classical (Pólya, *Bemerkung über die Integraldarstellung der Riemannschen ξ-Funktion*, 1926; see also Csordas–Norfolk–Varga). It is **not** re-proved here. Everything else is self-contained.
- **No result of PR #158, and no Connes–van Suijlekom or Connes–Consani theorem, is used.** In particular this lemma does not depend on the imported Weil-radical theorem `L-15101.5`.

## Gap audit

- The identity (c) is a statement about $\widehat k$, **not** about any localized or sampled version. Nothing here says a truncation of $k$ has a transform close to $\Xi$ in any norm — that is `L-15101` §4 and is separate.
- Nothing here says anything about zeros. $\widehat k=\tfrac14\Xi$ is an identity, not a zero-localization statement, and it is of course consistent with RH being false.
- (f) is imported. If Pólya's positivity were false the collapse argument of `R-16001` would still apply to any strictly positive target, but would no longer be known to apply to *this* target. The imported status is flagged deliberately.
- The scaling dictionary in (e) is now stated explicitly, but it remains the most likely site of a downstream error, because $\Phi$ and $\Phi_{\mathrm{cl}}$ differ by *both* a factor and a change of variable. Every import from the classical literature must be transported through it; in particular the de Bruijn–Newman parameter $\tau$ is calibrated to $\Phi_{\mathrm{cl}}$ and does **not** transfer verbatim.
- The factor $\tfrac14$ in (c) has not been traced back through `L-15101`'s derivation to determine whether the error is in the imported Connes–Consani normalization or in `L-15101`'s transcription of it. That trace is left open.

## Adversarial tests

All performed at 30–40 decimal digits with `mpmath` (floating point, therefore **EMPIRICAL** confirmation of a **PROVED** statement, not a substitute for it):

| test | result |
|---|---|
| $h(0)$ | $0$ exactly |
| $\int_{\mathbb R}h$ | $-2.5\cdot10^{-49}$ (numerical zero at 40 digits) |
| $\widehat h(y)-h(y)$ at $y=0.3,\,1.1,\,2.7$ | $<7\cdot10^{-42}$ |
| $Mh(s)$ vs $\tfrac{s(s-1)}{8}\pi^{-s/2}\Gamma(s/2)$ at $s=2.3,\,1.5,\,0.7+1.3i$ | agreement to $\ge 41$ digits |
| $k(u)-k(1/u)$ at $u=0.4,\,0.75,\,1.6$ | $<4\cdot10^{-32}$ |
| $\int_{\mathbb R}K(t)e^{-izt}dt$ vs $\Xi(z)/4$ at $z=0,\,3.5,\,14.1347\ldots,\,2+0.4i$ | agreement to $\ge 32$ digits, **including complex $z$** |
| $\widehat k(z)$ vs $\Xi(z)$ (no factor) | disagrees by exactly a factor $4$ at every test point |
| $K(t)>0$ for $t\in[-4,4]$ step $0.5$ | all positive; minimum $4.6\cdot10^{-4059}$ at $t=\pm4$ |

Reference values for reuse: $K(0)=0.223348450233561722\ldots$, $K(1/4)=0.121593705183543547\ldots$, $K(1/2)=0.0150943629460871638\ldots$, $K(3/4)=1.97883551661652968\cdot10^{-4}$, $K(1)=6.8890697031781688\cdot10^{-8}$, $K(3/2)=3.2441977245456912\cdot10^{-24}$, $\Xi(0)=\xi(1/2)=0.497120778188314\ldots$.

## Remaining uncertainty

The author is fully confident in (a)–(e) and (g), which are elementary and independently checked numerically to more than 30 digits. Item (f) is imported and carries the usual risk of an imported classical statement whose exact hypotheses were not re-read in the original. The scaling dictionary in the gap audit is the most likely place for a downstream interface error.

## Suggested next attack

1. Trace the factor $\tfrac14$ back through the Connes–Consani $E$-map normalization to determine where `L-15101.7` lost it, and correct every downstream quantitative bound.
2. Re-read Pólya (1926) and confirm the exact statement and proof of $\Phi>0$ and of the monotonicity of $\Phi$ on $(0,\infty)$, so that (f) can be promoted from imported to internally proved.
3. Exploit the identification: every classical result about $\Phi$ — Pólya's $\Xi^{*}$ surrogate with provably real zeros, the de Bruijn–Newman flow, the moment/Jensen inequalities — is now directly applicable to the repository's target. See `O-16001` and `C-16001`.
