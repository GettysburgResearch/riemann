# L-27901 — The dyadic parabolic shell density has exactly one sign change

Claim ID: `L-27901`  
Title: The complete dyadic shell defect is positive below one explicit ratio, negative above it, and has no secondary oscillation  
Status: **PROPOSED COMPLETE ELEMENTARY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Frozen parent: PR #276 at `a65a02b9463c1cc3a10d0af03ab359a637e357cd`  
Dependencies: PR #240 `L-23823`; elementary sum–integral bounds  
Scope: continuum dyadic-shell geometry; no prime-sampling estimate and no RH conclusion

## 1. The shell density

Retain the parabolic defect

\[
E(\theta)
=\sum_{1\le k\le 1/\theta}
 \left({\log(k\theta)+4\over\sqrt{k\theta}}-4\right)
-\theta^{-1/2}\log(1/\theta),
\qquad 0<\theta\le1.
\tag{L-27901.1}
\]

The dyadic shell density is

\[
\boxed{
D(\theta)
=E(\theta)-\sqrt2\,E(2\theta)\mathbf1_{\theta\le1/2}.}
\tag{L-27901.2}
\]

Its cumulative upper tail is the already proved shell moat

\[
\int_\theta^1D(u)\,du
=H_{1/2}(\theta)\le0.
\]

The new assertion is pointwise and substantially stronger.

## 2. Exact reciprocal-cell formula

Put

\[
S_N=\sum_{k=1}^Nk^{-1/2},
\qquad
A_N=\sum_{k=1}^Nk^{-1/2}\log k.
\]

On

\[
I_N=\left({1\over N+1},{1\over N}\right],
\]

`L-27501` gives

\[
E(\theta)
=\theta^{-1/2}
 [A_N+(S_N+1)\log\theta+4S_N]-4N.
\tag{L-27901.3}
\]

For `N>=2`, put

\[
M=\lfloor N/2\rfloor,
\quad
V_N=S_N-S_M>0,
\]

\[
U_N=A_N-A_M+4V_N-(S_M+1)\log2,
\]

and

\[
W_N=4(N-\sqrt2M).
\]

Since `floor(1/(2 theta))=M` throughout `I_N`, subtraction gives the exact cell formula

\[
\boxed{
D_N(\theta)
=\theta^{-1/2}[U_N+V_N\log\theta]-W_N.
}
\tag{L-27901.4}
\]

The entering summand at every reciprocal knot is zero, so the cell formulas join continuously.

## 3. No cell has an interior minimum

Differentiating (L-27901.4),

\[
D_N'(\theta)
=\theta^{-3/2}
\left[V_N-{1\over2}(U_N+V_N\log\theta)\right].
\tag{L-27901.5}
\]

The bracket is strictly decreasing in `theta`, because `V_N>0`. Thus the derivative can change only from positive to negative. Every reciprocal cell has at most one critical point, and any such critical point is a strict maximum.

Consequently the minimum of `D_N` is always attained at one of the two reciprocal endpoints.

## 4. Monotonicity on every cell below `1/9`

It is enough to check the derivative at the left endpoint. Equation (L-27901.5) is nonpositive throughout `I_N` when

\[
\mathcal M_N
:=
\sum_{k=M+1}^{N}{2+\log(k/(N+1))\over\sqrt k}
-(S_M+1)\log2
\ge0.
\tag{L-27901.6}
\]

Let

\[
f_N(x)=x^{-1/2}[2+\log(x/(N+1))].
\]

On the relevant interval it is increasing and concave. The midpoint inequality therefore gives

\[
\sum_{k=M+1}^{N}f_N(k)
\ge
\int_{M+1/2}^{N+1/2}f_N(x)\,dx,
\tag{L-27901.7}
\]

and

\[
\int f_N(x)dx=2\sqrt x\log(x/(N+1)).
\tag{L-27901.8}
\]

### Odd cells

For `N=2M+1`, the integral lower bound minus `2 sqrt(M) log 2` is bounded below by

\[
-{2\sqrt{2M+3/2}\over4M+3}
+{2\sqrt{M+1/2}\over2M+2}
+2(\sqrt{M+1/2}-\sqrt M)\log2.
\tag{L-27901.9}
\]

