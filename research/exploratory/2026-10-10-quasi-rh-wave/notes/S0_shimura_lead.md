# Note S0 (lead): the Shimura-lift Möbius generator — first exponent pass

```text
Status: PROPOSED (lead derivation, 12 Oct; tested numerically in note T; the separate architecture write-up planned as note S was not produced)
Scope: a quadratic-family analogue of the common-signal architecture, Part I level
Exact sources: Shimura (1973) / Kohnen (1980): a_g(dn^2) = a_g(d) sum_{m|n} mu(m) chi_d(m) m^{k-1} lambda_f(n/m); OpenAI Prop. 2.1 (slope-one remark, line ~381-383); Kintali's T_{m,s,eta}(t) (q_c^{-1/2-t} q_n^{-1-3t})
What was actually run: nothing (hand derivation)
Smallest remaining gap: whether any averaging variable can restore slope one in the reciprocal variable (Section 3)
```

## 1. The identity and where the reciprocal sits

For a half-integral weight eigenform $g$ (weight $k+1/2$) with Shimura lift $f$ (weight $2k$), in the analytic normalization $\tilde a(N)=a_g(N)N^{-(k-1/2)/2}$, $\tilde\lambda(n)=\lambda_f(n)n^{-(k-1/2)}$:
$$\sum_{n\ge1}\tilde a(dn^2)\,\eta(n^2)\,n^{-s}=\tilde a(d)\,\frac{L(s,\tilde f\otimes\eta^2)}{L(s+\tfrac12,\chi_d\eta^2)}\qquad(d\ \text{squarefree}).$$
So each squarefree $d$ is a "row" carrying $1/L(\cdot,\chi_d\eta^2)$, the row family $\{\chi_d\eta^2\}$ is closed under quadratic twists (the self-referential bootstrap of Prop. 2.1 applies), the row weights are $\tilde a(d)$ with $|\tilde a(d)|^2\asymp L(1/2,f\times\chi_d)$ (Waldspurger/Kohnen–Zagier), and the row counts could use the perfectly orthogonal quadratic large sieve. For the Cohen–Eisenstein series the lift is Eisenstein and $L(s,\tilde f)=\zeta(s)\zeta(s-1)$-type, so the principal row's $1/\zeta$ **cancels**; a cuspidal $g$ is required. Everything in the notes' classification (Jacobi-sum sign pairings) is bypassed: here Möbius comes from the completion over $n^2$, not from a Gauss-sum sign.

## 2. The slope obstruction

Probe $\tilde P_\eta(Z)=\sum_N\tilde a(N)\eta(N)V(N/Z)$. Direct side: a twisted sum of half-integral weight coefficients, square-root cancellation by Voronoi, exponent $1/2$ in $Z$. Shimura side: $\tilde P_\eta(Z)=\sum_d\tilde a(d)\eta(d)\,\frac1{2\pi i}\int\tilde V(s)(Z/d)^s\frac{L(2s,\tilde f\otimes\eta^2)}{L(2s+1/2,\chi_d\eta^2)}\,ds$. In the reciprocal's own variable $u=2s+1/2$ the principal row ($d=1$) is
$$f_\eta(Z)=\tilde a(1)\frac1{4\pi i}\int Z^{\,u/2-1/4}\,\tilde V\!\Big(\tfrac{u-1/2}2\Big)\frac{L(u-\tfrac12,\tilde f\otimes\eta^2)}{L(u,\eta^2)}\,du,\qquad C(u)=\frac u2-\frac14 .$$
**The signal exponent has slope $1/2$**, because the reciprocal comes from the $n$-variable, which enters the index $N=dn^2$ squared; in the cubic probe the reciprocal comes from the squarefree part $c$ of $A=cn^3$ (via the Hasse–Davenport sign), which enters to the first power, so $x=t+1-z$ has slope one. A zero at $\beta_*$ gives a signal $Z^{\beta_*/2-1/4}\le Z^{1/4}$ against a direct bound $Z^{1/2}$: no contradiction for any $\beta_*\le1$; one would need $\beta_*>3/2$. Equivalently, the balanced quadratic probe can never see a zero.

## 3. What would be needed, and why thin probes are circular

Restricting the probe to $N=dn^2$ with $d\le X$ small makes the direct side thin, but any bound for that thin sum uses the Hecke/Shimura structure (the thin-set indicator $1[n^2\mid N]$ is realized by $T(n^2)$), so it is the Shimura side again — circular. An additional averaging variable (as the cubic probe's $m$ and $s$ averages) acts on the $N$-variable or on a twist, not on the $n$-variable alone, so it rescales both sides equally. The only way to restore slope one is a coefficient structure in which the reciprocal is attached to a variable entering the index linearly — i.e. a *squarefree-part* reciprocal — which is exactly the Hasse–Davenport sign of the sextic/cubic pairing. In that sense the quadratic (N=2) route is closed for a reason different from note C's: not the triviality of Jacobi's theta but the squared variable of the Shimura completion. A Kubota $E^{(2)}(w)$ variant, where the reciprocal sits at $2w-1$ for the same reason, was not written up; note T's data support the slope obstruction.

## 4. Why the extraction tax is intrinsic (bookkeeping remark)

A family mean value bounds an individual member only through Cauchy–Schwarz over the rows on which the member's character is principal (identity rows $u=a^N$, density $H^{1/N}$): $|A_1|^2\le J^{-1}\sum_{\text{identity rows}}|A_u|^2+\text{error}$, and the identity-row mean square is only available through the full-family Lindelöf-quality mean square (the cubic theta), at cost $H^{1-1/N}$. The quadratic large sieve cannot replace it because it excludes exactly the non-squarefree (identity) rows. Hence the sparsity cost $1/(2N)$ at Part I is structural to "family mean value + sparse extraction"; the compensated probe lowers it by $\ell/4$ with $\ell\le1/5$ forced by the direct side. A route past $\approx0.86$ must change the extraction principle, not the lemmas.

## 5. Addendum (after note T's numerics): the $m$-average does not help

Insert the cubic probe's character average $\sum_mW(m/X)\chi_N(m)$ with $\chi_N(m)=(m/D)\mathbf 1_{(m,n)=1}$ for $N=Dn^2$. Direct side by the quadratic large sieve (over squarefree $m$) and Cauchy–Schwarz: $|P|\ll X^{1/2}(X+Z)^{1/2}Z^{1/2+\epsilon}$. Shimura side: the principal row is $X\cdot T_1(Z)\asymp X\,Z^{\beta/2-1/4}$ (the $m$-sum is complete for $D=1$); after Poisson in $m$ the nonprincipal rows total $X^{1/2}\sum_D\tilde a(D)|T_D(Z/D)|$, consistent with the direct bound. The comparison principal versus direct at $X=Z$ is $Z^{\beta/2+3/4}$ against $Z^{3/2}$: a contradiction needs $\beta>3/2$. The extra average multiplies both sides by the same power of $X$ and leaves the $Z$-exponent gap $3/4-\beta/2>0$ untouched. Note T's data say the same thing from the other end: the direct side with a smooth weight is identically zero for $\theta^3$ (and $O(1)$ for the Cohen–Eisenstein series) because $L(s,g\otimes\eta)$ is entire, so the rows' reciprocal poles cancel exactly across rows; a hypothetical off-line zero would give a row of size $Z^{\beta/2}$, never above the sharp-cutoff Voronoi noise $Z^{1/2}$. **The quadratic Shimura route is closed by the slope of its signal, in every arrangement in which the zero-sensitive variable enters the index squared.**
