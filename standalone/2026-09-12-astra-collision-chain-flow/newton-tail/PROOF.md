# NJT26: terminal-moment control of the entire tail

2026-09-12. **Proposed component proofs, requiring independent mathematical
review. RH and native unbounded-order feasibility are not proved.**

Add-only continuation of PR875 at
`17ad26fd0b3de0c88b56d356ab850b881227b2f5`. In particular, this starts after
CJB26's eight-moment chain and joint bridge, not after the older six-moment
packet alone. No earlier result, source, checker, or status is changed.

The new contribution is the combination of a terminal-moment tail bound,
a growth-budget minimum-modulus bound, and a smaller explicit joint schedule.
Newton inequalities, canonical products, Lee--Yang, and convergence of entire
functions are classical. No claim of external priority is made. The proof
below does not infer a real-zero property for the native source from the
nonnegativity of its ordinary moments.

## 1. Precise model class and the two sources

Let F(z)=E exp(izT) be the characteristic function of a symmetric probability
law with all exponential moments. Write

    F(z)=sum_(k>=0) (-1)^k f_k z^(2k),
    f_k=E T^(2k)/(2k)! >=0,   f_0=1.

F need not have real zeros. In the application it is the original centered
gamma transform F_N of #862, not a newly fitted gamma law.

The comparison model G is an even real entire function of the form

    G(z)=exp(-alpha z^2) product_j (1-lambda_j z^2),
    alpha>=0, lambda_j>0, sum_j lambda_j<infinity.          (1)

The empty product and finite products are allowed. Analytic multiplicities
are represented by repeated factors. Put

    A(w)=G(i sqrt(w))=exp(alpha w) product_j(1+lambda_j w)
        =sum_(k>=0) a_k w^k,  a_k>=0, a_0=1.              (2)

The notation i sqrt(w) means this power series; it introduces no branch into
A. A finite zero-field ferromagnet with nonnegative observable weights and
couplings gives such a G, with alpha=0, by the classical weighted Lee--Yang
theorem and even canonical factorization. Complete infinite-chain limits of
the repository give further examples with a justified product representation.
The statements actually proved below apply to (1), even when G is not itself
a characteristic function. In the ferromagnetic application a_k are its
ordinary even moments divided by (2k)!.

An arbitrary polynomial with nonnegative coefficients is NOT enough for (1).
Nor is checking a finite list of Newton inequalities a certificate of (1).
The admissible graph/product construction is a separate required input.

## 2. NJT1: the terminal coefficient controls every later coefficient

**Lemma.** The sequence b_k=k! a_k is log-concave, has no internal zeros, and
b_0=1. If m>=1 and a_m>0, set

    d_m=(m! a_m)^(1/m).

Then, for every j>=0,

    a_(m+j) <= a_m d_m^j m!/(m+j)!.                      (3)

When a_(m-1)>0, the sharper d_m in (3) can be replaced by

    tau_m=m a_m/a_(m-1) <= d_m.                          (4)

If a_m=0, every later coefficient is zero. Consequently, for s>=0 and
rho=d_m s/(m+1)<1,

    sum_(k>m) a_k s^k <= a_m s^m rho/(1-rho).            (5)

### Proof, including the infinite product

For a finite polynomial with only nonpositive real roots, Newton's
coefficient inequalities imply

    a_k^2 >= ((k+1)/k) a_(k-1)a_(k+1).

One quick self-contained verification of this weaker form is to take the
(k-1)st derivative of the polynomial. Its roots remain real by Rolle and
remain nonpositive. If its first three coefficients are B0,B1,B2 and B0>0,
factor it as B0 product_l(1+u_l w), with u_l>=0. Then
B1^2-2B0B2=B0^2 sum_l u_l^2>=0. Substituting
B0=(k-1)!a_(k-1), B1=k!a_k, and B2=(k+1)!a_(k+1)/2 gives the inequality.
Cases with zero coefficients follow directly or by positive perturbation.
This is the log-concavity of b_k, not of the raw probability moments.

Approximate exp(alpha w) by (1+alpha w/n)^n and truncate the positive product.
These real-rooted polynomials converge locally uniformly to A. Cauchy
coefficient convergence passes each displayed inequality to A. Positivity
of the factors also gives no internal zeros; if a_m=0 there are fewer than
m effective product factors and alpha=0, so the later tail vanishes.

