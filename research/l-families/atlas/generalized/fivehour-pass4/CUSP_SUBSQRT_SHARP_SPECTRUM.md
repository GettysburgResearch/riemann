# Sharp native cusp spectrum below the square-root scale

Status: complete analytic proof; independent review required.  No
period-zero, quotient, or RH conclusion.  The target was frozen before the
proof at `c254b9844`.

Authoring parent: `09ca23951`.  Retain the exact notation and normalization
of the accepted K/L packets.  In particular `nu=k-1`, `T_k` is the
Petersson compression of the finite part `E_0=h+r_0`, and

\[
 m_{k,J}={\nu\over24J}-{1\over2}\log{\nu\over4\pi J}+c_0.
\]

## Frozen target

For every sequence of even weights and indices

\[
 1\le J=J_k=o(\sqrt{k}),
\]

prove the strict refinement of Theorem L

\[
 \boxed{\lambda_J(k)=m_{k,J}+o(1).}                 \tag{S1}
\]

The intended new step is to remove L's fixed `R_1` upper loss.  On the
coefficient flag `W_J`, use full-cusp Parseval to split the `n=J` Fourier
mass from `n>J` and the compact mass.  The radial conditional-Gamma symbols
must satisfy

\[
 \mu_{\nu,4\pi J}-\mu_{\nu,4\pi(J+1)}\longrightarrow\infty,    \tag{S2}
\]

uniformly in this range.  Any mass outside the first Fourier mode then pays
an unbounded radial loss.  For the retained `n=J` mass, prove that it lies
above a height tending to infinity, where the nonconstant term `r_0`
vanishes exponentially.  The loss must absorb all compact and cross-term
contributions without assuming the Fourier pieces are orthogonal below
height one.

## Stop conditions

- Preserve the fixed-width L theorem if the compact/cusp bookkeeping does
  not yield a uniform `o(1)`.
- Do not claim S1 for the full `J=o(k)` range.
- Do not infer the first correction to a period zero; the exact-period
  analytic remainder is a separate term.
- Do not infer scalar quotient noncancellation or interlacing.

## 1. The radial gap is unbounded

Write

\[
 h(y)={\pi y\over6}-{1\over2}\log y+c_0,
 \qquad E_0(z)=h(y)+r_0(z).
\]

For rate `a=4*pi*n`, let `mu_(nu,a)` be the expectation of h under the
Gamma density `y^(nu-1) exp(-ay)` conditioned on `y>=1`, exactly as in L.
The conditioning error in L7 is superpolynomially small uniformly for
`n=J,J+1` when `J=o(sqrt(k))`.  Hence L8 gives

\[
 \begin{aligned}
 d_{k,J}
 &: =\mu_{\nu,4\pi J}-\mu_{\nu,4\pi(J+1)}\\
 &= {\nu\over24J(J+1)}
    -{1\over2}\log{J+1\over J}+o(1)\longrightarrow\infty .    \tag{S3}
 \end{aligned}
\]

The convergence is sequentially uniform over the declared range: a failure
would select a sequence `J=o(sqrt(k))` contradicting S3.  Also

\[
 \mu_{\nu,4\pi J}=m_{k,J}+o(1),qquad
 \mu_{\nu,4\pi J}\longrightarrow\infty.             \tag{S4}
\]

## 2. Radial loss on the complete coefficient flag

Take a Petersson-unit vector `f in W_J`, so its cusp expansion has no
Fourier terms below J.  On the full width-one cusp `y>=1`, Parseval gives an
orthogonal norm decomposition.  Let

\[
 c_J+c_>+c_K=1                                      \tag{S5}
\]

be respectively the Petersson mass of the `n=J` cusp term, all `n>J` cusp
terms, and the compact part of the fundamental domain.  These are
nonnegative; no orthogonality is asserted on the compact part.

The conditional Gamma family is stochastically decreasing in n and h is
increasing on `y>=1`.  If `M_h` is a fixed upper bound for h on the compact
part, full-cusp Parseval therefore gives

\[
 \langle f,hf\rangle
 \le \mu_{\nu,4\pi J}c_J
    +\mu_{\nu,4\pi(J+1)}c_>+M_hc_K
 \le \mu_{\nu,4\pi J}-D_{k,J}(c_>+c_K),             \tag{S6}
\]

where

\[
 D_{k,J}=\min\{d_{k,J},\mu_{\nu,4\pi J}-M_h\}
 \longrightarrow\infty.                            \tag{S7}
\]

Thus every component which is not the first allowed full-cusp Fourier mode
pays an unbounded radial loss.  This is the information discarded by the
uniform `R_1` estimate in L.

## 3. The nonconstant Fourier term is absorbed

Put

\[
 H_{k,J}=\sqrt{\nu/(4\pi J)}\longrightarrow\infty.
\]

For the conditioned `n=J` Gamma law, the mass below this height is at most

\[
 \tau_{k,J}
 \le 2\left(e\sqrt{4\pi J/\nu}\right)^\nu=o(1),      \tag{S8}
\]

for all sufficiently large k.  Indeed the unconditioned lower tail is at
most `(4*pi*J*H)^nu/Gamma(nu+1)`, Stirling's elementary lower bound
`Gamma(nu+1)>=(nu/e)^nu` gives the displayed expression, and the
conditioning probability above one tends to one.  The harmless factor two
absorbs that conditioning.

On the cusp,

\[
 |r_0(z)|\le R(y):={2e^{-2\pi y}\over(1-e^{-2\pi y})^2},
 \qquad R(1)=R_1,quad R(H_{k,J})=o(1).               \tag{S9}
\]

After integrating over the complete x-period, the mass in
`1<=y<H_(k,J)` is at most `tau_(k,J)c_J+c_>` by Parseval.  If `M_r` bounds
`|r_0|` on the compact part, S5 and S8--S9 give

\[
 |\langle f,r_0f\rangle|
 \le R(H_{k,J})+R_1\tau_{k,J}+R_1c_>+M_rc_K
 \le o(1)+C(c_>+c_K),                               \tag{S10}
\]

with one fixed C.  This estimates all cross terms through the literal
`|f|^2` mass; it does not diagonalize multiplication by `r_0` and uses no
compact-region Fourier orthogonality.

Combining S6, S7 and S10, and taking k large enough that `D_(k,J)>C`, yields

\[
 {\langle f,T_kf\rangle\over\langle f,f\rangle}
 \le\mu_{\nu,4\pi J}+o(1)=m_{k,J}+o(1),              \tag{S11}
\]

uniformly on the unit sphere of `W_J`.  Since `W_J` has codimension at most
`J-1`, min--max proves the upper half of S1.  The lower half is Theorem L's
Poincare-subspace bound, already valid throughout `J=o(k)`.  This proves S1.

## 4. Exact boundary

The only new range restriction is S3: the adjacent radial symbols are
separated by order `k/J^2`, which diverges precisely in the stated
sub-square-root regime.  This proof neither asserts nor denies an `o(1)`
remainder closer to the square-root scale.  In the sub-cube-root range of
Theorem R, S1 sharpens the center eigenvalue but does not remove R's
`O(j log k)` exact-period remainder, so no fine zero displacement follows.
