# Renormalization before Poisson: a simultaneous two-scale dilation

Status: PROPOSED exact adapter, not a new theta estimate. The initial-line
Euler identity and the finite physical operation are proved here. New
nonprincipal contour estimates and a signed power saving remain OPEN.
Source: Cureton--Thorner v1, equations labeled eq:probe and the triple Mellin
formula in Section 11. The v1 text was directly reread in this pass. #948
records the same structural interface for v2; no v2 body was freshly retrieved.
The v1 numerical parameters are NOT substituted for the v2 parameters.

## 1. The actual three-scale average and its finite support

Use the paper's S-integer ring R, allowed ideal generators, norm-one compact
quotient F_S^1/Gamma, and fixed weights W0 and W1. Its average is

    I(X,Y,Z)=integral_t (1/Y) sum_s W1(Ns/Y)/(Ns sqrt(X))
        sum_(m in R, m!=0) g_s(-m)
             W0(m/(t ell_(Ns X))) B_m(Z) dt.              (1)

In particular X is the physical additive-row scale, Y the denominator scale,
and Z the theta coefficient scale. The sextic characters in B_m and g_s keep
all nonunit zeros. No coprimality between s and the theta index is assumed.

Suppose the positive norm support of W0 is contained in [a0,b0], and that
of W1 in [a1,b1], and put B=b0*b1. The norm of every nonzero m in R is the
positive integer norm of its exterior integral ideal, so |m|_S>=1.
Whenever a summand is nonzero, |m|_S<=b0 Ns X<=BXY. Therefore

    I(X,Y,Z)=0 if BXY<1,                                 (2)

for every Z>0. The compact norm-one quotient does not change this inequality.
The theta series has infinite Gaussian support but the physical m-sum does
not. The integer-valued exterior norm, rather than a norm-only ball in a
positive-unit-rank number field, is being used here.

## 2. The simultaneous dilation that isolates the reciprocal variable

On the paper's initial absolute-convergence lines, its triple Mellin
integrand has the scale monomial

    X^(1/2-z) Z^(xi+z-1) Y^(w-1).                        (3)

The exact identity

    (X/q^6)^(1/2-z) (Z/q^6)^(xi+z-1)
      =X^(1/2-z) Z^(xi+z-1) q^(3-6xi)                   (4)

has NO residual z or w dependence. Thus define the physical dilation

    (T_d I)(X,Y,Z)=I(X/(Nd)^6,Y,Z/(Nd)^6).                (5)

It multiplies the whole frequency series by (Nd)^(3-6xi), not merely its
principal specialization. Dilation of Z alone gives the WRONG multiplier
(Nd)^(6-6xi-6z). Dilation of Y too changes the nonprincipal w variable.

Let eta be the actual phase in the principal correction, and define

    h_eta(d)=mu_F(rad(d)) eta(d) phi_F(rad(d))/(Nd),
    phi_F(rad(d))=product_(p|d)(Np-1),  h_eta(1)=1.        (6)

Then |h_eta(d)|<=1 and

    sum_(j>=0) h_eta(p^j) q^((3-6xi)j)
          =(1-eta(p)q^(3-6xi))/(1-eta(p)q^(2-6xi)).       (7)

**Theorem 1.** The geometrically renormalized average

    Ihat(X,Y,Z)=sum_d h_eta(d) I(X/(Nd)^6,Y,Z/(Nd)^6)     (8)

is a LITERAL FINITE SUM: only (Nd)^6<=BXY contribute. On the initial
triple Mellin lines it inserts the product of (7) in front of EVERY frequency
u. Its principal double residue has exactly the numerator Hhat of
MATHEMATICS.md, not H or the once-stripped numerator.

Proof. Finiteness is (2). For the analytic identity, the product of (7)
and its Dirichlet series are absolutely convergent for Re(xi)>2/3; the
paper starts much farther right. The sum of absolute scale multipliers is
bounded by sum_d (Nd)^(3-6 Re(xi)), since |h_eta|<=1. This converges and is
independent of imaginary parts. The source's absolute convergence and
rapid Mellin decay justify Fubini. Equation (4) gives the multiplier and
(7) its local Euler product. Multiplication of a meromorphic integrand by
a factor independent of w,z commutes with the principal residues at
w=1,z=1/6. Algebra (1)-(3) in MATHEMATICS.md identifies their numerator.
No new contour move or bound on the other residues is asserted. QED.

