# L-32715 — The complete cofinal Q=4 reflected row ledger fits inside one Kummer reserve

Claim ID: `L-32715`  
Title: On every sufficiently large quarter-balanced row, one Q=4 Kummer square simultaneously pays the complete Selberg forcing, the true pole-current square, both source-convolved individual terms, and the product-source term, with positive unused slack  
Status: **PROPOSED COMPLETE UNCONDITIONAL COFINAL ROW/BLOCK THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: PR #325 `L-32405`; PR #337 `L-32708/L-32710/L-32711`; correct source typing `R-32704`  
Scope: exact physical scalar localization and any nonnegative direct integral of those scalar rows; four-adic delayed routing and the global recurrence remain separate

## 1. Five quantities on one physical carry row

For a row

\[
 e=(n,j),
 \qquad k=n-j,
 \qquad n/4\le j\le3n/4,
\]

put

\[
 P_e=\mathcal L_e(\Lambda_4),
 \qquad
 S_e=\mathcal L_e(C_4),
 \qquad
 R_e=P_e^2-S_e.
 \tag{L-32715.1}
\]

Retain the Q=4 inverse source and its first two logarithmic currents

\[
 b_4,
 \qquad
 q_4=b_4*\Lambda_4,
 \qquad
 t_4=b_4*C_4.
\]

Define

\[
 Y_e=\mathcal L_e(b_4),
 \qquad
 Q_e=\mathcal L_e(q_4),
 \qquad
 T_e=\mathcal L_e(t_4).
 \tag{L-32715.2}
\]

The source typing is load-bearing. Since

\[
 \mathbf1*q_4=e_4*\Lambda_4=c_4,
\]

divisor switching gives

\[
 \boxed{
 Q_e
 =G_4(n)-G_4(j)-G_4(k)
 =Q_4^{\rm phys}(n,j),
 }
 \tag{L-32715.3}
\]

where `G_4` is the ordinary prefix of the correctly typed physical coefficient `c_4`. Thus `Q_e` is the true pole-sensitive centered-interval field, not the superseded extra-floor field.

## 2. Exact product and individual reflected terms

`L-32710` identifies the complete source-convolved independent-frequency terms after physical localization. On a real physical row, the two individual terms are

\[
 \boxed{I_e=2Y_eT_e,}
 \tag{L-32715.4}
\]

while the current square is

\[
 \boxed{E_e=2Q_e^2.}
 \tag{L-32715.5}
\]

The reflected coefficient identity

\[
 \text{product}-\text{individuals}=2q_4*q_4
\]

therefore gives the localized product-source row

\[
 \boxed{B_e=2Q_e^2+2Y_eT_e.}
 \tag{L-32715.6}
\]

Equations (L-32715.4)--(L-32715.6) are identities; no estimate or diagonal approximation enters them.

For complex physical rows the same statements hold with `Y_eT_e` replaced by the appropriate Hermitian real part. Every estimate below uses absolute values and therefore covers that form.

## 3. All non-Selberg reflected terms have vanishing reserve cost

PR #337 `L-32708` proves, uniformly on the quarter-balanced cone,

\[
 \boxed{
 \frac{Q_e^2}{R_e}\longrightarrow0.
 }
 \tag{L-32715.7}
\]

PR #337 `L-32711` proves

\[
 |Y_eT_e|\ll n\log^4(2n),
 \tag{L-32715.8}
\]

while PR #325 `L-32405` gives cofinally

\[
 R_e\ge\frac{n^2\log^22}{320}.
 \tag{L-32715.9}
\]

Consequently

\[
 \boxed{
 \frac{|Y_eT_e|}{R_e}\longrightarrow0
 }
 \tag{L-32715.10}
\]

uniformly on the same cone.

Combining (L-32715.7) and (L-32715.10), for every fixed `M>0` and every `delta>0` there exists `N_(M,delta)` such that

\[
 \boxed{
 M\bigl(Q_e^2+|Y_eT_e|\bigr)
 \le\delta R_e
 }
 \tag{L-32715.11}
\]

