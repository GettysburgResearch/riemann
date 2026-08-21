# L-93017 - Cycle Debt is one carry-coordinate discrepancy LP with a bottom-free dyadic borrowing recurrence

Claim ID: `L-93017`  
Status: **PROPOSED COMPLETE EXACT FINITE NORMAL FORM - INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-26205`, `L-27205`, `L-93010`, `L-93014`  
Scope: the exact finite balanced Cycle-Debt LP and its critical dyadic scaling; no bound for the final parity-borrowing functional and no RH conclusion

## 1. Carry potentials are a triangular basis

Fix an endpoint `X`, an allowed balanced split family, and positive column
weights

\[
a_q>0,\qquad 2\le q\le X.
\tag{L-93017.1}
\]

For every carry column define the potential

\[
g_q(n)=a_q\left\lfloor\frac nq\right\rfloor,
\qquad 1\le n\le X.
\tag{L-93017.2}
\]

The matrix

\[
\left(g_q(n)\right)_{2\le n,q\le X}
\]

is lower triangular and has diagonal entry \(a_n>0\). Hence every potential
\(H\) with \(H(1)=0\) has one unique carry-coordinate expansion

\[
\boxed{
H(n)=\sum_{q=2}^{n}\theta_H(q)\,
a_q\left\lfloor\frac nq\right\rfloor.
}
\tag{L-93017.3}
\]

The coefficients are recovered recursively by

\[
\boxed{
\theta_H(n)
=
\frac1{a_n}
\left[
H(n)
-\sum_{q=2}^{n-1}
\theta_H(q)a_q\left\lfloor\frac nq\right\rfloor
\right].
}
\tag{L-93017.4}
\]

No analytic limit or arithmetic source theorem enters this change of
coordinates.

## 2. Split defects become carry-set discrepancies

For an allowed split \(e=(n,j)\), \(k=n-j\), write

\[
\chi_e(q)
=
\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac kq\right\rfloor
\in\{0,1\}.
\tag{L-93017.5}
\]

Then

\[
\boxed{
\delta_H(e)
=
H(n)-H(j)-H(k)
=
\sum_{q=2}^{n}\theta_H(q)a_q\chi_e(q).
}
\tag{L-93017.6}
\]

The capacity potential is

\[
\mathcal G(n)
=
\sum_{q=2}^{n}
a_q\left\lfloor\frac nq\right\rfloor,
\tag{L-93017.7}
\]

so its carry coordinates are identically one and

\[
W_e:=\delta_{\mathcal G}(e)
=
\sum_{q=2}^{n}a_q\chi_e(q).
\tag{L-93017.8}
\]

Consequently the centered capacity ball of `L-93014` is exactly the finite
carry-discrepancy polytope

\[
\boxed{
\mathcal D_X
=
\left\{
\theta\in\mathbb R^{X-1}:
\left|
\sum_q\theta(q)a_q\chi_e(q)
\right|
\le\frac12 W_e
\quad\text{for every allowed }e
\right\}.
}
\tag{L-93017.9}
\]

## 3. The critical objective is diagonal in carry coordinates

Let \(t(q)\) be any prescribed carry target and let \(r^{(t)}\) be its exact
size-zero divergence from `L-26205`. By definition,

\[
\left\langle r^{(t)},
\left\lfloor\frac{\cdot}{q}\right\rfloor
\right\rangle
=t(q).
\tag{L-93017.10}
\]

Put

\[
\ell(q)=a_qt(q).
\tag{L-93017.11}
\]

Then the carry basis diagonalizes the complete dual objective:

\[
\boxed{
\langle r^{(t)},H\rangle
=
\sum_{q=2}^{X}\theta_H(q)\ell(q).
}
\tag{L-93017.12}
\]

For the critical target and capacity weights,

\[
a_q=q^{-1/2},
\qquad
t_X(q)=q^{-1/2}\log\frac Xq,
\tag{L-93017.13}
\]

one has

\[
\boxed{
\ell_X(q)=\frac{\log(X/q)}q.
}
\tag{L-93017.14}
\]

In particular,

\[
K_X=\sum_{q=2}^{X}\ell_X(q)
\tag{L-93017.15}
\]

is the fixed positive capacity baseline of `L-27205/L-93014`.

## 4. Remove the baseline and the absolute value exactly

Write an asymmetric Cycle-Debt dual potential as

\[
F(n)=\sum_{q=2}^{n}\lambda(q)a_q
\left\lfloor\frac nq\right\rfloor.
\tag{L-93017.16}
\]

The constraints

\[
0\le\delta_F(e)\le W_e
\tag{L-93017.17}
\]

are equivalent, after setting

\[
\psi(q)=-\lambda(q),
\tag{L-93017.18}
\]

to

\[
\boxed{
-W_e
\le
\sum_q\psi(q)a_q\chi_e(q)
\le0
\quad\text{for every allowed }e.
}
\tag{L-93017.19}
\]

Define the one-sided negative carry-discrepancy polytope

\[
\boxed{
\mathcal Q_X
=
\left\{
\psi:
-W_e\le
\sum_q\psi(q)a_q\chi_e(q)
\le0
\ \text{for every allowed }e
\right\}.
}
\tag{L-93017.20}
\]

The exact Cycle-Debt value is therefore

\[
\boxed{
\mathfrak N_X
=
\max_{\psi\in\mathcal Q_X}
\sum_{q=2}^{X}\psi(q)\ell_X(q).
}
\tag{L-93017.21}
\]

This is the baseline-free version of the centered identity

\[
\mathfrak S_X=\mathfrak N_X+\frac12K_X.
\]

The new form has three useful properties:

1. the objective is already one-sided;
2. the source vector no longer appears explicitly;
3. every constraint is a carry-set discrepancy inequality.

The actual square roots and logarithms remain in the declared weights
\(a_q,\ell_X(q)\), but there is no approximate source equality to authenticate.

## 5. Exact positive dual certificate

Let \(A\) be the split-by-carry matrix

\[
A_{e,q}=a_q\chi_e(q),
\qquad
W=A\mathbf1.
\tag{L-93017.22}
\]

Finite LP duality applied to (L-93017.21) gives

\[
\boxed{
\mathfrak N_X
=
\min_{\substack{u,v\ge0\\A^T(u-v)=\ell_X}}
W^Tv.
}
\tag{L-93017.23}
\]

Thus a proof-producing upper certificate consists of:

```text
nonnegative split multipliers u and v;
one exact symbolic or directed identity A^T(u-v)=ell_X;
one nonnegative cost W^T v.
```

This is a dual upper theorem, unlike the primal source certificate corrected by
`R-93016`. It can be checked directly in carry coordinates.

## 6. The bottom coordinate can never increase Cycle Debt

The split \(2=1+1\) is allowed for every fixed balance parameter below
\(1/2\). Its carry set consists only of \(q=2\). Hence (L-93017.19) gives

\[
-a_2\le a_2\psi(2)\le0,
\]

or

\[
\boxed{-1\le\psi(2)\le0.}
\tag{L-93017.24}
\]

For the critical objective \(\ell_X(2)\ge0\), so

\[
\boxed{
\psi(2)\ell_X(2)\le0.
}
\tag{L-93017.25}
\]

The logarithmic bottom term that appears after taking an absolute value in the
centered recurrence of `L-93014` is therefore absent from the exact
baseline-free Cycle-Debt excess.

## 7. Bottom-free dyadic parity borrowing

Let \(X=2Y\). The critical objective has the exact scaling

\[
\ell_{2Y}(2r)
=
\frac12\ell_Y(r),
\qquad 2\le r\le Y.
\tag{L-93017.26}
\]

For \(\psi\in\mathcal Q_{2Y}\),

\[
\begin{aligned}
\sum_{q=2}^{2Y}\psi(q)\ell_{2Y}(q)
={}&
\frac{\psi(2)}2\log Y\\
&+\frac12\sum_{r=2}^{Y}
\psi(2r)\ell_Y(r)\\
&+\sum_{\substack{3\le q\le2Y\\q\ {\rm odd}}}
\psi(q)\ell_{2Y}(q).
\end{aligned}
\tag{L-93017.27}
\]

The first line is nonpositive by (L-93017.24). Define the
**one-sided parity-borrowing defect**

\[
\boxed{
\begin{aligned}
\mathfrak B_{2Y}
=
\Bigg[
&\sup_{\psi\in\mathcal Q_{2Y}}
\left\{
\frac12\sum_{r=2}^{Y}\psi(2r)\ell_Y(r)
+
\sum_{\substack{3\le q\le2Y\\q\ {\rm odd}}}
\psi(q)\ell_{2Y}(q)
\right\}\\
&-\frac12\mathfrak N_Y
\Bigg]_+.
\end{aligned}
}
\tag{L-93017.28}
\]

Then

\[
\boxed{
\mathfrak N_{2Y}
\le
\frac12\mathfrak N_Y+\mathfrak B_{2Y}.
}
\tag{L-93017.29}
\]

There is no additive bottom logarithm.

The interpretation is exact. The even coordinates \(\psi(2r)\) inherit half
of the lower objective. Odd coordinates may contribute directly, and may also
lend cancellation in doubled split constraints so that the even restriction
need not lie in \(\mathcal Q_Y\). Both effects remain coupled inside the single
LP (L-93017.28).

A sufficient zero-borrowing condition is:

```text
the even restriction r -> psi(2r) belongs to Q_Y;
every odd coordinate with positive objective weight is nonpositive.
```

The theorem does not assert that condition.

## 8. The reduced closing theorem

The remaining Cycle-Debt theorem may now be stated as:

> **One-sided Parity Borrowing (`OPB`).** There are fixed constants \(A,C\)
> such that
> \[
> \mathfrak B_{2Y}\le C\log^A(2Y)
> \]
> for all sufficiently large \(Y\).

If OPB holds, the strict recurrence (L-93017.29) gives

\[
\mathfrak N_X=O(\log^A(2X))
\]

on even endpoints. The unit-endpoint interpolation of `L-27208` extends the
bound to all endpoints. `L-27205` then yields the sharp prime ramp and the
resident Mellin-Landau consumer yields RH.

Thus

\[
\boxed{
\mathrm{OPB}
\Longrightarrow
\text{polylogarithmic Cycle Debt}
\Longrightarrow
\mathrm{RH}.
}
\tag{L-93017.30}
\]

OPB is not proved here.

## 9. Relation to CDP

`CDP` in `L-93014` is a symmetric support-function statement for

\[
\mathfrak S_X=\mathfrak N_X+\frac12K_X.
\]

`OPB` is the translated one-sided statement for \(\mathfrak N_X\) itself.
The two formulations retain the same odd/even cancellation, but `OPB` removes:

```text
the fixed K_X/2 baseline;
the absolute-value orientation;
the artificial + (1/4) log Y bottom payment.
```

For a final upper theorem, `OPB` is the sharper interface.

## 10. Proof boundary

Established exactly:

1. triangular carry-coordinate basis for every node potential;
2. exact discrepancy form of every split constraint;
3. diagonalization of the target objective;
4. baseline-free one-sided Cycle-Debt LP;
5. positive split-multiplier dual certificate;
6. nonpositive bottom-coordinate contribution;
7. factor-one-half bottom-free dyadic recurrence.

Open:

1. the polylogarithmic OPB bound;
2. polylogarithmic Cycle Debt;
3. RH.