The once-stripped version replaces h_eta(d) by mu_F(d)eta(d). It has the
same finite physical cutoff, and inserts product_p(1-eta(p)q^(3-6xi)).
This supplies an exact pre-Poisson realization of the earlier formal
normalization, rather than applying a signed dilation only to its final
one-variable inequality.

## 3. Common primes and moving rows must remain

Each term of (8) uses the actual row domain of X/(Nd)^6. It does not replace
that domain by the one at X. All Gauss sums and theta coefficients retain
the original m in that term. In particular (8) introduces NO condition
(d,s)=1, (d,m)=1, or (d,theta index)=1.

A change of variables m'=d^6 m would require explicit new local formulas:
when p|d, a unit m can have chi_p(m)!=0 while chi_p(m')=0. The analogous
prime-modulus additive Gauss sum at frequency zero vanishes, whereas at a
unit frequency it does not. These are genuine common-prime terms, not an
inessential normalization. The checker tests the literal sextic mask failure.
The exact adapter avoids deleting them; it does NOT yet evaluate them into
a new reflected quadratic-sieve estimate.

Likewise the old fixed-curve estimate cannot be inserted termwise into (8).
If X=Z^alpha,Y=Z^beta and Z'=Z/(Nd)^6, then

    [X/(Nd)^6]/(Z')^alpha=(Nd)^(-6(1-alpha)),
    Y/(Z')^beta=(Nd)^(6beta).                             (9)

Except at d=1 these leave the original curve. A same-source estimate at
these off-curve scales is a separate requirement, not supplied by #948's
seven-parameter reconstruction.

## 4. The principal Gaussian and why the residual cannot be dropped

Write

    G_H(Z)=(1/(2pi i)) integral_(2)
             Z^s exp((s-5/6)^2) H(s)/zeta_F^S(s) ds.

The principal double residue of I is

    c0 X^(1/3) Z^(-5/6) G_H(Z),                          (10)

where c0 is the same fixed nonzero residue constant as in the source.
Thus the principal part of (8) is the same prefactor times

    Ghat(Z)=sum_d h_eta(d)(Nd)^3 G_H(Z/(Nd)^6)
      =(1/(2pi i)) integral_(2)
          Z^s exp((s-5/6)^2) Hhat(s)/zeta_F^S(s) ds.      (11)

The sum in (11), unlike (8), is INFINITE. It converges absolutely because
the Gaussian inverse Mellin source is flat at zero, obtained by moving its
initial line arbitrarily far right. Initial-line Fubini proves the identity.
No theorem for finite-order eta, or zero-free continuation of an isolated
angular L-factor, is used.

For example, define the exact residual R=I minus (10). Then linearity and
(11) give Ihat=c0 X^(1/3) Z^(-5/6) Ghat+Rhat, with Rhat=sum_d h_eta(d)T_d R.
Outside the finite row cutoff, T_d I=0 but the principal term usually is not
zero: that principal tail is cancelled by the residual. Defining R by this
identity gives NO estimate for it. To use a contour-defined nonprincipal
residual, one must retain the actual frequency terms and their domains.
A small error known only on the old fixed scale curve cannot be substituted.

The explicit remaining scalar estimate is

    Ghat(Z)=O_epsilon(Z^(1/2+epsilon)) for every epsilon>0. (OPEN-G)

Together with its zero-side flatness, Mellin holomorphy and Theorem 1 of
MATHEMATICS.md would exclude zeros to the right of 1/2. This is the same
outstanding arithmetic strength, not a weaker problem obtained by notation.
The direct alternative is OPEN-LIFT for the source in (5) of that file,
with the full inherited test/twist/height requirements.

The productive next bound must act on the coupled d,m,theta-index sum in
(8), or on the signed injection minus compensation, BEFORE separate absolute
values. This packet proves the exact initial-line/physical adapter and the
constant-cost source comparison; it does not prove that signed bound or the
new nonprincipal contour domains.
