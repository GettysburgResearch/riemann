# Independent analytic review of frequency-dependent logistic smoothing

Reviewed:

- ../three-hour-boundary/SHIFTED_SECH_POSITIVITY.md,
  SHA256 2a0143aad2ab349843dc27a0a52ee6cff9a4edc1b41619b9d903901e75a62964.
- ../three-hour-boundary/VARIABLE_SIGMA_LOGISTIC_DETECTOR.md,
  SHA256 b996d3f1ee0e5f674b0fda0f00ec60c90c9d7886e622233ceabfde86541a9f4c.

Scope: independent review of the new analytic interfaces, not a replay
of the new scalar certificate. The older baseline wrapper was my own
contribution; this receipt does not count that portion as independent.
Human review remains outstanding; no RH or fixed-width claim follows.

The shifted-sech positivity proof is correct. The product for cosh at
https://dlmf.nist.gov/4.36.E2 gives complete monotonicity of
h(s)=sech(sqrt(s)). The derivative h(s)^2/(2sqrt(s)) is completely
monotone, so tanh(sqrt(s)) is a Bernstein function. The composition
and Laplace closure statements in the cited Schilling--Song--Vondracek
preview apply, including at zero by continuity. The addition formula
therefore gives a positive Gaussian-mixture representation of
sech(a+b|x|). This proves the required finite Toeplitz positivity.
It is not the false claim that sech(x) itself is completely monotone.

Applying that matrix to the actual two integer square polynomials
proves arithmetic positivity at every prime power. The normalization
includes q0=sech((sigma0-1/2)u); it does not silently replace this by 1.
All f_k(0) still equal eta*w0/2. Consequently the gamma terms have the
same common prefactor even though the kernels differ for u>0.

For the retained prime terms, |sech'|<=1/2 gives coefficient
eta*w/4<=3eta/2. Multiplying by k*delta*u and Lambda(p^m)=log p
produces the stated m*(log p)^2*p^(-m/2) sum, so the loss
168eta*delta follows from the two displayed strict finite bounds.
All unretained prime powers remain nonnegative by Toeplitz positivity.

For each k>=1, log(k+.01)<c+kd implies the actual cutoff condition
sigma_k>=1-B/log(kt+T0). With the global minimum property and the
verified low zeros, this puts every retained zero in its own positivity
strip. The selected pair is retained for k=1. The k=0 cutoff is below
H, and its retained zeros lie on the critical line. Every omitted
real argument is in [-eta,alpha_k+eta] because sigma_k>=1-eta.
Thus the uniform far-zero estimate applies with the individual cutoff.
The baseline Lehman calculation already uses the enlarged integration
range starting at kt+T0, so no common Kt cutoff is being assumed here.

I checked the explicit-formula signs. F_0 supplies the zero-frequency
pole; F_1 supplies the isolated pair. Their separate alpha values in
(V4) are correct. The negative E_0 and retained-prime lower bound are
distinct favorable terms. The existing 10^(-7) remainder budget remains
valid since every sigma_k and eta stays in the old analytic range and
the coefficient sum stays below four. The minimum-zero localization
has the same logic with the separately checked enlarged endpoint.

Verdict: no defect found in these analytic interfaces. A global R=4.813
claim additionally needs the independently replayed full scalar
rectangle and a binding assembly review. This receipt supplies neither
an empirical zero census nor a substitute for the imported theorems.
