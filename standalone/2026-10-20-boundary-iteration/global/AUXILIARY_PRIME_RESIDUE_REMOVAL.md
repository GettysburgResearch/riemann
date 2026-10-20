# A fixed auxiliary prime removes the spherical residue from the probe

Status: proposed exact arithmetic/analytic adapter for the Eisenstein
physical probe; independently reviewable without accepting a new global
zero-free bound.

Dependencies: the pinned Ope26a source, specifically its Sections
“The base probe and its balanced low estimate”, “The scalar Euler
identity”, and “The compensated probe”; and the spherical-reflection
theorem proved in this directory. The source theorem is not being
applied outside its finite-order scope: the changed theta input is
proved here and the high coefficient identity is checked in unitary
phases.

## 1. The freedom in the source auxiliary data

Write \(T\) for Ope26a's fixed finite ray group carrying only the
supplementary and Gauss phases. It is chosen independently of the target.
For a target \(\eta=\alpha^m\eta_0N^{it}\), with \(\eta_0\) finite order,
absorb the fixed norm phase into the radial profile.

Choose a primary prime \(p_*\) outside the conductor of \(\eta_0\),
outside the modulus of \(T\), and outside the previously required
excluded set. Choose it in the identity ray class of \(T\). Existence
uses the same fixed-ray prime theorem as the source, before the scale
tends to infinity.

Add \(p_*\) to the fixed set \(S\). Let \(b_*\) be the primary generator
of the squarefree product of all primes in \(S\).
The source permits any primitive residue character \(\xi\) modulo
\(b_*\), with every local component nonprincipal and of order dividing
six. At the new prime choose specifically
\[
 \xi_{p_*}=\chi_{p_*}^{\,2}.                            \tag{1.1}
\]
This is a primitive cubic character of the finite residue field.
Every other component may be chosen as in the source.
Chinese remaindering gives a valid primitive \(\xi\), and its normalized
Gauss sum \(\tau\) has modulus one.

Exact source locators are lines 3331–3378 in Ope26a's immutable TeX
file at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a:
the paragraph before the definition of \(b_*\) explicitly permits
enlarging \(S\) without changing \(T\), and the following paragraph
permits every nonprincipal local character of order dividing six.

This is a fixed choice of data already permitted by the physical
construction. It is not a new moving prime slot or a new target twist.

## 2. The resulting theta character has forbidden digit three

The source defines
\[
 \Xi(a)=\xi(a)\chi_a(b_*),\qquad
 \Psi_{m_{\rm row},s,\eta}(a)=
       \eta(a)\Xi(a)^{-1}\mathcal R(a,s)\chi_a(m_{\rm row})
 \tag{2.1}
\]
on ideals prime to \(S\). Its corrected completed theta row has
coefficient \(\gamma_2(c)\bar\alpha(cb^3)
\Psi_{m_{\rm row},s,\eta}(cb^3)\bar G(cb^3)\).

Separate \(b_*=p_*b_0\). Sextic reciprocity gives
\(\chi_a(p_*)=\mathcal R(a,p_*)\chi_{p_*}(a)\).
Since \(p_*\in1_T\), the fixed bicharacter factor is one. Hence the
local \(p_*\) part of \(\Xi\) is
\[
 \chi_{p_*}^{2}\chi_{p_*}=\chi_{p_*}^{3},
 \qquad \Xi^{-1}\text{ has the same digit }3.           \tag{2.2}
\]
The target's finite component and every character in \(\widehat T\)
are unramified at \(p_*\).

The physical average multiplies the row by \(\xi(m_{\rm row})\);
therefore every surviving row is a \(p_*\)-unit. Reciprocity converts
\(\chi_a(m_{\rm row})\) to the usual moving-prime digit masks away from
\(p_*\), with only fixed \(T\)-phases. Likewise
\(\mathcal R(a,s)\) and the finite Fourier components of \(\bar G(a)\)
have conductor in the modulus of \(T\). They cannot change the
\(p_*\) digit.

Consequently every completed theta row in the physical low-side
separation carries the single local factor \(\chi_{p_*}^3\).
To apply the companion theorem formally, put \(p_*\) among its local
prime masks and choose its fixed \(L\) using all other fixed data.
The full zero at \(p_*\) is exactly the zero of \(\chi_{p_*}^3\).

