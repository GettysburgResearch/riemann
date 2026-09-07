# Conditional ending: what a work upper bound would prove

Status: CONDITIONAL IMPLICATION ONLY. The hypothesis below is NOT proved.
This restates the frozen parent argument so a reviewer can see the complete
logical chain. It is not evidence that the missing hypothesis holds.

Assume there is an unbounded sequence X_j such that

    log(1+max(W(X_j),0))/log X_j -> 0.                  (H)

Theorem EFB26.T1 gives E(X_j)=X_j^o(1). Here the log-log remainder is harmless,
and negative W causes no difficulty because E is nonnegative.

Suppose a nontrivial zeta zero rho=beta+i gamma has beta>1/2 and multiplicity m.
Choose one fixed sigma with 0<sigma<beta-1/2, put alpha=1/2+sigma,
lambda=rho-alpha and delta=Re lambda>0. The original factorial source is

    d_alpha(t)=exp(-alpha t)[floor(exp t)(1-t)+log(floor(exp t)!)],
    D_alpha(z)=(z+alpha-1)zeta(z+alpha)/(z+alpha)^2.

It belongs to L1 and L2, since 0<exp(alpha t)d_alpha(t)<=1+t. Its transform
identity follows first from the floor-function integral in Re(z+alpha)>1
and then by analytic continuation. The apparent pole at z+alpha=1 is removed.

Let h_X(z)=log A_X(1/2+z), using its analytic real-axis-normalized logarithm.
The finite approximants are outer on Re z>0, with O_X(1/|z+1/2|) Hardy bound;
these elementary finite-Euler facts and their proof are in parent PROOF, §1.
Their signed Poisson mean and positive cost imply

    (1/pi) integral |Re h_X(iy)|/(1+y^2)dy <=2E(X)+3.

The differentiated Schwarz formula and a fixed inward shift give

    Q_X(z)=h_X'(z+sigma)/(z+1)^3 in H2,
    ||Q_X||_H2 <=(2+2/sigma^2)(2E(X)+3)/sqrt(2).        (1)

For example, the kernel bound
(1+t^2)/[x^2+(y-t)^2]<=(2+2/sigma^2)(1+y^2), x>=sigma,
followed by integration of 1/(1+y^2), proves (1) with the Hardy normalization
||Lf||^2=(1/(2pi)) integral |Lf(iy)|^2dy. No sigma=0 limit is used.

The logarithmic derivative is the transform of the explicit signed measure

    [exp((1-alpha)t)1_[0,log X](t)-2exp(-alpha t)]dt
      -sum_(p<=X,k>=1)log(p)p^(-k alpha)delta_(k log p).

Convolve it with w(t)=t^2 exp(-t)/2 to obtain q_X in L2. Set

    y_X=d_alpha*q_X,      f_alpha=-w*(t d_alpha).

Then Y_X=D_alpha Q_X, F_alpha=D_alpha'/(z+1)^3, and
||y_X||<=K_alpha ||Q_X||, where K_alpha=1/alpha+1/alpha^2.
Causal Laplace uniqueness, initially in the absolute Euler half-plane, shows
that y_X=f_alpha before log X. Indeed the finite signed measure agrees there
with the inverse transform of D_alpha'/D_alpha, including every prime power.
Thus e_X=y_X-f_alpha is supported after L=log X and

    ||e_X|| <=C_(alpha,sigma)(1+E(X)).                 (2)

At lambda, Y_X vanishes through order m-1 whereas F_alpha vanishes only
through order m-2. For e_L(u)=e_X(u+L), all derivatives below m-1 of Le_L
at lambda vanish, and

    (Le_L)^(m-1)(lambda)
          =-exp(L lambda)D_alpha^(m)(lambda)/(lambda+1)^3.

Testing directly against u^(m-1)exp(-conj(lambda)u) gives

    ||e_X|| >=
      |D_alpha^(m)(lambda)| (2delta)^(m-1/2)
      /[|lambda+1|^3 sqrt((2m-2)!)] * X^delta.         (3)

The constant is positive because rho has exact order m. The parent supplies
a stronger Laguerre constant; this simpler nonzero bound suffices. Lower jets
vanish, so multiplication by exp(Lz) introduces no unwanted powers of L.
Equations (2)-(3) contradict (H) along its unbounded sequence. Reflection
then rules out zeros to the left of 1/2 as well, establishing RH CONDITIONAL
on (H). The previously identified source domains would consequently be full.

No phase averaging, zero simplicity, finite zero prefix, or new Hilbert metric
is used in this conditional ending. The only unsupplied assertion is (H),
which is a central arithmetic estimate, not a technical step for a referee.
PROOF and ATTEMPT do not prove (H). There is no completed RH proof in this pass.
