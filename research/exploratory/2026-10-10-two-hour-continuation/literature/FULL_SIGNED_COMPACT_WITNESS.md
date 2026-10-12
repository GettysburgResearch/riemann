# The entire native signed R2 under Fourier-compact smoothing

Status: finite, literal source experiment. No asymptotic moment estimate,
zero-free improvement or RH claim is made.

This supplements the independently reviewed
`FOURIER_COMPACT_BALANCED_TRACE.md`; its source normalization and positive
radial disk-square test are unchanged. D=30, H=40, and W is a fixed smooth
norm profile whose only nonzero integer-norm samples are 1 at norms
7,13,19,31. The fixed coefficient character nu is trivial. Thus the actual
source inverse family has exactly the eight prime-ideal columns already
used in the old 1176/456 witness. The Mobius coefficient of every column
is -1. We retain all ordered Hermitian four-column tuples, including
repetitions, rather than only the four-distinct-prime subface.

## C1. Exact critical partition

For each prime p, let r_p and s_p be its number of left and right
occurrences. Put e_p=r_p-s_p modulo 6. Let g1 be the product of primes
with r_p+s_p=1 and g2 the product of primes with r_p+s_p=2 and e_p!=0.
The literal PR914 critical criterion is

    g1 != 1 and Ng1 sqrt(Ng2)>H.

The checker uses the exact equivalent integer inequality
`Ng1^2 Ng2>1600`. It enumerates all 4096 tuples and places 3696 in this
critical sector. Its 120 product-column diagonals are all outside that
sector. Characters are grouped only after this exact partition; tuples
with identical residual characters but different multiplicities are
still counted with their correct sector multiplicity.

The primitive residual modulus q is the product of primes with e_p!=0.
The additional squarefree principal mask r is the product of occurring
primes with e_p=0. They are coprime. The literal tuple character is

    chi(u) 1_((u,r)=1),
    chi(u)=product_(p|q) chi_p(u)^(e_p).

In the critical sector q is nontrivial, and every local character at q
is nonprincipal. Cubic and quadratic local powers are retained exactly.
The value at a nonunit is zero even when an occurring exponent is a
positive multiple of six. No mask is erased by reduction modulo six.

## C2. Principal-mask Poisson formula

With the source test Phi and its compact Fourier transform Psi, the exact
row trace of this character is

    H gamma(chi)/sqrt(Nq)
      sum_(d|r) mu_K(d) chi(d)/Nd
        sum_(h!=0) conjugate(chi(h)) Psi(H Nh/(Nd Nq)).       (C1)

This follows by Mobius inversion of the principal mask, then substituting
u=dv and applying primitive Poisson at row scale H/Nd. The factor chi(d),
the factor 1/Nd and the changed Fourier support are all necessary.
The primitive zero-frequency term vanishes. This is the actual signed
kernel, not an upper envelope.

The normalized gamma is independently built from all five nonprincipal
sextic powers over the eight actual prime residue fields. CRT multiplies
each local gamma by chi_p(q/pi)^(e_p). Local quadratic and cubic Gauss
sums are therefore included, with no arbitrary replacement phase.

The source Phi is radial. The exact six-unit orbit projector kills a
group unless sum_p e_p(Np-1)/6=0 modulo 6. The checker enumerates 1092
different critical character/mask groups. Exactly 178 are neutral and
914 are killed; 568 ordered critical tuples lie in the neutral groups.
Every included dual lattice norm and every divisor of the principal mask
is retained. The complete source leading subface is reconstructed again
through this generic formula, independently of its balanced-polynomial
implementation in the earlier checker.

## C3. What the computation establishes

`check_full_signed_compact.py` sums C1 for every critical group with its
exact ordered multiplicity and separately records the leading subface
and the remaining critical contribution. The directed balls in its
receipt give the full native signed R2 for this positive radial
Fourier-compact test:

* full critical R2: 8852.5068916015827910965314252477411701769971627151;
* fully distinct leading face: 3916.7665189976260644009926745000130837431873375545;
* other critical faces: 4935.7403726039567266955387507477280864338098251606.

The full value is strictly between 8852 and 8853. Dropping the principal
masks would give 9251.8567576912013130298491628310946723335907643494.
Removing the principal masks changes the result;
the checker requires that difference to exceed one.

This full-sector experiment is a new window, so its value is not the old
sharp spatial-cutoff value 1176. Its leading value agrees with the new
independent value in (3916,3917). These finite values neither prove nor
disprove the source's asymptotic generalized moment estimate.

The same positive test can be replaced by a genuine smooth Schwartz
source test, using the explicitly paid compact Fourier mollification
in the companion document. For the whole critical sum, a coarser direct
bound pays this too: each critical tuple has at most two mask divisors,
the primitive norm is at least 7, and every combined mask/conductor norm
is at most (31*19)^2=346921. For delta=10^-12, the compact Fourier test
changes by at most 90delta. The complete norm box has at most
`16*346921/160<34693` points. Consequently the entire critical sum changes
in absolute value by less than

    3696 * 2 * (40/sqrt(7)) * 34693 * 90delta < .35.        (C2)

The identical odd-norm support gap ensures no new Fourier norm is added.
The actual mask denominators and primitive norms give smaller errors,
but this deliberately coarse bound already certifies that the smooth
replacement can be paid without altering a large strict native margin.
It is a fixed finite experiment, not a uniform D-dependent mollification.

The generic residual-exponent/mask grouping is independently checked on
the old complete 150-row spatial norm ball: it reconstructs exactly
R2=1176 and the leading face 456. This authenticates that the new full
sum preserves the original critical classifier and all principal masks,
although its radial smoothing and therefore its finite value have changed.
