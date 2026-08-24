# L-106025 — The balanced owner-conductor Vaughan row is a squared mollifier defect over `L`

Claim ID: `L-106025`  
Programme aliases: `LFAM1.MOLLIFIED_RECIPROCAL_L_DEFECT`, `STRESS.BALANCED_L_RATIO`  
Status: **PROVED EXACT DIRICHLET-SERIES IDENTITY**  
Created: 2026-08-24  
Depends on: `L-106022`; PR #719 `L-102888`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Fix a deterministic owner pair

\[
P=pq
\]

and work on the owner-excluded monoid

\[
\mathbb N^{(P)}=\{n:(n,P)=1\}.
\]

Let `rho` be a distinct opposite owner prime and let `eta` be an even Dirichlet
character modulo `rho`, extended by zero at multiples of `rho`. All identities
below are initially taken for `Re(w)>1`, where the series converge absolutely,
and also hold as formal Dirichlet-series identities coefficientwise.

## 1. Owner-excluded `L`-function

Define

\[
Z_{P,\eta}(w)
=
\sum_{(n,P)=1}{\eta(n)\over n^w}.
\tag{L-106025.1}
\]

Then

\[
\boxed{
Z_{P,\eta}(w)
=L(w,\eta)
(1-\eta(p)p^{-w})(1-\eta(q)q^{-w}).
}
\tag{L-106025.2}
\]

Its reciprocal is the full owner-excluded Möbius source

\[
M_{P,\eta}(w)
=
\sum_{(n,P)=1}{\mu(n)\eta(n)\over n^w}
={1\over Z_{P,\eta}(w)}.
\tag{L-106025.3}
\]

The finite owner factors are zero-free for `Re(w)>0`.

## 2. Fixed-cutoff mollifier and defect

Let

\[
M_{U;P,\eta}(w)
=
\sum_{\substack{n\le U\\(n,P)=1}}
{\mu(n)\eta(n)\over n^w}.
\tag{L-106025.4}
\]

The owner-excluded Vaughan remainder coefficient is

\[
a_U^{(P)}\eta
=
\varepsilon-(\mu_U^{(P)}\eta)*(1^{(P)}\eta).
\]

Therefore its Dirichlet series is the literal mollification defect

\[
\boxed{
A_{U;P,\eta}(w)
=1-M_{U;P,\eta}(w)Z_{P,\eta}(w).
}
\tag{L-106025.5}
\]

## 3. Exact balanced ratio

The balanced row in the fixed-cutoff Vaughan identity is

\[
(a_U^{(P)}\eta)*(a_U^{(P)}\eta)*(\mu^{(P)}\eta).
\]

Consequently its Dirichlet series is

\[
\boxed{
B_{U;P,\eta}(w)
=A_{U;P,\eta}(w)^2M_{P,\eta}(w)
={\bigl(1-M_{U;P,\eta}(w)Z_{P,\eta}(w)\bigr)^2
  \over Z_{P,\eta}(w)}.
}
\tag{L-106025.6}
\]

Equivalently,

\[
\boxed{
B_{U;P,\eta}
=Z_{P,\eta}^{-1}
-2M_{U;P,\eta}
+M_{U;P,\eta}^2Z_{P,\eta}.
}
\tag{L-106025.7}
\]

Equation (L-106025.7) is exactly the generating-series form of

\[
\mu^{(P)}\eta
=2\mu_U^{(P)}\eta
-(\mu_U^{(P)}\eta)^2*(1^{(P)}\eta)
+(a_U^{(P)}\eta)^2*(\mu^{(P)}\eta).
\]

Thus the RH-bearing balanced packet is not an arbitrary character sum. It is a
squared mollifier error divided by an explicit owner-excluded Dirichlet
`L`-function.

## 4. Physical shell projection

Let `mathcal S` be any finite core shell selected by the compact observation and
the dyadic horizon. If `Pi_mathcal S` denotes coefficient projection to that
shell, then the observed balanced core polynomial is exactly

\[
\boxed{
B_{U;P,\eta}^{\mathcal S}(w)
=\Pi_{\mathcal S}
\left[
{(1-M_{U;P,\eta}Z_{P,\eta})^2\over Z_{P,\eta}}
\right](w).
}
\tag{L-106025.8}
\]

The projection is load-bearing: replacing it by an untruncated analytic ratio
without justifying tails would change the physical source.

## 5. Pole audit

For the principal character modulo `rho`,

\[
L(w,\eta_0)=\zeta(w)(1-\rho^{-w}),
\]

so `Z_(P,eta_0)` has a simple pole at `w=1`. The balanced ratio in
(L-106025.6) has at most a simple pole there:

\[
B_{U;P,\eta_0}(w)
=M_{U;P,\eta_0}(w)^2Z_{P,\eta_0}(w)+O(1).
\tag{L-106025.9}
\]

The zero-moment derivative kernel cancels this pole in the physical Mellin
observation, as recorded precisely in `L-106026`. No principal carrier is
silently discarded.

## Scope

This theorem proves the exact rational normal form of the owner-conductor
balanced source. It does not prove any mean value of (L-106025.6), justify
removing the shell projection, prove `SOCM106020`, or prove RH.
