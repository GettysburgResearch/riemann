# Numerical contract and analytic remainder proofs

**These are finite computer-assisted component certificates, not formal proofs
of the infinite theorems.** The programs use Python's standard library only.
No floating arithmetic, zeta/gamma evaluator, zero table, fitted moment receipt
or predecessor executable enters accepting reconstruction. Normal and optimized
runs use the SAME implementation and are not independent referee acceptance.

## 1. Elementary arithmetic

exact_interval.py represents outward intervals with integer endpoints in units
2^-512. Rational-to-interval conversion rounds in both directions. Products,
reciprocals and square roots use integer division and isqrt. Exponentials are
reduced to [0,1/8], summed through order 100, with the remaining positive series
bounded by the next term divided by 1-x/102, then squared outward. Negative
exponents use reciprocals. For x<=-512, [0,2^-512] is valid since e>2.

Pi uses Machin's formula and 128 alternating arctangent terms with the full
first-omitted-term error. Logarithms use powers-of-two reduction to [1,2],
256 terms of the atanh expansion, and remainder
2 z^513/[513(1-z^2)]. No optimized-away assert implements acceptance.

## 2. Complete native theta moments through degree twenty

native_theta.py applies the WHOLE-LINE trapezoidal rule with step 1/128,
retaining |t|<=3 and theta indices n<=20. This is a computational partition of
the full source, not its definition. Jacobi's classical transformation makes
phi an even analytic function for |Im t|<pi/4. That identity is an analytic
input, not inferred from reflection of truncated theta sums.

For j=0,...,20 even, let f_j(z)=z^j phi(z). On |Im z|<=1/4 and Re z=x>=0,
cos(2 Im z)>=7/8, pi>3, pi<4, and

    |f_j(z)| <= 2^8 j! sum_(n>=1) n^4 exp(6x)
                                      exp[-(5/2)n^2 exp(2x)].

We used |z|^j<=j!exp(x+1/4)<2j!exp x, and bounded both signed prefactor terms
in absolute value. Substitution u=exp(2x), evenness and sum n^-2<2 show that
each full boundary-line L1 norm is less than 2^16 j!. Horizontal decay
justifies the analytic-strip contour proof of the trapezoidal alias estimate:

    |h sum_(k in Z) f_j(kh)-integral_R f_j(t)dt|
                  <= 2^17 j!/[exp(2pi(1/4)/h)-1].

For h=1/128, pi>3 and exp(3/4)>2 imply exp(64pi)>2^256. Thus the complete
alias error is less than j! 2^-238. The second allowed mesh, 1/160, has a
strictly stronger alias bound. The programs retain the same conservative
final bound for both.

### Both omitted spatial lattices

For real t>=3, the preceding bound is at most
2^10 j! exp(6t-(5/2)exp(2t)). This follows by bounding the full positive sum
over n using n^4<=exp(n^2) and a geometric majorant. Since exp(6)>400, its value
at 3 is below j! 2^-900. Its logarithmic derivative for t>=3 is at most
6-5exp(6)<-1994, so successive lattice terms, at either allowed step, have
ratio <1/2. Multiplying the full geometric tail by both step/reflection factors
is still less than j! 2^-505. Negative t has the same bound by Jacobi evenness.

### Every omitted theta index

On the retained real grid, t^j<=j!exp(t), and each n-th summand is bounded by
88 j! n^4 exp(6t-3n^2 exp(2t)). The exponential decreases for t>=0. For n>=21,
n^4<=2^n and e>2 make the remaining n-sum smaller than a geometric sum with
first term 88 j! 2^(21-3*21^2). Paying the complete grid length (<7) gives a
bound much smaller than j! 2^-383. No theta tail is dropped at a large n.

The three analytic errors together are less than j! 2^-237, which is added
to EACH raw moment interval. All elementary-function and summation rounding
is already separately outward in the interval calculations. The normalizing
integral is enclosed away from zero before division. Exact moment–cumulant
recursion then gives the native cumulant intervals.

## 3. The complete calibrated-chain tail

For integers s>1 and 0<=j<=8 put

    U_(s,j)=sum_(n>=32) n^-s (log n)^j.

The program sums through M=1024, adds the exact infinite integral, -f(M)/2,
-B2 f'(M)/2!, and -B4 f'''(M)/4!. It retains BOTH the omitted B6 boundary term
and the entire periodic-B6 remainder. With

    f^(k)(x)=x^(-s-k)P_k(log x),
    P_0(t)=t^j,  P_(k+1)=P_k'-(s+k)P_k,

an absolute error is

    |f^(5)(M)|/30240
      +(1/30240) integral_M^infinity
                   x^(-s-6) sum_l |[t^l]P_6| (log x)^l dx.

Here |B6({x})|<=1/42, for example from the absolutely convergent Bernoulli
Fourier series and its value at zero. The logarithmic integrals are explicit:

    integral_M^infinity x^-s(log x)^j dx
      =M^(1-s) sum_(l=0)^j j! (log M)^(j-l)/[(j-l)!(s-1)^(l+1)].

Every signed term in T_k=sum_(j=0)^k binom(k,j)2^(-(k-j)) d0^j U_(k+j,j)
is then retained by interval arithmetic. No alternating cancellation is used
to understate an absolute remainder. In particular the B6 boundary term is
NOT forgotten when only the B4 expansion is displayed.

Euler's constant uses M=4096 and

    H_M-log M-1/(2M)+1/(12M^2)-1/(120M^4)+1/(252M^6),

with absolute error at most 1/(240M^8), the standard signed harmonic
Euler–Maclaurin remainder. This and log2 evaluate A0 and d0 in (9) of ISING.md.

The entire native theta target, tail sums, center residuals, 16 exact inverse
identities, whole-box Jacobian and the complete eighth-moment mismatch are
reconstructed each time. The analytic positive-q continuation is proved in the
manuscript, not by a finite q grid. Its radius remains unevaluated.

## 4. Arithmetic and gamma scope

The arithmetic checker includes every coefficient and integer annular cell in
its finite native cases. Logarithms are outward, while its Newton identities
and total squared Q energy are exact rational calculations. A finite negative
C value is never promoted to a sign at unbounded crossings.

Gamma density-jet and score-derivative identities are checked against a second
finite algebraic representation, with exact rational shape parameters. The
positive-series evaluator pays its whole future by the Poisson/geometric
majorants in GAMMA.md. The root-current factors are checked algebraically.
No actual gamma Fourier zero, continuous zero track, new contour certificate,
whole signed-production integral or extinction bound was computed.

## 5. Authentication versus mathematical validation

The manifest records local packet byte identities. The accepting command first
checks that inventory, then reconstructs the result from source primitives and
compares typed canonical JSON. Hashes do not prove mathematics or protect
against an adversary replacing the entire checker and its manifest. Mutation
tests distinguish those scopes. All infinite statements still depend on the
written proofs and their explicitly credited classical/predecessor imports.
