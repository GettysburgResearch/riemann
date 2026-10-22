# Reassembling the cube inverse and the signed complement

22 October 2026. **Exact local identity and convergence-domain audit.**
The local cancellation below is not an analytic continuation theorem for
the remaining coherent Gauss series. In particular it does not permit
replacing a rectangular weight by a product-only weight.

Dependencies and normalizations are those listed in
`COMPLETED_RECTANGLE.md`. Every phase and omitted Euler factor is retained.
The finite ray characters below arise by expanding the actual reflected
cusp matrix; the nontrivial ones must not be silently replaced by one.

## 1. The actual uncompleted two-variable series

Write

\[
R_r(s;\ell)=Q_r(s;\ell)/L_E^{(3r)}(3s-1/2,\alpha^{3\ell}),
\]

and initially, for `Re s>1`, `Re w>1`, define

\[
\mathcal D(s,w)=\sum_r^*\mu_E(r)\widetilde g(r)
       \alpha(r)^\ell(Nr)^{-w}R_r(s;\ell).
\tag{1}
\]

Twisted Gauss multiplicativity, with its natural common-prime zero,
gives the exact absolutely convergent identity

\[
\mathcal D(s,w)=\sum_n^*\widetilde g(n)\alpha(n)^\ell(Nn)^{-s}
                  \prod_{\mathfrak p\mid n}(1-q^{s-w}).
\tag{2}
\]

In particular,

\[
                    \mathcal D(s,s)=1\qquad(\Re s>1).
\tag{3}
\]

The unit ideal supplies the right side. Equation (3) is a complete
Möbius convolution, not a statement about a fixed rectangular dyad.
The smooth raw rectangle is a two-dimensional Mellin integral of (1)
against `A^s B^w W_hat(s) f_hat(w)`. Its weight does not constrain
`w=s`.

## 2. The exact local factor after reflection

In one actual reflected finite-ray component, put

\[
 z_1=3s-\tfrac12,\qquad
 z_2=2s+w-\tfrac12,\qquad z_3=w+1-s,
\tag{4}
\]

and for a good prime outside the extracted divisor `k` set

\[
 x=\alpha(\mathfrak p)^{3\ell}q^{-z_1},\qquad
 z=\varphi(\mathfrak p)\alpha(\mathfrak p)^{3\ell}q^{-z_2},
 \qquad y=\varphi(\mathfrak p)q^{-z_3}.
\tag{5}
\]

The signed complementary prime in (T5), after division by the deleted
cube factor, is `(z-y)/(1-x)`. The common reciprocal cube factor
contributes `1-x` at the same prime. Therefore the combined local factor
is exactly

\[
\boxed{\qquad H_{\mathfrak p}(s,w)=1-x+z-y.\qquad}
\tag{6}
\]

At primes dividing `k`, the common reciprocal factor and the deletion
in `L^(3r)` cancel exactly. Thus the reassembled product is directly
over primes not dividing `3k`, with the fixed ray exclusions retained.
It is incorrect to count the same inverse Euler factor again there.

One exact factorization is

\[
 H_{\mathfrak p}
 =\frac{(1-x)(1-y)}{1-z}
       \left[1+\frac{(x-z)(z-y)}{(1-x)(1-y)}\right].
\tag{7}
\]

Hence its meromorphic continuation can be written

\[
\boxed{\displaystyle
 H_k(s,w)=
 \frac{L_E^{(3k)}(z_2,\varphi\alpha^{3\ell})}
 {L_E^{(3k)}(z_1,\alpha^{3\ell})
  L_E^{(3k)}(z_3,\varphi)}\;\mathcal E_k(s,w).
}
\tag{8}
\]

The correction is the product of the bracketed factors in (7),
defined directly over the retained primes. No quotient by the possibly
zero factor `H_p` is used.

The factorization has been checked by the elementary polynomial identity

\[
 (1-x+z-y)(1-z)-(1-x)(1-y)=(x-z)(z-y).
\tag{9}
\]

## 3. A complete convergence tube for the correction

The product defining `E_k` converges absolutely and locally uniformly
in the tube

\[
\begin{gathered}
 \Re z_1>0,\quad \Re z_3>0,\\
 \Re(z_1+z_2)>1,\quad \Re(z_1+z_3)>1,\quad
 2\Re z_2>1,\quad \Re(z_2+z_3)>1.
\end{gathered}
\tag{10}
\]

Indeed, the two local denominators in the correction are bounded below
by `1-q^(-Re z_1)` and `1-q^(-Re z_3)`. Its numerator is the sum
`xz-xy-z^2+zy`; each of the four corresponding prime series converges
by the listed inequalities. The resulting compact-subtube upper bound
is uniform in `k`, since removing primes only reduces this absolute
majorant. Holomorphy is asserted, not nonvanishing of every correction
factor.

Let `sigma=Re s`, `upsilon=Re w`. A common zero-free bound `beta`
for the two denominator families and the same reciprocal estimates
as above therefore give a pole-free region for (8) whenever

\[
\begin{split}
 \sigma&>(\beta+1/2)/3,\\
 \upsilon&>\max\{\beta-1+\sigma,\;2-5\sigma,
          \;1/2-2\sigma,\;1-2\sigma,\;1/4-\sigma/2\}.
\end{split}
\tag{11}
\]

