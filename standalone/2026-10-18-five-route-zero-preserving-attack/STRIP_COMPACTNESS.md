# Narrow-strip approximants: the missing compactness condition and a smaller target

Status: PROPOSED complete analytic component arguments, not independently
refereed. No unbounded sequence of theta approximants is constructed, and
no new zeta strip follows yet. Hurwitz, Montel and moment generating
functions are classical; the contribution is this scoped research adapter
and an explicit counterexample to the tempting weaker hypothesis.

## 1. The actual zeta variable

Use Xi(z)=xi(1/2+iz), normalized by Xi(0) when discussing a probability
characteristic function. A zero rho=beta+i gamma corresponds to

    z=gamma-i(beta-1/2).

The classical critical strip puts every nontrivial target zero in
|Im z|<1/2. Consequently a zero band |Im z|<=b<1/2 implies the ordinary
zeta bound Re rho<=1/2+b. A standardized theta random variable rescales
z; the variance normalization MUST be undone before using this b.

## 2. Exact strip-confined finite factors

For a>=0,w>0,

    f_(a,w)(z)=[a+cos(wz)]/(a+1)                       (1)

is the characteristic function of mass a/(a+1) at zero and mass
1/[2(a+1)] at each of +/-w. If 0<=a<=1 all zeros are real. If a>1,
its zeros are precisely

    [(2j+1)pi +/- i arcosh(a)]/w, j in Z.              (2)

Thus any finite product of such factors has zeros in |Im z|<=b when
each factor does. Independent real-zero factors can be added without
widening the band. There is no cancellation of zeros in a product.
The complete probability law, not merely some of its moments, is used.

## 3. Variance plus a common zero strip does NOT imply compactness

Fix b>0. Put a_n=cosh(bn),

    g_n(z)=[a_n+cos(nz)]/(a_n+1),
    v_n=n^2/(a_n+1),
    f_n(z)=cos(sqrt(1-v_n)z) g_n(z),                   (3)

for all sufficiently large n, when v_n<1.

These are symmetric characteristic functions of variance EXACTLY one.
Every zero has |Im z|<=b. Every fixed moment converges to the corresponding
moment of a symmetric +/-1 random variable: the rare-jump even moments
are n^(2k)/(1+cosh(bn)), which tend to zero, while 1-v_n tends to one.
Nevertheless, for every fixed y>b,

    f_n(iy)>=g_n(iy)
          =[cosh(bn)+cosh(ny)]/[1+cosh(bn)] -> infinity. (4)

Hence these functions are not locally bounded outside the zero band.
Even convergence of EVERY fixed moment has not provided convergence
on the complex region where zero exclusion is needed.

This corrects an important hazard in the preceding strategy discussion.
The strong compactness of variance-normalized Lee-Yang (real-zero) laws
cannot simply be carried over to arbitrary fixed-width zero strips.
The counterexample is a synthetic family, not a statement that the
repository's actual degree-20 ferromagnet is invalid.

## 4. One exponential moment suffices for an improved zeta strip

It is unnecessary to demand local uniform convergence on the ENTIRE
complex plane in order to improve the ordinary zeta boundary.

### Theorem S1 (one-budget strip transfer)

Let nu be the actual symmetric theta probability law whose characteristic
function is Xi(z)/Xi(0). Let nu_m be symmetric probability measures with
entire characteristic functions f_m. Suppose for fixed numbers

    0<=b<1/2<R, C<infinity,

that:

1. every f_m has no zeros in |Im z|>b;
2. integral exp(R|x|) dnu_m(x)<=C for all m;
3. every fixed moment of nu_m tends to the corresponding moment of nu.

Then Xi has no zeros with |Im z|>b, and ordinary zeta has no nontrivial
zero with Re rho>1/2+b. The same conclusion holds if condition 1 is
only certified on expanding horizontal windows within |Im z|<R.

Proof. For |Im z|<R, |f_m(z)|<=C. This gives a normal family on that
connected strip. Any subsequential holomorphic limit has at zero the
prescribed derivatives, because local uniform convergence permits
termwise differentiation and moments are the derivatives of f_m there.
It equals Xi/Xi(0) near zero, hence on the connected strip by analytic
uniqueness. Thus the entire sequence converges there locally uniformly.
The limit is not identically zero, since its value at zero is one.
Hurwitz applies on each of b<Im z<R and -R<Im z<-b, proving zero
exclusion there. Every possible nontrivial zeta zero already has
|Im z|<1/2<R. This proves the global zeta conclusion, including all
horizontal heights. Expanding windows cover each compact used by
Hurwitz, giving the stated variant. QED.

Thus the new target is cofinal approximate moment feasibility with ONE
explicit exponential-moment budget at, for example, R=3/4 in the actual
Xi variable. It is weaker than requiring all exponential moments uniformly.
It is not weaker than the desired zero exclusion once the other hypotheses
are met, and it has not been achieved for the theta source here.

### Explicit finite-order local error

If the first L moments match exactly and both measures have exponential
R-moment at most C, then on |z|<=r<R,

    |f_m(z)-Xi(z)/Xi(0)| <=2C (r/R)^(L+1).             (5)

Indeed the common Taylor polynomial cancels. For each measure the
absolute tail is at most (r/R)^(L+1) sum_(k>L) R^k E|X|^k/k!, which
is at most C(r/R)^(L+1). Moment mismatches add their explicit finite
Taylor sum. This estimate is on a disk, not claimed uniformly over an
unbounded horizontal strip; the full qualitative conclusion uses the
normal-family argument, not an illegal extrapolation of (5).

## 5. A directly enforceable budget for product constructions

For independent symmetric blocks X_j with |X_j|<=W, variance v_j, and
sum v_j<=V, their sum S satisfies, for every real t,

    E exp(tS) <= exp(V[cosh(tW)-1]/W^2).               (6)

Proof. Symmetry gives E exp(tX_j)=E cosh(tX_j). For k>=1,
E X_j^(2k)<=v_j W^(2k-2). Summing the nonnegative power series gives

    E cosh(tX_j)<=1+v_j[cosh(tW)-1]/W^2.

Multiply the inequalities and use 1+u<=exp u. QED.

This is stronger than bounding each block by its support independently:
it pays TOTAL VARIANCE, not the number of blocks. A uniform bound on the
size of each block need not bound the total support of their sum. Also
E exp(R|S|)<=2E exp(RS), so (6) supplies S1's budget. For the factors (1),
one may instead enforce the exact computable budget

    sum_j log([a_j+cosh(Rw_j)]/[a_j+1])<=log(C/2).       (7)

The total variance is sum w_j^2/(a_j+1). Thus candidate search has both
an explicit zero-band constraint and an explicit exponential-tail cost.
Rare-jump factors in (3) violate a fixed budget at every R>b, exactly
as required.

## 6. What the experiment would need to establish

At b=1/3, a successful S1 construction would yield Re rho<=5/6. Current
#994 matches only finitely many theta moments (through degree 20), albeit
with a rigorous real-zero finite model. It is not an unbounded construction.
Allowing nonreal zeros inside the chosen band enlarges the candidate
class, but does not prove cofinal feasibility. The next genuine milestone
is a family of admissible candidates with a controlled budget (7), not
another tiny residual without a full-law or tail certificate.

Finite checks here reconstruct the three-point probabilities and their
complete product moments, verify the exact reciprocal polynomial roots,
and retain variance in the counterexample. They do not constitute a new
Xi approximation or a degree-22 existence certificate.
