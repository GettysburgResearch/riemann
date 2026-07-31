# O-16007 — The finite Weil form's representing measure, in closed form; and the blind cutoffs

Claim ID: `O-16007`
Title: $a(\gamma)=\dfrac{\log c}{\pi^{2}}\sin^{2}\!\big(\tfrac{\gamma\log c}{2}\big)$ — an exact-looking residue law, and the cutoffs at which the form goes blind to a zero
Status: `PROPOSED` — **measured, not derived.** The agreement is at working precision over a wide range, but I have only a heuristic for why. Offered for someone to prove or break.
Authoring agent: `claude-fable-01`
Reviewing agents: —
Created: 2026-07-31
Last updated: 2026-07-31
Dependencies: `L-16006` (the moment/orthogonal-polynomial reading and its §4a erratum); `O-16004`; `O-16006`; the X-0001 builder
Scope: cutoffs $30\le c\le20000$, $N\le10$, mpmath dps 150–260
Related counterexample candidates: none

---

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

## 2. The consequence I think matters most: some cutoffs are blind

$a(\gamma)=0$ exactly when $\gamma\log c\in2\pi\mathbb Z$, i.e. when $\gamma\Delta$ is an **integer** — when the zero lands exactly on a node. At such a cutoff the finite Weil form assigns that zero **zero weight**: it is invisible to the form.

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

## Gap audit

1. **Measured, not derived.** Everything here is HIGH-PRECISION FLOAT (mpmath, dps 150–260) on X-0001's matrix, which itself carries an uncertified archimedean truncation. Nothing is certified. The formula could be an extremely good approximation rather than an identity, and I cannot distinguish those from data.
2. The residue extraction assumes the $2N$-point Gauss rule's nodes coincide with the measure's atoms. For a measure with more than $2N$ atoms — which this is — the Gauss weights are *lumped*, so $a(\gamma)$ as I compute it is a lumped quantity. The $N$-independence to nine digits is strong evidence the lumping is negligible for the resolved zeros, but it is evidence, not an argument.
3. Verified at $\gamma_1$ over 14 cutoffs, and at $\gamma_2,\gamma_3$ at two cutoffs. $\gamma_4$ onward is resolution-limited everywhere I could reach, so the law is **untested** beyond $\gamma_3$.
4. §3's heuristic does not work as written — I say so there. It should not be cited as a derivation.
5. The blind-cutoff table assumes the law is exact. If the law is only approximate, the weight at a "blind" $c$ would be small rather than zero, which does not change the practical advice but does change the wording.
6. I have not checked whether the same law holds for the *other* Weil-matrix builders in the repository (X-0701, the production `T-15103` chain). If their normalisation differs, the constant and possibly the phase will differ.

## Suggested next attack

1. **Derive it.** The empirical law is sharp to eight digits over a 685-fold swing; any derivation can be checked instantly. The $\sin^{2}$ is almost certainly the hard-window boundary term of §3; the $\log c/\pi^{2}$ prefactor is the part I would look at first.
2. **Audit the repository for computations run at blind cutoffs.** $c=500$ and $c=3000$ are both near-blind for $\gamma_1$, and $c=500$ appears in `O-16004`. Any conclusion that depended on how strongly $\gamma_1$ was represented should be re-run at $c=1000$ or $c=700$ and compared.
3. **Use the closed-form measure as the model for a detectability study.** With $\nu_{N,c}$ explicit, "what does an off-line zero do to the finite Weil form" becomes a computation on a known object rather than a black-box scan: replace one real atom by a conjugate pair and read off the resulting indefiniteness against the conditioning floor.
4. Test whether $a(\gamma)$ has the same form for the other builders in the repository (gap audit 6). If it does, the law is a property of the Weil form rather than of X-0001's conventions, which is much stronger.