The numerator character has nonzero angular order, so its Hecke
function has no principal or translated-principal pole. If `varphi`
is principal, its pole in the denominator creates a zero of (8),
not a pole. Deleted Euler factors cost prescribed small powers of `Nk`.

## 4. The diagonal cancellation, and its exact limitation

When `varphi=1` and `w=s`, one has `z=x`, so (6) reduces to

\[
                      H_{\mathfrak p}(s,s)=1-q^{-1}.
\tag{12}
\]

On the diagonal portion of the tube (10), namely `Re s>1/3`,
the angular ratio in (8) cancels identically, `E_k=1`, and the
remaining reciprocal principal L-function is evaluated at one.
The meromorphic continuation of this individual factor is zero.

This is **not** a proof that the original series (1) is zero: (3)
says it is one in its defining diagonal half-plane. The remaining
reflected `k` sum and the finite cusp components cannot be evaluated
term by term at the diagonal without their own continuation. A
singular contribution can exactly compensate the zero of the Euler
factor. For nontrivial `varphi`, `z=varphi(p)x` at `w=s`, so even
the elementary cancellation (12) is absent in that component.
All of these components remain in the actual reflection.

Consequently (12) is a useful exact structural identity, but a
zero-times-divergent-series substitution would be wrong. A product-only
weight that invokes the complete convolution (3) also removes the
nontrivial detector; it is not the original rectangular problem.

## 5. Where the remaining Gauss series converges

Apart from the retained gamma and finite-profile factors, the
reflected coherent `k` series contains

\[
 \sum_k^*\mu_E(k)\widetilde g(k)\kappa(k)\alpha(k)^{2\ell}
 \varphi(k)(Nk)^{1/2-s-w}
 Q_{k,\kappa}(1-s;-\ell) H_k(s,w).
\tag{13}
\]

For `1/4<sigma<1/2`, the supplied natural-count cubic mean on
`1-s`, followed by Cauchy on a dyad, costs `K^(1+epsilon)`.
In a strict subdomain of (11), the Euler ratio and its omitted
factors cost `K^epsilon` and a fixed polynomial in the Mellin heights.
Thus the absolute dyadic resource for (13) is

\[
                         K^{3/2-\sigma-\upsilon+\epsilon}.
\tag{14}
\]

It converges only when

\[
                         \upsilon>3/2-\sigma.
\tag{15}
\]

At the current cube-removal line
`p=(B_flat+1/2)/3 ~= 0.458295549013321`, condition (15) says
`upsilon>1.041704450986679`. The local Euler product already
continues much farther, to approximately `upsilon>0.333182196053286`
at this limiting line, but the supplied estimate for the coherent
Gauss series does not. Taking these contours only reproduces

\[
               A^{p+\epsilon}B^{3/2-p+\epsilon},
\tag{16}
\]

the existing pure-cubic Type-I bound. A new cancellation theorem for
(13), including its diagonal singular contribution, would be needed
to improve the rectangular raw sum by this route. The larger local
Euler domain alone is not such a theorem.

At a zero of `L_E(z_1,alpha^(3ell))`, the numerator in (8) does
not cancel it for an open set of independent `w`; equality on the
single diagonal is insufficient for a two-dimensional contour shift.
The rectangular Mellin kernel has two independent variables and must
retain residues crossed in either of them.

## 6. The quadratic conductor at the binding physical scale

For the quadratic/sextic pair, the source's full conductor factor is

\[
                   (Nr)^{1/2-2s} H^{1-2s},
\tag{17}
\]

where `H` is the quadratic conductor norm. In the full-divisor
term, `k=r~B`, so the free-inner reflected length ratio is

\[
                           BH^2/A.
\tag{18}
\]

The short-complement cutoff from the proof of the completed rectangle
would have to lie below `A/(BH^2)`. At the actual terminal
`A=HB`, this upper scale equals `1/H`. For `H>1` there is no
nonempty complementary ideal range below it, including the full
divisor `m=1`. Thus the completed pure-cubic result cannot remove
the quadratic terminal obstruction.

If `H` stays bounded, the terminal ratio `A/B=H` stays bounded as
well. The factor `(A/B)^(-(1-beta/2))` in the completed theorem
then supplies only a constant, not a power saving in the growing
parameters. Therefore neither growing nor bounded quadratic
conductors yield a new saving on this binding terminal face.
The length mechanism would become available only in free completed
blocks with `A/(BH^2)` growing by a positive power. A uniform
moving-`H` theorem for those longer blocks is not asserted here:
it would additionally require the finite-twist complementary
numerator bounds and the corresponding paired moment.

Even grant an optimistic natural-count right-line mean for every
quadratic conductor and preserve all other interfaces. On
`s=1/2-delta`, the full-divisor magnitude then costs

\[
                  A^{1/2-\delta}H^{2\delta}B^{1+\delta}.
\tag{19}
\]

At `A=HB`, divide by the terminal `sqrt(AB)`, square, and sum
over `O(H)` quadratic rows. The resulting upper-bound resource is

\[
                           H^{1+2\delta}B.
\tag{20}
\]

As `delta` tends to zero this reaches only the inherited `HB`
edge. At each positive fixed `delta` it has the extra
`H^(2delta)` cost. These are exact costs of the supplied bounds,
not lower bounds for the actual terminal norm. A coherent
quadratic-label estimate beyond those inputs is still required.

The two-variable identity therefore exposes, rather than closes,
the exact missing analytic continuation and physical-conductor
estimates. No zero-free improvement is asserted from it.
