# Sixth-power extraction does not yet identify a subtractable correction

Status: source audit and a precise remaining transfer statement.

Scope: de Faveri's sixth-order upper-bound proof and its possible use
with the new actual-Möbius primitive-residue pairing. No residual
large-sieve estimate or improved zero-free boundary is claimed.

## 1. Exact place where the cross term enters

Source: A. de Faveri, *Optimal large sieve for fixed order characters*,
arXiv:2610.04045v1, especially Lemmas 4.4, 5.1, 6.1 and Proposition 7.1:
<https://arxiv.org/html/2610.04045v1>.

The source completes the row sum, performs gcd sorting and Poisson,
and then extracts sixth powers from the dual row. With initial lengths
(A,B), the generic dual length is X=B^2/A. Writing the dual row as
r e^6, and fixing Ne about E, leaves a sixth-power-free core of length
X/E^6. The estimate replacing this block by an operator norm has cost

\[
 \frac AB\,E\,\Theta_6(X/E^6,B)\|\lambda\|_2^2.
 \tag{1}
\]

The B term, maximized at E about X^(1/6), produces
\(A^{5/6}B^{1/3}\). Symmetry supplies the other cross term.

This explains the exponent. It is an inequality after coefficient
suprema, rather than a finite-rank decomposition of the original
quadratic form.

## 2. What the exact short-core functional contains

In the squarefree-column branch the root-number splitting in source
Lemma 3.3 modifies the column coefficient to
\(\lambda'_n=\lambda_n\beta_n\), with |beta_n|=1. A short-core block
contains a functional of the form

\[
 L_{R,e}(\lambda)
   =\sum_{\substack{n\asymp B\\(n,eQ)=1}}
       \lambda_n\beta_n\overline{\chi_n(R)}\,
       W_1(Nn/B),
 \tag{2}
\]

with the source's Mellin powers and fixed ray factors retained in W1
and beta. The e mask is a natural character zero from extracting e^6;
it is not optional. Earlier gcd variables create additional fixed-in-
that-block punctures and cubic twists. For nonsquarefree columns, the
two cross-root-number factors in Lemma 3.3 also remain.

For the actual coefficient lambda_n=mu(n)nu(n)W(Nn/B)/sqrt(Nn), (2)
is a finite Möbius--Gauss sum. It is not the new residue pairing

\[
 \sum_n\frac{\mu(n)\nu(n)}{\sqrt{Nn}}W(Nn/B)
                 \rho_{\rm prim}(nR).
 \tag{3}
\]

The new reference-scale lemma estimates (3). Replacing (2) by (3)
requires an additional exact transform and an estimate for its
continuous remainder. Meromorphic continuation or a pole-only
identity does not provide that replacement.

## 3. Why the published recursion cannot simply be projected

The source takes absolute values across gcd and puncture contributions
in Lemma 4.4, before the final norm recursion. Its equation (5.3) then
bounds the two decoupled sums by |S1||S2|. The signed coprimality
projector has already been discarded at this point. Lemma 6.1 finally
uses a supremum over coefficients, and the iteration uses duality.

These operations are legitimate for an upper bound. They do not show
that the bad contribution equals the actual row compression
\(A^*VG^{-1}V^*A\). In particular, deleting the B summand in (1)
after subtracting that compression has no established justification.
The moving e masks in (2) also produce a family of masked Gauss
vectors, not one fixed Gram matrix.

For an arbitrary vector alpha, the exact statement remains

\[
 \|A\alpha\|^2
   =\|G^{-1/2}V^*A\alpha\|^2+
       \|(I-VG^{-1}V^*)A\alpha\|^2.
 \tag{4}
\]

An upper bound for the first summand is not an upper bound for the
second. This is especially relevant to the actual inverse range
U<D: even an arbitrary-coefficient complement estimate of size U+D
would retain D, whereas the inherited actual-coefficient term is
\(U^{1/6}D^{5/6}<D\).

## 4. A concrete sufficient next result

A usable transfer would keep the original coefficients and prove an
exact signed Poisson identity separating (i) a correction expressed
through the already estimated residue pairings and (ii) a remainder
whose quadratic form on the prescribed Möbius coefficient gains a
fixed power in the active range. It must retain every gcd projector,
the moving masks in (2), the two root-number orientations under
iteration, and the common Mellin profile.

Equivalently, at the signed inverse interface already isolated in the
repository, one can seek a fixed theta>0 in

\[
 I(H,D)\ll(HDNQ)^\epsilon
 \left[H+\frac HD
     \left(\frac{D^2}{H}\right)^{5/6-\vartheta}
                   D^{1/6+\vartheta}\right].
 \tag{5}
\]

The exponent in (5) improves the inherited non-volume term by
\((D/H)^{-\vartheta}\) when D>H. The de Faveri theorem, the conditioned
Gauss frame, and the new scalar residue estimates do not yet prove
(5). They identify useful pieces of the required correction, while
leaving its exact transfer to the full signed quadratic form open.

No numerical experiment was used in this audit.
