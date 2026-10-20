# Independent review of the opposite-cubic joint mean

20 October 2026. Reviewed file:
../mixed/OPPOSITE_CUBIC_JOINT_MEAN.md,
SHA256 c97a23c55c79a95b6a61080805617a87396285cbd6738b822cd80728efec92aa.

**Verdict: the stated extension and free-column consumer pass this
review, conditional on their explicitly imported source inputs.**
The finite cusp theorem and divisor identity are previously audited
inputs here; this receipt does not certify the entire upstream
preprints or turn the numerical comparisons into a priority claim.

## Local reflection and the complete scalar family

At a good prime dividing \(S\), write \(\chi\) for the primitive cubic
character. The first primitive Fourier transform contributes
\(\tau(\chi)\overline\chi(d)\). Substitution
\(d=(\lambda^8a)^{-1}\) changes the variable factor to \(\chi(a)\),
up to a unit independent of \(a\). The Kubota multiplier supplies
another \(\chi(a)\), so the second transform is
\(\tau(\chi^2)\overline{\chi^2}(u)=\tau(\overline\chi)\chi(u)\).
This verifies the exact orientation in (OC6): the positive cubic
character is self-reflected.

The two Gauss factors obey
\(\tau(\chi)\tau(\overline\chi)=\chi(-1)q=q\), since a cubic
character is trivial at \(-1\). CRT changes this by unit factors
only. Nonunit Fourier inputs vanish, so the original \(S\)-coprimality
mask remains. At the disjoint negative cubic conductor \(r\), the
Kubota cancellation still leaves the full signed Ramanujan sum.
The combined modulus magnitude is therefore
\((Nr)^{1/2-2\Re s}(NS)^{1-2\Re s}\), as used in (OC7).

The additional coefficient character \(\chi_S\) is cubic.
Consequently its cube power is exactly one on units, with zeros
still present at \(S\). This gives (OC2), not a quadratic-twisted
cube factor. In the divisor identity the multiplicative coefficient
is \(\kappa\chi_S\); it has cube one and keeps the same finite
ramified profile. New negative rows are \(k\mid r\), so
\((k,S)=1\) remains true.

At the prime above 3, \(\chi_S(\omega)\) merely shifts the integer
phase index of the exact three-cusp extraction minor.
\(\chi_S(\lambda)^3=1\) preserves the full geometric cube tail.
The finite reflection matrix at modulus \(rS\) is of the same
previously audited type; the unit lifts in the prime-to-3 modulus
are independent of the finite Fourier variable after its common
multiplier is accounted for. There is no claim of literal
four-dimensional coefficient-space invariance.
Both signs of the nonzero angular order are included, and every
cusp constant vanishes. These checks license the whole scalar
family in the norm inequality, including the full cube completion.

## The joint operator, absorption, and heights

I checked de Faveri's primary source
[arXiv:2610.04045v1, Proposition 8.1](https://arxiv.org/html/2610.04045v1#S8),
whose squarefree column kernel is \(\chi_c(ab^2)\) with arbitrary
complex column coefficients. Cubic reciprocity, after fixed finite
ray partitions, identifies the present kernel with \(a=S,b=r\).
The source permits all ideal rows, so squarefree and common-prime
row restrictions are legitimate restrictions of its positive sum.
The column Gauss, angular, norm and finite-profile factors remain
independent of the rows after the partition.

The three original terms in (OC9), their positive column powers,
and the cube exponents \(-1-3\delta,-5/2,-2\) all check.
No arbitrary multiplier is inserted into the complete cube factor.
The \(S\)-character of a cube is one, subject to its retained zero
mask, and Minkowski uses the complete convergent cube sum.

Squaring the exact reflection and summing multiples of \(k\)
gives (OC11), including the factor \(R^{4\delta}\) before partial
summation. All six piecewise \(R\)-powers listed in the draft
are correct. They exceed \(2\delta\) on the stated range
\(0<\delta<2/9\), and the monomials match continuously at \(R=H\).
This gives \(R^{-2\delta}F_\delta(R,H)\), hence precisely
\(Y^{-4\delta}R^{2\delta+\eta}H^{4\delta}L^{8\delta}\).
The proposed cutoff cancels these powers and contracts after
choosing fixed constants and allocating the small losses.

The finite row, positive-conductor and angular cutoffs all close:
reflection decreases \(r\), fixes \(S\), and reverses an included
angular sign. The preliminary right absolute line and reflected
left line give a conductor-polynomial bound with angular/height
degree \(2+4\eta\). Gaussian three-lines gives component degree
\(1-2\delta+2\eta\), below the final squared normalization when
\(\eta\) is sufficiently small. Thus the height supremum is finite
before absorption. No a priori global bound equal to the desired
conclusion is assumed. The paired fixed-shift gamma ratios also
cover both \(|t|\gg|\ell|\) and \(|\ell|\gg|t|\).

## Consumer and comparison

For the actual sum (OC14), Gauss multiplicativity yields
\(\widetilde g(r)\alpha(r)^\ell\chi_S(r)\) times the incomplete
series with column character
\(\overline{\chi_r(u)}\chi_S(u)\). These outer factors have
modulus one under the stated masks. The column is free and
smooth, so Mellin inversion is legitimate.
The ordinary Hecke factor in the cube completion is inverted
by an absolutely convergent Euler product on
\(\Re s=1/2+\delta\); Cauchy over the \(RH\) outer rows proves
(OC15), with the stated uniform angular exponent.

At \(A=R=H=N\), \(F_\delta\asymp N^2+N^{5/2-3\delta}\).
Choosing \(\delta=1/6\) gives \(N^{8/3+\epsilon}\), and this
choice is strictly inside the permitted interval.
Letting \(\delta\) tend to zero instead gives \(N^{11/4+\epsilon}\),
or \(X^{11/12+\epsilon}\) for \(X=N^3\).
No prime restriction or arbitrary arithmetic coefficient in the
free column is licensed.

The comparison with the separately averaged cubic sieve has the
stated meaning only on its indicated range \(0<\delta<1/6\).
The supplied recursive source has a different positive row:
representing this cubic character uses its sextic index \(z=S^2\).
With \(K=H^2\) and powerful part \(J=H^2\), its displayed
fixed-label completed bound becomes \(H+H^3R/D\), hence
\(RH+R^2H^3/D\) after undoing the label average.
At balance the crossing with the joint original operator occurs
at \(D=N^2\), with weighted peak \(N^{3-4\delta}\).
This does not recover (OC5) on the stated interval.
This is a check of that supplied interface, not an exhaustive
literature comparison.

The boundary-determining physical terminal has a different
quadratic/sextic character and a marked column. It cannot be
identified with this positive cubic conductor family. Accordingly
the scope paragraph excluding a new numerical zero-free bound
is necessary and correct.

## Optional range observation, not a defect in the reviewed theorem

The third term of \(F_\delta\) is globally dominated. For \(R\le H\),
its ratio to the second term is \(R^{-1/2}\le1\); for \(R\ge H\),
its ratio to \(RH\) is \(R^{-\delta}H^{-2\delta}\le1\).
One may therefore normalize instead with \(RH\) plus the second
term only. Its nontrivial \(R\)-powers are \(7/6-\delta\) and
\(5/6-\delta\), so the partial-summation condition holds at least
throughout \(0<\delta<1/4\).
The already audited gamma argument covers that range.
The author has retained the narrower reviewed theorem to avoid
changing its frozen scope; its optimal balanced consumer
\(\delta=1/6\) is unaffected.
