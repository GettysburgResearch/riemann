# Tensor phase current collapse and the four-adic Hilbert bound

Status: **PROPOSED COMPLETE EXACT ARITHMETIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Scope: finite main-pole-killing tensor phase bank, its source reserve, channel DFT, and coefficient/mean-square operator bounds; no complete Weil floor and no RH claim  
Depends on: PR #325 `L-32415`; ordinary Selberg–Kummer reserve; finite Fourier orthogonality; Montgomery–Vaughan's Dirichlet-polynomial mean-value theorem

## 1. Finite main-pole source and tensor phase bank

Put

\[
a(s)=4^{1-s},
\qquad L=\log4,
\]

and retain the finite Q4 main-pole source

\[
B_\sharp(s)=\frac{1-a(s)}{\zeta(s)},
\qquad
b_\sharp=(\varepsilon-4\delta_4)*\mu.
\tag{TP.1}
\]

PR #325 proves that its inverse/generalized-prime coefficients are positive, every nontrivial zeta-zero pole is retained, and its quarter-balanced Selberg–Kummer reserve

\[
\mathcal R_\sharp=P_\sharp^2-S_\sharp
\]

is strictly positive on every row.

Fix integers `k>=1`, `M>=2`, and let

\[
\boldsymbol\omega=(\omega_1,\ldots,\omega_k)
\in\Omega_M^k.
\]

Define

\[
\boxed{
F_{\boldsymbol\omega}(s)
=\prod_{\ell=1}^k(1-\omega_\ell a(s)),
\qquad
B_{\boldsymbol\omega}=F_{\boldsymbol\omega}B_\sharp.
}
\tag{TP.2}
\]

Every channel remains main-pole killing because the common factor `B_sharp` vanishes at `s=1`.

On the critical line, `|a|=2`, and independent phase averaging gives the exact tensor frame

\[
\boxed{
\frac1{M^k}
\sum_{\boldsymbol\omega\in\Omega_M^k}
|F_{\boldsymbol\omega}(1/2+it)|^2
=5^k.
}
\tag{TP.3}
\]

The frame is a tensor product of `k` one-stage critical frames; no binomial-power conditioning is present.

## 2. Complete source reserve after independent phase separation

Let

\[
\Lambda_{\boldsymbol\omega}
=-A_{\boldsymbol\omega}'/A_{\boldsymbol\omega},
\qquad A_{\boldsymbol\omega}=B_{\boldsymbol\omega}^{-1}.
\]

Finite logarithmic differentiation gives

\[
\boxed{
\Lambda_{\boldsymbol\omega}
=\Lambda_\sharp
+L\sum_{\ell=1}^k\sum_{r\ge1}
\omega_\ell^r4^r\delta_{4^r}.
}
\tag{TP.4}
\]

Fix an integer carry endpoint `n`, put

\[
R=\lfloor\log_4n\rfloor,
\]

and assume

\[
\boxed{M>2R.}
\tag{TP.5}
\]

For a carry row `e=(n,j)`, set

\[
d_r(e)=L4^r\chi_{n,4^r}(j).
\]

Then

\[
P_{\boldsymbol\omega}(e)
=P_\sharp(e)+
\sum_{\ell=1}^k\sum_{r=1}^{R}
\omega_\ell^rd_r(e).
\]

Independent Fourier orthogonality gives

\[
\boxed{
\frac1{M^k}\sum_{\boldsymbol\omega}
|P_{\boldsymbol\omega}(e)|^2
=P_\sharp(e)^2+k\sum_{r=1}^{R}d_r(e)^2.
}
\tag{TP.6}
\]

Let

\[
C_{\boldsymbol\omega}
=\Lambda_{\boldsymbol\omega}\log
 +\Lambda_{\boldsymbol\omega}*\Lambda_{\boldsymbol\omega}.
\]

Every term containing a phase-dependent local factor has nonzero phase in at least one independent coordinate. The condition `M>2R` also prevents a same-coordinate local/local phase from returning to zero. Hence

\[
\boxed{
\frac1{M^k}\sum_{\boldsymbol\omega}
C_{\boldsymbol\omega}=C_\sharp
}
\tag{TP.7}
\]

through the complete endpoint. Consequently the averaged row reserve is exactly

