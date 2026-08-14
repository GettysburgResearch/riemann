# T-91654 — Full direct-row factor-67 resolution proposal

Claim ID: `T-91654`  
Status: **COMPLETE RH PROOF PROPOSAL — INDEPENDENT FROZEN-COMMIT REVIEW REQUIRED**  
Created: 2026-08-14  
Supersedes as review target: `T-91652`, `T-91653`, the open `GRRT/CFFP` frontiers in `SPP-91661`  
RH status: **not accepted before independent reconstruction**

## 1. The completed reset theorem

Let `d_X` be the nonnegative row constructed recursively by `L-91667`. It is
feasible in every ordinary and radix-four physical column and every packet-owned
boundary coordinate. Its signed native loss satisfies

\[
\boxed{
 \mathfrak L_X(d_X)
 =J_\Lambda(X)-\operatorname{Score}(d_X)
 \le
 \mathfrak L_{X/67+C_0}(d_{X/67+C_0})+C_{\rm reset},
}
\tag{T-91654.1}
\]

where `C_0` and `C_reset` are absolute and effective on the frozen finite
producer inputs.

The recurrence is obtained from one exact native equality row, not from a
formal residual complement:

\[
 \Gamma(c_X)=w_X,
 \qquad
 \Xi(c_X)=\Omega_X,
\tag{T-91654.2}
\]

\[
 c_X=R_{\rm pre}+R_s(c_s)+R_h(c_h)+B_s+B_h\ge0,
\tag{T-91654.3}
\]

and

\[
 d_X=c_X-R_{\rm ch}+d_{\rm ch}.
\tag{T-91654.4}
\]

For every physical integer column,

\[
 \Gamma(d_X)
 =w_X-\Gamma(R_{\rm ch})+
   \Gamma(d_{\rm ch})
 \le w_X,
\tag{T-91654.5}
\]

\[
 \Xi(d_X)
 =\Omega_X-\Xi(R_{\rm ch})+
   \Xi(d_{\rm ch})
 \le\Omega_X.
\tag{T-91654.6}
\]

The exact fixed-67 literal-score theorem gives the score part of
(T-91654.1). Every global finite correction is current-only and charged once.

## 2. Logarithmic loss

Iteration terminates after `O(log X)` generations. Therefore

\[
\boxed{
 \mathfrak L_X(d_X)=O(\log X)=o(\log^2X).
}
\tag{T-91654.7}
\]

No absolute all-depth score transfer, scalar source-fraction weighting of a
signed loss, affine Pascal child, fractional physical column, or duplicated
small-prime block is used.

## 3. Finite dual bridge

The average-binomial/von-Mangoldt identity is

\[
 G_n=\sum_{q=p^a\le n}\Lambda(q)\beta_{nq}.
\tag{T-91654.8}
\]

Since `d_X` is ordinarily feasible,

\[
\begin{aligned}
 \operatorname{Score}(d_X)
 &=\sum_q\Lambda(q)\sum_nd_X(n)\beta_{nq}\\
 &\le\sum_q\Lambda(q)w_X(q)=P_\Lambda(X).
\end{aligned}
\tag{T-91654.9}
\]

Hence

\[
\boxed{
 F_\Lambda(X)=J_\Lambda(X)-P_\Lambda(X)
 \le\mathfrak L_X(d_X)
 =o(\log^2X).
}
\tag{T-91654.10}
\]

## 4. Analytic conclusion

The higher-prime-power contribution obeys

\[
 F_\Lambda(X)-A(X)
 =\frac{-1-\zeta(1/2)}4\log^2X+o(\log^2X),
\tag{T-91654.11}
\]

where `A(X)` is the undifferenced prime-only endpoint and

\[
 -1-\zeta(1/2)>0.
\]

Therefore (T-91654.10) gives

\[
 A(X)
 =-\frac{-1-\zeta(1/2)}4\log^2X+o(\log^2X)<0
\]

for all sufficiently large `X`.

The Mellin transform of the twice-integrated prime endpoint has a genuine pole
at `z=rho-1/2` for every nontrivial zero `rho`, with nonzero residue

\[
 \frac{m_\rho}{(\rho-1/2)^2}.
\]

If an off-line zero with `Re rho>1/2` existed, eventual one-sign of `A(e^t)`
would contradict Landau's theorem: either the Laplace transform is holomorphic
at the nonreal pole, or its abscissa of convergence forces a singularity on the
positive real axis where the exact symbol is regular. The functional equation
then gives

\[
\boxed{\mathrm{RH}.}
\tag{T-91654.12}
\]

## 5. Exact dependency order

A reviewer should reconstruct in this order:

1. exact component row and native response identity;
2. paired least-prime stopping-line source identity;
3. one-prime native target/score/row cocycle;
4. frozen no-upward Hall corridors and normalized-row monotonicity;
5. leafwise Hall Fubini theorem;
6. same-index ordinary and radix-four child replacement;
7. complete proof of the fixed-67 literal-score inequality `L-91666`;
8. finite mismatch, collar, terminal, safety, and corrected `P_61/67` port,
   checking one-use ownership;
9. equality-density score `4 sqrt(X)` and the native benchmark upper bound;
10. recurrence (T-91654.1), finite duality, prime-square drift, and Landau.

The exact verifier accompanying this theorem checks the new fixed-67 proof and
the algebraic shell. It deliberately does not replace reconstruction of the
expensive frozen finite certificates.

## 6. Falsifiers

The proposal is rejected on the first occurrence of any of:

```text
failed source-disjoint stopping identity;
failed frozen Hall prefix or normalized-row cell;
parent Hall row not equal to the exact native equality row;
failed same-index ordinary or detail replacement;
fixed-67 score inequality failure;
finite current correction charged in both current and child packets;
port using the obsolete P53 constant;
scale-dependent C_reset;
endpoint dual or analytic sign error.
```

## 7. Status boundary

```text
native equality response                       exact
positive leafwise Hall realization             exact on frozen inputs
same-index arbitrary-child replacement          exact
fixed-67 score difference                       proved analytic + directed
one-use root/current ledger                     proposed complete
loss recurrence                                 proposed complete
loss O(log X)                                   exact consequence
endpoint dual and analytic RH implication       exact on stated inputs
full theorem                                    complete proposal / review required
Riemann Hypothesis                              not accepted before review
```
