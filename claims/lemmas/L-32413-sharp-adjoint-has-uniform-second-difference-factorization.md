# L-32413 — Every SHARP row adjoint factors through one second-difference kernel

Claim ID: `L-32413`  
Title: After removing the universal total-tail coordinate, the row-j average-carry adjoint is exactly `(1-x)^2` times a positive quadratic-prefix kernel  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #329 `L-32303`; `L-32411`  
Scope: exact row-adjoint factorization; no positivity conclusion

## 1. Exact row adjoint

Let `u(m)` be the multiples-Mobius state of an arbitrary finite carry target at endpoint `T`. PR #329 gives

\[
 N_j:=j(j-1)c(j)
 =(j+1)[j u(j)-(j-2)u(j+1)]
 +2\sum_{m=j+2}^{T}u(m).
\tag{L-32413.1}
\]

Let

\[
 H=\sum_{m=1}^{T}u(m).
\]

Subtract the universal tail `2H`. Then

\[
\boxed{
 N_j=2H+\sum_{m=1}^{j+1}d_j(m)u(m),
}
\tag{L-32413.2}

where

\[
 d_j(m)=
 \begin{cases}
 -2,&1\le m\le j-1,\\
 (j-1)(j+2),&m=j,\\
 -j(j-1),&m=j+1,\\
 0,&m\ge j+2.
 \end{cases}
\tag{L-32413.3}

## 2. Uniform polynomial factorization

Define the ordinary finite generating polynomial

\[
 D_j(x)=\sum_{m\ge1}d_j(m)x^m.
\]

Then, for every `j>=2`,

\[
\boxed{
 D_j(x)
 =-2x(1-x)^2
   \sum_{r=0}^{j-2}\binom{r+2}{2}x^r.
}
\tag{L-32413.4}

### Proof

The standard finite identity

\[
 \sum_{r=0}^{J}\binom{r+2}{2}x^r
\]

is the degree-`J` truncation of `(1-x)^-3`. Multiplication by `(1-x)^2` leaves a finite first-difference tail. A direct coefficient comparison gives

```text
x^1,...,x^(j-1):  -2;
x^j:                (j-1)(j+2);
x^(j+1):            -j(j-1);
higher powers:       0,
```

after multiplication by `-2x`, exactly (L-32413.3).

Thus every row has the same double zero at `x=1`; the row dependence is confined to one positive quadratic-prefix polynomial.

## 3. Second-difference form

Write the forward second difference

\[
 \Delta^2u(m)=u(m)-2u(m+1)+u(m+2).
\]

Discrete summation by parts applied to (L-32413.4) gives

\[
\boxed{
 N_j
 =2H
 -2\sum_{r=0}^{j-2}inom{r+2}{2}\Delta^2u(r+1).
}
\tag{L-32413.5}

For the endpoint-vanishing square-root hinge,

\[
 H=h_T(1)=1-T^{-1/2}.
\]

Therefore

\[
\boxed{
 j(j-1)c_T(j)
 =2(1-T^{-1/2})
 -2\sum_{r=0}^{j-2}\binom{r+2}{2}\Delta^2u_T(r+1).
}
\tag{L-32413.6}

This is the same arithmetic content as the normalized-tail convexity theorem `L-32411`, but exposes the universal differential operator directly.

## 4. Relation to normalized-tail convexity

Let

\[
 S(j)=\sum_{m=j}^{T}u(m),
 \qquad
 V(j)={S(j)\over j-1}.
\]

`L-32411` gives

\[
 c_T(j)=(j+1)\Delta^2V(j).
\]

Equations (L-32413.5)--(L-32413.6) show why: the apparent triangular inverse first removes the universal total tail, then applies one second difference, and finally integrates that second difference against the positive quadratic-prefix Green kernel.

Thus the row index is not an independent combinatorial complexity. Every row probes the same second-difference arithmetic at a different positive prefix depth.

## 5. Firewall

The sequence `Delta^2 u_T(m)` is not one-signed in general. Therefore (L-32413.6) does **not** prove SHARP by termwise positivity. This is consistent with the reciprocal-zeta/Mertens firewalls on PR #332 and the componentwise Bernstein failure `R-32403`.

Any successful proof must control the **correlated quadratic-prefix sum** in (L-32413.6), or equivalently the convexity of `V_T` in `L-32411`.

## 6. Proof boundary

Closed exactly:

- finite-support row adjoint after total-tail removal;
- uniform `(1-x)^2` factorization;
- positive quadratic-prefix second-difference representation;
- equivalence in content with normalized-tail convexity.

Open:

- the required correlated bound on the second differences;
- SHARP;
- RH.
