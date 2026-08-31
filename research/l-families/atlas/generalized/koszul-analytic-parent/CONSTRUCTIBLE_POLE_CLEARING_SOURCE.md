# A constructible graded source for the elliptic pole-clearing operation

Use the actual generic S3 cubic cover and its joint quadratic cover from
the coherent place-Euler theorem. Work over F_Q in characteristic p>3,
with a coefficient field of characteristic zero as in the frozen finite
cover construction. Let j:U -> P1 omit the four old finite branch points,
zero and infinity. On U the coherent Segre algebra has finite grades

    A_n = R_n tensor chi^n.

Let S be the actual two-dimensional standard S3 local system, pulled back
to the joint group with its quadratic factor acting trivially. It is also
the nontrivial summand of the actual second Koszul relation module
M_2 = 1 direct-sum S. Thus the extra module below is specified from the
source representation, without fitting a Frobenius polynomial to zeros.

All j_* operations in this note are ORDINARY sheaf pushforwards, taken
separately in each finite grading degree. They are not derived or perverse
intermediate extensions. Tensor and symmetric powers are ordinary sheaf
operations over the coefficient field. Every finite grade is constructible;
the infinite graded collection is not asserted to be one finite-rank
constructible sheaf.

## 1. Define the algebra before taking Euler factors

Form the graded sheaf algebra

    B = (direct-sum_(n>=0) j_* A_n)
                       tensor Sym(j_*S placed in GRADING degree two).

Explicitly its finite degree m is

    B_m = direct-sum_(k=0..floor(m/2))
                  (j_*A_(m-2k)) tensor Sym^k(j_*S).                   (1.1)

The first factor has its inherited multiplication because j_* of an
algebra is an algebra. The second is the ordinary free commutative graded
algebra on the specified sheaf. These operations give multiplication and
the unit before point counts or analytic continuation are considered.

At a closed point v with inertia I_v and residual Frobenius phi_v, ordinary
stalks give

    (B_m)_v = direct-sum_k A_(m-2k)^(I_v)
                                  tensor Sym^k(S^(I_v)).             (1.2)

In particular the new free algebra is formed AFTER extension/invariants.
It is not (A tensor Sym(S in degree two))^(I_v). The distinction is part
of the source definition, not a correction imposed after seeing an Euler
factor. This note does not assert that j_* commutes with tensor or symmetric
powers; Section 3 exhibits its failure concretely.

Let t=z^deg(v). The trace identity for symmetric powers and the Cauchy
product in (1.2) give the full local Hilbert factor

    F_(B,v)(t) = F_(A,v)(t) / det(1-phi_v t^2 | S^(I_v)).             (1.3)

It retains the actual quadratic sign of A and the untwisted standard
summand S. Twisting that extra summand by chi would define a different
operation and would not give the factor below.

## 2. Full ramification and the global source identity

Write D_h(s)=det(1-s h | S) for the three S3 classes. The actual matrices
give

    D_e(s)=(1-s)^2, D_s(s)=1-s^2, D_c(s)=1+s+s^2.

The complete new local factors are therefore:

| Place | Standard stalk and new factor |
| --- | --- |
| Good joint class (h,epsilon) | S is unramified; divide the original F_h(epsilon t) by D_h(t^2). |
| Old finite C2 branch | S^C2 has dimension one and residual Frobenius acts as one; divide the full old coherent branch factor by 1-t^2. |
| New zero branch, inertia the central quadratic C2 | S is trivial on this inertia; divide the full even A factor by D_h(t^2), with its actual old S3 Frobenius h. |
| Infinity, joint inertia C6 projecting to C3 | S^C3=0, so the full coherent infinity factor is unchanged. |

The old C2 residual claim follows from N_S3(C2)=C2: both possible lifts
act trivially on its standard invariant line. The zero and infinity rules
do not replace the already frozen full A-invariant factors by invariants
of its two inputs.

Taking the product of (1.3) over ALL places, initially in a sufficiently
small absolute-convergence disk or coefficientwise as a formal series,
gives

    E_B(z) = E_chi(z) L(P1,j_*S,z^2)
           = E_chi(z) P_E(z^2).                                    (2.1)

The second equality is the actual standard-sector cohomology already
identified in the S3 source: H^0=H^2=0 and its two-dimensional H^1 has
the elliptic polynomial P_E. It includes the old branch and infinity
stalks; it is not an Euler product with ramified places silently omitted.
The extra removed point zero is unramified for S and is restored by the
ordinary j_* stalk above.

Each coefficient involves finitely many effective divisors and finite
grades. All the rational S3 representation characters and quadratic signs
are integral here, so the resulting global coefficients are integers.
The identity is a theorem for the newly defined source B. It does not
identify B with the original algebra A or with j_* of their generic tensor
algebra on U.

## 3. A degree-three ramification counterfeit

At an old finite C2 branch, chi is unramified and does not alter inertia.
The actual first grade A_1 is the regular S3 representation, of dimension
six and transposition trace zero. Hence dim(A_1^C2)=3. The standard module
has transposition eigenvalues 1,-1, so dim(S^C2)=1.

The actual third Segre grade has dimension forty and transposition trace
zero: Sym^3 of the standard module has dimension four and trace zero,
and Sym^3 of the three-dimensional permutation module has dimension ten.
Thus dim(A_3^C2)=20. Formula (1.2) consequently gives

    dim(B_3)_v = 20 + 3*1 = 23.                                    (3.1)

