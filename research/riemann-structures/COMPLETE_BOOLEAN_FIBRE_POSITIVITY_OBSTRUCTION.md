# Complete rough Boolean fibres force a growing canonical principal candidate

Status: **a lower bound for a completely defined arithmetic Boolean
candidate, not for the complete retained-gamma native source**. RH remains
unproved. Unlike the dense-owner restriction alone, this theorem includes
every allowed owner and core cofactor in its selected conductor fibres.
Their signs are forced nonnegative by the actual Boolean coefficient.
It follows that the clean canonical candidate defined below has principal
moment at least \(C Y^{1/2}/(\log Y)^{11}\). Its previously proved
subpower diagonal does not control that moment.
The completely unmasked candidate also has a power lower bound, with three
additional logarithms: \(P_B^{\rm all}\ge C'Y^{1/2}/(\log Y)^{14}\).

The candidate is the exact arithmetic object in the concurrently developed
[canonical Boolean diagonal theorem](https://github.com/gfreund123/riemann/blob/5b25f2dace65dd4d46e16d566f2dc7a34b98f41d/research/l-families/atlas/function_field/FFPS_CANONICAL_BOOLEAN_PRINCIPAL_DIAGONAL.md),
with a specified nonnegative physical mask. That theorem bounds its
diagonal and explicitly does not identify it with the native gamma
source. The related
[decoder diagnostic](https://github.com/gfreund123/riemann/blob/5b25f2dace65dd4d46e16d566f2dc7a34b98f41d/research/exploratory/NATIVE_BOOLEAN_DECODER_DIAGNOSTIC.md)
likewise leaves the full native map open. We retain both boundaries and
make no priority claim for those predecessor statements.

## 1. Define the complete candidate and its physical mask

Let \(U\) be dyadic and \(Y=U^6\). A tuple
\(\mathfrak a=(P,Q,g,c,d)\) belongs to the clean ordinary-prime chart if
\(g,c,d\) are squarefree and mutually coprime, \(c,d>1\), and \(P,Q\)
are products of two distinct primes each, with all four owner primes
distinct and disjoint from both cores. Exclude the exceptional prime 67.
Set

\[
 N=Pg^2c^2,\quad M=Qg^2d^2,\quad
 \ell=P^-(c),\quad\rho=P^-(d),\quad
 B_U(a)=\frac{b_U(a)}{\binom{\omega(a)+2}{2}},
\]
\[
 z^B_{\mathfrak a}(t)
 =\frac{B_U(gc)B_U(gd)}{g^2cd\sqrt{PQ}}
      e^{it\log(N/M)}.
\tag{1}
\]

The complete tuple set has \(N,M\le16Y\). Use the explicit physical mask

\[
 m_{\mathfrak a}
 =\mathbf1_{\{1/8<N/M<8,\ P\le gc,\ Q\le gd\}}.
\tag{2}
\]

These optional full-core owner inequalities make the comparison compatible
with the inherited owner-size chart. They retain the entire dense block
below. The proof also applies to any time-independent mask
\(0\le m_{\mathfrak a}\le1\) supported on ratio eight which equals one
on that dense block. A fixed positive lower bound there merely changes
the constant. Merely being nonzero there is insufficient.

Keep the actual quadratic classes
\(\sigma=\chi_\ell(Q),\tau=\chi_\rho(P)\), and form the complete
canonical member and principal moment

\[
 W^B_\iota(t)=\sum_{\mathfrak a\text{ in }\iota}
                m_{\mathfrak a}z^B_{\mathfrak a}(t),
 \quad
 P_B(Y)=\sum_\iota g^2\ell\rho c_\ell c_\rho
                   \int|W^B_\iota(t)|^2d\nu(t),
\tag{3}
\]

where \(\iota=(g,\ell,\rho,\sigma,\tau)\),
\(c_q=(q+1)/(q-1)\) and
\(d\nu=|\widehat\kappa(t)|^2dt/(2\pi)\) is the original native measure.
Every arithmetic tuple in the chart is included, not just a chosen set
of owners or core cofactors. There is one arithmetic atom per tuple;
the literal-history version has the same uncentered moment, with its
literal and grouped diagonals kept distinct.
For the scalar arithmetic candidate only, define \(\chi_2\) to be the
trivial character on odd integers. This makes its class convention total
when a phase prime is two; no characteristic-two Kummer or Gauss identity
is claimed. All selected rough fibres in the proof have odd phase primes.

## 2. Complete cofactor rigidity in the rough selected fibres

Use the seven intervals and conductor triples of the
[dense-owner theorem](DENSE_OWNER_PRINCIPAL_COEFFICIENT_FAMILY.md):
\(p,q,r,s,g,\ell,\rho\) lie in their seven successive windows just above
\(U\), with \(g,\ell,\rho\) in the last three. Now fix only
\((g,\ell,\rho)\) and consider **every** canonical tuple in that fibre.

Every prime factor of \(a=gc\) exceeds \(U\): the common core is the
prime \(g>U\), and the least prime of \(c\) is \(\ell>U\).
Also \(P\ge6\) and \(Pa^2\le16U^6\). If \(\omega(a)\ge4\), then

\[
 Pa^2>6U^8>16U^6\qquad(U\ge2),
\]

a contradiction. Therefore \(2\le\omega(a)\le3\). The same argument
applies to \(b=gd\).

On a squarefree support all of whose primes exceed \(U\), the truncated
Möbius source \(\mu_U\) is nonzero only on the empty support. The exact
Boolean identity gives

\[
 b_U(a)=\mu(a)-2\mu_U(a)+(\mu_U\star\mu_U\star1)(a)
        =\mu(a)+1.
\tag{4}
\]

It follows that \(b_U(a)=2\) for two labels and \(b_U(a)=0\) for three.
Thus every nonzero term in the complete selected fibre necessarily has

\[
 \boxed{c=\ell,\qquad d=\rho,\qquad
 B_U(gc)=B_U(gd)=1/3.}
\tag{5}
\]

Extra admissible prime cofactors do occur geometrically, but their complete
Boolean rows cancel exactly. They have not been discarded by a mask.
Every remaining owner coefficient is the positive real number
\(1/(9\sqrt{NM})\). The actual principal character roots may be chosen
trivial in L-106120.6; other root choices change only the sign of the whole
fixed quadratic class. Hence no extra character phase spoils this
positivity. No statement is made about the omitted native gamma factors.

## 3. A fixed observation interval prevents cancellation of the complete positive fibre

The ratio mask implies \(|\log(N/M)|<\log8\). Set

\[
 I=\left(-\frac1{2\log8},\frac1{2\log8}\right),\qquad
 C_\kappa=\frac14\nu(I)>0.
\tag{6}
\]

For \(t\in I\), every cosine of a retained Mellin phase exceeds one
half. Therefore, after choosing the harmless fixed class sign,

\[
 \operatorname{Re}W^B_\iota(t)
 \ge\frac12\sum_{\mathfrak a\text{ in }\iota}
       \frac{m_{\mathfrak a}}{9\sqrt{NM}}.
\]

Consequently

\[
 \boxed{\int|W^B_\iota|^2d\nu
 \ge C_\kappa\left(
       \sum_{\mathfrak a\text{ in }\iota}
       \frac{m_{\mathfrak a}}{9\sqrt{NM}}\right)^2.}
\tag{7}
\]

The strict positivity in (6) does not assume
\(\widehat\kappa(0)\ne0\); in fact that value vanishes. The compactly
supported nonzero \(\kappa\) has an entire Fourier transform: its
exponential power series converges uniformly on every bounded complex
set under the finite-support integral. If \(\nu(I)=0\), continuity
would make this transform zero throughout \(I\); the identity theorem
would make it zero everywhere, contradicting Plancherel and
\(\|\kappa\|_2^2>0\). Thus the fixed constant in (6) is positive.
No effective numerical lower bound is needed for the asymptotic theorem.

## 4. A lower bound for the complete canonical candidate

The dense owner block lies in the support of (2), with
\(Y<N,M<11Y/10\). Its left/right owner counts are
\(m,n=\Theta(U^2/(\log U)^2)\). The exact class partition gives
\(\sum m_\tau^2\ge m^2/2\),
\(\sum n_\sigma^2\ge n^2/2\), without a growing-modulus prime theorem.
Because the complete fibre coefficients are nonnegative, the sum in (7)
is at least the dense block's coefficient sum in each class.

There are \(\Theta(U^3/(\log U)^3)\) selected conductor triples and
each principal weight is \(\Theta(U^4)\). Repeating the dense theorem's
count with the positive constant \(C_\kappa\) instead of its local Gram
constant proves

\[
 \boxed{P_B(Y)\ge C\frac{Y^{1/2}}{(\log Y)^{11}}}
\tag{8}
\]

for all sufficiently large dyadic \(U\), with a fixed \(C>0\).
No matching upper order is claimed for the complete candidate. The other
fibres contribute nonnegative energies and cannot reduce this bound.

The predecessor's canonical arithmetic diagonal satisfies
\(D_B(Y)=Y^{o(1)}\), uniformly under the mask (2). Thus its centered
candidate \(P_B-D_B\) also has a power-sized lower bound. This does not
contradict the diagonal theorem; it settles the subsequent readout question
for this particular fully defined positive arithmetic candidate.

## 5. The completely unmasked canonical candidate also grows

Let \(P_B^{\rm all}\) use the same complete clean chart \(N,M\le16Y\)
and the mask identically one, without the ratio or owner-size conditions
in (2). The rough-cofactor argument (4)--(5) still applies in every
selected conductor fibre. All of its nonzero coefficients are positive.
Their physical products satisfy

\[
 6U^4<N,M\le16U^6,\qquad
 |\log(N/M)|\le\Lambda_U:=\log((8/3)U^2).
\tag{9}
\]

Use \(|t|<\delta_U=1/(2\Lambda_U)\) instead of the fixed interval (6).
The same cosine argument applies. The actual kernel has a simple Fourier
zero at zero, with a nonzero, explicitly known first derivative. Indeed,
putting \(r=2^s\), direct integration of the three literal kernel pieces
gives

\[
 \int_1^8 K(y)y^s\frac{dy}{y}
 =\frac{4(s+1)(r-1)^2(\sqrt2\,r-1)}{s(s+1/2)}.
\tag{10}
\]

The apparent singularities are removable. To check the identity without
analytic continuation, integrate \(A+B\sqrt y\) on each interval and
multiply by \(s(s+1/2)\). If
\(C(r)=4(r-1)^2(\sqrt2r-1)\), the numerator of the \(1/s\) terms is
\(2C(r)\), and that of the \(1/(s+1/2)\) terms is \(-C(r)\).
Their sum is \((s+1)C(r)\), proving (10) and its removable extensions.

With the native convention \(\widehat\kappa(t)\) equal to (10) at
\(s=-it\),

\[
 \widehat\kappa(t)=-i\alpha t+O(t^2),\qquad
 \alpha=8(\sqrt2-1)(\log2)^2>0,
 \qquad
 \nu((-\delta,\delta))\sim\frac{\alpha^2}{3\pi}\delta^3.
\tag{11}
\]

Thus the shrinking observation interval costs only
\(\Theta((\log U)^{-3})\). Apply the same complete positive-fibre and
dense-owner count on this interval to obtain

\[
 \boxed{P_B^{\rm all}(Y)\ge C'
             \frac{Y^{1/2}}{(\log Y)^{14}}.}
\tag{12}
\]

This does not infer monotonicity of Mellin energy under removal of a mask.
It proves a separate lower bound directly on the complete unmasked
positive fibres. No matching upper order is claimed. The unmasked
canonical diagonal remains bounded by the predecessor's subpower theorem.

## 6. Consequence for a proposed native decoder

Suppose a proposed decoder actually places the complete native source and
this candidate in the same original weighted principal Hilbert space,
with

\[
 W_{\rm nat}=W_B+R.
\]

The reverse triangle inequality gives the exact necessary condition

\[
 \boxed{\|R\|\ge\sqrt{P_B}-\sqrt{P_{\rm nat}}.}
\tag{13}
\]

If the intended native principal moment is subpower, (8) and (13) require

\[
 \|R\|=\Omega\!\left(
       Y^{1/4}/(\log Y)^{11/2}\right).
\tag{14}
\]

Therefore a subpower-error identification of the native member with this
positive canonical candidate cannot at the same time prove a subpower
native principal moment. Equality, a small correction, or a bounded
nonnegative physical mask retaining the dense block are not free decoder
choices. A viable map must carry substantial cancellation, change the
candidate/mask, or preserve further source information.

For the entirely unmasked candidate the same necessary argument using
(12) requires \(\|R\|=\Omega(Y^{1/4}/(\log Y)^7)\). In particular it
also excludes a subpower-error comparison with that exact candidate,
conditional on the intended native moment being subpower.

This is conditional on the common-Hilbert-space comparison, not an assertion
that such a decoder has been constructed. The actual native gamma source
and its moment remain unidentified here. In particular (8) is not a native
moment lower bound, a refutation of the inherited reduction, or a statement
about RH.

## 7. Bounded verification and limits

The replay authenticates the frozen dense source fixture, Boolean primitive,
kernel, original family, and concurrent canonical-candidate/decoder notes.
It verifies the complete all-rough Boolean rows at depths two and three,
the horizon exclusion of depth four, the exact \(1/3\) surviving owner
share, and the inherited dense physical/class geometry. A second tiny clean
ratio-eight chart has a genuine three-prime cofactor core and all twelve
signed histories summing to zero; its opposite two-prime core has two
positive histories. This checks that complete cofactor cancellation,
rather than an imposed deletion, supplies (5).
It also checks the finite polynomial identity behind (10) exactly in
\(\mathbb Q(\sqrt2)[r]\), without evaluating a Fourier transform.

The positive Fourier mass in (6), the unbounded PNT count and the full
candidate lower bound are proved above, not numerically estimated. The
finite tests do not enumerate the complete growing owner family or
reconstruct native carrier/renewal data. Root runs the bounded computations;
the independent reviewer checks the exact frozen proof and code separately.
