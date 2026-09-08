# Sharpness: positive heat is not real-rootedness

Status: PROPOSED PROVED COUNTEREXAMPLES AND A COMPACTNESS THEOREM;
independent review required. None is a counterexample to RH for actual zeta.
Scope: exact polynomial models, a source-explicit finite perturbation of Xi,
and a general finite-exterior approximation theorem.
Dependencies: the normalization and count bound in HEAT_BERNSTEIN.md;
classical analytic compactness/Hadamard facts as stated below.
What was run: exact rational polynomial and Hausdorff controls.
Smallest remaining gap: no approximating positive contractions for actual X
have been constructed; the mixed Hausdorff inequalities remain open.

## 1. All logarithmic derivative signs can hold with nonreal zeros

**Proposition ASTRA-TC-09.** The positive-coefficient polynomial

    F(u)=(1+u)(1+4u/5+u^2/5)
        =(1+u)((u+2)^2+1)/5                                  (1)

has nonreal zeros -2+i and -2-i, but log F is a Bernstein function on u>=0.
In particular F'/F is completely monotone at every order and every u>=0.

Proof. Its logarithmic derivative is the Laplace transform of

    S_F(t)=exp(-t)+2 exp(-2t) cos(t).

This is positive for 0<t<=pi/2 because cos(t)>=0. For t>=pi/2>log 2,
exp(-t)>2 exp(-2t), so it remains positive. Integrating gives the positive
Levy density S_F(t)/t. The nonreal roots are explicit in (1).

At v=1, P(z)=F(z)/F(1) has exact probability coefficients

    (1/4, 9/20, 1/4, 1/20).

Its logarithmic power coordinates are

    p_n^* = 2^(-n) + w_n,
    w_0=2, w_1=3/5,
    w_n=(3/5)w_(n-1)-(1/10)w_(n-2).

Although EVERY p_n^*>0 by the preceding analytic proof, the mixed
Hausdorff expression defined in THETA_COUNT.md satisfies exactly

    H_(0,14) = -433316717939/1000000000000000 < 0.             (2)

The checker reconstructs (2) both by this root-free recurrence and by
formal logarithms of the displayed PGF. This is a finite exact counterexample
at a specific mixed order, not evidence extrapolated to infinity.
It rules out promotion of the all-order result ASTRA-TC-04 to RH.

## 2. Preserve a positive smooth Xi source and insert an explicit quartet

The polynomial example could be dismissed because its source is not a theta
Fourier density. The following construction retains a much stronger list of
properties, with explicit uniform source positivity.

Set R=1000 and delta=1/4, and define the even polynomial

    Q(z)=1-alpha z^2+beta z^4,
    alpha=2(R^2-delta^2)/(R^2+delta^2)^2,
    beta=1/(R^2+delta^2)^2.                                   (3)

