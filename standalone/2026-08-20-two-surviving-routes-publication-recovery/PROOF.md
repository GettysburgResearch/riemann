# Two surviving closure routes — complete publication-recovery proof packet

**Scientific status:** exact reductions; `QACG100400`, `LPMW100410`, and RH
remain open.

## 1. Quadratic route

For `-1<=c<=0`, set `lambda_c=(3-c)^2/9`.  The exact scaling

\[
\lambda_c^{-1}S_c(\lambda_c y)^2=(4\sqrt y-3)^2
\]

holds whenever the shifted carrier is active.  Splitting at `n=X` yields

\[
\lambda_c^{-1}Q_c(\lambda_c X)=H_2(X)+P_c(X),
\]

where `P_c` contains every source integer in `X<n<=lambda_cX`.

Distributionally,

\[
d(e^{-u}Q_c(e^u))
=(1+c)^2\sum_n\beta(n)n^{-3/2}\delta_{\log n}
+(3-c)e^{-u}L_c(e^u)du.
\]

Integrating to infinity proves the exact future formula

\[
\begin{aligned}
\mathcal E_2(X)={}&X(1+c)^2\sum_{n>\lambda_cX}\beta(n)n^{-3/2}\\
&+(3-c)X\int_{\lambda_cX}^{\infty}L_c(t)dt/t^2+P_c(X).
\end{aligned}
\]

At `c=0`, `P_c=0` but the atoms remain.  At `c=-1`, the atoms vanish but
`lambda_c=16/9`, and

\[
P_{-1}(2)=-3^{-1/2}(4\sqrt{2/3}-3)^2<0.
\]

Thus the final quadratic gate is the complete atom-plus-collar sign, not
positivity of the shifted square by itself.

## 2. Minimal-wavelet route

The compact kernel `K_0` is supported on `[1,8]`.  For every squarefree
`n>1`, write `n=pm` with `p=P^+(n)` and `P^+(m)<p`.  Since
`mu(pm)=-mu(m)`,

\[
G_\mu(X)=K_0(X)-\sum_p p^{-1/2}
\sum_{X/(8p)\le m\le X/p\atop P^+(m)<p}
\mu(m)m^{-1/2}K_0(X/(pm)).
\]

For `X>8`, the root vanishes.  With
`Y_X=(log X)^(3/2)` and
`sigma_X=1/3+1/sqrt(log log X)`, Rankin's inequality gives

\[
\Psi(X,Y_X)=X^{1/3+o(1)}.
\]

The shell weight is `O(X^-1/2)`, so the smooth contribution is
`X^-1/6+o(1)`.  The remaining form is exactly `G_rough` from L-100410.4.
Its subpower logarithmic negative mass implies RH through the minimal-wavelet
consumer.

## 3. Phase-Hasse audit

Let

\[
P_B(\gamma)=\prod_i(1-a_ip_i^{i\gamma}),
\qquad s_B=\prod_i(1-a_i).
\]

Differentiating the minus-product in the random-key parameter gives

\[
\mathscr S_B(\gamma)
={1\over2}[\mathscr T_B(\gamma)+s_B-P_B(\gamma)].
\]

The neutral phase vanishes, but `-P_B(gamma)/2` remains for nonzero phase.
Therefore this is not a root-free third route.

## 4. Boundary

```text
QACG100400  open / RH-bearing
LPMW100410  open / RH-bearing
RH          unproved
```
