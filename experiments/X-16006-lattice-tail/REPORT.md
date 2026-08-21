# Adjudication of the reviewer's objection to L-16005(iii)

**Adjudicator:** independent computational check, 2026-07-31
**Object:** `/home/user/riemann/claims/lemmas/L-16005-hard-window-artifact-dominance.md`, item **(iii)** and its Proof paragraph
**Working directory:** `/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/tail/`
**Nothing in `/home/user/riemann` was modified; nothing was committed.**

---

## VERDICT IN ONE LINE

**The reviewer is right on the mathematics.** On the hard-window lattice the first
integration-by-parts boundary term vanishes *identically*, the sharp decay is
$j^{-2}$ and not $j^{-1}$, and L-16005's own measured table already exhibits
$j^{-2}$ rather than $j^{-1}$ — so item (iii)'s sharpness claim is **contradicted
by its own evidence**, not merely underdetermined by it. The reviewer's constant
is right in magnitude but **missing the $(-1)^j$ alternation and a sign flip**.
Two things the reviewer concedes are also confirmed: the uniform bound
$|E_j|\le 2\Phi(T)/(\pi\alpha j)$ **is valid**, and $O(1/j)$ **is** the sharp law
*off* the lattice. And a third thing neither side states: in the regime L-16005
recommends for actual work ($\alpha\lesssim0.4$, small $j$), **neither** power law
describes $|E_j|$, which is essentially flat there.

**None of L-16005's three downstream conclusions moves.** Details in §5.

---

## 1. Evidence labelling used here

Per `README.md` §10 and the four-level convention:

| Label | Meaning as used below |
|---|---|
| `EXACT` | symbolic identity, no numerics involved |
| `CERTIFIED` | rigorous enclosure / interval or ball arithmetic — **nothing in this report is CERTIFIED** |
| `HIGH-PRECISION FLOAT` | `mpmath` at `mp.dps` 50–90, non-rigorous quadrature, but cross-validated by two independent routes agreeing to 38–50 digits |
| `ORDINARY FLOAT` | double precision / heuristic |

Every number below is `HIGH-PRECISION FLOAT` unless explicitly marked `EXACT`.
Like L-16005's own tables, none of it is a certificate.

---

## 2. The symbolic computation, done independently  `EXACT`

Setup exactly as in L-16005: $\Phi=4K$, $T=1/(2\alpha)$, $\omega_j=2\pi\alpha j$,

$$E_j=2\int_T^\infty \Phi(t)\cos(\omega_j t)\,dt .$$

### 2.1 The lattice identity

$$\omega_j T=2\pi\alpha j\cdot\frac{1}{2\alpha}=\pi j
\quad\Longrightarrow\quad
\boxed{\ \sin(\omega_j T)=0,\qquad \cos(\omega_j T)=(-1)^j\ }\qquad\text{for every integer } j .$$

This is an identity in $\alpha$ — it holds at **every** $\alpha$, not just special
ones, because the cutoff $T=1/(2\alpha)$ and the sampling frequency
$\omega_j=2\pi\alpha j$ are locked together by the same $\alpha$. The reviewer's
observation is correct and is the whole content of the dispute.

### 2.2 First integration by parts

$$\int_T^\infty\Phi\cos(\omega t)\,dt=\Big[\Phi(t)\frac{\sin\omega t}{\omega}\Big]_T^\infty-\frac1\omega\int_T^\infty\Phi'(t)\sin(\omega t)\,dt
=\underbrace{-\frac{\Phi(T)\sin(\omega T)}{\omega}}_{\textbf{= 0 on the lattice}}-\frac1\omega\int_T^\infty\Phi'\sin(\omega t)\,dt .$$

L-16005's Proof writes this line correctly and then says "the lower contributes
$-\Phi(T)\sin(\omega T)/\omega$ … The boundary term is genuinely present and
$O(1/\omega)$, so the order cannot be improved by iterating." **That last sentence
is the error.** The term is present as an expression; it is *numerically zero* at
every lattice point $\omega=\omega_j$.

### 2.3 Second integration by parts

