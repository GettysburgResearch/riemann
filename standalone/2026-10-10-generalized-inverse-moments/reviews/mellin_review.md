# Independent audit of the universal test and moment-growth characterization

**Verdict:** PASS for the mathematical statements as scoped. No mathematical correction identified. The reciprocal lemma can be reconstructed from standard uniform Hecke strip growth and elementary complex analysis, without using either claimed quasi-Riemann theorem. Its zero-free hypothesis remains explicit.

**File read in full:** `analysis_amplification.md`.

**SHA256:** `f3bdeb168714d838a4b13347cd353675d9644b9629041cdf7def78dc496162e3`.

**Review scope:** mathematical identities, hypotheses, uniformity, analytic continuation, and limiting quantifiers. No numerical evidence or full upstream proof is certified.

## 1. Universal test

The infinite convolution construction is correct. The interval widths are absolutely summable, while their squares are summable as well. The first fact gives compact support and bounded convergence of the complex moment-generating functions; the second gives locally uniform convergence of the entire product. The characteristic-function estimate using the first `floor(sqrt(c|t|/2))` factors proves stretched-exponential Fourier decay, so Fourier inversion gives a globally smooth density, including at the support endpoints.

The selected translation puts the entire compact support strictly inside `(1,2)`. At every point off the imaginary axis all individual factors are nonzero, and the summable deviations from one imply that their infinite product is nonzero. Thus the universal test really does avoid every zero with positive real part. No lower bound for its Mellin transform at large height follows or is asserted.

The scale Mellin identity has the correct sign and normalization. The sum vanishes below a positive scale, so there is no lower-end singularity in the scale integral. A bound with every positive exponent loss gives holomorphy on the claimed open half-plane. The finite deleted Euler factors are nonzero there, and a pole of a principal `L` function produces a zero, not a pole, of its reciprocal.

## 2. Prime replicas, record scales, and excess exponents

The exact recursion is valid for every fixed base row. Excluding the finitely many prime divisors of that base row leaves the stated prime-ideal count. Distinct primary prime generators give distinct sixth-power replicas. Constants may depend on the fixed base row but never on the moving prime.

The record-scale argument is valid: the normalized absolute value is continuous, is zero below a fixed support floor, and is bounded on every compact interval. If it is unbounded, maxima on increasing compact intervals supply records tending to infinity. At a record scale, every lower-scale term in every prime recursion is bounded by the same record constant. This makes the replication error a vanishing geometric fraction of the recorded value, uniformly across the selected primes.

Letting the trial exponent approach a zero's real part is legitimate only after fixing that exponent and taking its own record sequence; the limsup lower bound handles this correctly. Taking the supremum over zeros and fixed twists does not require a common record sequence. Likewise the all-moment implications use a single sufficiently large finite moment for a fixed hypothetical off-critical zero. They require no constants uniform in the moment order.

The strict exceptional-row count in the one-good-replica lemma is correct, as is the subsequent induction. The `o(D^{h/6}/log D)` version works for every fixed base row even though its prime-count constant depends on that row.

## 3. Explicit reconstruction of the uniform reciprocal lemma

This gives the radii and uniformity details behind the paragraph in the audited file. It is a proof from standard Hecke analytic theory, rather than an application of the quasi-Riemann result.

Assume a family of primitive finite-order Hecke characters over the fixed field has no `L`-function zero in `Re(s)>b`, where `1/2<=b<1`. Fix `delta,eta>0` and put

\[
d=\min\{\delta,(1-b)/2,1/4\}>0.
\]

For a nonprincipal character set `F(s)=L_K(s,psi)`. For the principal character set

\[
F(s)=\frac{s-1}{s+1}\zeta_K(s),
\]

with its removable value at `s=1`. In either case `F` is holomorphic and nonzero in `Re(s)>b`. The standard uniform polynomial strip bound gives

\[
|F(\sigma+iv)|\le C\{2Q_\psi(3+|v|)^2\}^{C}
\tag{3.1}
\]

on the fixed strip needed below. A crude form suffices: Euler convergence on a right boundary, the finite-order Hecke functional equation on a left boundary, and Phragmen–Lindelof give such a bound. No zero-free region is used for this polynomial growth estimate. The principal regularization removes its only pole in the strip.

Center the disks at `z_0=2+it` and choose radii

\[
r_0=1-d/4,\quad
r=2-b-d,\quad
R_1=2-b-d/2,\quad
R=2-b-d/4.
\tag{3.2}
\]

They satisfy `0<r_0<r<R_1<R`. The closed outer disk lies in `Re(s)>=b+d/4`, strictly inside the assumed zero-free half-plane. It therefore has an analytic logarithm `g=log F`, normalized at its center by the Euler logarithm and, when needed, the elementary principal regularization.

On the disk of radius `r_0`, the real part exceeds `1+d/4`. The Euler logarithm, and the principal regularization logarithm when present, are uniformly bounded there. Hence

\[
M(r_0):=\max_{|s-z_0|\le r_0}|g(s)|\ll_d1.
\]

Throughout the outer disk the height differs from `t` by at most a fixed constant. Estimate (3.1) gives

\[
\Re g(s)\ll_{b,d}\log\mathcal Q,
\qquad \mathcal Q=2Q_\psi(3+|t|)^2.
\]

Borel–Carathéodory, using the fixed gap `R-R_1=d/4` and the bounded center value, yields

\[
M(R_1)\ll_{b,d}\log\mathcal Q.
\]

Hadamard's three-circles theorem now gives

\[
M(r)\ll_{b,d}(\log\mathcal Q)^\kappa,
\qquad
\kappa=\frac{\log(r/r_0)}{\log(R_1/r_0)}\in(0,1).
\tag{3.3}
\]

