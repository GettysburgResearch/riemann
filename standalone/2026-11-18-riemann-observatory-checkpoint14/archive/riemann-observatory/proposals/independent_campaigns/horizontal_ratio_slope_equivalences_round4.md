# Independent small-shift slope reconstruction for the zeta ratio

Date:17November2026. Contributor:equivalences. **Complete proof attempt pending independent adjudication and prior-source search.** I derived the product-defect and global-tail route before reading root's or li_skeptic's slope arguments. RH is assumed throughout. No simplicity, spacing, derivative-moment hypothesis or novelty claim is made.

Use exactly PAPER-C103's quantity

J_epsilon=(2pi)^−1 integral_R |1−zeta(1/2+it)/zeta(1/2+epsilon+it)|² dt/(1/4+t²).

The proposed limit is

lim_(epsilon↓0)J_epsilon/epsilon
 =sum_(distinct gamma) m_gamma[1−binom(2m_gamma,m_gamma)/4^m_gamma]/(1/4+gamma²).       (S1)

Here positive and negative ordinates are separate terms, and m_gamma is the order of the zero1/2+i gamma. The sum is absolutely convergent. Its smallest possible value, underRH, is

xi'(1)/xi(1)=1+gamma_E/2−(1/2)log(4pi),

with equality if and only if every nontrivial zero is simple. This is a statement about an asymptotic parameter of an already RH-conditional construction; it is not a finite numerical certificate of RH or simplicity.

## 1. Separate the completion factor from a positive zero product

Let s=1/2+it and

G_epsilon(t)=pi^(−epsilon) |(s+epsilon)(s+epsilon−1)/(s(s−1))|²
                   *|Gamma((s+epsilon)/2)/Gamma(s/2)|².

The even, normally convergent paired Hadamard product underRH gives exactly

|zeta(s)/zeta(s+epsilon)|²=G_epsilon(t)H_epsilon(t),

H_epsilon(t)=product_(distinct gamma)
 [(t−gamma)²/((t−gamma)²+epsilon²)]^m_gamma.                  (S2)

Each factor lies in[0,1]. Pairing gamma and−gamma agrees with the even product centered at1/2; the exponential factors cancel. The zero count ensures normal convergence away from the finitely many local zero ordinates. Values at a zero follow by continuity.

Fixepsilon0 in(0,1/4], and restrict0<epsilon<=epsilon0. Uniform Stirling and compact-height estimates give

G_epsilon(t)<=C(1+|t|)^epsilon0,

|(G_epsilon(t)−1)/epsilon|
 <=C(1+|t|)^epsilon0 log(|t|+3).                            (S3)

The polynomial completion factors have no zero/pole on the compact parameter strip used here; epsilon=1/2 is not approached. The bounds are integrable after multiplication by1/(1/4+t²).

## 2. Completion derivative and the exact linear cross term

At epsilon=0 the derivative of the squared polynomial-factor ratio is0: on the critical line

Re(1/s+1/(s−1))=0.

Therefore

g(t):=partial_epsilon G_epsilon(t)|_(epsilon=0)
 =Re psi(1/4+it/2)−logpi.

Dominated convergence using(S3) gives

lim_(epsilon↓0)(integral_R G_epsilon(t)dt/[2pi(1/4+t²)]−1)/epsilon
 =psi(1/2)−logpi
 =−gamma_E−log(4pi).                                      (S4)

For the integral identity, the measure dt/[2pi(1/4+t²)] is the Cauchy/Poisson probability measure of height1/2. Scalingt/2 gives Poisson height1/4 on the vertical lineRe(z)=1/4. Sincepsi is holomorphic inRe(z)>0 and has only logarithmic growth there, its Poisson mean ispsi(1/2). The logarithmic-growth version follows by the usual large semicircle limit or a truncated integral; no unbounded harmonic term is added.

PAPER-C103 Proposition5, independently reconstructed in `audits/balazard_roton_ratio_round3.md`, gives the exact cross term

L_epsilon=integral_R zeta(s)/zeta(s+epsilon) dt/[2pi(1/4+t²)]
 =(gamma_E−1)/zeta(1+epsilon)−zeta'(1+epsilon)/zeta(1+epsilon)²
 =1−(gamma_E+1)epsilon+O(epsilon²).                         (S5)

Thus the completion/cross contribution toJ_epsilon/epsilon is

−gamma_E−log(4pi)+2(gamma_E+1)
 =2+gamma_E−log(4pi)
 =sum_gamma m_gamma/(1/4+gamma²).                          (S6)

The last equality is the classical paired xi logarithmic-derivative identity underRH. In particular the full positive/negative sum equals2xi'(1)/xi(1); it is not the half-sum.