$$\int_T^\infty\Phi'\sin(\omega t)\,dt=\Big[-\Phi'(t)\frac{\cos\omega t}{\omega}\Big]_T^\infty+\frac1\omega\int_T^\infty\Phi''\cos(\omega t)\,dt
=\frac{\Phi'(T)(-1)^j}{\omega}+\frac1\omega\int_T^\infty\Phi''\cos(\omega t)\,dt .$$

Here the boundary term **does not** vanish: $\cos(\omega_jT)=(-1)^j\ne0$. Hence

$$\boxed{\ E_j=-\frac{2(-1)^j\,\Phi'(T)}{\omega_j^{2}}-\frac{2}{\omega_j^{2}}\int_T^\infty\Phi''(t)\cos(\omega_j t)\,dt\ }\qquad `EXACT`$$

### 2.4 Iterating: which boundary terms vanish

Odd-order boundary terms carry $\sin(\omega_jT)=0$ and die; even-order ones carry
$\cos(\omega_jT)=(-1)^j$ and survive. So exactly **half** of the boundary terms
vanish, the expansion advances in steps of $\omega^{-2}$, and

$$E_j\;\sim\;-2(-1)^j\sum_{m\ge0}\frac{(-1)^m\,\Phi^{(2m+1)}(T)}{\omega_j^{\,2m+2}}\qquad `EXACT` \text{ (asymptotic)} .$$

### 2.5 The sharp asymptotic, with the explicit constant

Since $\Phi'(T)<0$ (Φ decreasing on $(0,\infty)$), write $\Phi'(T)=-|\Phi'(T)|$:

$$\boxed{\;E_j=(-1)^{j}\,\frac{|\Phi'(1/(2\alpha))|}{2\pi^{2}\alpha^{2}\,j^{2}}\;+\;O(j^{-4})
\;=\;(-1)^{j+1}\,\frac{\Phi'(1/(2\alpha))}{2\pi^{2}\alpha^{2}\,j^{2}}+O(j^{-4})\;}$$

equivalently $|E_j|=\dfrac{C(\alpha)}{j^{2}}\bigl(1+O(j^{-2})\bigr)$ with
$C(\alpha)=\dfrac{2|\Phi'(1/(2\alpha))|}{(2\pi\alpha)^{2}}=\dfrac{|\Phi'(1/(2\alpha))|}{2\pi^{2}\alpha^{2}}$.

**The exponent is $j^{-2}$, not $j^{-1}$.** The next correction is
$+2(-1)^j\Phi'''(T)/\omega_j^4$, i.e. relative size $-\Phi'''(T)/(\Phi'(T)\omega_j^2)$;
since $\Phi'''(T)<0$ and $\Phi'(T)<0$ this is **negative**, so $j^2|E_j|$ must
approach $C$ **from below** — a falsifiable prediction, confirmed in §4.

### 2.6 Scorecard against the reviewer's statement

Reviewer wrote: $E_j = \Phi'(1/(2\alpha))/(2\pi^2\alpha^2 j^2)+O(j^{-4})$.

| Component | Verdict |
|---|---|
| first boundary term vanishes identically on the lattice | **correct** |
| exponent $j^{-2}$ | **correct** |
| constant magnitude $\lvert\Phi'(T)\rvert/(2\pi^2\alpha^2)$ | **correct** |
| remainder $O(j^{-4})$ (expansion in even powers) | **correct** |
| **sign** | **incomplete**: the true expression alternates as $(-1)^j$; the reviewer's has no alternation and, since $\Phi'(T)<0$, is a fixed negative number. Correct form is $(-1)^{j+1}\Phi'(T)/(2\pi^2\alpha^2j^2)$. Verified numerically at **all 160** $(\alpha,j)$ pairs tested: $\operatorname{sign}(E_j)=(-1)^j$ without exception. |
| "uniform $O(1/j)$ bound remains valid" | **correct** — see §3 |
| "the sharpness claim and the title/interpretation must change" | **correct for the sharpness claim**; see §5 for what does *not* need to change |

### 2.7 A free factor-2 improvement L-16005 left on the table  `EXACT`

L-16005's own one-step argument, with $\sin(\omega_jT)=0$ inserted, gives

$$|E_j|\le\frac{2}{\omega_j}\Bigl(\Phi(T)\underbrace{|\sin\omega_jT|}_{=0}+\int_T^\infty|\Phi'|\Bigr)=\frac{2\Phi(T)}{\omega_j}=\frac{\Phi(T)}{\pi\alpha j},$$

exactly **half** the stated $2\Phi(T)/(\pi\alpha j)$, with no new input at all.

### 2.8 A rigorous $O(j^{-2})$ bound is available (with one gap)

From §2.3, $\;|E_j|\le\dfrac{2}{\omega_j^{2}}\Bigl(|\Phi'(T)|+\int_T^\infty|\Phi''|\Bigr)$, and
**if** $\Phi''\ge0$ on $(T,\infty)$ then $\int_T^\infty|\Phi''|=-\Phi'(T)=|\Phi'(T)|$, giving

$$|E_j|\ \le\ \frac{4|\Phi'(T)|}{\omega_j^{2}}=\frac{|\Phi'(T)|}{\pi^{2}\alpha^{2}j^{2}}\qquad\text{— tight to a factor exactly 2.}$$

Grid scan on $t\in[0.30,5.00]$ step $0.01$: $\Phi''>0$ throughout
(`HIGH-PRECISION FLOAT`, **not a proof**). $\Phi''$ *is* negative near the origin
($\Phi''(0)=-16.73$, $\Phi''(0.1)=-12.88$, $\Phi''(0.2)=-3.67$), so convexity is a
genuine hypothesis that must be checked for the $T$ in use — but every $T$ in
L-16005's tables ($T\ge0.4545$) lies safely inside the convex region. **Convexity
of $\Phi$ on $(T,\infty)$ is a real gap** if this bound is to be used as a
certificate; it is one Pólya-type monotonicity statement away, in the same
family as the monotonicity L-16005 already imports.

---

## 3. Is the old $O(1/j)$ bound still valid? Yes — and it *is* sharp off the lattice

The claimed bound $|E_j|\le2\Phi(T)/(\pi\alpha j)$ was never violated in any of
my 160 evaluations. Its ratio to the truth at $\alpha=1$: 10.5 at $j=10$, 41 at
$j=40$ — valid, increasingly wasteful, exactly as an off-by-one-power bound should be.

**Discriminating experiment.** Keep $\omega_j=2\pi j$ but move the cutoff off the
lattice. Then $\sin(\omega_jT)\ne0$ and $O(1/j)$ must return. With
$T=0.711294492161$ ($\omega_jT/\pi=1.4226\,j$, irrational multiple), $\alpha=1$,
over $j=24\ldots40$:

| quantity | min | max | ratio |
|---|---|---|---|
| $j\,\lvert E_j\rvert$ | $5.62\times10^{-5}$ | $5.955\times10^{-4}$ | 10.6 (**bounded, oscillating**) |
| $j^{2}\lvert E_j\rvert$ | $2.13\times10^{-3}$ | $2.30\times10^{-2}$ | 10.8 (**growing $\propto j$**) |

and the envelope $\max_j j|E_j| = 5.955\times10^{-4}$ agrees with the predicted
$2\Phi(T)/(2\pi)=5.98\times10^{-4}$ to three digits. Off the lattice the
first-order prediction $-2\Phi(T)\sin(\omega T)/\omega$ tracks $E_j$ term by term.

**So L-16005(iii) is a correct theorem about a general cutoff $T$ and a false
theorem about the cutoff $T=1/(2\alpha)$ that L-16005 actually uses.** That is
the precise shape of the error: not a miscalculation, a failure to substitute
the lemma's own hypothesis into its own conclusion.

*(Caution for anyone re-running this: any $T$ with $2\alpha T$ rational, e.g.
$T=0.625$ at $\alpha=1$ where $\omega_jT=1.25\pi j$, gives a **sub**lattice —
$\sin=0$ whenever $4\mid j$. Sampling only $j\in4\mathbb{Z}$ there reproduces
the $j^{-2}$ law spuriously. Use an irrational multiple.)*

---

## 4. Numerical verification  `HIGH-PRECISION FLOAT`

### 4.1 Method and its validation

$\Phi$ is the repo's own evaluator, copied verbatim from
`/home/user/riemann/experiments/X-16002-cvs-sampled-target-census/decay.py`:
$\Phi(t)=\sum_{n\ge1}(4\pi^2n^4e^{9t/2}-6\pi n^2e^{5t/2})e^{-\pi n^2e^{2t}}$, matching `L-16001`(e).

Two changes were needed to reach $j=40$:

1. **Panel-aligned quadrature.** `decay.py` calls
   `quad(..., [T, T+1, T+2, 4])`, which at $j=40$ packs ~160 oscillations of
   $\cos(\omega t)$ into one panel. I subdivide at the half-periods of
   $\cos(\omega t)$, so every panel is non-oscillatory.
2. **Truncation of the tail at** $t_{\rm end}$ with $\Phi(t_{\rm end})<10^{-(\text{dps}+40)}$.

Validation (`check.py`):

| check | result |
|---|---|
| Route A (tail quadrature $2\int_T^\infty$) vs **Route B** ($\Xi(2\pi\alpha j)-2\int_0^T$, independent, uses `mpmath` `zeta`/`gamma`) | agree to **38–50 digits** at 11 test points spanning $\alpha\in\{0.4,\dots,1.0\}$, $j\in\{1,\dots,40\}$ |
| `mp.dps`=50/maxdeg 6 vs `mp.dps`=90/maxdeg 9 | agree to **42–52 digits** |
| $\Xi(z)=2\int_0^\infty\Phi\cos(zt)dt$ normalization | agrees to **50 digits** at $z=0,3,2\pi$ |
| closed-form $\Phi^{(k)}$ vs `mpmath.diff` | agree to **50 digits**, $k=1,2,3$ |
| reproduction of L-16005's (iv) table | all 7 entries reproduced, ratios **0.9998–1.0011** |

The last row matters: **L-16005's numbers are right.** The dispute is entirely
about how they were read.

### 4.2 The verdict table, $\alpha=1$ ($T=0.5$, $\Phi'(T)=-0.73378625$, $C=0.037174046$)

| $j$ | $E_j$ (signed) | sign $=(-1)^j$? | $j\lvert E_j\rvert$ | $j^{2}\lvert E_j\rvert$ | $j^2\lvert E_j\rvert/C$ | local slope |
|---|---|---|---|---|---|---|
| 4 | $+2.1024\times10^{-3}$ | yes | 0.008409 | **0.033638** | 0.9049 | 1.588 |
| 6 | $+9.9459\times10^{-4}$ | yes | 0.005968 | **0.035805** | 0.9632 | 1.892 |
| 8 | $+5.6933\times10^{-4}$ | yes | 0.004555 | **0.036437** | 0.9802 | 1.950 |
| 10 | $+3.6711\times10^{-4}$ | yes | 0.003671 | **0.036711** | 0.9876 | 1.971 |
| 12 | $+2.5594\times10^{-4}$ | yes | 0.003071 | **0.036856** | 0.9914 | 1.981 |
| 20 | $+9.2653\times10^{-5}$ | yes | 0.001853 | **0.037061** | 0.9970 | 1.994 |
| 30 | $+4.1249\times10^{-5}$ | yes | 0.001237 | **0.037124** | 0.99866 | 1.997 |
| 40 | $+2.3216\times10^{-5}$ | yes | 0.000929 | **0.037146** | 0.99925 | 1.998 |

$j\lvert E_j\rvert$ falls by a factor **9.1** over $j=4\to40$; $j^{2}\lvert E_j\rvert$
varies by **10%** and converges monotonically **from below** to the predicted
$C=0.0371740$, ratio $0.99925$ at $j=40$. The approach-from-below is the §2.5
prediction; quantitatively the two-term asymptotic predicts
$j^2|E_j|/C=1-1.2033/j^{2}$, giving 0.9248 / 0.98797 / 0.99699 / 0.999248 at
$j=4/10/20/40$ against measured 0.9049 / 0.98755 / 0.99697 / 0.99925. **This settles it.**

### 4.3 Across $\alpha$ — and an important caveat neither side raised

Least-squares exponent $p$ in $|E_j|\sim j^{-p}$:

| $\alpha$ | $T$ | $C(\alpha)$ | $p$ on $j{=}4..12$ | $p$ on $j{=}10..20$ | $p$ on $j{=}30..40$ | $j^2\lvert E_j\rvert/C$ at $j{=}40$ |
|---|---|---|---|---|---|---|
| 1.0 | 0.5 | $3.7174\times10^{-2}$ | 1.925 | 1.987 | **1.998** | 0.99925 |
| 0.7 | 0.71429 | $3.9125\times10^{-3}$ | 1.323 | 1.830 | **1.973** | 0.9901 |
| 0.5 | 1.0 | $2.3335\times10^{-6}$ | 0.413 | 1.042 | **1.766** | 0.9131 |
| 0.4 | 1.25 | $5.7287\times10^{-12}$ | 0.114 | 0.378 | **1.184** | 0.6723 |

**Nowhere does $p$ settle near 1.** It rises monotonically toward 2 in every
column. But at small $\alpha$ the convergence is slow, and this is a real
phenomenon, not noise:

**Onset of the $j^{-2}$ regime.** The expansion parameter is $\lambda/\omega_j$
with $\lambda=|\Phi''/\Phi'|(T)\approx2\pi e^{2T}=2\pi e^{1/\alpha}$. Empirically
$j^2|E_j|/C>0.9$ first holds at:

| $\alpha$ | $\lambda=\lvert\Phi''/\Phi'\rvert(T)$ | $e^{1/\alpha}/\alpha$ | first $j$ with $j^2\lvert E_j\rvert/C>0.9$ | $\omega_j/\lambda$ there |
|---|---|---|---|---|
| 1.0 | 9.258 | 2.72 | 4 | 2.7 |
| 0.7 | 18.99 | 5.96 | 13 | 3.0 |
| 0.5 | 39.56 | 14.78 | 38 | 3.0 |
| 0.4 | 69.83 | 30.46 | 83 | 3.0 |
| 0.3 | 169.5 | 93.4 | $>120$ | — |

Clean rule: the $j^{-2}$ law takes hold at $\;\omega_j\gtrsim3\lambda$, i.e.
$\;\boxed{j\gtrsim 3e^{1/\alpha}/\alpha}$, which **blows up as $\alpha\to0$**.

**Below that index $|E_j|$ is neither $j^{-1}$ nor $j^{-2}$ — it is essentially
flat.** At $\alpha=0.4$, $|E_j|$ moves only from $6.785\times10^{-15}$ ($j=1$) to
$5.879\times10^{-15}$ ($j=12$): a 13% change across a 12-fold range in $j$, local
exponent 0.005–0.25. In that regime the honest statement is
$|E_j|\approx\varepsilon_{\rm true}(T)=2\int_T^\infty\Phi$ (at $\alpha=0.4$:
$6.792\times10^{-15}$ vs $|E_1|=6.785\times10^{-15}$).

**This matters practically**, because $\alpha\lesssim0.4$ is exactly the regime
L-16005(v) and its "Suggested next attack" point 1 send future work into. So the
corrected lemma should say: *uniform bound $\varepsilon(T)$ for $j\lesssim3e^{1/\alpha}/\alpha$,
$j^{-2}$ law beyond* — and should not advertise **either** power law as
describing the computed range at small $\alpha$.

---

## 5. Do the downstream conclusions move? **No — all three stand.**

The reason is structural: **I reproduced every $|E_j|$ in L-16005's tables to
within 0.11%.** The measured values were correct; only their verbal
classification was wrong. Every downstream conclusion is a function of the
*values*, not of the exponent label.

### (a) Crossover $j\approx2$ where $|E_j|$ overtakes $|\Xi(2\pi\alpha j)|$ — **UNCHANGED**

| $\alpha$ | crossover $j$ | $\lvert E_j\rvert/\lvert\Xi_j\rvert$ at $j=1,2,3$ |
|---|---|---|
| 1.1 | **2** | 0.0827, 15.8, 724 |
| 1.0 | **2** | 0.0379, **1.049**, 22.4 |
| 0.7 | 5 | $4.59\times10^{-4}$, $1.86\times10^{-3}$, 0.0544 |
| 0.5 | 10 | $3.2\times10^{-8}$, $6.4\times10^{-8}$, $2.3\times10^{-7}$ |
| 0.4 | $>12$ | $1.6\times10^{-14}$, $2.5\times10^{-14}$, $5.4\times10^{-14}$ |

At $\alpha=1$ the crossover is at $j=2$ exactly as stated, and the ratio column
of table (iv) is reproduced verbatim. The crossover is set by $|E_j|$ vs an
**exponentially** decaying $|\Xi_j|$; whether $|E_j|$ falls like $j^{-1}$ or
$j^{-2}$ is irrelevant against $e^{-\pi^2\alpha j/2}$.
*(Bonus, not in L-16005: the crossover moves out sharply as $\alpha$ falls —
$j=2,5,10,>12$ at $\alpha=1.0,0.7,0.5,0.4$. Worth adding; it independently
supports (v).)*

### (b) Certification boundary $\alpha\lesssim0.4$ — **UNCHANGED**

Table (v) compares the **$j$-independent** uniform bound $\varepsilon(T)$ against
the smallest coefficient, so the exponent cannot enter at all. I reproduced
$\varepsilon(T)$ from L-16005's own formula (ii) — all eight rows match to three
digits — and then added the corrected rigorous bound
$B_2=|\Phi'(T)|/(\pi^2\alpha^2j^2)$ at $j=10$:

| $\alpha$ | $T$ | $\varepsilon(T)$ bnd | $\varepsilon(T)$ true | $B_1=\frac{2\Phi(T)}{\pi\alpha j}$ | $B_2$ (new) | $\lvert E_{10}\rvert$ actual | $\lvert\Xi_{10}\rvert$ | old verdict | **new verdict** |
|---|---|---|---|---|---|---|---|---|---|
| 1.1 | 0.4545 | $3.01\times10^{-2}$ | $1.56\times10^{-2}$ | $5.86\times10^{-3}$ | $9.00\times10^{-4}$ | $4.48\times10^{-4}$ | $4.26\times10^{-21}$ | no | **no** |
| 1.0 | 0.5 | $1.59\times10^{-2}$ | $8.32\times10^{-3}$ | $3.84\times10^{-3}$ | $7.44\times10^{-4}$ | $3.67\times10^{-4}$ | $2.38\times10^{-18}$ | no | **no** |
| 0.9 | 0.5556 | $6.62\times10^{-3}$ | $3.52\times10^{-3}$ | $2.06\times10^{-3}$ | $5.17\times10^{-4}$ | $2.51\times10^{-4}$ | $1.61\times10^{-17}$ | no | **no** |
| 0.8 | 0.625 | $1.88\times10^{-3}$ | $1.01\times10^{-3}$ | $7.81\times10^{-4}$ | $2.66\times10^{-4}$ | $1.24\times10^{-4}$ | $5.85\times10^{-15}$ | no | **no** |
| 0.7 | 0.7143 | $2.71\times10^{-4}$ | $1.49\times10^{-4}$ | $1.60\times10^{-4}$ | $7.83\times10^{-5}$ | $3.33\times10^{-5}$ | $1.14\times10^{-12}$ | no | **no** |
| 0.6 | 0.8333 | $1.06\times10^{-5}$ | $5.94\times10^{-6}$ | $9.68\times10^{-6}$ | $7.34\times10^{-6}$ | $2.44\times10^{-6}$ | $1.92\times10^{-11}$ | no | **no** |
| 0.5 | 1.0 | $2.20\times10^{-8}$ | $1.26\times10^{-8}$ | $3.51\times10^{-8}$ | $4.67\times10^{-8}$ | $8.53\times10^{-9}$ | $7.86\times10^{-9}$ | no | **no** (but see below) |
| 0.4 | 1.25 | $1.17\times10^{-14}$ | $6.79\times10^{-15}$ | $4.00\times10^{-14}$ | $1.15\times10^{-13}$ | $6.13\times10^{-15}$ | $1.43\times10^{-7}$ | **yes** | **yes** |

**Verdict column identical, row for row.** The gap at $\alpha=1$ is 14 orders of
magnitude ($3.7\times10^{-4}$ vs $2.4\times10^{-18}$); a single power of $j$ is
noise against that.

Two corrections to L-16005's *text* nonetheless follow:

- **Gap-audit item 3** currently reads "the sharper $j$-dependent bound of (iii)
  improves matters somewhat but, being $O(1/j)$, does not change the verdict for
  any $\alpha\ge0.5$ — at $\alpha=1$, $j=10$ it gives $3.8\times10^{-3}$ against a
  coefficient of $2.4\times10^{-18}$." Corrected number: $7.4\times10^{-4}$
  (rigorous $B_2$) or $3.67\times10^{-4}$ (actual). **Conclusion unchanged.**
- **$\alpha=0.5$ is now known to be marginal, not comfortable.** The *actual*
  $|E_{10}|=8.53\times10^{-9}$ against $|\Xi_{10}|=7.86\times10^{-9}$ — a factor
  1.08, i.e. essentially on the line. The best rigorous bound available,
  $\min(\varepsilon,B_1/2,B_2)=1.75\times10^{-8}$, still exceeds it by $2.2\times$,
  so "no" survives — but it survives by a factor of two, not by orders of
  magnitude. That is worth saying explicitly; it identifies $\alpha=0.5$ as the
  place where a *sharper* bound (or a slightly larger $T$) could flip a row.
  Note $B_2>\varepsilon$ at $\alpha=0.5,\,j=10$ precisely because $j=10<3e^{2}/0.5\approx44$:
  the asymptotic bound is not yet useful there (§4.3).

### (c) Artifact-dominance table (iv) — **UNCHANGED, verbatim**

All seven $|E_j|$ and all seven ratios reproduced (max deviation 0.11%). The
conclusion "beyond $j\approx2$ the hard-window coefficient is essentially pure
truncation artifact" is **unaffected**: it contrasts polynomial with exponential
decay, and $j^{-2}$ is still polynomial. Only the sentence *"while $|E_j|$
decays only like $1/j$"* must become *"like $1/j^{2}$"*.

---

## 6. Subtlety (3): could L-16005's own measurement have distinguished the two?

**Asked to check whether the original evidence was merely underdetermined. It was not — it was contradicted.** L-16005's exact window, $\alpha=1$, $j=4,6,8,10,12$:

| statistic | values | max/min | spread about mean |
|---|---|---|---|
| $j\lvert E_j\rvert$ (**as quoted in L-16005**) | 0.008409, 0.005968, 0.004555, 0.003671, 0.003071 | **2.738** | **104%** |
| $j^{2}\lvert E_j\rvert$ (same data) | 0.033638, 0.035805, 0.036437, 0.036711, 0.036856 | **1.096** | **9%** |

Least-squares exponent on that window: $p=\mathbf{1.919}$.

The five quoted numbers *are* $\Phi'$-driven $j^{-2}$ data. They fall by a factor
2.738 across a window whose $j$ range is a factor of 3 — that is a clean $1/j$
drift in $j|E_j|$, i.e. $1/j^2$ in $|E_j|$. The same data, multiplied by $j^2$
instead, is flat to 9% and **monotone increasing toward a limit**, exactly as §2.5
predicts.

So the two hypotheses were **separated by an order of magnitude in scatter**
(104% vs 9%) by the original measurement itself. The failure was one of reading,
and it is visible in two places in the file:

- (iii): *"constant up to a slow drift"* — of a quantity that falls by a factor of **2.74** across the window.
- Adversarial tests: *"$j|E_j|$ measured constant to within $\pm35\%$ over $j=4..12$"* — the actual spread about the mean is $+63\%/-40\%$, and *"inconsistent with any faster decay"* is the reverse of the truth.

Had the same table been printed with a $j^2|E_j|$ column — as
`decay.py`'s sibling `smooth.py` already does for the smooth cutoff — the error
would have been caught on sight. **Recommended process fix:** whenever a decay
order is asserted from a table, print $j^p|E_j|$ for $p$ and $p\pm1$ and report
each column's max/min. One extra column; it is exactly what settles this case.

For honesty in the other direction: at $\alpha=0.5$ and $0.4$ over the *same*
$j=4..12$ window, the fitted exponents are 0.41 and 0.11. A reader who ran only
those would be equally misled toward "$|E_j|$ is constant". The short-window
diagnosis is fragile in general; it happens to be decisive here because
$\alpha=1$ is well past the onset index.

---

## 7. What I recommend the patch to L-16005 say

1. **(iii) title and body.** Replace "The decay law is only $O(1/j)$, and this is
   sharp" with something like *"A coarse $O(1/j)$ bound, and the sharp lattice law
   $O(1/j^2)$."* Keep the bound $|E_j|\le2\Phi(T)/(\pi\alpha j)$ as a valid coarse
   bound (optionally halve it, §2.7). Delete "no further integration by parts
   improves the order, because the boundary term does not vanish", and delete the
   corresponding last sentence of the Proof.
2. **Add the lattice identity** $\omega_jT=\pi j$ as the reason, state the sharp
   asymptotic of §2.5 **with the $(-1)^j$**, and add the rigorous $O(j^{-2})$
   bound of §2.8 flagging the convexity hypothesis as an unproved (numerically
   supported) input, in the same status as the imported monotonicity.
3. **Add the onset caveat** of §4.3: the $j^{-2}$ law holds for
   $j\gtrsim3e^{1/\alpha}/\alpha$; below that $|E_j|\approx\varepsilon(T)$, flat.
   This is the practically binding statement at $\alpha\lesssim0.4$.
4. **Replace the (iii) sharpness table** with a $j^2|E_j|$ column, and fix the
   Adversarial-tests bullet, which currently asserts the opposite of what the
   data show.
5. **Correct the number** in Gap-audit item 3 ($3.8\times10^{-3}\to7.4\times10^{-4}$),
   and note the $\alpha=0.5$ marginality (§5b).
6. **Leave (i), (ii), (iv), (v), (vi) alone.** (ii)'s bound and its measured
   tightness ratios, (iv)'s table and crossover, and (v)'s verdict column all
   survive intact. In particular **do not weaken the artifact-dominance
   conclusion** — the reviewer's correction makes the error *smaller*, but not
   remotely small enough to matter against $e^{-\pi^2\alpha j/2}$.
7. **Item (vi) is untouched by this dispute but inherits a caution.** Its
   hard-vs-smooth comparison quotes $j|E_j|$ for both cutoffs as "approximately
   constant". The hard column there is the same mis-read data. The smooth
   column's $j|E_j|$ (0.029, 0.012, 0.0068, 0.0073) is non-monotone and L-16005
   itself flags it as its least reliable computation. **Someone should redo (vi)
   with panel-aligned quadrature and both $j$ and $j^2$ columns before it is
   relied on.** I did not re-derive the smooth case; that is outside this task
   and is the one place where L-16005 may still contain an unexamined numerical
   claim.

---

## 8. Files, reproduction, and remaining uncertainty

All under `/tmp/claude-0/-home-user-riemann/8aa2c694-669d-5c54-ab29-9ac46b683161/scratchpad/tail/`:

| file | purpose |
|---|---|
| `core.py` | $\Phi$ (repo's evaluator, verbatim), closed-form $\Phi^{(k)}$, $\Xi$, panel-aligned $E_j$, asymptotic $E_j$ |
| `sanity.py` | derivative and $\Xi$-normalization checks, $\Phi''$ sign scan |
| `pilot.py` | pilot, $\alpha=1$, $j\le16$ |
| `full.py` → `full.out`, `full.json` | main sweep: $\alpha\in\{1.0,0.7,0.5,0.4\}$, $j=1..40$ |
| `check.py` → `check.out` | Route A vs Route B; dps 50 vs 90 |
| `downstream.py` → `downstream.out` | tables (a), (b), onset index, $\Phi''$ scan |
| `fit.py` | exponent fits, reproduction of L-16005's (iv) values |
| `offlattice.py` | the discriminating off-lattice test |

**Cost:** pilot 9.3 s; full sweep ≈ 6 min; everything ≈ 12 min single-threaded.

**Remaining uncertainty, stated plainly.**

- No computation here is `CERTIFIED`. `mpmath.quad` is adaptive and non-rigorous.
  My confidence rests on two *independent* routes (one of which never touches
  the tail integral and instead uses `mpmath`'s `zeta`/`gamma`) agreeing to
  38–50 digits, and on the measured values matching a closed-form asymptotic
  derived independently. That is strong but it is not a certificate.
- $\Phi''>0$ on $(T,\infty)$ is a **grid observation on $[0.30,5.00]$**, not a
  proof. The rigorous $O(j^{-2})$ bound of §2.8 depends on it. The asymptotic of
  §2.5 does not.
- The $\alpha=0.3$ onset index is reported as "$>120$" because I stopped the scan
  at $j=120$; the trend $\omega_j\approx3\lambda$ predicts $j\approx280$.
- I did not re-examine item (vi)'s smooth-cutoff numbers (see §7.7).
- The asymptotic series of §2.4 is asymptotic, not convergent; the two-term
  truncation is what I verified, and it matches to 4–5 digits at $\alpha=1$, $j\ge10$.
