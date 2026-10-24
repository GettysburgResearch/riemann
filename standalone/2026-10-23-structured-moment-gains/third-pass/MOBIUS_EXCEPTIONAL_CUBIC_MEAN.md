# Möbius coefficients in the two exceptional cubic character means

24 October 2026. Status: proposed source-dependent adapter, with the exact
review binding recorded separately. This extends the coefficient class of a specified estimate; it does
not prove a new global zero-free boundary. The size of its positive saving is
not quantified below.

## 1. Exact source and claim

The imported argument is `openai/math` at
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/build/sections/dual.tex`,
Proposition `prop:dual`, its full-sum duality lemma and off-diagonal Gram lemma.
The source file has SHA256
`1209fd17cee79f4a21b71d66d3d8b60b210216fa783ec555959d2ebff2fba483`.
The associated dispersion source has SHA256
`9a04b892feb99a79ec4e825bcd5096d3adb994c53d539c41d2da35f0a77f317c`.
For fixed angular twists the additional input is
`sections/angular.tex`, Proposition `prop:angular-dual` and its proved
full-sum duality extension. The exact source file has SHA256
`f14a7c1c4f0b19b70d6705c8a2adcb658bfbc77814edb61cd57edb2465f38510`.

Use the source's primary-ideal conventions in the Eisenstein field, and its
cubic symbol extended by zero. Fix a smooth annular function W. Put

\[
 A(p,q)=\sum_{(b,e)=1}\mu(b)\Theta_\ell(b)\nu(b)
 W(Nb/Y)(Nb)^{iu}\chi_b(vpq^2).
\tag{1}
\]

Then the conclusion of `prop:dual` remains valid for (1): there are fixed
delta, eta > 0, depending on the test class, such that

\[
 \sum_{p,q}|A(p,q)|^2\ll Y^{7/3-\eta},
\tag{2}
\]

when p,q are coprime squarefree primary ideals, their norm exponents lie in
delta-neighborhoods of (1,0) or (1/3,1/3), Nv,Ne <= Y^delta, and
1+|u| <= Y^.36. Here ell is any fixed integer, Theta_ell is the source's
Hecke angular character on primary generators, and nu is a fixed ray
character. The constants may depend on ell and nu. Both belong to the
primitive Hecke character used in the full-sum duality lemma.

Unlike the printed prime-convolution theorem, (2) permits small prime
factors of b. It is a mean of ordinary cubic character sums with Möbius
coefficients, not yet a residual-subtracted Gauss-sum mean.

## 2. An exact short identity for Möbius

Let Y0 be a fixed constant times Y larger than every norm in the support
of W(Nb/Y), and put m = mu * 1_{N <= sqrt(Y0)}, where this star denotes
pointwise multiplication only in this definition. Write convolution as
`*_D` below, and let delta_1 be its identity. The function

\[
 E=\delta_1-m*_D1
\]

vanishes on every ideal of norm at most sqrt(Y0). Consequently E*_D E
vanishes on every ideal of norm at most Y0: every nonzero summand would
have both factors of norm greater than sqrt(Y0). Convolution by mu and
the identity mu*_D1=delta_1 give, on that range,

\[
 \mu=2m-m*_Dm*_D1.
\tag{3}
\]

This is an exact finite identity; no estimate for Möbius cancellation is
used. On the annular range Nb asymptotic to Y the 2m term is absent for
large Y, although retaining it does not change the argument.

Every complete multiplicative character, its zero extension, the
restriction (b,e)=1 and the norm twist distribute across (3). The smooth
weight W(Nb/Y) becomes a smooth weight in the product of three norms.
Insert smooth dyadic partitions for the factors and use Mellin inversion
of this one common product weight. The resulting polynomials have
coefficients bounded by divisor powers and at most three factors. Their
length exponents satisfy

\[
 a_1,a_2\le\tfrac12+o(1),\qquad a_3\ge0,
 \qquad a_1+a_2+a_3=1+o(1).
\tag{4}
\]

The first two factors have truncated Möbius coefficients. The third is a
full smooth ideal sum. Hard truncations of the first two factors are
allowed: subsequent sieves accept arbitrary divisor-bounded coefficients.
Their original dyadic smooth cutoffs are independent of the character
row. The common Mellin shifts can be truncated at Y^epsilon; the omitted
tails are negligible and the common L1 mass is subpower. Minkowski thus
reduces (2) to one such product exactly as in the source.

## 3. Why the rest of the source proof applies

In the source's proof the prime-convolution hypotheses are used only to
reach a bounded product of polynomials with the two properties in (4):
all Möbius factors have length at most Y^(1/2+o(1)), and a factor of full
length Y^(1+o(1)) is a full smooth ideal sum. Formula (3) supplies those
properties directly. There is no prime-power replacement error here.

If one factor has limiting exponent one, it must be the full smooth
factor. In the two exceptional configurations the variable primitive
cubic conductor has positive-power norm, even after fixing the
subpower conductor factors at ve. Hence the character is nonprincipal.
The source's full-sum functional equation shortens that factor; its
conductor-dependent root number is outside the dual polynomial. The
source obtains moments at most Y^(2.16+o(1)) in the (1,0) configuration,
and Y^(2/3+2(1/3+.37)+o(1)) in the other configuration. Both are strictly
below Y^(7/3).

Otherwise every factor exponent is less than one. The rest of the
argument uses only divisor-bounded coefficient products, not primality:

* At (1/3,1/3), the ordinary sieve applied to the square of the product
  forces value exponent 5/6 on Y^(2/3+o(1)) rows if no saving holds.
  Repeating a proper factor produces a strict contradiction.
* At (1,0), the unrestricted-inner cubic sieve applied after repeating
  or omitting factors forces every value exponent v_i to equal 5a_i/6,
  with row exponent 2/3. A positive short factor exists; repeated copies
  have length exponent z strictly between 4/3 and 2.
* The source's off-diagonal Gram estimate for that copied polynomial
  gives positive gaps (2-z)/3 and either (3z-4)/6 or (z-1)/6. Thus its
  alleged Y^(2/3) large-value set is impossible.

All copied polynomial coefficients remain bounded by fixed divisor
powers. The number of repetitions is fixed after the limiting exponents
are chosen, just as in the source. Its compactness/diagonal-sequence
argument supplies fixed neighborhoods and a fixed positive eta for the
bounded three-factor class (4). This proves the adapter (2), conditional
only on the source estimates being accepted in their stated scope.

## 4. Requirements for a Gauss-sum mean

The source's residual subtraction is stated for rough coefficients; it
throws away common divisors and cube-lattice coprimality at logarithmic
cost. That step cannot be copied unchanged for mu. Small-prime local
factors must be retained, and the true cube contribution must be bounded
or subtracted. The companion [full-moment proof](FULL_MOBIUS_CUBIC_MOMENT.md)
meets these requirements under its explicit zero-free hypothesis. The
[quantitative appendix](QUANTIFIED_MOBIUS_EXCEPTIONAL_MEAN.md) specifies a
saving for (2). Neither companion supplies the consumer needed for a
smaller global zero-free boundary.

There is a useful extension independent of (2): in the dispersion proof,
the prime-convolution hypothesis is invoked only when the limiting
length is B=X^(1/2+o(1)). For every fixed kappa>0 the large-conductor
frequency argument already works for arbitrary divisor-bounded
coefficients throughout B<=X^(1/2-kappa). Small-conductor cancellation
and the cube correction remain separate requirements.

## 5. Fixed angular twists, including the physical order -2

The source's Proposition `prop:angular-dual` proves precisely the needed
full-sum duality extension: the primitive character inducing the cubic
row times Theta_ell has dual length at most
Y^epsilon times conductor times (1+|t|)^2 divided by the full-sum length.
On the symmetry line its gamma quotient and root-number factor have
modulus one. The dual angular coefficient Theta_{-ell} is common to
every row, with a common smooth dyadic cutoff and common Mellin majorant.

Apply the multiplicative twist T(f)(n)=Theta_ell(n)nu(n)f(n) to (3).
It commutes with Dirichlet convolution. If factors are repeated, their
product still has angular coefficient Theta_ell of its product argument;
the angular order is not multiplied by the number of factors. The row
Gram matrix is unchanged since the fixed angular multiplier belongs to
the common coefficient vector. Thus every step above remains valid.
This covers ell=-2, the actual fixed angular factor encountered in the
attempted sextic-current reflection of a cubic inverse moment.

The fixed nu only changes the fixed conductor part in this argument.
Nonprincipality for ell=0 is forced by the surviving positive-power
cubic conductor, whose primes cannot all lie in the fixed or subpower
exceptional set. For ell nonzero it also follows from the infinity type.
Missing Euler factors are restored before the primitive equation, and
their exact values above 3 are retained as in the source proof.

No frozen repository statement has been edited. No smaller value of
B_flat follows from this note alone.