Otherwise the positive ratios b_k/b_(k-1) decrease. Their mth ratio is at
most their geometric mean (b_m/b_0)^(1/m)=d_m. Multiplying all subsequent
ratio inequalities gives (3) and (4). The factorial quotient obeys
m!/(m+j)! <= (m+1)^(-j). Sum the resulting nonnegative geometric series to
obtain (5). Every term of the infinite tail is retained. QED.

This is the important departure from a variance-only Gaussian estimate:
a small high-order coefficient prevents the model from hiding an arbitrarily
large higher-order Taylor tail.

## 3. NJT2: minimum modulus paid by the actual real-field growth

Let R>0, 0<b<=R and

    L_G=log G(2iR) >=0.

Every G in (1) satisfies, throughout |z|<=R and |Im z|>=b,

    |G(z)| >= exp(-2 L_G/3) (b/R)^(L_G/log2).            (6)

This uses no model-zero census or simplicity hypothesis.

**Proof.** Write each lambda as r^-2 with r>0. For z=x+iy,

    |1-z^2/r^2|^2=[(r^2-|z|^2)^2+4r^2 y^2]/r^4.

If r<=2R the factor's modulus is at least 2b/r>=b/R. There are at most
L_G/log2 such factors, counting multiplicity, because each contributes at
least log2 to log G(2iR).

For r>2R set u=4R^2/r^2<1. The factor's modulus is at least 1-u/4. The
integral bound -log(1-u/4)<=u/3 and log(1+u)>=u/2 give

    log |1-z^2/r^2| >= -(2/3)log(1+4R^2/r^2).

Finally |exp(-alpha z^2)|>=exp(-alpha R^2). Its cost is at most 2/3 times
its contribution 4alpha R^2 to L_G. Add these bounds over the entire far
product, replace its logarithmic budget by the larger L_G, and replace the
near-factor count by L_G/log2. Because b/R<=1 these replacements weaken the
lower bound in the correct direction. This proves (6). QED.

Unlike CJB26's variance-only exponent O(VR^2), the exponent in (6) is paid by
log G(2iR). It can be O(R log R) when the moment fit transfers the native
source's real-field growth.

## 4. NJT3: a finite-jet, whole-disk nonvanishing theorem

Use the coefficient error

    E_m(R)=sum_(k=0)^m |f_k-a_k| R^(2k),

and define

    U=F(4iR)+1 >=2,       L=log(2U).                     (7)

Let m>=1 be an integer. Suppose

    E_m(R)<=16^-m,               2^m>=U.                 (8)

Then

    G(2iR)<=F(2iR)+2<=2U,
    sup_(|z|<=R)|F(z)-G(z)|<=2U 16^-m.                  (9)

In particular, if additionally

    4m log2 > L [5/3+log(R/b)/log2],                     (10)

then F has NO zero with |z|<=R and |Im z|>=b. A sharper data-dependent
version uses L_*=log(F(2iR)+2)<=L and requires only

    4m log2 > L+[2/3+log(R/b)/log2] L_*.                  (10a)

No separate variance bound or three-term growth calibration on G is required.
The zero-safe model hypothesis (1) is still essential.

### Proof of the complete model-tail estimate

Positivity of the coefficients of F gives
f_m R^(2m)<=F(4iR)16^-m. Equation (8) therefore implies

    a_m <= U/(4R)^(2m).                                 (11)

If a_m=0 the model tail is zero and the following conclusions hold directly.
Otherwise apply NJT1. At s=(2R)^2,

    d_m s/(m+1)
      <= U^(1/m) (m!)^(1/m)/[4(m+1)] <=1/2,

using U<=2^m and m!<=m^m. Thus the ENTIRE model tail at 2R is at most

    a_m(2R)^(2m)<=U4^-m<=1.

The fitted polynomial at 2R differs from F's polynomial by at most
4^m E_m(R)<=4^-m<=1. Hence G(2iR)<=F(2iR)+2<=U+1<=2U.

