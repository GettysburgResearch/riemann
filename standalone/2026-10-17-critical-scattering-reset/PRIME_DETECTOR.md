# A Gaussian prime-discrepancy detector that permits multiple critical zeros

Status: a proposed, fully written application of the classical explicit
formula. It changes the diagnostic from reciprocal zeta to its logarithmic
derivative. It does not prove an upper bound beyond what is equivalent to
the desired zero-free statement. The explicit formula and the prime-counting
interpretation are classical; no novelty claim is made for them.

## 1. Literal prime source and the exact continuum term

Fix F, a finite prime-ideal set S, Gaussian width a>0 and a separately fixed
real height t. Write Z(s)=zeta_F^S(s), and let Lambda_F^S(I)=log Np if
I=p^k with p outside S, and zero otherwise. Use

    g_a(x)=exp(-x^2/(4a))/sqrt(4 pi a),
    b=1/2-it,
    C_(a,t)(x)=integral_0^infinity exp(bu)g_a(x-u)du,
    P_(a,t)(x)=sum_I Lambda_F^S(I)(NI)^(-1/2-it)
                         g_a(x-log NI)-C_(a,t)(x).          (1.1)

Thus the baseline is a one-sided continuum measure convolved with the same
Gaussian. It is not simply exp(x/2+a/4) at all x. At height t=0 it is exactly

    C_(a,0)(x)=1/2 exp(x/2+a/4)
                         erfc(-(x+a)/(2 sqrt(a))).         (1.2)

More generally, with the entire complementary error function,

    C_(a,t)(x)=1/2 exp(bx+a b^2)
                         erfc(-(x+2ab)/(2 sqrt(a))).       (1.3)

These formulas follow by completing the square in the defining integral.
The integral definition is sufficient everywhere in this note. In
particular |C_(a,t)(x)|<=C_(a,0)(x) for real x.

All prime-power sums and derivatives converge locally uniformly by Gaussian
decay and the elementary majorant

    sum_(NI=n) Lambda_F(I) <= [F:Q] log n

when n is a rational prime power, and zero otherwise. This majorant retains
all distinct prime ideals and powers. As x tends to minus infinity the
source and continuum both have Gaussian decay, up to a fixed polynomial
factor, so their negative-half-line Laplace transforms are entire.

