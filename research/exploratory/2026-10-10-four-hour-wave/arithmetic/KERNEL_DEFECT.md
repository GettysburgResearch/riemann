# An exact product bound that prices the kernel activation defect

Status: **PROPOSED quantitative lemma.** This gives a direct Euler product
comparison without truncating the level factorial series. Its scope is
eventual positivity at each fixed supercritical power. No uniform critical
bound or RH conclusion follows.

Use the literal beta source and H_m from `POWER_THRESHOLD.md`. For t>1,
define its signed and absolute Dirichlet products

\[
 B(t)=\sum_n\beta(n)n^{-t}=\frac{1-67^{-t}}{\zeta(t)},\qquad
 A(t)=\sum_n|\beta(n)|n^{-t}
          =(1+67^{-t})\frac{\zeta(t)}{\zeta(2t)}.
 \tag{K1}
\]

The second identity is exact, not a triangle majorant. If n=67^k l with
67 not dividing l, beta equals mu(l), -2mu(l), mu(l), and zero at
k=0,1,2, and k>=3 respectively. Therefore

\[
 |\beta(n)|=\mu(n)^2+\mathbf1_{67\mid n}\mu(n/67)^2.
\]

Equivalently A(t)=product over all labels of (1+q^-t), while B(t) is the
product of (1-q^-t). The ordinary and extra 67 factors are both retained.
Different labelled subsets yielding the same integer always have the same
parity, so the labelled absolute product projects exactly to |beta|.

## 1. Full absolute product comparison

Fix m>1, put a=(m+1)/2, and choose

\[
 0<\delta<\min(1/2,a-1),\qquad C_m=\max(1,3m/4).
 \tag{K2}
\]

For every real x>=1,

\[
 \left|\frac{H_m(x)}{4^m x^{m/2}}-B(a)\right|
           \le C_m A(a-\delta)x^{-\delta}.
 \tag{K3}
\]

Indeed, with u=n/x, let
\(h_m(u)=(1-3\sqrt u/4)^m\) for u<=1 and zero for u>1.
For 0<=u<=1, Bernoulli gives
\(0\le1-h_m(u)\le(3m/4)\sqrt u\le C_m u^\delta\).
For u>1, the defect is one, bounded by u^delta. Insert this uniform
defect into the absolutely convergent beta series at a and use (K1) at
a-delta>1. This proves (K3).

It follows that H_m(x)>0 whenever

\[
 x>\left[\frac{C_m A(a-\delta)}{B(a)}\right]^{1/\delta}.
 \tag{K4}
\]

This is a direct product estimate; it does not require retaining any fixed
number of label levels. It is generally less numerically efficient than
the squarefree prefix estimate in this packet.

## 2. Price only even-parity activation defects

The normalized ratio from (T1) can be written

\[
 r_n(m,x)=n^{-a}h_{m,x}(n),\qquad
 h_{m,x}(n)=\left[
  \frac{1-3\sqrt{n/x}/4}{1-3/(4\sqrt x)}\right]^m
        \mathbf1_{n\le x}.
 \tag{K5}
\]

For n>=1, 0<=h<=1, and h(1)=1. Fix X>=1. For x>=X, the activation
defect obeys

\[
 0\le1-h_{m,x}(n)\le C_{m,X}(n/x)^\delta,
 \quad C_{m,X}=\max\left(1,\frac{3m}{4-3/\sqrt X}\right).
 \tag{K6}
\]

On the active domain, write the ratio inside (K5) as 1-v, where
\(v=(3/4)(\sqrt{n/x}-1/\sqrt x)/(1-3/(4\sqrt x))\in[0,1)\).
Then 1-(1-v)^m<=mv, bounded by
\([3m/(4-3/\sqrt X)]\sqrt{n/x}\); (K2) bounds this by its delta
power. The inactive domain is again bounded by (n/x)^delta.

The complete normalized Euler sum at exponent a is B(a). Subtracting
the activation defect from each labelled subset gives the exact identity

\[
 \frac{H_m(x)}{T(x)^m}
    =B(a)+\sum_A(-1)^{|A|+1}n_A^{-a}[1-h_{m,x}(n_A)].
 \tag{K7}
\]

All sums converge absolutely for a>1. Odd-subset defect contributions
are nonnegative, so discarding them and using (K6) on even subsets gives

\[
 \frac{H_m(x)}{T(x)^m}
 \ge B(a)-C_{m,X}x^{-\delta}
       \left[\frac{A(a-\delta)+B(a-\delta)}2-1\right],\quad x\ge X.
 \tag{K8}
\]

The empty subset has zero defect and is excluded by the minus one.
The remaining even weighted mass is exactly (A+B)/2-1, because the
positive and signed Euler products separate parity. This prices only
the even activation defects, which are the adverse contributions relative
to the complete Euler product; it has no factorial-truncation remainder.

For example, if the right side of (K8) is positive at x=X with its
constant C_(m,X), it stays positive for every x>=X. This is a genuine
whole-tail implication at a fixed m.

## 3. The explicit critical obstruction in this absolute product norm

Both (K3) and (K8) require a-delta>1. As m decreases to one, the available
positive delta tends to zero. Writing epsilon=a-1=(m-1)/2 and
t=a-delta, the elementary pole expansions give

\[
 B(a)\sim\frac{66}{67}\epsilon,\quad
 A(t)\sim\frac{68}{67\zeta(2)}\frac1{\epsilon-\delta},\quad
 B(t)\sim\frac{66}{67}(\epsilon-\delta).
 \tag{K9}
\]

Thus the adverse even mass in (K8), relative to B(a), has size
constant/[epsilon(epsilon-delta)]. In particular its best horizon from
this bound still escapes to infinity: since delta<epsilon, its logarithm
is at least order log(1/epsilon)/epsilon as epsilon tends to zero.
For the concrete choice delta=epsilon/2, the logarithm has precisely
that order, up to fixed multiplicative constants.

The exact product comparison therefore isolates a valid activation-defect
cost and removes the factorial bookkeeping, but its absolute source norm
does not pay the native critical negative-mass gap. A cancellation theorem
for those defects would be additional mathematics. This is consistent
with the fact that all-endpoint positivity for every m>1 would pass by
continuity at each fixed x to critical positivity and imply the inherited
RH consequence.
