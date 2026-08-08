# L-27801 — Third-Abel kernel and complete monotonicity of the critical carry source

Claim ID: `L-27801`  
Title: Producer positivity reduces exactly to a third cumulative kernel plus an endpoint collar for the critical source  
Status: **PROPOSED EXACT REDUCTION — THIRD-KERNEL SIGN THEOREM OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #277 `L-23811/L-23814`; `R-27801`  
Scope: source-specific attack on binary–ternary producer positivity

## 1. Producer kernel

At endpoint `X`, let `K_X(n,q)` be the linear response defined by

\[
A_w(n)=\sum_{q=2}^{X}K_X(n,q)w(q),
\tag{L-27801.1}
\]

where `A_w` is the exact binary–ternary producer obtained from the Möbius divergence of the target `w`.

Define the third cumulative producer kernel

\[
\boxed{
S_X(n,Q)=
\sum_{q=2}^{Q}\binom{Q-q+2}{2}K_X(n,q)
}
\tag{L-27801.2}
\]

for `2<=Q<=X`. Equivalently, `S_X(n,Q)` is the producer coefficient at node `n` for the integer target

\[
w_Q^{(3)}(q)=\binom{Q-q+2}{2}1_{q\le Q}.
\]

Because third backward differences invert the third prefix operation, `K_X(n,.)` is the third backward difference of `S_X(n,.)` with the zero convention below column two. Consequently finite summation by parts gives an exact representation of `A_w(n)` as third differences of `w` paired with `S_X(n,Q)`, with all right-end boundary terms retained.

A convenient zero-extension form is

\[
\boxed{
A_w(n)=
\sum_{Q=2}^{X}S_X(n,Q)
\bigl[w(Q)-3w(Q+1)+3w(Q+2)-w(Q+3)\bigr],
}
\tag{L-27801.3}
\]

where `w(X+1)=w(X+2)=w(X+3)=0`. Equation (L-27801.3) is a finite algebra identity, not an asymptotic approximation.

`R-27801` shows that one or two cumulative integrations are insufficient. The third prefix is the first candidate surviving exact stress tests.

## 2. Complete monotonicity of the actual source

The critical target is the restriction to integers of

\[
f_X(x)=x^{-1/2}\log(X/x),\qquad 0<x\le X.
\tag{L-27801.4}
\]

Put `L=log(X/x)`. For every `k>=0`, there is a polynomial `P_k(L)` such that

\[
\boxed{
(-1)^k f_X^{(k)}(x)=x^{-k-1/2}P_k(L).
}
\tag{L-27801.5}
\]

The polynomials obey

\[
P_0(L)=L,
\qquad
P_{k+1}(L)=\left(k+\frac12\right)P_k(L)+P_k'(L).
\tag{L-27801.6}
\]

Induction shows that every coefficient of `P_k` is nonnegative. Hence

\[
oxed{(-1)^k f_X^{(k)}(x)\ge0}
\qquad(0<x\le X,\;k\ge0).
\tag{L-27801.7}
\]

Thus `f_X` is completely monotone on its finite source interval.

Repeated use of

\[
g(q)-g(q+1)=\int_q^{q+1}-g'(t)dt
\]

then gives, whenever all arguments stay inside `[1,X]`, the discrete sign

\[
oxed{
 w_X(Q)-3w_X(Q+1)+3w_X(Q+2)-w_X(Q+3)\ge0
}
\tag{L-27801.8}
\]

for `Q+3<=X`.

This is precisely the source feature unavailable to the false generic and second-Abel surrogates.

## 3. The endpoint obstruction is finite and explicit

The zero extension in (L-27801.3) is not completely monotone across `X`. The last three coefficients are

\[
\begin{aligned}
 d_{X-2}&=w_X(X-2)-3w_X(X-1),\\
 d_{X-1}&=w_X(X-1),\\
 d_X&=w_X(X)=0.
\end{aligned}
\tag{L-27801.9}
\]

In particular `d_(X-2)` need not be nonnegative. Therefore an argument saying merely

```text
third cumulative kernel >= 0 + complete monotonicity => producer >= 0
```

is incomplete: the endpoint collar has to be paid exactly.

More generally choose a collar width `L_X>=3` and split (L-27801.3) into

\[
A_{w_X}(n)=I_X(n)+B_X(n),
\tag{L-27801.10}
\]

where

\[
I_X(n)=
\sum_{Q=2}^{X-L_X-1}S_X(n,Q)\Delta_3w_X(Q)
\tag{L-27801.11}
\]

and `B_X(n)` is the exact remaining finite sum over the last `L_X+1` columns. Here

\[
\Delta_3w(Q)=w(Q)-3w(Q+1)+3w(Q+2)-w(Q+3).
\]

By (L-27801.8), every coefficient in `I_X` is nonnegative.

## 4. Third-Abel Collar Positivity criterion

The following two statements are sufficient for producer positivity:

1. **Interior third-kernel positivity**
   \[
   S_X(n,Q)\ge0
   \quad(2\le n\le X,\;2\le Q\le X-L_X-1);
   \tag{L-27801.12}
   \]
2. **source-bound collar positivity**
   \[
   B_X(n)\ge0
   \quad(2\le n\le X).
   \tag{L-27801.13}
   \]

Then `I_X(n)>=0` and therefore

\[
\boxed{A_X(n)=A_{w_X}(n)\ge0.}
\tag{L-27801.14}
\]

No positivity statement is required for arbitrary targets, for the raw kernel, or for the second cumulative kernel.

A proof with an absolute or polylogarithmic collar width would be especially auditable, but any explicit source-bound collar theorem closing (L-27801.12)--(L-27801.13) cofinally is enough for the conditional RH chain of `T-27801`.

## 5. Finite evidence and its exact boundary

`X-27801` verifies with `Fraction` arithmetic:

```text
raw producer kernel has a negative entry             exact
second cumulative producer has the -13/16 witness   exact
third cumulative producer kernel                     >=0
for every 2<=Q,n<=80                                 6,241 rows
```

The third item is finite reconnaissance. It is not promoted to (L-27801.12) for all `X`.

Separate numerical exploration suggests that a short endpoint collar can absorb the zero-extension defect at much larger finite levels, but no such numerical observation enters this lemma as proof.

## 6. Why this route is genuinely source-specific

The sequence of statements is now fail-closed:

```text
K_X >= 0                                  FALSE
second prefix of K_X >=0                  FALSE
third prefix of K_X >=0                   OPEN
actual w_X has nonnegative interior Δ^3   PROVED
actual endpoint collar                    OPEN
```

This is exactly the kind of theorem left visible by the scope audit. The failed ambient surrogates no longer obscure the stronger arithmetic question.

## 7. Proof boundary

Proved here:

- exact third-Abel summation identity;
- complete monotonicity of `x^-1/2 log(X/x)`;
- nonnegative interior discrete third differences;
- exact separation of the endpoint collar;
- `third-kernel + collar positivity => producer positivity`.

Open:

- cofinal nonnegativity of `S_X(n,Q)` in the required interior;
- an exact uniform collar theorem;
- producer positivity;
- RH.
