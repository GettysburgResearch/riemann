# Two incommensurate scale probes remove real biases without hiding a zeta zero

Status: PROPOSED complete operator/component argument. No improved theta
estimate or zero-free half-plane is proved. This develops the multiprobe
proposal, not a claim to have solved its remaining signed arithmetic.
Finite differences and elementary Diophantine approximation are classical.

## 1. An exact operation on the complete source

For a real exponent lambda, a positive h, and any function F on (0,infinity),
put

    Delta_(lambda,h)F(X)=F(X)-exp(-lambda h)F(exp(h)X).

Its m-th power is the explicit finite combination

    sum_(j=0)^m (-1)^j binom(m,j) exp(-lambda h j)F(exp(jh)X). (1)

If F(X)=sum_n a_n W(n/X), with the complete original coefficients and a
convergent source, (1) is EXACTLY the same sum with profile

    W_h(x)=sum_(j=0)^m (-1)^j binom(m,j)
                                  exp(-lambda h j)W(exp(-jh)x). (2)

No coefficient, ideal, nonunit zero, prime power or tail has been deleted.
For ideal sources replace n by the ideal norm. Smooth compact profiles
remain smooth and compact; logarithmic Gaussians retain all their tails.
Fixed finite combinations have fixed seminorm costs. If a physical theta
identity also changes other linked lengths, that complete rescaling must
be checked separately; (2) does not grant an arbitrary new CT test vector.

### Theorem P1 (full polynomial bias removal)

For any polynomial P of degree less than m,

    Delta_(lambda,h)^m [X^lambda P(log X)]=0.            (3)

Proof. After removing X^lambda this is the ordinary m-th forward
difference of P, with sign (-1)^m. Each difference lowers its degree.
This is an all-X identity, not an asymptotic assertion. QED.

Thus a known term c X^lambda, or a finite logarithmic tower at that real
exponent, can be removed coherently before taking absolute values.

## 2. Why TWO probes matter

In any initial strip where the full Mellin transform converges, substitution
Y=exp(h)X shows

    Mellin[Delta_(lambda,h)^m F](s)
             =[1-exp(h(s-lambda))]^m Mellin[F](s).       (4)

For h=1, the multiplier vanishes on lambda+2pi i Z. A single notch could
therefore hide a hypothetical target zero on that vertical line. This is
not repaired by claiming the real bias has been subtracted.

Take instead h_1=1 and h_2=sqrt(2). Their zero sets have exactly ONE
common point, s=lambda: a common point would require integers k,l with
sqrt(2)k=l. No nonzero such pair exists.

### Theorem P2 (joint zero preservation, including multiplicities)

