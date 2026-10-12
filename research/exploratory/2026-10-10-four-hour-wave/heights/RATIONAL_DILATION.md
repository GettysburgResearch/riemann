# A full-axis rational dilation bound and a sharp tail obstruction

Status: elementary analytic lemmas and exact finite controls. These results
describe a potential mechanism for sharpening the annular proofs; they do
not upgrade the certified xi Pick order by themselves.

## 1. Full real-axis control

Fix positive numbers `x_1,...,x_n`, with repetitions allowed, and put

\[
 Q(b)=\prod_{j=1}^n(b+ix_j),\qquad
 \mathcal V=\{P(b)/Q(b):\deg P\le n-1\}.
\]

Every member of this `n`-dimensional rational Hardy space satisfies

\[
 \boxed{\|bR'(b)\|_{L^2(\mathbb R)}
 \le\sqrt{\frac{n(n+1)(2n+1)}6}\,
                    \|R\|_{L^2(\mathbb R)}.} \tag{D1}
\]

Here the measure is ordinary Lebesgue measure. No assumption on the scales
or separation of the positive `x_j` is needed.

To prove this, use the explicit Malmquist rational functions

\[
 e_k(b)=\sqrt{x_k/\pi}\,\frac1{b+ix_k}
                    \prod_{j<k}\frac{b-ix_j}{b+ix_j},\quad1\le k\le n.
 \tag{D2}
\]

Their norms are one because every product factor has modulus one on the real
axis and `int x_k/(pi(b^2+x_k^2)) db=1`. For `k>l`, cancellation in
`e_k conjugate(e_l)` leaves a rational integrand with all poles in the lower
half-plane and decay `O(b^-2)`. Closing a large semicircle in the upper
half-plane proves orthogonality. All `e_k` belong to `V`, including repeated
poles; `n` orthonormal functions in this `n`-dimensional space form a basis.

On the real axis the logarithmic derivative gives

\[
 \left|\frac{b e_k'}{e_k}\right|
 \le\left|\frac b{b+ix_k}\right|
       +\sum_{j<k}\frac{2|b|x_j}{b^2+x_j^2}\le k.
\]

Thus `||b e_k'||_2<=k`. Write `R=sum c_k e_k` and apply the norm triangle
inequality followed by Cauchy--Schwarz:
`||bR'||_2<=sum k|c_k|<=sqrt(sum k^2) sqrt(sum|c_k|^2)`.
This proves (D1).

For even `n` and real even numerator `P(b)=P_0(b^2)`,
`R(-b)=conjugate(R(b))`. More generally the sign is `(-1)^n` for any `n`.
The squared moduli of `R` and `bR'` are even, so (D1) also holds with both
norms over `(0,infinity)`. This statement applies directly to the rational
functions arising in the xi moment congruence.

## 2. Restricting both norms to a high tail cannot retain linear growth

There is a concrete obstruction to transferring (D1), or a possible sharper
`Cn` full-axis bound, to a norm over `[H,infinity)`. For every even
`n=2d+2`, there are rational functions

\[
 R_\epsilon(b)=\frac{\widetilde P_d(b^2)}
                    {\prod_{j=1}^n(b+i x_j(\epsilon))},
 \qquad\deg\widetilde P_d=d,
 \tag{D3}
\]

with all `x_j(epsilon)>0` distinct, for which

\[
 \lim_{\epsilon\downarrow0}
 \frac{\|bR_\epsilon'\|_{L^2([1,\infty))}}
      {\|R_\epsilon\|_{L^2([1,\infty))}}
 \ge\frac{n^2}4+\frac12. \tag{D4}
\]

Scaling `b=Hu` yields the same obstruction on `[H,infinity)` for every
positive `H`. Consequently no fixed `C` can give a uniform truncated-tail
bound `Cn`, or `Cn^(3/2)`, for this even-numerator class. A bound with an
`n^2` factor remains possible; it is not proven here.

## 3. Exact endpoint-kernel construction

Let `L_k` be the ordinary Legendre polynomial, normalized by `L_k(1)=1`.
Define the shifted endpoint reproducing kernel

\[
 P_d(v)=\sum_{k=0}^d(2k+1)L_k(2v-1),\quad
 \widetilde P_d(s)=s^dP_d(1/s).
 \tag{D5}
\]

Orthogonality on `[0,1]` gives exactly

\[
 P_d(1)=(d+1)^2,\qquad \int_0^1P_d(v)^2\,dv=(d+1)^2.
 \tag{D6}
\]

The zero-pole limiting function is
`R_0(b)=b^-2 P_d(b^-2)`. Write

\[
 S=\int_0^1v^{1/2}P_d(v)^2\,dv>0,\qquad
 U=\int_0^1v^{1/2}(P_d(v)+vP_d'(v))^2\,dv.
\]

Changing variables `v=b^-2` gives

\[
 \|R_0\|_{[1,\infty)}^2=S/2,\qquad
 \|bR_0'\|_{[1,\infty)}^2=2U. \tag{D7}
\]

Integration by parts has no boundary term at zero, and gives

\[
 \int_0^1v^{1/2}P_d(P_d+vP_d')\,dv
     =\frac S4+\frac{P_d(1)^2}{2}.
\]

Cauchy--Schwarz therefore implies

\[
 \frac{\|bR_0'\|}{\|R_0\|}
 =2\sqrt{U/S}\ge\frac{P_d(1)^2}{S}+\frac12
 \ge(d+1)^2+\frac12,
 \tag{D8}
\]

where the final inequality uses `S<=int P_d^2=(d+1)^2`. This is the analytic
all-degree proof of (D4), rather than an extrapolation from finite controls.

For a legal distinct-node family take
`x_j(epsilon)=epsilon(1+j/n)`, `1<=j<=n`. On `b>=1`, the rational functions
and their dilation derivatives converge pointwise to `R_0` and `bR_0'`.
Each denominator factor has modulus at least `b`, while the numerator has
degree `n-2`. Thus, uniformly for `0<epsilon<=1`, both functions are bounded
in modulus by a constant depending on `d` times `b^-2`. The derivative
bound follows directly by differentiating the quotient and using
`|b/(b+i x_j)|<=1`. The square of this majorant is integrable. Dominated
convergence gives convergence of both squared norms, and the denominator
norm tends to the positive value `S/2`. This proves (D4).

## 4. Mechanism boundary and replay

The tail obstruction concentrates a polynomial peak near the finite boundary
of the integration interval. Its positive poles tend below that boundary;
the full-axis norm then includes a large low-height contribution. It therefore
does not contradict (D1), nor rule out a stronger full-axis inequality.
Conversely, a full-axis estimate alone cannot control the relative high-tail
error in the xi source by simply restricting both norms.

[verify_rational_dilation.py](verify_rational_dilation.py) constructs the
shifted Legendre kernels with rational coefficients, checks (D6), the
integration-by-parts identity, and the squared lower bound from (D8) through
degree 32. Weighted integrals are exact because
`int[0,1] v^(j+1/2) dv=2/(2j+3)`. It also checks `sum k^2` exactly for sample
orders. The proof of orthonormality, dominated convergence, and the all-degree
obstruction is analytic; finite controls do not replace those arguments.
