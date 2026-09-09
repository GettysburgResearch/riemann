# Direct RH attack: the critical energy, exact completion, and a shorter signed integral

**Status: PROPOSED component proofs; the closing estimate in Section 1 is OPEN. RH is not proved.**

This packet belongs to `GettysburgResearch/riemann`. It attacks the actual
arithmetic estimate in PR805. All completions retain the literal finite Moebius
prefix; identities relating their critical scalar values are proved before any
change of representation is used.

Frozen main: `f99d9e3908dde4865377c75d9ca051c1f545bf4f`.
Inspected PR805: `602d7ddf9dbd2ba79bd6cada149772111ca72150`; its balanced
hyperbola parent is `ccd0a80dbd9844d06ccd6331a15b085b9c9afa41`.
The short-source Newton identity, Mellin consumer and analytic tools are credited
below. The exact variational/completion statements and proposed application are
written out here; no external priority claim is made.

## 1. The full problem being attacked

All arithmetic functions in Sections 1--5 are on positive **odd** integers. Let

\[
 M(x)=\sum_{n\le x,\ n\text{ odd}}\mu(n),\qquad
 m(x)=\sum_{n\le x,\ n\text{ odd}}\frac{\mu(n)}n,\qquad
 Q(x)=M(x)-xm(x).
\]

They vanish below 1. Define

\[
 \mathcal E(X)=\int_1^X m(t)^2\,dt.
\]

The direct target is

\[
 \tag{TARGET}\boxed{\forall\epsilon>0\quad
 \mathcal E(X)=O_\epsilon(X^\epsilon)\quad(X\to\infty).}
\]

This is a statement about the ordinary Möbius function at **all** large scales.
It is not an ensemble average over other multiplicative functions, a diagonal
coefficient bound, or an estimate with an exponent chosen after a hypothetical
zero. The following proof explains exactly why TARGET would settle RH.

### 1.1 Exact energy identity

For every real X>=1,

\[
 \tag{1}\boxed{\mathcal E(X)
 =\int_1^X\frac{M(t)^2}{t^2}\,dt+\frac{Q(X)^2}{X}.}
\]

Between successive odd integers, M and m are constant and Q'=-m. Differentiate
the right side, substitute M=Q+Xm, and obtain m(X)^2. At an odd integer n,
the jumps of M and Xm are both mu(n), so Q is continuous. Both sides are
continuous and vanish at X=1. This proves (1), including activation endpoints.
In particular |Q(X)|<=sqrt(X E(X)).

### 1.2 TARGET implies RH, with no source cancellation omitted

TARGET gives Q(X)=O_epsilon(X^(1/2+epsilon)). Put
Z(s)=(1-2^(-s))zeta(s). Initially for Re(s)>1, termwise integration gives

\[
 \tag{2}\int_1^\infty Q(x)x^{-s-1}\,dx
       =-\frac1{s(s-1)Z(s)}.
\]

Indeed Q(x)=-sum_(n<=x, odd) mu(n)(x/n-1), and the Mellin transform of
(x/n-1)_+ is n^(-s)/[s(s-1)]. The bound on Q makes the integral holomorphic
in Re(s)>1/2, by locally uniform absolute convergence, including differentiated
integrals. The function s(s-1)Z(s) is holomorphic in that half-plane: the
factor s-1 removes the pole at 1. The identity
s(s-1)Z(s) times the integral = -1 therefore extends there by the identity
theorem. A zero of zeta in Re(s)>1/2 is impossible. The factor 1-2^(-s)
has no zero there. The usual functional equation and zero symmetry give RH.
No off-line zero is assumed to have a largest real part or be simple.

Conversely, the classical RH-to-Mertens estimate is
M_all(x)=O_epsilon(x^(1/2+epsilon)). From
M(x)=sum_(2^j<=x) M_all(x/2^j), the same bound holds for M. Partial summation
and sum_(n odd) mu(n)/n=0 give
m(x)=M(x)/x-integral_x^infinity M(t)t^(-2)dt.
Thus m(x)=O_epsilon(x^(-1/2+epsilon)), and TARGET follows. This direction
imports the classical consequence of RH, not an unconditional ingredient.

Consequently TARGET is RH-equivalent. The elementary implication is not
counted as a new solution. Section 7 records precisely which attempted
estimate has and has not been established.

## 2. The existing terminal balance is globally energy-optimal

Fix an odd integer Y>=3. Let A_Y be the class of all real, finitely supported
sequences lambda on odd integers with

