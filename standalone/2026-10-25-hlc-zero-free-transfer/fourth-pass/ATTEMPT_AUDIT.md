# Audited continuation routes: backtracks and multiple ratio scales

This records two further attempts made during the fourth pass. One proposed
backtrack bound failed a source-normalization check and is withdrawn. The
multiple-scale argument does give the uniform witness statement below, but
it does not yield a new power saving. No lower bound for the actual native
moment or the complete HLC pairing is asserted.

## 1. The rejected raw-backtrack normalization

The HLC source is Lü--Wang--Wu,
[arXiv:2610.20242v1](https://arxiv.org/pdf/2610.20242), p. 18, the
definition of K_1 immediately before T_1. Its geometric prefactor is

\[
 \frac{d_0}{D}\,
 \eta(a/Y)\eta(b/Y)\psi_1(t/Y),
\]

followed by the raw-minus-major-arc bracket and the retained damping.
**There is no further factor \(1/Y\) in this original kernel.**

In normalized unordered-list states, `HLC_PATH_CANCELLATION.md`,
Section 6, correctly gives the entry

\[
 (J+1)^{-K}\left(\prod_i V_i^{-1}\right)
                         K_1(P,Q;D,a,b).
\]

The proposed payment was to combine an entry of size \(O(1/Y)\)
with \(O(Y)\) candidate targets and infer an \(O(1/Y)\) diagonal
of the raw operator times its adjoint. That first entry bound was based
on misreading \(d_0/D\) followed by \(\eta(a/Y)\) as if it
contained \(d_0/(DY)\). The author of the HLC note independently
caught the error. The proposal was withdrawn before publication.

The \(1/Y\) occurring in the source's separately converted clean
auxiliary operator is accompanied by a different measure and coordinate
normalization. It cannot be copied into this original matrix entry.
With the genuine original normalization, the same crude target count
does not save a power. A row sum of squares would describe the diagonal
of \(T_{\rm raw}T_{\rm raw}^*\), but would not by itself control
the norm of that entire operator or the full signed Fock trace.

The new integer backtrack theorem remains valid: a largest-group
immediate memory return under the full source good-state condition
restores the unordered complete lists and the integer position. Paying
all such contractions with their genuine memory weights, or controlling
their pairing with the actual structured endpoints, is still additional
work. No incorrect \(1/Y\) bound is used in another fourth-pass result.

## 2. A valid simultaneous thin-shell localization

This deduction uses the exact scope, coefficients, natural zeros,
primitive reflection, finite-order family cap and buffered bins of
`COHERENT_IDENTITY.md` and `MIDDLE_JOINT.md`. The analytic premises
remain imported with those notes' qualifications.

Fix \(0<\kappa<4/25\), \(29/25\le r\le117/100\), and
\(D=U^r\). For any scale

\[
                     U\le T\le D/U^\kappa,                 \tag{1}
\]

use three common smooth weights

\[
 H_T(a)=\chi(Na/(2T)),\quad
 K_T(a)=\chi(Na/(T/U^\kappa)),\quad
 G_T(R)=1-\chi(R/T).                                       \tag{2}
\]

They obey \((1-H_T)(1-G_T)=0\), since \(Na\le R\) term by
term in the full reflected expression. Thus

\[
 M=M_{H_T,1}+M_{1,G_T}-M_{K_T,G_T}-C_T,
 \qquad C_T=M_{H_T-K_T,G_T}.                               \tag{3}
\]

Every term of the coherent corner C_T satisfies

\[
            R>T,\qquad T/U^\kappa<Na<4T,\qquad Na\le R.    \tag{4}
\]

### The two pointwise terms are small on the same bin

For a buffered bin with \(\delta=2a_\circ-1\), the joint returned
head theorem gives

\[
 |M_{H_T,1,u}|\ll (2T/D)^{1/8}D^{\delta/2}U^\epsilon.
\]

The three-Mellin overlap proof, with T retained as its outer threshold,
gives the corresponding pointwise bound

\[
 |M_{K_T,G_T,u}|\ll
 \left(\frac{T/U^\kappa}{T}\right)^{1/8}
                         D^{\delta/2}U^\epsilon.
\]

Hence both are

\[
                 O(U^{-\kappa/8+\epsilon}D^{\delta/2})       \tag{5}
\]

uniformly over (1). The exponent \(1/8\) has its usual arbitrarily
small loss from choosing \(\beta>7/8\). Norm-height and fixed
seminorm costs are absorbed only after the source's order of choices.
All frequencies use one actual buffered height; no independent row
character or coefficient choice is introduced.

### The original far term can be controlled at every T at once

The old asymmetric far proof is uniform for \(G_T\) when \(T\ge U\).
Its nonempty triples still have their long inverse exponent in
\([1-\alpha,r-\alpha]\), with \(\alpha=2/125\). The same
proof applies to its logarithmic scale derivative, since

\[
 \frac{\partial}{\partial\log T}G_T(R)
                       =(R/T)\chi'(R/T)
\]

is a common smooth cutoff supported in \(T<R<2T\). Therefore both
the far expression and this derivative have squared row mean

\[
                 \ll U^{e_0(r)-1/750+\epsilon}.             \tag{6}
\]

Cover the interval of \(\log T\) in (1) by \(O(\log U)\) unit
intervals. On each, the one-dimensional Sobolev inequality bounds the
supremum of the square by the integral of the square of the function
and its first derivative. Sum rows before integrating. The logarithmic
number of intervals is absorbed in epsilon. Consequently

\[
 \boxed{\quad
 \sum_u w_U(u)\sup_{U\le T\le D/U^\kappa}
                         |M_{1,G_T,u}|^2
       \ll U^{e_0(r)-1/750+\epsilon}.
 \quad}                                                     \tag{7}
\]

This is an actual simultaneous bound; it does not require assigning
statistically independent errors to different scales. The finite
dimensional common detector-profile parameters can be included using
the same prescribed Sobolev calculus. For an unweighted count below,
take \(w_U=1\) on the relevant class, or a weight bounded below there.

Suppose an actual detector supplies

\[
                 |M_u(D;V_u)|\ge\sqrt c\,
                         U^{\delta r/2-\omega/2},           \tag{8}
\]

with fixed \(c>0\) and sufficiently small preliminary loss omega.
Choose \(\epsilon+\omega/2<\kappa/8\). By (5), for sufficiently
large U, the two pointwise terms in (3) are each at most one eighth
of the threshold in (8), uniformly in T.

Outside at most

\[
              U^{e_0(r)-\delta r-1/750+\epsilon+\omega}      \tag{9}
\]

rows, (7) makes the far term at most one quarter of that threshold for
**every** T in (1). The triangle inequality in (3) then proves

\[
 \boxed{\quad
 |C_{T,u}|\ge\tfrac12\sqrt c\,
 U^{\delta r/2-\omega/2}
 \quad\hbox{for every }U\le T\le D/U^\kappa,
 \quad}                                                     \tag{10}
\]

for each remaining witness. This is a proved localization consequence;
it is not an upper bound for the unresolved corner spike set.

## 3. Why these many corners do not yet improve the exponent

For fixed positive kappa, disjoint exponent shells in the interval
(1) yield only \(O((r-1)/\kappa)\) pieces. Ordinary dyadic choices
yield \(O(\log U)\) scales, with substantial overlap in (4). Their
norms cannot be added as orthogonal energies without a separate theorem.

There is also an exact arithmetic reason not to posit independence.
Let \(D_{C_T,P}(m)\) denote the returned primal coefficient of C_T.
The coefficient calculation from `COHERENT_IDENTITY.md`, (21)--(24),
now gives

\[
 D_{C_T,P}(m)
 =D_{H_T,1,P}(m)-D_{K_T,G_T,P}(m)-A(m)\chi(Nm/T),           \tag{11}
\]

and, for each fixed \(\theta=1-\beta\in(0,1/8)\),

\[
 |D_{H_T,1,P}(m)|+|D_{K_T,G_T,P}(m)|
        \ll U^\epsilon\{(2T/D)^\theta+U^{-\kappa\theta}\}
        \ll U^{-\kappa\theta+\epsilon}.                   \tag{12}
\]

Thus, for every natural-unit m with \(Nm\le U\), all these returned
corners have the **same** coefficient

\[
                 D_{C_T,P}(m)=-A(m)
                               +O(U^{-\kappa\theta+\epsilon})
\]

uniformly over (1). In particular the old critical squarefree primal
coefficients are repeated coherently as T varies. This is not a lower
bound for their signed row sums, but it precludes treating the different
reflected shells as independent primal supports.

No new fixed-power mean saving, no new residual spike estimate, and no
new zero-free region follows from (7)--(12) alone. The useful new content
is the simultaneous witness localization and its explicit exceptional
count, together with the exact coefficient identity that must be
respected by any proposed multiple-scale gain.
