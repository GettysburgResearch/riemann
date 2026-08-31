# Pure Blaschke height is equivalent to finite bare low-pass trace

Status: PROPOSED ANALYTIC THEOREM; independent exact-SHA review required.
Scope: any pure upper-half-plane Blaschke product, including boundary
accumulation and repeated zeros. This is a BARE low-pass result, with U=1.
No meromorphic continuation across the real line is needed. RH remains open.

Frozen inputs: HC6--HC7 and the finite-divisor exhaustion in HC Section 3
at 90e8dff3d184cbfe59974969ca89615856c33c51; the conditional actual-Xi
component heights GH3 at 9da33e7ea2b15a4badb3cb436e38e54762ad5e1d.
Both complete notes are authenticated. Their proofs are not modified.
The analytic argument below is not machine-certified by its finite controls.

## 1. Exact theorem and normalization

Identify H^2(C+) with L^2(0,infinity) by the unitary convention
\[
 f(z)=(2\pi)^{-1/2}\int_0^\infty h(t)e^{izt}\,dt.             \tag{LP1}
\]
Boundary measure is dx, with no further factor. For a pure Blaschke B with
zeros b_j=a_j+i eta_j, eta_j>0, repeated according to multiplicity, set
\[
 S(B)=\sum_j\eta_j,\qquad K_B=H^2\ominus BH^2,\qquad
 A_L(B)=\operatorname{tr}(\Pi_{[0,L]}P_{K_B}\Pi_{[0,L]}).
                                                                  \tag{LP2}
\]
Traces are extended nonnegative traces. A unimodular constant B has S=A_L=0.

**Theorem.** The following statements are equivalent:

1. S(B)<infinity.
2. A_L(B)<infinity for at least one L>0.
3. A_L(B)<infinity for every L>0.
4. For at least one y>0, integral_R (1-|B(x+iy)|^2) dx is finite.
5. The same integral is finite for every y>0.

In the finite case, A_L(B)<=2L S(B). In particular,
\[
 \boxed{S(B)=\infty\ \Longrightarrow\
             A_L(B)=\infty\text{ for EVERY }L>0.}          \tag{LP3}
\]
This conclusion concerns intervals starting at zero. It does NOT imply
infinite trace on every shifted or shrinking band. Section 6 gives a
pure meromorphic counterexample to that stronger claim.

A compatible nonnegative, decreasing, extended diagonal k_B(t) exists and
obeys, for all y>0, the exact identity in [0,infinity],
\[
 \boxed{\int_0^\infty e^{-2yt}k_B(t)\,dt
     =\int_{\mathbb R}\frac{1-|B(x+iy)|^2}{4\pi y}\,dx.}    \tag{LP4}
\]
Here A_L(B)=integral_0^L k_B(t)dt. Neither side of LP4 is assumed finite.

## 2. Finite diagonals, compatible exhaustion, and monotonicity

For a finite product, the inverse Fourier model space is spanned by
w_(j,r)(t)=t^r exp(-(eta_j+i a_j)t)/r!, 0<=r<m_j.
These are independent; let w be their row, G=integral_0^infinity w^*w dt,
w'=wA, and c=w(0). Thus G is positive definite. Integration by parts gives
\[
 A^*G+GA=-c^*c,\quad
 k(t)=w(t)G^{-1}w(t)^*,\quad
 k'(t)=-|w(t)G^{-1}c^*|^2\le0.                            \tag{LP5}
\]
Indeed multiply the first identity on both sides by G^(-1) to substitute
A G^(-1)+G^(-1)A^* in the derivative of k. Taking a trace after multiplication
by G^(-1) also gives
\[
 k(0)=cG^{-1}c^*=-\operatorname{tr}(A+A^*)
                =2\sum_jm_j\eta_j.                       \tag{LP6}
\]
Consequently the finite trace is integral_0^L k(t)dt<=2LS.
This retains confluent poles and all real parts; no separation is assumed.