Suppose a fixed original source has Mellin transform

    H(s)/zeta(s), or H(s)[-zeta'(s)/zeta(s)],

up to explicitly holomorphic terms, with H nonzero at every target zero.
Assume lambda is a real point in (0,1). If BOTH transforms in (4), for
h_1,h_2, are holomorphic in Re s>theta, then zeta has no nontrivial zero
there. The same statement applies after a known real Mellin shift, provided
the joint lost point corresponds to a real point where zeta has no zero.

Proof. At a nonreal target zero rho at least one multiplier is nonzero.
Multiplication by it preserves the full reciprocal pole order, or the
nonzero multiplicity residue of the logarithmic derivative. Thus both
filtered transforms cannot be holomorphic there. At the only common point
lambda, ordinary zeta is nonzero: the alternating eta series is positive
for real 0<s<1 and 1-2^(1-s)<0. There is consequently no target pole lost
at that real point. This proof assumes neither simplicity nor a rightmost
zero. QED.

### A concrete advantage of the two smallest imaginary quadratic fields

The same no-lost-real-zero argument is unconditional for the PRINCIPAL
Dedekind zeta functions of Q(sqrt(-3)) and Q(i), not merely for ordinary
zeta. For every real s>0,

    L(s,chi_-3)=sum_(n>=0)[(3n+1)^(-s)-(3n+2)^(-s)]>0,
    L(s,chi_-4)=sum_(n>=0)[(4n+1)^(-s)-(4n+3)^(-s)]>0. (4a)

Every bracket is strictly positive. The mean-value formula bounds its
absolute size on complex compact subsets of Re s>0 by a constant times
(n+1)^(-Re s-1), so these paired series converge normally there and agree
with their Dirichlet L-functions from Re s>1. Thus (4a) does not assume
absence of Siegel zeros. The factorizations zeta_K=zeta L and the elementary
real nonvanishing of zeta show that neither field has a real zero in
(0,1). Fixed omitted Euler factors are positive and nonzero on that real
interval. P2 therefore also applies to H/zeta_K or H[-zeta_K'/zeta_K]
for these TWO fields, preserving every nonreal zero and its multiplicity.

For an arbitrary quadratic field the analogous sign assertion is NOT
supplied here. This is a precise field-specific freedom: a real-mode notch
can sacrifice a location known independently to be free of target zeros.
It still does not control the filtered arithmetic remainder.

This is a fixed-source statement, not a family-average nonexceptionality
claim. Holomorphy of the filtered transforms is STILL a missing arithmetic
estimate in the intended application.

## 3. A polynomial-height lower bound, not only qualitative preservation

Let |Re s-lambda|<=A and |Im s|>=2pi. Then

    max_(h in {1,sqrt(2)}) |1-exp(h(s-lambda))|
       >= exp(-sqrt(2)A/2)/[3(1+|Im s|)].              (5)

Proof. Write u=Im s/(2pi), so |u|>=1, and choose nearest integers n to
u and k to sqrt(2)u. Put e=max(||u||,||sqrt(2)u||). Then n is nonzero,
and the nonzero integer 2n^2-k^2 has absolute value at least one. Hence

  1 <= |sqrt(2)n-k|(sqrt(2)|n|+|k|)
    <= (sqrt(2)+1)e [2sqrt(2)|u|+(sqrt(2)+1)/2]
    <=12e(1+|u|).

The phase estimate |1-exp(2pi i v)|>=4||v|| now gives a lower bound
1/[3(1+|u|)] for one phase multiplier. Finally, for real a,b,

    |1-exp(a+ib)|^2=(exp(a)-1)^2+exp(a)|1-exp(ib)|^2.

For a=h(Re s-lambda) this costs at most exp(-sqrt(2)A/2) in the root
norm. Since |u|<=|Im s|, (5) follows. QED.

For the m-th differences raise the bound in (5) to m. Thus recovering a
pole from the vector of filtered transforms loses only a fixed polynomial
in height. Gaussian Mellin tests can afford that polynomial. This is much
stronger than a purely qualitative assertion that two frequencies differ.
On compact height sets away from zero the corresponding positive lower
bound follows by continuity; no uniform positive bound at s=lambda is
claimed.

For finitely many DISTINCT real biases one can take products of the
corresponding difference operators. Their joint zero set consists only of
the specified real points. On a bounded real strip only one bias line can
be approached within half the minimum separation; the other factors are
uniformly bounded away from zero. The same proof gives a polynomial-height
lower bound with exponent at most the largest assigned multiplicity, with
constants depending on the fixed separations. No changing list of biases
or growing multiplicity is asserted here.

## 4. The actual Eisenstein task, rather than a manufactured improvement

The #934 mechanism audit identifies real cubic Gauss bias and a principal
Gram obstruction, but also explains that a worst-case bound can remain
sharp for the probe's own vector. The fresh external nonorthogonality paper
confirms that the cubic/quartic obstruction is genuine, not random noise.
Those facts are not proofs that the whole binding contribution is one
homogeneous bias. In particular an X^(5/6) Gauss mean is not by itself the
entire selected-character Poisson remainder.

The useful next question is now precise:

* Identify each coherent REAL Mellin mode in the COMPLETE principal-target
  physical expression, with its true scale and logarithmic multiplicity.
* Apply (1) to that full expression. Verify both rescaled physical profiles,
  all principal residues, all nonprincipal rows, and all tails.
* Bound the resulting two signed remainders more strongly than their
  original separate absolute-value estimates.

The first two filters will not delete any ordinary off-critical zeta zero
by P2. But P1 alone does NOT give the third step. Applying the triangle
inequality to the old bounds merely reproduces their old power exponent.
Likewise, removing a bias from a FIRST mean is not a bound for its entire
Gram covariance. OPEN-PROBE is the full signed filtered physical estimate.

A useful failure test is to compare the desired signal vector with the
span of the proposed canceled components. If every signal is in that span,
no linear combination can preserve it. The two-scale construction avoids
that particular obstruction only for the known zero-free REAL modes, not
for an arbitrary troublesome vector or a nonreal bias at a target zero.

## 5. Scope of finite checks

The checker tests full finite source rescaling, exact ordinary differences,
and the integer identity underlying (5). Synthetic poles are NOT actual
zeta zeros. No CT integral, cubic-theta census or signed remainder estimate
is evaluated. The analytic argument above is separate from these checks.
