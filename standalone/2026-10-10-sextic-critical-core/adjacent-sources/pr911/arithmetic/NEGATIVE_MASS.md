# Quantitative critical-SHARP negative mass and off-line poles

Status: **PROPOSED analytic lemmas; independent review requested.**

Scope: global implications for one fixed literal arithmetic source; the
upper-growth implication first states its Mertens hypothesis explicitly.
`ZERO_FREE_MERTENS.md` derives that hypothesis from a fixed zero-free
half-plane. No new zero-free half-plane, critical estimate, or RH proof is
claimed.

Exact dependencies: the Möbius Dirichlet series in its absolutely convergent
half-plane, the classical meromorphic continuation of zeta and its absence
of positive real zeros, and the eventual-sign Landau theorem, whose full
argument is resident in `reviews/C/pass4-math-completion/proofs/`.
The reviewed SHARP definitions and distributional-descent conventions are
recorded in `research/integrated/CURRENT_RESULTS.md`, sections 2 and 3, and
`reviews/D/CLAIMS.tsv`, D-U010/D-U011. The derivations below are new proposed
objects and do not change those source verdicts.

What was actually run: to be completed in the execution receipt. All analytic
arguments are written out below; finite checks are not infinite proofs.

Smallest remaining gap: an unconditional source-specific bound on negative
mass better than the bounds supplied by currently available cancellation.

## 1. Fix the arithmetic source before taking any norm

For integers n>=1 define

\[
 \beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
 \qquad T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}.
\]

The critical SHARP detector in this note is exactly

\[
 F(x)=\sum_{n\le x}{\beta(n)\over\sqrt n}T(x/n),\qquad x\ge1.
 \tag{A1}
\]

It is right continuous, locally integrable, and has the signed activation
jump beta(n)/sqrt(n) at x=n. Set

\[
 N(Y)=\int_1^Y F_-(x){dx\over x},\qquad F_- =\max(-F,0).
 \tag{A2}
\]

The two prefix sums give the exact formula

\[
 F(x)=4\sqrt x\sum_{n\le x}{\beta(n)\over n}
       -3\sum_{n\le x}{\beta(n)\over\sqrt n}.
 \tag{A3}
\]

In particular |F(x)|=O(sqrt(x) log(2x)) and N(Y)=O(sqrt(Y) log(2Y))
unconditionally, since |beta(n)|<=2. Values at individual jumps do not
affect N.

In Re(s)>1/2, absolutely convergent integration and summation give

\[
 \mathcal M F(s)
 =\frac{1-67^{-(s+1/2)}}{\zeta(s+1/2)}
       \left({4\over s-1/2}-{3\over s}\right)
 =\frac{(1-67^{-(s+1/2)})(s+3/2)}
        {s(s-1/2)\zeta(s+1/2)}.
 \tag{A4}
\]

The apparent pole at s=1/2 is removable, because 1/zeta(1+h)=h+O(h^2).
The expression is holomorphic near every real s>0. For 0<z<1 the alternating
eta series is positive, while 1-2^(1-z)<0, so zeta(z)<0; for z>1 zeta(z)>0.
This verifies the needed real-axis normalization instead of appealing to an
arbitrary total-function value at the pole of zeta.

If rho is a nontrivial zeta zero with Re(rho)>1/2, s0=rho-1/2 is a genuine
pole in Re(s)>0. None of the other factors cancels it: |67^(-rho)|<1,
s0 is neither 0 nor 1/2, and s0+3/2=rho+1 is nonzero.

## 2. Polynomial negative mass gives a quantitative zero-free strip

**Proposed lemma A-NM1.** Fix 0<=lambda<1/2. If for every epsilon>0

\[
 N(Y)=O_\epsilon(Y^{\lambda+\epsilon}),
 \tag{A5}
\]

then zeta has no zero with Re(rho)>1/2+lambda. For lambda=0 this is the
usual critical-SHARP subpower implication; a positive lambda supplies only
the displayed weaker strip.

**Proof.** The nonnegative measure dN(x)=F_-(x) dx/x has Mellin transform
holomorphic in Re(s)>lambda. Indeed, on a compact subset choose epsilon
less than its minimum real part minus lambda. Integration by parts, or
dyadic summation, bounds the integral and every fixed derivative uniformly.

