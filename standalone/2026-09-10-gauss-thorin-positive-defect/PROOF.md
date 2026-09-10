# GTP26 — Gauss–Thorin approximation and positive branching defects

Date: 2026-09-10. **Status: proposed component proofs, independently unreviewed. RH is NOT proved.**

This packet connects the variance-matched gamma orbit of PR #850 to the positive-defect construction of PR #846. It constructs a finite-gamma hierarchy at every order, proves a positive probability-law representation of its complete error, and transports that representation through the literal Brownian branching map. A directed calculation rules out a tempting phase-monotonicity shortcut. The remaining zero-location theorem is stated separately; it is not supplied by the positive error representation.

The Brownian source is classical Biane–Pitman–Yor (BPY). Gaussian quadrature, Stieltjes/Padé approximation, infinite divisibility of gamma laws, Fourier uniqueness, and Hurwitz are classical mechanisms. No external-priority claim is made. The contribution proposed relative to the inspected branches is their source-specific composition, the all-order positive defect and exact smooth-test distance, and the certified second-level obstruction.

## 1. Frozen sources and conventions

Repository baseline: `main @ f99d9e3908dde4865377c75d9ca051c1f545bf4f`.

* PR #850: `5c26d1f7e1075fdea18119a5abb447102ab5850b`, `standalone/2026-09-10-astra-branching-fixedpoint/PROPOSAL.md`.
* PR #846: `d9b60f8569af65b6787fc33c75c849640c8974e6`, `standalone/2026-09-10-astra-brownian-renormalization/PROOF.md`.
* PR #849: `11a12b8ceb7db98c7961a5cebf3870b2f31dfa79`, `standalone/2026-09-10-reciprocal-gamma-cascade/PROPOSAL.md`, sections 1–4 opening. Its raw gamma-coordinate truncation and reciprocal density projection are different from the quadrature construction here.
* BPY: *Probability laws related to the Jacobi theta and Riemann zeta function and Brownian excursions*, arXiv:math/9912170, Proposition 1 and equations (43)–(45).

Use the entire continuation

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad \xi(0)=\xi(1)=\tfrac12.
\]

Write Gamma(shape, scale), with Laplace transform `(1+scale*t)^(-shape)`. A shape zero at an auxiliary mixture endpoint denotes the constant zero variable. All sums use independent variables unless sharing is explicitly specified. Powers of positive real variables use their real logarithm.

Set

\[
\alpha_j=\frac6{\pi^2j^2},\quad X_* =\sum_{j\ge1}\alpha_jE_j,\quad
L_*(t)=\mathbb E e^{-tX_*}=\frac{\sqrt{6t}}{\sinh\sqrt{6t}},
\tag{1}
\]

where the `E_j` are mean-one exponentials. The removable value at zero is one. The positive series converges almost surely and in `L²`. It has mean one and variance `2/5`.

Define

