# Independent skeptic reconstruction: smooth positive kernels and finite Li prefixes

Date: 2026-11-17. Reviewer: `/root/li_skeptic`. The advocate's draft was not read. This is an independently reconstructed model obstruction, not a theorem about the Riemann zeta function. Priority has not been established. Classification: independently checked with no issue found in the argument below. The explicit quantitative Li parameter is a supplied strengthening of the continuity argument.

## Statement and quantifiers

Write `w=s-1/2`, let `H_m=sum_{j<=m}1/j`, and set

\[
 d=H_{13}/2-\gamma-1,\quad
 B(w)=\frac{\sinh(dw)}{dw}\prod_{j=14}^{\infty}
             \frac{\sinh(w/(2j))}{w/(2j)},\quad
 C_a(w)=\cosh w+\cosh a.
\]

For `0<=a<1/2`, define

\[
 F_a(s)=\frac{B(s-1/2)C_a(s-1/2)}{B(1/2)C_a(1/2)}.
\]

Then `F_a` is a real entire function of order one and infinite exponential type, symmetric under `s -> 1-s`, with `F_a(0)=F_a(1)=1`. In the centered variable it is the bilateral Laplace transform of an even, smooth, everywhere strictly positive density, up to a positive normalization. All its zeros are in `0<Re(s)<1`. Its positive-ordinate zero count, **with multiplicity**, satisfies

\[
 N_a(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}
       -\frac{T}{2\pi}+O(\sqrt T).
\]

For **every fixed integer `N>=1`**, put `a_N=1/(100 N 5^N)`. For **every `0<a<=a_N`**, the first `N` Li coefficients (with the usual derivative definition) satisfy `lambda_n(F_a)>1/1152`, `1<=n<=N`, although `F_a` has off-line zeros. This is not positivity of every coefficient for one fixed positive `a`.

## Positive scale and convergence

The positivity of `d` does not require an unvalidated decimal evaluation. Since `gamma<H_64-log64` and the first three positive terms of the atanh series give `log2>842/1215`,

\[
 d>H_{13}/2-H_{64}-1+6(842/1215)
  =\frac{14898922139351236715859107}
         {3546800652308466802534084800}>0.
\]

Let `delta_13=d`, `delta_j=1/(2j)` for `j>=14`. Because `sum delta_j^2<infinity` and `sinh(delta_j w)/(delta_j w)=1+O_R(delta_j^2)` uniformly on every compact disk, the product converges locally uniformly to an entire function. Away from the individual factor zeros it is nonzero; this follows from the absolutely convergent tail logarithm. Every bounded region meets only finitely many factor zero sets. No additional zeros arise in taking the product.

## Probability and an everywhere positive smooth density

Let `U_j` be independent uniform random variables on `[-delta_j,delta_j]`. Their centered partial sums converge in `L^2` (and almost surely by the independent-sum convergence theorem), since the variances sum. Denote the limit by `X`. For real `z`,

\[
 \sinh z/z\le\cosh z\le e^{z^2/2}.
\]

Consequently the exponential moments of the partial sums, including moments with the exponent doubled, are uniformly bounded on compact real parameter sets. Uniform integrability identifies `B(w)=E exp(wX)` for real `w`; finiteness of all exponential moments and dominated differentiation give the entire bilateral Laplace transform.

There is a direct exponential characteristic-function bound. For `|t|>=28pi`, take all integers `j` in `[|t|/(2pi),|t|/pi]`. These indices are at least 14, and `|t|/(2j)` lies in `[pi/2,pi]`, where `|sin u/u|<=2/pi=:q<1`. There are at least `|t|/(2pi)-1` such factors. Every other factor has characteristic modulus at most one. Hence

\[
 |B(it)|\le q^{-1}\exp[-\log(\pi/2)|t|/(2\pi)].
\]

Fourier inversion therefore gives an even `C^infinity` density `k` (in fact an analytic density in a nonzero strip).

Strict positivity requires an additional argument; it does **not** follow merely from nonnegativity plus full support. Remove `U_13` and call the remaining sum `Y`. The support of `Y` is all of `R`: a finite sum of its uniforms has a density positive on the interior of its support, the half-lengths of these supports diverge because `sum_{j>=14}1/(2j)=infinity`, and the independent remaining tail has arbitrarily small variance. Given any open target interval, take a finite sum whose support contains a slightly enlarged target, and a tail which has positive probability in a sufficiently small neighborhood of zero; conditioning proves positive probability in the target. Thus

