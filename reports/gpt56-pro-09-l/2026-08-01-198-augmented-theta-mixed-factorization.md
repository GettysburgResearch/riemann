# Augmented theta mixed factorization

Agent: `gpt56-pro-09-l`  
Date: 2026-08-01  
PR: #202  
Classification: exact cross-mode factorization and explicit theta variance channel; trace Schur sign remains load-bearing

## Executive result

This pass moved beyond the refuted modewise-square and old-trace routes.

1. The complete normalized theta source has an exact pairwise mode-variance square. The one-mode source is missing precisely this channel.
2. After adjoining the exact Mellin boundary row, the original theta operator minus its augmented trace Schur form has one explicit positive mixed square:

\[
\mathcal S_\theta-R_{\rm aug}^*D_{\rm aug}R_{\rm aug}
=4J_{\rm mix}^*J_{\rm mix}.
\]

3. `J_mix` is the common full-theta moving-tail synthesis plus the minimal Douglas cross-mode mixer. It is not a direct sum over theta modes.

The remaining sign needed for the unrepaired contraction is exactly

\[
D_{\rm aug}\succeq0.
\]

## Full-theta pair square

For

\[
b_n(v)=e^{v/4-\pi n^2e^v},\qquad B=\sum_nb_n,
\]

let

\[
p_n=b_n/B,\qquad Y_n=\pi n^2e^v,
\qquad a=\mathbb E[Y]-1/4.
\]

Then

\[
\frac{\Phi(v/2)}{B(v)}
=4(a-5/4)(a+1/4)+4\operatorname{Var}(Y),
\]

and

\[
4\operatorname{Var}(Y)
=2\sum_{m,n}p_mp_n(Y_m-Y_n)^2.
\]

This is an explicit positive source term genuinely mixing separate theta modes. It vanishes identically in a one-mode model.

## Mellin augmentation

For one incomplete-gamma atom, the exact split at the Volterra base point is

\[
X_i(z)=B_i(s,z)+T_i(s,z).
\]

The moving tail `T_i` is diagonal in the Volterra atom, while the prefix `B_i` can be nearly the complete atom. The old endpoint rows do not span this prefix. The exact missing functional is

\[
M_z(f)=\int_0^L B(s,z)f(s)ds
      =\int_0^LB'(s,z)F(s)ds.
\]

Thus

\[
R_{\rm aug}=(\Lambda_a,M)
\]

is the smallest trace on whose kernel the complete incomplete-gamma boundary packet vanishes.

## Exact mixed Schur square

Let

\[
N=\ker R_{\rm aug},\qquad f=n+Ex,\qquad x=R_{\rm aug}f.
\]

The moving full-theta tail gives

\[
A=\mathcal S_\theta|_N=\mathcal V^*\mathcal V.
\]

Write

\[
\mathcal S_\theta=\begin{pmatrix}A&B\\B^*&C\end{pmatrix}.
\]

The augmented Mellin split forces the cross block through the common moving-tail range. With

\[
\Gamma=(\mathcal V^*)^\dagger B,
\qquad B=\mathcal V^*\Gamma,
\]

put

\[
D_{\rm aug}=C-\Gamma^*\Gamma.
\]

Then

\[
J_{\rm mix}f
=\frac12[\mathcal V(f-ER_{\rm aug}f)+\Gamma R_{\rm aug}f]
\]

and direct expansion yields

\[
\boxed{
\mathcal S_\theta-R_{\rm aug}^*D_{\rm aug}R_{\rm aug}
=4J_{\rm mix}^*J_{\rm mix}.}
\]

This is the actual mixed factorization requested. It is a completed-domain identity, not a finite-mode or one-mode ansatz.

## Sign convention

The displayed identity uses the intrinsic Schur form `D_aug`. A positive repair uses

\[
D_-=(-D_{\rm aug})_+
\]

and the plus-sign form

\[
\mathcal S_\theta+R_{\rm aug}^*D_-R_{\rm aug}\succeq0.
\]

The two formulas should not be conflated.

## Exact remaining sign

The factorization isolates the unrepaired contraction to

\[
D_{\rm aug}\succeq0.
\]

Equivalently, in the Cayley notation of `L-19815`,

\[
D_{\rm aug}=\operatorname{Re}L.
\]

The new work removes the mode-mixing and range-factorization ambiguity. It does not independently prove that the augmented trace Schur form is positive.

## Exact regression

`X-19803` verifies both the theta variance identity and the mixed Schur identity using exact rational arithmetic. The retained values are

```text
mean                 4
variance             2
scalar theta channel 40
pair theta channel   8
mu                    48
trace Schur           3/5
```

The proof-object SHA-256 is

```text
a9a5f7f6458a14ad38a74f65ff9174307ab012e4cba087f59369dcd7be66a107
```

and all eight adversarial tests pass.

## Honest conclusion

The positive cross-mode kernel has been constructed. A full RH closure additionally requires a theta-specific proof that the augmented Mellin trace Schur form is nonnegative. Generic Green stationarity, pointwise multiplier contraction, and the mode-variance identity alone do not prove that sign.