\[
\boxed{
\mathcal R_{k,M}(e)
=\mathcal R_\sharp(e)
+k\sum_{r=1}^{R}d_r(e)^2
\ge0.
}
\tag{TP.8}

Thus independent phase depth adds only positive local storage; it creates no mixed Selberg debt.

## 3. Exact tensor DFT of the bare sources and currents

For a subset `S subset {1,...,k}`, write `|S|=r` and let `chi_S` be the corresponding product character on `Omega_M^k`. Use the normalized DFT

\[
\widehat B_S
=\frac1{M^k}\sum_{\boldsymbol\omega}
\overline{\chi_S(\boldsymbol\omega)}
B_{\boldsymbol\omega}.
\]

Since every phase coordinate appears only linearly in (TP.2), the only nonzero DFT modes are subsets, and

\[
\boxed{
\widehat B_S=(-a)^rB_\sharp.
}
\tag{TP.9}

Put

\[
q_\sharp=B_\sharp',
\qquad q_{\boldsymbol\omega}=B_{\boldsymbol\omega}'.
\]

Because `a'=-La`, differentiation of (TP.9) gives

\[
\boxed{
\widehat q_S
=(-a)^r(q_\sharp-rLB_\sharp).
}
\tag{TP.10}

All DFT modes outside `{0,1}^k` vanish identically.

Channel Parseval and `|a|^2=4` now give

\[
\boxed{
\frac1{M^k5^k}\sum_{\boldsymbol\omega}
|q_{\boldsymbol\omega}|^2
=\sum_{r=0}^k
\binom kr\frac{4^r}{5^k}
|q_\sharp-rLB_\sharp|^2.
}
\tag{TP.11}

The weights are the law of a binomial variable

\[
J\sim\operatorname{Binomial}(k,4/5).
\]

Therefore the whole current bank collapses exactly to

\[
\boxed{
\frac1{M^k5^k}\sum_{\boldsymbol\omega}
|q_{\boldsymbol\omega}|^2
=\left|q_\sharp-rac{4k}{5}LB_\sharp\right|^2
+rac{4k}{25}L^2|B_\sharp|^2.
}
\tag{TP.12}

After atomized physical localization, `zeta B_sharp N_theta=(1-a)N_theta` is deterministic. Thus the tensor bank carries only one genuine pole current, one deterministic linear gauge, and one deterministic variance term. Its complete causal current cost is quadratic, not exponential, in `k`.

## 4. Critical polynomial norm of an arbitrary channel direction

Equip channel coefficient vectors with the averaged norm

\[
\|x\|_{\rm ch}^2
=\frac1{M^k}\sum_{\boldsymbol\omega}|x_{\boldsymbol\omega}|^2.
\]

For `||x||_ch=1`, synthesize the normalized scalar multiplier

\[
H_x(a)
=\frac1{M^k5^{k/2}}
\sum_{\boldsymbol\omega}
\overline{x_{\boldsymbol\omega}}
F_{\boldsymbol\omega}(a)
=\sum_{r=0}^kh_r a^r.
\tag{TP.13}

Let `xhat_S` be the unitary tensor DFT of `x`. Then

\[
h_r={(-1)^r\over5^{k/2}}
\sum_{|S|=r}\widehat x_S.
\]

Cauchy–Schwarz and DFT Parseval imply

\[
\begin{aligned}
\sum_{r=0}^k4^r|h_r|^2
&\le
\sum_{r=0}^k
{4^r\binom kr\over5^k}
\sum_{|S|=r}|\widehat x_S|^2\\
&\le\sum_S|\widehat x_S|^2=1.
\end{aligned}
\]

Hence

\[
\boxed{
\|H_x\|_{\rm crit}^2
:=\sum_{r=0}^k4^r|h_r|^2\le1.
}
\tag{TP.14}

This estimate is uniform in the channel count and tensor depth.

## 5. Two-layer four-adic support and exact bandedness

The common source coefficient

\[
b_\sharp(n)=\mu(n)-4\mathbf1_{4\mid n}\mu(n/4)
\]

has a special support law:

\[
\boxed{
b_\sharp(n)\ne0
\Longrightarrow v_4(n)\in\{0,1\}.}
\tag{TP.15}

Indeed a squarefree integer has `v_4=0`, while the second tap produces exactly the layer `v_4=1`; every deeper layer contains a square factor and vanishes under `mu`.

Therefore the coefficient sequence of `a^rB_sharp` is supported only on the two four-adic layers

\[
v_4(n)\in\{r,r+1\}.
\tag{TP.16}

At any integer `n`, a sum

\[
\sum_rh_ra^rB_\sharp
\]

has at most two nonzero mode contributions. This gives a uniform banded coefficient Gram before any analytic estimate.

For a finite sequence `d(n)`, put

\[
\|d\|_{1/2,X}^2
=\sum_{n\le X}{|d(n)|^2\over n}.
\]

If `H(a)=sum h_r a^r`, then the two-layer law and `|u+v|^2<=2(|u|^2+|v|^2)` give

\[
\boxed{
\|H(a)B_\sharp\|_{1/2,X}^2
\le32(1+\log X)\|H\|_{\rm crit}^2.
}
\tag{TP.17}

Here we used only `|b_sharp(n)|<=4` and the harmonic-sum bound.

Differentiating the Dirichlet series gives the sharper load-bearing form

\[
\boxed{
\|(H(a)B_\sharp)'\|_{1/2,X}^2
\le32(1+\log X)(\log X)^2
\|H\|_{\rm crit}^2.
}
\tag{TP.18}

Indeed the coefficient arising from mode `r` and base integer `m` is

\[
-4^rh_rb_\sharp(m)\log(4^rm),
\]

and `4^rm<=X` makes the logarithm at most `log X`.

Likewise, for every derivative order `d>=0`,

\[
\boxed{
\|(H(a)B_\sharp)^{(d)}\|_{1/2,X}^2
\le32(1+\log X)(\log X)^{2d}
\|H\|_{\rm crit}^2.
}
\tag{TP.19}

Combining with (TP.14), every unit channel direction has source, current, and second-current coefficient norms bounded by fixed powers of `log X`, independently of `k`.

## 6. Montgomery–Vaughan operator corollary

Let `c_x^{(d)}(n)` be the coefficients of the `d`th derivative in (TP.19), truncated at `X`, and form

\[
D_{x,X}^{(d)}(t)
=\sum_{n\le X}{c_x^{(d)}(n)\over\sqrt n}\,n^{-it}.
\]

The classical Montgomery–Vaughan mean-value theorem gives

\[
\int_{-T}^{T}|D_{x,X}^{(d)}(t)|^2dt
\ll(T+X)
\sum_{n\le X}{|c_x^{(d)}(n)|^2\over n}.
\]

Therefore, uniformly over every tensor depth, channel count, and unit channel direction,

\[
\boxed{
{1\over T}\int_{-T}^{T}|D_{x,X}^{(d)}(t)|^2dt
\ll(1+X/T)(1+\log X)^{2d+1}.
}
\tag{TP.20}

In the natural regime `T>=X`, the bare source, current, and second current have respectively `O(log X)`, `O(log^3 X)`, and `O(log^5 X)` normalized mean square.

This is the first powered-Euler arithmetic estimate on the branch which is uniform over **coherent channel vectors**, rather than only the averaged diagonal bank.

## 7. What this closes and what remains

The theorem closes:

```text
independent phase source reserve             exact and positive;
tensor channel proliferation                 collapses to subset DFT;
causal current bank                          exact binomial two-state law;
arbitrary coherent channel synthesis         critical coefficient norm <=1;
source/current coefficient Gram              uniformly two-layer banded;
Dirichlet mean-square operator cost           polylogarithmic, uniform in k.
```

It does **not** by itself prove the corrected Weil-kernel floor. The complete Gabor/Weil compression contains an archimedean term and a prime-shift Toeplitz operator whose worst coherent direction is not controlled merely by a vertical mean square. Equivalently, the reflected left-half-plane boundary state is not the same object as the causal current Gram in (TP.12).

Thus the remaining theorem has been narrowed further:

> convert the uniform coefficient/mean-square estimate (TP.20), together with the positive tensor reserve (TP.8), into a lower bound for the complete source-convolved reflected block on the Xi-cardinal or Gaussian terminal direction.

Any proof must retain the exact reflected subtraction. Replacing the complete block by its causal current Gram or by a Frobenius average is an automatic rejection.

## Exact boundary

```text
tensor critical frame                         PROPOSED COMPLETE EXACT
tensor phase-separated reserve                 PROPOSED COMPLETE EXACT
tensor DFT current collapse                    PROPOSED COMPLETE EXACT
binomial current/gauge law                     PROPOSED COMPLETE EXACT
coherent critical polynomial norm              PROPOSED COMPLETE EXACT
two-layer four-adic coefficient bandedness      PROPOSED COMPLETE EXACT
uniform coefficient and MV mean-square bounds   PROPOSED COMPLETE
complete corrected-kernel arithmetic floor      OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```
