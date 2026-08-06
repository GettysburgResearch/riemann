# L-15435 — Probabilistic beta-resolvent factorization and the archimedean total-positivity boundary

Claim ID: `L-15435`  
Title: The smoothing kernel is the law of an exponential plus a logarithmic beta variable, and is not a Pólya-frequency density of infinite order for `0<s<1`  
Status: `PROPOSED — COMPLETE PROBABILITY FACTORIZATION AND PF-INFINITY OBSTRUCTION`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: `L-15430`, `L-15434`; Schoenberg's characterization of Pólya-frequency densities on the half-line  
Scope: the archimedean beta-resolvent alone; the coupled arithmetic defect may still be totally positive  
Related counterexample candidates: none

## 1. Normalize the beta-resolvent

For `0<s<1`, let `n_s` be the density from `L-15434`, with

\[
\widehat n_s(q)
=\pi^{s/2}
 {\Gamma((3+q)/2)
  \over(q+s)\Gamma((3+s+q)/2)}.
\tag{L-15435.1}
\]

Its total mass is

\[
\boxed{
\mathfrak m_s
=\widehat n_s(0)
=\pi^{s/2}
 {\Gamma(3/2)
  \over s\Gamma((3+s)/2)}.}
\tag{L-15435.2}
\]

## 2. Exact beta–exponential law

Let

\[
U_s\sim {\rm Beta}(s,1),
\qquad
B_s\sim {\rm Beta}(3/2,s/2)
\tag{L-15435.3}
\]

be independent, and define

\[
\boxed{
T_s=-\log U_s-{1\over2}\log B_s.}
\tag{L-15435.4}
\]

Equivalently,

\[
T_s=E_s+V_s,
\qquad
E_s\sim {\rm Exp}(s),
\qquad
V_s=-{1\over2}\log B_s.
\tag{L-15435.5}
\]

Then

\[
\boxed{
{n_s(t)\over\mathfrak m_s}\,dt
=\Pr(T_s\in dt).}
\tag{L-15435.6}
\]

### Proof

For `q>=0`,

\[
\mathbb E[U_s^q]={s\over s+q},
\tag{L-15435.7}
\]

and the beta moment formula gives

\[
\mathbb E[B_s^{q/2}]
={\Gamma((3+q)/2)\Gamma((3+s)/2)
  \over
  \Gamma(3/2)\Gamma((3+s+q)/2)}.
\tag{L-15435.8}
\]

Multiplication and (L-15435.1)--(L-15435.2) yield

\[
\mathbb E[e^{-qT_s}]
={\widehat n_s(q)\over\widehat n_s(0)}.
\tag{L-15435.9}
\]

Uniqueness of Laplace transforms proves (L-15435.6).

Thus the special incomplete-beta kernel in the final RH gate has a concrete
probabilistic meaning:

```text
one exponential Green delay
    +
one logarithmic beta delay.
```

## 3. Resolvent equation from the probability split

Let `beta_s` denote the positive source density associated with `V_s`, with the
normalization inherited from `L-15431`.  Convolution with the exponential law
in (L-15435.5) gives

\[
\boxed{
n_s'(t)+s n_s(t)=\beta_s(t),
\qquad n_s(0)=0.}
\tag{L-15435.10}
\]

This recovers the beta-resolvent differential equation without differentiating
an incomplete beta function.  The positive exponential mixture of `beta_s`
and the no-interior-minimum theorem of `L-15431` are probabilistic consequences
of this split.

## 4. The archimedean kernel is not PF-infinity

A density on the half-line is Pólya-frequency of infinite order only if the
reciprocal of its normalized Laplace transform extends to an entire function of
Schoenberg product form.

Here

\[
\boxed{
{1\over\mathbb E[e^{-qT_s}]}
={q+s\over s}
 {\Gamma(3/2)\Gamma((3+s+q)/2)
  \over
  \Gamma((3+s)/2)\Gamma((3+q)/2)}.}
\tag{L-15435.11}
\]

For `0<s<1`, the numerator gamma factor has poles at

\[
q=-3-s-2k,
\qquad k=0,1,2,\ldots,
\tag{L-15435.12}
\]

while the reciprocal denominator gamma has zeros at

\[
q=-3-2k.
\tag{L-15435.13}
\]

The two lattices do not coincide, and the factor `q+s` cancels none of the
poles in (L-15435.12).  Therefore the reciprocal transform is meromorphic but
not entire.  Schoenberg's necessary condition fails, and

\[
\boxed{
{n_s\over\mathfrak m_s}
\text{ is not a }PF_\infty\text{ density for }0<s<1.}
\tag{L-15435.14}
\]

## 5. Consequence for the global proof strategy

The complete-monotonicity target in `L-15434` cannot follow from a generic
variation-diminishing theorem applied to the beta-resolvent alone.  The
archimedean smoother does not possess infinite-order total positivity in the
relevant parameter range.

This is a useful fail-closed boundary:

```text
false shortcut:
    n_s is PF-infinity
    -> every signed Jordan discrepancy is regularized to one sign;

surviving route:
    the arithmetic prime-coordinate law and the beta delay must be coupled
    before total positivity is tested.
```

In particular, the completed-xi ratio defect may still be completely monotone.
Equation (L-15435.14) says only that such a theorem would be genuinely
arithmetic; it cannot be inherited for free from the gamma/beta channel.

## 6. Proof boundary

- The beta/exponential factorization is exact.
- The PF-infinity obstruction uses only the necessary entire-reciprocal part of
  Schoenberg's theorem.
- No finite-order sign-regularity classification is claimed here.
- The result does not refute `Y_s>=0`; it refutes only an archimedean-only
  total-positivity proof of that inequality.