At s=R^2 the same tail ratio is at most1/8. Thus the model tail at R is at
most U16^-m/7. The entire source tail at R is at most
F(4iR)16^(-m-1)<=U16^-m/16. Add these two remainders and the fitted error:

    |F-G| <=16^-m[1+U/7+U/16] <2U16^-m.

This proves (9), uniformly on the full complex disk, not just the real axis.

At a hypothetical zero rho of F in the indicated off-axis region, (9) would
give |G(rho)|<=exp(L-4m log2). NJT2 and L_G<=L_* give the contrary lower bound
exp(-2L_*/3)(b/R)^(L_*/log2), which is strictly larger under (10a).
Because L_*<=L, the simpler (10) is sufficient as well. QED.

## 5. NJT4: an explicit smaller moving-source schedule

Here the source is exactly the original centered gamma family. Let independent
G_n have Gamma(shape2,rate1) law and define

    X_N=sum_(n<=N)G_n/n^2, tau_N=2sum_(n>N)n^-2,
    g_N=density(X_N+tau_N),
    h_N(t)=sqrt(g_N(pi exp(2t))g_N(pi exp(-2t))),
    F_N(z)=integral h_N(t)exp(izt)dt / integral h_N(t)dt.

The proposed complete-source results of #862, at its frozen source, supply

    F_N -> Phi=Xi/Xi(0), locally uniformly in C,
    F_N(ir)<=204800(r+2)^(r/2),
    n_N(r)<=26+2r log(2r+2), r>=1,
    Delta_N=(1/4)sum_(all zeros rho) mult(rho)(Im rho)^2/|rho|^4,
    tail_(|rho|>R) Delta_N <=7/R^2+[log(4R)+1]/R,
    Delta_N -> Delta_Phi,             RH iff Delta_Phi=0.       (12)

These are explicit imported analytic components, not recomputed by the finite
checker. In particular (12) does NOT assert Delta_Phi=0.

For every integer j>=2 set

    R_j=2^j, b_j=1/R_j,
    B_j=20+2R_j(j+3),
    m_j=(j+1)[10+R_j(j+3)] = (j+1)B_j/2,
    epsilon_j=2^(-4m_j).                                    (13)

**Conditional completion theorem.** Suppose for an unbounded set of such j
there exist N_j tending to infinity and comparison models G_j of class (1)
with

    sum_(k=0)^m_j |f_(k,N_j)-a_(k,G_j)| R_j^(2k)<=epsilon_j.  (OPEN-NJT)

Then, on the inherited identification/convergence statements (12), RH follows.
Finite ferromagnets are one admissible construction class for G_j; finite
products of real-zero factors are another, without requiring that those
polynomials themselves be probability characteristic functions. The new
criterion is therefore not tied to one graph architecture. A polynomial with
positive alternating coefficients alone is insufficient: its complete real
zero geometry must be established. An unbounded-order realization is NOT
supplied by this theorem.

### The exact integer budget

For R=2^j>=4, 204800<2^18 and 4R+2<=8R give

    F_N(4iR)<=2^[18+2R(j+3)],
    U<=2^[19+2R(j+3)]=2^(B_j-1),  L=log(2U)<=B_j log2.

Because m_j>=B_j, 2^m_j>=U. Also log(R/b)/log2=2j, and

    4m_j=2(j+1)B_j > (2j+5/3)B_j.

The exact margin in this last inequality is B_j/3. NJT3 therefore excludes
all zeros in |z|<=R_j at distance at least 1/R_j from the real axis.

No additional low-frequency source assumption is necessary for convergence
of the whole defect. Here is a complete uniform small-zero budget. The
r=2 bound in (12) gives F_N(2i)<=819200. Positivity of the even moments gives

    |F_N(z)-1| <= (|z|^2/4)[F_N(2i)-1]
                <=204800 |z|^2, |z|<=2.

Thus EVERY stage has a zero-free disk |z|<=delta=1/512, since
204800/512^2=25/32<1. The count in (12) gives n_N(1)<29. Splitting at one,
and dropping only the favorable boundary term in the large-radius part,

    sum_rho mult(rho)/|rho|^4
      <=29*512^4+4int_1^infinity [26+2r log(4r)]r^-5 dr
      <29*2^36+31.

