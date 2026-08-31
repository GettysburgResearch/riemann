# Actual Xi: a cancellation-safe low-pass lower bound from Laplace evaluation

Status: PROPOSED ANALYTIC/FINITE CERTIFICATE; independent review pending.
Authoring base: `7fbcd592042a5cc98c17d0db2fac62f8171267f2` (BC).
Scope: the literal boundary-dx Hardy norm and output bands [0,D].
The physical interpretation is conditional on the declared inner premise.
No native outer metric, cofinal Xi capture, or RH conclusion is asserted.

Preregistered computation, before evaluating the new bound: use ALL fourteen
BC surviving nodes, their original separate lambda32/64/128 operators,
D in {1/4,1/16,1/64,1/256}, and h=2^j for EVERY j=6,...,16.
Retain all calibration values and all node/band/calibration bounds. Taking
the best proved bound from this declared finite grid is permitted; no root,
parameter, band or calibration is added after seeing its output. The initial
question is whether each of the twelve operator/band cells has a positive
certified lower bound. No numerical floor is predicted in advance.

## 1. A general band inequality, not band Loewner monotonicity

Use the unitary Fourier identification

    f(z)=(2pi)^(-1/2) integral_0^infinity h(t) exp(i z t) dt.

For b=x+i y, y>0, the normalized inverse kernel is

    e_b(t)=sqrt(2y) exp[-(y+i x)t],  ||e_b||_2=1.

Let U be inner in C+, let P_U project onto U H2, and let Pi_D project in
the Fourier variable onto [0,D], D>0. For any h>0 define

    A(U;b,h)=2 sqrt(h y) |U(i h)| / sqrt[(h+y)^2+x^2].

**Theorem LB1 (one-kernel estimate).**

    ||Pi_D P_U e_b||
      >= |U(b)| [A(U;b,h)-exp(-hD)]_+
                          / sqrt[1-exp(-2hD)].                 (LB1)

Proof. Write w for the inverse Fourier transform of U e_b, so ||w||_2=1.
Laplace evaluation gives the exact identity

    integral_0^infinity w(t) exp(-h t) dt
       =sqrt(2y) U(i h)/(h+y+i x).

Splitting the integral at D and applying Cauchy--Schwarz separately gives

    sqrt(2h) |integral w(t) exp(-h t) dt|
       <= ||Pi_D w|| sqrt(1-exp(-2hD)) + exp(-hD).

The first term on the left is A(U;b,h). Take the positive part and use
P_U e_b=conjugate(U(b)) U e_b. This last scalar factor is indispensable:
the estimate concerns the physical projection P_U, not merely M_U. QED.

Suppose now that inner functions Theta0,Theta5 have common inner divisor
Gamma and reduced factors U,B:

    Theta0=Gamma U,  Theta5=Gamma B.

At a zero b of Theta5 with Theta0(b)!=0, the zero survives in B, e_b is
in K_B, and |U(z)|>=|Theta0(z)| at EVERY z in C+ by the product identity
and |Gamma(z)|<=1. Thus the right side of LB1 may be replaced by

    L_D(b,h)=|Theta0(b)|
       [2sqrt(h y)|Theta0(i h)|/sqrt((h+y)^2+x^2)-exp(-hD)]_+
                              /sqrt(1-exp(-2hD)).                (LB2)

This uses two scalar modulus comparisons. It does NOT assert that inserting
Pi_D preserves the global projection order P_U>=P_Theta0. BC correctly
rejects that implication. No value or phase of the unknown Gamma is needed.

## 2. The actual Xi calibration and all positive band widths

Keep f(z)=xi_R(1/2+i z), with the exact normalization of BC1, and fixed
lambda>0. At z=i h, put s=1/2+h>1 and

    ell(s)=xi_R'(s)/xi_R(s)
      =1/s+1/(s-1)-log(pi)/2+psi(s/2)/2+zeta'(s)/zeta(s).

Functional equation and the chain rule give, exactly,

    Theta0(i h)=(1-lambda ell(s))/(1+lambda ell(s)).        (LB3)

The denominator is nonzero for sufficiently large h. Stirling and the
absolutely convergent zeta logarithmic derivative give

    ell(1/2+h)=(1/2)log(h/(2pi))+O(1/h),
    Theta0(i h)->-1                                     (LB4)

for every FIXED positive lambda. This is a statement about the literal Xi
companion, not an arbitrary inner function or a changed lambda(h).

**Corollary LB2a.** Under the inner premise, for every locally surviving
node b and EVERY D>0, ||Pi_D P_U e_b||>0.

Indeed |Theta0(b)|>0, while the first term inside LB2's brackets is
asymptotic to2sqrt(y/h), which eventually exceeds exp(-hD). This proves
positivity for arbitrary band width analytically; the finite grid below
only supplies explicit quantitative floors for its declared cases.