\[
 \lambda_n=\mu(n)\ (n<Y),\qquad \sum_n\lambda_n/n=0.
\]

There is no upper support bound in this section. Write
P_lambda(s)=sum lambda_n n^(-s), and A_lambda(t)=sum_(n<=t)lambda_n. Its
critical Cauchy-weighted energy has three identical forms:

\[
 \tag{3}\mathcal J(\lambda)=\frac1{2\pi}\int_{\mathbb R}
 \frac{|P_\lambda(1/2+it)|^2}{t^2+1/4}\,dt
 =\sum_{a,b}\frac{\lambda_a\lambda_b}{\max(a,b)}
 =\int_1^\infty\frac{A_\lambda(t)^2}{t^2}\,dt.
\]

This is the energy of P_lambda itself. It is **not** PR805's different
Nyman--Beurling/Green norm of the floor-function source, whose Fourier
representation contains an additional zeta multiplier. No minimizing
assertion for that other norm is made.

All sums are finite. The first equality follows from
integral_R e^(itu)/(t^2+1/4)dt=2pi exp(-|u|/2); the second follows by
expanding A_lambda(t)^2 and integrating from max(a,b). There is no sampled
Fourier integral in the argument.

Let lambda^T be the terminal-balanced source from PR805:

\[
 \lambda^T_n=\mu(n)\ (n<Y),\qquad
 \lambda^T_Y=-Y\sum_{n<Y,\ n\text{ odd}}\mu(n)/n,
\]

zero above Y. This agrees exactly with the convention
mu(n)-Y m(Y)1_(n=Y), even if Y is not squarefree. Its cumulative value after Y
is Q(Y).

For every lambda in A_Y the exact identity is

\[
 \tag{4}\boxed{\mathcal J(\lambda)=\mathcal E(Y)
 +\int_Y^\infty\frac{(A_\lambda(t)-Q(Y))^2}{t^2}\,dt.}
\]

Proof: the balance condition says integral_1^infinity A_lambda(t)t^(-2)dt=0.
On t<Y the cumulative sum is M(t). Partial summation gives
integral_1^Y M(t)t^(-2)dt=-Q(Y)/Y. Hence
integral_Y^infinity (A_lambda(t)-Q(Y))t^(-2)dt=0.
Expand the tail square, use integral_Y^infinity t^(-2)dt=1/Y, and apply (1).

In particular

\[
 \tag{5}\boxed{\inf_{\lambda\in\mathcal A_Y}\mathcal J(\lambda)
 =\mathcal J(\lambda^T)=\mathcal E(Y).}
\]

The minimizer is unique. Equality in (4) makes the right-continuous finite
step function A_lambda equal Q(Y) after Y, hence forces all remaining
coefficients to vanish and the coefficient at Y to be lambda^T_Y.

This is a full-tail statement, not a fixed-support optimization. Arbitrarily
many later coefficients cannot lower the critical energy while preserving
the native prefix and balance. It does not assert that changing completion
is useless for a **signed** quadratic or for a different norm.

## 3. A bounded-coefficient completion improves the direct contour cutoff

For odd Y>=3, put

\[
 I_Y=\{Y,Y+2,\ldots,2Y-1\},\quad N_Y=|I_Y|=(Y+1)/2,\quad
 S_Y=\sum_{k\in I_Y}1/k,\quad a_Y=m(Y-),\quad c_Y=-a_Y/S_Y.
\]

Define lambda^D_k=mu(k) for odd k<Y, lambda^D_k=c_Y for k in I_Y, and zero
otherwise. The superscripts T and D refer to terminal and diffuse, not to
different Möbius functions. All coefficients are exact rationals.

### 3.1 Uniform coefficient and diagonal bounds

The elementary bound |m(x)|<=2 suffices. To verify it, first use
sum_(n<=N)mu(n)floor(N/n)=1 at integer N to obtain
|sum_(n<=N)mu(n)/n|<=1: the n=1 fractional part is zero, so the remaining
fractional-part error is at most N-1. The sum is constant between integer
cutoffs. Separating the even terms and iterating then gives
m(x)=sum_j 2^(-j)m_all(x/2^j), and the bound 2.

Because S_Y>N_Y/(2Y)>1/4, we have |c_Y|<8. Exact balance holds. Moreover

\[
 \tag{6}D_Y:=\sum_k\frac{|\lambda^D_k|^2}k
 =\sum_{k<Y,\ k\text{ odd}}\frac{\mu(k)^2}k+\frac{a_Y^2}{S_Y}
 <17+\frac12\log Y.
\]

