# R-92930 — The `q=2` rough-lift separator is exact, but the unqualified `109/1200` PR falsifier is withdrawn

Claim ID: `R-92930`
Status: **PROVED EXACT SCOPE FIREWALL AND FORMAL WITHDRAWAL**
Created: 2026-08-15
Frozen comparison heads: PR #496 `96f8a6b3cc3d474217633e16d4caa490a0aae518`; PR #500 `d73c1e7a1a482cac31581211a84db43cc34c824e`
RH status: **unproved**

## 1. Two different objects

For the native datum put

\[
 w_X(q)=q^{-1/2}\log(X/q)\mathbf 1_{q\le X},
 \qquad
 \Omega_X(q)=w_X(q)-2w_X(4q).
\]

Let `P=P_61`, and let

\[
 \mathcal R_{67}=\{m\ge1:P^-(m)\ge67\}.
\]

The row-first finite-Euler rough lift has detail response

\[
 \Theta_{P,X}(q)
 =\sum_{m\in\mathcal R_{67}}m^{-1/2}\Omega_{X/m}(q).
\tag{R-92930.1}
\]

This is not the native response `Omega_X`; it is the native response plus the positive rough reservoir.

## 2. Exact `q=2` separation

For every `Y>=8`,

\[
 \Omega_Y(2)
 =\frac1{\sqrt2}\log(Y/2)
  -\frac1{\sqrt2}\log(Y/8)
 =\frac{\log4}{\sqrt2}.
\tag{R-92930.2}
\]

If `X>=536`, both `m=1` and `m=67` in (R-92930.1) have `X/m>=8`. Every other rough term is nonnegative. Therefore

\[
\boxed{
 \Theta_{P,X}(2)-\Omega_X(2)
 \ge\frac1{\sqrt{67}}\Omega_X(2)
 =\frac{\log4}{\sqrt{134}}.
}
\tag{R-92930.3}
\]

The elementary bounds `log 4>4/3` and `sqrt(134)<12` give

\[
 \frac{\log4}{\sqrt{134}}>\frac19>\frac{109}{1200}.
\tag{R-92930.4}
\]

Thus a row which is literally the complete unthinned `P_61` rough lift is separated from the native packet already at `q=2`.

## 3. The previously quoted numerical bound, with its missing hypotheses restored

Set

\[
 X_0=10^{16},
 \qquad
 K_0=\left\lfloor X_0/67\right\rfloor+1,
 \qquad
 \tau_0=\frac{\sqrt{K_0}}{\sqrt{K_0}+130}.
\]

Since `K_0>129870^2`,

\[
 \tau_0>\frac{999}{1000}.
\]

Using `sqrt(67)<9`, `sqrt2<3/2` and `log4>4/3`,

\[
\begin{aligned}
 \tau_0\Theta_{P,X_0}(2)-\Omega_{X_0}(2)
 &\ge
 \left[\tau_0\left(1+\frac1{\sqrt{67}}\right)-1\right]
 \frac{\log4}{\sqrt2}\\
 &>
 \frac{11}{100}\cdot\frac89
 =\frac{22}{225}
 >\frac7{75}.
\end{aligned}
\tag{R-92930.5}
\]

Also `K_0>48550^2`, so the frozen nonterminal comparison majorant at `q=2` obeys

\[
 \frac{971}{8\sqrt{K_0}}<\frac1{400}.
\tag{R-92930.6}
\]

Consequently, **if** all of the following are proved for a proposed output row:

1. before the signed comparison its `q=2` response is exactly `tau_0 Theta_(P,X_0)(2)`;
2. support restriction or omission removes no additional positive rough-lift `q=2` mass;
3. every remaining signed `q=2` change has absolute value below `1/400`;

then its final overfill is greater than

\[
 \frac{22}{225}-\frac1{400}
 =\frac{343}{3600}
 >\frac{109}{1200}.
\tag{R-92930.7}
\]

This is the precise theorem behind the earlier informal number.

## 4. Why the earlier PR-specific assertion is withdrawn

PR #496 does not assert that its realized current is the complete rough lift `mathfrak D_X`. PR #500 describes a paired stopping-line source, retained whole cells, a physical child kernel and a label-blind output coupling; it likewise does not prove the three hypotheses in Section 3 for its actual retained output marginal.

In particular, source-tree rough children and row-first rough-lift summands are different typed objects. The response of an omitted or externally exported source class cannot be recovered from (R-92930.1) after labels have been erased.

Therefore the earlier statement

```text
PR #496 or PR #500 is refuted by a final q=2 excess >109/1200
```

was not established and is formally withdrawn.

## 5. Normative firewall

The exact separator (R-92930.3) remains load bearing as a regression test:

```text
if a producer identifies its native parent with the full P61 rough lift,
reject it at q=2;

if a producer uses the native paired source tree,
prove that source identity explicitly and do not substitute the rough lift.
```

```text
full rough-lift/native distinction             exact
unthinned q=2 separator                        exact
conditional X=10^16 109/1200 separator         exact with three stated hypotheses
application to frozen PR #496                  withdrawn
application to frozen PR #500                  not automatic / normalization test required
Riemann Hypothesis                             unproved
```
