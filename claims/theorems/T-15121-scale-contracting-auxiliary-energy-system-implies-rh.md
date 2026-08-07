# T-15121 — Scale-contracting auxiliary-energy systems imply RH

Claim ID: `T-15121`  
Title: A finite row-energy system with strict logarithmic scale contraction and subexponential coefficients forces subexponential prime energy  
Status: **PROPOSED EXACT COMPOSITION THEOREM PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15151`, `L-15154`, `L-15155`  
Scope: exact replacement for the adjacent-block coefficient-`<1` recurrence

## 1. Finite vector system

Fix an integer `r>=1`, an initial index `J0`, and a contraction

\[
 0<\delta<1.
 \tag{T-15121.1}
\]

Let

\[
 E_i(J)\ge0,
 \qquad1\le i\le r,
 \qquad J\ge J_0,
 \tag{T-15121.2}
\]

be finite source-bound block energies. Suppose that for every sufficiently large
`J`,

\[
 \boxed{
 E_i(J)
 \le a_i(J)
 +\sum_{h=1}^r b_{ih}(J)
 \max_{J_0\le k\le\lfloor(1-\delta)J\rfloor}E_h(k).}
 \tag{T-15121.3}
\]

Assume all coefficients are nonnegative and

\[
 \boxed{
 \max_i\log(1+a_i(J))=o(J),
 \qquad
 \max_{i,h}\log(1+b_{ih}(J))=o(J).}
 \tag{T-15121.4}
\]

Then

\[
 \boxed{
 \max_{1\le i\le r}E_i(J)=\exp(o(J)).}
 \tag{T-15121.5}
\]

No coefficient smaller than one is required.

## 2. Proof

Put

\[
 M(X)=1+\max_{\substack{1\le i\le r\\J_0\le J\le X}}E_i(J).
 \tag{T-15121.6}
\]

Fix `epsilon>0`. By (T-15121.4), after increasing a threshold `X_epsilon`,

\[
 1+a_i(J)\le e^{\epsilon J},
 \qquad
 1+b_{ih}(J)\le e^{\epsilon J}
 \tag{T-15121.7}
\]

for `J>=X_epsilon`. Absorbing the finite range and the number `r` into a
constant `C_epsilon`, (T-15121.3) gives

\[
 \boxed{
 M(X)
 \le C_\epsilon e^{\epsilon X}
 M((1-\delta)X)}
 \tag{T-15121.8}
\]

for all sufficiently large `X`.

Iterate until `(1-delta)^mX<X_epsilon`. Then

\[
\begin{aligned}
 \log M(X)
 &\le
 \epsilon X\sum_{j=0}^{m-1}(1-\delta)^j
 +m\log C_\epsilon+O_\epsilon(1)\\
 &\le {\epsilon\over\delta}X+O_\epsilon(\log X).
\end{aligned}
 \tag{T-15121.9}
\]

Since `epsilon` is arbitrary,

\[
 \log M(X)=o(X),
\]

which proves (T-15121.5).

## 3. Matrix and multiple-lag form

The same proof applies when the right side of (T-15121.3) is a finite sum over
lags

\[
 b_{ih\nu}(J)
 \max_{k\le\alpha_{ih\nu}J}E_h(k),
 \qquad
 \alpha_{ih\nu}\le1-\delta.
 \tag{T-15121.10}
\]

Thus a finite auxiliary-energy vector may contain separate:

- ordinary-prime rows;
- full-von-Mangoldt rows;
- Type-I rows;
- balanced Type-II rows;
- Möbius packets;
- divisor/logarithmic rows;
- prime-power correction rows;
- transformed-window rows.

Closure under a single scalar prime block is not required.

## 4. Tensor-product corollary

Some exact convolution packets yield products of lower-scale energy factors.
Suppose instead that

\[
 E_i(J)
 \le a_i(J)
 +\sum_{\nu}b_{i\nu}(J)
 \prod_{s=1}^{m_\nu}
 \left[
 1+\max_{k\le\alpha_{\nu s}J}E_{h_{\nu s}}(k)
 \right]^{\theta_{\nu s}},
 \tag{T-15121.11}
\]

where the number of terms is finite, all coefficient logarithms are `o(J)`,
and

\[
 \boxed{
 \kappa:=\max_\nu
 \sum_{s=1}^{m_\nu}\theta_{\nu s}\alpha_{\nu s}<1.}
 \tag{T-15121.12}
\]

Then the same logarithmic induction gives

\[
 \max_iE_i(J)=\exp(o(J)).
 \tag{T-15121.13}
\]

Indeed, if `L(X)=log M(X)`, then

\[
 L(X)\le o(X)+\max_\nu
 \sum_s\theta_{\nu s}L(\alpha_{\nu s}X),
 \]

and iteration contracts the linear scale by at least the factor `kappa`.

This is the natural composition theorem for a finite tensorized Type-II packet.

## 5. RH conclusion

Assume one component is either

\[
 E_{i_0}(J)=\mathcal B_J^{\mathbb P}
 \quad\text{or}\quad
 E_{i_0}(J)=\mathcal B_J^{\Lambda}
 \tag{T-15121.14}
\]

for a compact safe window. By (T-15121.5) or (T-15121.13),

\[
 \mathcal B_J^{\mathbb P}=\exp(o(J)).
 \]

The equivalence of the prime and full-von-Mangoldt blocks is `L-15154`.
Summing the unit blocks gives a cumulative energy `exp(o(X))`. The standalone
Hardy transfer `L-15151` then forces the rightmost shifted zeta-pole exponent to
be zero. Therefore

\[
 \boxed{
 \text{a closed scale-contracting auxiliary-energy system}
 \quad\Longrightarrow\quad\mathrm{RH}.}
 \tag{T-15121.15}
\]

## 6. Why this theorem repairs the previous recurrence target

The earlier scalar recurrence required an adjacent-block coefficient below one.
A finite Vaughan or Heath--Brown packet more naturally separates factors at
strict fractions of the logarithmic scale. In that regime:

- coefficients may grow polynomially or even subexponentially;
- no spectral-radius estimate at the immediately preceding block is needed;
- auxiliary rows need not be copies of the prime block;
- a finite tensor system is allowed.

The only load-bearing requirement is genuine strict scale contraction.

## 7. Proof boundary

The composition theorem is complete. What remains arithmetic is to construct a
source-bound finite row system satisfying (T-15121.3) or (T-15121.11). That task
is specified in `L-15156/M-15112`.