If the theta angular degree \(m-1\) is nonzero, the pure derivative
already removes all cusp constants. If \(m=1\), the row is spherical,
but Theorem 1 of EISENSTEIN_SPHERICAL_REFLECTION.md permits only digits
\(0,4\) for a nonzero residue. Digit \(3\) therefore makes its residue
zero. It also excludes the conjugate support \(\{0,2\}\).
Thus **every physical completed row is residue-free**, for every
unitary target \(\eta\), every row, and every fixed sector.

## 3. All compensated terms preserve the same zero

The source's compensated operation at a selected prime \(q\notin S\)
is
\[
 \overline{\eta(q)}I_{\eta;q}(X,Y,Zq)
             -q_q^{-3/2}I_\eta(X/q_q,Y/q_q,Z).          \tag{3.1}
\]
Every selected prime is distinct from \(p_*\).
A divisibility mark on the full index multiplies the residue by
\(1/q_q\), while a rescaling changes only the radial profile and norm
length. Neither operation alters digit \(3\) at \(p_*\).
Thus the residue vanishes separately in every term of the finite
compensated expression, before any positive norm estimate.

All nonconstant reflected terms are exactly the original local
\(B_p\) transforms with the spherical gamma quotient or its higher
angular counterpart. Their small-argument power \(1/4\), fixed finite
seminorm bounds, and separated unitary row/column factors are proved
in the companion reflection notes. The fixed prime can be absorbed
in the finite data of the ensuing estimates, since it was chosen
before \(Z\). The existing additive Gram and hybrid sieve comparisons
therefore keep their norm exponents.

## 4. The high scalar signal is unchanged by this choice

This must be checked in the exact physical identity, rather than by
informally discarding an auxiliary character.

Ope26a's local scalar computation at the primes of \(b_*\) gives
\[
  \sqrt{q_{b_*}}\tau\,\xi(A)\overline{\xi(H/s)}.
 \tag{4.1}
\]
With \(H=ua^6\) and \(\xi^6=1\),
\(\overline{\xi(H/s)}=\overline{\xi(u)}\xi(s)\).
These factors cancel the corresponding displayed \(\xi\) factors
in eq:local-full-coefficient. The remaining fixed-numerator factors
cancel \(\chi_s(b_*)\chi_A(b_*)^{-1}\).
This is exactly the coefficientwise cancellation in the pinned
source's paragraph “The finite scalar and its unit factors”.
It applies to the cubic choice (1.1).
The exact cancellation and unchanged-\(T\) statement occur at source
lines 3941–3951. Lines 16336–16341 also permit additional fixed
target-dependent excluded primes after the pretarget slot windows
have been chosen.

The outside frequency phase \(\overline{\xi(u)}\) has modulus one.
At the principal row \(u=1\) it is one. Hence the principal factor
remains the reciprocal of the original target \(L_E^S(s,\eta)\),
with the same unitary Euler correction \(H_\eta(s)\).
No residual twist by \(\chi_{p_*}^3\) survives in that target.

Enlarging \(S\) deletes finitely many Euler factors. Its scalar
\[
 c_S=\widehat W_1(1)M(1/6)
        \bigl(\operatorname{Res}_{v=1}\zeta_E^S(v)\bigr)^2/6
 \tag{4.2}
\]
is still strictly positive. The compensated prime normalizer is the
same target-free identity-ray sum; excluding one more fixed prime
does not alter its eventual nonzero asymptotic. The source explicitly
permits fixed enlargements of \(S\) without changing \(T\).

Every local high-side identity is polynomial in the target values
\(\eta(p)\), and its absolute estimates use \(|\eta(p)|=1\).
The special auxiliary choice therefore removes a low-side theta
residue while retaining the high-side reciprocal signal of the
original unitary target.

## 5. What this resolves

The previously identified direct-comparison residue obstruction over
\(E\) is removed by an allowed choice of fixed auxiliary data.
Together with EISENSTEIN_UNITARY_INVERSE.md, this supplies both
resonant theta interfaces needed for a refined-boundary bootstrap.

EISENSTEIN_REFINED_BOUNDARY.md assembles the ordinary product moment
for the enlarged angular family with native Eisenstein refined
numerator estimates and field-independent scalar inequalities.
It gives a proposed extension of \(B_\flat\) to every unitary Hecke
character of E, including the formerly missing resonant types.
The numerical boundary is unchanged. No theorem whose stated
hypothesis is \(F\supset\mu_{12}\) is applied directly with \(F=E\).