Choose any enumeration with multiplicity and finite subproducts B_n whose
zero divisors increase to the complete divisor of B. Unimodular normalizing
constants do not affect their model spaces or moduli. The spaces K_(B_n)
increase and their union is dense in K_B: a Hardy function perpendicular
to the union belongs to every B_n H^2, so its inner factor contains every
zero of B with its multiplicity. Canonical Hardy factorization then makes
it divisible by the PURE factor B. Thus the orthogonal complement is BH^2.
No geographic local-finiteness hypothesis at the boundary was used.

Choose compatible orthonormal bases of these nested finite spaces; their
inverse transforms are continuous exponential polynomials. Then
\[
 k_n(t)=\sum_{\ell\le\deg B_n}|h_\ell(t)|^2
 \uparrow k_B(t)=\sum_{\ell\ge1}|h_\ell(t)|^2.              \tag{LP7}
\]
Every k_n is decreasing by LP5, hence the extended limit is decreasing.
Tonelli and the orthonormal-basis definition of the Hilbert--Schmidt norm
give
\[
 A_L(B)=\|\Pi_{[0,L]}P_{K_B}\|_{\mathcal S_2}^2
       =\int_0^L k_B(t)dt
       =\lim_n A_L(B_n).                                 \tag{LP8}
\]
All equalities allow infinity. In particular finite S proves statement 3
and its bound without assuming trace-class convergence in advance.

## 3. The weighted trace bridge

The reproducing kernel for our boundary dx normalization is
\[
 K_B(z,w)=\frac{i}{2\pi}
            \frac{1-B(z)\overline{B(w)}}{z-\bar w},\qquad
 K_B(z,z)=\frac{1-|B(z)|^2}{4\pi\Im z}.                    \tag{LP9}
\]
For completeness the Hardy kernel is
(2pi)^(-1) integral_0^infinity exp(i(z-bar w)t)dt
=i/[2pi(z-bar w)]. Its projection onto BH^2 is
B(z)bar B(w) times that kernel because multiplication by inner B is an
isometry. Subtraction proves LP9 and fixes the factor 4pi.

For each basis vector with transform h_l, evaluation at x+iy is the Fourier
transform of exp(-yt)h_l(t). Plancherel therefore gives
\[
 \int_{\mathbb R}|f_l(x+iy)|^2dx
       =\int_0^\infty e^{-2yt}|h_l(t)|^2dt.
\]
The model-kernel identity sum_l |f_l(z)|^2=K_B(z,z) follows by Parseval
for the bounded evaluation functional. Sum the displayed identities and
apply Tonelli on both sides to prove LP4. Alternatively prove it for
each B_n and use k_n increasing and
1-|B_n(z)|^2 increasing to 1-|B(z)|^2. No interchange of signed series,
conditional integral, or unbounded inverse Gram is involved.

If A=A_L(B)<infinity, monotonicity gives k_B(t)<=A/L for t>=L. Hence
\[
 \int_0^\infty e^{-2yt}k_B(t)dt
 \le A+\frac{A}{2yL}e^{-2yL}
 \le A(1+(2yL)^{-1})<\infty.                              \tag{LP10}
\]
Conversely, finiteness of the weighted integral implies
A_L(B)<=exp(2yL) integral_0^infinity exp(-2yt)k_B(t)dt.
These are analytic inequalities, not numerical exponential evaluations.

## 4. Horizontal defect integrability forces finite height

Fix y>0 and write q_y(x)=1-|B(x+iy)|^2. It is continuous, nonnegative,
and at most one. Schwarz--Pick in the half-plane gives
\[
 |B'(x+iy)|\le\frac{1-|B(x+iy)|^2}{2y},\qquad
 |q_y'(x)|\le1/y.                                        \tag{LP11}
\]
One direct derivation composes B with the disk map
z=x+iy(1+w)/(1-w), whose derivative at w=0 is 2iy, and the disk
automorphism carrying B(x+iy) to zero. Schwarz's lemma gives LP11.
A constant unimodular product is handled separately.

