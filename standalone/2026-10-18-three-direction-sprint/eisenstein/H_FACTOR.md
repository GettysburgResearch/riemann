# The physical correction is one shifted angular L-function times a controlled inverse

Status: **PROPOSED component theorem; independent review required.** This
isolates the exact numerator obstruction. It does not bound the physical
average or exclude a new zeta zero.

Fix one field F satisfying the CT mu_12 interface, its fixed S and its actual
correction vartheta. At an exterior prime P, Q=NP and a= vartheta(P)^6.
The pinned CT source, `eq:principal-factor`, gives

    H_P(s)=(1-Q^(-2))
       [1-(1-Q^(-1))Q^(-s)-a Q^(2-6s)]
            /[(1-a Q^(3-6s))(1-Q^(-s))].                 (1)

Set kappa=vartheta^6. It is a unitary Hecke character, unramified outside
the same fixed S. Its angular order at every complex place is +6 or -6,
since vartheta has order +1 or -1 there. Thus kappa is nonprincipal and
cannot be a pure imaginary norm twist. Its Hecke L-function is entire.

## 1. The exact factorization and its continuation

Define

    R_P(s)=(1-Q^(-2))
       [1-(1-Q^(-1))Q^(-s)-a Q^(2-6s)]/(1-Q^(-s)),
    R_reg(s)=product_(P outside S) R_P(s).               (2)

Then initially for Re s>2/3,

    H(s)=L_F^S(6s-3,kappa) R_reg(s).                    (3)

The product R_reg is holomorphic, nonzero, and has a holomorphic inverse
on the larger half-plane Re s>1/2. Indeed write r=Q^(-1), X=Q^(-s) and
E=a Q^(3-6s). The local numerator is 1-(1-r)X-rE. For Re s>1/2,

    |(1-r)X+rE| < (1-r)Q^(-1/2)+r <1.                 (4)

All local denominators are nonzero. Direct subtraction in (2) gives

    R_P(s)-1=O_(sigma0)(Q^(-2)+Q^(-1-sigma0)+Q^(2-6sigma0))

uniformly on Re s>=sigma0>1/2. Every exponent is strictly less than -1.
Normal convergence and a convergent logarithm prove the assertions about
R_reg and its inverse. Formula (3) therefore continues H holomorphically
to Re s>1/2. Its only zeros there are precisely the shifted zeros of the
one fixed angular L-function, with their multiplicities unchanged.

This refines the statement that H is zero free for Re s>2/3: there the
argument 6s-3 of L lies in its absolute Euler domain. Below 2/3 it is not
legitimate to discard that L-factor or assume its zeros do not coincide
with target zeros.

## 2. A quantitative Dirichlet-algebra bound, including the critical cost

For an ideal Dirichlet series A(s)=sum_I a(I)(NI)^(-s), write

    ||A||_sigma=sum_I |a(I)|(NI)^(-sigma).

Both R_reg and its inverse belong to this algebra for every sigma>1/2.
More precisely there is a constant C_(F,S) such that, uniformly for
1/2<sigma<=3/4,

    ||R_reg||_sigma+||R_reg^(-1)||_sigma
          <= C_(F,S) zeta_F^S(6sigma-2)
          <= C'_(F,S)/(sigma-1/2).                     (5)

Here the second inequality uses only the ordinary simple pole and positive
residue of the fixed Dedekind zeta function at one.

Proof. Remove the fixed constant product product_P(1-Q^(-2))=1/zeta_F^S(2)
and call the remaining local factor r_P. Put

    x=Q^(-sigma), u=Q^(-1)x, v=Q^2 x^6=Q^(-(6sigma-2)).

The local power series in X are

    r_P=1+[Q^(-1)X-a Q^2 X^6]/(1-X),
    r_P^(-1)=1+[-Q^(-1)X+a Q^2 X^6]
                           /[1-(1-Q^(-1))X-a Q^2 X^6]. (6)

The geometric-series absolute majorants give

    ||r_P||_sigma<=1+(u+v)/(1-x),
    ||r_P^(-1)||_sigma<=1+(u+v)/(1-x+u-v).              (7)

