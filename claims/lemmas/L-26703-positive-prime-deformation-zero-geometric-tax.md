# L-26703 — Positive prime deformation has zero geometric tax

Claim ID: `L-26703`  
Title: The parabolic seed can be deformed inside the nonnegative coordinate cone to the exact ordinary-prime optimum; only the prime-ramp scalar remains  
Status: **PROPOSED COMPLETE FINITE THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Frozen base: PR #248 at `5f2b25f89afbb90a3bc4ca6d40148f530303eb54`  
Dependencies: `L-24501`, `L-24507`, `L-24517`; finite linear-programming duality  
Scope: ordinary-prime carry system at every integer `X>=104301`; no estimate of the prime ramp and no RH conclusion

## 1. Ordinary-prime carry system

Fix an integer

\[
X\ge104301.
\]

Let

\[
\mathcal P_X=\{p\le X:p\text{ prime}\}
\]

and for a real vector `b=(b_2,...,b_X)` put

\[
(V_X^{\mathbb P}b)_p
=\sum_{kp\le X}(b_{kp}-b_{kp+1}),
\qquad b_{X+1}=0.
\tag{L-26703.1}
\]

The target is

\[
w_X(p)=p^{-1/2}\log(X/p).
\tag{L-26703.2}
\]

For the parabolic seed `b_X^(0)` define

\[
r_X(p)
=(V_X^{\mathbb P}b_X^{(0)})_p-w_X(p).
\tag{L-26703.3}
\]

The ordinary-prime objective is

\[
J_{\mathbb P,X}(b)
=\sum_{p\le X}(\log p)(V_X^{\mathbb P}b)_p.
\tag{L-26703.4}
\]

Equivalently,

\[
J_{\mathbb P,X}(b)
=\sum_{m=2}^X c_X(m)b_m,
\tag{L-26703.5}
\]

where

\[
\boxed{
c_X(m)=\log\operatorname{rad}(m)-\log\operatorname{rad}(m-1).
}
\tag{L-26703.6}
\]

Indeed each ordinary prime contributes once to `log rad(n)`.

Put

\[
P_X=\sum_{p\le X}\frac{\log p}{\sqrt p}\log(X/p).
\tag{L-26703.7}
\]

Every ordinary-prime feasible vector satisfies

\[
J_{\mathbb P,X}(b)\le P_X.
\tag{L-26703.8}
\]

## 2. A finite rigidity lemma for strongly additive monotone potentials

Let nonnegative numbers `a_p`, indexed by the primes `p<=X`, define the strongly additive function

\[
A(n)=\sum_{p\mid n}a_p,
\qquad A(1)=0.
\tag{L-26703.9}
\]

Assume

\[
A(1)\le A(2)\le\cdots\le A(X).
\tag{L-26703.10}
\]

Let

\[
R_X=2^{\lfloor\log_2X\rfloor},
\qquad X/2<R_X\le X.
\tag{L-26703.11}
\]

Then

\[
\boxed{
a_p=0\qquad(p\le R_X).}
\tag{L-26703.12}
\]

### Proof

The initial monotonicity chain gives

\[
a_2=A(2)\le A(3)=a_3\le A(4)=a_2,
\]

so `a_2=a_3`. Next,

\[
A(6)=a_2+a_3=2a_2
\le A(7)=a_7
\le A(8)=a_2.
\]

Since the coefficients are nonnegative,

\[
a_2=a_3=a_7=0.
\]

Then

\[
0\le A(5)=a_5\le A(6)=0,
\]

so `a_5=0`. In particular `A(8)=0`.

For every power of two `2^k<=X`, strong additivity gives

\[
A(2^k)=a_2=0.
\]

By monotonicity and nonnegativity,

\[
0\le A(n)\le A(R_X)=0
\qquad(1\le n\le R_X).
\]

Thus `A(n)=0` throughout the prefix and, at `n=p`, every prime coefficient with `p<=R_X` vanishes. QED.

The lemma is finite and elementary. It is a special exact version of the classical rigidity phenomenon that a monotone additive arithmetic function must be logarithmic; no global classification theorem is imported here.

## 3. The nonnegative correction cone is nonempty

Consider the finite system

\[
\boxed{
h_m\ge0,
\qquad
V_X^{\mathbb P}h\le-r_X.
}
\tag{L-26703.13}
\]

It is feasible.

### Proof by Farkas

If it were infeasible, finite Farkas duality would give a vector `y_p>=0` such that

\[
(V_X^{\mathbb P})^Ty\ge0
\tag{L-26703.14}
\]

and

\[
\sum_{p\le X}y_pr_X(p)>0.
\tag{L-26703.15}
\]

Define

\[
Y_y(n)=\sum_{p\mid n}y_p.
\tag{L-26703.16}
\]

The transpose identity is

\[
\boxed{
((V_X^{\mathbb P})^Ty)_m
=Y_y(m)-Y_y(m-1).
}
\tag{L-26703.17}
\]

Thus (L-26703.14) says that `Y_y` is nondecreasing. Section 2 implies

\[
y_p=0\qquad(p\le R_X).
\tag{L-26703.18}
\]

