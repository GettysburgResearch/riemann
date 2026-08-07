# L-25604 — Cyclic phase lift and positive depth frame

Claim ID: `L-25604`  
Title: Root-of-unity polarization turns the finite-resolvent depth decomposition into an exact positive Fourier frame, but leaves one full-scale Möbius anchor  
Status: **PROPOSED EXACT ALGEBRAIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-07  
Issue: #256  
Dependencies: `L-25601`; finite Fourier orthogonality; `L-9518`  
Scope: exact positive frame and reflected color identities; no estimate of the anchor color

## 1. Colorized inverse systems

Retain `M=M_V`, `R=1-zeta M`, and `C=M^(-1)`.  For every `K`-th root of
unity `omega`, define

\[
\boxed{
A_\omega(s)=C(s)(1-\omega R(s)),}
\tag{L-25604.1}
\]

\[
\boxed{
B_\omega^{[K]}(s)
=M(s)\sum_{j=0}^{K-1}\omega^jR(s)^j.}
\tag{L-25604.2}
\]

Then

\[
A_\omega B_\omega^{[K]}=1-R^K.
\tag{L-25604.3}
\]

Because the coefficients of `R^K` occur strictly above the finite endpoint,
`B_omega^[K]` is the coefficientwise inverse of `A_omega` through `X`.

For `omega=1`,

\[
A_1=C(1-R)=\zeta.
\tag{L-25604.4}
\]

Thus the physical zeta source is one distinguished color.

## 2. Color logarithmic derivatives

The exact logarithmic derivative is

\[
L_\omega(s)
=-{A_\omega'(s)\over A_\omega(s)}
={M'(s)\over M(s)}
+{\omega R'(s)\over1-\omega R(s)}.
\tag{L-25604.5}
\]

Its finite depth synthesis through `X` is

\[
\boxed{
L_\omega^{[K]}(s)
=\lambda_0(s)+
\sum_{j=1}^{K-1}\omega^j\lambda_j(s),}
\tag{L-25604.6}
\]

with the depth coefficients `lambda_j` of `L-25601`.  The omitted tail is
coefficientwise zero through `X`.

## 3. Exact depth Parseval frame

Let `Omega_K` be the set of `K`-th roots of unity and let
`f_0,...,f_(K-1)` be vectors in any complex Hilbert space.  Put

\[
F_\omega=\sum_{j=0}^{K-1}\omega^jf_j.
\]

Finite Fourier orthogonality gives

\[
\boxed{
\sum_{\omega\in\Omega_K}\|F_\omega\|^2
=K\sum_{j=0}^{K-1}\|f_j\|^2.}
\tag{L-25604.7}
\]

In particular,

\[
\boxed{
\|F_1\|^2
\le
\sum_{\omega\in\Omega_K}\|F_\omega\|^2.}
\tag{L-25604.8}
\]

Apply this to the physical block fields associated with the depth coefficients
`lambda_j`.  The zeta field `F_1` is therefore contained in one exact positive
finite color frame.

## 4. Reflected Selberg identity for every color

For each `omega`, the generalized Selberg coefficient identity applies to
`A_omega`.  Pair `A_omega(w+it)` with
`A_conj(omega)(w-is)`.  Their logarithmic derivatives are conjugate on a real
vertical line, so the two-frequency reflected identity produces the positive
physical color energy

\[
\int_J^{J+1}|F_\omega(x)|^2dx.
\tag{L-25604.9}
\]

Summing these identities over all colors and using (L-25604.7) preserves every
depth cross term exactly and leaves a diagonal positive depth frame.

This is a genuine positive enlargement of the single zeta identity, not an
entrywise absolute-value bound.

## 5. What the phase lift closes

The phase lift supplies:

1. an exact positive depth frame;
2. a complete packet source map for every color;
3. Fourier cancellation of unequal depth indices;
4. a source-bound route for checking all reflected cross terms;
5. at most a polynomial-in-`K` frame cost, harmless for fixed `K` as
   `J->infinity`.

Thus the packet/global mismatch and abstract depth-kernel obstruction are not
fundamental once all colors are retained.

## 6. The anchor color survives

The color `omega=1` is exactly `zeta`.  The other colors do not subtract its
positive energy; they enlarge the left side.  To derive an upper bound for
`F_1`, the summed color forcing must still be estimated.

By `L-25603`, all reciprocal-free color/depth differences can be routed into
finite complete-lattice or boundary terms, but one full-scale meromorphic
anchor remains.  Its physical representative is a fixed-ratio Möbius shell.

Therefore (L-25604.8) is not itself a proof of a subexponential zeta block.  It
reduces the reserve problem to the statement

\[
\boxed{
\text{summed nonanchor color forcing}
+\text{lower-scale terms}
\text{ dominate the anchor forcing with a strict margin}.}
\tag{L-25604.10}
\]

No such margin follows from Fourier orthogonality alone.

## 7. Proof boundary

Closed exactly here:

- the root-of-unity finite inverses;
- the finite color logarithmic derivatives;
- Hilbert-space depth Parseval;
- one reflected positive identity per color;
- polynomial frame containment of the zeta color.

Open:

- a strict source-specific forcing reserve for the anchor color;
- fixed-ratio shell energy;
- RH.