\[
\mathcal T(X)=U^{-2}(X+X'),\qquad U\sim\mathrm{Unif}[1,2],
\quad a_j=\int_1^2u^{-2j}du=\frac{1-2^{1-2j}}{2j-1},\quad r_j=2a_j.
\tag{2}
\]

The **same U** multiplies both siblings. Independent multipliers give a different map. Direct integration, with `v=sqrt(6t)`, gives

\[
\int_1^2L_*(t/u^2)^2du=v[\coth(v/2)-\coth(v)]=v/\sinh v.
\]

Thus `X_*` is a fixed law. Equal-mean independent-copy coupling gives

\[
W_2(\mathcal T\mu,\mathcal T\eta)\le\sqrt{7/12}\,W_2(\mu,\eta).
\tag{3}
\]

This identifies the unique mean-one finite-second-moment fixed law without zero data. BPY's normalization supplies the separate complete Mellin identity

\[
\frac12(\pi/6)^{s/2}\mathbb E(X_*+X_*')^{s/2}=\xi(s),\qquad s\in\mathbb C.
\tag{4}
\]

The source has every positive and negative moment. This follows either from BPY or directly from the exponential decay of (1) at large positive `t` for inverse moments, and the summable gamma construction for positive moments.

## 2. An exact finite-gamma hierarchy

Introduce the probability measure

\[
\nu=\sum_{j\ge1}\alpha_j\delta_{\alpha_j},\qquad
\mu_\ell=\int a^\ell d\nu(a)=\sum_{j\ge1}\alpha_j^{\ell+1}.
\tag{5}
\]

Its support lies in `[0,alpha_1]`, with infinitely many distinct positive atoms and `alpha_1<1`. Its logarithmic-Laplace resolvent is

\[
g(t)=-L_*'(t)/L_*(t)=\int\frac{d\nu(a)}{1+ta}.
\tag{6}
\]

The moments `mu_l` are rational: equivalently obtain them from the formal identity `g=S'/S`, where `S(t)=sinh(sqrt(6t))/sqrt(6t)`. In particular

\[
\mu_0=1,\qquad\mu_1=2/5,\qquad\mu_2=8/35.
\]

For `m>=1`, let `p_m` be the monic degree-m orthogonal polynomial for `nu`, let `x_1,...,x_m` be its zeros, and let `w_i` be the Gaussian weights. These objects are fixed by the actual source, not fitted to zeta zeros.

For clarity, their existence and positivity need no numerical assumption. The moment Gram matrices are strictly positive because a nonzero polynomial cannot vanish at every atom. The usual sign-change argument places all `m` zeros of `p_m` simply in `(0,alpha_1)`. Polynomial division by `p_m` proves quadrature exactness through degree `2m-1`. If `ell_i` is the Lagrange polynomial of node `i`, the weight is `integral ell_i² dnu>0`. In particular `sum w_i=1`.

Define

\[
X_{m,0}=\sum_{i=1}^m\mathrm{Gamma}(w_i/x_i,x_i),\quad
L_{m,0}(t)=\prod_i(1+x_it)^{-w_i/x_i},\quad
 g_m(t)=\sum_i\frac{w_i}{1+x_it}.
\tag{7}
\]

### GTP1: moment matching and an explicit signed logarithmic defect

`X_{m,0}` and `X_*` have identical moments through order `2m`. In particular every seed has mean one and variance `2/5`. Put

\[
k=2m+1,\quad h_m=\int p_m(a)^2d\nu(a)>0,\quad d_m=h_m/k.
\]

Then, for `t>=0`,

\[
g(t)-g_m(t)=t^{2m}R_m(t),\quad
R_m(t)=\frac{\displaystyle\int\frac{p_m(a)^2}{1+ta}d\nu(a)}
                  {\displaystyle\prod_i(1+x_it)^2},
\tag{8}
\]

and

\[
\log L_{m,0}(t)-\log L_*(t)=t^kQ_m(t),\quad
Q_m(t)=\int_0^1u^{k-1}R_m(ut)du,\quad Q_m(0)=d_m.
\tag{9}
\]

Both `R_m` and `Q_m` are Laplace transforms of finite positive measures.

**Proof.** Moment matching follows from quadrature applied to the logarithmic-Laplace series: its jth cumulant is `(j-1)! integral a^(j-1) dnu`. To prove (8), put `S(z)=integral (z-a)^(-1)dnu(a)` and `q_m(z)=integral [p_m(z)-p_m(a)]/(z-a) dnu(a)`. Orthogonality yields

\[
S(z)-\frac{q_m(z)}{p_m(z)}
=\frac1{p_m(z)^2}\int\frac{p_m(a)^2}{z-a}d\nu(a).
\]

Indeed the difference between the two remainders vanishes by integrating `p_m(a)` against the degree-`m-1` polynomial `[p_m(z)-p_m(a)]/(z-a)`. Substitute `z=-1/t`. The rational approximant is the quadrature resolvent, giving (8), including its sign and normalization. Integrating from zero to `t` gives (9).

The factor `(1+ta)^(-1)` is an exponential Laplace transform; each `(1+x_it)^(-2)` is a gamma Laplace transform. Positive products and mixtures preserve that interpretation. The same is true after scaling `t` and integrating in (9). No complex zero conclusion is being deduced from complete monotonicity. □

### GTP2: a positive probability law for the COMPLETE error

There is an explicitly defined positive variable `B_{m,0}` such that

\[
\boxed{L_{m,0}(t)-L_*(t)=d_m t^k\mathbb E e^{-tB_{m,0}}.}
\tag{10}
\]

This holds for the complete transforms, not only their expansions at zero. In particular

\[
0\le L_{m,0}(t)-L_*(t)\le d_m t^k.
\tag{11}
\]

**Proof and constructive law.** Both transforms in (9) are infinitely divisible by their explicit gamma representations. Therefore

\[
\frac{L_{m,0}-L_*}{t^k}
=Q_m(t)\int_0^1L_{m,0}(t)^\theta L_*(t)^{1-\theta}d\theta
\tag{12}
\]

is a positive Laplace transform of mass `d_m`.

Explicitly, choose `A` with probability measure `p_m(a)^2 nu(da)/h_m`. Let `Z` be an exponential of conditional scale `A` plus independent gamma variables of shape two and scales `x_i`. Let `V` have density `k v^(k-1)` on `[0,1]`. Independently choose `Theta` uniform on `[0,1]`, and conditional on it form `J_Theta` by giving every gamma shape in the seed the factor `Theta` and every shape in the infinite source the factor `1-Theta`. Then

\[
B_{m,0}=VZ+J_\Theta
\]

has the claimed law. All of its positive moments exist. This construction proves (12) without using a numerical approximation or an unspecified positivity oracle. □

### GTP3: superfactorial control of the seed defect

\[
0<d_m\le\frac{\alpha_1^{2m+1}}{m(2m+1)(m!)^4}.
\tag{13}
\]

**Proof.** A monic orthogonal polynomial minimizes its squared norm among monic polynomials of its degree. Compare with `prod_(j=1)^m(a-alpha_j)`. Its values vanish at the first `m` atoms; at every remaining atom their absolute values are at most `prod_(j=1)^m alpha_j`. Finally `sum_(j>m)alpha_j<=alpha_1/m` and `prod_(j=1)^m alpha_j=alpha_1^m/(m!)²`. □

As `m` tends to infinity the seeds converge weakly to `X_*`: (11),(13) give pointwise Laplace convergence, and their fixed means give tightness. This is an all-order construction, not a finite moment fit. It does not give a zero-free class of Mellin transforms.

## 3. The gamma seed in #850 is the first exact member

For `m=1`, the Gaussian rule has `x_1=2/5,w_1=1`. Thus

\[
X_{1,0}\sim\mathrm{Gamma}(5/2,2/5),\quad k=3,\quad
h_1=8/35-4/25=12/175,\quad d_1=4/175.
\tag{14}
\]

So the seed already selected in #850 is precisely the first Gaussian quadrature of the Brownian logarithmic-Laplace source. Equation (10) upgrades its fixed-moment agreement to the positive complete cubic defect

\[
L_{1,0}(t)-L_*(t)=\frac4{175}t^3\mathbb E e^{-tB_{1,0}}.
\tag{15}
\]

For this first case, the key resolvent identity can also be checked without orthogonal polynomials. If `A~nu` and `b=EA=2/5`,

\[
\mathbb E\frac1{1+tA}-\frac1{1+tb}
=\frac{t^2}{(1+tb)^2}\mathbb E\frac{(A-b)^2}{1+tA}.
\]

This is an exact second-order remainder, not an application of Jensen that drops the error law.

For reference, the first four exact constants are

| m | k | d_m |
|---|---|---|
| 1 | 3 | 4/175 |
| 2 | 5 | 16/202125 |
| 3 | 7 | 64/876750875 |
| 4 | 9 | 256/10316226545625 |

The checker regenerates these from the sinh source, not from an input moment table.

## 4. Branching preserves the positive defect at every depth

Fix `m` and put `X_{m,n+1}=T(X_{m,n})`. For `k=2m+1`, choose `U_k` with density `u^(-2k)/a_k` on `[1,2]`. Let `Y_{m,n}` be an equal-probability mixture of the laws of `X_{m,n}` and `X_*`. Define

\[
B_{m,n+1}=U_k^{-2}(B_{m,n}+Y_{m,n}),\qquad
C_{m,n}=B_{m,n}+\widehat Y_{m,n}.
\tag{16}
\]

Every variable in each sum is independent; the hatted copy is a fresh copy.

### GTP4: exact error transport and exact smooth-test distance

For every `n>=0,t>=0`,

\[
\boxed{L_{m,n}(t)-L_*(t)=d_m r_k^n t^k\mathbb E e^{-tB_{m,n}},}
\tag{17}
\]

\[
L_{m,n}(t)^2-L_*(t)^2=2d_mr_k^nt^k\mathbb E e^{-tC_{m,n}}.
\tag{18}
\]

For every real `C^k` function on `R` with bounded kth derivative,

\[
\mathbb E f(X_{m,n})-\mathbb E f(X_*)
=(-1)^k d_mr_k^n\mathbb E f^{(k)}(B_{m,n}).
\tag{19}
\]

In particular the precisely defined smooth-test distance is

\[
\sup_{f\in C^k(\mathbb R),\ \|f^{(k)}\|_\infty\le1}
|\mathbb Ef(X_{m,n})-\mathbb Ef(X_*)|=d_mr_k^n.
\tag{20}
\]

Lower moments match, so arbitrary lower-degree polynomial parts cause no problem.

**Proof.** Subtract the two branching Laplace recursions and factor their difference of squares. Inserting (17), the factor `u^(-2k)` changes the uniform law to `U_k`, and the sum of the two Laplace transforms is twice the transform of `Y_{m,n}`. The resulting factor is exactly `2a_k=r_k`. This proves (17) by induction; (18) is its difference-of-squares product.

For completeness (19) is a distributional identity, not a claim about an arbitrary complex test function. If `beta_n` is the law of `B_{m,n}`, (17) identifies the signed difference of the two probability measures with `d_mr_k^n D^k beta_n`: their Laplace transforms coincide in `Re t>0`. To justify uniqueness, fix a positive real part and apply Fourier uniqueness to the exponentially weighted distributions. This first gives (19) on smooth compactly supported test functions. Smooth cutoff approximation extends it to `C^k` functions with bounded kth derivative, using polynomial growth, finite moments and dominated convergence. Those moments hold for `B_{m,0}` by its construction and then at every finite depth by (16). The upper bound in (20) follows. Taking `f(x)=x^k/k!` attains it. □

Equation (20) is stronger than an upper estimate on one moment. It still does not control signs of Fourier/Mellin transforms at arbitrary complex arguments.

## 5. The entire source error in Mellin coordinates

Set `c=pi/6`, `q=s/2` and

\[
F_{m,n}(s)=\tfrac12c^q\mathbb E(X_{m,n}+X_{m,n}')^q,
\qquad(q)_{\underline{k}}=q(q-1)\cdots(q-k+1).
\tag{21}
\]

### GTP5: exact source-bound Mellin defect

For every `Re q>0`,

\[
\boxed{F_{m,n}(s)-\xi(s)
=(-1)^k d_mr_k^n c^q(q)_{\underline{k}}\mathbb EC_{m,n}^{q-k}.}
\tag{22}
\]

Since `k` is odd, the sign before the right side is negative. In particular

\[
F_{1,n}(s)-\xi(s)
=-\frac4{175}(31/80)^n(\pi/6)^q q(q-1)(q-2)
  \mathbb EC_{1,n}^{q-3}.
\tag{23}
\]

**Proof.** For `0<Re q<1`, the Mellin–Laplace difference formula applied to the pair sums and (18) gives

\[
\frac{2d_mr_k^n}{\Gamma(-q)}
\int_0^\infty t^{k-q-1}\mathbb Ee^{-tC_{m,n}}dt
=2d_mr_k^n\frac{\Gamma(k-q)}{\Gamma(-q)}\mathbb EC_{m,n}^{q-k}.
\]

The gamma ratio is `(-1)^k(q)_underlined(k)`. Multiply by `c^q/2` and use the exact BPY identity (4).

All interchanges are paid for: near zero `k-Re q>0`; at infinity (17) implies `E exp(-tB_{m,n})<=1/(d_mr_k^n t^k)`. Thus `B_{m,n}`, and hence `C_{m,n}`, has inverse moments of every order less than `k`. Positive moments are finite. Both sides of (22) are holomorphic on `Re q>0`; continuation proves that full domain, including positive integers where the displayed polynomial vanishes. No assertion at the boundary `q=0` is needed. □

### Complete absolute error on the critical strip

Here is a bound with both probability tails included. All seeds, iterates and `X_*` have `E X^j<=j!` for integer `j>=0`. For seeds this follows from their cumulants and `x_i<1`; for iterates use the moment recursion and `(j+1)a_j<=1` for `j>=1`.

Also `L_{m,0}(t)<=1/(1+t)`, since `g_m(t)>=1/(1+t)`. The exponential seed is a supersolution of the branching recursion. One direct verification writes `J(t)=integral_1^2du/(u²+t)` and uses

\[
\frac1{1+t}-\int_1^2\frac{u^4}{(u^2+t)^2}du
=\frac t2\left[3J(t)-\frac1{1+t}-\frac2{4+t}\right]\ge0.
\]

For the sign, apply the endpoint chord bound for the concave function `a/(1+ta)` to `a=U^-2`, whose mean is `1/2` and range is `[1/4,1]`.

A depth-N tree has `2^N` exponential leaves and minimum weight `4^-N`. Monotonicity therefore gives, whenever `n>=N`,

\[
L_{m,n}(t),L_*(t)\le(1+t/4^N)^{-2^N}.
\]

For `0<p<2^N`, Tonelli's gamma integral yields

\[
\mathbb EX_{m,n}^{-p},\ \mathbb EX_*^{-p},\ \mathbb EC_{m,n}^{-p}
\le4^{Np}\frac{\Gamma(2^N-p)}{\Gamma(2^N)}.
\tag{24}
\]

The last bound uses `C>=Y`. Thus, for `0<sigma=Re s<1`, `p=k-sigma/2`, `2^N>k` and `n>=N`,

\[
|F_{m,n}(s)-\xi(s)|\le
 d_mr_k^n c^{\sigma/2}|(s/2)_{\underline{k}}|
 4^{Np}\frac{\Gamma(2^N-p)}{\Gamma(2^N)}.
\tag{25}
\]

This is a full-height **absolute** error, growing polynomially in `|Im s|`. It is not a relative estimate where xi is tiny and does not certify any zero location.

## 6. A hierarchy of independent limiting companions

For a fixed `k=2m+1`, the positive error variable converges to the perpetuity

\[
B_{k,*}=\sum_{j\ge1}\left(\prod_{i=1}^jU_{k,i}^{-2}\right)X_{*,j},
\qquad C_{k,*}=B_{k,*}+X_{*,0}.
\tag{26}
\]

These definitions use the explicit source (1), not zeros of xi. Put `b=a_(k+1)/a_k<1`. The series converges almost surely and in `L¹`, since its mean is `b/(1-b)`, and

\[
\mathbb EC_{k,*}=\frac1{1-b}.
\]

For the cubic seed,

\[
b=635/868,\qquad \mathbb EB_{3,*}=635/233,\qquad
\mathbb EC_{3,*}=868/233.
\tag{27}
\]

This is not the quadratic companion in #846, whose means are different.

To verify convergence, (3) gives `W_1(Y_(m,n),X_*)<=C(7/12)^(n/2)`. Couple affine recursions with the same `U_k`; the distance to (26) satisfies `e_(n+1)<=b e_n+b C(7/12)^(n/2)`, hence tends to zero. Uniform positive moments follow recursively from `E U_k^(-2j)<1` and the already bounded moments of `Y`. Uniform inverse moments of `C_(m,n)` at each fixed order follow eventually from (24); the limit has them because `C_(k,*)>=X_*`. Truncation to a positive compact interval, with these two tail bounds, proves local uniform convergence of Mellin transforms.

Consequently the rescaled errors in (22) have a specified limiting profile,

\[
r_k^{-n}(F_{m,n}(s)-\xi(s))\longrightarrow
(-1)^k d_m c^{s/2}(s/2)_{\underline{k}}\mathbb EC_{k,*}^{s/2-k}
\tag{28}
\]

locally uniformly on `Re s>0`. Its right side extends to an entire function. The finite-depth statement was only claimed on its established domain.

## 7. A rigorous obstruction to the easiest closing argument

A tempting extension of #850's single-gamma proof would make the symmetrized gamma hierarchy zero-safe by the same positive modulus-ratio derivative. That proposed invariant is false already at `m=2`.

Here

\[
p_2(a)=a^2-\tfrac23a+\tfrac4{105},\quad
x_- =\tfrac13-\sqrt{23/315},\quad x_+ =\tfrac13+\sqrt{23/315},
\]

\[
w_-=(x_+-2/5)/(x_+-x_-),\quad \beta_-=w_-/x_-,\quad
\beta_+=(1-w_-)/x_+,\quad\beta_-+\beta_+=7.
\]

Beta–gamma splitting of the pair sum gives its unnormalized Mellin transform

\[
M(s)=(cx_+)^q\frac{\Gamma(14+q)}{\Gamma(14)}A(q),\quad
A(q)={}_2F_1(-q,2\beta_-;14;1-x_-/x_+),\quad q=s/2.
\tag{29}
\]

This follows directly by writing the pair sum as `x_+ T(1-zV)`, where `T~Gamma(14,1)` and `V~Beta(2beta_-,2beta_+)` are independent. The beta integral of the binomial series gives (29).

Define

\[
D(t)=\left.\partial_\sigma\log\left|
\frac{M(\sigma+it)}{M(1-\sigma-it)}\right|\right|_{\sigma=1/2}.
\]

The enclosed value at `t=8` is strictly

\[
\boxed{-13/1000<D(8)<-11/1000.}
\tag{30}
\]

This is a statement about the proposed approximant, **not** an off-critical zero or a counterexample to RH. It also does not disprove zero-safety of this approximant; modulus monotonicity is a stronger sufficient mechanism.

### Directed certificate and its analytic remainder

Put `q=1/4+4i`, `a=57/4`, `b=2beta_-`, `z=1-x_-/x_+`. Then

\[
D(8)=\log(cx_+)+\Re\psi(a+4i)+\Re(A'(q)/A(q)).
\]

Use the series coefficients and their q derivatives

\[
c_0=1,d_0=0,\quad v_j=\frac{z(j+b)}{(j+14)(j+1)},
\quad c_{j+1}=(j-q)v_jc_j,\quad
 d_{j+1}=(j-q)v_jd_j-v_jc_j.
\]

The checker encloses their sums through `N=320`. It verifies `0<b<14`, `0<z<9/10`. For `j>=N`, the multiplier has modulus at most `19/20` and `|v_j|<=1/(N+1)`. If `C,D` enclose `|c_N|,|d_N|`, the entire omitted tails are at most `19C` and `19D+400C/(N+1)`, respectively. The nonzero denominator of `A'/A` is checked using its full complex rectangle.

For the digamma term, Binet's integral gives

\[
|\psi(w)-\log w+1/(2w)|\le1/[12(\Re w)^2].
\]

The underlying bound is `0<(1/2)coth(t/2)-1/t<t/12`; integrating against `exp(-Re(w)t)` proves the remainder. Thus evaluate

\[
\log(cx_+)+\tfrac12\log(a^2+16)-\frac{a}{2(a^2+16)}+\Re(A'/A)
\]

and widen by `1/(12a²)`.

Every arithmetic operation rounds outwards on a 288-bit dyadic grid. The square root uses integer square roots. Pi uses Machin's formula with alternating-series tails. Logarithms use a scaled atanh series with its full geometric tail. No floating special-function call is trusted. The resulting outward decimal enclosure is

`[-0.012270544269418342, -0.011449778905716176]`.

`check.py` binds that output to the source series and also rebuilds the rational orthogonal-polynomial fixtures. It is not a machine verification of the other analytic theorems.

## 8. The attempted RH ending and its exact missing theorem

Define the reflected, normalized source

\[
H_{m,n}(s)=\frac{F_{m,n}(s)+F_{m,n}(1-s)}{1+2F_{m,n}(1)}.
\tag{31}
\]

It is holomorphic on `0<Re s<1`, real-type, and symmetric under `s->1-s`. Its denominator is positive. For fixed `m`, (25) gives `H_(m,n)->xi` locally uniformly as `n->infinity`.

There is also a separate all-order limit `H_(m,0)->xi` as `m->infinity`. By GTP3 the seed laws converge weakly, with their first moment fixed. On a compact subset of the critical strip, the relevant powers have real parts bounded strictly between zero and one. The small-variable portion is bounded by a positive power of its cutoff; the large-variable portion is bounded by the fixed first moment times a negative power of its cutoff. Uniform convergence on the middle compact interval then proves convergence of the complete Mellin expectations. The normalizing expectations converge by the same argument.

Therefore either of the following would finish this route:

* for an unbounded sequence of `m`, the complete `H_(m,0)` is zero-free in the two open half-strips `0<Re s<1/2` and `1/2<Re s<1`;
* for one fixed `m`, the same statement holds for an unbounded sequence of branching depths `n`.

Hurwitz in each connected half-strip would make xi zero-free there. The limit is not identically zero, as its real-interior values are positive. Classical zero-strip localization and the functional equation then give RH.

**Neither zero-free statement is proved in this packet.** The single-gamma starting theorem in #850 covers only the first seed. Equations (10),(17),(20),(22) and (28) add full-source error geometry, not a complex zero-location invariant. Equation (30) eliminates the naive positive ratio-derivative extension even before the branching problem is addressed.

The next noncircular target is a zero-confinement or phase theorem derived from the specified gamma quadrature/branching laws and their positive companions. It must retain their oscillatory Mellin phases; replacing those transforms by their positive real-axis bounds does not suffice. Small absolute error near an exponentially small xi value likewise supplies no relative zero certificate.

## 9. Inspection and review boundary

The repository pass read the frozen main entrypoints and cumulative statement guide; inventoried 35 recently updated PR descriptions; read the #846 and #850 proof sources; inspected the source construction of #849; and read current programme bodies including #736–#741, #743, #744, #746, #763 and #764. It did not exhaustively audit every historical file, every new branch, every programme comment, or the full recent computation archive. Metadata-only findings are not promoted to mathematical acceptance.

The chosen connection is within the xi/Brownian/structure programmes. No estimate on native Möbius energy, no family-to-principal extraction theorem, and no arithmetic Hodge trace bound was established here. No existing status or claim identifier is changed.

For independent review, the load-bearing new steps are the Gaussian remainder normalization (8), the infinitely divisible mixture in (12), the exact signed distribution identity (19), the Mellin factor and domain in (22), and the complete error budget in (30). The finite checker authenticates rational fixtures and one directed diagnostic. It does not authenticate RH, all-order Mellin zero-safety, or the imported BPY source theorem.
