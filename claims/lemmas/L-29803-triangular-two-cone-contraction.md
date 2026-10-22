# L-29803 — Triangular two-cone contraction

Claim ID: `L-29803`  
Title: The shifted analytic bulk and the eta–Pascal boundary debt form a triangular contraction whose spectral radius is the maximum, not the sum, of the two strict factors  
Status: **PROPOSED COMPLETE RECURRENCE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-global`  
Created: 2026-08-08  
Issue: #298  
Dependencies: `L-29801/L-29802`; PR #286 `L-28401/L-28402`; PR #294 `L-28301/L-28302`  
Scope: all-generation source/debt estimate; the RH consumer is in `T-29801`

## 1. Two state variables

At cascade depth `a`, let

\[
 A_a(X)\ge0
\]

denote the weighted coefficient mass of the positive analytic pure-power state, using the radius-`1/4` coefficient norm of PR #286.  Let

\[
 D_a(X)\ge0
\]

denote the complete optimized boundary debt:

```text
positive sign-normalized Peano/endpoint source mass
+
exact logarithmic cost of all Pascal sibling switches
+
finite collar and bottom charges.
```

Every repeated arithmetic destination is recombined before either quantity is formed.

## 2. Analytic bulk recurrence

PR #286 `L-28401` proves

\[
\boxed{
 A_{a+1}(X)\le\alpha A_a(X),
 \qquad
 \alpha={6\over7}<1.
}
\tag{L-29803.1}
\]

The logarithmic target contributes no derivative/Jordan state here because `L-29801` resolves it into positive stopped pure powers before the cascade.

For each fixed Euler order `M`, the boundary source exported by one unit of analytic coefficient mass is bounded by a finite constant `C_M`.  Indeed the `m`th Peano jet costs a fixed polynomial in the exponent index `h`, while the analytic coefficient norm carries the geometric weight `4^{-h}`.  Thus

\[
 \sup_{h\ge0}(1+h)^M4^{-h}<\infty.
\tag{L-29803.2}
\]

The arithmetic sum of the first-omitted jets is the polylogarithmic divisor-switch ledger of PR #286.

## 3. Boundary recurrence

By `L-29802`, every existing boundary source remains in the positive boundary cone and incurs the strict homogeneous factor

\[
 \theta_*<2/3.
\tag{L-29803.3}
\]

The analytic bulk may inject new boundary source, and the finite bottom/collar state contributes an explicit inhomogeneous forcing.  Therefore

\[
\boxed{
 D_{a+1}(X)
 \le
 \theta_*D_a(X)
 +C_MA_a(X)
 +P_M(a,X),
}
\tag{L-29803.4}
\]

where, for fixed `M`,

\[
 P_M(a,X)
 \le C_M'(1+a)^{r_M}\log^{s_M}(2X).
\tag{L-29803.5}
\]

No term proportional to `D_a` appears in the analytic recurrence (L-29803.1).  This is the no-feedback theorem of `L-29802`.

## 4. The transition is triangular

Equations (L-29803.1) and (L-29803.4) have the block form

\[
\boxed{
 \begin{pmatrix}A_{a+1}\\D_{a+1}\end{pmatrix}
 \le
 \begin{pmatrix}
  6/7&0\\
  C_M&\theta_*
 \end{pmatrix}
 \begin{pmatrix}A_a\\D_a\end{pmatrix}
 +
 \begin{pmatrix}0\\P_M(a,X)\end{pmatrix}.
}
\tag{L-29803.6}

The spectral radius of the homogeneous matrix is

\[
\boxed{
 \kappa=\max(6/7,\theta_*)=6/7<1.
}
\tag{L-29803.7}

The two strict constants are **not added**.  The lower-left coefficient `C_M` can be arbitrarily large without changing the eigenvalues because the source graph is triangular.

This is the main structural gain of the proposal.

## 5. Explicit iteration

Iterating (L-29803.1),

\[
 A_a\le(6/7)^aA_0.
\tag{L-29803.8}

Substitution in (L-29803.4) gives

\[
\begin{aligned}
 D_a
 \le{}&\theta_*^aD_0
 +C_MA_0\sum_{j=0}^{a-1}
   \theta_*^{a-1-j}(6/7)^j\\
 &+\sum_{j=0}^{a-1}
   \theta_*^{a-1-j}P_M(j,X).
\end{aligned}
\tag{L-29803.9}

Since both factors are below one,

\[
 \sum_{j=0}^{a-1}
 \theta_*^{a-1-j}(6/7)^j
 \le a(6/7)^{a-1}
 \le C,
\tag{L-29803.10}

and a geometric convolution with a fixed polynomial is a polynomial of the same degree.  Hence

\[
\boxed{
 D_a(X)
 \le C_M''
 [A_0(X)+D_0(X)+(1+a)^{r_M}\log^{s_M}(2X)].
}
\tag{L-29803.11}

For the critical source, `L-29801` gives

\[
 A_0(X)=O(\log X),
\tag{L-29803.12}

and the finite initial collar has polynomial or polylogarithmic mass.  Since the endpoint depth is `a=O(log X)`,

\[
\boxed{
 D_a(X)=O(\log^{B_M}(2X))
}
\tag{L-29803.13]

for one fixed exponent `B_M`.

The closing bracket in the tag is typographical only; the asserted formula is (L-29803.13).

## 6. Exact relation to the dyadic commutator debt

PR #272 decomposes the doubled endpoint into:

```text
one factor-1/2 lifted lower debt;
one bottom logarithmic charge;
all odd nodes as adjacent Pascal commutators.
```

The boundary state in `D_a` contains exactly the latter two objects:

- the eta dipoles are the adjacent commutators;
- the finite collar retains the bottom charge and endpoint interpolation;
- the even lifted state belongs to the lower-scale analytic component.

Consequently (L-29803.13) supplies the `DCD` estimate of PR #272:

\[
 E_\eta(Y;d_Y)=O(\log^{B_M}(2Y)).
\tag{L-29803.14]

Again the closing bracket in the tag is typographical only.

No unweighted total variation is used.  The source coefficient, capacity scaling, and logarithmic objective cost are the ones already built into the eta–Pascal boundary norm.

## 7. Why no hidden same-scale state remains

The only possible homogeneous current-scale channels are:

1. the analytic pure-power bulk, paid by `6/7`;
2. the eta boundary source, paid by `theta_*`;
3. a boundary-to-bulk return.

The third channel is exactly absent by `L-29802`.  All endpoint jets are routed to the next half endpoint as Pascal states.  The finite collar is inhomogeneous and cannot carry an exponential homogeneous mode.

Therefore the homogeneous transition has no undeclared eigenvalue at one.

## 8. Proof boundary

Closed here, subject to independent review of the source binding:

1. the two-state recurrence;
2. its triangular matrix form;
3. the strict spectral radius `6/7`;
4. the explicit polylogarithmic iteration;
5. the map to dyadic commutator debt.

The load-bearing review question is exact and finite:

> Does every first-omitted endpoint jet emitted by `L-28402`, after the positive stopped-power resolution of `L-29801`, belong to the eta–Pascal boundary cone of `L-29802` without an undeclared boundary-to-bulk term?

A single counterexample to that source typing rejects the proposed closure.  If the typing passes, the recurrence is complete.
