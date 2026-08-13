# T-91651 — Provenance-causal factor-54 resolution proposal

Claim ID: `T-91651`  
Status: **PROPOSED COMPLETE RH COMPOSITION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-13  
Depends on: `L-91650`, `L-91652`, `L-91653`, `L-91654`, `L-91655`, `L-91656`, `T-91650`; imported finite inputs locked in `t91651-dependency-lock.json`  
Mandatory firewalls: `R-91650`, `R-91651`, `R-91652`  
RH status: **proposed, not established**

## 1. Mathematical types

Use the free provenance-labelled cone of `L-91652`. Coefficient mass is measured
in that cone. A fixed linear map sends each label to the complete endpoint data
of `L-91653`: benchmark, target, declared and literal score, component rows,
ordinary and radix-four capacities, finite boundary reserves, and tail-prime
index.

The deficit of a certificate is the physical endpoint deficit after this map.
Thus the coefficient ledger and the physical equality are distinct but linked
by one immutable linear realization.

## 2. Generator types

A base generator at quotient `u` carries the exact nonnegative component row
`Q_u`, target `4sqrt(u)-3`, declared score `5sqrt(u)-3`, its literal row score,
and its exact ordinary/radix-four responses.

For an active prime `p`, with `r=p^(-1/2)`, the causal generator is the complete
two-endpoint difference

\[
P_u-rU_pP_{u/p}.
\]

`L-91654` proves that this difference has nonnegative target, component rows,
ordinary capacities and radix-four capacities, together with a strictly
favorable declared score surplus. `L-91656` gives one absolute bound for the
remaining declared-versus-literal score discrepancy.

Finite Hall edges, mismatch, B-spline collar, terminal omission and finite
endpoint corrections are nonrecursive current-generation data.

## 3. Exact reset identity

For the ordered active primes, use

\[
r_i=p_i^{-1/2},
\quad s_i=\prod_{h\le i}(1-r_h),
\quad \lambda_i=r_i s_{i-1},
\quad \alpha_i=r_i\lambda_i.
\]

Then

\[
s_k+\sum_i\lambda_i=1,
\qquad
\sum_i\alpha_i<1/8.
\]

The free-certificate production rule is

\[
\widehat A
\longmapsto
s_k\widehat A+
\sum_i\lambda_i\widehat C_i+
\sum_i\alpha_i\widehat A_i^{child}.
\tag{T-91651.1}
\]

After realization, (T-91651.1) equals the original physical datum exactly.
Current certificate mass is one; total recursive child mass is below one eighth.
Every child endpoint is at most `X/67`, and its tail-prime index advances.
A causal generator remains current and creates no child. Hence the certificate
cone is closed under the reset.

## 4. Local debt

The native base row is feasible against its exact response capacities. Its
positive deficit is confined to the fixed quotient interval below `67`.

For a causal generator, the literal score discrepancy is nonpositive when the
child quotient is at least `67` and uniformly bounded otherwise. The finite Hall,
collar, terminal and endpoint corrections have one absolute score charge by the
locked finite theorems.

Consequently there is an absolute `C` such that the complete current output from
a mass-one certificate has positive deficit at most `C`.

## 5. Root entry and one-use correction ledger

The fixed-window score-Hall theorem produces nonnegative residual coefficients
`nu(e)<=1` on fewer than `55` nodes. Their recursive certificate mass is at most
`54`. Hall edge corrections have nonnegative score and remain current.

The finite mismatch, collar, terminal omission and endpoint corrections are
applied once after current terms are summed. `L-91655` records

\[
\Delta_X(P_X^{nat})
\le C_{root}+\Delta_X(P_{root}^{rec}),
\]

and the exact endpoint theorem gives

\[
F_\Lambda(X)\le\Delta_X(P_X^{nat}).
\tag{T-91651.2}
\]

No finite small-prime block is reintroduced on a tail child.

## 6. Envelope contraction

Let `Lambda(X)` be the worst positive deficit among mass-one provenance
certificates at endpoints at most `X`, with every tail-prime index included.
Homogeneity and subadditivity of the realized deficit, together with the reset,
give

\[
\boxed{
\Lambda(X)
\le C+\frac18\Lambda(X/67).
}
\tag{T-91651.3}
\]

Therefore

\[
\boxed{
\Lambda(X)\le\frac{8C}{7}=O(1).
}
\tag{T-91651.4}
\]

The root mass bound and (T-91651.2) yield

\[
F_\Lambda(X)=O(1)=o(\log^2X).
\]

The resident endpoint-score criterion then implies RH.

## 7. Exact status boundary

This is a complete proposal, not an accepted proof. A hostile review must
reconstruct at the locked blobs:

1. the root score-Hall and row representation;
2. global endpoint monotonicity of the component and response families;
3. the directed finite base in `X-91650`;
4. the finite mismatch, collar, terminal and endpoint correction constants;
5. the root comparison (T-91651.2) and its sign;
6. the certificate-realization definitions and deficit cone;
7. the claim that all current correction data are charged once.

```text
causal coefficient identity                  PROVED
recursive coefficient mass <1/8             PROVED
certificate/realization type distinction      PROVED
causal target/row/capacity positivity         PROVED
literal score base correction                 PROVED / REPLAY
root one-use ledger                           PROPOSED COMPLETE / REVIEW
packet-envelope contraction                   PROVED CONDITIONAL
full RH composition                           PROPOSED / NOT VERIFIED
Riemann Hypothesis                            UNPROVEN
```