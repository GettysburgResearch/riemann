# A conductor mean for the canonical Gauss Dirichlet family

**Status:** proposed source-conditional analytic theorem, derived from the
imported completed theta mean square and the classical squarefree sextic
large sieve. No inverse-Möbius higher moment is assumed or proved.

**Authorship:** root. An independent reconstruction must be attached to
the exact frozen source commit before this is represented as reviewed.

**Scope:** squarefree primary rows outside the fixed bad set, a fixed
finite family of ray characters, a moving squarefree auxiliary divisor,
and a strict interior vertical strip. The squarefree restriction on the
rows is essential to the particular estimate proved here.

**Exact inputs:** OpenAI/math commit
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`, October 5 `paper2.tex`,
equations `eq:T`, `eq:completed-twist`, and Proposition `prop:R`;
Blomer–Goldmakher–Louvel, *L-functions with n-th order twists*,
[Theorem 1.3](https://arxiv.org/abs/1112.1650), in the primary-element
normalization recorded in Section 1 of
[ALL_ROW_SIEVE_AND_GCD_TAIL.md](../2026-10-10-sextic-moment-descent/ALL_ROW_SIEVE_AND_GCD_TAIL.md).
The latter repository file is fixed at
`9959364671f89b86f3992ec5ed5e19f804eb607b`. We use only its squarefree
input, not its all-row extension. The imported theta foundation is an
explicit assumption of this result, rather than a newly verified input.

## 1. Exact family and theorem

Let `K=Q(omega)`, `O=Z[omega]`, and let `N` be the ideal norm. Use the
inherited primary generators and sextic symbols with their literal zero
extensions. The fixed set S contains the primes over 2 and 3 and every
fixed ray conductor. For a fixed finite ray character xi, put

\[
a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n),
\qquad \alpha(n)=n/|n|.
\tag{1.1}
\]

For a squarefree primary d outside S, initially for `Re(u)>1`, define

\[
G_{k,d}(u)=\sum_{(n,S)=1}^{*}
\frac{a_\xi(n)\chi_n(k)\chi_n(d)^4}{(Nn)^u},
\tag{1.2}
\]

and its exact cube completion

\[
\begin{split}
\mathcal T_{k,d}(u)&=G_{k,d}(u)
 L_{S,kd}\left(3u-\tfrac12,
                  \overline\alpha^{\,3}\xi^3\chi_k^3\right).
\end{split}
\tag{1.3}
\]

The convention for `chi_k^3` in (1.3) is the inherited reciprocal
primary convention: on the cube index it is `chi_b(k)^3`. In particular
the Euler product vanishes at no omitted prime because those factors
are not inserted in the first place. Formula (1.3) includes the zero
mask at d: `chi_b(d)^{12}=1_(b,d)=1`.

Write `F=Nd`, let `Q>=2`, and let `K_Q` be any subset of the squarefree
primary rows with `Q<=Nk<2Q` and `(k,S)=1`. One may impose `(k,d)=1`
or retain any smaller subset. All constants below are uniform in that
choice of subset.

### Theorem 1.1

Both (1.2) and (1.3) continue holomorphically to `Re(u)>1/2` by the
construction below. For any closed real strip

\[
\frac58<a_0\le a=\Re u\le a_1<1
\tag{1.4}
\]

and any epsilon greater than zero there is a finite M such that

\[
\boxed{
\sum_{k\in\mathcal K_Q}|G_{k,d}(a+it)|^2
\ll_{a_0,a_1,\epsilon,S,\xi}
Q^{1+\epsilon} F^{1-a+\epsilon}(2+|t|)^M.
}
\tag{1.5}
\]

The identical bound holds for `mathcal T` in place of G. The conclusion
is uniform over a fixed finite ray-character family. It does not
require a zero-free theorem: the cube reciprocal in this strip is in
its absolutely convergent Euler half-plane. No endpoint assertion at
`a=5/8` is included.

## 2. Two bounds for one smooth completed block

Fix a compact interval `I=[c,C]` in `(0,infinity)` and
`W in C_c^infinity(I)`. Define precisely the imported completed sum

\[
\begin{split}
T_W(X;k,d)=X^{-1/2}
\sum_{(n,S)=1}^{*}\sum_{\substack{b\equiv1\ (3)\\(b,dS)=1}}
&a_\xi(n)\chi_n(k)\chi_n(d)^4
\overline{\alpha(b)}^{\,3}\xi(b)^3\chi_b(k)^3
\sqrt{Nb}\,W\left(\frac{Nn(Nb)^3}{X}\right).
\end{split}
\tag{2.1}
\]

No condition `(n,b)=1` is present. The row characters in the two
indices include the row zero mask. This is `eq:T` with
`V_*(y)=sqrt(y)W(y)` and `f=d`, not an uncompleted squarefree block.

For every positive epsilon, the imported Proposition R gives

\[
\sum_{k\in\mathcal K_Q}|T_W(X;k,d)|^2
\ll (QFX)^\epsilon\|W\|_{C^J(I)}^2
\left(Q+\frac{Q^2F}{X}\right),\qquad X\ge1.
\tag{2.2}
\]

To fit its reference-parameter formulation uniformly, take its D to be
`max(2Q,F,X,2)` and take `C_0=1`. These choices dominate every parameter
in the source statement, and `D^epsilon <= (2QFX)^epsilon`. The order
J consequently does not depend on Q,F,X. Restricting its nonnegative
all-row sum to `K_Q` is legitimate.

The second bound is

\[
\sum_{k\in\mathcal K_Q}|T_W(X;k,d)|^2
\ll (QX)^\epsilon\|W\|_\infty^2
\left(Q+X+(QX)^{2/3}\right).
\tag{2.3}
\]

Here and below fixed constants depending on I are harmless, including
when X lies in a fixed bounded interval. To prove (2.3), write
`L_b=X/(Nb)^3` and

\[
S_W(L_b;k,d)=L_b^{-1/2}
 \sum_{(n,S)=1}^{*}a_\xi(n)\chi_n(k)\chi_n(d)^4 W(Nn/L_b).
\tag{2.4}
\]

Then (2.1) is the sum over b of `S_W(L_b;k,d)/(Nb)` times the
displayed cube character of modulus at most one. It is empty for
`Nb>(CX)^{1/3}`. Since `|a_xi(n)chi_n(d)^4|<=1`, ideal counting bounds
the squared coefficient norm in (2.4) by `O_I(||W||_infinity^2)`
whenever `L_b>=1/C`. Below this range the block is empty. Thus the
squarefree sextic large sieve, including the fixed primary reciprocity
classes, gives

\[
\sum_{k\in\mathcal K_Q}|S_W(L_b;k,d)|^2
\ll (QX)^\epsilon\|W\|_\infty^2
 \left(Q+L_b+(QL_b)^{2/3}\right).
\tag{2.5}
\]

For bounded `1/C<=L_b<1`, replace `L_b` in the sieve's cutoff by a
fixed positive constant; this changes (2.5) only by an I-dependent
constant. The d mask is part of the arbitrary column coefficients.

Weighted Cauchy in the b sum uses
`sum_(Nb<=(CX)^(1/3))1/Nb <<_I log(2X)`. After summing (2.5) with
weight `1/Nb`, its three terms are respectively bounded by

\[
Q\log(2X),\qquad
X\sum_b(Nb)^{-4}\ll X,\qquad
(QX)^{2/3}\sum_b(Nb)^{-3}\ll (QX)^{2/3}.
\tag{2.6}
\]

Absorb the logarithms into an arbitrarily small power of X. This
proves (2.3), uniformly in d, without requiring any new sieve for
completed coefficients or for nonsquarefree rows.

## 3. Mellin reconstruction is normally convergent

Choose a fixed smooth dyadic partition with
`sum_(j>=0) W_0(y/2^j)=1` for every real `y>=1`, allowing the first
term to be a separate fixed smooth cutoff. All its supports lie in a
fixed compact interval inside `(0,infinity)`; changing that first
cutoff has no effect on the estimates. Let `X=2^j`, and put
`W_u(y)=y^{-u}W_0(y)`, with the analogous first-cutoff definition.
For every finite J and bounded real strip,

\[
\|W_u\|_{C^J}\ll (2+|\Im u|)^J.
\tag{3.1}
\]

For `Re(u)>1`, absolute convergence and the partition give the exact
identity

\[
\mathcal T_{k,d}(u)
=\sum_{X=2^j,\ j\ge0} X^{1/2-u}T_{W_u}(X;k,d).
\tag{3.2}
\]

This reconstructs the factor `(Nn(Nb)^3)^(-u)sqrt(Nb)` term by
term, so the cube exponent is exactly `3u-1/2`.

For fixed Q,F, (2.2), Minkowski's inequality, and (3.1) make the tail
of (3.2) normally convergent in the finite-dimensional row Hilbert
space on every compact subset of `Re(u)>1/2`. Indeed choose the small
loss in (2.2) below twice the distance of that compact set from 1/2;
the dyadic tail is bounded by a convergent geometric series in
`X^(1/2-Re(u)+epsilon)`. Each smooth block is an entire function of u
and is a finite sum. This proves holomorphic continuation of the
completed family and equality with its original series on the overlap.

Also, in `Re(u)>1/2`,

\[
L_{S,kd}\left(3u-\tfrac12,
 \overline\alpha^{\,3}\xi^3\chi_k^3\right)^{-1}
\tag{3.3}
\]

is an absolutely convergent product, uniformly bounded in k,d and
both its fixed ray family and its imaginary part on strict interior
strips. This follows from `Re(3u-1/2)>1` and comparison with
`prod_p(1+(Np)^(-1-delta))`. It is nonzero there. Dividing the
continued completed family by this L-function proves the stated
holomorphic continuation of G, with no angular reciprocal theorem.

## 4. The conductor calculation and the threshold 5/8

For `a=Re(u)>1/2`, combine (2.2) and (2.3). In the following dyadic
estimates the arbitrarily small losses in Q,F,X can first be retained
and then absorbed by shrinking the strict strip margins and adjusting
the final epsilon. Define

\[
\begin{split}
\mathcal B(Q,F,X)
&=\min\left(Q+X+(QX)^{2/3},\ Q+Q^2F/X\right)\\
&\le Q+\min(X,Q^2F/X)
          +\min((QX)^{2/3},Q^2F/X).
\end{split}
\tag{4.1}
\]

Taking square roots, using Minkowski in (3.2), and summing the base
term gives `O(Q^(1/2))`, since `sum_X X^(1/2-a)` converges.
For the first minimum the crossover is

\[
X_1=QF^{1/2}.
\tag{4.2}
\]

On `X<=X_1` its dyadic contribution is `X^(1-a)`; on `X>X_1` it
is `QF^(1/2)X^(-a)`. For `1/2<a<1` the two sums are bounded by

\[
Q^{1-a}F^{(1-a)/2}.
\tag{4.3}
\]

For the second minimum the crossover is

\[
X_2=Q^{4/5}F^{3/5}.
\tag{4.4}
\]

Its lower contribution is `Q^(1/3)X^(5/6-a)` and its upper
contribution is again `QF^(1/2)X^(-a)`. When `1/2<a<5/6`, both
dyadic sums are bounded by

\[
Q^{1-4a/5}F^{1/2-3a/5}.
\tag{4.5}
\]

At `a=5/6` the lower sum has a logarithm. For `5/6<a<1` it is
bounded by `O(Q^(1/3))`; the upper sum is also at most this quantity.
Uniformly when a crosses 5/6 in a closed strip, one may bound by the
sum of the expressions in (4.5) and `Q^(1/3)`, times `log(2QF)`.
This avoids introducing a constant singular at 5/6.

For `a>5/8` the displayed contributions all satisfy the desired
bound. Explicitly,

\[
1-a<\tfrac12,\qquad
1-\tfrac45a<\tfrac12,\qquad
\tfrac12-\tfrac35a\le\tfrac{1-a}{2}.
\tag{4.6}
\]

Since Q,F are at least one, (4.3) and (4.5), as well as the base
term and `Q^(1/3)`, are bounded by
`Q^(1/2)F^((1-a)/2)`. The strict lower margin above 5/8 permits the
arbitrarily small power losses from (2.2) and (2.3); retaining the
logs near 5/6 costs at most another such loss. We obtain

\[
\left\|\mathcal T_{k,d}(a+it)\right\|_{\ell^2(\mathcal K_Q)}
\ll Q^{1/2+\epsilon}F^{(1-a)/2+\epsilon}(2+|t|)^M.
\tag{4.7}
\]

Absorb a factor two into the epsilon and M names on squaring. The
uniform absolutely convergent reciprocal (3.3) gives the same result
for G. This proves Theorem 1.1.

## 5. What this estimate supplies, and what it leaves open

The norm in (1.5) has the expected square-root row-count factor, with
an explicit moving-divisor loss `F^((1-a)/2)` before squaring. This is
the input needed when a normally convergent divisor expansion produces
canonical Gauss series at an argument u with `Re(u)>5/8`.

Neither the original Möbius polynomial nor its `2k`-th power occurs in
(1.2). The row set here is squarefree, whereas the requested inverse
moment sums all nonzero element rows. Restoring the actual moment,
removing its cube completions, and proving the needed signed covariance
at the long dual scales remain separate tasks. A better bound for this
particular continued family is not by itself a new zero-free boundary.

The threshold 5/8 is the intersection `1-4a/5=1/2` between the two
available block bounds; it is not asserted to be optimal. Improving
it through these inputs requires a stronger block estimate or a way to
use cancellation across scales instead of Minkowski's inequality.
