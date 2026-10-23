# Shifted hyperbolic secants preserve trigonometric positivity

2026-10-21. This lemma permits a different real part at each frequency
of the logistic detector. It is independent of any zero-free numerical
certificate.

**Lemma.** For all a,b>=0, the sequence q_k=sech(a+b|k|), k in Z,
is positive definite. Equivalently, every finite matrix
(sech(a+b|j-l|))_(j,l) is positive semidefinite.

Here is a proof retaining the necessary shift a. The infinite product
for cosh, NIST DLMF 4.36.2, gives

    h(s)=sech(sqrt(s))
        =product_(n>=1) [1+4s/((2n-1)^2 pi^2)]^(-1), s>=0.

Each finite product is a Laplace transform of a positive measure
(a convolution of exponential laws). The limit is continuous at zero
with value one, so h is completely monotone. Products of such functions
remain completely monotone, as does multiplication by s^(-1/2).
Consequently

    d/ds tanh(sqrt(s))=h(s)^2/(2sqrt(s))

is completely monotone. The nonnegative function B(s)=tanh(sqrt(s))
is therefore a Bernstein function. The composition theorem for these
functions shows that (1+cB(s))^(-1) is completely monotone for c>=0.
For clarity, it follows also from

    (1+cB(s))^(-1)=integral_0^infinity exp(-t)exp(-ctB(s))dt

and the Laplace-transform property of exp(-rB(s)). The latter follows
from the Bernstein Levy representation by compound-Poisson truncation;
it does not assume complete monotonicity of sech in its original
argument, which would be false near zero.

The hyperbolic addition identity now gives

    sech(a+sqrt(s))
      =sech(a) h(s)/(1+tanh(a)B(s)).                    (S1)

Thus (S1) is completely monotone for every a>=0. By its Laplace
representation, for a finite positive measure nu_a of mass sech(a),

    sech(a+b|x|)=integral_[0,infinity) exp(-r b^2 x^2)nu_a(dr).

Each Gaussian is positive definite on the real line, so their positive
mixture is positive definite; restrict x to the integers to obtain
the lemma. Degenerate a=0 or b=0 follows directly or by continuity.

The precise primary references for the elementary closure steps are
Schilling, Song and Vondracek, *Bernstein Functions*, 2010, Theorem 1.4
(Laplace representation), Corollary 1.6 (products and limits), and
Theorem 3.6 (composition/exponential characterization). The publisher's
preview includes these statements and the proof of Theorem 3.6:
https://api.pageplace.de/preview/DT0400.9783110215311_A15706968/preview-9783110215311_A15706968.pdf .
The product is https://dlmf.nist.gov/4.36.E2 .

## Application to the exact polynomial in this packet

Let P(x) be the degree-12 sum of two squared polynomials in
LOGISTIC_DEGREE12_PRIME_GAIN.md. For any nonnegative a,b, the lemma
implies

    sum_(k=0)^12 a_k sech(a+bk)cos(kx)>=0.              (S2)

Indeed expanding each square expresses the left side as the sum of
two nonnegative quadratic forms in the matrix (q_(j-l)), with the
same positive normalization. This proof uses the actual exact square
representation, so no extra factorization theorem for P is needed.

Take a=(sigma0-1/2)u, b=delta*u, with sigma0>=1/2, delta>=0. For
sigma_k=sigma0+k delta and its own logistic function

    f_k(u)=eta*w(eta*u)/(1+exp(-(2sigma_k-1)u)),

one has exactly

    exp(-sigma_k*u)f_k(u)
       =(eta/2)w(eta*u)exp(-u/2)sech((sigma_k-1/2)u).

Since w>=0, (S2) proves nonnegativity of the combined arithmetic
detector at every integer n, with u=log n. The smoothing functions
are allowed to depend on k; applying each explicit formula separately
and summing is therefore legitimate. This proves positivity only;
the changed zero cutoff, prime lower bound and scalar optimization
must be checked separately.
