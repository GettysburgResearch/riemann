# L-19887 — An elementary Chebyshev bound makes the factor-67 square-root thinning native-cost bounded

Claim ID: `L-19887`  
Status: **PROPOSED EXACT ANALYTIC ESTIMATE — PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-y`  
Created: 2026-08-15  
Frozen inputs: `L-91377/L-91378`; PR #477 at `5acd9007b4f4bb1792466f5013c39bf4eac33f9e`; PR #479 at `518b6a5ec2b49b7decbd4c2e349d0ee5b26bfc9b`  
RH status: **unproved**

## 1. A fully elementary bound for the Chebyshev function

Put

\[
 \psi(x)=\sum_{n\le x}\Lambda(n).
\]

For every integer `n>=1`,

\[
 \boxed{
 \psi(2n)-\psi(n)\le \log {2n\choose n}\le 2n\log2.
 }
\tag{L-19887.1}
\]

For the first inequality, fix a prime `p`. Legendre's formula gives

\[
 v_p{2n\choose n}
 =\sum_{k\ge1}
 \left(\left\lfloor\frac{2n}{p^k}\right\rfloor
       -2\left\lfloor\frac n{p^k}\right\rfloor\right).
\]

Every summand is zero or one, and it is one whenever `n<p^k<=2n`. Thus the binomial coefficient contains at least the complete prime-power product measured by `psi(2n)-psi(n)`. The second inequality is `{2n choose n}<=2^(2n)`.

Choose `m` with `2^(m-1)<x<=2^m`. Dyadic telescoping gives

\[
\begin{aligned}
 \psi(x)
 &\le\psi(2^m)\\
 &\le\sum_{j=0}^{m-1}2^{j+1}\log2\\
 &=(2^{m+1}-2)\log2
 <4x\log2.
\end{aligned}
\]

Therefore

\[
 \boxed{
 \psi(x)<4x\log2
 \qquad(x\ge1).
 }
\tag{L-19887.2}
\]

No prime number theorem or zero-free region is used.

## 2. Native benchmark is `O(sqrt X)` unconditionally

Recall

\[
 J_\Lambda(X)
 =\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\log\frac Xn.
\]

Stieltjes integration by parts, using `psi(1)=0`, gives

\[
 J_\Lambda(X)
 =\int_1^X\psi(t)t^{-3/2}
   \left(1+\frac12\log\frac Xt\right)dt.
\tag{L-19887.3}
\]

Using (L-19887.2) and extending the two positive integrals down to zero,

\[
\begin{aligned}
 J_\Lambda(X)
 &<4\log2
 \int_0^X t^{-1/2}
 \left(1+\frac12\log\frac Xt\right)dt\\
 &=4\log2\,[2\sqrt X+2\sqrt X].
\end{aligned}
\]

Hence

\[
 \boxed{
 J_\Lambda(X)<16(\log2)\sqrt X.
 }
\tag{L-19887.4}
\]

This is the correct unconditional estimate for the cost of a common scalar source thinning. The cruder `O(sqrt X log^2 X)` estimate is unnecessary.

## 3. The PR #479 square-root thinning has absolute native cost

Put

\[
 K=\left\lfloor\frac X{67}\right\rfloor+1,
 \qquad
 \tau_K=\frac{\sqrt K}{\sqrt K+130}.
\]

Then

\[
 1-\tau_K<\frac{130}{\sqrt K}.
\]

If the complete common-parent packet before thinning is the exact finite Möbius packet of `L-91377`, its native dual score is exactly `J_Lambda(X)`. Therefore the literal unused native capacity introduced by this thinning has cost

\[
\begin{aligned}
 (1-\tau_K)J_\Lambda(X)
 &<2080(\log2)\sqrt{X/K}\\
 &<2080(\log2)\sqrt{67}.
\end{aligned}
\]

The elementary rational bounds

\[
 \log2<\frac7{10},
 \qquad
 \sqrt{67}<\frac{33}{4}
\]

give

\[
 \boxed{
 (1-\tau_K)J_\Lambda(X)<12012.
 }
\tag{L-19887.5}
\]

Thus the stronger all-column thinning of `L-91723` costs one absolute amount in the exact native `Y_4` metric, not `O(log^2 X)`.

## 4. The remaining all-column realization error is summable

`L-91723` gives, on every nonterminal physical column,

\[
 |e_X(q)|<\frac{971}{4q\sqrt K}.
\]

`L-19885` gives

\[
 \sum_{q\le X}\frac{Y_4(q)}q
 \le3+2L+2L^2,
 \qquad L=\log(2X).
\]

Consequently

\[
 \boxed{
 \sum_{q\le X/4}Y_4(q)|e_X(q)|
 \le\frac{971}{4\sqrt K}(3+2L+2L^2)
 =o(1).
 }
\tag{L-19887.6}
\]

The activation-knot collar and retained-cell refinement of `L-91724` each have score cost below `X^-2`. The fixed terminal omission, finite base correction, and one common uncolored port have bounded frozen cost. Therefore every finite-realization operation after the exact ideal common-parent identity has bounded total native-dual cost.

## 5. Boundary

```text
psi(x)<4 log(2) x                               exact elementary
J_Lambda(X)<16 log(2) sqrt(X)                  exact elementary
sqrt-K thinning native cost <12012              exact
all-column mismatch/collar native cost          o(1)
knot collar and refinement cost                 o(1)
fixed top/base/common-port cost                 bounded frozen input
exact common-parent one-use identity            PR #479 stack / reconstruct
Riemann Hypothesis                              unproved at this lemma
```
