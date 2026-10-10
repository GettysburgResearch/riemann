# Note H (lead): what a generalized 2k-th moment of the detector witnesses would buy

```text
Status: EMPIRICAL (floating-point model of the Part II row-count system) / PROPOSED (reading)
Scope: the zero detector of Section 8 and the row counts of Proposition 19.2, with hypothetical moment inputs
Exact sources: qrh_main.txt Prop. 8.3 (eq. (8.3)-(8.4)), Lemma 17.1, Lemma 18.1, Prop. 19.2; notes/B_bootstrap_barrier.md (closed-form model with side constraints)
What was actually run: scripts/moment2k_v2.py (grid search; reproduces R*(delta_c,1/2)=0.667 and B=0.87497 at the baseline)
Smallest remaining gap: the model treats a hypothetical moment lemma as an input; whether any such lemma is provable is the subject of note G
```

## 1. How the detector fixes the witness lengths

Proposition 8.3 is the classical truncated-inverse detector: for a row $u$ whose twist has a zero $\rho$ of real part $a=(1+\delta)/2$, the integral $J=\frac1{2\pi i}\int Y_*^z\Gamma(z)L(\rho+z,\psi)C_\psi(\rho+z)\,dz$ with $C_\psi$ the truncated Möbius series of length $D_*=U^t$ equals $1+o(1)$ (the residue at $z=0$ vanishes because $L(\rho,\psi)=0$), and expanding $L\cdot C_\psi$ shows that *some* dyadic pair $(D,N)=(U^r,U^m)$ with $r\le t$, $r+m\ge t$ carries mass $\gg(\log U)^{-2}$. After central normalization this is $|M_rS_m|^2\gg U^{\delta(r+m)-\epsilon}$, and the pointwise bound $|S_m|^2\ll U^{\delta\min(m,1-m)}$ (Hecke reflection) forces $m\le1/2+O(\epsilon)$, hence $r\ge t-1/2$. **The split $(r,m)$ is chosen by the row, not by us**: the count must hold for the worst split in $r\in[t-\tfrac12,\min(t,1)]$, $m=t-r$ (rows with $r>1$ are routed to $L(t)$). Taking $m=t-r$ rather than $m\ge t-r$ is justified because $F_I$ and $F_S$ below are increasing in $r$ and $m$ for $x\le1/2$ (slopes $1-2xc_I\ge1/2$ and $2(1-2xc)\ge14/9$), so a longer witness only improves the count. The detector's range $t\le3/2$ is also without loss: $t>3/2$ is admissible for the $J=o(1)$ bound, but then every split has $r>1$ and $L(t)$ increases in $t$ since $\alpha>\delta$. Each witness can only be used at its own length (the inverse witness has no reflection; a plain witness longer than $1/2$ is reflected to $1-m$).

So the row-count exponent is
$$R_*(\delta,x)=\min_{t\in[1,3/2]}\max\Big\{\max_{r\in[t-1/2,1]}\big(1-\delta\max\{F_I(r),F_S(t-r)\}\big),\ L(t)\Big\},$$
with $F_I(r)=r+2x\,c_I(1-r)$ (Lemma 17.1 with inverse capacity $z\le c_I(1-r)$, $c_I=1/2$), $F_S(m)=2m+2x\,c\,(1-2m)$ (Lemma 18.1, two plain copies, capacity $2m+6\kappa z\le1$, $c=1/(6\kappa)$), and $L(t)=1-\delta+(\alpha-\delta)(t-1)$ for rows with $r\ge1$ (Lemma 17.6, $\alpha=5/6$). At $(\delta_c,x)=(0.3886,1/2)$ this gives $R_*=0.667=2/3$, Liu's value from his (24.1).

## 2. A generalized $2k$-th moment of the plain witness buys nothing

Hypothesis "Lemma 18.1(k)": for $k$ copies, $\sum_u|S_m^kQ|^2\ll U^{1+\epsilon}$ when $km+6\kappa z\le1$, giving $F_S^{(k)}(m)=km+2xc(1-km)$ for $m\le1/k$, and $F_S=\max_k F_S^{(k)}$.

| plain moments available | best $B$ | active class |
|---|---|---|
| $k=2$ only (the paper) | 0.874973 (grid-limited: the $\delta$ step $\approx0.012$ misses the tangency at $\delta_c=0.3886$ where the exact value is 0.874957) | $\delta=0.366$, $x=1/2$, $R_*=0.687$ |
| $k\in\{2,3\}$ | 0.874973 | unchanged |
| $k\in\{2,\dots,8\}$ | 0.874973 | unchanged |
| $k\in\{2,\dots,40\}$ | 0.874973 | unchanged |

Reason: at the binding class the worst split has $m^*\approx0.41\in(1/3,1/2]$, where only $k=2$ is admissible ($3m>1$), and the adversary can always choose such a split. Higher plain moments improve the count only for rows with $m\le1/3$, which are never the worst rows. The same holds for a hypothetical fourth moment of the *inverse* witness with capacity $2r\le1$ (a hypothesis by analogy, not a reading of any lemma): it needs $r\le1/2$, i.e. $t=1$, $r=m=1/2$, where the plain count already gives $1-\delta$. The structural argument ($m^*>1/3$) is what carries the conclusion, not the grid values.

## 3. What does move the bound

| hypothetical input | best $B$ |
|---|---|
| inverse capacity $c_I=1/2\to0.6$ | 0.87399 |
| inverse capacity $c_I\to3/4$ | 0.87329 (active class moves to $\delta\approx0.3$, $x\approx0$) |
| amplification slope $\alpha=5/6\to3/4$ | 0.87451 |
| all classes at density-hypothesis strength $R_*=1-\delta$ | 0.87236 (floor bin binds), then 0.87004 (floor removed), then $13/15$ (direct bound) |

The "generalized moment" that matters is therefore not a higher power of a witness but a **mixed moment**: the second moment of the inverse witness against a *longer* selected-prime product (capacity $z\le c_I(1-r)$ with $c_I>1/2$), or equivalently a large-values inequality for $M_r$ at the spike $V=U^{\delta r/2}$ that beats the mean-value count $U^{1-\delta r}$ when $\delta r\approx0.28$. Both are zero-density-type statements for the sextic Kummer family at real part $\approx0.69$; note G examines whether the Section 17 induction (two masked Poisson transforms) can carry them.