Let c_+ be the absolute-convergence abscissa of the transform of F_+.
It is at most 1/2 by (A3). If it is minus infinity, its transform is entire.
Otherwise it is finite. In the initial half-plane its transform equals
the right side of (A4) plus the transform of F_-. If c_+>lambda, the latter
expression continues it analytically through the positive real point c_+.
The Landau theorem for a nonnegative function forbids analytic continuation
through its finite convergence abscissa. Thus c_+<=lambda. Both positive
and negative transforms are holomorphic in Re(s)>lambda, so (A4) has no
pole there. Its established noncancellation excludes the claimed zeros.
This proof includes the entire-transform case. QED.

Writing Theta=sup Re(rho) over the nontrivial zeros, define

\[
 \lambda_-:=\limsup_{Y\to\infty}{\log(1+N(Y))\over\log Y}.
\]

The elementary bound gives 0<=lambda_-<=1/2. Lemma A-NM1 implies

\[
 \Theta-1/2\le\lambda_-.
 \tag{A6}
\]

For example, a zero with real part beta>1/2 forces failure of every
O(Y^lambda) negative-mass bound with lambda<beta-1/2. This is an obstruction
for the fixed source (A1), not a statement that such a zero has been found.

## 3. The converse rate uses a literal Mertens estimate

**Proposed lemma A-NM2.** Let 1/2<=theta<1 and assume

\[
 M(x):=\sum_{n\le x}\mu(n)=O_\epsilon(x^{\theta+\epsilon})
 \quad\text{for every epsilon>0}.
 \tag{A7}
\]

Then |F(x)|=O_epsilon(x^(theta-1/2+epsilon)) and the same bound holds for
N(Y), with a harmless log(Y) at an exact zero power, absorbed by increasing
epsilon. Consequently lambda_-<=theta-1/2.

**Proof.** The beta prefix is M_beta(x)=M(x)-M(x/67), with the same bound.
Choose epsilon small enough that t=theta+epsilon<1. Partial summation gives

\[
 \sum_{n\le x}\frac{\beta(n)}{\sqrt n}=O_\epsilon(x^{t-1/2}).
\]

The series sum beta(n)/n converges by the assumed prefix bound. Its value is
zero: Abel's theorem identifies it with the limit as z decreases to 1 of
(1-67^(-z))/zeta(z). Hence

\[
 \sum_{n\le x}\frac{\beta(n)}n
 =-\sum_{n>x}\frac{\beta(n)}n
 =O_\epsilon(x^{t-1}).
\]

Insert these two bounds in (A3), then integrate the absolute bound in dx/x.
For larger requested epsilon the weaker bound follows automatically. QED.

Thus, **if** a claimed fixed zero-free half-plane Re(s)>theta is accompanied
by (A7), it supplies the following rates for this particular detector:

| Imported theta | Resulting exponent theta-1/2 |
|---|---|
| 11/12 | 5/12 |
| 7/8 | 3/8 |
| a refined theta<7/8 | theta-1/2 |
| 1/2 | 0, meaning subpower |

This packet does not prove the external zero-free results or import their
Mertens consequence silently. The full zero-free-to-Mertens growth/Perron
adapter is derived in `ZERO_FREE_MERTENS.md`, theorem A-ZM1. The external
2026 quasi-RH manuscripts inspected during the wave remain imported inputs,
not repository review verdicts. With that classical adapter, (A6) and this
lemma give the exact exponent lambda_-=Theta-1/2; the endpoint Theta=1 is
handled by the trivial bound rather than by a zero-free theorem with theta<1.

## 4. A rightmost pole forces an explicit negative-mass constant

**Proposed lemma A-NM3.** Suppose c>0, F is absolutely Mellin integrable in
every Re(s)>c, the expression (A4) is holomorphic near the real point c,
and a nontrivial zero rho=c+1/2+i*tau, tau!=0, has multiplicity r>=1.
Let

\[
 A=\lim_{s\to c+i\tau}(s-c-i\tau)^r\mathcal MF(s)
   =\frac{r!(1-67^{-\rho})(\rho+1)}
    {(\rho-1/2)(\rho-1)\zeta^{(r)}(\rho)}.
 \tag{A8}
\]

Then

\[
 \limsup_{Y\to\infty}\frac{N(Y)}{Y^c(\log Y)^{r-1}}
 \ \ge\ \frac{|A|}{2c(r-1)!}.
 \tag{A9}
\]

