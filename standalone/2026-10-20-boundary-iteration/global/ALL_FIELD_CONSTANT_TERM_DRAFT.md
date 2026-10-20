# All-field spherical constant term: an audit draft

Status: **not yet a proved input**. This draft records a proposed way to
close the all-field residue interface. The rational torus transport and
the fixed puncture convention require independent source-level review.
No conclusion elsewhere in this packet may use this draft as a theorem.

Source: Baiying Liu, [arXiv:2610.26835v1](https://arxiv.org/html/2610.26835v1),
Proposition 4.1 and Lemma 5.1, especially (5.3), (5.7), (5.8), and the
absolute convergence estimates in the proof of Lemma 5.1. The source
is pinned in the preceding packet. The proposed addition concerns its
missing spherical archimedean case, not its nonconstant Fourier tables.

## 1. The two weighted constant terms

Retain the source's actual automorphic theta representation and its
ordinary torus sections. At each complex place use the spherical vector
with Whittaker function

\[
 x^{1/2}K_{1/3}(c_v\sqrt{x}),\qquad x=|y_v|_v.
\]

The finite coefficient character and finite local test family are fixed.
Let \(C_m^+(l)\) and \(C_m^-(l)\) be the weighted constant terms of the
two digit-averaged automorphic functions in source Lemma 5.1, integrated
over the same compact norm sheet modulo sixth powers of S-units.
Rational automorphy, before any Mellin transform, gives

\[
 T_m(l)=T_m^\vee(l)+C_m^-(l)-C_m^+(l).                 \tag{1.1}
\]

Here the two \(T\)'s are the actual nonconstant Fourier sums; no
constant term is included in either one. The unchanged absolute local
Whittaker product in the source gives, for every \(\sigma>1/2\),

\[
 T_m(l)=O_{m,\sigma}(l^{-\sigma}),\qquad
 T_m^\vee(l)=O_{m,\sigma}(l^{\sigma}).                 \tag{1.2}
\]

The constants in (1.2) need not be uniform in the moving row. These
bounds are used only to exclude an impossible exponent for each fixed
row. Uniform row bounds must instead come from the finite local formula.

## 2. Compact norm-one averaging

At each complex place the constant-term Jacquet characters have real
powers \(1/3\) and \(2/3\), as stated in the source proof. Tensoring
them gives a finite translation span. If necessary, allow generalized
eigencharacters and finite powers of logarithms at this stage.

The weighted sheet integral annihilates every component whose restricted
real character on the positive archimedean norm-one torus is nontrivial.
Indeed, spectral projections onto distinct generalized characters are
polynomials in one separating translation operator. They preserve
S-unit invariance. Haar invariance then gives
\((1-\lambda)^N\int f=0\) for a component with translation eigenvalue
\(\lambda\ne1\). Only the components with the same exponent at every
complex place can survive.

Consequently the integrated constant terms have the forms

\[
 C_m^+(l)=l^{1/3}P_{m,+,1}(\log l)
             +l^{2/3}P_{m,+,2}(\log l),
\]
\[
 C_m^-(l)=l^{-1/3}P_{m,-,1}(\log l)
             +l^{-2/3}P_{m,-,2}(\log l),              \tag{2.1}
\]

with polynomial degrees bounded by the fixed representation and profile
family. This statement must include the finite sheet-class cutoffs:
they are invariant under the positive archimedean norm-one torus.

Take \(1/2<\sigma<2/3\) in (1.2). In (1.1), as \(l\to0\), a nonzero
\(l^{-2/3}\) polynomial cannot be canceled by any other displayed term.
Thus \(P_{m,-,2}=0\). The same argument as \(l\to\infty\) gives
\(P_{m,+,2}=0\). This excludes the second exponent without asserting
that it is absent from the local Jacquet module.

## 3. A fixed puncture removes the direct constant term

Choose one fixed good prime \(p_0\) outside a base set \(S_0\) for the
theta construction and retain \(1_{p_0\nmid A}\) as an explicit prime
mask on the full completed theta index. All other fixed conductors and
the principalization primes may lie in \(S_0\). Omitting this extra Euler
factor from the target Hecke function does not affect zeros in
\(\Re s>0\).

For every digit \(j\), including \(j=0\), the exact source coefficients
satisfy

\[
 \sum_{z\bmod p}\alpha_{p,j}(z)=\chi_p(0)^j=0.        \tag{3.1}
\]

The notation on the right means the source's zero extension, so its
value is zero also at exponent zero. At an exterior prime the direct
constant term is unchanged by the translation \(n(z/p)\). Therefore
the retained puncture makes \(C_m^+(l)=0\), including rows with no
other prime factors. If the row has a power of \(p_0\), its digit merely
changes \(j\); (3.1) still holds.

The point needing a full audit is that this prime must remain an
explicit exterior mask in the theta calculation even if the analytic
ideal sums are described as exterior to \(S_0\cup\{p_0\}\). The source
finite mask and priority-assignment machinery should permit this
convention; it must be checked through both Poisson transformations.
It is not enough to absorb \(p_0\) into an unspecified finite profile.

## 4. Moving-prime residue support and size

For an active local digit use the exact lifted identity (5.7):

\[
 wn(z/p)=(z/p)I\,n(-p/z)a(p^2z^{-2})\bar n(p/z).
\]

The central scalar is trivial in the source quotient, the left
unipotent has no effect on a constant term, and the final compact
factor fixes the good spherical vector. The ordinary torus section and
spherical unit invariance give the same unit phase as in (5.8), namely
\(\chi_p(z)^4\). Thus the active constant-term digit sum is

\[
 \sum_{z\ne0}\alpha_{p,j}(z)\chi_p(z)^4
 =\begin{cases}
   (q_p-1)/\tau_{p,4},&j=4,\\
   0,&j\ne4.
  \end{cases}                                          \tag{4.1}
\]

Its nonzero magnitude is \(q_p^{1/2}(1-q_p^{-1})\).
For digit zero the active branch vanishes and the inactive coefficient
is \(1-q_p^{-1}\).

Let \(r\) be the product of active primes. Move the diagonal
\(a(r^2)\) from the exterior places to \(S_0\) using rational torus
invariance of the automorphic constant term. The remaining unit phases
have modulus one. The weighted sheet is now at norm
\((lq_r^2)^{-1}\), with one of finitely many shifted local power-class
weights. Its surviving exponent \(1/3\) gives \(q_r^{-2/3}\).
Combining with (4.1) therefore gives

\[
 |\mathfrak r_m|\ll q_r^{-1/6}
             \prod_{p\mid m}(1-q_p^{-1})(q_m)^\epsilon,
 \qquad j_p\in\{0,4\};                              \tag{4.2}
\]

and zero otherwise. A bounded power of \(\log q_r\), if present, is
absorbed in the declared epsilon loss. Whole conjugation replaces
digit four by digit two.

The torus transport must be checked with the actual class weight and
the actual ordinary-section cocycle; (4.2) is presently a proposed
deduction, not an established substitute for that calculation.

## 5. Marks and the intended analytic consequence

At a fresh good prime a full-index coprimality mask has digit zero, so
only its inactive branch contributes to the residue. Its factor is
\(1-q_p^{-1}\). Subtracting this mask from the unrestricted index gives
the full-index divisibility factor \(q_p^{-1}\). This is precisely the
mark law required by RESIDUE_INDUCTION_INTERFACE.md.

Once (1.1)--(4.2), the retained-puncture convention, and the uniform
finite-profile transport are verified, Mellin subtraction gives the
same reflected compact-test kernels as in the existing angular packet,
plus finitely many terms of size
\(X^{1/3}(1+|\log X|)^J\mathfrak r_m\). The weighted-row lemma then
puts these terms below the canonical inverse target by its existing
strict margin. The fixed logarithms are absorbed by that margin.

This would remove the all-field resonant exception in the inverse
moment. An additional auxiliary-prime cancellation in the direct
comparison would still be needed for the sharp boundary. Neither
completion would lower the numerical value of \(B_{\flat}\).
