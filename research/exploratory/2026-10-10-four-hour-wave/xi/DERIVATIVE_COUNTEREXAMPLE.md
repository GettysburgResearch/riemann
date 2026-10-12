# An exact obstruction to unpriced adjacent-order descent

Status: proposed exact synthetic theorem, with a complete elementary proof.
Scope: positive discrete Fourier sources; not the arithmetic theta source.
Coordinate: real zeros correspond to the `Xi(t)` convention.

## 1. An arbitrarily thin strip with real-rooted positive derivatives

Fix `0 < delta <= log 2`, put

\[
c=\cosh\delta,\qquad
\epsilon=\frac{\cosh\delta}{\cosh(2\delta)}
        =\frac{c}{2c^2-1},\qquad
F_\delta(z)=\cos z+\epsilon\cos(2z).
\]

This is the Fourier transform of the finite positive even measure with masses
`1/2` at `+/-1` and `epsilon/2` at `+/-2`. It is even, real entire of order
one and exponential type two, and bounded on the real line. Moreover

\[
10/17\le\epsilon<1.
\]

The lower bound follows because `c/(2c^2-1)` decreases for `c>=1` and
`cosh(log 2)=5/4`. Factorization gives

\[
F_\delta(z)=2\epsilon
 (\cos z+c)(\cos z-1/(2c)).                         \tag{D1}
\]

Consequently the complete zero set consists of the real zeros

\[
z=\pm\arccos(1/(2c))+2\pi k
\]

and the nonreal zeros

\[
z=(2k+1)\pi\pm i\delta,\qquad k\in\mathbb Z.       \tag{D2}
\]

All are simple. Thus all zeros lie in `|Im z|<=delta`, while two of the four
zeros per real period are nonreal, for every positive delta in this range.
Making the strip arbitrarily narrow does not change this count.

Nevertheless **every derivative of positive order has only real zeros**.
For `r=2k>=2`, up to an irrelevant sign,

\[
F_\delta^{(2k)}(z)=\cos z+w\cos(2z),\qquad
w=\epsilon 2^{2k}>1.
\]

Its zeros correspond to the two roots of `2w v^2+v-w=0`. Both roots lie
strictly in `(-1,1)` when `w>1`, so every solution of `cos z=v` is real.
For `r=2k+1>=1`, up to an irrelevant sign,

\[
F_\delta^{(2k+1)}(z)
 =\sin z\left(1+2\epsilon 2^{2k+1}\cos z\right).
\]

Here `epsilon 2^{2k+1}>1/2`, so both the sine zeros and the additional cosine
zeros are real and simple. These formulas enumerate all zeros; this is not a
numerical sample or a fixed-box assertion.

## 2. The frozen companion fails at the immediately adjacent order

For an arbitrary fixed `lambda>0`, define

\[
E_{j,\lambda}=F_\delta^{(j)}-i\lambda F_\delta^{(j+1)}.
\]

Differentiation gives the genuine frozen-parameter equality
`E'_(j,lambda)=E_(j+1,lambda)`.

On the complete lower ray `z=pi-iy`, `y>=0`, write

\[
f(y)=-\cosh y+\epsilon\cosh(2y),\quad
g(y)=f'(y)=\sinh y(4\epsilon\cosh y-1),\quad
h(y)=f''(y)=4\epsilon\cosh(2y)-\cosh y.
\]

Then

\[
E_{0,\lambda}(\pi-iy)=f(y)+\lambda g(y),\qquad
E_{1,\lambda}(\pi-iy)=i(g(y)+\lambda h(y)).          \tag{D3}
\]

For all `y>=0`, `g(y)>=0` and `h(y)>0`, since `4 epsilon>1` and
`cosh(2y)>=cosh y`. Therefore `E_(1,lambda)` is nonzero on the entire ray.
In contrast, `f(0)=epsilon-1<0`, `g(0)=0`, `f(delta)=0`, and `g(delta)>0`.
The derivative of `f+lambda g` is `g+lambda h>0`. It follows that there is
**exactly one** ray zero

\[
E_{0,\lambda}(\pi-i y_\lambda)=0,
\qquad 0<y_\lambda<\delta.                           \tag{D4}
\]

The exact adjacent quotient is

\[
\frac{iE_{0,\lambda}}{E_{1,\lambda}}(\pi-iy)
 =\frac{f(y)+\lambda g(y)}{g(y)+\lambda h(y)}.        \tag{D5}
\]

It is negative for `0<=y<y_lambda`, zero at `y_lambda`, and positive after
that point. Neither globally real-rooted positive derivatives nor a genuine
frozen derivative chain supplies positive signed transport back to order zero.

The zero moves strictly toward the real axis as lambda increases:

\[
\frac{dy_\lambda}{d\lambda}
 =-\frac{g(y_\lambda)}{g(y_\lambda)+\lambda h(y_\lambda)}<0.
\]

Changing the positive companion parameter therefore does not remove the
obstruction.

## 3. Exact residue and quantitative ray-zero bounds

The real critical point `pi` is a wrong-sign maximum. The simple pole of
`F/F'` there has positive residue

\[
\rho=\frac{F(\pi)}{F''(\pi)}
     =\frac{1-\epsilon}{4\epsilon-1}>0.              \tag{D6}
\]

The complete lower-ray analysis accounts for precisely this event, without
discarding an endpoint or a nonreal derivative block. On `0<=y<=delta`,
`h` increases, so

\[
h_0=4\epsilon-1\le h(y)\le
h_\delta=4\epsilon\cosh(2\delta)-\cosh\delta.
\]

Integrating twice from `f(0)=-(1-epsilon)` and `f'(0)=0` gives

\[
\sqrt{\lambda^2+\frac{2(1-\epsilon)}{h_\delta}}-\lambda
\le y_\lambda\le
\min\left\{\delta,\sqrt{\lambda^2+2\rho}-\lambda\right\}. \tag{D7}
\]

For the exact fixture `delta=log 2`, `epsilon=10/17`, these constants are

\[
\rho=7/23,\quad h_0=23/17,\quad h_\delta=15/4.
\]

Putting `q=exp(y)` converts (D4) into an exact rational quartic:

\[
\epsilon(1+2\lambda)q^4-(1+\lambda)q^3
 +(\lambda-1)q+\epsilon(1-2\lambda)=0,\quad1<q<2.   \tag{D8}
\]

At the positive-source native parameter
`lambda_0=(1+epsilon)/(1+2epsilon)=27/37`, (D5) at the real endpoint is
`-259/621`. At the limiting high-derivative parameter `lambda=1/2`, (D8)
reduces, after removal of the positive factor q, to
`(40/17)q^3-3q^2-1=0`.

As `delta->0`, `rho=delta^2/2+O(delta^4)`, although the nonreal-zero count
per period stays equal to two. A uniform lower charge per wrong extremum
therefore cannot be inferred from a thin-strip assumption alone.

## 4. What this does and does not refute

This refutes generic descent from positive Fourier sources, strip localization,
or globally real-rooted high derivatives without a signed adjacent-order
ledger. It does not refute the reviewed reverse-Rolle identity, which retains
these wrong extrema, and it does not refute any correctly stated exact-theta
transport theorem. No such decisive exact-theta transport bound is proved here.

The smooth construction in `THETA_TAIL_OBSTRUCTION.md` separately shows that
matching the actual theta tail does not cure the generic gap. Its perturbed
transform is not asserted to retain the discrete model's global zero strip or
global real-rootedness of every positive derivative.
