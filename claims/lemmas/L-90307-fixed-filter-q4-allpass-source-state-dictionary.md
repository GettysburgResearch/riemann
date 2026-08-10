# L-90307 — Fixed-filter Q4 all-pass source/state dictionary

Claim ID: `L-90307`  
Title: Freezing the dyadic Euler filters and deforming only the odd Euler core places the compact Q4 source, its zero-bare input, and the all-pass reservoir in one parameter-independent physical block metric  
Status: **PROPOSED COMPLETE EXACT SOURCE/STATE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: PR #339 `L-33804`; PR #345 `L-34405`; `L-90306`  
Scope: exact source/state typing and block-metric compatibility; no global recurrence or RH conclusion

## 1. Freeze the dyadic variable

Put

\[
z=2^{-s},\qquad x=4^{-s}=z^2,
\]

and write

\[
B_0(s)=\frac1{\zeta(s)}=(1-z)\mathcal O(s),
\qquad
\mathcal O(s)=\prod_{p\ \mathrm{odd}}(1-p^{-s}).
\]

Use the positive odd-prime Jordan deformation of PR #345,

\[
J_{\mathrm{odd},\tau}(s)
=\frac{\mathcal O(s)}{\mathcal O(s-\tau)},
\]

and define one common carrier

\[
\boxed{g_\tau=B_0J_{\mathrm{odd},\tau}.}
\tag{L-90307.1}
\]

The dyadic factors below are independent of `tau`.

Define

\[
\boxed{h_\tau=(1-x)g_\tau,}
\tag{L-90307.2}
\]

and

\[
\boxed{c_\tau=(1-4x)g_\tau.}
\tag{L-90307.3}
\]

At `tau=0`, `c_0=(1-4^{1-s})/\zeta(s)=B_\sharp`, the compact Q4 source of PR #345.

## 2. Exact Q4 all-pass dictionary

For `Q=4`, the centered Euler--Blaschke transfer and its state transfer are

\[
E_4(s)=\frac{1-4x}{1-x},
\qquad
R_4(s)=\frac{\sqrt3/2}{1-x}.
\tag{L-90307.4}
\]

Therefore, for every `tau` for which the paths are defined,

\[
\boxed{E_4h_\tau=c_\tau,}
\tag{L-90307.5}
\]

and

\[
\boxed{R_4h_\tau=\frac{\sqrt3}{2}g_\tau.}
\tag{L-90307.6}
\]

These are identities of Dirichlet multipliers, not first-jet approximations.

Because `E_4` and `R_4` are independent of `tau`, every Jordan derivative satisfies the same state dictionary:

\[
E_4\,\partial_\tau^r h_\tau
=\partial_\tau^r c_\tau,
\qquad
R_4\,\partial_\tau^r h_\tau
=\frac{\sqrt3}{2}\partial_\tau^r g_\tau
\tag{L-90307.7}
\]

for every `r>=0` at `tau=0`.

Thus no derivative gauge is generated inside the colligation.

## 3. The input is exactly zero-bare in the balanced interior

Let `b_h` be the Dirichlet coefficient sequence of `h_0`. Since

\[
\mathbf 1*B_0=\varepsilon,
\]

one has

\[
\boxed{\mathbf1*b_h=\varepsilon-\delta_4.}
\tag{L-90307.8}
\]

Its prefix is zero for every argument at least four. Hence every carry row whose two children are at least four has

\[
\boxed{Y_h=0.}
\tag{L-90307.9}
\]

The same holds for the centered physical bare field on every sufficiently deep fixed balanced block.

For the odd-Jordan path this means that the source curvature of the input is simply its odd-current square on such a block:

\[
\boxed{
\mathfrak C_I(h)
=\|\mathcal P_{h\Lambda_{\rm odd}}\|_I^2\ge0.
}
\tag{L-90307.10}
\]

No bare-times-second-current cross survives.

## 4. Exact independent-frequency curvature identity in one metric

Apply PR #339 `L-33804` to the path `h_tau` and differentiate in the imaginary Jordan direction. Using (L-90307.5)--(L-90307.6) gives exactly

\[
\boxed{
4\mathfrak C_I(h)-\mathfrak C_I(c)
=3\bigl[\mathfrak C_I(g)-\mathfrak C_{I-\log4}(g)\bigr].
}
\tag{L-90307.11}
\]

Equivalently,

\[
\boxed{
\mathfrak C_I(c)+3\mathfrak C_I(g)
=4\mathfrak C_I(h)+3\mathfrak C_{I-\log4}(g).
}
\tag{L-90307.12}
\]

This recovers the resident Q4 reservoir identity, now with an explicit source/state dictionary and with all three paths living in the **same independent-frequency physical block metric**.

There is no mass-matrix change, no orthonormalisation, and no diagonal-frequency replacement.

## 5. Q2 cascade uses the same carrier

With the same `g_tau`, put

\[
p_\tau=(1+z)g_\tau,
\qquad
r_\tau=(1-z)g_\tau,
\qquad
c_{2,\tau}=(1-2z)g_\tau.
\tag{L-90307.13}
\]

The fixed-filter Q2 identities resident on the corrected Q2/Q4 branch are therefore identities of the **same odd-Jordan carrier**. In particular the Q4 factorization

\[
\frac{1-4z^2}{1-z^2}
=\frac{1-2z}{1-z}\,
 \frac{1+2z}{1+z}
\tag{L-90307.14}
\]

is an exact two-stage cascade without introducing a new Jordan deformation or a new Hilbert metric.

Thus the current/predecessor states in the Q2 tight frame and the Q4 all-pass state can be assembled before any inequality is applied.

## 6. Why the odd-Jordan energy is already RH-sensitive

The first odd-Jordan jet of the compact source is

\[
q_{\sharp,\mathrm{odd}}
=B_\sharp\Lambda_{\rm odd}.
\tag{L-90307.15}
\]

At any hypothetical nontrivial zeta zero `rho` with `Re rho>1/2`, the dyadic numerator `1-4^{1-rho}` is nonzero and the odd Euler logarithmic derivative has a simple pole. Hence `q_(sharp,odd)` has a non-cancelled pole of order at least two at `rho`.

Consequently a subexponential physical local-energy bound for this odd-Jordan current is itself a valid pole-exclusion target; one does not need to return to the full `s`-derivative before applying the pole criterion. This statement uses only zero-safety of the finite dyadic factors; it does not prove the required energy bound.

## 7. Relation to the transcript's mass-matrix lesson

The Anthropic campaign's one-half proof initially suffered from an ill-conditioned mass-matrix normalisation and was repaired by working directly in coefficient coordinates and using an exact Poisson identity. The present identity follows the analogous proof order:

```text
freeze the source coordinate;
keep the exact independent-frequency block metric;
apply parameter-independent filters there;
only then estimate inertia/curvature.
```

Trying instead to differentiate moving dyadic filters recreates derivative gauges which are absent in (L-90307.7).

## 8. Proof boundary

Closed exactly here:

1. common odd-Jordan carrier for `g,h,c`;
2. exact all-order Q4 source/state identities `E4 h=c`, `R4 h=(sqrt3/2)g`;
3. exact zero-bare property of the input `h` on deep balanced blocks;
4. one-metric independent-frequency curvature identity;
5. compatibility with the exact two-stage Q2 cascade;
6. zero-safety of the compact odd-Jordan current as an RH pole consumer.

Still open:

1. inserting the lower-order inertia defect of `L-90304/L-90305` into this exact source dictionary at the full finite-block level;
2. finite endpoint collars and any source species not contained in the odd-core deformation;
3. the coefficient-one global recurrence;
4. RH.