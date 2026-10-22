# The unsolved bridge is identification of Xi, not a decimal comparison

**OPEN for the actual source.** The results below are conditional consumers
and stability lemmas; their hypotheses are not claimed established.
Let X(z)=xi(1/2+iz)/xi(1/2). It is real even, X(0)=1. Use only functions
F_a from Theorem R at tau=0, with a legal kappa for each actual interval,
or finite functions licensed by PROOF.md Section 4. No zero table is an
input to their construction.

## 1. Ordinary normality

An even real entire function F of exponential type with only real zeros
and F(0)=1 has the paired Hadamard product

    F(z)=product_j (1-z^2/x_j^2),   x_j>0,
    V=-F''(0)=2 sum_j x_j^(-2),
    |F(z)|<=exp(V|z|^2/2).                                         (10)

Multiplicities are retained. The exponential-type condition excludes a
quadratic exponential factor; evenness removes the linear one. The paired
zero series converges absolutely. Thus bounded V gives normality.
If all fixed Taylor coefficients tend to those of X along a cofinal sequence
and V stays bounded, Montel, the identity theorem and Hurwitz prove RH.
Neither the uniform bound nor the cofinal coefficient matching follows
from positivity of each shifted form.

The exact coefficient being asked for is

    (-1)^m F_a^(2m)(0)
      = <x^(2m),(A_a-kappa)^(-1)1> / <1,(A_a-kappa)^(-1)1>.         (11)

This retains the full arithmetic source. It is not a random-matrix average
or a fitted collection of known zeta zeros.

## 2. Zero-free Gaussian compensation allows a weaker normalization

The numerical experiments suggested that a large part of the mismatch is
quadratic. Define V_X=-X''(0) and

    H_a(z)=exp((V_a-V_X)z^2/2) F_a(z).                              (12)

This factor introduces NO zeros. Matching V_X is a stated normalization,
not independent agreement with Xi. With Q_a=sum_j x_j^(-4), the elementary
inequality |(1-w)exp(w)|<=exp(|w|^2/2) gives

    |H_a(z)| <= exp(V_X |z|^2/2 + Q_a |z|^4/2).                    (13)

Indeed log|1-w| <= -Re w + |w|^2/2 follows from log u<=u-1.
Also Q_a=-2[z^4]log F_a. A uniform quartic logarithmic-coefficient bound
therefore suffices for normality after compensation; a uniform bound for
V_a itself is not needed. This canonical-product estimate is classical
and overlaps the repo's earlier weighted-canonical programme. The new
construction here supplies F_a from the actual Weil form.

If every fixed Taylor coefficient of H_a converges to X's and sup Q_a is
finite along a cofinal sequence, the same normality and Hurwitz argument
proves RH. Equivalently one may match the logarithmic coefficients of
orders 4,6,..., together with (12). Finite orders never imply the cofinal
premise. The finite results do not prove this hypothesis.

## 3. A quantitative residual test for the source bridge

This version does not require identifying any eigenvector or proving that
its eigenvalue is simple. Put q_kappa=q_a-kappa<.,.>, with kappa<lambda_0,
and let f be its unique minimizer subject to f_hat(0)=1. Then
f=(A_a-kappa)^(-1)1/<1,(A_a-kappa)^(-1)1>.
Let v in D_a satisfy v_hat(0)=1, and define

    H_0={w in D_a: w_hat(0)=0},
    gamma=inf_(w in H_0, ||w||=1) q_kappa[w] >0.

If |q_kappa(v,w)|<=epsilon ||w||_2 for every w in H_0, then

    ||f-v||_2 <= epsilon/gamma,
    |f_hat(z)-v_hat(z)| <= sqrt(2a) exp(a |Im z|) epsilon/gamma.    (14)

Proof: d=f-v belongs to H_0, and q_kappa(f,d)=0 by the constrained
Euler equation. Hence gamma||d||^2<=q_kappa[d]=-q_kappa(v,d)
<=epsilon||d||. Fourier evaluation gives the second inequality.
If v is in the operator domain, epsilon can be taken to be
||P_(1-perp)(A_a-kappa)v||_2. All quantities refer to the same a,kappa.

Equation (14) replaces a vague 'small residual' claim by the ratio to
coercivity on the zero-mean subspace and the exact complex evaluation
cost. A tiny residual alone is insufficient when gamma is also tiny.
No lower bound of the required strength for the actual gamma is proved.
The explicit safe shift in PROOF.md makes gamma positive but does not
make the source residual small enough for the desired limit.

## 4. Attempts and failure boundary

A fixed large negative shift produces perfectly legitimate real-zero
functions but need not approach Xi. A shift just below the finite spectral
minimum can emphasize a very different scale; it is not certified legal
for the full operator. Both effects are included in the experiment design.

For fixed a=1.3, increasing the Fourier cutoff improves the displayed
Gaussian-compensated finite comparison. Increasing a at only linearly
increasing cutoff did NOT show monotonically improving agreement. This is
not evidence against a better schedule, but it is insufficient to assert
convergence. The observed smallest eigenvalues are extraordinarily small;
ordinary double precision cannot resolve them. Even a high-precision
matrix replay is not a lower bound for the continuum spectrum.

A larger coefficient match or a higher precision run is not the next
analytic theorem. The structural target is a source-uniform estimate such
as (14) on expanding intervals, or cofinal logarithmic-coefficient control
with (13). No such estimate is obtained in this packet. No smaller
zero-free half-plane, RH proof, or validated off-critical zero follows.
