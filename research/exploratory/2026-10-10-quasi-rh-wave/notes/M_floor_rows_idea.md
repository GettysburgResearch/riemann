# Note M (lead, draft): the floor wall is a diagonal, and a mollified first moment might subtract it

```text
Status: PROPOSED (idea, not a proof; the cost/benefit is unresolved — see Section 4)
Scope: the floor bin of Part II (rows whose twist has no zero above 51/100), at frequency U = Z^h
Exact sources: qrh_main.txt Lemma 10.4 (triangle inequality over rows), Lemma 20.1 and eq. (20.5) (floor exponent), Lemma 7.1/eq. (7.13) (row structure zeta_F(6z) L(w,chi_u)/L(x,eta chi_u) H), Prop 8.3 (truncated inverse); notes A, E (floor constraint C0 <= 0)
What was actually run: nothing (a heuristic diagonal computation)
Smallest remaining gap: whether the approximation 1/L ≈ truncated Möbius polynomial on floor rows can be made uniform at a contour close enough to Re x = a that the Mellin cost does not eat the first-moment saving
```

## 1. Why the wall is a diagonal

Lemma 10.4 bounds a bin of rows by the triangle inequality and a count; for the floor bin the count is the trivial $U^1$ (§10.5: "uses no witness"). Notes A and E show that this single estimate, with ideal zero counts for every other class, pins the architecture at $13/15$ ($0.8698$–$0.87236$ with the side constraints). Under GRH for the family *every* row is a floor row, so the statement is: **even with GRH for all twists as an input, the bookkeeping cannot go below $\approx0.87$.**

Is the trivial bound sharp? Expand the row integrand's Dirichlet series formally: $\sum_u\sum_{n,m}\mu(m)\eta(m)\chi_n(u)\chi_m(u)\,n^{-w}m^{-x}W(u/U)$. The $u$-sum picks out $nm\in(F^\times)^6$ (sixth-power-free $u$, orthogonality), giving a diagonal main term
$$U\cdot\sum_{m\ \mathrm{sf}}\mu(m)\eta(m)m^{w-x}\sum_{\mathrm{rad}(m)\mid k}k^{-6w}\ \approx\ U\cdot\frac{\zeta_F(6w)}{L(x+5w,\eta)}\times(\text{local factors}).$$
On the floor contours ($\Re w\approx1/2$, $\Re x\approx1/2$) this is $U\times O(1)$: exactly the size of the trivial bound. So the floor wall is not an artifact of a lossy inequality; it is the **diagonal** of the sum over rows. But the diagonal is an explicit, holomorphic function of $(x,w,z)$ with $1/L$ evaluated at $\Re(x+5w)\approx3$, far inside the zero-free region. Proposition 2.1 only needs the *difference* between the probe and a holomorphic signal to be small: a term that is holomorphic on $\Re s>\sigma_0$ can be **absorbed into the signal** $f_\eta$ instead of being bounded. What remains of the floor rows after subtracting the diagonal is the off-diagonal, which has genuine cancellation (the Poisson dual in $u$ carries Gauss sums).

## 2. The proposal

