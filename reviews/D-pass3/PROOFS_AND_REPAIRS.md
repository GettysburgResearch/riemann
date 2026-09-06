# Reviewer D, pass 3 — proof reconstructions and scoped repairs

This is a review supplement, not a replacement for any frozen source. Source
labels S01–S29 resolve to full commit/path/blob identities in `SOURCES.tsv`.
The baseline main is `8d16f8d9c475db290bc85e53d775b93b9bcdb336`.
These deductions require independent integrator review before promotion.
No arithmetic positivity criterion implying RH is established here.

## R16. Xi-cardinal domain and complete-background capture (S01)

Use `Xi(z)=xi(1/2+iz)` and `fhat(z)=integral f(u) exp(izu) du`.
Let G consist of smooth functions for which every derivative times every
Gaussian weight is bounded. The theta source in GC2 belongs to G.
Here is a normalization and boundary audit of that assertion.

Put `psi(v)=sum_(n>=1) exp(-pi*n^2*v)` and
`F(u)=exp(u/2) psi(exp(2u))`. Jacobi's transformation gives

```
F(-u)=F(u)+sinh(u/2),   F'(0)=-1/4.
```

Thus `(D^2-1/4)F` is even. Direct differentiation on u>=0 gives exactly

```
Phi(u)=sum_n [4*pi^2*n^4*exp(9u/2)-6*pi*n^2*exp(5u/2)]
                 * exp(-pi*n^2*exp(2u)).
```

The transformed theta identity gives all matching derivatives at zero;
it is not enough merely to extend an arbitrary half-line function evenly.
Each differentiated positive-half-line summand has a polynomial factor
against its double-exponential tail. Comparison with a stronger tail makes
all Gaussian-weighted derivatives summable. The usual theta Mellin formula
for completed xi and two integrations by parts give

```
2 integral_0^infinity Phi(u)cos(zu)du
 =1/2-2(z^2+1/4) integral_0^infinity F(u)cos(zu)du
 =Xi(z).
```

This fixes the factor two in GC2. The classical inputs are Jacobi inversion
and the completed-xi Mellin identity, not a numerical zero verification.

For f in G with fhat(omega)=0 define

```
g(u)=-i exp(-i*omega*u) integral_(-infinity)^u exp(i*omega*t) f(t)dt
    = i exp(-i*omega*u) integral_u^infinity exp(i*omega*t) f(t)dt.
```

For either tail choose a Gaussian decay exponent stronger than the desired
one; the fixed factor exp(|Im omega|*|u|) is then harmless. Consequently g
has every Gaussian-weighted zeroth bound. The ODE `(iD-omega)g=f` supplies
all derivative bounds by induction. Integration by parts yields
`ghat=fhat/(z-omega)`, with the singularity removable. Division can be
iterated exactly through the multiplicity of omega: the intermediate
quotient still vanishes there until the last division.

Normalize the final quotient by its nonzero value at omega. Subtract the
corresponding quotient for conjugate omega. The resulting q belongs to G
and has Fourier values 1,-1 at that pair and zero at every other distinct
zero. Multiplicity gives Weil value `-2m`; it does not require simplicity.

For a>1/2, evaluation on H_a=L2(exp(2a|u|)du) has kernel
`4a/[4a^2+(z-conj(w))^2]`. For every finite distinct zero packet its Gram is
positive definite: a finite exponential polynomial vanishing on an interval
is zero, so all coefficients vanish. The minimum interpolation norm is
`t* K^-1 t`, and q supplies the common bound `||q||_H_a^2`. Schur elimination
of nuisance coordinates then yields

```
t_pair* S^-1 t_pair <= M,  S >= t_pair t_pair*/M.
```

The second conclusion is a rank-one inequality, not a uniform lower bound
for every direction of S. The constant depends on the chosen target pair.

For each finite packet, compact smooth functions have surjective evaluation:
density gives dense image, and a linear subspace of a finite-dimensional
space is closed. Select a finite evaluation right inverse. Compact cutoffs
of q converge in H_a and in