For the harmonic prefix, compare 1/k for k=3,5,... with one half the
integral of 1/t over [k-2,k]. The sum telescopes to at most (log Y)/2;
the k=1 term is 1. The tail term is below 16.

The constant diffuse coefficient also uniquely minimizes the tail diagonal
sum sum_(I_Y)|c_k|^2/k under the one constraint sum_(I_Y)c_k/k=-a_Y,
by weighted Cauchy--Schwarz. This is a **different** minimization from (5).
Indeed J(lambda^D)>=J(lambda^T), with the exact excess in (4).

### 3.2 Exact source identity for arbitrary balanced completions

For a finite sequence lambda in A_Y whose support is contained in [1,Y^2],
let u(n)=1 on odd integers, e the Dirichlet identity, and b=e-u*lambda.
Then b(n)=0 for n<Y. Formal Dirichlet convolution gives

\[
 \mu-(2\lambda-u*\lambda*\lambda)=\mu*b*b.
\]

The right side is supported on n>=Y^2. Its coefficient at n=Y^2 may be
nonzero, but the weight 1-Y^2/n is zero there. Therefore, defining

\[
 W(z)=\sum_{r\le z,\ r\text{ odd}}(z/r-1),\quad W(z)=0\ (z<1),
\]

we obtain exactly

\[
 \tag{7}\boxed{Q(Y^2)=2\sum_k\lambda_k+
 \mathcal B_Y(\lambda),\qquad
 \mathcal B_Y(\lambda)=\sum_{a,b}\lambda_a\lambda_b W(Y^2/(ab)).}
\]

Here balance removes the linear Y^2/k term. The support restriction is
necessary for replacing the weighted linear sum by the total sum. For a
completion extending beyond Y^2, retain the full weighted linear sum instead.
The quadratic includes every cross term and W=0 below one, not an analytic
main-term substitution. This is a source-faithful extension of the classical
short-Möbius/Newton identity already used in PR805 and Huxley--Watt.

For the diffuse and terminal completions both support restrictions hold.
Since N_Y/S_Y lies strictly between Y and 2Y,

\[
 \tag{8}\boxed{|\mathcal B_Y(\lambda^D)-\mathcal B_Y(\lambda^T)|<4Y.}
\]

Indeed their difference is 2a_Y(N_Y/S_Y-Y). Thus the changed completion
preserves the near-linear RH target up to a completely explicit O(Y) term.
It is not a positive replacement for the Möbius source.

More generally, two balanced completions with the same total coefficient sum
have **identical** B_Y. In particular a tail perturbation h supported on
[Y,Y^2] with sum h=0 and sum h/k=0 cannot change this full quadratic.
The tail-tail block itself is zero: its arguments satisfy Y^2/(ab)<=1.
This invariance does not forbid finding a useful representation of B_Y; it
forbids mistaking a changed auxiliary objective for a changed critical value.

## 4. The complete critical-line tail can be removed much earlier

For P_Y(s)=sum lambda^D_k k^(-s), let Z(s)=(1-2^(-s))zeta(s). Mellin inversion
and contour shifting, exactly as in PR805 but for the diffuse source, give

\[
 \tag{9}\boxed{\mathcal B_Y(\lambda^D)=-\frac Y\pi\Re\int_0^\infty
 \frac{Z(1/2+it)P_Y(1/2+it)^2Y^{2it}}{t^2+1/4}\,dt.}
\]

P_Y(1)=0 cancels the double possible pole at s=1 of
Z(s)P_Y(s)^2/[s(s-1)]. No RH is needed: zeta is in the numerator. Atoms at
an exact product boundary contribute zero. Standard strip bounds make the
horizontal sides vanish for fixed Y, and the integral is absolutely convergent.
The square is P_Y^2, not |P_Y|^2.

The two classical analytic inputs used next are:

* |Z(1/2+it)|<=C_z t^(1/4) for t>=1, with an unspecified finite constant;
  this follows by bounding both sums in the approximate functional equation.
* For any polynomial sum_(n<=N)d_n n^(-it) on any interval of length V,
  its squared L2 integral is at most (V+14N)sum |d_n|^2. This is a
  non-sharp Montgomery--Vaughan mean-value bound; the same constant is
  retained in the repository's current-results/Q4 account.

These are not numerical certificates or new bounds for zeta. For T>=1,
divide [T,infinity) into dyadic intervals [V,2V]. The second input applies
with d_k=lambda^D_k/sqrt(k) and N=2Y-1. Summing all dyadic intervals proves

