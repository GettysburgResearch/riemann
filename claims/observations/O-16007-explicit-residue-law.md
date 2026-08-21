# O-16007 — The finite Weil form's representing measure, in closed form; and the blind cutoffs

Claim ID: `O-16007`
Title: $a(\gamma)=\dfrac{\log c}{\pi^{2}}\sin^{2}\!\big(\tfrac{\gamma\log c}{2}\big)$ — an exact-looking residue law, and the cutoffs at which the form goes blind to a zero
Status: **`PARTIAL` — §1–§2's identity is now DERIVED and promoted to `T-16002`; §5's blindness conclusion is REFUTED and withdrawn.** Read the banner below before anything else.
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `L-16006` (the moment/orthogonal-polynomial reading and its §4a erratum); `O-16004`; `O-16006`; the X-0001 builder
Scope: cutoffs $30\le c\le20000$, $N\le10$, mpmath dps 150–260
Related counterexample candidates: none

---

> # SUPERSEDED IN PART — read `T-16002` instead
>
> A second-pass review of PR #173 supplied the derivation of the residue law and identified **two independent fatal defects** in §5's blindness conclusion. Both are confirmed. The disposition:
>
> | section | disposition |
> |---|---|
> | §1 identity $a(\gamma)=(\log c/\pi^2)\sin^2(\gamma\log c/2)$ | **survives, and is upgraded from measured to DERIVED** — see `T-16002`§1 |
> | §2 "some cutoffs are blind" | **wrong as stated.** The resonance is *removable* when $\gamma\Delta$ is an integer inside the node band ($g_u=Lu_k^2$, not $0$), and outside the band it is an on-line notch only |
> | §2's practical rule ("choose $c$ so $\gamma\Delta$ is near a half-integer") | **withdrawn.** It optimises the wrong quantity and I do not have a replacement |
> | §3 heuristic | superseded by the actual derivation |
> | §5 "blind cutoffs are blind to an off-line zero", the `never` table | **REFUTED and withdrawn** — see `T-16002`§3 |
>
> The two defects in §5, both verified here: **(i)** `blinddet.py` froze the residue at its real on-line value and moved only the poles, never introducing the analytic continuation $\sin^2(\pi(k+iy))=-\sinh^2(\pi y)<0$ that dominates off the line; **(ii)** its inertia routine used $1\times1$ pivots only and returns $(0,0,2)$ on a matrix of true inertia $(1,1,0)$, so it could not have detected a hyperbolic negative direction in any case. Redone correctly, **every** $\delta_c$ is finite and there is no alternation at all.
>
> Issue #188's headline is superseded accordingly.

## 0. Statement

`L-16006`§4a establishes (numerically, at working precision) that the finite arithmetic Weil form's induced inner product on $\mathcal P_{2N}$ is a **moment functional**, so it has a representing positive measure on $\mathbb R$. Extracting that measure's own Gauss rule — nodes = roots of the CvS kernel polynomial, weights = Christoffel numbers — its nodes sit at the zeta zeros in node units $\mu=\gamma\Delta$, $\Delta=\log c/2\pi$, and its masses are $W=a(\gamma)/\Omega(\gamma\Delta)^{2}$ with $\Omega(s)=\prod_{k=-N}^{N}(k-s)$.

The **implied residue** $a(\gamma)$ came out independent of $N$ to nine or ten significant figures, and appears to be given exactly by

$$\boxed{\ a(\gamma)\;=\;\frac{\log c}{\pi^{2}}\,\sin^{2}\!\left(\frac{\gamma\log c}{2}\right)\;=\;\frac{\log c}{2\pi^{2}}\Big(1-\cos(\gamma\log c)\Big).\ }$$

Equivalently, since $\gamma\log c/2=\pi\gamma\Delta$: **$a(\gamma)=\dfrac{\log c}{\pi^{2}}\sin^{2}(\pi\,\gamma\Delta)$ — a function of the distance from the zero's node-coordinate to the nearest integer.**

