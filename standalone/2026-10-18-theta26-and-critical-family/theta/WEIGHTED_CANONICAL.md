# Positive weighted moments suffice on the two open half-planes

Status: **PROPOSED complete conditional component theorem.** This note removes
unit root multiplicity, Gaussian reserve, inverse-density positivity, and a
common support bound from the sufficient all-order construction. It does not
prove that the required weighted moment systems are feasible at unbounded
orders. In particular, it does not establish RH or a new zeta boundary.

The argument is elementary and self-contained. No worldwide priority claim is
made for the criterion or for the canonical-factor method.

## 1. The remaining sufficient finite problem

Use the variance-one theta entire function H from `PROOF_GAUSSIAN.md`:

\[
 H(z)=\frac{\xi(1/2+iz/\sqrt{v_\theta})}{\xi(1/2)},
 \qquad H(0)=1,\qquad H''(0)=-1.
\]

There is a disk about zero on which H is nonzero. Choose the analytic logarithm
that is zero at zero and write

\[
 \log H(z)=-\frac{z^2}{2}
                -\sum_{r\ge2}\frac{Q_r}{r}z^{2r}.       \tag{1}
\]

The numbers Q_r are the same exact standardized cumulant combinations used by
the directed finite checker. Their definition does not assume RH.

### Theorem W: cofinal positive weighted feasibility implies RH

Suppose that for an unbounded sequence of integers M there are finitely many
positive real numbers `b_(M,j)` and positive real weights `lambda_(M,j)` such
that

\[
 \boxed{\qquad
   \sum_j\lambda_{M,j}b_{M,j}^{\,r}=Q_r,
                 \qquad 2\le r\le M.
 \qquad}                                                \tag{2}
\]

Then every zero of H is real, and hence RH holds. No uniform bound on the
number of nodes, the sum of the weights, the node support, or
`sum_j lambda_j b_j` is assumed. The weights need not be integers.

The complete native source and the finite existence certificates currently
verify (2), even with weights one, through M=13. They do not supply the
unbounded sequence required by the theorem.

## 2. Fractional factors are holomorphic where the proof needs them

Let U be the open upper half-plane. For a positive node b, the value
`1-b z^2` avoids the nonpositive real axis when z is in U: if its imaginary
part vanishes, the real part of z is zero and `1-b z^2` is strictly positive.
Thus the principal branch

\[
                    \ell_b(z)=\operatorname{Log}(1-bz^2) \tag{3}
\]

is holomorphic on U and is real at every z=it with t>0. Define

\[
 P_M(z)=\exp\!\left\{-\frac{z^2}{2}
       +\sum_j\lambda_{M,j}
                       [\ell_{b_{M,j}}(z)+b_{M,j}z^2]\right\}.
                                                            \tag{4}
\]

This function is holomorphic and nonvanishing on U. For noninteger weights
it need not be an entire function: its potential branch points are on the
real boundary. The proof will only use holomorphic convergence on U. The same
construction is available on the lower half-plane.

For every complex w,

\[
                         |(1-w)e^w|\le e^{|w|^2/2}.      \tag{5}
\]

Indeed `|1-w|^2=1-2 Re(w)+|w|^2`, so `log(1+u)<=u` proves the inequality
away from w=1, and w=1 is immediate. Since the weights in (4) are positive,
(2) with r=2 gives the uniform bound

\[
 \boxed{\qquad
       |P_M(z)|\le
          \exp\!\left(\frac{|z|^2}{2}
                              +\frac{Q_2|z|^4}{2}\right),
                      \qquad z\in U.
 \qquad}                                                \tag{6}
\]

This does not require a bound on any individual b. It is valid for arbitrary
positive real weights, since taking the real part of (3) gives the logarithm
of the corresponding modulus.

## 3. Identify the limit without a common Taylor disk

Node supports could increase with M, bringing branch points arbitrarily
close to zero along the real boundary. Consequently, matching Taylor
coefficients at zero alone must not be substituted for a common domain of
holomorphy. The following direct estimate on the positive imaginary axis
resolves that issue.

