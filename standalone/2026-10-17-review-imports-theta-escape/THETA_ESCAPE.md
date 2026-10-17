# Removing the extra ties and isolating a target beyond 1/12

**Status:** complete proposed component deductions from the CT/BGL/de Faveri inputs; the final improved zero-free conclusion has an explicitly OPEN hypothesis. This document does not claim a new unconditional exponent.

Keep CT's literal field, S-data, profiles, quotient measure, nonunit zeros and additive factor. Write

    I(X,Y,Z) = integral sum_{m != 0} A_t(m;X,Y) B_m(Z) dt,

as in CT Section 10.3. Here t denotes a bounded representative of the compact norm-one quotient, not the height of an L-function. The support has full ideal norm O(XY). For each physical m, write mR=h(m)d(m), with h powerful, d squarefree and (h,d)=1. This is a decomposition of the PHYSICAL theta row, not the Poisson frequency u.

## 1. A saving already available on high-powerful rows

Fix beta<=alpha, M=alpha+beta>1 and tau>0. Define I_high by retaining precisely those original rows with N h(m)>=Z^tau; I_low is the complementary original sum. No coefficients or phases are replaced.

For a reflected dyad P<=N h<2P, D<=N d<2D, CT gives

    Q(P,D) <= Z^eta P^(1/2)(D+D^2 P/Z),   PD << Z^M.

Retain the factor previously discarded:

    P^(1/2)D <= Z^M P^(-1/2),
    P^(3/2)D^2/Z <= Z^(2M-1) P^(-1/2).

Since M>1, and high rows lie in dyads P>=Z^tau/2,

    sum_high |B_m|^2 << Z^(2M-1-tau/2+eta).

The full additive square bound is still an upper bound for any subset. Its exponent is -beta. Cauchy and the finite quotient volume therefore give

    |I_high| << Z^(alpha+beta/2-1/2-tau/4+eta).       (H)

The dyadic logarithms are absorbed into eta. This proves a genuine tau/4 gain on this subfamily using existing inputs. It does not prove a full theta improvement: low-powerful rows, including squarefree rows, remain. Claiming tau/2 after Cauchy would be an error; a negative control catches it.

## 2. Why improving only the old theta estimate is insufficient

For alpha=1/2+e, beta=1/2, the old calculation has three limiting growth exponents equal to 1/4:

- the theta/additive norm product;
- the good Poisson class shifted beyond sigma=3/4;
- the principal z remainder on xi=1+e, z=e.

Thus a new theta gain would be hidden by two unchanged error terms. We now move both without assuming #959's conclusion.

## 3. Move the good class slightly farther left

Use first zero threshold sigma0=187/250 instead of 3/4, retaining the next thresholds 21/25 and 19/20. The exact de Faveri substitution has

    g(sigma0)=62212/85183.

It follows either from the source's middle-range formula with q=2sigma0-1 or by checking each of the ten terms of the displayed detector. `verify.py` does both formula evaluation and all-term upper-bound checks. Fixed S-unit twists and complete columns are retained exactly as in #959's adapter.

With z0=2/5, alpha=1/2+e and beta=1/2, the four top-frequency exponents become

    good:      31/125 + 11e/10;
    middle 0:  522101/2129575 + 37e/20;
    middle 1:  85111/353840 + 37e/20;
    last:      11/94 + 37e/20.

The first constant is 0.248; the next is approximately 0.24516676. Each lies strictly below 249/1000+2e throughout 0<e<=10^-5. The complete four-way partition, lower-count/upper-contour rule, fixed exceptional sets and reciprocal disks are unchanged in structure. This step uses a stronger good contour, not an invented bound for inverse-L moments.

## 4. Move the principal remainder using the already stated CT theorem

Use only CT's upstream zero-free region Re(s)>31/32, not #959. Move the principal xi line to

    x_p=31/32+e.

For this fixed field and positive e, ordinary zero-free logarithm arguments give polynomial vertical growth of 1/zeta_F^S on that line. One can apply Borel--Caratheodory to the pole-removed zeta on fixed-width disks inside the zero-free half-plane; its Euler-side normalization and fixed-strip growth bound the logarithm by O_e(log(2+|t|)). Its reciprocal is then polynomial. The bounded-height part is compact, and the pole at one is a zero, not a singularity, of the reciprocal. Joint Gaussian/Schwartz factors absorb these polynomial costs.