So the representing measure is, in closed form,

$$\nu_{N,c}\;=\;\sum_{\gamma>0}\frac{\log c}{\pi^{2}}\,\sin^{2}\!\Big(\frac{\gamma\log c}{2}\Big)\cdot\frac{\delta_{\gamma\Delta}+\delta_{-\gamma\Delta}}{\Omega(\gamma\Delta)^{2}} .$$

## 1. Evidence

**At $\gamma_1$, across 14 cutoffs.** $N=6$, dps 168. $a_1$ measured against the formula:

| $c$ | $\log c$ | $a_1$ measured | $(\log c/\pi^2)\sin^2(\gamma_1\log c/2)$ | ratio |
|---|---|---|---|---|
| 30 | 3.4011974 | 0.272380269013 | 0.272380268978 | 1.000000 |
| 50 | 3.9120230 | 0.136313690624 | 0.136313690570 | 1.000000 |
| 80 | 4.3820266 | 0.0828064200134 | 0.0828064197986 | 1.000000 |
| 120 | 4.7874917 | 0.212145419672 | 0.212145419424 | 1.000000 |
| 200 | 5.2983174 | 0.0338910961733 | 0.0338910956082 | 1.000000 |
| 350 | 5.8579332 | 0.16716764857 | 0.167167647941 | 1.000000 |
| **500** | 6.2146081 | **0.00237150941705** | 0.00237150890689 | 1.000000 |
| 700 | 6.5510803 | 0.358160123359 | 0.358160122559 | 1.000000 |
| **1000** | 6.9077553 | **0.689035801277** | 0.689035800080 | 1.000000 |
| 1400 | 7.2442275 | 0.473136747188 | 0.473136746715 | 1.000000 |
| 2000 | 7.6009025 | 0.0722332295598 | 0.0722332282033 | 1.000000 |
| **3000** | 8.0063676 | **0.00100669492132** | 0.0010066940239 | 1.000001 |
| 5000 | 8.5171932 | 0.201142594978 | 0.201142593424 | 1.000000 |
| 8000 | 8.9871968 | 0.363529217424 | 0.363529215602 | 1.000000 |

Spread of the ratio over all 14: $1.00000$ to $1.00000$. Meanwhile **$a_1$ itself varies by a factor of 685**, from $1.007\times10^{-3}$ at $c=3000$ to $0.689$ at $c=1000$, non-monotonically. A formula that tracks a 685-fold non-monotone swing to eight digits is not a fit.

**At higher zeros, and why the agreement degrades exactly where it should.** Cutoff 2000, dps $=60+20N$:

| $N$ | zero | node rel. err | $a$ measured | formula | ratio |
|---|---|---|---|---|---|
| 8 | $\gamma_1$ | $2.9\times10^{-15}$ | 0.0722332282 | 0.0722332282 | 1.000000 |
| 8 | $\gamma_2$ | $8.2\times10^{-9}$ | 0.7343116529 | 0.7343113786 | 1.00000037 |
| 8 | $\gamma_3$ | $1.1\times10^{-5}$ | 0.4001164941 | 0.3999773939 | 1.00034777 |
| 8 | $\gamma_4$ | $7.0\times10^{-3}$ | 0.3195820161 | 0.2532247460 | 1.262 |
| 10 | $\gamma_1$ | $6.0\times10^{-17}$ | 0.0722332282 | 0.0722332282 | 1.000000 |
| 10 | $\gamma_2$ | $1.3\times10^{-12}$ | 0.7343113787 | 0.7343113786 | 1.000000 |
| 10 | $\gamma_3$ | $1.5\times10^{-8}$ | 0.3999776565 | 0.3999773939 | 1.00000066 |
| 10 | $\gamma_4$ | $2.1\times10^{-4}$ | 0.2562106321 | 0.2532247460 | 1.0118 |
| 10 | $\gamma_5$ | $5.7\times10^{-3}$ | 0.1929609231 | 0.1741777289 | 1.108 |