for every quarter-balanced parent `n>=N_(M,delta)`.

## 4. One no-double-spend budget pays the complete reflected row

Take `M=8` and `delta=1/2`. Cofinally,

\[
 8Q_e^2+8|Y_eT_e|
 \le\frac12R_e.
 \tag{L-32715.12}
\]

The complete absolute charge of the product row, the two individual rows, and the current square is bounded by

\[
\begin{aligned}
 |B_e|+|I_e|+E_e
 &\le(2Q_e^2+2|Y_eT_e|)
   +2|Y_eT_e|+2Q_e^2\\
 &=4Q_e^2+4|Y_eT_e|\\
 &\le\frac14R_e.
\end{aligned}
 \tag{L-32715.13}
\]

Therefore

\[
\boxed{
 S_e+|B_e|+|I_e|+E_e
 \le
 P_e^2-\frac34R_e.
}
 \tag{L-32715.14}
\]

The constant `3/4` is only a convenient declared slack. Any fixed fraction below one is available by moving the parent threshold outward.

This is a genuine no-double-spend statement:

1. `S_e` is paid first;
2. every source-convolved reflected term is then charged to the single explicit remainder `R_e=P_e^2-S_e`;
3. at least `3R_e/4` remains unused;
4. no term is assigned simultaneously to a current reserve and a boundary reserve.

## 5. Direct physical-block form

The independent-frequency block kernel of `L-32710` is exactly the Fourier representation of integration over physical logarithmic position and carry position. Hence a fixed physical block is a nonnegative direct integral of scalar rows `e(x,theta)`.

Let `nu` be any finite nonnegative measure supported on cofinal quarter-balanced physical rows, including the real-`X` collar refinement of PR #325. Integrating (L-32715.14) gives

\[
 \boxed{
 \begin{aligned}
 &\int S_e\,d\nu
 +\int|B_e|\,d\nu
 +\int|I_e|\,d\nu
 +\int E_e\,d\nu\\
 &\qquad\le
 \int P_e^2\,d\nu
 -\frac34\int R_e\,d\nu.
 \end{aligned}
 }
 \tag{L-32715.15}
\]

No arbitrary source Gram is diagonalized here: the diagonalization is the exact physical Plancherel localization already proved in `L-32710`. Equation (L-32715.15) may not be applied to an unrelated abstract matrix orientation.

## 6. Finite collars

Parents below the cofinal threshold form one finite base table. The real-`X` discrepancy is one raw coefficient and has logarithmic size by PR #325 `L-32410`. The adverse unweighted source sector is confined to a fifteen-contact collar with values `-1,-4` by `L-32706`.

Thus every excluded row belongs to a fixed finite-parent or fixed-child collar and contributes at most a polynomial function of the logarithmic block index after the standard finite-color decomposition.

No cofinal RH-bearing field is hidden in this collar statement.

## 7. What this closes

The Q=4 source-convolved reflected ledger had four potentially separate current-scale obligations:

```text
complete Selberg forcing;
product-source term;
two individual source-convolved terms;
true pole-current square.
```

They now fit simultaneously inside one generalized-prime Kummer square, with a strict cofinal leftover reserve. Thus **current-scale reflected reserve accounting is closed** at the exact physical-row/direct-integral orientation.

The remaining global task is no longer another current-scale estimate. It is to route the finite-deformation product descendants through the exact four-adic normal form of `L-32714`, using the reserve storage of `L-32713`, and compose that routing with the unitary terminal state of PR #325 `L-32406`.

## 8. Proof boundary

Closed here, subject to review:

1. exact source typing of the physical current;
2. exact physical product/individual/current row identities;
3. uniform vanishing reserve cost of every non-Selberg term;
4. one complete cofinal no-double-spend row budget;
5. its exact physical direct-integral form;
6. finite-collar separation.

Still open:

1. the all-generation four-adic descendant allocation;
2. composition with the all-pass terminal state into a coefficient-one delayed recurrence;
3. RH.
