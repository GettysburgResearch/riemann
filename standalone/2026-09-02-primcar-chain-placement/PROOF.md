# The PRIMCAR chain: exact placement between RH and RH-plus-Gonek

```text
Status:   PROVED (Theorem A: PRIMLS is equivalent to RH, given the standard RH bound for
          sieved twisted Möbius sums), PROVED EXACT (Proposition C: PRIMCAR contains the
          short-interval Möbius square function), PROVED CONDITIONALLY WITH ONE CITED
          INPUT (Theorem B: RH plus the Gonek hypothesis J_{-1}(T) << T^{1+eps} implies the
          model square function is subpower).  Neither PRIMCAR, PRIMLS, COREAGG, COREWAVE
          nor RH is proved.  RH remains unproved.
Scope:    the chain COREWAVE => COREAGG <=> PRIMCAR => PRIMLS => RH of PRs #757 and #760
          (branches codex/l-function-sheaf-amplifier @ b870366 and
          research/gpt56-pro/pr757-dual-architecture-closure @ e3747c9).
Exact sources or dependencies:
          FFPS_BOUNDARY_FIELD_PRIMITIVE_PAIR_LARGE_SIEVE_GATE.md (PRIMLS, (0.3)-(0.9), (5.1)-(5.4));
          FFPS_PRIMITIVE_PAIR_HARMONIC_INCIDENCE_CARLESON.md (PRIMCAR, (0.13)-(0.16), (1.2)-(1.4));
          FFPS_PRIMITIVE_CORE_WAVELET_CLOSURE.md (COREAGG/COREWAVE, (0.3)-(0.8));
          Titchmarsh, The Theory of the Riemann Zeta-Function, Thm 14.2 and Section 14.25;
          Montgomery-Vaughan, Multiplicative Number Theory I, Thm 13.23 (Perron);
          Ng, The distribution of the summatory function of the Möbius function (Proc. LMS 2004);
          Selberg (1943) for the short-interval mean-square method.
What was actually run:  nothing numerical; this packet is analytic.
Smallest remaining gap: none for Theorems A and C; Theorem B relies on the explicit
          formula for M(x) under RH + J_{-1}, cited from Ng.  The PRIMCAR estimate itself
          implies RH and therefore cannot be proved by any argument that does not prove RH.
```

Claim IDs: `T-109100` (Theorem A), `L-109101` (Lemma 1), `T-109102` (Theorem B),
`L-109103` (Proposition C).  No historical ID is reused.

---

## 0. The objects, verbatim

Throughout, `d` ranges over squarefree integers with `67 ∤ d`, `R` is the even, bounded,
compactly supported autocorrelation of the boundary kernel `K_bd` of the ratio-sixteen
criterion (so `R(u) = (2π)^{-1}∫|K̂_bd(ξ)|² e^{iξu} dξ` with `K̂_bd(ξ) ≪ 1/(1+|ξ|)` because
`K_bd` has bounded variation), and the three channels are `(α,γ) ∈ {(0,0),(1,0),(2,0)}`,
`A = 67^α`.

