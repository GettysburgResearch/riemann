# Zero-loss compression by a bounded-variation transport flux

Status: **PROPOSED component theorem, pending independent exact-draft
review. The complete remaining balanced-source bound is OPEN.**

This sharpens `DIAGONAL_COMPRESSION.md`: its power error 14/33 can be
replaced by a subpower error. The improvement uses a compact signed
transport flux and a classical critical-line zeta bound. It does not
assume any zero-free strip, RH, or cancellation in arbitrary Mobius
coefficients. In particular it does not itself estimate the remaining
balanced source. All definitions of that source remain EXACTLY those
of `DIAGONAL_COMPRESSION.md` Section 2.

## 1. General signed finite-transport lemma

Let integer targets N and integer reference points M lie in [cD,CD],
where c,C>0 are fixed. At each target put a signed real coefficient
alpha_N, |alpha_N|<=A/D. Give its references a probability law P_N,
supported on |M-N|<=G, where 1<=G<=cD/2. Suppose there are O(D)
targets; no factorization uniqueness and no sign coherence are needed.
Define the COMPLETE finite source and its compact cumulative flux

    W(x)=sum_N alpha_N[R(x/N)-E_N R(x/M)],
    F(u)=sum_N alpha_N[1_(N<=u)-E_N 1_(M<=u)].                  (1)

Then, for any fixed 1/6<theta<1/2,

    ||W||_L2(0,infinity)^2
        <<_(c,C,theta) A^2 D^(-1+2theta)G^(2-2theta).           (2)

The constant depends on the stated classical critical-line growth
estimate, not on the target/ref arithmetic. One may alternatively
retain theta=1/6 and a fixed logarithmic loss; (2) suffices here.

## 2. Every BV resource and the exact Mellin multiplier

The total transported mass at every target is zero, so F is compactly
supported in [c'D,C'D]. At a fixed u only targets |N-u|<=G can cross u.
There are at most 2G+2 distinct such integers. Thus

    ||F||_infinity<<AG/D,
    TV(F)<=2sum_N|alpha_N|<<A,
    integral |F(u)|^2du<<A^2G^2/D.                             (3)

These estimates use the ABSOLUTE signed mass and therefore include
oppositely signed targets, probability branching and repeated reference
products. No unproved load bound occurs in (3).

Put f(v)=exp(v/2)F(exp v). Its support is an interval of bounded
length, translated by log D. Direct BV multiplication gives

    ||f||_infinity<<AG/sqrt(D),
    TV(f)<<A sqrt(D),
    ||f||_2^2<<A^2G^2/D.                                      (4)

The absolutely convergent Mellin transform of R, for 0<Re s<1, is

    integral_0^infinity R(x)x^(s-1)dx=-zeta(1-s)/s.             (5)

This is the same classical transform used in the pinned #994 Section 7.
For completeness, split at 1, use the Euler summation formula for zeta
on the upper part, and integrate the elementary -log x-gamma lower
part; all terms at both endpoints converge in this strip. Equivalently
one may first truncate the harmonic remainder and pass to its absolutely
integrable limit. The sign can also be checked at real s in (0,1).

For the finite compact signed measure dF,

    sum_N alpha_N[N^s-E_N M^s]
       =integral u^s dF(u)=-s integral F(u)u^(s-1)du.            (6)

There is no boundary term because F vanishes outside its compact support.
Consequently the factor s in (6) cancels the exact factor 1/s in (5).
With the Fourier convention fhat(t)=integral f(v)exp(itv)dv,
Mellin Plancherel at Re s=1/2 gives

    ||W||_L2(dx)^2
       =(1/(2pi))integral_R
          |zeta(1/2-it)|^2 |fhat(t)|^2dt.                      (7)

All x>0 and all real frequencies are retained. W is a finite linear
combination of L2 dilates, so the left side is defined independently;
the Mellin identity holds pointwise on this strip before Plancherel.

## 3. Fractional Sobolev estimate, including the jump singularities

A compact BV function satisfies

    integral |f(v+h)-f(v)|dv <=TV(f)|h|.

Multiplying by 2||f||_infinity and also using the L2 triangle bound
therefore gives

    ||f(.+h)-f||_2^2
       <<A^2 min(G|h|,G^2/D).                                 (8)

This is valid for EVERY h, not just translations smaller than a jump
spacing. In particular the integer endpoint jumps have not been
discarded or replaced by differentiability.

