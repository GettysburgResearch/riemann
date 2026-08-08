# L-32408 — The Q=4 physical current is a base-4 generalized-factorial defect

Claim ID: `L-32408`  
Title: After complete divisor recombination, every integer `Q=4` physical carry row is the logarithmic superadditivity defect of one explicit recursively defined integer sequence  
Status: **PROPOSED COMPLETE EXACT FINITE/ARITHMETIC LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32404`, `L-32407`; Legendre's floor identity in base four  
Scope: integer parent/split rows; this lemma deliberately does not promote integer-row signs to the continuous pole field

## 1. Divisor-prefix state

Retain

\[
 c_4=e_4*\Lambda_4,
 \qquad
 e_4(1)=1,
 \qquad
 e_4(4^r)=-3\ (r\ge1).
\]

Define

\[
 \boxed{
 A_4(N)=\sum_{q\le N}c_4(q)\left\lfloor\frac Nq\right\rfloor,
 \qquad A_4(0)=0.
 }
 \tag{L-32408.1}
\]

Then every integer physical carry row is exactly

\[
 \boxed{
 Q_4(n,j)=A_4(n)-A_4(j)-A_4(n-j).
 }
 \tag{L-32408.2}
\]

## 2. Base-4 digit-sum representation

Let `s_4(t)` denote the sum of the base-four digits of the nonnegative integer `t`. Legendre's elementary identity is

\[
 \boxed{
 t-3\sum_{r\ge1}\left\lfloor\frac{t}{4^r}\right\rfloor
 =s_4(t).
 }
 \tag{L-32408.3}
\]

Since `c_4=e_4*Lambda_4`, finite convolution and (L-32408.3) give

\[
\begin{aligned}
 A_4(N)
 &=\sum_{m\le N}\Lambda_4(m)
 \left[
  \left\lfloor\frac Nm\right\rfloor
  -3\sum_{r\ge1}
   \left\lfloor\frac{N}{4^rm}\right\rfloor
 \right]\\
 &=\boxed{
 \sum_{m\le N}\Lambda_4(m)
 s_4\!\left(\left\lfloor\frac Nm\right\rfloor\right)}.
\end{aligned}
 \tag{L-32408.4}
\]

This is an exact digit-carry expression for the complete source-convolved physical current.

## 3. Prime-free factorial formula

Split `Lambda_4` into the ordinary von Mangoldt sequence and its local `4`-adic correction.

For the ordinary part, (L-32408.3) and

\[
 \sum_{m\le N}\Lambda(m)\left\lfloor\frac Nm\right\rfloor
 =\log(N!)
\]

give

\[
 \sum_m\Lambda(m)s_4(\lfloor N/m\rfloor)
 =\log(N!)-3\sum_{r\ge1}
  \log\!\left(\left\lfloor\frac N{4^r}\right\rfloor!\right).
 \tag{L-32408.5}
\]

For the local correction, write

\[
 m_t=\left\lfloor\frac N{4^t}\right\rfloor.
\]

Using (L-32404.8), its contribution is

\[
 (\log4)\sum_{h\ge1}(4^h-1)s_4(m_h).
\]

Substitute (L-32408.3). The coefficient of `m_t` is

\[
 (4^t-1)-3\sum_{h=1}^{t-1}(4^h-1).
\]

But

\[
 3\sum_{h=1}^{t-1}(4^h-1)
 =4^t-3t-1,
\]

so the coefficient is exactly `3t`. Therefore

\[
 \boxed{
 A_4(N)
 =\log(N!)
 -3\sum_{r\ge1}\log(m_r!)
 +3\log4\sum_{r\ge1}r m_r.
 }
 \tag{L-32408.6}
\]

Every prime sum has disappeared.

## 4. Generalized factorial

Define

\[
 \boxed{
 \mathfrak F_4(N)
 =N!\prod_{r\ge1}
  \frac{4^{3r\lfloor N/4^r\rfloor}}
       {(\lfloor N/4^r\rfloor!)^3},
 \qquad
 \mathfrak F_4(0)=1.
 }
 \tag{L-32408.7}
\]

The product is finite. Equation (L-32408.6) becomes

\[
 \boxed{A_4(N)=\log\mathfrak F_4(N).}
 \tag{L-32408.8}
\]

Consequently

\[
 \boxed{
 Q_4(n,j)
 =\log\frac{\mathfrak F_4(n)}
  {\mathfrak F_4(j)\mathfrak F_4(n-j)}.
 }
 \tag{L-32408.9}
\]

Thus every integer physical row is one generalized-factorial superadditivity defect.

## 5. Exact radix-four recursion

Put

\[
 M=\left\lfloor\frac N4\right\rfloor.
\]

Using

\[
 \sum_{r\ge1}\left\lfloor\frac M{4^r}\right\rfloor
 =\frac{M-s_4(M)}3,
\]

separating the first layer of (L-32408.7) gives

\[
 \boxed{
 \mathfrak F_4(N)
 =\mathfrak F_4(M)
  \frac{N!}{(M!)^4}
  4^{\,4M-s_4(M)}.
 }
 \tag{L-32408.10}
\]

This is an exact one-step renormalization, not an asymptotic recurrence.

The right side is an integer. Indeed, if

\[
 N=4M+r,
 \qquad0\le r\le3,
\]

then

\[
 \frac{N!}{(M!)^4}
 =r!\binom{N}{M,M,M,M,r},
\]

where the multinomial notation means four blocks of size `M` and one residual block of size `r`. Hence induction from `F_4(0)=1` shows

\[
 \boxed{\mathfrak F_4(N)\in\mathbb Z_{>0}.}
 \tag{L-32408.11}
\]

The `Q=4` physical carry problem at integer rows therefore has a fully discrete radix-four state.

## 6. Why this does not by itself prove RH

It is tempting to combine (L-32408.9) with a supermultiplicativity claim for `mathfrak F_4` and invoke a one-sign theorem. That shortcut is not valid without an additional analytic bridge.

The continuous pole-preserving atomized current has transform

\[
 E_4(s)L_4(s)N_\theta(s),
\]

which retains every nontrivial zeta-zero pole by `L-32404`.

Passing to the integer floor row (L-32408.1) performs an additional divisor-prefix summation. On Dirichlet series this introduces a factor `zeta(s)`:

\[
 \sum_N[A_4(N)-A_4(N-1)]N^{-s}
 =\zeta(s)E_4(s)L_4(s)
 =-E_4(s)\zeta'(s)+\zeta(s)E_4'(s).
 \tag{L-32408.12}
\]

The zeta-zero poles have disappeared from (L-32408.12). Therefore an elementary sign or supermultiplicativity theorem for the integer generalized factorial, even if established, is not alone an RH proof. The between-row/independent-frequency physical block must remain in the argument.

This firewall explains why strong integer-row behavior is compatible with the unresolved continuous RH problem.

## 7. Strategic use

Equation (L-32408.10) supplies a concrete radix-four state for the finite arithmetic part of the reflected recurrence:

```text
integer physical row
 -> one generalized factorial F_4
 -> exact radix-four renormalization
 -> finite residue r in {0,1,2,3}
 -> lower parent floor(N/4).
```

Unlike an odd-prime radix, no nonprincipal Dirichlet-character sector is introduced. The only missing bridge is the continuous/independent-frequency collar which restores the pole-sensitive information removed by the divisor-prefix operation.

## 8. Proof boundary

Closed exactly here:

1. base-four digit-sum representation;
2. prime-free factorial formula;
3. generalized-factorial realization;
4. exact radix-four recursion;
5. integer-valuedness;
6. the pole-cancellation scope firewall for integer rows.

Open:

1. the continuous collar between integer rows;
2. the source-convolved reflected block in that collar;
3. the neutral scattering recurrence;
4. RH.