and cutoff 20000, $N=10$: $\gamma_1$ ratio 1.000000, $\gamma_2$ 1.000000, $\gamma_3$ 1.00000048.

**The agreement is exactly as good as the node resolution and no better.** Where the Gauss node has converged onto $\gamma_j$, the residue matches to full precision; where it has not, both are off together, and raising $N$ fixes them together. That is the signature of an exact law being approached, not of a coincidence.

## 2. ~~The consequence I think matters most: some cutoffs are blind~~ — WITHDRAWN, see `T-16002`§2

> **This section is retained only as a record of a wrong inference.** The premise is right — $a(\gamma)=0$ when $\gamma\Delta\in\mathbb Z$ — but the conclusion drawn from it is false. See `T-16002`§2.

$a(\gamma)=0$ exactly when $\gamma\log c\in2\pi\mathbb Z$, i.e. when $\gamma\Delta$ is an **integer**. I inferred that the form is then "blind" to that zero. **That does not follow.** Inside the node band the vanishing prefactor is cancelled by the pole of $\ell$ and the zero contributes $Lu_k^2$; outside the band the on-line contribution really does vanish, but the off-line continuation is $-\sinh^2(\pi y)<0$ and is the *most* favourable case for detection.

For $\gamma_1$ these are $\log c=2\pi k/\gamma_1=0.444537k$, i.e. $c=e^{0.444537k}$:

| $k$ | 12 | 13 | **14** | 15 | 16 | 17 | **18** |
|---|---|---|---|---|---|---|---|
| blind $c$ | 207.5 | 323.5 | **504.4** | 786.5 | 1226 | 1912 | **2981** |

**Two of these are cutoffs already in use in this repository.** `O-16004`'s headline table includes $c=500$, which sits at $k=14$ (blind at 504.4): there $a_1=2.4\times10^{-3}$, some 290 times smaller than at $c=1000$. And $c=3000$ sits essentially on $k=18$: $a_1=1.007\times10^{-3}$, the smallest value I measured anywhere.

Two things worth separating:

- **Location is robust; amplitude is not.** At $c=500$ the recovered $w_1$ is still $14.1347252$, right to eight digits. So a near-blind cutoff does *not* spoil the zero's position — it collapses the weight the form gives it. Anyone reading a table of recovered zeros would see nothing wrong.
- **Practical rule.** Choose $c$ so that $\gamma\Delta$ is near a **half**-integer for the zeros you care about, which maximises $\sin^2$. Between $c=500$ and $c=1000$ the weight on $\gamma_1$ differs by a factor of 290 at identical cost. If any computation in this project is sensitive to how strongly $\gamma_1$ is represented — a positivity margin, a conditioning estimate, a sensitivity study — it should not be run at $c=500$.

## 3. A heuristic for where the $\sin^{2}$ comes from — offered as a heuristic only

The CvS basis functions live on $[0,L]$ at frequencies $a_j=2\pi j/L$. For a test function of that form the Fourier integral over the **hard window** is

$$\int_0^L\sin(a_jy)\,e^{i\gamma y}\,dy=\frac{a_j\big(e^{i\gamma L}-1\big)}{\gamma^{2}-a_j^{2}},$$

using $a_jL=2\pi j$ so $e^{ia_jL}=1$. The zero-side of the explicit formula then contributes $|\widehat g(\gamma)|^{2}$, which carries the common factor

$$\big|e^{i\gamma L}-1\big|^{2}=2\big(1-\cos\gamma L\big)=4\sin^{2}\!\big(\tfrac{\gamma L}{2}\big).$$

