# L-91321 — Minimality of the completed dyadic cascade descends zero-free half-planes

Claim ID: `L-91321`  
Status: **EXACT MEROMORPHIC CASCADE REDUCTION; ARITHMETIC MINIMALITY REMAINS OPEN**  
Created: 2026-08-12  
Depends on: main `L-91027`; standard scalar realization/minimality algebra  
RH status: **unproved**

## 1. Shifted completed quotient

Put

\[
 X(w)=\xi\!\left(\frac12+w\right)
 \tag{L-91321.1}
\]

and, for `a>0`,

\[
 \boxed{
 \Phi_a(w)=\frac{X(w)}{X(w+2a)}.
 }
 \tag{L-91321.2}
\]

This is the horizontal quotient in the coordinate whose moving critical
boundary is `Re(w)=-a`.

The exact completed cocycle is

\[
 \boxed{
 \Phi_{a+b}(w)
 =\Phi_a(w)\Phi_b(w+2a).
 }
 \tag{L-91321.3}
\]

In particular,

\[
 \boxed{
 \Phi_{2a}(w)
 =\Phi_a(w)\Phi_a(w+2a).
 }
 \tag{L-91321.4}
\]

The intermediate factor `X(w+2a)` cancels algebraically.

## 2. Annular zeros are exactly internal cancellations

Let

\[
 \rho=\frac12+d+i\gamma
 \qquad(0<d<1/2)
 \tag{L-91321.5}
\]

be a zero, and let `lambda=d+i gamma` be the corresponding zero of `X`.

A pole of `Phi_a` occurs at

\[
 w_0=\lambda-2a.
 \tag{L-91321.6}
\]

It lies in the target half-plane `Re(w)>-a` exactly when `d>a`. In the cascade
(L-91321.4), the shifted second factor has a numerator zero at the same point:

\[
 \Phi_a(w+2a)
 =\frac{X(w+2a)}{X(w+4a)}.
 \tag{L-91321.7}
\]

Thus the pole at `w_0` is canceled internally.

If `Phi_(2a)` is analytic in `Re(w)>-2a`, then no zero has `d>2a`.
Consequently the possible fine-scale poles are exactly the annular zeros

\[
 \boxed{
 a<d\le2a,
 }
 \tag{L-91321.8}
\]

and every one of them is hidden by the intermediate pole--zero cancellation in
(L-91321.4).

## 3. Abstract cascade minimality lemma

Consider scalar meromorphic transfer functions `F,G` on a domain `Omega`,
with a state-space cascade realization of `H=FG`. A pole `p` of `F` canceled by
a zero of `G` produces a nonzero internal state which is either uncontrollable
from the cascade input or unobservable at the cascade output. Therefore a
minimal cascade realization has no pole--zero cancellation in `Omega`.

For rational transfers this is the standard coprime/minimal-realization
criterion. For locally finite meromorphic products the statement follows on
every finite pole packet and then by exhaustion: the canceled mode is the
Cauchy/Jordan chain at `p`; its residue is annihilated by the composite transfer,
so the controllability or observability Gram has a null vector.

Hence:

\[
 \boxed{
 \begin{array}{c}
 H=FG\text{ analytic in }\Omega,\\
 \text{the declared cascade is minimal in }\Omega
 \end{array}
 \Longrightarrow
 F\text{ has no pole canceled by }G\text{ in }\Omega.
 }
 \tag{L-91321.9}
\]

## 4. Dyadic descent theorem

Assume:

1. `Phi_(2a)` is analytic/inner in `Re(w)>-2a`;
2. the source-ordered completed realization of
   \[
   \Phi_{2a}(w)=\Phi_a(w)\Phi_a(w+2a)
   \]
   is minimal on the intermediate state space.

Then (L-91321.8)--(L-91321.9) exclude every zero with `a<d<=2a`. The first
assumption already excludes `d>2a`. Therefore no zero has `d>a`, so

\[
 \boxed{
 \Phi_a\text{ is analytic/inner in }\Re(w)>-a.
 }
 \tag{L-91321.10}
\]

Thus innerness descends from scale `2a` to scale `a`.

## 5. Start of the descent

All nontrivial zeros satisfy `0<Re(rho)<1`, hence `0<d<1/2`. Therefore for
any `A>=1/2`, `Phi_A` has no denominator pole in its target half-plane.
Equivalently, the large-scale quotient is inner after the standard completed
normalization.

Fix `a>0` and choose `J` with `2^J a>=1/2`. If every cascade

\[
 \Phi_{2^{j+1}a}(w)
 =\Phi_{2^ja}(w)\Phi_{2^ja}(w+2^{j+1}a)
 \tag{L-91321.11}
\]

is minimal for `j=0,...,J-1`, repeated application of (L-91321.10) gives
innerness of `Phi_a`.

For every `a>0`, this proves RH.

## 6. Meaning of minimality in the three routes

### Canonical-system route

The integrated Marchenko/canonical system has no nonzero state orthogonal to
both boundary ports. An annular Xi zero would be exactly such a hidden
cancellation state.

### Lévy--Fock--Hardy route

The cascade of the two radial Fock intervals is controllable from the positive
prime-jump coherent core and observable in the causal/anti-causal Hardy plus
bridge outputs. No Poisson-chaos state may be traced out before this test.

### Theta/Brownian DtN route

The coupled `(S,Delta)` bulk has no zero-energy interior mode with both even
and odd boundary traces zero. The theta, Beta, Poisson, and `p=2` energies must
be summed before testing the nullspace.

These are three formulations of the same minimality theorem.

## 7. Exact remaining theorem

> **Completed Dyadic Cascade Minimality (`CDCM_a`).**  
> Construct the source-ordered completed realization of (L-91321.4) and prove
> that its controllability and observability Grams have trivial common kernel
> on every annular intermediate state.

`CDCM_a` is sufficient to descend from the unconditional large-scale regime to
all positive scales. It is the dynamic/cascade form of the analytic
intertwiner in `O-91302`.

## 8. Firewall

The scalar identity (L-91321.4) alone does not imply minimality; it explicitly
cancels every intermediate Xi factor. A generic cascade such as

\[
 b_p(w)^{-1}b_p(w)=1
\]

is inner at the coarse scale while carrying a hidden pole state. The complete
source and boundary channels are load-bearing.