But `R_X>X/2>X/28`. The certified outer-feasibility theorem `L-24507` gives

\[
r_X(p)\le0
\qquad(p>R_X).
\tag{L-26703.19}
\]

Equations (L-26703.18)--(L-26703.19) contradict (L-26703.15). Therefore the cone (L-26703.13) is nonempty.

This is already a positivity-preserving deformation theorem: adding `h>=0` to the nonnegative parabolic seed repairs every ordinary-prime constraint.

## 4. Exact zero-tax optimum

Among the vectors in (L-26703.13), maximize the objective increment

\[
\Phi_X
=\max\left\{
\sum_{m=2}^Xc_X(m)h_m:
 h\ge0,
 V_X^{\mathbb P}h\le-r_X
\right\}.
\tag{L-26703.20}
\]

Then

\[
\boxed{
\Phi_X
=P_X-J_{\mathbb P,X}(b_X^{(0)}).
}
\tag{L-26703.21}
\]

Consequently there exists an explicit finite nonnegative correction `h_X` such that

\[
\boxed{
b_X^{+}=b_X^{(0)}+h_X\ge0,
}
\tag{L-26703.22}
\]

\[
\boxed{
V_X^{\mathbb P}b_X^{+}\le w_X,
}
\tag{L-26703.23}
\]

and

\[
\boxed{
J_{\mathbb P,X}(b_X^{+})=P_X.
}
\tag{L-26703.24}
\]

Thus imposing positivity on the physical coordinates costs **nothing beyond the exact scalar ordinary-prime deficit itself**.

### Dual proof

The dual of (L-26703.20) is

\[
\Phi_X
=\min\left\{
-\sum_{p\le X}y_pr_X(p):
 y_p\ge0,
 (V_X^{\mathbb P})^Ty\ge c_X
\right\}.
\tag{L-26703.25}
\]

The choice

\[
y_p=\log p
\tag{L-26703.26}
\]

is feasible with equality because

\[
Y_y(n)=\log\operatorname{rad}(n)
\]

and (L-26703.17) becomes (L-26703.6). Its dual value is

\[
-\sum_p(\log p)r_X(p)
=P_X-J_{\mathbb P,X}(b_X^{(0)}).
\tag{L-26703.27}
\]

Now let `y` be any dual-feasible vector and put

\[
a_p=y_p-\log p,
\qquad
A(n)=\sum_{p\mid n}a_p.
\tag{L-26703.28}
\]

Dual feasibility is exactly

\[
A(m)-A(m-1)\ge0.
\tag{L-26703.29}
\]

Since `A(1)=0`, monotonicity gives `a_p=A(p)>=0`. Section 2 therefore applies and yields

\[
a_p=0\qquad(p\le R_X).
\tag{L-26703.30}
\]

For `p>R_X`, one only knows `a_p>=0`, but (L-26703.19) gives `r_X(p)<=0`. Hence

\[
\begin{aligned}
\sum_py_pr_X(p)
&=\sum_p(\log p)r_X(p)+\sum_{p>R_X}a_pr_X(p)\\
&\le J_{\mathbb P,X}(b_X^{(0)})-P_X.
\end{aligned}
\tag{L-26703.31}
\]

Thus every dual value is at least the value in (L-26703.27), proving (L-26703.21) by finite strong duality.

## 5. Construction and review interface

A proof-producing instance consists only of the finite LP (L-26703.20). Any exact rational/interval LP implementation may emit:

```text
nonnegative correction h_X;
all ordinary-prime residuals;
objective interval;
dual weights y_p;
transpose inequalities;
primal-dual equality.
```

The theorem proves existence at every `X>=104301`, independently of a numerical solver.

The construction is compatible with the affine oversupport lift `L-26701`: if one needs a full prime-power nonnegative certificate, higher powers can first be removed at the `O(log^2 X)` scale by `L-24517`, and a final affine boundary block can absorb any remaining uniform coordinate defect.

## 6. What this theorem changes

The following issues are no longer load bearing for the ordinary-prime route:

- preservation of physical-coordinate positivity;
- existence of a defect-to-slack transport;
- blocker forests or convergence of a signed flow;
- a monotone positive-part cover;
- the full Green-energy norm;
- pointwise positivity of the canonical Möbius Green solution.

They are replaced by one finite positive deformation whose optimum is exact.

But (L-26703.24) also shows the sharp boundary: the constructed objective is the actual unknown prime ramp. The theorem cannot by itself prove

\[
P_X\ge4\sqrt X-X^{o(1)}.
\]

The positivity geometry is closed; the scalar arithmetic inequality remains.

## 7. Proof boundary

Closed here, subject to independent review:

1. finite rigidity of nonnegative strongly additive monotone potentials;
2. feasibility of a nonnegative correction to the parabolic seed;
3. exact primal-dual optimum;
4. a nonnegative ordinary-prime carry vector attaining the complete prime-ramp objective;
5. zero extra objective tax from positivity.

Open:

1. the critical lower bound for `P_X`;
2. an independent source-specific estimate on the logarithmic dual ray;
3. RH.