\[
 \tag{10}\begin{split}
 &\left|\mathcal B_Y(\lambda^D)+\frac Y\pi\Re\int_0^T
 \frac{Z(1/2+it)P_Y(1/2+it)^2Y^{2it}}{t^2+1/4}\,dt\right|\\
 &\quad\le\frac{2^{1/4}C_z}{\pi}YD_Y
 \left(\frac{T^{-3/4}}{1-2^{-3/4}}
 +\frac{28Y T^{-7/4}}{1-2^{-7/4}}\right).
 \end{split}
\]

Every omitted frequency is included. No source-dependent sign was assumed
in the tail estimate. Set the predetermined cutoff

\[
 \tag{11}T_Y=[Y(1+\log Y)]^{4/7}.
\]

Since D_Y<=17(1+log Y), the first term in (10) is O(T_Y) and the second is
O(Y). The elementary inequality log Y<=sqrt(Y), Y>=1, implies T_Y<=2Y.
Consequently the **complete** omitted tail is O(Y), uniformly over odd Y>=3.
No numerical value for its absolute constant is claimed.

Compared with the triangle-bound cutoff Y^(4/3) in the inspected PR805
continuation, this gives a shorter sufficient integration range, with a
bounded-coefficient source differing in its critical scalar only by O(Y).
It is a reduction of the analytic workload, not a bound for the retained
integral and not a new zero-free region.

## 5. The exact signed integral target is still the full RH problem

Let I_Y be the real part of the integral in (9), truncated at (11). Then

\[
 \tag{12}\boxed{\forall\epsilon>0\quad |I_Y|=O_\epsilon(Y^\epsilon)
 \quad\text{for all odd }Y\to\infty}
\]

is equivalent to RH. Neither (12) nor TARGET is proved in this packet.
Here and in (12), constants cannot depend on Y.

For the forward direction, (10)--(11) give B_Y(lambda^D)=O_epsilon(Y^(1+epsilon)).
Equation (8) gives the same estimate for the original terminal scalar.
The terminal Newton identity Q(Y^2)=2Q(Y)+B_Y(lambda^T), with |Q(Y)|<=3Y,
then gives the square-root bound for Q at all odd squares. Between consecutive
odd squares the gap is 4Y+4; Q is continuous with |Q'|=|m|<=2 almost
everywhere, so interpolation costs O(sqrt(x)). The bound holds at every
large real x. Apply the Mellin argument (2) to obtain RH.

Under RH the classical Mertens estimate gives Q(x)=O_epsilon(x^(1/2+epsilon));
the two exact scalar identities and the O(Y) omitted tail give (12).

Nothing here permits replacing I_Y by the corresponding absolute-value
integral and declaring that integral subpower. Its finiteness at each Y is
not its growth estimate. Generic balanced-vector diagonal bounds were already
refuted by the inspected PR805 countercontrols; our diagonal improvement (6)
does not remove those cross terms for the actual Möbius vector.

## 6. The SHARP critical source is the same energy problem up to stable filters

This section uses the ordinary, not odd-only, Möbius function. Preserve the
repository's exact coefficient
beta(n)=mu(n)-1_(67|n)mu(n/67), and define

\[
 F(u)=\sum_{n\le e^u}\frac{\beta(n)}{\sqrt n}
           (4\sqrt{e^u/n}-3),\qquad u\ge0.
\]

Extend every logarithmic source by zero to u<0. Put
b_o(u)=e^(u/2)m(e^u), a_beta(x)=sum_(n<=x)beta(n)/n,
and b_beta(u)=e^(u/2)a_beta(e^u).

For (Sf)(u)=f(u-log q), the exact arithmetic factorization is

\[
 \tag{13}b_\beta=(I-2^{-1/2}S_2)(I-67^{-1/2}S_{67})b_o.
\]

It follows either from even/odd separation and the 67 correction, or directly
coefficient by coefficient. Partial summation gives, including every active
atom and the lower endpoint,

\[
 \tag{14}F(u)=b_\beta(u)+\frac32\int_0^u b_\beta(v)\,dv.
\]

Let L>=0, Jb(u)=integral_0^u b, and a=3/2. Squaring (14) and integrating yields

\[
 \tag{15}\|F\|_{L^2(0,L)}^2=\|b_\beta\|_2^2
 +a\,|Jb_\beta(L)|^2+a^2\|Jb_\beta\|_2^2.
\]