```
P(f)=integral exp(|u|/2)(|f|+|f''|)du.
```

Correct each cutoff by that right inverse; for a fixed packet the correction
converges to zero in both topologies. Diagonal selection is permitted only
after the packet is fixed. Two integrations by parts give
`|fhat(z)| <= C P(f)/(1+|z|^2)` on the zero strip. The standard O(T log T)
zero count makes the complete squared evaluation tail summable. Hence the
compact exact interpolants converge in the full Weil form to -2m.

For a smooth cutoff phi equal to one on the interpolant's support, extend
f/phi by zero where phi is zero. It is just the compact smooth f. Fourier
series on an enclosing interval of length L give coefficient squared norm
`||f||_2^2/L`. On each fixed packet the finite mode Gram converges to the
full Gram. Smooth periodic convergence also holds in the P topology after
multiplication by phi. A finite-mode evaluation right inverse, fixed after a
full-rank block is reached, corrects the residual interpolation errors.
This proves the asserted adaptable O(1/L) capture, not capture for a
prescribed fixed grid or arbitrary nuisance configuration.

Finally, for every sigma>0,

```
h=(1-D^2)(q/exp(-sigma*u^2)) belongs to L2,
J_sigma h=exp(-sigma*u^2)(1-D^2)^(-1)h=q.
```

The same holds after a fixed modulation. This discharges the previously
uninspected cardinal-range input used by the Gaussian Fredholm construction.
Its complete zero-side index argument still uses the specified Weil form;
none of these domain facts proves the prime-side lower floor. The earlier
D-F11 Fourier normalization repair remains binding.

## R17 / D-F12. The two annular core sets are not equivalent (S20)

L-95401.16 requires, in the odd squarefree annulus,

```
n-m>H,  gcd(m,n)<X/H.
```

L-95401.17 additionally requires `a=m/gcd(m,n)>H`. That condition is not a
change of variables. For X=1024,H=8,m=3,n=17 all conditions of .16 hold,
but a=3 fails .17. The checker also encloses both actual G numerators away from zero, so the
chosen pair is not an inactive kernel artifact. The same example works
for H=log(2048), which lies
strictly between 7 and 8; thus the issue is not confined to a nonallowed
choice of the later logarithmic cutoff.

A correct disjoint ownership rule is:

```
N: n-m<=H;
G: n-m>H and dH>=X;
S: n-m>H and dH<X and a<=H;
C: n-m>H and dH<X and a>H,
```

where H>=1, d=gcd(m,n), a=m/d, b=n/d. Every pair lies in exactly one class.
All classes retain X/1024<m<n<=X and odd squarefreeness. In gcd variables
retain `(a,b)=(a,d)=(b,d)=1`, `d(b-a)>H`, and the original intersection of
both activation intervals. The uniform annular estimate
`|G_X(m)|<=34560 log(2X)/sqrt(X)` yields

```
|N| contribution <= 2*34560^2 H log^2(2X),
|G| contribution <= 4*34560^2 H log^2(2X),
|S| contribution << H log^2(2X).
```

For S, count at most X/b possible d and use
`sum_(a<b<1024a)1/b <= log(1024)`. These are bounds on contributions,
not cardinalities as denoted by the first lines' words. For H beyond X,
the corresponding estimates follow trivially by the total pair count;
otherwise the standard reciprocal-square tail bound supplies G.

Thus .16 equals S union C, and the two CORRELATIONS differ by an explicitly
bounded S contribution. The final core can be used after that contribution
is charged to the error. The polylogarithmic or subpower criterion survives
this repair; no signed core bound is proved.

The diagonal must mean a sum over odd squarefree m, or must include
`mu(m)^2`. "Sign-free common divisor" means the factor mu(d)^2 has become
one on its support. It does not make the product of the two real kernel
weights nonnegative. In the counterexample above, the actual numerator of
G_X(3) is positive and that of G_X(17) negative, as certified by rational
intervals; thus an allowed individual common-divisor kernel weight is negative.

