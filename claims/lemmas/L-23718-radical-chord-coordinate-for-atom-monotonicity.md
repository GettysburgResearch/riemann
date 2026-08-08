# L-23718 — Radical-chord coordinate for endpoint monotonicity

Claim ID: `L-23718`  
Title: The total endpoint-atom tail is one explicit radical-prefix chord, and its nonnegativity would make the prime-ramp deficit monotone  
Status: **PROPOSED EXACT LEMMA; RADICAL-CHORD SIGN OPEN**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Dependencies: `L-23717`; PR #248 ordinary-prime reduction; elementary finite summation  
Scope: exact scalar coordinate; no sign theorem and no RH conclusion

## 1. Ordinary-prime objective

Let

\[
R(m)=\log\operatorname{rad}(m)
=\sum_{p\mid m}\log p,
\qquad R(1)=0.
\tag{L-23718.1}
\]

For any finite carry coordinate `b`, ordinary-prime divisor switching gives

\[
\boxed{
J_X^{\mathbb P}(b)
:=
\sum_{p\le X}(\log p)v_p(b)
=
\sum_{m=2}^{X}b(m)[R(m)-R(m-1)].
}
\tag{L-23718.2}
\]

For the parabolic seed `b_X`, define

\[
P_X=
\sum_{p\le X}\frac{\log p}{\sqrt p}\log\frac Xp,
\tag{L-23718.3}
\]

and the ordinary-prime deficit

\[
\boxed{D_X=J_X^{\mathbb P}(b_X)-P_X.}
\tag{L-23718.4}
\]

The total endpoint atom of `L-23717` is exactly

\[
\boxed{
\mathcal A_{N+1}(2)=D_{N+1}-D_N.
}
\tag{L-23718.5}
\]

## 2. Three finite prefixes

For an integer `N>=2`, put

\[
A_N=
\sum_{m=2}^{N}
\sqrt m\,[R(m)-R(m-1)],
\tag{L-23718.6}
\]

\[
C_N=
\sum_{m=2}^{N}
m\,[R(m)-R(m-1)],
\tag{L-23718.7}
\]

and

\[
U_N=\sum_{p\le N}\frac{\log p}{\sqrt p}.
\tag{L-23718.8}
\]

Let

\[
\ell_N=\log\left(1+\frac1N\right),
\qquad
\kappa_N=
\frac{4\left(N^{-1/2}-(N+1)^{-1/2}\right)}{\ell_N}>0.
\tag{L-23718.9}
\]

Define the radical-chord margin

\[
\boxed{
\mathfrak R_N
=
\kappa_NC_N-2A_N+U_N.
}
\tag{L-23718.10}
\]

Every term is a finite elementary expression involving only prime divisors through `N`, logarithms, and square roots.

## 3. Exact difference identity

For `m<=N`, direct subtraction of the two parabolic seeds gives

\[
b_{N+1}(m)-b_N(m)
=
2\ell_N\sqrt m
+4m\left((N+1)^{-1/2}-N^{-1/2}\right).
\tag{L-23718.11}
\]

The entering coefficient at `m=N+1` is zero.  Substitute (L-23718.11) into (L-23718.2):

\[
J_{N+1}^{\mathbb P}(b_{N+1})
-J_N^{\mathbb P}(b_N)
=
2\ell_NA_N
+4\left((N+1)^{-1/2}-N^{-1/2}\right)C_N.
\tag{L-23718.12}
\]

The new prime, when `N+1` is prime, enters the ramp with weight `log 1=0`. Hence

\[
P_{N+1}-P_N=\ell_NU_N.
\tag{L-23718.13}
\]

Combining the two identities gives

\[
\boxed{
D_{N+1}-D_N
=-\ell_N\mathfrak R_N.
}
\tag{L-23718.14}
\]

Thus

\[
\boxed{
\mathfrak R_N\ge0
\iff
D_{N+1}\le D_N
\iff
\mathcal A_{N+1}(2)\le0.
}
\tag{L-23718.15}
\]

This is the scalar front door of AWTO.

## 4. Summation-by-parts form

The radical prefixes also satisfy

\[
A_N
=
\sqrt N R(N)
-
\sum_{m=1}^{N-1}
(\sqrt{m+1}-\sqrt m)R(m),
\tag{L-23718.16}
\]

\[
C_N
=
N R(N)-\sum_{m=1}^{N-1}R(m).
\tag{L-23718.17}
\]

Therefore the apparently large boundary oscillation `R(N)` is multiplied in `mathfrak R_N` by

\[
\kappa_NN-2\sqrt N,
\]

which tends to zero.  The sign problem is a genuinely smoothed radical chord, not a pointwise estimate for `rad(N)`.

Equivalently,

\[
\mathfrak R_N
=
\sum_{p\le N}(\log p)\,\mathfrak r_N(p),
\tag{L-23718.18}
\]

where the explicit one-prime kernel is obtained by inserting

\[
R(m)-R(m-1)
=
\sum_p(\log p)
[\mathbf1_{p\mid m}-\mathbf1_{p\mid m-1}].
\]

The individual prime kernels have both signs; a proof may not estimate them separately by absolute value.

## 5. Radical-Chord Theorem and RH

The proposed scalar theorem is

\[
\boxed{
\textbf{RCT:}\qquad
\mathfrak R_N\ge0
\quad(N\ge2).
}
\tag{L-23718.19}
\]

Under RCT, (L-23718.14) gives

\[
D_X\le D_2=0.
\tag{L-23718.20}
\]

Hence

\[
P_X\ge J_X^{\mathbb P}(b_X).
\tag{L-23718.21}
\]

The prime-only reduction on PR #248 gives

\[
J_X^{\mathbb P}(b_X)
\ge4\sqrt X-O(\log^2X).
\tag{L-23718.22}
\]

Thus RCT implies the critical prime-ramp lower bound and, through the source-pinned square-screw/Landau transfer,

\[
\boxed{\mathrm{RH}.}
\tag{L-23718.23}
\]

RCT is weaker than full AWTO because it controls only the cutoff `z=2`.  It is nevertheless a complete finite RH proposal.

## 6. Review boundary

Closed exactly:

1. the radical objective identity;
2. the consecutive-deficit formula;
3. the radical-chord coordinate and its equivalence to total atom monotonicity;
4. the conditional deduction `RCT -> prime ramp -> RH`.

Open:

1. `mathfrak R_N>=0` for all `N`;
2. AWTO at every tail cutoff;
3. RH.