Its zeros are exactly +R+i delta, +R-i delta, -R+i delta, -R-i delta.
Put

    Xi_tilde(z)=Xi(z) Q(z),
    Phi_tilde=Phi+alpha Phi''+beta Phi''''.                    (4)

Fourier integration by parts proves that Phi_tilde is the actual Fourier
source of Xi_tilde. It is not a source chosen from an unproved zero set.

**Theorem ASTRA-TC-10.** This explicit source satisfies

    Phi_tilde(tau) > (9999/10000) Phi(tau)>0,   every real tau. (5)

The function Xi_tilde is real even and entire of order one. Every zero lies
in |Im z|<1/2; its zero set and multiplicities below ordinate 100 are exactly
those of Xi. It has the four explicit nonreal zeros in (3). Its upper zero
count differs from zeta's by exactly two once T>=1000, counted with
multiplicity, even if a new point coincides with an old zero. Thus the usual
zero-count asymptotic is preserved up to O(1).

Proof of (5). For one theta atom use x=pi m^2 exp(2 tau) and g=exp(tau/2-x).
Let P_0(x)=4x^2-6x and let

    Dcal P = 2x P'(x)+(1/2-2x)P(x).

Then Phi^(k)(tau)=sum_m P_k(x_m)g_m, where P_k=Dcal^k P_0. Exact expansion gives

    P_2=16x^4-112x^3+165x^2-(75/2)x,
    P_4=64x^6-1056x^5+5176x^4-8512x^3
                                  +(15465/4)x^2-(1875/8)x.    (6)

For x=y+3 with y>=0,

    P_2+20P_0 = 16y^4+80y^3+101y^2+(33/2)y+9/2 >= 0.

Also

    P_4(y+3)=64y^6+96y^5-2024y^4-6880y^3
                         -(2391/4)y^2+(142233/8)y+108585/8.

On 0<=y<=17 the negative part is at most

    2024*17^4+6880*17^3+(2391/4)*17^2=812082775/4.

Since P_0(y+3)>=18, this proves P_4>=-20000000 P_0 on 3<=x<=20.
For x=20+y, all seven coefficients of P_4 are positive; in ascending order:

    [2956811625/2, 4316576125/8, 324142185/4,
     6421568, 283576, 6624, 64].

Thus for EVERY x>=3,

    P_2>=-20P_0,       P_4>=-20000000 P_0.                    (7)

Every atom at tau>=0 has x>=pi>3, so (7) gives

    Phi_tilde >= (1-20alpha-20000000beta) Phi.

Because alpha<2/R^2 and beta<1/R^4, the coefficient is greater than
1-40/10^6-20000000/10^12=0.99994>9999/10000. Evenness extends this to all tau.
Smoothness and superexponential decay follow from the differentiated theta
series. The remaining zero and order statements follow from multiplication
by the explicit even polynomial Q. No zeros can be cancelled by multiplication.

The corresponding invariant function is

    X_tilde(u)=X(u)[1+alpha(u+1/4)+beta(u+1/4)^2].              (8)

It has strictly positive coefficients and order at most 1/2. Its value at
zero is positive, but is NOT 1/2; use its own value in normalizing a PGF.
The two extra invariant a parameters are

    R^2+3/16 + iR/2,       R^2+3/16 - iR/2.

## 3. The counterfeit also satisfies the entire Bernstein layer

**Corollary ASTRA-TC-11.** The logarithmic derivative X_tilde'/X_tilde is
strictly completely monotone. Its invariant zero heat is positive for every
t>0, with the same lower bound (6) in HEAT_BERNSTEIN.md. Every logarithmic
factorial-cumulant coordinate of its normalized count has the same positive
lower bound as the actual count. Nevertheless it is NOT Poisson-binomial,
and at least one of its mixed Hausdorff inequalities fails.

Proof. For T>=100 the enlarged upper zero count obeys

    N_tilde(T)<=4T^(3/2)+2<=T^2.

The last inequality follows from 4/sqrt(T)+2/T^2<=0.4002<1.
The finite prefix V100 and the zero between 14 and 15 are unchanged. The
inserted quartet has centered imaginary displacement 1/4, so (1) of
HEAT_BERNSTEIN.md still holds. The SAME all-time heat proof therefore applies
without any tail or derivative extrapolation. Apply ASTRA-TC-04 and the
one-scale Hausdorff equivalence. The explicit nonreal quartet precludes
Poisson-binomiality.

This example preserves positive smooth Fourier source, reflection, order,
critical-strip confinement, finite-prefix verification, zero-count asymptotic,
and the entire proved Bernstein layer simultaneously. It does NOT preserve
the original Euler product, exact theta-lattice differential polynomial, or
all arithmetic explicit-formula data. Those distinctions are potential
sources of the missing theorem, not dispensable decoration.
The result refutes a class of proposed shortcuts, not RH and not the
possibility of a genuinely arithmetic positive realization.

## 4. Finite exterior approximants need no separately assumed consistency

A different attempted construction was to match increasingly many exterior
coefficients with finite positive contractions. The following theorem removes
one unnecessary interface from that programme, while leaving existence open.

**Theorem ASTRA-TC-12 (no-Poisson-escape compactness).** Let F be entire of
order strictly less than one, with F(0)=1. Suppose K_m are positive
trace-class contractions, possibly on unrelated Hilbert spaces, with
Tr K_m<=C. Suppose each fixed Taylor coefficient of det(I+y K_m) converges
to the corresponding coefficient of F. Then there exists a positive
trace-class contraction K such that

    F(y)=det(I+yK).                                           (9)

No compatible embeddings or nested compressions are required.

Proof. Positivity bounds the nth exterior coefficient by C^n/n!, so the
coefficient convergence gives locally uniform convergence of the entire
determinants. List the eigenvalues decreasingly, padding by zero. Then
0<=k_(m,j)<=min(1,C/j). Along a diagonal subsequence each converges to k_j,
and the traces converge to T<=C. Fatou gives sum_j k_j<=T. Write

    a=T-sum_j k_j>=0.

On |y|<=1/2, the difference between the logarithm of a tail product and its
linear term is bounded by 2|y|^2 sum_(j>J) k_(m,j)^2
<=2|y|^2 C^2/(J+1), uniformly in m. Pass first in m, then in J, obtaining

    F(y)=exp(a y) product_j (1+k_j y).

Both sides are entire, so equality holds globally. If a>0, F(r)>=exp(ar)
on the positive ray, contradicting order less than one. Hence a=0 and the
diagonal operator with eigenvalues k_j proves (9).

Exact matching through degree m automatically gives the trace bound as soon
as degree one is matched: Tr K_m=F'(0). For actual F(y)=P_v(1+y), whose order
is at most 1/2, finite exterior feasibility at every degree would therefore
already imply RH. Projective consistency is not an additional open premise.
Feasibility itself is NOT supplied by this theorem or by ASTRA-TC-04.

The order condition cannot be deleted. K_m=I_m/m has trace one, while

    det(I+yK_m)=(1+y/m)^m -> exp(y).

All eigenvalues escape individually to zero and the limiting trace survives
as a Poisson factor. The checker verifies its finite coefficient formula;
the displayed limit is the analytic argument. This compactness mechanism is
classical in substance, and no external priority is claimed.
