# L-26701 — Affine oversupport boundary lift

Claim ID: `L-26701`  
Title: Every finite signed carry certificate has an explicit nonnegative prime-boundary lift with one scalar charge  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Frozen base: PR #248 at `5f2b25f89afbb90a3bc4ca6d40148f530303eb54`  
Dependencies: PR #248 `L-24501`, `L-24508`, `L-24509`; Bertrand's postulate  
Scope: finite carry/prime-power algebra; no cofinal estimate and no RH conclusion

## 1. Carry response and objective

Fix an integer endpoint \(X\ge2\). For a real vector
\[
b=(b_2,\ldots,b_X),
\qquad b_{X+1}=0,
\]
and an integer \(q\ge2\), define
\[
\boxed{
v_q^{(X)}(b)
=
\sum_{kq\le X}\bigl(b_{kq}-b_{kq+1}\bigr).
}
\tag{L-26701.1}
\]

Let
\[
\mathcal Q_X=\{p^a:p^a\le X\}
\]
be the prime-power set. The physical objective is
\[
\boxed{
J_X(b)
=
\sum_{m=2}^X b_m\log\frac{m}{m-1}.
}
\tag{L-26701.2}
\]

The von Mangoldt divisor identity gives, for every real \(b\),
\[
\boxed{
J_X(b)
=
\sum_{q\in\mathcal Q_X}\Lambda(q)v_q^{(X)}(b).
}
\tag{L-26701.3}
\]

Indeed the coefficient of \(b_m\) on the right is
\[
\sum_{q\mid m}\Lambda(q)-\sum_{q\mid m-1}\Lambda(q)
=
\log m-\log(m-1).
\]

Let \(w_X(q)\) be any target values and put
\[
P_X(w)=\sum_{q\in\mathcal Q_X}\Lambda(q)w_X(q).
\tag{L-26701.4}
\]

## 2. A finite signed certificate and its deficit

Let \(a=(a_2,\ldots,a_X)\) be a nonnegative benchmark. Suppose a real vector
\(b=(b_2,\ldots,b_X)\) satisfies
\[
\boxed{
v_q^{(X)}(b)\le w_X(q)
\qquad(q\in\mathcal Q_X).
}
\tag{L-26701.5}
\]

No sign condition on \(b\) is assumed.

Define the uniform benchmark deficit
\[
\boxed{
C_X(a,b)
=
\max_{2\le m\le X}(a_m-b_m)_+.
}
\tag{L-26701.6}
\]

By Bertrand's postulate choose a prime
\[
\boxed{X<Y<2X.}
\tag{L-26701.7}
\]

Extend \(b\) by zero on \(X<m\le Y\), and define
\[
\boxed{
\widetilde b_m
=
\begin{cases}
b_m+C_X(a,b),&2\le m\le X,\\[1mm]
C_X(a,b),&X<m\le Y.
\end{cases}}
\tag{L-26701.8}
\]

Then
\[
\boxed{
\widetilde b_m\ge a_m\ge0\quad(2\le m\le X),
\qquad
\widetilde b_m\ge0\quad(X<m\le Y).
}
\tag{L-26701.9}
\]

Thus the signed finite certificate has been deformed into an explicitly
nonnegative vector.

## 3. The affine block creates only one new divisor charge

Let
\[
\mathbf c_Y(m)=\mathbf1_{2\le m\le Y}.
\]
A direct telescope gives
\[
\boxed{
v_q^{(Y)}(\mathbf c_Y)=\mathbf1_{q\mid Y}.
}
\tag{L-26701.10}
\]

Because \(Y\) is prime and \(Y>X\),
\[
v_q^{(Y)}(\mathbf c_Y)=0
\qquad(2\le q\le X).
\tag{L-26701.11}
\]

The zero extension of \(b\) has the same response at every \(q\le X\), hence
\[
\boxed{
v_q^{(Y)}(\widetilde b)
=
v_q^{(X)}(b)
\le w_X(q)
\qquad(q\in\mathcal Q_X).
}
\tag{L-26701.12}
\]

For prime powers in the oversupport interval,
\[
v_q^{(Y)}(\widetilde b)=0
\quad(X<q<Y),
\qquad
v_Y^{(Y)}(\widetilde b)=C_X(a,b).
\tag{L-26701.13}
\]

The affine correction therefore has no old divisor charge and one new boundary
charge at the oversupport prime \(Y\).

In the adjacent-flow notation of PR #254, this correction is the constant
incidence block
\[
C_X(a,b)\mathbf1_{1<m\le Y}.
\]
Its physical potential is affine and has zero interior second difference. The
construction is consequently an exact bridge from the Green gauge to the
constraint-dipole gauge.

## 4. Exact objective inequality

The constant block telescopes:
\[
\sum_{m=2}^{Y}\log\frac{m}{m-1}=\log Y,
\qquad
\sum_{m=X+1}^{Y}\log\frac{m}{m-1}=\log\frac YX.
\tag{L-26701.14}
\]

Hence
\[
J_Y(\widetilde b)
=
J_X(b)+C_X(a,b)\log Y.
\tag{L-26701.15}
\]

By (L-26701.5) and the nonnegativity of \(\Lambda\),
\[
J_X(b)\le P_X(w).
\tag{L-26701.16}
\]

By (L-26701.9),
\[
J_Y(\widetilde b)
\ge
J_X(a)+C_X(a,b)\log\frac YX.
\tag{L-26701.17}
\]

Combining the last three displays cancels the arbitrary prime \(Y\):
\[
\boxed{
P_X(w)
\ge
J_X(a)-C_X(a,b)\log X.
}
\tag{L-26701.18}
\]

If \(b\) satisfies equality in every old carry constraint, then
\[
J_Y(\widetilde b)
=
P_X(w)+C_X(a,b)\log Y
\tag{L-26701.19}
\]
exactly.

## 5. Why this is an actual construction

For every finite endpoint, once any signed feasible vector \(b\) is supplied,
the theorem explicitly emits:

```text
one prime Y in (X,2X),
one scalar boundary charge C_X(a,b),
one nonnegative oversupported vector tilde b,
all old carry responses,
one new boundary response at Y,
and the exact objective ledger.
```

No positivity-preserving homotopy, limiting compactness argument, or finite
cover theorem remains at this step.

The construction is stronger than simply clipping negative coordinates:
clipping would perturb many old prime-power constraints. The affine lift is in
the exact old-constraint null direction and pays only one controlled boundary
atom.

## 6. Proof boundary

Closed exactly:

1. nonnegative deformation of every signed feasible vector;
2. preservation of every old prime-power constraint;
3. isolation of one oversupport-prime boundary charge;
4. the exact objective inequality (L-26701.18);
5. the adjacent-flow/constraint-dipole interpretation.

Open:

1. a subpower bound for the least boundary charge in the actual parabolic
   problem;
2. the RH conclusion.