No pole isolation, simplicity, finite zero census, or inverse Mellin
contour is assumed. Absolute integrability to the right of c is essential;
for a rightmost zero it is supplied by A-ZM1 with theta=c+1/2, provided
c+1/2<1. The strict strip of nontrivial zeros ensures this whenever such a
rightmost zero exists.

**Proof.** For real sigma>c, write M_+(sigma) and M_-(sigma) for the two
nonnegative Mellin integrals. The triangle inequality yields

\[
 |\mathcal MF(\sigma+i\tau)|
 \le M_+(\sigma)+M_-(\sigma)
 =\mathcal MF(\sigma)+2M_-(\sigma).
\]

The real-axis transform stays bounded as sigma decreases to c, whereas
(sigma-c)^r |MF(sigma+i*tau)| tends to |A|. Therefore

\[
 \liminf_{\sigma\downarrow c}(\sigma-c)^r M_-(\sigma)\ge|A|/2.
 \tag{A10}
\]

Let K be the limsup in (A9). If K is infinite there is nothing to prove.
Otherwise, for any eta>0 and all sufficiently large u,

\[
 N(e^u)\le(K+\eta)e^{cu}u^{r-1}.
\]

Integration by parts gives M_-(sigma)=sigma integral_0^infinity
N(e^u)e^(-sigma*u) du. The finite initial interval contributes zero after
multiplication by (sigma-c)^r. On the tail, the gamma integral gives

\[
 \limsup_{\sigma\downarrow c}(\sigma-c)^r M_-(\sigma)
 \le c(K+\eta)(r-1)!.
\]

Compare with (A10), then let eta decrease to zero. This proves (A9). QED.

The constant depends on the actual zero and derivative of zeta; it is not
a numerically certified constant without certified primitive enclosures.

## 5. Quadratic positivity and even global BV do not pay this rate

Put H2(x)=sum_(n<=x) beta(n)/sqrt(n) T(x/n)^2 and J(u)=exp(-u) H2(exp(u)).
Away from activation points the exact derivative identity is

\[
 J'_{\rm ac}(u)=3e^{-u}F(e^u).
\]

At u=log(n), the derivative measure additionally has the activation atom
beta(n)n^(-3/2). These atoms must be excluded from the critical negative
mass identity:

\[
 N(Y)=\frac13\int_0^{\log Y}e^u(dJ_{\rm ac})_-.
 \tag{A11}
\]

In fact J has globally bounded variation **unconditionally**. Its nth
signed atom-profile is beta(n)n^(-3/2) phi(u-log(n)), where phi is zero for
negative arguments and

\[
 \phi(v)=16-24e^{-v/2}+9e^{-v},\quad v\ge0.
\]

The jump is 1, and phi'(v)=12e^(-v/2)-9e^(-v)>0. Each profile has total
variation 16. Hence

\[
 \operatorname{TV}(J)\le16\sum_{n\ge1}|\beta(n)|n^{-3/2}<\infty,
\quad
 \lim_{u\to\infty}J(u)
 =\frac{16(1-67^{-3/2})}{\zeta(3/2)}>0.
 \tag{A12}
\]

Absolute convergence justifies the BV bound and dominated-convergence
limit. The reviewed quadratic positivity says J(u)>0, but neither that
nor (A12) controls the e^u weight in (A11).

A synthetic, non-arithmetic firewall makes the failure exact. For
0<a<1, tau>0, and 0<eta<1, set

\[
 J_*(u)=1+\eta e^{-au}\sin(\tau u),\quad u\ge0.
\]

It is positive, has finite total variation, and tends exponentially to 1.
Nevertheless the corresponding descent

\[
 F_*(e^u)=\frac{e^u}{3}J_*'(u)
 =\frac\eta3 e^{(1-a)u}
    (\tau\cos(\tau u)-a\sin(\tau u))
\]

has logarithmic negative mass with growth exponent 1-a>0. To see the lower
bound, choose a fixed phase interval in each period where the parenthesis
is bounded above by a negative constant; integration over the last such
interval gives a fixed positive multiple of exp((1-a)u) along an unbounded
sequence. The matching upper bound follows by integrating the absolute
amplitude. This example respects descent, positivity, BV, and exponential
return, but does not have the Möbius source. It refutes promotion from those
properties alone, not the native-source conjecture.