Suppose q_y is integrable. A nonnegative integrable uniformly Lipschitz
function tends to zero at both infinities: if q_y(x_n)>=epsilon along
an unbounded sequence, the Lipschitz bound makes q_y>=epsilon/2 on
[x_n-epsilon*y/2,x_n+epsilon*y/2]. An infinite disjoint subsequence of
these intervals contributes at least epsilon^2*y/2 each, a contradiction.
Thus outside some compact interval q_y<=1/2, where
\[
 -\log|B(x+iy)|=-\tfrac12\log(1-q_y(x))\le q_y(x).          \tag{LP12}
\]
Inside that compact interval B is holomorphic in a neighborhood of the
horizontal segment and not identically zero. It has finitely many zeros
there; locally at a zero of order m, log|B(x+iy)| is m log|x-x_0|
plus a bounded continuous term. These logarithmic singularities are
integrable. No continuation across the REAL axis is required.
It follows that integral_R -log|B(x+iy)|dx<infinity.

For one zero b=a+i eta the modulus of its factor gives
\[
 -\log|\beta_b(x+iy)|
 =\tfrac12\log\frac{(x-a)^2+(y+\eta)^2}
                         {(x-a)^2+(y-\eta)^2},
\]
and, exactly,
\[
 \int_{\mathbb R}-\log|\beta_b(x+iy)|dx
                    =2\pi\min(y,\eta).                   \tag{LP13}
\]
To verify the integral including y=eta, put u=|y-eta| and v=y+eta.
Write the half-log ratio as integral_u^v t/((x-a)^2+t^2)dt.
Tonelli and integral_R t/(x^2+t^2)dx=pi for t>0 give pi(v-u).
The endpoint t=0 is a measure-zero endpoint, not an omitted logarithmic
divergence. The case a arbitrary follows by translation.

For a PURE product, negative log moduli add as nonnegative extended
functions. Tonelli therefore proves
\[
 \int_{\mathbb R}-\log|B(x+iy)|dx
                    =2\pi\sum_j\min(y,\eta_j).            \tag{LP14}
\]
The last sum is finite if and only if S(B) is finite. In one direction,
min(y,eta)<=eta. In the other, a finite sum permits only finitely many
eta_j>=y, whose individual heights are finite, and the remaining sum is
exactly their height sum. This proves statement 4 implies statement 1.
Statements 1=>3=>2=>5=>4, using LP4/LP10, finish the theorem.

One-factor normalization check: q_y(x)=4y eta/
((x-a)^2+(y+eta)^2), so the right side of LP4 is eta/(eta+y),
equal to integral_0^infinity 2eta exp(-2(eta+y)t)dt.

## 5. Inner numerators and singular denominators remain separate

Nothing above supplies a lower bound for
T_[0,L](B,U)=||Pi_[0,L] M_U P_(K_B)||_HS^2 or for the corrected physical
C_[0,L](B,U)=||Pi_[0,L] P_(UH^2) P_(K_B)||_HS^2.
For U(z)=exp(i tau z), tau>=L, multiplication shifts every waveform
right by tau. Therefore
\[
 T_{[0,L]}(B,U)=0                                        \tag{LP15}
\]
for EVERY B, including products of infinite height. In this particular
example P_(UH^2)=Pi_[tau,infinity), so the physical C trace is also zero.
This is a genuine infinite-rank countercontrol to any proposed numerator-
independent converse. It is not the native Xi numerator.

Purity is essential to the equivalence's sufficiency: B=exp(i tau z),
tau>0, has no zeros but K_B=L^2(0,tau), with infinite trace on [0,L]
for every L>0. The theorem does not bury this singular mass in S=0.

## 6. Why shifted bands cannot be inferred

There is a pure MEROMORPHIC example with S=infinity but finite bare trace
on every [A,D] with 0<A<D<infinity. Put eta_n=256^n, n>=1, and
\[
 B(z)=\prod_{n\ge1}\frac{1+iz/\eta_n}{1-iz/\eta_n}.
                                                                  \tag{LP16}
\]
This is a pure Blaschke product: sum eta_n/(1+eta_n^2)<infinity.
The displayed factors converge locally normally off their lower-plane
poles since sum eta_n^(-1)<infinity; in particular B extends across every
finite real point. It has precisely the zeros i eta_n, and S=infinity.