The horizontal points `sigma+it` with `b+d<=sigma<=2` lie in this disk. Thus both `F` and its reciprocal have modulus at most

\[
\exp\{C_{b,d}(\log\mathcal Q)^\kappa\}
\ll_{b,d,\eta}\mathcal Q^\eta.
\]

For `sigma>=2`, Euler convergence suffices. For the principal character,

\[
\frac1{\zeta_K(s)}=\frac{s-1}{s+1}\frac1{F(s)},
\]

and `|(s-1)/(s+1)|<=1` when `Re(s)>=0`. This proves the stated reciprocal bound on `sigma>=b+delta`, uniformly in the conductor and height. All constants depend only on fixed buffers and standard fixed-field analytic estimates.

The use of a logarithm of a nonvanishing function is justified on each simply connected disk. Its normalization matches the Euler branch on the small disk by uniqueness of analytic continuation. A zero arbitrarily close to the line `Re(s)=b` is harmless because every disk keeps the fixed positive buffer `d/4`.

## 4. Conductor, deleted factors, and the exact characterization

The polynomial conductor bound is sufficient and correct. The sextic Kummer character is unramified outside primes dividing `6u`; outside the fixed primes above six its conductor exponent is at most one, and the local sixth-power quotients at the fixed primes are finite. The fixed character `nu` changes only the fixed conductor datum. A polynomial discriminant bound would also suffice, so no optimal conductor exponent is required.

The deleted-factor bound is uniform in the row: the large-prime local cost is absorbed into any fixed positive power of the radical norm, and the finitely many small primes cost a fixed constant. Combining this with the reciprocal bound and `Nu<=D^h` gives the claimed uniform pointwise bound after shifting the fixed smooth Mellin contour. The parameters controlling conductor and height losses can be chosen arbitrarily small before the contour shift, and the fixed smooth transform controls the vertical tails.

The endpoint `B_nu=1` is handled separately by counting, so the proof does not assume a nonexistent fixed zero-free buffer below one. Functional equations and conjugation give the critical-line reflection of the nontrivial zeros, sufficient for the GRH equivalences. No closure of the fixed-`nu` twist family under changing `nu` is needed for this reflection.

Accordingly the bounds

\[
2kB_\nu+h/6\le\lambda_k\le2kB_\nu+h
\]

and their limiting characterization are valid under the explicitly stated standard analytic inputs. The proof assumes no quasi-Riemann theorem. Its upper bound uses the actual zero supremum as the hypothesized zero-free boundary; it supplies no independent upper estimate for that supremum.

## 5. A conditional higher-moment bound obtainable from the existing inputs

There is a useful corollary from the imported inputs, but it does not improve their zero-free exponent.

Assume the full twist family has no zeros in `Re(s)>B`, with `1/2<=B<1`, and assume the exact short-row second moment

\[
M_2(D,H)\ll_\epsilon HD^{1+\epsilon},
\qquad H=D^h.
\tag{5.1}
\]

The uniform reciprocal lemma above gives

\[
\max_{0<Nu\le H}|A_u(D;W)|\ll_\epsilon D^{B+\epsilon}
\]

for every fixed compact smooth test. Here the polynomial conductor bound and deleted Euler factors have been included. Therefore, for each fixed integer `k>=1`,

\[
\boxed{\displaystyle
M_{2k}(D,H)
\ll_\epsilon HD^{1+2B(k-1)+\epsilon}.}
\tag{5.2}
\]

Indeed, bound `|A_u|^{2k-2}` by its maximum and sum the remaining square; choose all initial losses smaller than the requested final epsilon. This is conditional on the displayed zero-free and second-moment inputs. It is not a new off-diagonal arithmetic estimate.

For the imported `B=7/8` and `h=1+theta`, it gives

\[
M_4(D,H)\ll HD^{11/4+\epsilon},
\tag{5.3}
\]

a `D^{1/4}` improvement over the bound `D^2 M_2(D,H)`. In general the excess over `HD^k` is

\[
e_k=(2B-1)(k-1).
\tag{5.4}
\]

This is linear in `k` whenever `B>1/2`. Applying the proved extraction gives

\[
\alpha_k
=B+\frac{\frac12+\frac{5h}{12}-B}{k}.
\tag{5.5}
\]

At `B=7/8` and `h` tending to one, the fourth-moment value is `43/48`, and the general value is `7/8+1/(24k)`. Every such exponent is weaker than the zero-free exponent already assumed. Hence this interpolation does not bootstrap `7/8` toward `1/2`.

### Sharpness from these two norm budgets alone

The loss in (5.2) cannot be improved using only the pointwise and second-moment budgets. Suppose `h+1-2B>0`, which holds in the intended range `h>1`, `B<1`. On

\[
R=\lfloor HD^{1-2B}\rfloor
\]

rows put `x_u=D^B`, and put zero on all other rows. Since `B>=1/2`, at most `H` rows are used. Then

\[
\max|x_u|=D^B,\qquad
\sum|x_u|^2\le HD,
\]

while

\[
\sum|x_u|^{2k}\asymp HD^{1+2B(k-1)}.
\]

This is an abstract norm-budget example, not a claimed realization by the arithmetic coefficients.

It can accommodate the full prime-replica count when

\[
B<\frac12+\frac{5h}{12},
\]

because then

\[
\frac{R}{D^{h/6}/\log D}
\asymp D^{1+5h/6-2B}\log D\longrightarrow\infty.
\]

This includes `B=7/8` and the intended `h=1+theta`. Thus replica counting does not rescue an improvement from these norm budgets. An excess `e_k=o(k)` needs additional arithmetic input, beyond both the existing second moment and the uniform `7/8` zero-free control.