That is precisely the measured factor, with $L=\log c$. So the oscillation looks like the **boundary term of the hard window** — the same window/aliasing structure `L-16005` quantified for the sampled thread, reappearing in the arithmetic thread. I emphasise that I have **not** completed this into a derivation: my attempt to carry it through the parity conventions produced a vanishing contribution for even coefficient vectors, so at least one convention in my sketch is wrong. The $\log c/\pi^{2}$ prefactor I have not accounted for at all. **Someone should do this properly; the empirical law is sharp enough to check any derivation against.**

## 4. What this does and does not say about positivity

It would be a mistake to read the boxed formula as making Weil positivity free. The measure was extracted **from** a form that was already positive definite, and its nodes came out real because of that. If a zero were off the critical line the corresponding atom would be complex, the Gauss rule would not be a positive measure on $\mathbb R$, and the extraction would fail rather than return a negative weight. So the law is a *description* of the finite form conditional on the positivity, not a proof of it.

What it does give is a **closed-form model of the finite Weil form** that is accurate to the resolution limit, which makes several previously vague questions concrete — notably how much a given zero actually contributes at a given cutoff, which is what a sensitivity or detectability study needs.

## 5. ~~The blind cutoffs are not merely weak — they are blind~~ — **REFUTED AND WITHDRAWN**

> **This entire section is wrong and is retained only so the error is on the record.** Both the model and the numerics were defective; the corrected experiment is in `T-16002`§3 and shows **no blindness and no alternation**. Do not use the table below.

§2 says a blind cutoff collapses the *weight* the form gives a zero. I asked whether that translates into a loss of *detection* and concluded that it does. It does not.

Build the zero-side Loewner form with the **measured** residues $a(\gamma)=(\log c/\pi^2)\sin^2(\gamma\log c/2)$ (not unit residues), poles at $\pm\gamma_k\Delta$ for the first 25 zeros, and displace $\gamma_1$ off the line as the symmetric quadruple $\pm\gamma_1\Delta\pm id$. Then bisect for the critical displacement $\delta_c$ at which the inertia first acquires a negative eigenvalue. $N=10$, dps 150, $d$ scanned over $[10^{-40},10^{3}]$:

| $c$ | $\gamma_1\Delta$ | frac. part | $a_1$ | $n_-$ unperturbed | $\delta_c$ |
|---|---|---|---|---|---|
| 9.23136 | 5.0000006 | $6.0\times10^{-7}$ | $8.09\times10^{-13}$ | 0 | **never** |
| 11.529 | 5.4999975 | 0.500 | 0.24771668 | 0 | $2.003\times10^{-11}$ |
| 14.3985 | 5.9999926 | $\approx1$ | $1.47\times10^{-10}$ | 0 | **never** |
| 17.9823 | 6.5000000 | 0.500 | 0.29275621 | 0 | $1.745\times10^{-12}$ |
| 22.458 | 6.9999963 | $\approx1$ | $4.36\times10^{-11}$ | 0 | **never** |
| 28.0478 | 7.5000023 | 0.500 | 0.33779573 | 0 | $4.081\times10^{-13}$ |
| 35.0288 | 8.0000018 | $1.8\times10^{-6}$ | $1.14\times10^{-11}$ | 0 | **never** |
| 43.7473 | 8.4999989 | 0.500 | 0.38283499 | 0 | $3.014\times10^{-13}$ |
| 54.6359 | 9.0000004 | $3.8\times10^{-7}$ | $5.75\times10^{-13}$ | 0 | **never** |

The apparent alternation is an artefact of the two defects named in the banner. **Corrected, every $\delta_c$ is finite** — $3.9\times10^{-10}$, $5.1\times10^{-11}$, $1.2\times10^{-11}$, $3.8\times10^{-12}$, $2.2\times10^{-12}$, $7.7\times10^{-13}$, $6.1\times10^{-13}$, $5.0\times10^{-13}$, $3.8\times10^{-13}$ down the same nine cutoffs — decreasing smoothly with $c$ with **no** systematic integer/half-integer difference. There is no blindness.