The normalized kernels at these zeros have inverse transforms
v_n(t)=sqrt(2eta_n) exp(-eta_n t). Their Gram entries are
2sqrt(eta_n eta_m)/(eta_n+eta_m). For n!=m they are <=2*16^(-|n-m|), so
\[
 \sup_n\sum_{m\ne n}|G_{nm}|\le4/15,\qquad
             (11/15)I\le G\le(19/15)I.                   \tag{LP17}
\]
The synthesis operator V is bounded above and below. Its closed range
is K_B: orthogonality to all kernels means vanishing at all the simple
zeros, hence divisibility by B; intersection with K_B is zero. Thus
P_(K_B)=V G^(-1)V^*, with these bounded operators on the entire space.
For A>0, Tonelli and the upper inverse bound give
\[
 \operatorname{tr}(\Pi_{[A,D]}P_{K_B}\Pi_{[A,D]})
 \le\frac{15}{11}\sum_{n\ge1}
       (e^{-2A256^n}-e^{-2D256^n})
 \le\frac{15}{11}\sum_{n\ge1}e^{-2An}<\infty.              \tag{LP18}
\]
The convergence follows from 256^n>=n. In contrast the lower inverse
bound gives infinite [0,L] trace directly because each summand
1-exp(-2L256^n) tends to one. This is compatible with LP3.
No sampled exponentials or eigenvalues are used as a proof of these limits.

## 7. Conditional actual-Xi consequence and replay scope

Under exactly GH's inner/RH premise and each separately fixed lambda>0,
the unreduced Theta_(0,lambda) and Theta_(5,lambda) are pure and each has
infinite height. LP3 therefore gives infinite BARE [0,L] trace for each
component and every L>0. This is not an unconditional RH result.

GH4 still allocates the native ratio as Theta_0/Theta_5. Its maximal common
inner divisor may remove infinite height; GH's reduced-height dichotomy
remains unresolved. The present theorem neither determines the reduced
denominator nor controls the native inner numerator, corrected P_U source,
outer-normalized jets, arbitrary shifted/shrinking bands, cofinal physical
limits, total charge, reverse-Rolle descent, or critical-line density.

The exact finite producer checks confluent real-height Grams, Lyapunov and
origin identities, and the weighted bridge by TWO different algebraic routes:
a shifted Gram trace and a partial-fraction integral of the finite product
defect. The latter uses
integral_R (x^2+a^2)^(-j)dx/pi
=binom(2j-2,j-1)/(4^(j-1)a^(2j-1)), following by differentiating the
j=1 Cauchy integral. Rational one-factor/product, logarithmic-integral,
Lipschitz-area, tail-coefficient, delay and lacunary-Gram controls are included.
They do not evaluate logarithms, exponentials, Xi, or analytic limits.

Arithmetic is MIXED: EXACT_RATIONAL and CERTIFIED_INTEGER_COVERAGE, no
rounding. Public rational inputs have <=32-bit numerator/denominator and
bounded stated domains; internal rationals <=4096 bits; confluent degree<=4,
lacunary prefix<=8, local charged work<=200000, UTF-8 JSON/source/artifact
bytes<=2000000. Complete typed reconstruction, primitive hashes, four
artifact hashes, duplicate/nonfinite JSON rejection and strict bool/int
separation are required in normal and optimized Python.

Classical references personally inspected:

- [Fricain--Hartmann--Ross, Multipliers between model spaces,
  arXiv:1605.07418v2](https://arxiv.org/pdf/1605.07418v2), printed pages 11--12:
  boundary dx norm, model space and reproducing kernel. Their Fourier
  variable uses 2pi; LP1 and LP9 explicitly fix ours. The complete relevant
  pages were visually inspected with the PDF workflow.
- [Tao, 246A Notes 5, Lemma 17 and disk automorphisms](https://terrytao.wordpress.com/2016/10/18/246a-notes-5-conformal-mapping/):
  Schwarz's lemma underlying the explicitly derived half-plane estimate LP11.

Remote bytes are not authenticated by the offline checker. Hardy
factorization, Plancherel and elementary complex-analysis facts are classical.
No exhaustive novelty search or new abstract Hardy theory is claimed.
Smallest result-invalidating burden: LP4, diagonal monotonicity/exhaustion,
or the integrability implication LP11--LP14; each has a written proof above.
