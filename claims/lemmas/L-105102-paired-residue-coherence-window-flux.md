# L-105102 — Paired residue-coherence window flux

Claim ID: L-105102

Status: **PROPOSED EXACT FIXED-WINDOW IDENTITY; review pending**

Created: 2026-08-23

Depends on: L-105101; residue theorem; PR #720 only as exact-head,
post-freeze prior-art context

RH status: **not assumed**

## 1. First-residue contour

Let \(F\), \(T\), and \(\eta\) satisfy the regular-rectangle hypotheses of
L-105101. Put

\[
P_F(z)=\frac{F(z)}{F'(z)}
\tag{L-105102.1}
\]

and

\[
\Phi_{1,F}(T,\eta)
=\frac1{2\pi i}\int_{\partial\Omega_{T,\eta}}P_F(z)\,dz.
\tag{L-105102.2}
\]

At a simple zero \(c\) of \(F'\),

\[
\operatorname{Res}_{z=c}P_F
=\frac{F(c)}{F''(c)}
=\rho_c.
\tag{L-105102.3}
\]

If \(F(c)=0\), then \(P_F\) is removable at \(c\) and the displayed residue
is zero. There are no other possible poles, so

\[
\boxed{
\Phi_{1,F}(T,\eta)
=
\sum_{\substack{F'(c)=0\\c\in\Omega_{T,\eta}}}\rho_c.
}
\tag{L-105102.4}
\]

## 2. Exact first-moment split

Define

\[
\mathcal M_{1,F}(T)
=
-\sum_{\substack{-T<c<T\\c\in\mathbb R,\ F'(c)=0}}\rho_c
\tag{L-105102.5}
\]

and the nonreal first-residue correction

\[
C_{1,F}(T,\eta)
=
\sum_{\substack{F'(c)=0,\ c\in\Omega_{T,\eta}\\c\notin\mathbb R}}\rho_c.
\tag{L-105102.6}
\]

Conjugate pairing makes \(C_{1,F}\) real. Splitting (L-105102.4) gives

\[
\boxed{
\mathcal M_{1,F}(T)
=-\Phi_{1,F}(T,\eta)+C_{1,F}(T,\eta).
}
\tag{L-105102.7}
\]

The correction is load bearing: a complete contour sees nonreal critical
points even though the real critical-point moment does not.

## 3. Four-edge and parity reduction

The same counterclockwise parameterization as L-105101 gives

\[
\boxed{
\begin{aligned}
\Phi_{1,F}(T,\eta)
={}&-\frac1\pi\int_{-T}^{T}
\Im P_F(x+i\eta)\,dx\\
&+\frac1{2\pi}\int_{-\eta}^{\eta}
\left[P_F(T+iy)-P_F(-T+iy)\right]\,dy.
\end{aligned}
}
\tag{L-105102.8}
\]

If \(F\) has definite parity, then \(P_F(-z)=-P_F(z)\). Hence

\[
\boxed{
\Phi_{1,F}(T,\eta)
=\frac2\pi\left[
\int_0^\eta\Re P_F(T+iy)\,dy
-\int_0^T\Im P_F(x+i\eta)\,dx
\right].
}
\tag{L-105102.9}
\]

Every edge and orientation sign is retained. \(\Phi_{1,F}\) is a contour
charge, not an argument-principle zero count.

## 4. Exact paired coherence identity

Write \(\mathcal M_{2,F}:=M_{2,F}\) in the second-moment notation of
L-105101:

\[
\mathcal M_{2,F}(T)
=B_F(T,\eta)-C_{2,F}(T,\eta)-D_{2,F}(T,\eta),
\tag{L-105102.10}
\]

where \(C_{2,F}\) is the algebraic squared-residue correction and \(D_{2,F}\)
is the adjacent-derivative debt. Let \(R_F(T)\) be the number of simple real
zeros of \(F'\) in \((-T,T)\).

When \(R_F(T)\mathcal M_{2,F}(T)>0\), the residue coherence is exactly

\[
\boxed{
\mathfrak C_F(T)
=
\frac{\bigl(-\Phi_{1,F}(T,\eta)+C_{1,F}(T,\eta)\bigr)_+^2}
{R_F(T)\bigl(B_F(T,\eta)-C_{2,F}(T,\eta)-D_{2,F}(T,\eta)\bigr)}.
}
\tag{L-105102.11}
\]

Thus, for any \(\delta>0\), the strict transfer-safe fixed-window coherence
input is equivalent to

\[
\boxed{
\bigl(-\Phi_{1,F}+C_{1,F}\bigr)_+^2
>
\left(\frac12+\delta\right)
R_F\bigl(B_F-C_{2,F}-D_{2,F}\bigr).
}
\tag{L-105102.12}
\]

This is an exact reformulation, not an estimate.

The symbol \(\Phi_{1,F}\) deliberately differs from the corrected carrier
called \(A\) in draft PR #720 L-104522. That carrier is
\(\mathcal M_{1,F}=-\Phi_{1,F}+C_{1,F}\).

For each fixed regular \(T\), the thin-strip choice supplied by L-105101 may
be made with no nonreal \(F'\)-zero in the rectangle. Then
\(C_{1,F}=C_{2,F}=0\) simultaneously. This is a pointwise simplification, not
control of the boundary charges along an asymptotic sequence
\(\eta=\eta(T)\).

## 5. Xi derivative specialization

For an integer \(k\ge1\), take \(F=\Xi^{(k-1)}\). Then

\[
P_k(z)=\frac{\Xi^{(k-1)}(z)}{\Xi^{(k)}(z)}
\tag{L-105102.13}
\]

and

\[
C_{1,k}(T,\eta)
=
\sum_{\substack{\Xi^{(k)}(c)=0,\ c\in\Omega_{T,\eta}\\
c\notin\mathbb R}}
\frac{\Xi^{(k-1)}(c)}{\Xi^{(k+1)}(c)}.
\tag{L-105102.14}
\]

Conditional on the rectangle hypotheses,

\[
\mathcal M_{1,k}(T)=-\Phi_{1,k}(T,\eta)+C_{1,k}(T,\eta),
\tag{L-105102.15}
\]

On the simple, common-zero-free stratum, and with
\(F(-T)F(T)\ne0\), (L-105102.11) is precisely the fixed-window coherence
statistic in draft PR #720 L-104522--L-104523.

The literal squared inequality in draft T-104530's RCMV104530 statement
coincides with this positive-part gate only after
\(\mathcal M_{1,k}(T)>0\) is established. A large negative first moment may
have a large square but cannot activate the reverse--Rolle transfer.

The contour identities permit a common zero at which \(\Xi^{(k)}\) is simple,
contributing residue zero; \(\Xi^{(k-1)}\) then has multiplicity two. Direct
use in L-104522 additionally requires its common-zero exclusion, or a separate
multiplicity branch. The relevant Xi-derivative simplicity and common-zero
hypotheses are not asserted here.

## 6. Relation to the global first ledger

For a real polynomial \(p\) satisfying draft PR #720 L-104524, an outer
rectangle containing every zero of \(p'\) gives

\[
\Phi_{1,p}(\mathrm{outer})=-\frac{V_2(p)}{n^2}.
\tag{L-105102.16}
\]

For an inner regular rectangle,

\[
-\frac{V_2(p)}{n^2}-\Phi_{1,p}(T,\eta)
=
\sum_{\substack{p'(c)=0\\c\notin\Omega_{T,\eta}}}\rho_c.
\tag{L-105102.17}
\]

The direct entire-function formula bypasses polynomial exhaustion at fixed
\((T,\eta)\), but it replaces the explicit root variance by the unevaluated
boundary charge \(\Phi_{1,F}\). It does not close the canonical-product
route.

Draft PR #720 L-104523.2 already contains the individual local-circle
first-residue formula, and L-104524 contains the global polynomial variance
ledger. The new content here is the complete finite-window first-moment
closure, its oriented edge reduction, and its exact pairing with L-105101
into the coherence quotient.

No novelty is claimed for the residue theorem or for four-edge contour
decomposition in general.

## 7. Scope

This theorem does not:

- handle multiple derivative zeros without confluent residues;
- establish Xi-derivative simplicity or the downstream common-zero exclusion;
- establish the endpoint nonvanishing required by L-104522;
- estimate \(\Phi_{1,F},B_F,C_{1,F},C_{2,F}\), or \(D_{2,F}\);
- choose or control an admissible asymptotic height/strip sequence;
- prove the strict inequality (L-105102.12), RCMV104530, or RH.