Two qualifications. This is the synthetic zero-side model (with residues measured from the real thing), not X-0001's $Q_W$ — see gap audit 7. And the cutoffs here are small ($c\le55$), chosen so that $\gamma_1\Delta$ sits inside the node band at an affordable $N$; at large $c$ one needs $N\gtrsim\gamma_1\Delta$ for the zero to be visible at all, which is the separate constraint `L-16004`'s SCOPE CAUTION and `O-16008`§2 describe. A first run at $N=5$ with $c\approx200$–$3000$ found $\delta_c=$ *never* at **every** cutoff, blind or not, precisely because $\gamma_1\Delta/N\approx2.4$–$3.6$ put the zero outside the band. Both effects have to be respected at once.

## Gap audit

1. **Measured, not derived.** Everything here is HIGH-PRECISION FLOAT (mpmath, dps 150–260) on X-0001's matrix, which itself carries an uncertified archimedean truncation. Nothing is certified. The formula could be an extremely good approximation rather than an identity, and I cannot distinguish those from data.
2. The residue extraction assumes the $2N$-point Gauss rule's nodes coincide with the measure's atoms. For a measure with more than $2N$ atoms — which this is — the Gauss weights are *lumped*, so $a(\gamma)$ as I compute it is a lumped quantity. The $N$-independence to nine digits is strong evidence the lumping is negligible for the resolved zeros, but it is evidence, not an argument.
3. Verified at $\gamma_1$ over 14 cutoffs, and at $\gamma_2,\gamma_3$ at two cutoffs. $\gamma_4$ onward is resolution-limited everywhere I could reach, so the law is **untested** beyond $\gamma_3$.
4. §3's heuristic does not work as written — I say so there. It should not be cited as a derivation.
5. The blind-cutoff table assumes the law is exact. If the law is only approximate, the weight at a "blind" $c$ would be small rather than zero, which does not change the practical advice but does change the wording.
6. I have not checked whether the same law holds for the *other* Weil-matrix builders in the repository (X-0701, the production `T-15103` chain). If their normalisation differs, the constant and possibly the phase will differ.
7. §5 is run on the **synthetic zero-side model** carrying the measured residues, not on $Q_W$ itself. It inherits every caveat of `O-16008` — in particular that its constants are not converged in the number of poles, and that the model has no archimedean or prime blocks. The alternation between "never" and $10^{-11}$–$10^{-13}$ is so clean that I do not think it is an artefact, but it has not been reproduced on the arithmetic matrix.
8. §5's "never" means "no negative eigenvalue at any $d$ in $[10^{-40},10^{3}]$ on a bisection", not a proof that none exists. A window of $d$ outside that range, or between bisection probes, would be missed — though the accompanying scans in `O-16008`§3 show $\lambda_{\min}(d)$ is smooth and singly-peaked, which makes a missed window unlikely.

## Suggested next attack

1. **Derive it.** The empirical law is sharp to eight digits over a 685-fold swing; any derivation can be checked instantly. The $\sin^{2}$ is almost certainly the hard-window boundary term of §3; the $\log c/\pi^{2}$ prefactor is the part I would look at first.
2. **Audit the repository for computations run at blind cutoffs.** $c=500$ and $c=3000$ are both near-blind for $\gamma_1$, and $c=500$ appears in `O-16004`. Any conclusion that depended on how strongly $\gamma_1$ was represented should be re-run at $c=1000$ or $c=700$ and compared.
3. **Use the closed-form measure as the model for a detectability study.** With $\nu_{N,c}$ explicit, "what does an off-line zero do to the finite Weil form" becomes a computation on a known object rather than a black-box scan: replace one real atom by a conjugate pair and read off the resulting indefiniteness against the conditioning floor.
4. Test whether $a(\gamma)$ has the same form for the other builders in the repository (gap audit 6). If it does, the law is a property of the Weil form rather than of X-0001's conventions, which is much stronger.