## R18 / D-F13. Repair the annular mean-square argument (S21)

The estimate

```
integral_(-T)^T |sum_m c_m m^(-it)|^2 dt
 <= (2T+C X) sum_m |c_m|^2
```

is valid. Its printed justification bounds the off-diagonal kernel in
absolute value by `2X/|m-n|` and then invokes Hilbert's inequality. That
argument has lost the cancellation Hilbert's inequality needs. Indeed the
matrix with off-diagonal entries 1/|j-k| has Rayleigh quotient on the
normalized constant vector

```
2 H_(N-1) - 2(N-1)/N,
```

which diverges. This is a proof repair, not a refutation of the estimate.
Here is a self-contained reduction to the ordinary L2 Hilbert transform.

For real delta-separated nodes lambda_j, put h=delta/2 and let I_j be the
disjoint intervals of length h centered at lambda_j. For finitely many c_j
set `f=sum c_j h^(-1/2) 1_(I_j)`. The unnormalized continuous Hilbert kernel
pv 1/(x-y) has L2 norm pi (Fourier multiplier of modulus pi). Dividing its
quadratic form by h shows that

```
|sum_(j!=k) c_j conj(c_k) A(lambda_j-lambda_k)|
 <= (2pi/delta) sum |c_j|^2,
```

where A(d) is the average of 1/(d+u-v) over the two length-h intervals.
The same-interval principal value is zero. The exact expansion

```
1/(d+s)=1/d-s/d^2+s^2/[d^2(d+s)]
```

and mean(u-v)=0, mean((u-v)^2)=h^2/6 give

```
|A(d)-1/d| <= h^2/(3|d|^3).
```

Here |d|>=delta and |u-v|<=h. Since sorted node distances are at least
|j-k|delta, the absolute row-sum error is at most

```
(2h^2/(3delta^3)) sum_(k>=1) k^-3
 <= h^2/delta^3 = 1/(4delta),
```

using sum k^-3 <=3/2. Consequently

```
|sum_(j!=k) c_j conj(c_k)/(lambda_j-lambda_k)|
 <= (2pi+1/4)/delta * sum |c_j|^2.
```

For lambda_m=log m and m<=X, the spacing is at least 1/X. The integrated
Dirichlet-polynomial off-diagonal is the difference, divided by i, of the
last signed forms with coefficients `c_m exp(+iTlambda_m)` and
`c_m exp(-iTlambda_m)`. Retaining these phases proves

```
integral_(-T)^T |P(t)|^2dt
 <= [2T+(4pi+1/2)X] sum |c_m|^2
 < (2T+14X) sum |c_m|^2.
```

For completeness, the multiplier modulus pi follows by damping 1/x:
`integral_0^infinity exp(-epsilon*x)sin(x*xi)dx/x=arctan(xi/epsilon)`,
as seen by differentiating in xi and fixing the value at zero. Letting
epsilon decrease to zero and using Plancherel gives the multiplier and
norm bound used above. This is Fourier analysis, not an arithmetic
cancellation theorem. The resulting O(X) loss still does not
prove a polylogarithmic estimate for the Q4 source.

Also, the literal large-prime split has p>sqrt(X) and d<sqrt(X). A reciprocal
coordinate for p is not an independent integer variable; the phrase "both
variables at most sqrt(X)" cannot justify a balanced integer Type-II estimate.
The displayed prime-divisor identity itself survives.

## R19 / D-F14. The column-one Riesz gauge has an activation range (S02)

For zero-extended sums define ell(X)=max(log X,0). If f(1)=1, the exact
identity for every X>0 is

```
R_f^full(X)=R_f^circle(X)+ell(X).
```

Combining this with the full-scale relation in L-90427.13 gives the gauge

```
-3sqrt(2) ell(X/2)+4ell(X/4).
```