\[
 k(x)=\frac{P(Y\in(x-d,x+d))}{2d}>0
\]

for every `x`. The exponential characteristic bound also holds after removing this one factor, so `Y` has a continuous density; the displayed convolution expression is indeed the pointwise smooth density already obtained by inversion.

Finally `C_a(w)/(1+cosh a)` is the MGF of a three-point even probability distribution, with weights `1/[2(1+cosh a)]` at each of `+1,-1` and `cosh a/(1+cosh a)` at zero. Multiplication therefore produces a shifted mixture of `k`, still even, smooth, and everywhere positive. Dividing by `B(1/2)C_a(1/2)>0` changes only the positive scale. The kernel is not compactly supported.

## Exact zeros and zero count

The zeros of `B` are `w=i pi k/d`, `k` a nonzero integer, and `w=2pi i j k`, `j>=14`, `k` a nonzero integer, with all multiplicities retained. The identity

\[
 C_a(w)=2\cosh((w+a)/2)\cosh((w-a)/2)
\]

gives zeros `w=+a+i(2k+1)pi` and `w=-a+i(2k+1)pi`. For `a=0` these are double line zeros; for every `a>0` they are off the line. Their ordinates do not change with `a`.

Put `Y=T/(2pi)` and `D(Y)=sum_{j>=1} floor(Y/j)`. The exact count for `T>=0` is

\[
 N_a(T)=D(Y)-\sum_{j=1}^{13}\lfloor Y/j\rfloor
       +\lfloor2dY\rfloor+2\lfloor Y+1/2\rfloor.
\]

Coincident zeros are counted by adding multiplicities; no irrationality assumption on `d` is needed. Using `D(Y)=Y logY+(2gamma-1)Y+O(sqrtY)` and `2d=H13-2gamma-2` gives the stated main term.

Here is also a fully explicit elementary bound: for `Y>=1`,

\[
 |N_a(T)-(Y\log Y-Y)|\le2\sqrt Y+20.
\]

Indeed let `m=floor sqrtY`, `S=sum_{j<=m}{Y/j}` and `r_m=H_m-logm-gamma`, so `0<r_m<1/m`. The hyperbola identity gives divisor error

\[
 E_D=Y(\log z+1-z)+2Yr_m-2S,\qquad z=m^2/Y.
\]

Since `logz>=1-1/z`, the first term lies in `[-9,0]`; the inequalities `Y<(m+1)^2`, `0<=S<m` give `-2m-9<E_D<2m+6`. The remaining floor-function correction to its linear main term lies between `-2` and `14`. The safe bound above follows. The elementary estimate on `r_m` follows by summing `0<log(1+1/k)-1/(k+1)<1/k-1/(k+1)` over `k>=m`.

## Order and infinite type

For real `r` tending to infinity,

\[
 \log B(r)=\tfrac12 r\log r+O(r).
\]

For the upper bound split at `j=ceil r`. For indices below the split use `log(sinh z/z)<=z`; for the tail use `log(sinh z/z)<=z^2/2`. The contributions are respectively `(r/2)logr+O(r)` and `O(r)`. For the lower bound use `14<=j<=floor(r/2)`, where `z=r/(2j)>=1`, and `log(sinh z/z)>=z-logz-C`. The sum of the `z` terms is `(r/2)logr+O(r)`, whereas the logarithm and constant sums are `O(r)` by the elementary factorial integral bound. Other real factors are at least one. The `d` factor contributes `O(r)`.

The MGF representation gives `|B(w)|<=B(|w|)`, with equality at positive real `w`. Adding `C_a` changes the logarithmic maximum only by `O(r)`. Translating the variable and dividing by a positive constant preserve order and type. Thus the order is exactly one but `log M(r)/r` is unbounded: the type is infinite.

## Li coefficients: exact factors and a quantitative prefix

Use

\[
 \lambda_n(F)=\frac1{(n-1)!}
  \left.\frac{d^n}{ds^n}[s^{n-1}\log F(s)]\right|_{s=1}.
\]