The integral is 26+(8/3)log4+8/9<31; for example log2<3/4 follows from
the strict trapezoidal integral bound for 1/x on [1,2]. The small-zero
contribution has not been deleted or assumed to consist of simple real roots.
Combining this bound with the off-axis exclusion and the FULL tail in (12)
gives, conservatively,

    Delta_(N_j) <=2^39/R_j^2+[log(4R_j)+1]/R_j ->0.          (14)

Then (12) gives Delta_Phi=0. The large constant is intentional, not a useful
low-height bound. It removes the extra condition F_N(2i)<=2 from the cofinal
feasibility premise.

There is also a useful sharper OPTION. Whenever F_N(2i)<=2 has separately
been certified, the same Taylor argument gives a zero-free unit disk. Then
sum |rho|^-4<31 directly, and the bound improves to

    Delta_N <=15/R_j^2+[log(4R_j)+1]/R_j.                   (14a)

Neither version assumes simplicity, a finite global zero census, or reality
of the native approximants at every stage.

### What has improved, and what has not

CJB26's displayed sufficient schedule had
m_j=(2j+4)4^j=O(R_j^2 log R_j). The new sufficient count is
O(R_j (log R_j)^2). Both m count EVEN MOMENT COORDINATES; the raw polynomial
moment degree is 2m. The error allowances also change; this is an asymptotic
improvement of a sufficient joint budget, not a claim of uniform optimality
or of a practical algorithm at the resulting degrees.

At R=1024, m changes from25,165,824 to146,542. No such high-order native fit
was computed. The eight-moment chain already on PR875 is not an example of
OPEN-NJT. A nonsingular finite Jacobian does not establish that larger target
vectors are reachable inside the positive-parameter domain.

### No unnecessary all-order Ising representation hypothesis

There is a useful exact scope distinction. If the comparison class is limited
to one family of spin graphs, OPEN-NJT might be stronger than RH. It need not
be: allow finite products

    G_j(z)=product_(l=1)^d_j (1-lambda_(j,l) z^2),
    lambda_(j,l) positive RATIONAL numbers.                    (14b)

Then existence in OPEN-NJT is also NECESSARY for RH, on the same classical
source/product inputs. To see this direction, assume RH. The even order-one
Hadamard product for Phi has positive real-zero factors and no Gaussian
factor. Its finite products converge locally uniformly to Phi. Approximate
each of the finitely many positive inverse-square root parameters by positive
rationals. For each fixed j this gives a polynomial (14b) whose first m_j
weighted coefficients differ from Phi's by less than epsilon_j/3. Next,
F_N -> Phi and Cauchy coefficient convergence give arbitrarily large N with
the other weighted difference less than epsilon_j/3. Choose N_j increasingly.
Their combined error is below epsilon_j. Multiplicities cause no difficulty.

This is a conditional existence argument, NOT a construction using unknown
zero locations without assuming RH. It shows that the rational-polynomial
version does not impose an extraneous all-order inverse-Ising conjecture.
The qualitative Laguerre--Pólya closure characterization is classical; the
new part here is the explicit joint source/degree/error budget and the
terminal-moment estimates that justify it.

For an actual candidate, positivity and rationality of its lambda factors
make its complete real-zero geometry exact by construction. Verifying its
native coefficient error still requires source-certified intervals. Choosing
those factors to make that error small at unbounded j remains the substantive
unproved task. Merely making Taylor coefficients positive, or repairing a
known nonreal zero set and assuming the repair is small, does not do it.

## 6. NJT5: a stronger fixed-stage obstruction (conditional on GE4)

The native defining-integral certificate GE4 in PR858 supplies a centered
F_5 zero rho with |rho|<32 and Im rho>1/5. It is explicitly NOT a zero of Xi.
That certificate is an imported finite theorem; its quadrature is not rerun.

The support of its probability density lies in (-11/10,11/10), as recorded
in CJB26. The following elementary bounds rederive the support allowance:

    tau5 >=13/36,
    pi/tau5 <=792/91 < exp(11/5).                          (15)

The lower bound tau5>=13/36 follows from the convex trapezoidal inequality
sum_(n>=6)n^-2 >= int_6^infinity x^-2 dx+1/(2*6^2).
A positive rational Taylor sum for exp(11/5) proves the last strict inequality.
Equation (15) gives T5=(1/2)log(pi/tau5)<11/10.

