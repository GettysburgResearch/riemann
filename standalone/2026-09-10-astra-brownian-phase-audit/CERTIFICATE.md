# Complete-source certificate contract

This is a directed finite computation of one value of the **whole** native source. It is not a zero census, a proof of RH, or a finite-model substitute for the source. The paper derivations and the implementation remain subject to independent review.

## Arithmetic

Let Q=2^512. `B(a,b,e)` encloses all complex numbers differing from (a+ib)/Q by at most e/Q in the complex **L1 norm**. All a,b,e are Python integers and all radii are nonnegative. Exact rational scalings use `Fraction`. A floor in either center coordinate adds its outward error to the radius.

For multiplication, use submultiplicativity of the L1 norm. The radius numerator before division by Q is

```
(|a|+|b|)*f + (|c|+|d|)*e + e*f
```

for input radii e,f. For inversion put m=max(|a|,|b|); reject unless m>e. The perturbation of the exact reciprocal center has L1 radius at most

```
2*e*Q^2 / [m*(m-e)]
```

in integer units, in addition to both center-rounding errors. This follows by bounding the Euclidean distance from zero below by (m-e)/Q and then using L1<=2*Euclidean. All complex absolute-value analytic remainders below likewise acquire a factor two before entering an L1 ball. Remainders already bounded in L1, or positive real coefficient tails, need no further conversion.

Elementary functions are implemented explicitly:

* Square roots of positive rationals use `isqrt` on the scaled exact quotient, with an outward unit.
* Pi uses Machin's identity, with alternating arctangent tails. Positive real logarithms use powers-of-two reduction and the atanh series on [1,2], with its full geometric tail.
* Exponentials reduce the L1 input bound to <=1/2 by powers of two, retain degrees 0 through 128, bound the remaining L1 series by `2/(2^129*129!)`, and square with outward balls.
* The principal complex logarithm is used only in the right half-plane. At the center its real part is half the real log of the exact squared modulus, and its imaginary part is an arctangent of a rational. Reciprocal and pi/4 reductions reduce the arctangent argument to absolute value <=1/2; 256 terms have remainder <2^-512. The input perturbation contributes at most `2e/(a-e)` in L1 norm.
* Log gamma shifts the argument by 64, evaluates Stirling terms k=1,...,31 with exact Bernoulli numbers, and subtracts the 64 right-half-plane logarithms. All inputs have positive real part. The complex absolute remainder is bounded by `|B_64|/[64*63*64^63]` and is doubled for L1. DLMF 5.11(ii) bounds the remainder by the first neglected term times sec^(64)(arg(w)/2). For |arg(w)|<pi/2, `sec^(64)(arg(w)/2)<=sec^(63)(arg(w))`; this yields the stated bound from Re(w)>=64. No claim that principal log(Gamma(z)) equals the analytic log-gamma branch is required; exponentiation removes branch multiples in any case.

No floating-point value, external special-function implementation, or adaptive numerical integrator enters acceptance. Floats are used only when printing nonbinding progress diagnostics.

## Origin: the full laws, not truncated perpetuities

The coefficients `x_n=E X^n/n!` are reconstructed by inverting the series of `sinh(sqrt(-6t))/sqrt(-6t)`. The coefficients p_n for W come from equation (6) of PROOF.md, with the exact rational `b_n=a_(n+2)/a_2`. Convolution gives the coefficients of H and L^2. Computation through order 385 supplies the degree-384 origin integrals for H and the derivative of L^2.

For r0=1/2,

```
K_origin(q) = r0^(2-q) sum_(n=0)^384 i^n h_n r0^n/(n+2-q),
J_origin(q) = r0^(1-q) sum_(n=1)^385 [-n i^n z_n] r0^(n-1)/(n-q),
```

where z_n are the normalized moments of X+X'. Each remainder has L1 radius at most `1024*(2/3)^385`, using the radius-3/4 bounds |H|<=64 and |J|<=128 from the full moment majorants. Both integrals of the remaining real weight over [0,1/2] are <1 for the actual q values.

The initial value p(1/2) uses its moment series and the complete L1 tail

```
sum_(n>=385) (n+1) 2^-n = (384+3)/2^384.
```

