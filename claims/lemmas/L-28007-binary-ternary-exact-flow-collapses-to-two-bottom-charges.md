# L-28007 — The exact binary–ternary flow collapses the RH source to two bottom charges

Claim ID: `L-28007`  
Title: In the explicit binary–ternary saturation, every parent at least four is invisible to the dyadic Möbius source, and the complete Riesz coordinate is exactly `-2 A_X(2)-A_X(3)`  
Status: **PROPOSED EXACT CROSS-ROUTE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #280  
Dependencies: PR #247 `L-23811`; `L-28005`  
Scope: exact finite source pairing; no bottom-charge estimate

## 1. Exact binary–ternary flow

Let `A_X(n)` be the descending producer coefficients of PR #247 `L-23811`.
At every parent `n`, the flow sends half of `A_X(n)` through

\[
 n=\lfloor n/2\rfloor+\lceil n/2\rceil
\]

and half through

\[
 n=\lceil n/3\rceil+\lfloor2n/3\rfloor.
\]

Its carry load is exactly the critical target

\[
 w_X(q)=q^{-1/2}\log(X/q),
 \qquad2\le q\le X.
\tag{L-28007.1}

## 2. Two-contact source test

Let

\[
 b_2=(\varepsilon-\delta_2)*\mu.
\]

For every split,

\[
 \sum_{q=2}^{n}b_2(q)\chi_{n,q}(j)
 =-\mathbf1_{j=1}-\mathbf1_{j=n-1}.
\tag{L-28007.2}

For every parent `n>=4`, both binary and ternary children lie in

\[
 2\le j\le n-2.
\]

Hence both retained split rows are exactly invisible to `b_2`.

At `n=2`, the two rules coincide at `1+1`; after combining their half weights,
the source value is `-2A_X(2)`.

At `n=3`, the two rules coincide at `1+2`; after combining their half weights,
the source value is `-A_X(3)`.

Therefore pairing the exact column saturation with `b_2` gives

\[
 \boxed{
 \mathcal R_2(X)
 :=\sum_{q=2}^{X}{b_2(q)\over\sqrt q}\log{X\over q}
 =-2A_X(2)-A_X(3).
 }
\tag{L-28007.3}

No coefficient with `n>=4` appears.

## 3. Divergence interpretation

Let `r_X(m)` be the unique Möbius node divergence of `L-23810`.  Since

\[
 \sum_{q\le m}b_2(q)\left\lfloor{m\over q}\right\rfloor
 =\mathbf1_{m=1},
\]

one also has directly

\[
 \boxed{
 \mathcal R_2(X)=r_X(1).
 }
\tag{L-28007.4}

Mass conservation for the binary–ternary fragmentation gives

\[
 r_X(1)=-2A_X(2)-A_X(3),
\]

which independently checks (L-28007.3).

Thus the complete reciprocal-zeta obstruction is the terminal bottom flux of
the exact balanced fragmentation tree.

## 4. Strong scope reduction

PR #247 proposed the sufficient weighted-variation theorem

\[
 \sum_{n\le X}|A_X(n)|\sqrt n=X^{o(1)}.
\]

Equation (L-28007.3) shows that this is far stronger than necessary.  The exact
minimal theorem is

\[
 \boxed{
 2A_X(2)+A_X(3)=O_\varepsilon(X^\varepsilon)
 \qquad\text{for every }\varepsilon>0.
 }
\tag{L-28007.5}

No estimate for the total variation of the growing producer is required.

## 5. RH consumer

For `Re(z)>1/2`,

\[
 \int_1^\infty\mathcal R_2(X)X^{-z-1}dX
 ={(1-2^{-z-1/2})/\zeta(z+1/2)-1\over z^2}.
\tag{L-28007.6}

The finite factor cannot cancel a zero with `Re(z)>0`.  Hence

\[
 \boxed{
 2A_X(2)+A_X(3)=O_\varepsilon(X^\varepsilon)
 \text{ for every }\varepsilon>0
 \quad\Longrightarrow\quad
 \mathrm{RH}.
 }
\tag{L-28007.7}

## 6. Production interpretation

The exact recurrence has converted the full balanced flow into one boundary
problem:

```text
all parents n>=4        source invisible;
parent 3                one bottom charge;
parent 2                double bottom charge;
RH source               terminal flux 2 A(2)+A(3).
```

A valid proof may use the factor-five transition reserve, reflected two-contact
Selberg block, dyadic chain descent, or a direct bottom-flux martingale.  It need
not bound the interior flow coefficientwise.

The theorem remains RH-bearing: the bottom flux equals the full `b_2` Riesz
coordinate exactly.

## 7. Proof boundary

Closed exactly:

- invisibility of every parent at least four;
- the two bottom multiplicities;
- the identity with the `b_2` Riesz coordinate;
- the divergence interpretation;
- the reduced sufficient criterion for RH.

Open:

- a subpower bottom-charge recurrence;
- physical/carry contraction producing that recurrence;
- RH.
