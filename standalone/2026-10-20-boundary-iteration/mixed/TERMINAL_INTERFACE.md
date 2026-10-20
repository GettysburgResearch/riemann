# Where the new cubic estimate meets the selected terminal norm

Date: 2026-10-20. Status: exact interface and exponent audit. The quadratic
twist estimate discussed below is a separate proposed input in the
neighboring `type_i` directory. This note does not certify its analytic
proof or claim an improved zero-free boundary.

## 1. The actual arithmetic block

The inherited selected terminal polynomial, Liu Theorem 11.2 and
Lemma 11.1, is recorded in
`../../2026-10-20-angular-hecke-continuation/ANGULAR_THETA_AND_INVERSE.md`,
equation (7.7). After fixing the cube index, supported factors, finite
sectors, and the common smooth Fourier mode, its physical squarefree
coefficient has the form

\[
 \sum_P\frac{a(P)}{\sqrt{q_P}}\mathbf1_{(P,Rb)=1}
 \sum_n\frac{\widetilde g(n)\alpha(n)^\ell\nu(n)}{\sqrt{q_n}}
   \chi_R(n)^3\chi_P(n)^{-2}W_U(q_n/U)W_L(q_P/L),
 \tag{1.1}
\]

up to bounded frozen phases and the separate cube normalization. Here
\(R,n,P\) are squarefree, \(q_R\asymp K,q_n\asymp U,q_P\asymp L\),
\(\ell\ne0\) is fixed, and the prime-tuple coefficient \(a(P)\) is
independent of \(R,n\). The condition \((n,P)=1\) is already the
literal zero of \(\chi_P(n)^{-2}\). A fixed finite ray twist can be
absorbed only if the imported Type-I statement includes it; it cannot be
treated as a growing conductor for free.

The cubic Gauss multiplicativity identity is

\[
 \widetilde g(nP)=\widetilde g(n)\widetilde g(P)
                      \chi_P(n)^{-2}
 \tag{1.2}
\]

on coprime squarefree indices. Both sides vanish on collisions. At each
fixed \(R,b\), the bounded outer coefficient

\[
 b_P=\frac{a(P)\mathbf1_{(P,Rb)=1}}
             {\widetilde g(P)\alpha(P)^\ell\chi_R(P)^3}
 \tag{1.3}
\]

therefore converts (1.1) into the quadratic-twisted cubic Type-I block,
with free variable length \(A=U\), outer variable length \(B=L\),
cubic level \(r=1\), and quadratic conductor norm \(H=K\). Equation
(1.3) is evaluated only on its coprime support; no zero symbol is
inverted. Its dependence on the fixed row is harmless for a **pointwise**
Type-I bound, but prevents treating it as a row-independent coefficient
in a subsequent average without another argument.

## 2. The conductor range is the obstruction

The proposed quadratic-twisted bound from the neighboring work has shape

\[
 |T_\xi|\ll A^p B^{3/2-4p/5}H^{1-6p/5},
 \qquad H\le B,
 \quad p=(2\beta+1)/6.
 \tag{2.1}
\]

Its useful conductor range becomes \(K\le L\) in (1.1). The source
class which determines the current boundary has short active prime
tuples: \(K\gg L\). Thus applying (2.1) there without its condition
would be invalid.

The free-split approximate functional equation suggests the following
outside-range bound by balancing its large original-series term against
the absolute dual term:

\[
 |T_\xi|\ll A^p B^{3/2-p}H^{1-p},\qquad H\ge B.
 \tag{2.2}
\]

Even granting (2.2), dividing by \(\sqrt{UL}\), squaring, and summing
over the \(O(K)\) possible rows gives only

\[
 U^{2p-1}L^{2-2p}K^{3-2p}.
 \tag{2.3}
\]

At the binding physical terminal scale \(U=KL\), this is exactly

\[
 K^2L,
 \tag{2.4}
\]

independently of \(p\). The inherited hybrid sieve at the same scale
is \(O(KL)\), up to small powers, when \(K\ge L\). Consequently
improving the fixed-character zero-free input in this pointwise route
does not fix the missing factor \(K\). A genuine average over the
quadratic rows, preserving the dependence in (1.3), is necessary.

Swapping the two Type-I variables is not an immediate remedy: the new
free variable would be the selected prime tuple, whose coefficients and
support are not an unrestricted smooth sum. A prime decomposition also
moves the long column into the costly outer variable, and needs its own
complete estimate.

## 3. The marked-canonical route meets the same scale

The new bound in `MARKED_CANONICAL_MEAN.md` gives, in the unlabelled case,

\[
 J_A(K,D)\ll K+D+K^{5/6}D^{1/6}P^{5/6}
                         +K^{5/6}D^{-1/9}P^{5/3}.
 \tag{3.1}
\]

Its local saving \(KP^{5/6}\) occurs at \(D=K\), for
\(P\le K^{1/3}\). At the actual first selected-moment edge
\(D=KP\), however, the first marked cross term in (3.1) equals
\(KP\) exactly. For \(K\ge P^2\), the last term is no larger.
The bound therefore reaches the inherited edge but gives no strict
saving there.

The minimal useful target for this route is a strict power saving over
\(KP\) for the prescribed marked canonical norm at \(D=KP\),
uniformly on an open range with \(K\gg P\), including its original
puncture, finite ray factors, complete cube dependence after reflection,
and joint smooth profile. A bound for an unrelated unmarked coefficient,
or at the isolated balanced scale \(D=K\), does not supply that target.

The following exact identity also prevents a spurious feedback claim.
The squarefree product of an inverse polynomial of length \(D\) and
selected primes of total length \(P\) becomes a divisor-marked inverse
at length \(Y=DP\), after the original common-prime splits. Applying
the new marked inverse bound at \(Y\) yields

\[
 U^{1/6}\max\{U,DP^2,D^{2/3}P^{8/3}\}^{5/6},
 \tag{3.2}
\]

the same all-length selected estimate from which it was deduced.
The arithmetic transformation is useful for locating the gap; it does
not produce a new independent analytic input.

## 4. The sharp additive Gram estimate is already included

Xu--Sang, arXiv:2610.17675v1, Lemma 4.1, (4.3), gives at
\(q=XY,L=Y\) the three effective terms
\(X+X^{5/6}Y^{1/6}+Y/X\). Liu's current compensated comparison
already uses exactly these terms in Lemma 13.2, (13.7), with the actual
subset scales \(X',Y'\). Consequently the apparent square-root saving
\(Z^{-5b/12}\) over the older bound \(Y\) is already incorporated in
\(G=\max(0,b/12,b-l_y/2)\); it cannot be subtracted again from the
current low-side exponent. The full substitution and source pins are in
[ADDITIVE_GRAM_COMPARISON.md](ADDITIVE_GRAM_COMPARISON.md).