In contrast, forming the generic tensor algebra first and then extending
would give (A_3 direct-sum (A_1 tensor S))^C2 at degree three. The tensor
term has dimension twelve and transposition trace zero, so its invariant
dimension is six. That alternative has dimension

    20 + 6 = 26.                                                   (3.2)

This exact low-grade mismatch authenticates the order of operations. It
does not say that either algebra is ill-defined; they are different
constructible extensions of the same generic algebra. Only (1.1) has the
stalkwise factorization (1.3) and hence the source identity (2.1).

## 4. A sharp two-case analytic effect of the source operation

The frozen arithmetic pole-divisor theorem applies to E_chi. Its first
poles are precisely at the zeros of P_E(z^2), with their multiplicities,
so the new source (2.1) removes
them for every generic S3 parameter. This statement changes the function;
the original coefficients retain their previously proved Q^(1/4) root
growth.

If every eigenvalue of E AND D satisfies alpha^2=Q, the effective fully
resonant theorem proves that those two double poles are the ONLY interior
poles. Thus E_B is holomorphic on the unit disk and has a meromorphic
natural boundary there. Its integer coefficients b_m satisfy

    limsup abs(b_m)^(1/m) = 1.                                     (4.1)

In this case P_E(z^2) is also the unique constant-one polynomial of minimal
degree that clears all interior poles. This does not make B the unique
possible algebra source or regularization.

Otherwise choose an actual elliptic eigenvalue alpha from E or D with
alpha^2 != Q. The fourth Lie grade has B_4=C_4=1. At each solution of
z^4=alpha^(-1), its elliptic denominator therefore contributes a positive
pole order. The only possible same-radius cancellation is the grade-eight
trivial zero, and the exact theorem says that cancellation requires
alpha^2=Q. No local numerator cancels these arithmetic points. The new
factor P_E(z^2) has zeros at the earlier radius Q^(-1/4), so cannot cancel
a grade-four point at radius Q^(-1/8).

There are no intervening poles: grade two was removed, odd coherent
grades supply only polynomial zeros, and every later possible even-grade
pole has larger radius. Consequently, in this nonfully-resonant case,

    radius of the Taylor series of E_B = Q^(-1/8),
    limsup abs(b_m)^(1/m) = Q^(1/8).                                (4.2)

The full function still continues meromorphically to the unit disk with
its natural boundary. Multiplication by a nonzero polynomial cannot
remove that boundary. Equations (4.1)--(4.2) are an exact dichotomy for
this specified source operation, not an improved bound on the original
Euler coefficients or a number-field critical-line statement.

## 5. The same source operation gives a finite even-grade ladder

Fix any even N>=2. For each even n<=N take the actual nontrivial isotypic
summand of the source Lie module,

    T_n = M_n / (its trivial isotypic summand)
        = B_n copies of the sign module plus C_n copies of S.

The finite-group averaging idempotent makes this summand canonical in
characteristic zero. Its proper H^0 and H^2 vanish, while its H^1 numerator
is P_D(T)^(B_n) P_E(T)^(C_n). Form a NEW graded algebra by adjoining the
finite direct sum of j_*T_n, with each T_n in grading degree n, freely to
the already extended j_*A. The same stalkwise calculation as (1.2) gives
its full Euler function

    E_(B,N)(z) = E_chi(z)
          product_(even 2<=n<=N) P_D(z^n)^(B_n) P_E(z^n)^(C_n).      (5.1)

This finite polynomial multiplier removes every possible pole at the
selected grades, even when a particular apparent pole was already canceled
by a principal zero. The only remaining possible coherent pole grades
are even and at least N+2. Therefore

    E_(B,N) is holomorphic on abs(z)<Q^(-1/(2(N+2))).                (5.2)

This is a guaranteed disk, not always the exact Taylor disk: the fully
resonant source already reaches the unit disk when N=2. For every fixed
N the meromorphic continuation still has its natural boundary at abs(z)=1,
since multiplication by a finite nonzero polynomial cannot remove it.

The guaranteed radii approach one as N increases, but these are different
finite-generator constructible graded algebras. There is no assertion of
uniform convergence in N, a convergent infinite product of the added
cohomological factors, or a larger trace-class domain for the original Lie
operator. The finite source construction and its analytically controlled
effect must not be exchanged for an unproved infinite completion.

## 6. Bounded verification and remaining limits

The companion replay uses the authenticated standard/regular source
characters and the previously frozen coherent place factors. It checks
the three standard determinants, every branch-type extra factor, and the
degree-three 23-versus-26 discrepancy. It retains the actual grading
substitution t=z^deg(v), with the new generator in degree two.

Low-grade order checks cover resonant and nonresonant elliptic points.
The established F7-to-F49 example supplies the fully resonant case without
enumerating another field; the existing nonsquare-field sources provide
the complementary case. The all-grade sheaf construction, global Euler
identity and analytic dichotomy are proved above, not inferred from a
finite factor table.

The operation deliberately chooses an ordinary constructible extension.
It supplies no universal tensor-commutation theorem, automatic perverse
or derived realization, archimedean gamma factor, native retained-gamma
decoder or RH consequence. The symmetric algebra is an actual source
construction, while convergence of an infinite operator or cohomology of
one infinite-rank sheaf would require its own additional definition.