## 3. Local defect mass at a zero of multiplicitym

Define

kappa_m=m binom(2m,m)/4^m.

The elementary integral is

integral_R [1−(u²/(1+u²))^m]du=2pi kappa_m.                 (S7)

Foru>=0, integration by parts gives2m integral_0^infinity u^(2m)/(1+u²)^(m+1)du. Doubling for the real line and applying the beta integral yields(S7). Boundary terms vanish because the defect isO_m(u^−2) at infinity.

For a finite set of distinct ordinates, use

1−product_j f_j=sum_j(1−f_j)product_(k<j)f_k,

withf_j=[(t−gamma_j)²/((t−gamma_j)²+epsilon²)]^m_j. Aftert=gamma_j+epsilon u, the other finitely many factors tend to1, G_epsilon tends to1, and the denominator tends to1/4+gamma_j². The integrable profile in(S7), together with the uniform boundedness ofG_epsilon(t)/(1/4+t²), permits ordinary dominated convergence in u. Consequently the finite-product defect has limiting mass

sum_j kappa_(m_j)/(1/4+gamma_j²).                           (S8)

No positive lower bound on different zero gaps is used: a finite set has positive separation, and the infinite tail is handled separately below. Allowing a zero configuration to depend on epsilon would be a different statement.

## 4. Infinite zero tails: the missing uniformity check

For any finite cutoffY,

0<=H_(epsilon,|gamma|<=Y)−H_epsilon
 <=sum_(|gamma|>Y) m_gamma epsilon²/((t−gamma)²+epsilon²).    (S9)

This follows from1−productf<=sum(1−f) and1−x^m<=m(1−x),0<=x<=1. It keeps multiplicity explicit and applies to convergent finite products before passing monotonically to the limit.

There is a constant independent ofepsilon andgamma such that

integral_R [G_epsilon(t)/(1/4+t²)]
  *epsilon/((t−gamma)²+epsilon²) dt
 <=C(1+|gamma|)^(−2+epsilon0).                             (S10)

To prove it, use(S3). Forlarge|gamma| split into|t−gamma|<=|gamma|/2, where the first bracket isO(|gamma|^(−2+epsilon0)) and the Poisson kernel has bounded total mass, and its complement, where the kernel isO(epsilon/gamma²) and the bracket has an integrable bound independent ofepsilon. Boundedgamma are absorbed by the uniform boundedness of the bracket. This proof controls the entire real-height integral, not only compact sets.

Riemann–von Mangoldt gives

sum_gamma m_gamma(1+|gamma|)^(−2+epsilon0)<infinity,

sinceepsilon0<1. Combining(S9),(S10) shows that the omitted defect after division byepsilon tends to0 asY→infinity **uniformly in small epsilon**. This justifies passing from(S8) to the whole zero product:

lim_(epsilon↓0) integral_R G_epsilon(t)[1−H_epsilon(t)]
                         dt/[2pi epsilon(1/4+t²)]
 =sum_gamma kappa_(m_gamma)/(1/4+gamma²).                   (S11)

This is the global domination argument absent from a merely local zero-expansion calculation. It uses only the zero count and completion bounds, not a negative moment or lower bound onzeta' at zeros.

## 5. Assemble the limit and characterize the minimum

Exactly,

J_epsilon=integral_R G_epsilon(t)dt/[2pi(1/4+t²)]
 −integral_R G_epsilon(t)[1−H_epsilon(t)]dt/[2pi(1/4+t²)]
 −2L_epsilon+1.

Equations(S4),(S5),(S11) give(S1). Absolute convergence follows from0<kappa_m<=m and the usual sum ofm_gamma/(1/4+gamma²).

Letb_m=binom(2m,m)/4^m. Thenb1=1/2 and b_(m+1)/b_m=(2m+1)/(2m+2)<1. Hence m−kappa_m>=m/2, with equality exactly whenm1. Every summand has a positive denominator, so equality in the summed lower bound holds exactly when all multiplicities are1. This proves the stated minimumxi'(1)/xi(1), subject to independent adjudication of the full argument.

## Priority and continuation

The sourceC103 pp8 remarks that it would be interesting to determineJ_epsilon's precise asymptotic, but that remark is not evidence that no later result exists. Search Burnol's ratio estimates, Nyman–Beurling approximation papers, inner-function/Poisson norm identities, and later work on reciprocal-zeta moments before making any novelty claim. The central-binomial constant also appears in the finite polynomial critical-taper calculation; its shared beta integral is an exact connection, not by itself evidence of a new arithmetic theorem.