For 0<theta<1/2, Fourier Plancherel and Tonelli give the exact finite
positive-constant identity

    integral |t|^(2theta)|fhat(t)|^2dt
       =c_theta integral_0^infinity
            ||f(.+h)-f||_2^2 h^(-1-2theta)dh.                  (9)

It follows directly by substituting th in
integral_0^infinity |exp(ith)-1|^2 h^(-1-2theta)dh; both endpoints
converge for 0<theta<1. Split the upper bound (8) at h_0=G/D.
The two pieces are

    G integral_0^h0 h^(-2theta)dh,
    (G^2/D)integral_h0^infinity h^(-1-2theta)dh,

both O_theta(D^(-1+2theta)G^(2-2theta)). The condition theta<1/2
is precisely what pays the step discontinuities. The unweighted L2
term from (4) is no larger than this bound since D/G>=1.

The primary input is the unconditional corrected Weyl estimate of
Hiary, Patel and Yang, *An improved explicit estimate for zeta(1/2+it)*,
[arXiv:2207.02366v1, Theorem 1.1, PDF page 2]
(https://arxiv.org/pdf/2207.02366):

    |zeta(1/2+it)|<=0.618 t^(1/6)log t, t>=3.                  (10)

This paper explicitly repairs the older Kusmin--Landau constant; we do
not import the affected older explicit constant. Bounded t is handled
by continuity and conjugation handles negative t. Thus for every fixed
theta>1/6, |zeta(1/2+it)|^2<<_theta(1+|t|)^(2theta). Combining
(7)--(10) proves (2). The numerical 0.618 is not needed in our exponent.

## 4. Apply the lemma to the COMPLETE original source transport

For a product block d~X^2 in `DIAGONAL_COMPRESSION.md`, put D=X^2,
A<<_epsilon X^epsilon, G<<X^(7/10+eta). Write g=7/10+eta.
The global energy of the full difference W_X satisfies

    ||W_X||_L2(0,infinity)^2
      <<_epsilon X^epsilon X^(-2+4theta+(2-2theta)g).            (11)

At theta arbitrarily close to 1/6 its exponent is

    -1/6+(5/3)eta+o(1).                                      (12)

Choose fixed eta>0 and theta>1/6 sufficiently small that (11) is a
negative power, for example eta=1/100, theta=9/50. The exact exponent
then is

    -2+4(9/50)+(2-18/50)(71/100)=-289/2500<0.                 (13)

After arbitrarily small divisor losses, all transported blocks have
decaying global root norm. Since their smallest X is at least a
constant times Y^(1/4), their O(log Y) sum also decays. This controls
the entire native output interval automatically, with no horizon
restriction and no uncounted harmonic jumps.

There is a further coefficient refinement, supplied by the coordinating
sprint track and independently checked here. Let t_d be the aggregate
R(x/d) coefficient of B_X, including every reference factorization.
Equation (10) of `DIAGONAL_COMPRESSION.md` and the elementary divisor
bound give max_d|t_d|<<X^(-3/2+epsilon). Probability transport also gives
sum_d|t_d|<<X^epsilon. Consequently

    sum_d|t_d|^2<<X^(-3/2+epsilon).                            (13a)

Cauchy over all multiples of q in d<=CX^2 yields

    sum_(q<=Q)q^2|sum_(q|d)t_d|^2
       <<X^2 sum_d |t_d|^2 sum_(q|d,q<=Q)q
       <<X^(1/2+epsilon)Q.                                   (13b)

Combine (13b) with the sharper geometric resource
X^epsilon(Q+Q^2/X) already proved in that file. Splitting X at
Q^(2/3) gives the uniform full coefficient resource

    sum_(q<=Q)q^2|D_X(q)|^2<<Y^epsilon Q^(4/3).               (13c)

The target part has the cheaper Q times logarithms resource. Thus,
after all product blocks, the complete low-denominator energy on
an actual native annulus is at most

    Y^epsilon[K^((4/3)rho-1)+K^((10/3)rho-2)].               (13d)

It decays geometrically for the BROADER fixed range 1/2<rho<3/5.
At rho=13/24 its complete energy is O(Y^(-7/36+epsilon)).
The reference small-core root cost remains
Y^epsilon H_S^5[sqrt(S)H_Y+S]. Low product
terms have EXACTLY zero q>Q_j projection. The original top corner has
global root norm O(1), plus the explicitly paid low/core projections.
The q=1 bookkeeping is exactly as in that file.

We conclude for its explicit balanced source B_Y, ANY FIXED
1/2<rho<3/5 and ANY fixed subpower S(Y) that

    ||V_Y^rough-B_Y^rough||_2^2<<_epsilon Y^epsilon              (14)

for every epsilon>0, retaining the actual q>Q_j and core(q)>S(Y)
mask, all old products, all shared primes, the entire strict native
square step and coherent cross terms. The same bound holds for the
complete large-denominator source with NO core removal.

## 5. Exact consumer and the unproved arithmetic task

The lower artificial energy floor 7/33 in the earlier compression
consumer disappears. At the exact source-qualified native crossings,
the all-prefix exponent theorem of #848 and the native energy comparison
of #994 show that a PROVED estimate on this specified balanced source

    ||B_Y^rough||_2^2
       <<_epsilon Y^(a+epsilon)(1+F_Y)^p, 1<=p<2,              (15)

on an unbounded crossing subsequence would give

    2kappa<=a+p kappa, kappa<=a/(2-p),
    Re rho_zero<=[1+a/(2-p)]/2.                               (16)

The native F_Y term has exponent kappa and is dominated because
a>=0,p>=1. The subpower error in (14) contributes exponent zero.
Thus (15) with a=0 and p<2 would imply RH; with
a<(2-p)kappa_0 it would improve the imported intermediate benchmark.
These remain CONDITIONAL conclusions. No estimate (15) has been proved.

There is a concrete reason not to substitute a generic bilinear Mobius
estimate. From the actual definition,

    w_X(a,b)mu(a)mu(b)/(ab)
        =(1/2)sum_(d:(a,b) in G_d)z_Y(d)/(d g_d).               (17)

The apparent reference Mobius signs are exactly compensated by the
weights. The genuine arithmetic is the LOCAL signed original
convolution z_Y(d), not freely oscillating mu(a)mu(b) at the reference
points. Treating the latter signs as an independent cancellation
resource would be circular. Equations (14) and (17) isolate the actual
remaining local convolution problem without claiming it has been solved.

## 6. A quantitative obstruction inside the new balanced class itself

The geometry and weight cap (3) of `DIAGONAL_COMPRESSION.md` do NOT
imply an improving bound uniformly over that class. There is an actual
old-source counterexample, not merely a freely chosen coefficient vector.
Retain only the old unordered pairs of distinct primes p,l in (Y/2,Y],
each with its actual ordered coefficient 2/(pl), and apply the SAME
linear reference transport (9). Call the balanced result B_Y,prime.
All estimates above apply, because this fixed product mask satisfies
(17). Its corner is still O(1), and its references obey precisely the
same squarefree input, strip, weight and native mask conditions.

On the complete witness window
ceil(Y^2/32)<=k<=floor(Y^2/16), all q=pl exceed Q_j, and all q=p,l
are below Q_j for large Y, since rho>1/2. All those pl cores exceed
every fixed subpower S. Thus the retained original source is exactly

    sum_(p<l) 2/(pl) S_(pl)(k).

`PROOF.md` Section 3 proves S_(pl)(k)>=1/5 there, and ordinary PNT
gives its complete energy >>Y^2/log(Y)^4. Equation (14), applied to
this actual source, and the reverse norm triangle inequality imply

    ||B_Y,prime^rough||_2^2 >>Y^2/log(Y)^4.                     (18)

Consequently no uniform bound Y^(a+epsilon)(1+F_Y)^p with a+p<2
can hold for all legal balanced sources satisfying those size caps;
F_Y<=Y suffices for the contradiction. In the COMPLETE signed source
(2), the remaining transported old pairs must cancel this transported
prime sector. That cancellation is retained explicitly by the local
z_Y(d) weights. A claim based only on generic strip sparsity, bounded
coefficients, or reference Mobius randomness fails the test (18).

Another tempting iteration also fails: square PRODUCTS do not mean
square reduced denominators. R(x/r^2) contains all q|r^2, including
large exponent-one cores. Replacing it by S_(r^2) introduces every
lower R(x/(re)), e|r, with its exact Mobius coefficient. Their total
mass and the S_(r^2) mass are not the original reciprocal-square
resource. In particular diagonal references lose the essential
r<=|a-b| bound used in (24) of `DIAGONAL_COMPRESSION.md`. None of
those terms can be deleted as a cheap core-1 sector.