The first two terms already have positive sum: after squaring, their comparison reduces to

\[
{(4M+3)(4M^2+2M-1)\over2}>0.
\]

Hence `mathcal M_(2M+1)>0` for every `M>=1`.

### Even cells

For `N=2M`, define

\[
\delta_M=2\sqrt M-(S_M+1).
\]

One has

\[
\delta_{M+1}-\delta_M>0,
\qquad
\delta_5>6/25.
\tag{L-27901.10}
\]

Using (L-27901.7), `log(1-x)>=-x/(1-x)`, and

\[
\sqrt{M+1/2}-\sqrt M
\ge {1\over4\sqrt{M+1/2}},
\]

gives

\[
\mathcal M_{2M}
\ge
\delta_5\log2
-{2\sqrt{2M+1/2}\over4M+1}
+{\log2\over2\sqrt{M+1/2}}.
\tag{L-27901.11}
\]

The last two terms have decreasing absolute deficit for `M>=5`; at `M=5` that deficit is less than `81/500`, while

\[
\delta_5\log2>{6\over25}{69\over100}>{81\over500}.
\]

Therefore `mathcal M_(2M)>0` for every `M>=5`.

It follows that

\[
\boxed{D'(\theta)<0\quad(0<\theta\le1/9),}
\tag{L-27901.12}
\]

apart from the reciprocal knots, where the integrated monotonicity continues.

## 5. Positive lower sector

The exact finite evaluations

\[
D(1/9)>0.1065,
\qquad
D(1/8)>0.0931
\tag{L-27901.13}
\]

are separated from zero by the rational interval replay in `X-27901`.

Equation (L-27901.12) proves positivity on `(0,1/9]`. The `N=8` cell has no interior minimum and both of its endpoint values are positive. Hence

\[
\boxed{D(\theta)>0\qquad(0<\theta\le1/8).}
\tag{L-27901.14}
\]

The same sum–integral argument gives the useful quantitative form

\[
D(\theta)\ge c_0\theta^{-1/2}-C_0
\qquad(0<\theta\le1/8)
\tag{L-27901.15}
\]

for explicit absolute constants.

## 6. Negative upper sector and the unique transition

For `theta>=1/2`, `N=1` and

\[
E(\theta)=4\left({1+\log\sqrt\theta\over\sqrt\theta}-1\right)\le0
\]

by `log x<=x-1`.

For cells `N=2,...,6`, the maximum described in Section 3 is strictly negative. The smallest negative moat is larger than `1/100`; all six finite inequalities are replayed with directed rational logarithm and square-root enclosures in `X-27901`.

On the `N=7` cell, the derivative is strictly negative and

\[
D(1/8)>0,
\qquad
D(1/7)<-0.0128.
\]

Therefore there is exactly one root

\[
\boxed{
\theta_*\in(1/8,1/7),
}
\tag{L-27901.16}
\]

and it is simple. The retained numerical enclosure is

\[
0.1408520350<\theta_*<0.1408520351.
\tag{L-27901.17}
\]

Combining all cells,

\[
\boxed{
D(\theta)>0\ (0<\theta<\theta_*),
\qquad
D(\theta)<0\ (\theta_*<\theta<1).
}
\tag{L-27901.18}
\]

## 7. Meaning for the RH programme

The continuum dyadic shell is not merely upper-tail ordered. It is a literal one-crossing signed density:

```text
low ratios       positive defect;
high ratios      negative slack;
exactly one interface, in quotient cell 7.
```

Thus the finite WSTS maximum should not require an arbitrary family of tail cuts. The only ways finite arithmetic can obstruct exact order are:

1. displacement of the single interface by the carry-floor error;
2. the total logarithmically weighted prime-sampling scalar.

`L-27902/L-27903` make this reduction precise.

## 8. Proof boundary

Closed here, subject to review:

- exact reciprocal-cell shell formula;
- absence of interior minima;
- all-cell monotonicity below `1/9`;
- positive lower sector;
- finite negative upper sectors;
- one unique simple zero in `(1/8,1/7)`.

Not closed:

- the corresponding finite-prime one-crossing theorem;
- the sign of the total weighted finite shell;
- WSTS or RH.