After the w=1 residue, stop z at **1/100**, not at e. The two remainder exponents are

    w remainder: 5/96 + 11e/6 - e^2;
    z remainder: 179/800 + 149e/100.

All contour vertices and the connecting segments remain in CT's convex correction domain. This includes x+6z>1. In fact retaining z=e on the new xi line would VIOLATE that condition for our small e; this tempting shortcut is expressly rejected by the checker.

The main double residue is the same c0 f_alpha. Its defining original Mellin contour can be moved to x_p by the known CT zero exclusion and H's convergence; no new zero-free conclusion is presumed. The pole at s=1 in zeta causes no extra reciprocal pole. The original w and z poles remain the only residue crossings in this principal calculation.

## 5. Complete comparison with slack

Keep #959's small-frequency range U<=Z^(1/100), large-frequency cutoff U=Z^(1/2), and its original-line large-frequency calculation. The small exponent is 417/2000+11e/10, and the large exponent is -19/4-3e/2. The intermediate horizontals are handled by the same fixed positive height exponent and joint height decay; only fixed real contour coordinates have changed. Every new coordinate remains strictly in the correction domain and inside its assigned zero-free rectangle. Thus that argument remains valid, after choosing larger but fixed decay orders if needed.

The new four-class table and principal contours give the proposed comparison

    I(X,Y,Z) = c0 f_alpha(Z) + O_e(Z^(249/1000+3e)).    (P)

All remaining arbitrary power losses are allotted total cost less than e. This is a deduction from the imported analytic package, not from a new signed estimate. The independent checker proves its finite polynomial budgets on the whole e interval, not by endpoint sampling alone.

## 6. One explicit OPEN gate that would beat 1/12

Set tau=1/100 and define I_low using exactly N h(m)<Z^(1/100). Require, for every sufficiently small fixed e>0 and every eta>0,

    |I_low(Z^(1/2+e), Z^(1/2), Z)|
       <<_(F,S,e,eta) Z^(249/1000+e+eta).             (OPEN-L)

This is a signed estimate for the actual original additive/theta pairing with the stated row cutoff. It is not a moment of a randomized substitute and does not permit taking termwise absolute values first.

By (H), the complementary high sector has exponent

    1/4 + e - 1/400 + eta = 99/400 + e + eta,

which is smaller than the required 249/1000+e+eta. Combining (H), OPEN-L and (P), then taking eta<e, gives

    f_alpha(Z) <<_e Z^(249/1000+3e).

Since b=2/3-e/3, its Mellin transform extends to

    Re(s) > 2747/3000 + 8e/3.

The same nonvanishing H and pointwise fixed-e argument as #959 would exclude zeros in the strict half-plane

    Re(s) > 2747/3000 = 11/12 - 1/1000.

Abelian descent would then give the all-field and finite-order Hecke versions. **OPEN-L has not been proved here.** The new fraction is only a certified consequence of that one remaining hypothesis and the named source inputs. The choice 1/1000 is a concrete demonstration with room in every other budget, not an optimization claim.

## 7. What to investigate inside the remaining sector

CT's reflected formula makes the joint squarefree interaction quadratic, chi_d(c)^3, with a smooth function of Z N(a_f) N(c) N(n)^3/[N(d)^2 N(f)^2]. The additive factor must be paired with this expression BEFORE either a rowwise absolute value or an unconditional norm-product bound. Natural exact tests are projection onto the coherent c=1 modes and bilinear cancellation in the remaining quadratic symbols. Coprimality with h,n,f, the cubic n repetitions, all finite phases, and the original compact t average must remain.

A useful computational experiment would compare the literal signed low-powerful pairing with its two separate squared norms over increasing cutoffs, retaining the arithmetic family. Randomizing coefficients tests another problem. This packet does not report numerical field experiments or a proved projection cancellation. Formula (H) justifies putting the first analytic effort into low-powerful rows rather than trying to strengthen every row uniformly.