Only for X>=4 does it equal

```
(4-3sqrt(2))log X+(3sqrt(2)-8)log 2.
```

At X=1 the full and deleted-column expressions are zero, while the expanded
printed gauge is strictly negative. Restore X>=4 (or the stronger earlier
X>=15 context) explicitly, or use ell everywhere. This does not invalidate
the fourteen-row computation or its large-endpoint applications. The
separate filtered renewal in L-90430 already states X>=16; retain that range.

## R20 / D-F15. Crossed poles have NET multiplicity (S12–S13)

A denominator zero rho gives a candidate pole of
`q^-1 xi(1+q)/xi(1+2a+q)` at q=rho-1-2a. Its order, away from deterministic
prefactors, is

```
max{mult_xi(rho)-mult_xi(rho-2a),0}.
```

The inequality Re(rho)-1/2>a locates a raw denominator zero relative to the
moving contour; it does not rule out a numerator zero there. S13 explicitly
cancels common factors first, repairing S12's stronger wording. Extraction
must use the successor's net-pole convention rather than combine the
uncorrected classifications.

An exact finite model shows the distinction. Let

```
E(z)=product_(d in {3/8,1/8,-1/8,-3/8}) [(z-d)^2+16],  a=1/8.
```

E is real and even, with all horizontal depths less than 1/2. Nevertheless

```
E(z-a)/E(z+a)=[(z-1/2)^2+16]/[(z+1/2)^2+16].
```

The candidate crossed pole 1/4+4i cancels exactly; the reduced quotient has
no right-half-plane pole. This is not a zeta function and does not preserve
an Euler product. It refutes raw divisor-to-pole inference from the displayed
symmetries alone, not RH or the successor's all-scale criterion.

The successor's dense-scale reduction can be justified without the false
principle that a dense set avoids every countable exceptional set. Fix one
actual hypothetical right-side zero. At its fixed ordinate there are only
finitely many distinct zeros in the compact critical strip. Therefore only
finitely many shifts a in a small interval can cancel that fixed zero.
Choose a rational scale in the remaining nonempty open set. Its net port is
nonzero. This proves the all-rational-scale absence criterion, not absence
of ports at every individual scale from a single zero.

For a pole-removed inner factorization, the four-term kernel equality follows
from `K_(FG)=K_F+F conj(F)K_G`. Scalar congruence preserves its three positive
terms. Their equality with the arithmetic Hankel source is still a separate
common-domain intertwining problem. The finite algebra does not construct
that intertwiner. Symmetric Hadamard/Blaschke convergence and the no-adverse-
exponential factor are the standard analytic inputs to the stated inner
factorization; the identities after that factorization do not prove it by
themselves.

## R21. Literal P61 base has the required weighted variation (S16–S18)

The exact unsieved dictionary is

```
q*(1)=0, q*(2)=15, q*(3)=6, q*(4)=3, q*(n)=6 for n>=5.
H_x(n)=min(log 4,log(x/n))_+,
A*(x)=sum q*(n)n^(-1/2) H_x(n).
```

If `S(x)=sum_(n<=x) n^(-1/2)log(x/n)`, then directly

```
A*(x)=6[S(x)-S(x/4)]-6H_x(1)+(9/sqrt(2))H_x(2)-(3/2)H_x(4).
```

For x>=16 the exceptional hinges saturate. The Hurwitz Euler–Maclaurin
formula used in S18 gives

```
S(x)=4sqrt(x)+zeta(1/2)log x+zeta'(1/2)+R(x),
|R(x)|<5x^(-3/2).
```

The source's remainder proof is checked as follows. Put a=floor(x)+1 and
h=log(a/x)<=1/(a-1). The three elementary terms of a^(3/2)R have total
absolute bound at most 2+1+1/12<25/8. The differentiated periodic-Bernoulli
remainder has bound `1/9+h/24+1/36<1/5`. This establishes the stated loose
constant 5. Differentiation in the complex exponent is justified by an
integrable logarithmic tail in a neighborhood of 1/2. No special-function
value is numerically evaluated in this argument.

