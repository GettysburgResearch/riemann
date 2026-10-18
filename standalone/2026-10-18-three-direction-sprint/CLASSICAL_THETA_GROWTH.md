# The variance-sharp theta growth bound and its precise imported premise

Status: **PROPOSED elementary consumer of a classical theta-kernel theorem.**
This is a useful quantitative complement to theta/THETA_GROWTH.md. It is
not a new assertion about the location of the zeros of xi. The native
strong-log-concavity proof in that file remains a separate, self-contained
way to obtain a slightly larger growth constant.

Let T have the actual symmetric normalized theta density, with variance v,
and let Y=T/sqrt(v). The classical imported premise is that its even
potential V=-log density has V' convex on [0,infinity). This property is
asserted for the Riemann theta kernel in the primary publisher abstract of
C. M. Newman, [The GHS inequality and the Riemann hypothesis (1991)]
(https://link.springer.com/article/10.1007/BF01888165).
Newman's displayed Fourier variable uses a positive linear rescaling of
the theta variable. Such rescaling preserves the premise. The full article
was not available in this session; the premise is an explicitly imported
classical result, not a newly checked proof of the kernel inequality.

The related primary result of Ellis, Monroe and Newman,
[The GHS and other correlation inequalities for a class of even
ferromagnets (1976)](https://link.springer.com/article/10.1007/BF01608495),
provides the general context. The short one-variable argument below avoids
importing a general many-site correlation theorem.

## An elementary two-copy proof

Suppose an even smooth potential V has V'' even and nondecreasing on the
positive half-line, with enough decay to justify the following
differentiations. Convexity of V' is exactly the required monotonicity of
V'' there. The actual theta density and all its real exponential tilts
have the requisite superexponential decay.

Write E_h for expectation under density proportional to exp(hx-V(x)).
Take independent copies X,X' with this tilted law and put

    U=(X+X')/2, W=(X-X')/2.

Their joint density is proportional to

    exp(2hU-V(U+W)-V(U-W)).

Consequently g(u)=E[W^2 | U=u] does not depend on h. It is even. For
u,w>=0 the derivative in w of the derivative in u of the conditional
potential is

    V''(u+w)-V''(u-w)>=0,

since |u+w|>=|u-w|. Thus the even function
V'(u+w)+V'(u-w) is nondecreasing in |w|. Differentiating the conditional
expectation gives

    g'(u)=-Cov(W^2,V'(u+W)+V'(u-W) | U=u)<=0.

The last sign follows directly from the covariance identity for two
nondecreasing functions of the same real variable. This proves that g is
nonincreasing on [0,infinity).

Independence of X,X' gives Var_h(X)=2 E_h g(U). Differentiate with
respect to h, retaining the factor 2 in the density of U:

    d Var_h(X)/dh = 4 Cov_h(g(U),U).

Conditional on R=|U|, the even untilted U-density implies

    E_h[U | R]=R tanh(2hR).

For h>=0 this is nondecreasing in R, while g(R) is nonincreasing. Hence
the covariance is nonpositive. The tilted variance is at most its value v
at h=0. If K(h)=log E exp(hT), then K''(h)<=v, K(0)=K'(0)=0, and therefore

    E exp(hT)<=exp(v h^2/2),
    E exp(hY)<=exp(h^2/2),                 h real.

By taking the absolute value inside the Fourier integral, the standardized
entire characteristic function satisfies the sharper complex bound

    |F_Y(z)|<=exp((Im z)^2/2)<=exp(|z|^2/2).

This is an unconditional growth estimate once the stated classical kernel
premise is imported. It supplies the target constant B=1/2 in the
quantitative complex-disk consumer of theta/THETA_GROWTH.md. It supplies no
approximants, no zero-strip theorem for an approximant, and no cofinal
moment-feasibility result. Those remain separate mathematical tasks.