For x>=0 and every M>=2, the exact integral remainder for log gives

\[
 \log(1+x)-x
   =\sum_{r=2}^{M-1}\frac{(-1)^{r+1}x^r}{r}+R_M(x),
 \qquad
 R_M(x)=(-1)^{M-1}\int_0^x\frac{u^{M-1}}{1+u}\,du,
 \qquad |R_M(x)|\le\frac{x^M}{M}.                       \tag{7}
\]

This estimate holds for all x>=0, including x>1. At z=it, (4) is positive
real. Its real logarithm therefore satisfies

\[
 \left|\log P_M(it)-\left(
       \frac{t^2}{2}+\sum_{r=2}^{M-1}
                           \frac{(-1)^{r+1}Q_rt^{2r}}r\right)\right|
               \le\frac{Q_Mt^{2M}}M.                   \tag{8}
\]

Choose a radius d>0 on whose closed disk the logarithm in (1) is analytic,
and put `C=max_(|z|=d)|log H(z)|`. Cauchy's coefficient bound yields

\[
                    \frac{|Q_r|}{r}\le Cd^{-2r}.        \tag{9}
\]

For fixed 0<t<d, both the right side of (8) and the tail in (1), evaluated at
it, tend to zero. Explicitly, with `s=(t/d)^2<1`, their sum is at most

\[
                          C s^M\left(1+\frac1{1-s}\right). \tag{10}
\]

For sufficiently small d, H(it) is positive and its analytic logarithm is
the real one. Equations (8)--(10) prove

\[
                         P_M(it)\longrightarrow H(it)
                 \quad\text{for every }0<t<d.          \tag{11}
\]

The radius d is used only for the actual target, which is an entire function
with H(0)=1. There is no assumption that all auxiliary P_M extend to its disk.

## 4. Normality and zero exclusion

The bound (6) makes the P_M a normal family on U. Every subsequence has a
further subsequence converging uniformly on compact subsets to a holomorphic
limit. By (11), every such limit equals H on the interval `{it:0<t<d}`.
That set has accumulation points inside U, so the identity theorem identifies
the limit with H throughout U. Consequently the whole cofinal sequence
converges to H locally uniformly on U.

Each P_M is nonvanishing on U. Hurwitz's theorem makes H either nonvanishing
there or identically zero there. The latter is impossible by (11) and
H(0)=1. H therefore has no upper half-plane zeros. Its real Taylor
coefficients give the same conclusion in the lower half-plane. All zeros
are real, proving Theorem W.

## 5. What this changes, and what it leaves open

For each M, set

\[
          \nu_M=\sum_j\lambda_{M,j}b_{M,j}^{\,2}\delta_{b_{M,j}}.
\]

Then (2) is exactly the finite positive moment problem

\[
                 \int x^k\,d\nu_M(x)=Q_{k+2},
                           \qquad 0\le k\le M-2,       \tag{12}
\]

with finitely many atoms in `(0,infinity)`. This is a linear positivity
problem in the measure, instead of a requirement that all node
multiplicities equal one. For example, any proposed solution necessarily
makes every available matrix

\[
            [Q_{i+j+2}]_{i,j=0}^d,
       \qquad [Q_{i+j+3}]_{i,j=0}^d                     \tag{13}
\]

positive semidefinite whenever all its entries occur in (12): the associated
quadratic forms are the integrals of `p(x)^2` and `x p(x)^2`. These finite
matrix tests are necessary conditions. No converse for a truncated system is
silently assumed here, and no all-order positivity theorem for the actual
theta cumulants has been proved in this packet.

The finite real-node certificates remain useful explicit constructions, but
their unit multiplicities and positive Gaussian reserves are conveniences
of those certificates. Theorem W shows they are not prerequisites of the
all-order zero-exclusion argument. The remaining substantive task is proving
positive weighted feasibility of (12) at unbounded orders, or finding a
different analytic route that verifies the same criterion.