It follows that

```
A*(x)=12sqrt(x)+C0+O(x^(-3/2)),
C0=[6zeta(1/2)-15/2+9/sqrt(2)]log4.
```

Independently, on every open activation cell above 16,

```
D_log A*(x)=6 sum_(x/4<n<x) n^(-1/2)
          =6sqrt(x)+O(x^(-1/2)).
```

Endpoint conventions affect only a measure-zero set for this derivative.
The last estimate follows from monotone integral comparison on an interval,
with endpoint error bounded by a constant times x^(-1/2). It is not obtained
by differentiating an undifferentiated big-O remainder.

Let P=product_(p<=61)p, and define the ACTUAL fixed-base source

```
b(x)=sum_(d|P) mu(d)d^(-1/2) A*(x/d),   h(x)=b(x)/sqrt(x).
```

Above 16P every fixed color is active, and the finite sum gives

```
b(x)=a*sqrt(x)+c*+O_P(x^(-3/2)),
D_log b(x)=(a*/2)sqrt(x)+O_P(x^(-1/2)),
a*=12 product_(p<=61)(1-1/p)>0.
```

Hence

```
D_log h(x)=-c*/(2sqrt(x))+O_P(x^-1),
integral_[1,infinity) x^eta |dh(x)| < infinity  (0<=eta<1/2).
```

On compact intervals all sums are locally finite continuous ramps, so h is
locally absolutely continuous. It has h(1)=0 and limit a*, and the total
signed mass of dh is a*. These facts prove the weighted-variation premise
previously retained in D2-U026/D2-U027, without assuming the finite global
bias campaign or positivity of the signed measure dh. Constants can depend
on the fixed P61 base; this is not uniform in a growing primorial.

The exact Stieltjes transport follows even more directly by finite Fubini:
write each h(Y/m) as the integral of dh up to Y/m and interchange. The
coefficient at x is precisely the literal rough prefix A_z(Y/x). This
retains endpoints and signs. The prior Dickman/Vinogradov–Korobov comparison
still needs its named classical estimates and moving-parameter ranges;
weighted variation does not reach the fixed-small-prime critical region.

At X=184 the new independent interval checker reconstructs this literal
source by divisor convolution and proves `40F-M<-18` and `42F-M>3`.
It uses integer square roots and an atanh logarithm series, not the original
MPFR/long-double implementation. It confirms the known local refutation of
1/40, not the global 1/42 theorem or the million-endpoint computation.

## R22. Green hierarchy and the missing between-knot argument (S08–S11)

For finitely many primes use independent geometric exponents with weights
proportional to 1/n. Both F_s(n)=product_(p|n)(1-p^-s) and a decreasing
nonnegative h(n) are decreasing in each exponent. The one-coordinate
covariance identity and induction give Harris association; truncate the
geometric exponents and then pass by bounded convergence. Cancelling the
normalizing product proves the source's weighted inequality. Its strict
second inequality requires h not identically zero. For m=0 the truncated
power is an activation indicator; it is not the everywhere-defined value
0^0. These conventions give the nonnegative E_(s,m), its Laplace transform,
and the safe half-plane Gram exactly as stated.

The cubic boundary-jet formula includes the unit contact rho''(0)=1.
All positive atoms at log n, n>=2, and the continuous density
`B=-c+(A+B)E0+AB E1` must be kept. It is not legitimate to differentiate
only its open-cell smooth density and drop contacts.

S09 first proves the affine lower envelope

```
B_(2a,a)(t)>c[-1+kappa*a*delta+4a^2*delta*t+2a^2*(log2)^2]
```

at knot left limits, where delta=1-log2. To extend it throughout t>=log2,
compare on each closed cell with the chord of the two one-sided values.
B is concave within the cell. At its left endpoint the jump is positive,
so the starting value also exceeds the SAME affine lower envelope. Both
endpoint comparisons imply the interior comparison. This fills the omitted
step in using a knot estimate as a pointwise threshold theorem.

