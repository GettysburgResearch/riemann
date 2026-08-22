# L-105206 — The complete derivative-ladder boundary telescopes to one Levinson quotient

Claim ID: `L-105206`  
Status: **PROVED EXACT TELESCOPE; HIGH-ENDPOINT ASYMPTOTIC DEPENDS ON THE PROPOSED L-105200 SADDLE THEOREM**  
Created: 2026-08-23  
Depends on: PR #720 `L-104518--L-104521`; `L-105200--L-105201`  
RH status: **unproved**

## 1. Adjacent derivative companions

Fix `lambda>0` and put

\[
F_k(z)=\Xi^{(k)}(z),
\qquad
E_{k,\lambda}(z)=F_k(z)-i\lambda F_{k+1}(z).
\]

In the `s`-plane, with

\[
s={1\over2}+iz,
\]

define

\[
G_{k,\lambda}(s)
=\xi^{(k)}(s)+\lambda\xi^{(k+1)}(s).
\]

Then

\[
\boxed{
E_{k,\lambda}(z)=i^kG_{k,\lambda}(s),
\qquad
G_{k,\lambda}'=G_{k+1,\lambda}.
}
\tag{L-105206.1}
\]

Fix a regular ordinate `T`.  On a zero-free horizontal segment

\[
\gamma_{T,R}=\{\sigma+iT:1/2\le\sigma\le R\}
\]

continue all arguments from `R` toward `1/2` and put

\[
\Theta_{k,\lambda}(T;R)
=
\Delta_{\sigma:R\to1/2}
\arg {G_{k,\lambda}(\sigma+iT)
      \over G_{k+1,\lambda}(\sigma+iT)}.
\tag{L-105206.2}
\]

## 2. Exact horizontal telescope

For every finite `r`, multiplication of the adjacent quotients gives

\[
\prod_{k=0}^{r-1}
{G_{k,\lambda}\over G_{k+1,\lambda}}
={G_{0,\lambda}\over G_{r,\lambda}}.
\]

Because all branches are continued from one common endpoint, there is no
independent integer ambiguity at the intermediate levels.  Hence

\[
\boxed{
\sum_{k=0}^{r-1}\Theta_{k,\lambda}(T;R)
=
\Delta_{\sigma:R\to1/2}
\arg {G_{0,\lambda}(\sigma+iT)
      \over G_{r,\lambda}(\sigma+iT)}.
}
\tag{L-105206.3}
\]

For each fixed finite ladder, the far-right Stirling normalization of
`L-104519--L-104521` permits `R->infinity`.  Thus the sum of all limiting
vertical charges is

\[
\boxed{
\sum_{k=0}^{r-1}
\mathfrak V_{k,\lambda}^{\infty}(T)
=-{1\over\pi}
\Delta_{\sigma:\infty\to1/2}
\arg {G_{0,\lambda}(\sigma+iT)
      \over G_{r,\lambda}(\sigma+iT)}.
}
\tag{L-105206.4}
\]

The former `r` horizontal-argument gates are therefore one relative Levinson
argument, not `r` independent boundary problems.

## 3. Exact top-boundary and index telescope

On any common regular rectangle, the top charges of `L-104518` satisfy

\[
\boxed{
\sum_{k=0}^{r-1}\mathfrak T_k(T)
={1\over2\pi i}
\int_{-T}^{T}
\left(
{E_{0,\lambda}'\over E_{0,\lambda}}
-
{E_{r,\lambda}'\over E_{r,\lambda}}
\right)dt.
}
\tag{L-105206.5}
\]

The complete argument-principle ledger is consequently

\[
\boxed{
N_\Omega(E_{0,\lambda})-N_\Omega(E_{r,\lambda})
={1\over2\pi i}
\int_{\partial\Omega}
 d\log {E_{0,\lambda}\over E_{r,\lambda}}.
}
\tag{L-105206.6}
\]

Every intermediate companion cancels exactly.  This is the correct boundary
counterpart of the cancellation in the derivative zero counts.

## 4. Natural high endpoint

For a high terminal order `r`, choose the native mean-frequency parameter

\[
\lambda_r={M_r\over M_{r+1}}
={1\over\mu_r}
={1\over w_r}(1+o(1)).
\tag{L-105206.7}
\]

The `C^1` form of the proposed Gaussian saddle theorem `L-105200` gives, on
every fixed lower strip inside the natural box,

\[
E_{r,\lambda_r}(z)
=C_r
\exp\!\left(iw_rz-{s_r^2z^2\over2}\right)(1+o(1))
\tag{L-105206.8}
\]

with a nonzero scalar `C_r`.  Since `E_(r+1)=E_r'`,

\[
\boxed{
{G_{r,\lambda_r}(s)\over G_{r+1,\lambda_r}(s)}
={1\over w_r+i s_r^2z}(1+o(1)).
}
\tag{L-105206.9}
\]

Its argument variation on each fixed bounded part of the safe horizontal path
is `o(1)`.  This does **not** by itself control the complete far-right-to-line
argument uniformly in a growing derivative order; that passage remains part
of the review obligation.

## 5. Meaning for the low-order problem

After the high endpoint is made zero-free, the boundary problem is not a sum
of thousands of derivative-level winding estimates.  It is one continued
relative argument

\[
{\xi+\lambda_r\xi'
 \over
 \xi^{(r)}+\lambda_r\xi^{(r+1)}}.
\]

The denominator is asymptotically explicit in the high tail.  The numerator
is the classical low-order Levinson auxiliary function.  Proving that this one
relative quotient carries no inward unit is still an RH-strength theorem; the
exact telescope exposes rather than solves it.