The large-imaginary calibration is load-bearing. A generic inner factor
exp(i tau z) shifts all Fourier support by tau, so no comparable positive
bound on every [0,D] can hold for arbitrary inner numerators when D<tau.
LB4 rules out precisely that exponential-delay obstruction for this use
of the actual raw Xi companion. It does not identify every inner factor.

## 3. Finite trace bound with the correct input metric

For distinct surviving nodes b_j=x_j+i y_j, let E be their kernel span,
and let C be any upper bound for the largest eigenvalue of their normalized
Gram matrix

    G_ij=2sqrt(y_i y_j)/[y_i+y_j+i(x_j-x_i)].

For example, C=max_i sum_j |G_ij| is a valid bound. If l_j is any proved
lower bound LB2 for node j (with h allowed to differ among nodes), then

    ||Pi_D P_U P_E||_HS^2 >= (sum_j l_j^2)/C,
    ||Pi_D P_U P_E|| >= max_j l_j.                       (LB5)

To prove the trace inequality, let T synthesize the normalized kernels.
TT*<=C P_E. Consequently

    sum_j ||Pi_D P_U e_j||^2
        <=C ||Pi_D P_U P_E||_HS^2.

This is a Bessel upper-bound argument, not a sum of nonorthogonal diagonal
entries declared to be a trace. Both bounds also apply to input K_B since
E subset K_B. All operators for a fixed sum use ONE fixed lambda.

## 4. A sufficient cofinal criterion, whose Xi hypotheses remain unpaid

**Theorem LB3 (weighted alignment criterion).** Suppose the inner premise
holds for one fixed lambda, and let b_j=x_j+i y_j be distinct surviving B
zeros such that |x_j|->infinity, 0<y_j<=|x_j| eventually, and:

1. Their normalized kernel family is Bessel, with one finite uniform bound C.
2. For every D>0, sum_j exp(-2D|x_j|)<infinity.
3. sum_j |Theta0(b_j)|^2 y_j/|x_j| diverges.

Then for EVERY D>0,

    ||Pi_D P_U P_(K_B)||_HS^2=infinity.                  (LB6)

Proof. Choose h=|x_j| in LB2. By LB4, eventually |Theta0(i h)|>=1/2.
The denominator of A is at most sqrt(5)|x_j|, so A>=sqrt(y_j/(5|x_j|)).
For a,e>=0, [a-e]_+^2>=a^2/2-e^2. The factor
1/sqrt(1-exp(-2hD)) is at least one. Also |Theta0(b_j)|<=1. Hence

    ||Pi_D P_U e_j||^2
      >= |Theta0(b_j)|^2 y_j/(10|x_j|)-exp(-2D|x_j|).

The sum diverges by2--3. Apply the Bessel/HS inequality of Section3 to
arbitrarily long prefixes, with the SAME C, to conclude LB6. QED.

Condition2 follows from any polynomial counting bound on the real parts.
The actual R5 entire function has O(R log R) zeros in |z|<=R: the positive
theta representation bounds f and its first six derivatives by
exp(O(R log R)), and Jensen applies since R5(0)=-i lambda f6(0)!=0.
One direct bound is obtained from Phi(t)<=C exp(9|t|/2-pi exp(2|t|))
and the change of variable exp(2|t|); t^j<=j!exp(|t|) handles derivatives.
If y_j<=|x_j|, this disk count bounds the real-part count as needed.

The actual-Xi Bessel bound and weighted native alignment divergence in1
and3 are NOT proved here. Bare height or coprimeness does not supply them;
the CP counterexample has small numerator values and fails the divergent
weighted alignment condition. LB3 is a source-specific sufficient interface,
not a solution of the remaining cofinal problem.

## 5. Finite certificate obligations

The new computation must authenticate the frozen BC/OA sources and rebuild
the fourteen local roots and raw values from the primitive Xi function.
Large-imaginary values use LB3's logarithmic derivative with exact rational
s, ball digamma and zeta-series derivative, avoiding enormous gamma values.
Direct reflected Xi ratios at selected h provide an additional algebraic
route. Every occurrence of b uses its full containing root rectangle.

Only a strict positive lower endpoint of LB2's bracket may contribute a
positive floor. Negative or zero-containing brackets contribute0, not an
optimistically rounded value. The Gram row-sum bound must be outward and
the final trace/norm floors strict rational comparisons. The full declared
grid is retained even when a cell gives no positive bound.

The finite ball results are unconditional evaluations; their Hardy operator
interpretation explicitly assumes innerness. The all-D positivity and LB3
are written analytic arguments. No finite grid certifies their quantifiers.