For a>=1/2 this affine expression is increasing in a and t. Its minimum is
at a=1/2,t=log2. As a function of L=log2 that expression decreases on
[.693,.694] when kappa>=4.43; therefore substituting kappa=4.43,L=.694 gives
`32743/250000>13/100`. First-cell positivity handles t<log2. Thus the
terminal-scale theorem survives with an explicit positive margin.

For small s>0 the positive measures e_s(y)dy have Laplace transforms tending
to 1/z. Positive-measure Laplace continuity gives I_s(y)=integral_0^y e_s
converging locally uniformly to y. Since e_s+r_s y is nondecreasing, a fixed
pointwise downward deficit would persist on a fixed preceding interval,
contradicting that integrated convergence. This proves the uniform lower
liminf on every compact interval away from zero. The near-zero quadratic
bound is positive up to y=.7 (lower bound 239/1000 using kappa>4.43).
I_s(2)>1.5 eventually covers all y>=2. Together they prove existence of
s0 with full-time positivity for 0<s<s0. This is non-effective as stated:
no numerical s0 or exhaustive compact-middle certificate is supplied.

## R23. Recovered C4MBI and endpoint source identities (S23–S28)

The row coefficients of 5Q2+3Q3 are exactly q* from R21. In convolution form

```
q*=6*1-6*delta1+9*delta2-3*delta4,
mu*q*=6*epsilon-6*mu+9*delta2*mu-3*delta4*mu.
```

This derives the sparse dictionary of S23, including the unit term, rather
than assuming it from a programme slogan. Finite Fubini gives

```
sum mu(n)n^-1/2 H_Y(n)=integral_(Y/4)^Y B_(1/2)(t)dt/t.
```

Combining the three scaled hinges gives the four coefficients of S23.8.
The new checker verifies this for each source atom as an exact formal
prime-log identity, including subunit and activation endpoints. For
squarefree n>1, `mu(n)log n=-sum_(p|n)mu(n/p)log p`. This gives the exact
prime-owner decomposition with p not dividing the cofactor, and unit term
kept separately. It does not prove the resulting one-sided inequality.
The root Bellman equivalence in T-97701 is conditional algebra on its stated
parent identities U_full=U_Z-I-T=A/sqrt(X); those parent definitions were
not all reconstructed this pass. A root identity is not a descendant bound.

For the native endpoint, finite adjoint inversion gives

```
<Y4,D4(w-C_d)>=sum_q Lambda(q)(w(q)-C_d(q))
             =P_Lambda-H(d).
```

Consequently `J_Lambda-H(d)=F_Lambda+P_Lambda-H(d)`. The benchmark term is
not removed by improving the physical packing error. The general affine
cell formula is proved by the weighted mean of s^-1/2 between its two
endpoint values. Specify a<b and positive finite mass; zero mass has zero
integral and needs no division. Actual row geometry and primitive directed
fixtures remain separate inputs. No global native feasibility is inferred.

## R24. Scope of the Cauchy three-square recurrence (S29)

Direct common-denominator algebra gives the numerator
`y(378y^2+4401y+6048)` in the residual d_a-d_(2a)/16. The three rational
squares in S29 are therefore exact on real frequencies. Multiplication by
a^-4 turns the return coefficient into one. Finite telescoping followed by
the vanishing terminal term gives the all-generation scalar frame at each
fixed real frequency. This does not assert positivity on complex zero
coordinates.

Fourier inversion of n_a gives `(a/4)(1+a|t|)exp(-a|t|)` and exactly the
three-exponential residual in the source. Its integral is zero while its
value at zero is positive; it is not a pointwise nonnegative density.
It IS a positive-definite autocorrelation sum. Insertion of the arithmetic
prime weights is an additional signed operation and receives no positivity
from this identity alone.
