# Note E (lead): the Part II exponent bookkeeping, independently reconstructed, and what each dial buys

```text
Status: EMPIRICAL (floating-point reconstruction of a published exponent system) / PROPOSED (mechanism reading)
Scope: the exponent comparison of OpenAI 30-Sept-2026 Part II (Sections 19-20) and Liu arXiv:2610.12234
Exact sources: qrh_main.txt eq. (20.4), (20.8), Prop. 19.2, Lemma 20.2; Liu intro eq. (0.1)
What was actually run: scripts/quick_E.py, scripts/dials2.py, scripts/dials3.py (numpy grid search)
Smallest remaining gap: the model omits the supply/contour/small-row side constraints, which are slack at the current optimum but would bind for ell >> 1/5
```

## 1. The endpoint exponent for general lengths

With $l_x=(1-b-\ell)/2$, $l_y=(1+b-\ell)/2$, $h=1-l_x+\ell=(1+b+3\ell)/2$ and target boundary $B(\ell)=11/12-\ell/4$, substituting the geometry into eq. (20.4) of the main paper gives, at the critical frequency $d=h$,

$$E(h;\delta,x)=C_0(b,\ell)+\delta\Big(\tfrac12+\ell\Big)+x\,\delta\,\ell-h\,(1-R_*(\delta,x)),\qquad C_0(b,\ell)=-\tfrac14+\tfrac{5\ell}{4}+\tfrac{b}{6}.$$

Check: $(b,\ell)=(1/8,1/6)$ gives $C_0=-1/48$, $\delta$-coefficient $2/3$, $q$-coefficient $1/6$, exactly eq. (20.4). Here $\delta=2a-1$ is the zero class of the twist (its rightmost zero has real part $a$), $x=q/\delta\in[0,1/2]$ the prime-amplitude ratio, and $R_*$ the row-count exponent of Proposition 19.2 / eq. (20.8) with $\alpha=5/6$ and (after $7/8$ is known) $\kappa=3/4$. The contradiction needs $E(h;\delta,x)\le0$ on $0\le\delta\le5/6$, $0\le x\le1/2$ (plus slack side constraints).

**Numerical check.** At the paper's parameters the maximum of $E$ is $-2.28\times10^{-4}$ (the paper certifies $-E_*\ge49/440640=1.11\times10^{-4}$, consistent). Maximizing $\ell$ subject to $\max E\le0$ returns $b=0.1237$, $\ell=0.16684$, $B=0.874957$, with the active class at $\delta\approx0.389$, $x=1/2$ — Liu's $B_{\rm new}$ and his critical class $\delta_c=(49-\sqrt{921})/48=0.3886$ to all printed digits. So the bookkeeping above is the whole story of the current bound.

## 2. What each input buys (dial table)

| Dial (lemma it represents) | Current | Hypothetical | Best $B$ | Active class |
|---|---|---|---|---|
| none (Liu) | — | — | 0.874957 | $\delta=0.389$, $x=1/2$ |
| $\alpha$: amplification slope of the long inverse moment, Lemma 17.6 (count $1-\alpha+(\alpha-\delta)r$ for $r\ge1$) | 5/6 | 0.75 / 0.70 / 0.60 | 0.874510 / 0.874175 / 0.873284 | same class |
| $c$: plain fourth-moment capacity $z_P=c(1-2m)$, Lemma 18.1 | 2/9 | 0.3 / 0.5 / 1.0 | 0.874789 / 0.874177 / 0.872625 | same class |
| $s_M$: inverse capacity $z_M=s_M(1-r)$, Lemma 17.1 | 1/2 | 0.75 / 1.0 | 0.873053 / 0.872558 | moves to $x=0$ |
| **ideal counts** $R_*=1-\delta$ (density-hypothesis quality for every class, every witness length) | — | — | **13/15 = 0.866667** | **$\delta=0$ (the floor)** |
| generic-row saving $U^{-f}$ on the zero-free (floor) rows, with ideal counts | 0 | 0.1 / 0.25 / 0.389 | 0.8485 / 0.8095 / **3/4** | floor |

Reading: all three moment lemmas together are worth at most about $8\times10^{-3}$; the binding class $a=(1+\delta)/2\approx0.69$ sits well inside the strip, so it is the *zero-density quality of the sextic-twist row counts at real part $\approx0.69$ with maximal prime amplitude* that pins Liu's bound. If every class were counted at density-hypothesis strength ($U^{1-\delta}=U^{2(1-a)}$), the architecture reaches exactly $13/15$ and is then pinned by the **floor**: twists with no zero above $51/100$, counted trivially ($U^1$) and bounded pointwise (Lindelöf-quality after the zero-free disk). The floor constraint is just $C_0\le0$, i.e. $\ell\le\tfrac15-\tfrac{2b}{15}$.

## 3. Where 3/4 would come from

$B(\ell)=11/12-\ell/4$ reaches $3/4$ at $\ell=2/3$. In this bookkeeping that needs a saving of $U^{7/18}$ ($f\ge0.389$) over the trivial sum of generic rows at $d=h$, on top of ideal counts. Nothing in the present proof exploits cancellation *between* different Poisson rows $u$: every nonprincipal row is bounded in absolute value and the rows are counted. A mean-value estimate for $\sum_{u\asymp U}(\text{row}_u)$ that saves a power of $U$ (the rows carry the Gauss-sum phases $\gamma_2$ and the twisted $L$-quotients, so square-root cancellation over $u$ is the natural conjecture) is therefore the single structural input that could move the boundary by more than $10^{-2}$. Formally:

> **Target (PROPOSED).** For the compensated probe of Section 12, and for the floor bin at frequency $U=Z^{h}$, prove $\sum_{u\asymp U,\ u\ \text{floor}}\mathrm{Row}_u(Z)\ll Z^{C(7/8)+C_0-fh+\epsilon}$ with some $f>0$, i.e. a power saving over the absolute-value bound of Lemma 20.1 for the zero-free rows.

Each $0.01$ of $f$ is worth about $0.0025$ in $B$ at the floor (once counts are ideal), and about the same with the current counts (table: $f=0.1$ gives $0.857$ even with the current moments). This is a much larger lever than any moment lemma.

## 4. Caveats

- The model holds the three side constraints of Section 20 fixed (prime supply $\ell/d>7/37$, small-row margin, $\Re z=17/50$ contour); all are slack at the optimum, and the $17/50$ cancels at $d=h$. They would re-enter for $\ell\gtrsim0.3$.
- For $\alpha<\delta_{\max}$ the row-count formula changes branch; the $\alpha$ rows below $0.6$ in the table are outside the model's validity and were discarded.
- All numbers are ordinary floating point: this is reconnaissance, not a certificate.
