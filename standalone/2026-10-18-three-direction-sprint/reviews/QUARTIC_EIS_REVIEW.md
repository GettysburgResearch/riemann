# Scoped mathematical review of the late quartic square-index note

Reviewed publication target: `quartic/ALL_SQUARE_INDICES.md`.

Reviewed final raw SHA256:
`cb75e0939efa1d8e51892e65477c562e383dd9fee359aa13997a92e9a2a935c3`.

**Verdict: no blocking issue found at the stated arithmetic and scalar-Mellin
scope.** No global square-index period, weighted automorphic filter,
noncancelling reciprocal estimate or new zero-free region is authenticated.
The reviewer supplied the stronger original Suzuki source pin and the
direct-diagonal correction used in the base-index existence argument; this
is a fresh reconstruction of the final mathematics, not a claim of complete
authorship independence.

## Primary sources actually inspected

1. David--Dunn--Hamieh--Lin,
   [arXiv:2306.11875v2](https://arxiv.org/html/2306.11875v2), equations
   (3.2)--(3.11), (4.6), (4.12)--(4.22), the constant-term table immediately
   after (4.22), and (4.34)--(4.38).
2. Suzuki, *Some results on the coefficients of the biquadratic theta
   series*, J. Reine Angew. Math. 340 (1983), 70--117, original scanned
   pages [103](https://gdz.sub.uni-goettingen.de/content/PPN243919689_0340/1000/0/00000107.jpg)
   and [114](https://gdz.sub.uni-goettingen.de/content/PPN243919689_0340/1000/0/00000118.jpg),
   viewed as pixels, with the surrounding OCR read for context. The page
   114 image has SHA256
   `7b12dba6bb9ef33fe6525b0f67fa067d3d5a85e67a692c611b7b4e49b42e6bd0`.

The original page 103 fixes squarefree primary m. Page 114 Theorem 3 states
psi_i(m^4 mu)=psi_i(mu) with NO coprimality assumption on mu. The adjacent
Theorem 4 explicitly requires (mu,m)=1, confirming the distinction. Thus
full p^4 periodicity, including odd valuations of the index, is classical
after taking m=p. The note correctly credits this and presents its finite
calculation as an independent reconstruction rather than a new periodicity
theorem.

## Arithmetic reconstruction

The quartic reciprocity factor in coprime-modulus CRT squares to one.
The degree-one prime formula gives the stated mu*epsilon square, and
the inert primary prime -p has normalized Gauss sum 1 and epsilon=-1,
which verifies the otherwise easily missed degree-two Euler factor.
The numerator-one sum vanishes at every repeated prime. For a moving
nonunit numerator that vanishing is unavailable: at (nu,c)=(p,p^2), the
normalized square is q. This agrees with the draft's explicit warning.

I reconstructed the two-ray prime-power calculation. Its residual
quartic exponent is 2*ell-k modulo four. For k=4j, the local exponents
ell=4i give H_0 and the terminal exponent 4j+1 gives H_2. For k=4j+2,
they give H_2 and H_0 respectively. The odd-exponent ray operator is
-J in the nontrivial primary class; T_p^2=a_p I. The conjugate local
Gauss branch is a_p*conjugate(G), including the numerator phase. Hence
A B=q^(3-4z) I with no lost sign. At z=5/4 the one coprime p^4 identity
forces A h_2=q^(-1)h_0 and B h_0=q^(-1)h_2. The identity
Q_j+q^(-j-1)=1+q^(-1) proves both complete even-valuation recurrences.

For m=d^2 r, no condition (d,r)=1 is permitted or needed. Every primary
d has d^2=1 modulo four, so R(m)=R(r). The fixed symmetric cusp pairings
with J^T B J=kappa B give the finite character delta_kappa exactly.
Multiplying by chi(m)(Nm)^(1/2-s) leaves a d factor
chi(d)^2 (Nd)^(1-2s) and a squarefree r factor
mu(r)chi(r)conjugate(epsilon(r))delta_kappa(r)/(Nr)^s.
Their independent sums therefore give the displayed Euler ratio, including
all primes shared by d and r. Choosing chi=epsilon*delta_kappa gives
L(2s-1,epsilon^2)/zeta(s), not an untwisted numerator zeta.

## Nonzero fixed base and scalar Mellin normalization

The direct diagonal scattering term phi_(i1,i1), at its OWN cusp, has
nonzero residue at 5/4. This establishes that theta_(i1) is nonzero without
transposing the two scattering indices. If every nonzero Fourier mode at
infinity vanished, its expansion would be C y^(3/4) globally. C=0 contradicts
nonvanishing; C!=0 contradicts automorphy under
[[1,0],[lambda^4,1]], whose multiplier is one and whose height action is
nonconstant. Thus some fixed nu_a has f(nu_a)!=0. This is an existence
argument, not a claim that f(1) is nonzero or effectively normalized.

For m prime to the enlarged fixed S_a, the additional quadratic character
(nu_a/m)_2 has square one. The choice chi_a=epsilon*(nu_a/.)_2*delta_kappa
therefore removes it from the denominator while leaving numerator
epsilon^2. The fixed radial factor (Nnu_a)^(1/4-s/2) is entire and nonzero.
The omitted Euler factors are fixed and nonzero for Re(s)>0.

Finally I reconstructed the K_(1/4)^2 Mellin integral. The Fourier factor
(Nnu)^(1/4) and hyperbolic radial measure give exponent
(Nnu)^(1/4-s/2). At nu=m^2 this is (Nm)^(1/2-s), exactly the arithmetic
variable in the note. The stated four-gamma Bessel factor is correct on
Re(s)>1/2 with Fourier-torus Haar mass one. This scalar computation does
not itself justify global unfolding at a noncuspidal residual product.

## Unpaid analytic gates

The same-variable compensated Rankin--Selberg unfolding selects all equal
Fourier indices, not one squareclass. Unknown nonsquare coefficients,
ramified and unit classes, fixed archimedean type, all cusps and the
regularized integral remain. The numerator L(2s-1,epsilon^2) can cancel a
target reciprocal pole; an Eisenstein Fourier denominator cannot simply
be counted a second time to cancel this numerator. Formal square summation
of replica-deflation coefficients does not prove a weighted automorphic
operator bound. The draft preserves these distinctions.

Final-hash refresh: I also checked the ordinary-index angular-type warning.
An integral type k twist in nu restricts to type 2k in m on nu=nu_a*m^2,
while the squared quartic coefficient contributes type -1. Therefore this
simple twist cannot make the denominator principal; this does not rule out
a genuine descent or Weil kernel whose root variable is m.