On Re z>1/2, absolute convergence gives

    integral_R P_(a,t)(x) exp(-zx)dx
      =exp(a z^2)[-Z'/Z(1/2+z+it)-1/(z-1/2+it)].        (1.4)

The rational term is the transform of (1.1)'s exact continuum. It cancels
the sole pole contributed by the pole of Z at s=1. It is not a subtraction
at an unknown zero. Every zero rho of Z remains a SIMPLE pole of (1.4),
whose residue is

    -m_rho exp(a(rho-1/2-it)^2),                         (1.5)

where m_rho is its multiplicity. This is the key distinction from 1/Z:
there is no reciprocal derivative at a zero and no higher-order pole.

## 2. Which zeros are included

Let Z_+ be the set of distinct zeros of Z in Re s>=0, counted in formulas
below with their actual multiplicities m_rho. It consists of:

* the nontrivial Dedekind zeros, with 0<Re rho<1;
* the zero at s=0, if present, of order r_1+r_2-1+|S|;
* the nonzero imaginary zeros of missing Euler factors. A prime p in S
  contributes zeros 2 pi i k/log Np, k in Z. When grids or ideal norms
  coincide their multiplicities add; no equal-norm ideal is dropped.

There are no other zeros in Re s>=0. Here one uses the classical
nonvanishing of zeta_F on Re s=1 away from its pole, its functional equation,
and its usual trivial-zero description. The order r_1+r_2-1 at zero is
nonnegative, including the value zero for Q and imaginary quadratic fields.
One may equivalently keep the Dedekind and finite Euler-factor contributions
as separately indexed sums; their addition gives the same multiplicities.

The standard zero-counting estimate, with multiplicity, is

    sum_(rho in Z_+, |Im rho|<=T) m_rho
                          =O_(F,S)((1+T)log(3+T)).     (2.1)

Finite Euler grids contribute only O_S(1+T). Consequently Gaussian-weighted
zero sums converge absolutely. No simplicity or lower bound on Z'(rho) is
involved in this counting statement.

## 3. An unconditional absolutely convergent modal formula

### Theorem 3.1

For every real x,

    P_(a,t)(x)
       =-sum_(rho in Z_+) m_rho
          exp(a(rho-1/2-it)^2+(rho-1/2-it)x)
         +R_(a,t)(x),                                   (3.1)

where the zero sum converges absolutely, locally uniformly in x, and

    |R_(a,t)(x)| <= C_(F,S,a,t) exp(-3x/4),  x>=0.       (3.2)

The remainder is the original inversion integral on Re z=-3/4:

    R_(a,t)(x)=1/(2 pi i) integral_(-3/4-i infinity)^(-3/4+i infinity)
      exp(a z^2+zx)[-Z'/Z(1/2+z+it)-1/(z-1/2+it)]dz.   (3.3)

Proof. Start from inversion of (1.4) on Re z=3/4. Move that line only to
Re z=-3/4. Its Z-argument then has real part -1/4. This line contains no
Dedekind trivial zero, nontrivial zero, or missing Euler-factor zero.

On the left line the functional equation expresses Z'/Z through a
logarithmic derivative of zeta_F in Re s=5/4, gamma logarithmic derivatives,
fixed conductor/discriminant terms, and finitely many Euler terms. The
first is absolutely convergent, the gamma terms grow as O_F(log(3+|v+t|)),
and each Euler term is bounded because |(Np)^(-s)|=(Np)^(1/4)>1 there.
The rational term is bounded on the same line. Hence (3.3) converges
absolutely and is O_(F,S,a,t)(exp(-3x/4)) for x>=0.

To justify the horizontal edges, use the standard logarithmic derivative
bound away from zeros, which follows from the Hadamard product of the
completed Dedekind zeta function. On each sufficiently large unit height
interval choose a height separated from every zero in the relevant strip
by at least a fixed inverse power of that height. Such choices exist by
the zero count (one may use the classical local O_F(log T) count, or the
weaker global (2.1) with a more generous inverse power). The finitely many
Euler grids are avoided as well. Along these horizontal segments Z'/Z
has at most polynomial growth. The factor exp(-a T^2) makes their
integrals tend to zero. This is the usual Gaussian explicit-formula
contour argument; it never crosses infinitely many poles without a limit.

The pole at s=1 was canceled in (1.4). Every crossed pole therefore has
residue (1.5), yielding the finite truncated zero sum. For x in any fixed
compact real interval and 0<=Re rho<1, its absolute summand is bounded
by a fixed constant times m_rho exp(-a(Im rho-t)^2). Estimate (2.1)
therefore permits the limit and gives local uniform convergence. QED.

It would be incorrect to move the left line to minus infinity and sum
all negative trivial zeros: their Gaussian factors exp(a(Re rho-1/2)^2)
grow quadratically in their negative real parts. Keeping (3.3) is part
of the theorem. Likewise replacing the one-sided C by its large-x leading
exponential would break the bilateral Laplace normalization.

## 4. A stability criterion exactly compatible with multiplicity

Write

    E_P(U)=integral_0^U |P_(a,t)(x)|^2 dx.

### Theorem 4.1

For any one fixed a>0 and t, the following statements are equivalent:

    (i)   zeta_F satisfies its Riemann hypothesis;
    (ii)  P_(a,t)(x)=O_(F,S,a,t)(1) for all x>=0;
    (iii) E_P(U)=O_(F,S,a,t)(1+U) for all U>=0.           (4.1)

Moreover, under (i) one has the precise Cesaro energy limit

    lim_(U -> infinity) E_P(U)/U
       =sum_(rho=1/2+i gamma, distinct)
                  m_rho^2 exp(-2a(gamma-t)^2).           (4.2)

Zeros are distinct in the sum and their multiplicity is squared in the
weight. Both signs of gamma and a possible central zero are retained.
No zero-simplicity or reciprocal-derivative hypothesis is required.

Proof of (i) => (ii) and (4.2). Under RH the nontrivial-zero contribution
in (3.1) is the absolutely and uniformly convergent trigonometric series

    -sum_(rho=1/2+i gamma) m_rho exp(-a(gamma-t)^2)
                                          exp(i(gamma-t)x). (4.3)

The Re rho=0 terms are O_(F,S,a,t)(exp(-x/2)), and (3.2) is even smaller.
Thus P is bounded. For a finite sum in (4.3), integrating its squared
modulus and dividing by U kills all unequal frequencies in the limit.
Absolute convergence permits uniform approximation by finite sums,
so the same holds for the full series. The exponentially decaying error
has zero Cesaro contribution. This proves (4.2). The series on its right
converges since it is bounded by the square of the convergent positive
sum of the unsquared weights in (4.3).

The implication (ii) => (iii) is immediate. For (iii) => (i), Cauchy-Schwarz
on successive unit intervals makes the one-sided Laplace integral of P
holomorphic in Re z>0. Its negative-half-line transform is entire.
Uniqueness therefore identifies (1.4) with a holomorphic function there.
An off-critical zero rho with Re rho>1/2 would give the nonzero residue
(1.5) at z=rho-1/2-it, a contradiction. The functional equation then
puts every nontrivial zero on the critical line. A fixed vertical shift
t still tests all imaginary parts. QED.

This is a classical RH-equivalent prime-error criterion in the chosen
Gaussian coordinates. It is NOT a proof of (ii) or (iii). Its advantage
as a research target is that even arbitrarily large finite multiplicities
produce bounded oscillations here; they do not create polynomial log-time
modes as they do for reciprocal-zeta detectors.

## 5. Quantitative calibration and height

The residue at a zero rho=1/2+delta+i gamma has squared magnitude

    m_rho^2 exp(2a[delta^2-(gamma-t)^2]).                 (5.1)

Thus choosing t close to a particular ordinate removes Gaussian blindness
without requiring a derivative of zeta at the zero. The multiplicity stays
as an explicit coefficient. The off-critical part of the pole-energy
lemma in POLE_CALIBRATION.md, with pole order ONE, gives

    limsup_(U -> infinity) E_P(U)/exp(2 delta U)
       >= m_rho^2 exp(2a[delta^2-(gamma-t)^2])/(2 delta),
                   delta>0.                           (5.2)

This is a limsup result with no rightmost-zero premise or effective onset.
Several distinct zeros on the same real-part line can be included by
summing the squared residue weights. Other modes cannot cancel this
Gram lower bound. The formula follows from the analytic pole, not from
treating a single formal residue as the whole source.

If all nontrivial zeros satisfy Re rho<=b0 for some 1/2<=b0<1, then the
unconditional formula (3.1) immediately yields

    |P_(a,t)(x)| <= C_(F,S,a,t) exp((b0-1/2)x), x>=0.    (5.3)

The Gaussian permits this endpoint exponent without a contour approaching
the unknown zero line; the convergent sum in (3.1) gives the estimate.
This is a consequence of a known zero-free boundary, not an improvement
of it. A proposed 11/12 boundary would give the rate exp(5x/12) here,
subject to that proposal's own independent-review qualifications.

For fixed a, the usual local zero-counting estimate also gives, under RH,

    sup_(x>=0) |P_(a,t)(x)| <<_(F,S,a) log(3+|t|).       (5.4)

One bounds (4.3) in unit ordinate intervals and uses Gaussian decay;
(3.3) has the same logarithmic height cost from its gamma terms.
The finitely many Euler grids have bounded Gaussian mass per unit
interval. This is an RH-conditional, height-priced estimate, not a
center-uniform constant or an escape from #955's native hull obstruction.

### What finite-height verification can and cannot reveal

Suppose, separately, that RH has been rigorously verified only for the
Dedekind zeros with |Im rho|<=T. At center t=0, the possible contribution
of the remaining nontrivial zeros in (3.1), uniformly for 0<=x<=U, is at
most

    exp(U/2+a/4) sum_(rho nontrivial, |Im rho|>T)
                                m_rho exp(-a(Im rho)^2). (5.5)

This follows from |Re rho-1/2|<=1/2 and needs no assumption on the
unverified zeros. Zero counting makes the sum a Gaussian tail with
polynomial/logarithmic factors; no numerical constant is asserted here.
Thus finite-height verification can already explain very long apparently
stable Gaussian trajectories when U is well below 2aT^2. This is a
conditional caution about detector sensitivity, not a claim that such a
height verification was performed in this packet or a substitute for an
all-scale estimate. The finite Euler-grid terms remain known decaying
terms and are not part of the unknown tail in (5.5).

## 6. Relation to the prime-memory equation and computational use

At height zero, the memory kernel in PRIME_MEMORY.md is

    K=sum_I Lambda_F^S(I)(NI)^(-1/2) delta_(log NI).

The detector here is exactly its Gaussian-smoothed discrepancy from
the universal continuum kernel exp(u/2)1_(u>=0)du:

    P_(a,0)=g_a*[K-exp(u/2)1_(u>=0)du].                 (6.1)

Consequently this construction is tied to the actual source of the delay
equation. It identifies a reasonable stability goal for the prime error,
with a finite, explicit treatment of the pole at one and of multiplicity.
It does not make the discrepancy small automatically, nor does it yield
the required bound on its convolution with the native inverse source.

For finite numerical work compute the prime-power sum and the erfc
continuum with the SAME a, x and excluded-prime convention. Retain every
prime power; primes alone produce a different signal. If S is nonempty,
its missing prime-power terms must be matched to Z=zeta_F^S throughout.
For narrow Gaussians the prime cutoff can be padded on the log scale and
controlled by the same kind of absolute Gaussian tail bound as in the
memory theorem. Plots and bounded finite tables cannot establish (4.1).

## 7. Direct specialization to a fixed primitive Dirichlet character

Fix one primitive Dirichlet character chi of conductor q, with its usual
zero extension at integers not coprime to q. The primitive principal case
is q=1 and L(s,chi)=zeta(s). Write delta_chi=1 in that case and zero
otherwise. For fixed a>0 and t put

    P_(chi,a,t)(x)=sum_(n>=1) Lambda(n)chi(n)n^(-1/2-it)
                         g_a(x-log n)-delta_chi C_(a,t)(x). (7.1)

Every prime power is retained with chi(p^k)=chi(p)^k. No extra Euler mask
is introduced. The same absolute Gaussian calculation gives

    Laplace[P_(chi,a,t)](z)
      =exp(a z^2)[-L'/L(1/2+z+it,chi)
                          -delta_chi/(z-1/2+it)]          (7.2)

on Re z>1/2. For nonprincipal chi there is no pole at one to subtract.

Let kappa in {0,1} satisfy chi(-1)=(-1)^kappa. The completed primitive
Dirichlet functional equation uses Gamma((s+kappa)/2). For nonprincipal
chi its trivial zeros are at the nonpositive integers of parity kappa;
zeta has its usual negative even trivial zeros. At zero,
an even nonprincipal primitive character has a SIMPLE trivial zero, since
the completed value there is nonzero by the functional equation and
L(1,conjugate(chi))!=0. An odd primitive character has no zero at zero;
zeta(0) is also nonzero in the principal case. These are the only extra
zero contributions crossed besides the nontrivial zeros when the z-line
is moved to -3/4, where the L-argument has real part -1/4. The gamma and
Euler-product estimates used in Section 3 apply on that same line.

Consequently the proof of (3.1) gives an absolutely convergent Gaussian
sum over the nontrivial zeros of L(s,chi), plus the just-described zero
at zero when present, and a remainder O_(chi,a,t)(exp(-3x/4)) for x>=0.
The fixed nonprincipal character can have complex coefficients; absolute
convergence and the Hermitian energy calculation do not require reality.

For this one fixed character, therefore,

    every nontrivial zero of L(s,chi) has real part 1/2
      <=> P_(chi,a,t)(x)=O_(chi,a,t)(1), x>=0
      <=> integral_0^U |P_(chi,a,t)(x)|^2 dx=O_(chi,a,t)(1+U). (7.3)

The reverse implication correctly stays within the fixed chi. The
functional equation first sends a zero rho of L(s,chi) to a zero 1-rho
of L(s,conjugate(chi)). Complex conjugation then gives a zero
1-conjugate(rho) of L(s,chi). Thus absence of right-half zeros also
excludes left-half zeros for this same character. It is unnecessary and
generally incorrect to assume conjugate pairs of zeros within a nonreal
character's L-function.

Under the first condition in (7.3), the identical finite-sum approximation
argument gives

    lim_(U -> infinity) (1/U) integral_0^U |P_(chi,a,t)(x)|^2 dx
       =sum_(rho=1/2+i gamma of L(s,chi), distinct)
                              m_rho^2 exp(-2a(gamma-t)^2). (7.4)

The sum includes the zeros that actually occur, without doubling positive
ordinates or postulating simplicity. This is an explicit specialization
to a fixed primitive Dirichlet L-function, not a claim for arbitrary
Euler products or an unproved general Artin L-function class. It supplies
a common prime-discrepancy diagnostic for the Dirichlet and Dedekind
directions; it proves no new upper estimate for either.

## 8. Sources and scope

This theorem uses the classical analytic continuation, functional equation,
Hadamard product and zero-counting estimates for Dedekind zeta functions,
plus finite Euler factors and Gaussian inversion. These are also the
standard explicit-formula ingredients in the primary Mertens-type paper
of Hu--Kaneko--Martin--Schildkraut, especially its analytic preliminaries
and Section 2:

https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/on-a-mertenstype-conjecture-for-number-fields/B01C7628DF4D57CAE8410901FD6A9321

Their assertions about unsmoothed Mertens functions or conditional inverse
derivative moments are not premises of this log-derivative detector.
The exact Gaussian continuum, the finite left-line remainder, the explicit
S-zero accounting, and (4.2)'s multiplicity weights are derived above.

No new zero-free region, prime-discrepancy upper estimate, formal proof
assistant verification, or all-height computational check is asserted.
This is a cleaner formulation of a missing estimate, together with its
complete spectral calibration, rather than evidence that the estimate
has been proved.