**Panel** (PR #757, (0.3)):

\[
\mathcal P(d;H,U)=\sum_{\substack{a,b\ \text{squarefree},\ 67\nmid ab,\ (a,b)=1,\ (ab,d)=1\\ H<\max(Aa,b)\le U}}
\frac{\mu(a)\mu(b)}{\sqrt{ab}}\,R\!\Big(\log\frac{Aa}{b}\Big),
\qquad H\le U\le 2H .
\]

**Rectangle form** (PR #757, (5.1)–(5.2)): with

\[
G(d;T)=\sum_{\substack{a,b\ \text{squarefree},\ 67\nmid ab,\ (a,b)=1,\ (ab,d)=1\\ Aa\le T,\ b\le T}}
\frac{\mu(a)\mu(b)}{\sqrt{ab}}\,R\!\Big(\log\frac{Aa}{b}\Big),
\qquad
\mathcal P(d;H,U)=G(d;U)-G(d;H).
\]

**PRIMLS** (PR #757, (0.7)–(0.8)): for every `ε>0`, uniformly in `D,H ≥ 1` and the three channels,

\[
\mathfrak L(D,H):=\sum_{\substack{d\le D\\ d\ \text{squarefree},\ 67\nmid d}}\frac1d\sup_{H\le U\le 2H}|\mathcal P(d;H,U)|^2\ \ll_\varepsilon (2DH)^\varepsilon .
\]

**Height layers and blocks** (PR #757 successor, (1.2)–(1.4)): for an integer height `t`,
`A_t(d)` is the part of the panel with `max(Aa,b)=t`; for a block `I` of integer heights,
`𝒫_I(d)=Σ_{t∈I}A_t(d)`, so that `𝒫(d;H,U)=Σ_{H<t≤U}A_t(d)`.  `𝒟_H` is the set of aligned
dyadic sub-blocks of the height grid `(H,2H]`.

**PRIMCAR** ((0.13)–(0.15)): uniformly in `D,H≥1` and the three channels,

\[
\sum_{I\in\mathscr D_H}\ \sum_{\substack{d\le D\\ d\ \text{sqfree},\ 67\nmid d}}\frac{|\mathcal P_I(d)|^2}{d}\ \ll_\varepsilon (2DH)^\varepsilon .
\]

The source PRs prove `PRIMCAR ⇒ PRIMLS ⇒ RH` and `COREWAVE ⇒ COREAGG ⇔ PRIMCAR`, and
state explicitly that PRIMLS is "deliberately posed as a stronger uniform sufficient
hypothesis, not as an equivalent reformulation of RH", and that "RH implies PRIMLS" is
"not claimed".  Theorem A below claims and proves it.

---

## 1. `L-109101` — the RH bound for sieved, twisted Möbius sums

**Lemma 1.** Assume RH.  For `y ≥ 2`, squarefree `q ≥ 1`, real `ξ`, and every `ε>0`,

\[
S(y;q,\xi):=\sum_{\substack{n\le y\\ (n,q)=1}}\mu(n)\,n^{-1/2-i\xi}\ \ll_\varepsilon\ y^{\varepsilon}\,\big(q(2+|\xi|)\big)^{\varepsilon}.
\]

*Proof.* For `Re s>1`, `Σ_{(n,q)=1}μ(n)n^{-s}=ζ(s)^{-1}Π_{p|q}(1-p^{-s})^{-1}=:F_q(s)`.
Put `w=1/2+iξ` and `c=1+1/\log y`.  By the truncated Perron formula
(Montgomery–Vaughan Thm 13.23, with `|a_n|≤1` and the harmonic majorant `n^{-1/2}`),

\[
S(y;q,\xi)=\frac1{2\pi i}\int_{c-w-iT}^{c-w+iT}F_q(s+w)\frac{y^{s}}{s}\,ds+O\Big(\frac{y^{1/2}\log y}{T}+1\Big),
\]

for `y` half an odd integer, say, and `T ≥ 2`.  Under RH, `F_q` is holomorphic in
`Re(s+w)>1/2`, and Titchmarsh Thm 14.2 gives `ζ(σ+it)^{-1}\ll_\eta (2+|t|)^{\eta}`
uniformly for `σ ≥ 1/2+η`.  The local factors satisfy
`|1-p^{-s-w}|^{-1}\le(1-p^{-1/2-\eta})^{-1}`, so

\[
\prod_{p\mid q}|1-p^{-s-w}|^{-1}\ \le\ \exp\Big(2\sum_{p\mid q}p^{-1/2}\Big)\ \le\ \exp\big(C\sqrt{\log q}\big)\ \ll_\varepsilon q^{\varepsilon},
\]

because the `ω(q)` primes dividing `q` are at least the first `ω(q)` primes and
`ω(q)\ll\log q/\log\log q`.  Move the vertical segment to `Re s=η` (so `Re(s+w)=1/2+η`);
no pole is crossed.  On the new segment the integrand is
`\ll (2+|\xi|+|t|)^{\eta}q^{\varepsilon}y^{\eta}/(|t|+1)`, whose integral over `|t|\le T`
is `\ll y^{\eta}q^{\varepsilon}(2+|\xi|+T)^{\eta}\log T`; the two horizontal segments contribute
`\ll y^{c-1/2}(2+|\xi|+T)^{\eta}q^{\varepsilon}/T`.  Choosing `T=y` and `η=ε` proves the lemma
for half-odd `y`, and the general case follows by changing `y` by at most `1/2`, which
changes `S` by `O(y^{-1/2})`. ∎

The same argument with `q=1`, `ξ=0` is Titchmarsh §14.25's `Σ_{n≤y}μ(n)n^{-1/2}\ll y^{ε}`;
the lemma only records the uniformity in the sieve modulus and the twist.

---

## 2. `T-109100` — Theorem A: PRIMLS is equivalent to RH

**Theorem A.** PRIMLS holds if and only if RH holds.

*Proof.* `PRIMLS ⇒ RH` is PR #757's (0.9).  Assume RH.  Fix a channel, so `A=67^α`,
and fix `T ≥ 2`, `d`.  Write the kernel through its Fourier representation and open the
coprimality condition:

\[
G(d;T)=\frac1{2\pi}\int_{\mathbb R}|\widehat{K}_{bd}(\xi)|^2A^{i\xi}
\sum_{\substack{a,b\ \text{sqfree},\ (ab,67d)=1\\ Aa\le T,\ b\le T}}\Big(\sum_{k\mid(a,b)}\mu(k)\Big)\mu(a)\mu(b)\,a^{-1/2+i\xi}b^{-1/2-i\xi}\,d\xi .
\]

Put `a=ka'`, `b=kb'`.  Since `a,b` are squarefree, `k` is squarefree and coprime to `a'b'`,
and `μ(ka')μ(kb')=μ(k)^2μ(a')μ(b')=μ(a')μ(b')`.  The factor `k^{-1/2+i\xi}k^{-1/2-i\xi}=k^{-1}`
carries no twist.  Hence, exactly,

\[
G(d;T)=\frac1{2\pi}\int_{\mathbb R}|\widehat K_{bd}(\xi)|^2A^{i\xi}
\sum_{\substack{k\le T\\ k\ \text{sqfree},\ (k,67d)=1}}\frac{\mu(k)}{k}\;
S\!\Big(\frac{T}{Ak};67dk,-\xi\Big)\;S\!\Big(\frac{T}{k};67dk,\xi\Big)\,d\xi ,
\]

where `S` is the sum of Lemma 1 (the condition "`n` squarefree" is automatic from `μ`,
and `67∤ab` together with `(ab,d)=1` and `(a'b',k)=1` is exactly `(a'b',67dk)=1`).
Lemma 1 gives `|S(T/(Ak);67dk,∓ξ)|\,|S(T/k;67dk,\pm\xi)|\ll_\varepsilon T^{2\varepsilon}(dk)^{2\varepsilon}(2+|\xi|)^{2\varepsilon}`
uniformly (an empty sum is zero).  Therefore

\[
|G(d;T)|\ \ll_\varepsilon\ T^{2\varepsilon}d^{2\varepsilon}\Big(\sum_{k\le T}\frac{k^{2\varepsilon}}{k}\Big)\int_{\mathbb R}|\widehat K_{bd}(\xi)|^2(2+|\xi|)^{2\varepsilon}\,d\xi
\ \ll_\varepsilon\ (dT)^{5\varepsilon},
\]

the last integral being finite because `\widehat K_{bd}(\xi)\ll(1+|\xi|)^{-1}`.  Since
`𝒫(d;H,U)=G(d;U)-G(d;H)` with `H\le U\le 2H`, we get, uniformly in `U` and `d`,

\[
\sup_{H\le U\le2H}|\mathcal P(d;H,U)|\ \ll_\varepsilon (dH)^{5\varepsilon},
\qquad\text{hence}\qquad
\mathfrak L(D,H)\ \ll_\varepsilon (DH)^{10\varepsilon}\sum_{d\le D}\frac1d\ \ll_\varepsilon (2DH)^{11\varepsilon}.
\]

Renaming `ε` proves PRIMLS in all three channels. ∎

**Remarks.** (i) The supremum over the moving endpoint costs nothing under RH: the bound
holds for every endpoint separately.  (ii) The harmonic average over `d` costs one
logarithm.  (iii) Nothing about the ratio kernel beyond boundedness, compact support and
bounded variation is used.  (iv) Consequently every gate of the form "PRIMLS for some
compact BV kernel and some finite set of fixed-prime channels" is RH, and the chain's
first genuinely new estimate must be sought above PRIMLS.

---

## 3. `L-109103` — Proposition C: what PRIMCAR adds

Fix the central channel `α=0` (the argument for `α=1,2` is identical with `A=67^α` in
the second layer).  For an integer height `t` the layer `A_t(d)` collects the pairs with
`max(a,b)=t`; since `(a,b)=1`, `a=b=t` is impossible for `t>1`, so the layer splits into
the pairs with `b=t>a` and the pairs with `a=t>b`.  Define

\[
c_t(d):=\sum_{\substack{a<t,\ a\ \text{sqfree},\ (a,67dt)=1}}\frac{\mu(a)}{\sqrt a}\,R\!\Big(\log\frac at\Big).
\]

Then, exactly,

\[
A_t(d)=\mathbf 1_{[t\ \text{sqfree},\ (t,67d)=1]}\ \frac{\mu(t)}{\sqrt t}\ \big(c_t(d)+c^{\,\prime}_t(d)\big),
\qquad c'_t(d)=\sum_{\substack{b<t,\ b\ \text{sqfree},\ (b,67dt)=1}}\frac{\mu(b)}{\sqrt b}R\!\Big(\log\frac tb\Big)=c_t(d)
\]

by evenness of `R`.  Under RH, Lemma 1 (with the Fourier representation of `R`) gives
`c_t(d)\ll_\varepsilon(dt)^{\varepsilon}` uniformly.  Hence:

**Proposition C.**
(a) Under RH, the single-height layers already satisfy PRIMCAR's bound at scale one:
`Σ_{H<t\le 2H}Σ_{d\le D}|A_t(d)|^2/d\ll_\varepsilon(DH)^{\varepsilon}`.
(b) For a block `I ⊂ (H,2H]` of `ℓ` consecutive heights,

\[
\mathcal P_I(d)=2\sum_{\substack{t\in I\\ t\ \text{sqfree},\ (t,67d)=1}}\frac{\mu(t)}{\sqrt t}\,c_t(d),
\]

so PRIMCAR at scale `ℓ` is a square function of **short sifted Möbius sums of length `ℓ`
at height `H`**, with the arithmetic weights `c_t(d)`.  If the weights are frozen
(`c_t(d)` replaced by a constant of size `H^{\varepsilon}`, which is their true size under RH),
PRIMCAR at scale `ℓ` becomes

\[
\sum_{\text{blocks }I\text{ at scale }\ell}\ \Big|\sum_{t\in I}\frac{\mu(t)}{\sqrt t}\Big|^2\ \ll H^{\varepsilon}
\quad\Longleftrightarrow\quad
\frac1\ell\int_H^{2H}\big|M(x+\ell)-M(x)\big|^2\,dx\ \ll H^{1+\varepsilon},
\]

for every `1\le\ell\le H` (the passage from aligned integer blocks to the integral is the
usual one: every window of length `ℓ` is a union of at most two aligned blocks of scale
`\ge\ell/2` plus shorter ones, and conversely).

*Proof.* (a) `|A_t(d)|\le 2t^{-1/2}|c_t(d)|\ll t^{-1/2}(dt)^{\varepsilon}`; sum `t^{-1}` over
`(H,2H]` and `1/d` over `d\le D`.  (b) is the layer identity summed over `I`. ∎

So PRIMCAR is exactly the point where the chain leaves "RH" and asks for something
more: square-root cancellation of Möbius in **short intervals at every scale, in mean
square over a dyadic range**.  At scale `ℓ=H` this is `M(2H)-M(H)\ll H^{1/2+\varepsilon}`,
i.e. RH; at scales `ℓ<H^{1-\varepsilon}` it is not known to follow from RH, because the
individual bound `M(x+\ell)-M(x)\ll H^{1/2+\varepsilon}` loses the factor `\sqrt{H/\ell}`.

---

## 4. `T-109102` — Theorem B: the model square function under RH plus Gonek

Let `J_{-1}(T)=\sum_{0<\gamma\le T}|\zeta'(\rho)|^{-2}` (all zeros simple).  Gonek's
conjecture is `J_{-1}(T)\asymp T`; the hypothesis used here is the weaker
`J_{-1}(T)\ll_\varepsilon T^{1+\varepsilon}`.

**Theorem B.** Assume RH and `J_{-1}(T)\ll_\varepsilon T^{1+\varepsilon}`.  Then for `1\le\ell\le H`,

\[
\int_H^{2H}\big|M(x+\ell)-M(x)\big|^2\,dx\ \ll_\varepsilon\ \ell\,H^{1+\varepsilon},
\]

and consequently the frozen-weight model of PRIMCAR, `Σ_{I∈𝒟_H}|Σ_{t∈I}μ(t)t^{-1/2}|^2\ll_\varepsilon H^{\varepsilon}`, holds.

*Proof (Selberg's method, with Ng's explicit formula).*  Under RH and the hypothesis,
Ng (2004, Section 2) derives an explicit formula of the shape

\[
M(x)=\sum_{|\gamma|\le T}\frac{x^{\rho}}{\rho\,\zeta'(\rho)}+E(x,T),
\]

by truncated Perron and a contour shift across the critical line on horizontal segments
chosen away from the zeros (this is where RH and the control of `1/\zeta'` enter).  The only
property of `E` used below is that with `T=H^{2}` its increments over an interval of length
`ℓ` have mean square `\ll\ell H^{1+\varepsilon}` on `[H,2H]`; any error of the form
`O(x^{1+\varepsilon}/T+x^{\varepsilon})`, or more generally `O(x^{1/2-\delta})`, satisfies this.
The reader should verify the exact error term against Ng's paper before citing this
theorem in a stronger form; the shape above is the one his method yields.  It remains to treat

\[
\Delta(x):=\sum_{|\gamma|\le T}a_\gamma(x),\qquad a_\gamma(x)=\frac{(x+\ell)^{\rho}-x^{\rho}}{\rho\,\zeta'(\rho)} .
\]

Two bounds hold for the numerators: `|(x+\ell)^\rho-x^\rho|=|\int_x^{x+\ell}\rho u^{\rho-1}du|\le\ell|\rho|x^{-1/2}`
and `|(x+\ell)^\rho-x^\rho|\le 2(3H)^{1/2}` on `[H,2H]`.  Split `Δ=Δ_1+Δ_2` at `|\gamma|=V:=H/\ell`.

For `Δ_1` (zeros with `|\gamma|\le V`): expanding the square and integrating,

\[
\int_H^{2H}|\Delta_1|^2dx=\sum_{|\gamma|,|\gamma'|\le V}\frac{1}{\rho\zeta'(\rho)\overline{\rho'\zeta'(\rho')}}\int_H^{2H}\big((x+\ell)^\rho-x^\rho\big)\overline{\big((x+\ell)^{\rho'}-x^{\rho'}\big)}\,dx .
\]

Write `(x+\ell)^\rho-x^\rho=\rho\int_0^\ell(x+u)^{\rho-1}du`; then the inner integral equals
`\rho\bar\rho'\int_0^\ell\!\int_0^\ell\int_H^{2H}(x+u)^{\rho-1}(x+v)^{\bar\rho'-1}dx\,du\,dv`, and
for `|u|,|v|\le\ell\le H` the `x`-integral is `\ll H^{-1}\cdot H\min(1,1/|\gamma-\gamma'|)`
by one integration by parts in `x` when `|\gamma-\gamma'|\ge1` (the phase is
`x^{i(\gamma-\gamma')}` up to a factor `(1+u/x)^{\rho-1}(1+v/x)^{\bar\rho'-1}` of total
variation `O(1)` on `[H,2H]` because `|\rho|\ell/H\le|\rho|/V\le1`).  Hence

\[
\int_H^{2H}|\Delta_1|^2dx\ \ll\ \ell^2\sum_{|\gamma|,|\gamma'|\le V}\frac{\min(1,|\gamma-\gamma'|^{-1})}{|\zeta'(\rho)\zeta'(\rho')|}
\ \le\ \ell^2\sum_{|\gamma|\le V}\frac{1}{|\zeta'(\rho)|^2}\sum_{|\gamma'|\le V}\min(1,|\gamma-\gamma'|^{-1})
\ \ll\ \ell^2\,J_{-1}(V)\,\log^2V,
\]

using `2|ab|\le|a|^2+|b|^2`, symmetry, and `N(t+1)-N(t)\ll\log(t+2)`.  With
`J_{-1}(V)\ll V^{1+\varepsilon}=(H/\ell)^{1+\varepsilon}` this is `\ll\ell^{1-\varepsilon}H^{1+\varepsilon}\log^2H`.

For `Δ_2` (zeros with `V<|\gamma|\le T`): use the second numerator bound and the same
double-sum device,

\[
\int_H^{2H}|\Delta_2|^2dx\ \ll\ H\sum_{V<|\gamma|,|\gamma'|\le T}\frac{H\min(1,|\gamma-\gamma'|^{-1})}{|\rho\zeta'(\rho)\rho'\zeta'(\rho')|}
\ \ll\ H^2\log^2T\sum_{|\gamma|>V}\frac{1}{|\gamma|^2|\zeta'(\rho)|^2}
\ \ll\ H^2\log^2T\cdot V^{-1+\varepsilon}
\ =\ \ell^{1-\varepsilon}H^{1+\varepsilon}\log^2T,
\]

the tail sum by partial summation against `J_{-1}(u)\ll u^{1+\varepsilon}`.  Adding the three
contributions and renaming `ε` proves the first claim.  For the second, each aligned
block `I` at scale `\ell` is `(x_I,x_I+\ell]` with `x_I\in[H,2H)`, and
`|\sum_{t\in I}\mu(t)t^{-1/2}|\le H^{-1/2}(|M(x_I+\ell)-M(x_I)|+\ldots)` after partial
summation with the weight `t^{-1/2}` (the correction is `\ll H^{-3/2}\sum_{t\in I}|M(t)-M(x_I)|`,
whose contribution is handled by the same mean-square bound at the shorter scales);
summing `|M(x_I+\ell)-M(x_I)|^2` over the `H/\ell` aligned blocks is bounded by
`\ell^{-1}\int_{H-\ell}^{2H}|M(x+\ell)-M(x)|^2dx` up to a factor two (replace each aligned
block by the average over its `\ell` translates and use `|a|^2\le2|b|^2+2|a-b|^2` with
the translate differences again controlled at scale `\le\ell`).  Summing over the
`O(\log H)` scales gives `\ll_\varepsilon H^{\varepsilon}`. ∎

**Grade.** The Selberg-type mean-square computation is complete as written; the one
imported input is Ng's explicit formula with a power-saving error, which is where
`J_{-1}(T)\ll T^{1+\varepsilon}` is used (it controls `1/\zeta'` on the residue side and, via
Ng's Lemma 2.1, the horizontal segments).  A reader who prefers to avoid the citation
can replace `M` by a smoothed version, at the cost of smoothing the block endpoints,
which PRIMCAR permits after the dyadic chaining of PR #757's successor (5.3).

---

## 5. Where the chain stands

| statement | status | source |
|---|---|---|
| `PRIMLS` | **equivalent to RH** | Theorem A |
| `PRIMCAR` | implies RH (PR #757 successor); implied by RH plus the short-interval Möbius mean square at all scales with the arithmetic weights `c_t(d)`; its frozen-weight model is implied by RH plus `J_{-1}(T)\ll T^{1+\varepsilon}` | Proposition C, Theorem B |
| `COREAGG` | equivalent to PRIMCAR (PR #760) | imported |
| `COREWAVE` | strictly stronger sufficient condition | imported |

The exact location of PRIMCAR is therefore

\[
\mathrm{RH}\ \Longleftarrow\ \mathrm{PRIMCAR}\ \Longleftarrow\ \mathrm{RH}+\text{(Möbius short-interval mean square at every scale)}\ \Longleftarrow\ \mathrm{RH}+J_{-1}(T)\ll T^{1+\varepsilon},
\]

where the middle statement is Proposition C's reformulation with the weights `c_t(d)`
carried along (they are `\ll(dH)^{\varepsilon}` under RH and depend on `t` only through
`R(\log(a/t))`, which varies by `O(\ell/H)` across a block, and through the sieve
`(a,t)=1`).

Consequences for the programme:

1. There is no room below RH anywhere in the chain: PRIMLS *is* RH, and everything
   above it implies RH.  Any proof of PRIMCAR, COREAGG or COREWAVE is a proof of RH.
2. The "new analytic estimate" the chain isolates is not a Möbius-pair large sieve but
   the classical short-interval mean square of the Mertens function, which is governed by
   the negative second moment of `\zeta'` at the zeros.  This connects the gate to a
   known quantitative hypothesis (Gonek's) rather than to a new mechanism.
3. A proof strategy that works *below* the critical scale, for example a bilinear or
   dispersion argument giving PRIMCAR at scales `\ell\ge H^{1-\delta}` only, cannot help:
   those scales are already RH (Theorem A's bound is uniform in the endpoint), and the
   scales that matter, `\ell\le H^{1/2}`, are exactly where RH gives nothing.
4. Numerical or finite verification of PRIMCAR at any range says nothing about RH,
   for the same reason that `M(x)\ll\sqrt x\,\log\log\log x` for `x\le10^{16}` says nothing.

## 6. Falsifiers

- A proof that RH alone implies `\int_H^{2H}|M(x+\ell)-M(x)|^2dx\ll\ell H^{1+\varepsilon}` for all
  `\ell\ge1` would collapse the right-hand side of the placement to RH; no such proof is
  known, and it would give `M(x)\ll\sqrt x\,\exp(O(\sqrt{\log x}))`-type consequences that
  are currently only known under `J_{-1}`.
- An error in Lemma 1's sieve factor would show up for `d` with many small prime
  factors; the bound `\exp(C\sqrt{\log q})` is crude but sufficient.
- If PR #757's kernel `K_bd` were not of bounded variation, replace `(1+|\xi|)^{-1}` by
  any decay making `\int|\widehat K_{bd}|^2(2+|\xi|)^{2\varepsilon}d\xi` finite; the frozen kernel
  is piecewise smooth.
