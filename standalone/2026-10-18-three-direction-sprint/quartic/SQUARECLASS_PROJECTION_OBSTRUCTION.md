# A sharp norm obstruction for a naive squareclass selector

**Proposed late addendum, 18 October 2026.** This concerns one explicit family of commuting finite Fourier projections on the ACTUAL quartic theta vector. It proves that their all-prime squareclass limit has zero norm in the normalized common-cover Hilbert space. It does not rule out a descent, a different kernel, or an unbounded but controlled trace construction. No zero-free region follows.

## 1. Interfaces and statement

Use F=Q(i), O=Z[i], lambda=1+i. The primary inputs are David--Dunn--Hamieh--Lin, [arXiv:2306.11875v2](https://arxiv.org/html/2306.11875v2), equations (3.1)--(3.3) and Section4.3: on Gamma={gamma in SL2(O): gamma=I mod lambda^4}, the quartic theta functions have the SAME unitary character

    kappa([[a,b],[c,d]])=(c/a)_4  if c!=0, and 1 if c=0.

In particular kappa is a homomorphism. Let theta be any vector in the span of the two quartic residues in the companion ALL_SQUARE_INDICES note, or any L2 function with this same transformation law. Put Gamma0=ker(kappa). Work in the normalized common-cover Hilbert space from COFINAL_HILBERT_FILTER: a function on a finite-index H0 subset Gamma0 has norm squared [Gamma0:H0]^(-1) times its quotient integral. Rational pullbacks D_g f(w)=f(gw) are unitary there. This follows directly from change of variables and equality of conjugate covolumes; no unramified local representation theorem is imported.

Write n(t)=[[1,t],[0,1]]. The vector theta is periodic under n(lambda^4 O). For a good squarefree primary D, let E_(D,nu) be the finite additive Fourier projection

    E_(D,nu) = (ND)^(-1) sum_(b mod D)
                    echeck(-nu*b/D) D_(n(lambda^4 b/D)).       (1)

The trace pairing is nondegenerate at every good prime, so these are the orthogonal character projections indexed by nu modulo D. Their base-cusp Fourier multiplier is 1_(index=nu mod D).

**Theorem.** For EVERY residue nu modulo D,

    ||E_(D,nu) theta||^2 = (ND)^(-1)||theta||^2.          (2)

Consequently, for arbitrary allowed residue sets A_p subset O/p at finitely many good primes, the corresponding joint projection R_P satisfies

    ||R_P theta||^2 = product_(p in P) |A_p|/(Np)
                                                  *||theta||^2. (3)

This is exact, not a random-phase model or a pure-tensor assumption.

## 2. Exact vanishing of every nontrivial squarefree-denominator correlation

It suffices to prove

    <theta,D_(n(lambda^4 b/D))theta>=0                  (4)

whenever D is squarefree nonunit and (b,D)=1. An arbitrary nonzero b modulo a squarefree modulus reduces to this case by cancelling its gcd with the modulus.

Fix such D,b and put t=lambda^4 b/D. Choose a primary Gaussian integer a such that

    a=1 mod lambda^4, (a,D)=1, and (a/D)_2=-1.

This is possible by CRT: choose a nonsquare nonzero residue at one prime of D and square nonzero residues at the other primes. Choose a primary u satisfying

    lambda^8 b u = a-a^(-1) mod D,   u=1 mod a,
    u=1 mod lambda^4.                                  (5)

The inverse a^(-1) in (5) is only modulo D. These conditions are compatible because a,D,lambda are pairwise coprime. There is NO requirement (u,D)=1. In particular all shared primes between u and D are retained. Avoid the finitely many choices giving u=0 or a-lambda^8bu=0.

Set c=D lambda^4 u. Since (a,c)=1, choose d with

    ad=1 mod c lambda^4,

and set B=(ad-1)/c. Then

    gamma=[[a,B],[c,d]] is in Gamma.

Indeed B is divisible by lambda^4; a,d are 1 modulo lambda^4; and c is divisible by lambda^4. The conjugate

    gamma'=n(-t) gamma n(t)
          =[[a-tc, B+t(a-d)-t^2c],[c,d+tc]]             (6)

is also in Gamma. For integrality of its upper-right entry, note that d=a^(-1) modulo D and tc=lambda^8bu, so a-d-tc=0 modulo D. Its lambda-level follows because t has lambda-valuation at least4, tc has valuation at least8, and gamma already has the stated level.

Put a'=a-tc=a-lambda^8bu. The two top-left entries are primary and 1 modulo4; furthermore

    a'=a^(-1) mod D,       a'=a mod u.

Both are coprime to c. The finite quartic symbols therefore give

    kappa(gamma)/kappa(gamma')
       =(D/a)_4/(D/a')_4 * (u/a)_4/(u/a')_4
       =(a/D)_4/(a'/D)_4
       =(a^2/D)_4=(a/D)_2=-1.                          (7)

Here the lambda^4 factor is a fourth power. The u symbols cancel by quartic reciprocity and a'=a modulo u. All reciprocity signs are 1 because a,a' are 1 modulo4: their (Na-1)/4 parities are even. No squarefreeness of u or a is needed.

The two vectors theta and f=D_(n(t))theta are eigenvectors of the SAME unitary pullback D_(gamma'): theta has eigenvalue kappa(gamma'), whereas

    f(gamma'w)=theta(n(t)gamma'w)
              =theta(gamma n(t)w)=kappa(gamma) f(w).

Their eigenvalues are opposite by (7). Unitarity forces orthogonality, proving (4).

This argument is a classical multiplier-intersection calculation. As a consistency check, the local fourfold-cover torus commutator is the square of the quartic Hilbert symbol, making odd Cartan matrix coefficients vanish for a spherical genuine vector. The proof above does not need that extra local interface.

## 3. Uniformity and the zero cofinal squareclass norm

Expanding the projection's quadratic form, or using its self-adjoint idempotence, gives

    ||E_(D,nu)theta||^2=<theta,E_(D,nu)theta>.

Every term with b!=0 modulo D vanishes by (4), after reduction of the fraction. Only b=0 remains, proving (2). Distinct character projections are orthogonal, so summing over allowed residues and using CRT gives (3).

Fix a nonzero base index nu_a and omit its finitely many prime divisors. At each remaining good prime put

    A_p={nu_a*x^2 mod p: x in O/p}.

Zero is INCLUDED, so |A_p|=(Np+1)/2. This is a necessary local condition on every integer in the squareclass nu_a*m^2, including integers divisible by p. Thus

    ||R_P theta||^2
       = product_(p in P) (Np+1)/(2Np) *||theta||^2.      (8)

There are infinitely many good primes. Every factor is at most3/5 since Np>=5, so this product tends to zero. The projections commute and decrease; therefore their cofinal strong limit annihilates theta. The same statement holds after omitting any other fixed finite set of primes.

This does not claim that every frequency passing these residue tests is a square. Such a local-global sufficiency statement is unnecessary: the necessary tests already annihilate the vector's Hilbert norm. Excluding zero would produce an even smaller projection and the same obstruction.

## 4. Exact scope of the obstruction

The hard fourth-power-free filter in the companion note retains a positive norm product. The present quadratic-residue filter has the opposite behavior: its norm loss is about one half at EVERY prime, so no nonzero all-prime Hilbert limit survives. Boundedness of each finite Fourier projector is therefore insufficient to extract a nonzero squareclass vector by this simple method.

A fixed base-cusp Fourier sequence can nevertheless retain nonzero squareclass coefficients in a pointwise or local smooth limit. This does not contradict (8): the fixed-cusp trace is not a bounded functional on the completed normalized common-cover Hilbert space, as explicitly shown in COFINAL_HILBERT_FILTER. The vanishing norm cannot be repaired merely by interchanging that trace with the cofinal limit. Renormalizing by the inverse square root of (8) incurs an unbounded norm cost.

The conclusion is limited to these explicit orthogonal quadratic-residue tests applied to the original same-character quartic vector. A higher-rank/descent kernel, a different observable, or a separately controlled unbounded period is not ruled out. No global arithmetic period or new zero-free strip is asserted.