## Every finite cell

All 4092 cells cover [1/2,512] consecutively, without overlap omission. Put h=1/8 and z=(r-r_j)/h. The final degree is N=80.

For the explicit source F(r)=1/L(-ir), `2rF''+3F'+3iF=0`. The constant coefficient is sinh(a)/a, with a=(1-i)sqrt(3r_j); the first coefficient is `h*(cosh(a)-F)/(2r_j)`. Higher coefficients satisfy

```
f_(k+2) = -[h(k+1)(2k+3)f_(k+1)+3i h^2 f_k]
             / [2r_j(k+2)(k+1)].
```

Formal series inversion gives the true coefficients ell_k of L(-ir) through order 81. Differentiating the full product L^2 gives the true J coefficients through order 80.

The delay r/4 lies in an already completed cell, or in the origin model. If the earlier-cell fractional offset is delta in {0,1/4,1/2,3/4}, its local variable is `delta+z/4`. Polynomial translation gives the delayed H coefficients. For nonzero delta, on |z|<=2 the earlier displacement is <=5/32. Its radius-1/2 Cauchy bound therefore bounds the omitted polynomial by

```
8*(5/16)^81/(1-5/16).
```

Cauchy on |z|=2 bounds the k-th omitted coefficient by that number times 2^-k; it is doubled for L1. At delta=0 the relevant coefficients are exact scaled earlier derivatives. When the delay lies in the origin model, the analogous bound is `256*(3/4)^385`, again doubled for L1 and multiplied by 2^-k.

Write the delayed coefficients as d_k. The exact equation (8) gives, sequentially,

```
H_k = sum_(j=0)^k ell_j p_(k-j),
p_(k+1) = [h*(24/7)*H_k - h*(3+2k)*p_k - h*(3/7)*d_k]
              / [2r_j(k+1)].
```

Thus each true derivative is enclosed; no finite recursion depth approximates the probability law. The next endpoint includes the complete P Taylor tail `4*(1/4)^81/(1-1/4)`, doubled for L1. True H and J Taylor tails on the cell use bounds 8 and 16 respectively, with the same geometric factor.

## Complex power integration

For alpha=1-q_1, 1-q_2, or -q_1 and u=h/r_j, integrate a source polynomial by

```
h*r_j^alpha sum_k f_k sum_n binom(alpha,n) u^n/(n+k+1).
```

Generate the binomial coefficients recursively. After n>=32, every subsequent ratio is at most 2u, because |alpha|<=|Re alpha|+|Im alpha|<31. Stop only when the first omitted coefficient's enclosing L1 bound is <=2^-230. Its entire tail is bounded by division by 1-2u, which is positive since u<=1/4. The source Taylor polynomial has modulus <=32; real-axis power moduli are bounded by r_j+1 or 2. All complex remainders are converted to L1 explicitly.

The complete true source Taylor tail is integrated separately, not treated as part of the binomial truncation. Thus neither an omitted source derivative nor an omitted power coefficient is discarded.

## Infinite tails, normalization, and acceptance

Equations (11)--(14) of PROOF.md bound the complete [512,infinity) contribution. These absolute bounds are doubled before adding them to the L1 integral balls. The log-gamma and exponential enclosures then give the two scaled constants in (10), and outward operations give the scaled A, B and product A*conj(B).

For `phase_scaled=(a,b,e)/Q`, the strict acceptance rule is the exact integer comparison

```
-4700000*Q < b-e  and  b+e < -4600000*Q.
```

There is no positive numerical tolerance or floating sign decision. The actual q values, scale, cell count, endpoint, moment order, both tail numerators and the resulting complex balls reside in result.json. `check.py --full` reconstructs the complete result from the primitive definitions and compares a canonical typed serialization. Duplicate keys are refused. A hash-only or internally self-consistent result is not sufficient.

## Remaining trust boundary

The elementary arithmetic, analytic remainder derivations, source identification and executable implementation are written and reviewable, not machine-verified in a proof assistant. The producer and checker have the same author. Exact finite controls and normal/optimized replays are not independent mathematical peer review. The external BPY identity and standard gamma remainder theorem are explicit imports. No full repository build, remote CI or Lean check is asserted.