At `a=0`, the centered sinh and cosh products have paired quadratic zero factors and no hidden exponential factor. The zero count implies `sum |rho|^-2<infinity`. Their paired logarithms and each fixed derivative converge normally near `s=1`. Reflection `rho -> 1-rho` must be used when converting the rootwise derivative's inverse-power expression into the usual `1-(1-1/rho)^n` sum. A conjugate line pair contributes `2(1-cos(n theta))>=0`, where `theta=2 arctan(1/(2 Imrho))`.

For a lower bound take the double conjugate pair of `C_0=2cosh^2(w/2)` at `Imrho=(2n+1)pi=:v`. The elementary bounds `z/2<=arctanz<=z` for `0<=z<=1` give `1/(2v)<=theta<=1/v`; thus `0<n theta<1`. Since `1-cosu>=u^2/4` there, its contribution is

\[
 4(1-\cos(n\theta))\ge n^2/(4v^2)\ge1/(36\pi^2)>1/576.
\]

All other pair contributions are nonnegative.

For the perturbation consider `|s-1|<=1/4`. Here `|Imw|<=1/4`, so `Re(C_0(w))=cosh(Rew)cos(Imw)+1>=1`. For `0<=a<=1/2`, `cosh a-1<=a^2`. Therefore

\[
 L_a(s)=\log(C_a(w)/C_0(w))=\log(1+u),\quad
 |u|\le a^2\le1/4,\quad |L_a|\le4a^2/3.
\]

The analytic logarithm is the convergent local logarithmic series. Write `L_a=sum d_k(s-1)^k`. Cauchy's estimate gives `|d_k|<=(4a^2/3)4^k`. The normalization constants contribute only a constant to the logarithm and hence nothing to Li coefficients. The derivative definition gives

\[
 |\lambda_n(F_a)-\lambda_n(F_0)|
 \le\sum_{k=1}^n k\binom nk |d_k|
 \le\tfrac{16}{3}a^2 n5^{n-1}.
\]

For `a<=a_N=1/(100N5^N)` and `n<=N`, this is at most `16/(150000 N5^N)<=2/93750<1/1152`. Subtracting from the baseline greater than `1/576` proves the advertised strict lower bound. This avoids relying on numerical Li computations.

## Serious scope limitations and negative knowledge

* The off-line zeros number `T/pi+O(1)` for every fixed `a>0`. They have density zero relative to the total `TlogT` count, but violate sublinear zero-density estimates in any fixed strip `Re(s)>=sigma` with `1/2<sigma<1/2+a`. This model does **not** satisfy all known zeta zero-density restrictions.
* The zero-count error is `O(sqrtT)`, not the classical `O(logT)` remainder. Many line zeros have divisor multiplicities. These are substantial missing constraints.
* No Euler product, arithmetic Dirichlet series, zeta gamma factor, prime explicit formula, simplicity, or fine spacing law is asserted. Smooth kernel positivity, the smooth RVM main term, order one/infinite type, symmetry, and a finite positive Li prefix by themselves do not encode those arithmetic restrictions.
* A fixed `a>0` has off-line zeros and cannot have every Li coefficient nonnegative under the applicable all-coefficients criterion. The explicit statement is `for every N there exists a_N`, with the function allowed to depend on `N`.
* There is no claim of novelty. The divisor product is closely related to known divisor spectral determinants; actual primary-source reading is needed before making a historical claim. The searches listed below are discovery leads only.

## Reproduction and provenance

`experiments/code/positive_kernel_skeptic_round3.py` uses only integer and exact Fraction arithmetic. It checks the positive rational lower bound for `d`, the hyperbola identity at integer `Y=1,...,2000`, and the rational Li constants for representative `N`. Output: `experiments/results/positive_kernel_skeptic_round3.json`. These finite checks support bookkeeping; the analytic proofs above carry the mathematical conclusions.

Primary-source discovery leads, **not read for this audit**: Endres and Steiner, arXiv:1104.1364, *An exact trace formula and zeta functions for an infinite quantum graph with a non-standard Weyl asymptotics*, J. Phys. A 44 (2011), 185202, DOI 10.1088/1751-8113/44/18/185202; primary PDF https://www.uni-ulm.de/fileadmin/website_uni_ulm/nawi.inst.260/paper/11/tp11-1.pdf. The unmodified product can be regrouped as `product_{n>=1}(1+w^2/(4pi^2n^2))^{d(n)}`, making the divisor connection explicit. No bibliographic audit level or full-source reading is claimed here.