The cross term is a times the square of the endpoint primitive. No
zero-boundary condition at u=L was inserted. Thus
||b_beta||_2<=||F||_2<=(1+3L/2)||b_beta||_2.
Translations with zero extension are contractions on every finite interval.
Writing c_-=(1-1/sqrt(2))(1-1/sqrt(67)) and
c_+=(1+1/sqrt(2))(1+1/sqrt(67)), both positive, (13) gives

\[
 \tag{16}\boxed{c_-^2\mathcal E(e^L)\le\int_0^L|F(u)|^2du
 \le c_+^2(1+3L/2)^2\mathcal E(e^L).}
\]

Hence the native **critical-power mean-square** estimate is equivalent to
TARGET and RH. This is a global same-source comparison with no growing-prime
parameter, no future resampling, and no claim about different powers m>=2.
It makes precise where the established higher-power SHARP positivity stops:
it does not give the upper bound on either side of (16).

## 7. Outcome of the direct proof attempt

The completed chain is:

1. The original terminal balance globally minimizes the full critical energy
   over every admissible finite tail completion; its value is exactly E(Y).
2. Diffuse balancing lowers the coefficient-diagonal cost and gives a shorter
   all-frequency-controlled representation of the same RH-strength scalar.
3. The critical SHARP source, the minimum critical energy and the near-linear
   balanced Möbius scalar have exact implication/identity links.
4. Either TARGET or (12), proved for the actual source, closes the entire
   reciprocal-zeta argument and hence RH, not merely a special zero family.

The missing step is still a subpower bound for the actual arithmetic energy
or the retained signed integral. The unconditional elementary bound
E(X)<=4(X-1) follows from |m|<=2; it is far weaker. No power-saving, subpower,
all-order positivity, or new zero-free-region estimate is derived here.

Two proposed shortcuts have been checked rather than used: optimizing a tail
cannot lower E(Y), by (4); a small diagonal cost does not bound the full signed
quadratic, and can coexist with a *larger* critical energy. Neither the
higher-power positivity theorem nor the line-one Euler/Dickman norm theorem
supplies the missing critical estimate. No infinite-horizon assertion is
inferred from the finite checks. This packet is a direct full-problem attack
with completed components and an explicitly unsuccessful closing step, not
an unconditional proof proposal awaiting only routine verification.

## References and attribution

- PR805 at `602d7ddf9dbd2ba79bd6cada149772111ca72150`,
  also `standalone/2026-09-06-astra-terminal-endpoint/PROOF.md`,
  whose terminal uniqueness statement and distinct Green norm are retained;
  `standalone/2026-09-07-astra-critical-line-attempt/PROOF.md`;
  its Newton/terminal parent at `ccd0a80dbd9844d06ccd6331a15b085b9c9afa41`,
  `standalone/2026-09-07-astra-balanced-hyperbola/PROOF.md`.
- M. N. Huxley and N. Watt, *Mertens Sums requiring Fewer Values of the
  Moebius function* (2018), https://arxiv.org/abs/1807.05890 . The
  short-source hyperbola/Newton method is classical, not invented here.
- H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, J. London Math.
  Soc. (1974), https://doi.org/10.1112/jlms/s2-8.1.73 . The non-sharp
  mean-value constant used here also appears with a proof in main's
  `reviews/D-pass3/PROOFS_AND_REPAIRS.md`, R17--R19.
- NIST DLMF 25.9.1, https://dlmf.nist.gov/25.9 . Bounding the two approximate
  functional-equation sums at length comparable with sqrt(t) gives the
  classical t^(1/4) estimate used in (10).
- K. Soundararajan, *Partial sums of the Moebius function*, J. reine angew.
  Math. 631 (2009), 141--152, https://doi.org/10.1515/CRELLE.2009.044 ; author preprint
  https://arxiv.org/abs/0705.0723 . RH-to-Mertens is a classical imported implication; no external computation
  or stronger constant is replayed or asserted.
- The main source guide at the frozen main,
  `research/integrated/CURRENT_RESULTS.md`, Sections 2--5, and
  `research/integrated/sharp_native/README.md`, fixes the literal beta source,
  higher-power positivity scope, and critical-variation boundary.

The Cauchy-transform isometry, energy identity, Mellin pole
consumer, Cauchy--Schwarz minimization, and stable-filter bounds are elementary
or classical. This packet makes no claim to a comprehensive priority survey.
Its finite checks authenticate the stated arithmetic instances, not these
analytic theorems or TARGET.