For floor rows, replace $1/L(x,\eta\chi_\bullet(u))$ by the truncated Möbius polynomial $M_r(u)$ (valid with small error precisely because these twists are zero-free above $a$ in the height window; this is the identity $J=1+o(1)$ of Prop. 8.3 read backwards), so that
$$\sum_{u\ \mathrm{floor}}\mathrm{Row}_u\ \approx\ \int\!\!\int\!\!\int(\text{Mellin weights})\,\zeta_F^S(6z)\sum_{u}L^S(w,\chi_\bullet(u))\,M_r(x;u)\,H_{\eta,u}\,,$$
a **mollified first moment** of the sextic Kummer family with a long mollifier. Its diagonal is the explicit term above (absorbed into the signal); its off-diagonal is bounded by Poisson in $u$ (Section 17's two masked transforms) and the reflected energy. If the off-diagonal saves $U^{-f}$ over the trivial $U^1$, the dial table (note E §3; note A) gives $f=0.1\Rightarrow B\approx0.857$ with the current counts and $0.8485$ with ideal counts; $f=1/4\Rightarrow0.81$; $f=7/18$ with ideal counts $\Rightarrow3/4$. For comparison, the untwisted first moment of cubic Hecke $L$-functions has error $X^{13/18+\epsilon}$ (Diaconu–Ion–Paşol–Popa Theorem B, $r=3$), a saving of $5/18$; twisted versions lose with the twist length.

## 3. Why this is not circular

Writing $\sum_{\text{all }u\ne1}\mathrm{Row}_u=J-P$ and then "bounding" the floor rows through $J$ is circular ($P$ is the unknown). The proposal instead bounds the floor rows by an **independent mean value** (a first moment of $L$-values against a Möbius polynomial), whose off-diagonal is a different object from $J$ even though it is estimated with the same tools (Poisson in $u$, Gauss sums, cubic reflection, quadratic sieve).

## 4. The unresolved cost

The approximation $1/L(x,\psi)\approx M_r(x;\psi)$ on a zero-free-above-$a$ row has error $\ll U^{-r(\Re x-a)+\epsilon}$; the paper's contour $\Re x=a+16e$ is deliberately as close to $a$ as possible, where the error is $U^{-16er}$, i.e. no saving. Moving the floor contour right by $\eta$ makes the truncation accurate ($U^{-r\eta}$) but costs $Z^{\eta(1-l_y+d/2)}$ in the row exponent (the coefficient of $a$ in eq. (20.4)); the net gain is $f h-\eta(1-l_y+h/2)$ with $f$ the first-moment saving at mollifier length $r$ and contour $\Re x=a+\eta$. Whether this is positive for some $(r,\eta)$ is the question a dedicated analysis must answer (it was not answered in this wave). A second difficulty: the floor bin is defined by a height-window zero-free condition, which is not a condition one can average over directly; one must average over *all* rows and subtract the zero rows (already counted) — this is fine for upper bounds since the zero rows are a thin set whose contribution is bounded separately.

## 5. First-order cost/benefit (lead, 16:30; being checked by note N)

Use eq. (10.15) at $d=h$: the contour parameter $a$ enters $E$ with coefficient $(1-l_y)$ directly and through $\delta/2=a-1/2$ in the reflected-numerator bound $U^{\delta/2}$ with coefficient $d$. Placing the floor contour at $\Re x=a_0+\eta$ therefore costs
$$\eta\,(1-l_y+h)=\eta\Big(1-\tfrac{23}{48}+\tfrac{13}{16}\Big)=\tfrac43\,\eta$$
in the row exponent, while the mollified-first-moment gain is at most $h\cdot\min(f,\,r\eta)\le\tfrac{13}{16}\,r\eta\le\tfrac{13}{16}\,\eta$ for a mollifier of length $r\le1$ (the truncation error of $M_r$ on a row that is zero-free above $a_0$ is $U^{-r(\Re x-a_0)+\epsilon}$). Since $4/3>13/16$, **the net change is positive (worse) for every $\eta>0$ and $r\le1$: the proposal fails at first order.** At $\eta=0$ the truncation is not an approximation at all (the detector's identity $J=1+o(1)$ says the truncated inverse differs from $1/L$ by $O(1)$ on the paper's contour), so the only way to use $M_r$ is to pay $\eta$. Escapes that would have to be examined: a truncation error better than $U^{-r\eta}$ from the zero-free *rectangle* (height $2T_1$) rather than half-plane; a mollifier longer than the family ($r>1.64$, outside every mean-value lemma); or subtracting the diagonal exactly at the level of the Poisson identity before any contour is moved. If none works, the floor wall is intrinsic to any architecture that bounds rows individually behind a zero detector, because the floor rows' total is the diagonal of the row sum and the diagonal is only separable where $1/L$ expands, i.e. right of the line where the signal is largest.