Consequently F5(128i)<=exp(704/5) and F5(64i)<=exp(352/5). For R=32,
U=F5(128i)+1 and L_*=log(F5(64i)+2), the following convenient bounds hold:

    U<exp(141),       L=log(2U)<708/5,       L_*<141/2.

For the first, exp(1/5)>6/5 and exp(704/5)>5 suffice. For the second,
the positive cubic Taylor sum gives exp(4/5)>11/5 and exp(704/5)>10,
so exp(708/5)>2exp(704/5)+2. For the last, exp(1/10)>11/10 and
exp(352/5)>20 give exp(141/2)>exp(352/5)+2. These are complete elementary
inequalities, not rounded values of a special function.

Choose m=256 and b=1/5. Then

    2^m>exp(256*69/100)>exp(141)>U,
    log(R/b)/log2=log(160)/log2<22/3,
    4m log2>17664/25 >708/5+8*(141/2)=3528/5.             (16)

Here log2>69/100 follows from just the first three positive terms of its
atanh series. The integer inequality 160^3<2^22 verifies the logarithmic
ratio bound. The last strict rational margin is 24/25.

NJT3, in its sharper form (10a), would therefore exclude the imported zero
if a comparison model G satisfied E_256(32)<=2^-1024. We conclude:

**No finite ferromagnet, or more generally model (1), can match the first
256 even coefficients of the ACTUAL F5 to this tolerance. In particular no
exact match through raw moment degree512 exists.**

There is no variance-cap hypothesis in this stronger obstruction. It improves
CJB26's sufficient forbidden degree32768 to512; it does NOT claim the first
forbidden degree, a newly computed nonreal zero, or an obstruction to the
moving N_j schedule. The dependence on the unreplayed GE4 certificate remains
visible rather than being converted into a fresh numerical certification.

## 7. The remaining theorem is native feasibility

NJT1--NJT3 solve two quantitative issues: paying the entire model Taylor tail
from the fitted terminal moment and replacing the variance-only minimum
modulus by a source-transferred growth budget. NJT4 gives their complete
conditional path to RH. NJT5 proves that an obvious universal fitting scheme,
which fits each fixed centered stage indefinitely, cannot work.

What is NOT supplied is OPEN-NJT, nor the original native collision covariance
upper bound, nor a favorable total signed zero production on the gamma or
#876 fixed-point homotopy. The latter's positive Laplace response does not
imply the complex comparison-model feasibility in (OPEN-NJT).

The practical research target is now explicit: construct admissible models
and directed coefficient errors at a jointly increasing source stage and
moment order, or prove an inductive realization theorem that guarantees them.
The improved sufficient budget does not remove that substantive mathematical
obligation. See ARITHMETIC.md for a separate sharp constraint on attempts to
make the arithmetic covariance small by optimizing the completion.

## 8. A fully specified synthetic witness, not a native one

To exercise the finite-jet theorem independently of native-source premises,
take F(z)=exp(-z^2/2), the standard Gaussian characteristic function, and

    n=2^100, G(z)=(1-z^2/(2n))^n,
    R=1, b=1/2, m=16.

This polynomial is not itself a probability characteristic function; it is
an admissible real-zero comparator of form (1). Its degree is2n, represented
by ONE rational factor and an integer multiplicity, not by an expanded list
of2n coefficients. The exact first17 coefficients are

    f_k=1/(2^k k!), a_k=binomial(n,k)/(2n)^k.

The checker reconstructs them in two ways and verifies E_16(1)<2^-64. Also
F(4i)+1=exp(8)+1<3^8+1<2^13, using the elementary exp(1)<3, and
2(F(4i)+1)<2^14. Thus m>=13 and

    4m=64>14*(5/3+1).

NJT3 excludes zeros of the Gaussian target in |z|<=1, |Im z|>=1/2, with the
whole infinite target tail and whole polynomial tail paid by the theorem.
This example is not new information about Gaussian zeros. It demonstrates
the compact rational-factor certificate architecture without falsely labeling
an input moment table as the actual theta or gamma source. No corresponding
native witness was produced in this pass.