The second denominator is positive uniformly down to sigma=1/2. In fact
its minimum over Q>=2,sigma>=1/2 is at least
d0=(2-sqrt(2))/4>0: write t=Q^(-1/2)<=1/sqrt(2) and note that
1-t-t^2+t^3 is decreasing on that interval. One can also differentiate
t+t^2-t^3 directly to obtain this bound.

Multiply each bound in (7) by (1-v). In the first case its difference
from one is at most (u+vx)/(1-x); in the second it is at most
(u+vx)/(1-x+u-v). Since u<=Q^(-3/2), vx<=Q^(-3/2), both are
O(Q^(-3/2)) uniformly in sigma. Consequently

    (1-v)||r_P^(+/-1)||_sigma <=1+C Q^(-3/2).           (8)

One may take C=14: d0>1/7 and 1-1/sqrt(2)>1/7. The product of the right
sides is at most zeta_F^S(3/2)^14, since 1+14x<=(1-x)^(-14). The product
of (1-v)^(-1) is exactly zeta_F^S(6sigma-2). Restoring the fixed constants
zeta_F^S(2) and its inverse proves (5), with the completely explicit choice

    C_(F,S)=[zeta_F^S(2)+1/zeta_F^S(2)] zeta_F^S(3/2)^14.

All infinite Euler tails are included.

## 3. A complete causal inverse with all Lp horizons

Let r(I),r_inv(I) be the Dirichlet coefficients just constructed. For any
source A with finite weighted past norm, every 1<=p<=infinity, T>0 and
sigma>1/2, Minkowski and positive rational dilations give

    ||sum_I r^(+/-1)(I) A(D/NI)||_(sigma,p,T)
           <=||R_reg^(+/-1)||_sigma ||A||_(sigma,p,T).  (9)

The series converges in that norm, and the two operators are inverse on
the same past horizon by absolute convolution. No unproved reciprocal
Hecke estimate occurs in (9). In particular the regular correction can be
removed at cost O((sigma-1/2)^(-1)); only the shifted angular factor in (3)
survives. Physical detectors with a fixed Mellin shift must first undo
that displayed power of D when selecting the norm sigma.

This proves more than pointwise nonvanishing of a formal Euler product:
the exact whole correction and its inverse have a complete resource for
causal source estimates arbitrarily near the critical line.

## 4. A conditional zero-chain lemma and its exact limitation

This paragraph is conditional and is NOT an imported theorem about CT's
existing target class. Fix kappa as above and suppose one has a family of
unitary target characters omega closed under omega -> kappa omega^6,
including omega=1, with holomorphic quotient detectors

    L(6s-3,kappa omega^6) R_omega(s)/L(s,omega)

on Re s>theta, where theta>=1/2 and every R_omega is holomorphic and
nonzero on Re s>1/2. No uniformity of constants over omega is needed, but
the SAME exponent theta is required for every fixed member used.

Then L(s,1) has no zero with

    Re s>max(theta,3/5).                                (10)

For a zero rho_0 with beta_0>3/5, holomorphy of the quotient forces a zero
rho_1=6rho_0-3 of the next target; its real part exceeds beta_0. Repeating,

    beta_j=3/5+6^j(beta_0-3/5),

eventually places a zero in Re s>1, contradicting absolute Euler
convergence. All intermediate detectors are used only inside their assumed
holomorphic region. If an intermediate point is one, the quotient identity
still forces the next zero and gives the same contradiction; a target pole
cannot be a zero.

Starting from omega=1, the formal target chain is
omega_j=kappa^((6^j-1)/5). Its finite conductor remains supported on fixed
S; its archimedean order grows. The native correction vartheta_0 omega_j
has angular order +/-(6^(j+1)-1)/5, hence remains nontrivial. However the
existing source fixes a FINITE-ORDER eta and theta profiles of angular
order +/-1; extending its complete analytic bounds to this chain requires
proof. Equation (10) is only the logical consequence if that missing input
is obtained.

The functional equation can alternatively reflect the forced zero to real
part 4-6beta. This increases beta only for beta<4/7. The interval
[4/7,3/5] therefore cannot be eliminated just by a claim that one of these
two one-step moves always pushes right. No RH conclusion follows from this
zero-chain observation. CUBE_TILT.md describes a different, exact arithmetic
deformation intended to move the shifted angular factor itself.
