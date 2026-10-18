# The cofinal consumer needs feasibility, not an extra uniformity theorem

Status: classical analytic deduction specialized to the theta moment route. The cofinal realization hypothesis is OPEN. This is not claimed as an original general compactness theorem. Newman--Wu (2019), Section 3, Proposition 13 and Theorem 7 give a stronger general Lee--Yang closure framework. The elementary bounded-spin specialization below makes our quantifiers and an explicit convergence bound transparent.

## 1. Automatic common bound from one fixed variance

Let Y be a symmetric, finitely supported random variable whose characteristic function f(z)=E exp(izY) has only real zeros and E Y^2=1. The finite support makes f entire of exponential type. Hadamard factorization, pairing opposite real zeros, gives

    f(z)=product_j (1-z^2/lambda_j^2),
    sum_j 1/lambda_j^2=1/2.

There is no quadratic exponential factor for an exponential-type function. The possible linear exponential factor is zero by evenness and the constant is fixed by f(0)=1. Pairing the genus-one factors is justified by the convergent reciprocal-square zero sum. The variance identity follows by the second derivative at zero.

It follows immediately that, for every complex z,

    |f(z)| <= product_j (1+|z|^2/lambda_j^2) <= exp(|z|^2/2).   (1)

Moreover, expanding the positive product f(-it) gives

    E Y^(2r)/(2r)! <= 1/(2^r r!),                            (2)

because the r-th elementary symmetric sum of positive reciprocal-square zeros is bounded by (sum lambda_j^-2)^r/r!. These bounds are independent of the number of vertices, individual couplings, support diameter and choice of graph.

The zero-weight hub in our model causes no problem: its entire characteristic function still has finite support, symmetry and the real-zero property established by Hurwitz. Each single finite model may have enormous support; normalization by variance is enough for (1).

## 2. Exact finite feasibility at unbounded orders is sufficient

Let mu be an even probability law with an entire characteristic function; use the original standardized theta law here. Suppose there is an unbounded sequence n_j and finite zero-field ferromagnets with nonnegative weighted observables Y_j satisfying

    E Y_j^(2r) = integral x^(2r) dmu(x),  1<=r<=n_j,
    integral x^2 dmu(x)=1.                                (OPEN-FEAS)

No nesting of graphs, common architecture, bounded number of spins, or convergence of the individual couplings is required.

By (2), every target even moment is at most the corresponding Gaussian moment: for each fixed r select j large enough. The entire target characteristic function and every f_j therefore have Taylor coefficients bounded by 1/(2^r r!). On |z|<=R, matching through 2n_j gives the explicit bound

    |f_j(z)-f_mu(z)| <= 2 sum_(r>n_j) (R^2/2)^r/r!.        (3)

For each fixed R this tends to zero. This proves local uniform convergence without any further hypothesis about constants at growing order. Every f_j is zero-free off the real axis; its nonzero limit, normalized at zero, is likewise zero-free there by Hurwitz. For the theta law, the classical Fourier identity then gives RH.

Only the implication is asserted. RH alone is NOT claimed here to imply exact finite ferromagnetic matching at every order. The theorem does not follow from one degree-18 model. OPEN-FEAS is a substantive global construction problem, still unsolved in this packet.

## 3. Approximate feasibility also has a precise form

It suffices more generally that Var(Y_j) remains bounded and, for every FIXED r, E Y_j^(2r) tends to the corresponding theta moment. Apply (1) with the actual bounded variance. The common bound makes the characteristic functions a normal family. Every subsequential entire limit has the target derivatives, hence equals the target entire function. All subsequences therefore have the same limit, and Hurwitz gives the same implication.

Thus one need not solve infinitely many exact constraints in one finite model, nor supply an order-uniform inverse-Jacobian constant. One must actually produce a cofinal family whose moments converge at every fixed order; neither small residuals at a fixed order nor fitted trends establish that premise.

## 4. Consequence for the next research step

The new degree-18 certificate proves strict interior feasibility in one nine-moment projection with every coupling positive. The remaining objective is a general extension theorem or a constructive cofinal family. Splitting an existing component into a coupled pair preserves the finite ferromagnetic setting and provided this pass's extra degree of freedom. Its success at one order does not prove it works indefinitely.

The formulation avoids the numerator/reciprocal distinction and arithmetic averaging-volume loss of the recent 0.9 compositions: it targets the original theta law directly. The difficulty has not vanished; it is now the global ferromagnetic moment-feasibility problem, rather than an unproved claim that finite matching already identifies the entire function.

Primary source: C. M. Newman and W. Wu, *Lee--Yang Property and Gaussian Multiplicative Chaos*, Communications in Mathematical Physics 369 (2019), 153--170, DOI 10.1007/s00220-019-03453-0. Section 1 states the weighted finite-spin theorem; Proposition 13 gives the product and variance identity; Theorem 7 establishes weak closure more generally. The published HTML was read in this pass. No PDF, unpublished theorem, or fresh proof of Lee--Yang is claimed.
