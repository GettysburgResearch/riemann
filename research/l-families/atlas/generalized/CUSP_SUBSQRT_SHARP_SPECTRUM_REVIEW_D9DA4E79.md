# Independent review: sharp native cusp spectrum below square-root scale

Verdict: **PASS** for Theorem S at exact scientific commit
`d9da4e7942821215789ba7c3c2187e538267c024`.

Review date: 2026-09-01. The reviewed object is the complete 181-line proof
`fivehour-pass4/CUSP_SUBSQRT_SHARP_SPECTRUM.md`, Git blob
`2617c77c24a5625b1fd9963b031d76260f35e862`, normalized-LF SHA256
`15571f02949f728f0ed33d78245ac430bacfd938ca8d7b44a966df0fd9234614`.
Its target was frozen at
`c254b98446c5c31de7bb1fb699844cb68d943225`; the exact science delta is
one proof file (132 insertions and 2 deletions). I also read the full
accepted Theorem K and Theorem L proofs and the independent Theorem L review
at scientific commit `f1a158015a400a1ba9fc36fe16639cfb5c2f7c1a`.
No scientific source was edited and no push was made.

## Mathematical audit

For every sequence of even weights `k -> infinity` and indices
`1 <= J=o(sqrt(k))`, the proof establishes

    lambda_J(k) = m_(k,J) + o(1)

with an absolute sequential remainder. The load-bearing steps check as
follows.

1. For the two rates `4*pi*J` and `4*pi*(J+1)`, the conditioning errors in
   Theorem L are absolute `o(1)`, uniformly in the sequential sense. Thus

       d_(k,J) = nu/(24*J*(J+1))
                 - log((J+1)/J)/2 + o(1) -> infinity.

   The positive term has order `k/J^2`, whereas the logarithmic term tends
   to zero. This is exactly where `J=o(sqrt(k))` is used. The same estimate
   gives `mu_(nu,4*pi*J)=m_(k,J)+o(1)` and this quantity tends to infinity.

2. On the complete cusp rectangle `y>=1`, integration over the full
   `x`-period makes the Fourier terms orthogonal. Consequently `c_J` and
   `c_>` are the exact masses of the first retained Fourier term and all
   later terms; `c_K` is the remaining compact fundamental-domain mass and
   `c_J+c_>+c_K=1`. No compact-region Fourier orthogonality is used.

3. The function `h(y)=pi*y/6-log(y)/2+c_0` is increasing for `y>=1`.
   Conditional Gamma laws of the common shape `nu` are stochastically
   decreasing as their rates increase. Together with a fixed compact upper
   bound this gives the loss

       D_(k,J)=min(d_(k,J), mu_(nu,4*pi*J)-M_h) -> infinity

   against all mass `c_>+c_K` outside the first allowed cusp mode.

4. With `H=sqrt(nu/(4*pi*J))`, the unconditioned Gamma lower tail is at
   most `(4*pi*J*H)^nu/Gamma(nu+1)`. The elementary lower bound
   `Gamma(nu+1)>=(nu/e)^nu`, followed by conditioning above one, proves

       tau_(k,J) <= 2*(e*sqrt(4*pi*J/nu))^nu = o(1).

   This is an absolute sequential bound and does not assume a fixed `J`.

5. The literal pointwise estimate for `r_0` is integrated against
   `|f|^2`. Below `H`, Parseval bounds the cusp mass by
   `tau_(k,J)c_J+c_>`; above `H`, the cusp bound tends to zero; and on the
   compact part a fixed bound suffices. Hence

       |<f,r_0 f>| <= o(1)+C*(c_>+c_K).

   This pays all cross terms without diagonalizing multiplication by
   `r_0`. Since `D_(k,J)>C` eventually, the preceding radial loss absorbs
   both the compact and higher-Fourier contributions uniformly on the unit
   sphere of the coefficient flag.

6. The flag `W_J` has codimension at most `J-1`, so the decreasing-order
   Courant--Fischer formula gives the upper bound for the same eigenvalue
   `lambda_J`. Theorem L supplies the lower bound on its `J`-dimensional
   Poincare span in the larger range `J=o(k)`. There is no indexing shift or
   dimension gap, since `J<=dim V_k` eventually in the declared range.

The result is a native compression spectral asymptotic. It does not prove a
period zero, a quotient statement, simplicity, an effective onset, or any
RH/GRH assertion. It also makes no assertion at the square-root scale.

## Nonmaterial typography

Two displayed lines contain plain `qquad`/`quad` where `\qquad` was
intended (S4 and S9). They affect rendering only and do not change any
definition, estimate, or inference. I therefore do not classify them as a
scientific repair condition.

This theorem is proof-only: it introduces no producer, fixture, or finite
test module. The verdict rests on the complete analytic proof and its exact
accepted K/L dependencies, not on numerical sampling.
