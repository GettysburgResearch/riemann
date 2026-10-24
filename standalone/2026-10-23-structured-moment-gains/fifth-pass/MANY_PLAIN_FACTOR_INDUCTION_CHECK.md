# The six-full-factor ordinary moment: the exact missing closure

24 October 2026. Source-level investigation, not an impossibility theorem
for the underlying moment. No new global zero-free boundary is claimed.

## 1. The genuinely shorter proposed ordinary moment

The new question concerns the ordinary squarefree coefficient
\(\mu^2(n)d_6(n)\alpha(n)^2\), with column length
\(B=U^3\) and an ordinary row width \(K=U^4\). Relative
to base \(K\), its total column exponent is \(3/4\).
The exact Euler factorization
\[
 \mu^2d_6=1^{*6}*g_6,
 \qquad \sum_{j\ge0}g_6(p^j)x^j=(1+6x)(1-x)^6
\]
has a powerful correction, since its linear coefficient is zero.
The leading small-correction term therefore has six full smooth
factors, initially of length \(K^{1/8}\) in the balanced
configuration. This is a different range from six central factors
of total length \(3M\), or a three-factor product of total
length \(3M/2\). The initial total length here is genuinely
\(A=3M/4\).

The pinned input is the quasi-Riemann source
`openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`, local exact
source `arithmetic_lane/ope26a_source.tex`, SHA256
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`.
The relevant identities are `eq:first-poisson-bridge`,
`old-eq:2.8`, `old-eq:2.12`, `old-eq:2.13`, and `old-eq:2.14`.

## 2. The unchanged common-support-free child

The algebraic first and second transforms make sense for a fixed number
of full factors: extraction has a fixed divisor multiplicity, and a
common multiplicative angular character distributes across all of them.
This observation alone does not prove an induction theorem.

Consider the exact zero-slot branch with both common supports trivial,
all extracted lengths zero, and the first frequency at its nominal
scale. With \(q=0\), write the positive width step as \(s\).
The source gives
\[
 K_0=2A-M,\quad K_{\rm freq}=K_0,\quad J=0,
 \quad g=s,\quad \ell=0.
\]
The second transform then has
\[
 \boxed{M'=M-s,\qquad A'=A,\qquad
         \Delta_{\rm child}=0.}
 \tag{1}
\]
All six individual factor lengths are unchanged on this branch.
The new row range is nonempty throughout the proposed initial
\(A=3M/4\) range and its later descendants. No common-support
count or extraction weight supplies a hidden positive allowance.

The second-transform zero frequency is the genuine positive diagonal.
On this branch its exponent exceeds the permitted Gauss-norm exponent
by exactly
\[
 K_0+g-A=A-M+s.
 \tag{2}
\]
Equation (2) is the common-support-free specialization of
`old-eq:2.12`. The original argument can absorb a small padding or
one small width step, but it cannot absorb a fixed positive
\(A-M\) after many descents.

For a concrete trace, normalize the original width to one, put
\(A=3/4\), and take all six lengths equal to \(1/8\).
Repeated children (1) leave those lengths unchanged and lower \(M\)
through \(3/4\). When \(M\) is near \(3/4\), each
factor is still much shorter than \(M/2\). Reflecting an individual
full factor changes its length from \(a_i\) to \(M-a_i\),
and changes the total by \(M-2a_i>0\). It therefore increases
the total at precisely the point where the induction needs to shorten
it. At \(M=1/2\), the diagonal excess in (2) is already about
\(1/4\), while every factor remains of length \(1/8\).

The source's two-factor zero-slot proof has a different closure: after
reflecting each factor longer than \(M/2\), the sum of its two
remaining lengths is at most \(M\), apart from the prescribed
small padding. For six factors the same operation gives only the bound
\(3M\). It does not return descendants (1) to the needed region.
Thus the initial \(3M/4\) slack is spent under descent; it is
not a preserved invariant.

## 3. What fixed angular order two does and does not change

On the common-support-free branch the angular coefficient is
multiplicative, so it can be kept as one common angular type on every
full factor. The finite character operations in the two transforms do
not cancel a nonzero infinite type. This can remove the fixed finite
inducing-character volume main term that motivated the original
\(5M/6\) uncentered threshold. It is a useful simplification.

It does not remove (2). On the second-transform diagonal the column
coefficient is multiplied by its conjugate, so the unit angular factor
has absolute square one. The diagonal is positive and contains no
angular cancellation. A proof using it as a positive majorant still
requires a replacement for the closure above. The disappearance of a
fixed-character polar main term is therefore insufficient by itself.

An adequate new input would be a uniform zero-loss estimate for the
six-factor transition region with all \(a_i\le M/2\) and
\(\sum_i a_i\) near or just above \(M\), with the natural
moving masks and fixed angular type retained. At the balanced point
this includes a twelfth moment of a full smooth sum of length
\(K^{1/6}\). Alternatively, a new signed transform argument
would have to avoid the positive majorant producing (2). Neither input
is contained in the pinned two-plain-factor theorem.

## 4. A further size-model check at the actual 3/4 ratio

The frozen `RECTANGULAR_EXPONENT_OBSTRUCTION.md` (SHA256
`543b36ecc9171594957ac895510bc3156db84b5d8af69efa75f89bb7251f5b56`)
supplies a feasible copied-factor size model even if one grants its
cubic-sieve/Gram inequalities. Scaling
that model to row width one and total length \(3/4\), set
\[
 r=1/\sqrt2,\qquad a_i=1/8\ (1\le i\le6),\qquad
 v_i=\rho a_i,\qquad \rho=(3-\sqrt2)/2.
\]
All six factors are short; their full-sum functional-equation length
and value transforms obey the same model inequalities. The resulting
normalized moment exponent is
\[
 r+2\sum_i v_i-\sum_i a_i
   =\frac{6-\sqrt2}{4}
   =1.1464466094\ldots>1.
\]
This is a formal compatibility check, not an arithmetic construction,
and it is not a substitute for auditing the sextic source. It shows why
merely repeating the earlier factor-size inequalities does not give the
desired diagonal estimate at the shorter \(3/4\) ratio either.

## 5. The signed sixth-power consumer remains separate

Even an optimal positive bound for the proposed Gauss moment would
not on its own close the actual sixth-power consumer. At its scales
\(H=U^2\), \(B=U^3\), the Cauchy factor is
\[
 \frac{U}{\sqrt B}\sqrt H\sqrt{J_6(H,B)}
      =U^{1/2}\sqrt{J_6(H,B)}.
\]
The hypothetical bound \(J_6\ll H+B\) gives \(U^2\).
Even a bound retaining only the unavoidable row-diagonal term \(H\)
would give \(U^{3/2}\). Those exponents do not reach the proposed
global sixth-moment target.

The linear signed Poisson transform has scale \(B/H\), whereas
the positive pair norm has scale \(B^2/H\). Its phase cancellation
can be checked directly. For the actual conjugate sixth-dual column
\(\theta(n)=\alpha(n)\overline{G_{\rm ray}(n)}\), the source
identity \(\gamma_1\gamma_2=\mu\alpha G_{\rm ray}\) gives
\[
 \mu(n)\gamma_2(n)\theta(n)\gamma_1(n)\alpha(n)^{-2}
       =\mu(n)^2.
\]
The factor \(\alpha(n)^{-2}\) is the angular Hankel multiplier:
the angular transform at \(k/n\) has
\(\alpha(k/n)^2=\alpha(k)^2\alpha(n)^{-2}\), up to the
fixed field phase. The resulting \(k\)-row length is
\(B/H=U\), and the original physical root-angle/Dirichlet
coefficient form returns. With the paired smooth kernels this is the
inverse Fourier operation, so the exact linear transform alone gives
no new size bound. A complete numerical consumer needs additional
cancellation in that coherent signed form, alongside any new positive
ordinary-moment theorem.
