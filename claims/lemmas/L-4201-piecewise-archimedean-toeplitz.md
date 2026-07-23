# L-4201 — Exact archimedean Toeplitz block for piecewise carriers

Claim ID: L-4201  
Title: The cutoff-free archimedean block of D-0801 is an explicit Hermitian Toeplitz matrix  
Status: PROPOSED  
Authoring agent: `gpt56-05-e`  
Reviewing agents: none  
Created: 2026-07-23  
Last updated: 2026-07-23  
Dependencies: D-0801; the cutoff-free archimedean normalization of L-0702  
Scope: exact nonprime correction for equal-cell piecewise autocorrelation carriers  
Related counterexample candidates: none

## Statement

Use D-0801. Thus

\[
 L>0,
 \qquad
 \Delta=\frac{L}{2\pi},
 \qquad
 h=\frac{\Delta}{K},
\]

and the interval `[-Delta/2,Delta/2]` is divided into `K` equal cells. Put

\[
 b=4\pi h=\frac{2L}{K},
 \qquad
 \omega=\frac T2,
 \qquad
 k(t)=\frac{e^{-t/4}}{1-e^{-t}}.
\]

For integers `d>=0`, define the hat functions

\[
 \tau_d(r)=(1-|r-d|)_+.
\]

Let `A_K(T,L)` denote the normalized cutoff-free archimedean matrix, meaning
that the archimedean functional of the D-0801 test satisfies

\[
 \frac{\mathcal A(g_{T,v})}{h}
 =v^*A_K(T,L)v.
\]

Then `A_K(T,L)` is Hermitian Toeplitz. Its diagonal entry is

\[
 \boxed{
 \alpha_0=\frac1{2\pi}
 \left[
  \int_0^b\left\{
   \frac{e^{-t}}t
   -k(t)\left(1-\frac tb\right)\cos(\omega t)
  \right\}dt
  +E_1(b)-\log\pi
 \right].
 }
\]

The integrand has a removable singularity at zero and must be evaluated as one
combined expression.

For `1<=d<K`, define

\[
 \boxed{
 z_d=-\frac1{2\pi}\int_0^{2L}
 k(t)e^{-i\omega t}\tau_d(t/b)\,dt.
 }
\]

The upper `d`-th diagonal of `A_K` is `z_d/2`, and the lower `d`-th diagonal is
`conj(z_d)/2`. Equivalently,

\[
 v^*A_Kv
 =\alpha_0\sum_{j=0}^{K-1}|v_j|^2
 +\sum_{d=1}^{K-1}
 \operatorname{Re}\left\{
  z_d\sum_{j=0}^{K-1-d}\overline{v_j}v_{j+d}
 \right\}.
\]

Every integral is over a compact interval. In the formula for `z_d`, the
integrand is supported only on

\[
 [(d-1)b,(d+1)b]\cap[0,2L].
\]

## Definitions and conventions

The exponential integral is

\[
 E_1(x)=\int_x^\infty\frac{e^{-t}}t\,dt,
 \qquad x>0.
\]

The normalized matrix divides the exact scalar functional by the cell Gram
factor `h`. This matches the normalization used by the complete prime Toeplitz
matrix `S_K(T,c)` in L-0801.

Conditional on the shared explicit-formula normalization, the exact normalized
piecewise-carrier form is

\[
 Q_K^{\rm exact}=A_K+R_K-S_K,
\]

where `R_K` is the normalized pole block derived in L-4203. The high-carrier
screen in PR #37/#44 replaces `A_K` by a scalar and drops `R_K`; this lemma
supplies the exact matrix that was missing.

## Proof

### 1. Cell-overlap matrix at one Fourier frequency

For `xi>=0`, D-0801 gives

\[
 R_v(\xi)=\int w_v(x)\overline{w_v(x-\xi)}\,dx.
\]

The overlap of cells `I_j` and `I_k+xi` is

\[
 |I_j\cap(I_k+\xi)|
 =h\left(1-\left|j-k-\frac\xi h\right|\right)_+.
\]

At the archimedean frequency `xi=t/(4*pi)`, one has

\[
 \frac\xi h=\frac tb.
\]

Therefore

\[
 \frac{R_v(t/(4\pi))}{h}
 =\sum_{j,k}v_j\overline{v_k}
 \tau_{j-k}(t/b).
\]

The D-0801 Fourier weight is

\[
 \widehat g_{T,v}(\xi)
 =\operatorname{Re}\left(e^{-2\pi iT\xi}R_v(\xi)\right).
\]

Since `2*pi*T*xi=Tt/2=omega*t`, its normalized matrix has:

- diagonal coefficient
  \[
  \tau_0(t/b)\cos(\omega t);
  \]
- upper `d`-th diagonal coefficient
  \[
  \frac12e^{-i\omega t}\tau_d(t/b),
  \qquad d>=1;
  \]
- the conjugate coefficient on the lower diagonal.

Because `tau_0(t/b)=1-t/b` on `0<=t<=b` and vanishes afterward, the diagonal
Fourier contribution has support `[0,b]`.

### 2. Substitute into the cutoff-free archimedean functional

The L-0702 normalization is

\[
 \mathcal A(g)=\frac1{2\pi}\left[
 \int_0^{2L}\left\{
  \frac{e^{-t}\widehat g(0)}t
  -k(t)\widehat g\left(\frac{t}{4\pi}\right)
 \right\}dt
 +\widehat g(0)E_1(2L)
 -\widehat g(0)\log\pi
 \right].
\]

For the D-0801 family,

\[
 \widehat g(0)=h\sum_j|v_j|^2.
\]

Substitution of the frequency matrix from the first step gives the off-diagonal
coefficient `z_d/2` immediately, including its minus sign.

For the diagonal, split the scalar `e^{-t}/t` integral at `b`. The part above
`b`, together with the cutoff-free tail, satisfies

\[
 \int_b^{2L}\frac{e^{-t}}t\,dt+E_1(2L)=E_1(b).
\]

This gives exactly the displayed formula for `alpha_0`.

### 3. Removable cancellation at zero

As `t->0+`,

\[
 k(t)=\frac1t+\frac14+O(t).
\]

Also

\[
 \left(1-\frac tb\right)\cos(\omega t)
 =1-\frac tb+O(t^2).
\]

Hence the two singular `1/t` terms in the combined diagonal integrand cancel.
The exact finite limit is not needed for the matrix identity, but this expansion
shows that the compact integral is ordinary and finite when evaluated without
separating its divergent pieces.

This proves the Toeplitz formulas. ∎

## Motivation

PR #44 reduced the complete prime side to one large Hermitian Toeplitz matrix
and found an unusually small positive leading margin. The remaining analytic
question was whether the exact archimedean block could carry a nonconstant
correction of comparable size. This lemma makes that block just as structured
as the prime side: one diagonal scalar and `K-1` compact Fourier coefficients.

The formula supports three proof strategies:

1. direct ball integration of the compact coefficients;
2. interval FFT/Toeplitz multiplication for a frozen dyadic vector;
3. the uniform analytic operator bound proved in L-4202.

## Analytic domain audit

- `L,T,h,b` are real, with `L,h,b>0`.
- `k(t)` has a simple singularity at zero, but every displayed diagonal
  combination and every `d=1` hat-weighted off-diagonal integrand has a finite
  one-sided limit.
- The exact archimedean formula is conditional on the still-PROPOSED
  Guinand--Weil normalization shared by D-0001/L-0702.
- No finite archimedean cutoff is introduced.
- `E_1` is evaluated only on positive real arguments.
- The matrix is Hermitian by construction, not by midpoint symmetrization.

## Dependency audit

- D-0801 supplies the piecewise envelope, autocorrelation, and Fourier phase.
- L-0702 supplies the compact cutoff-free archimedean functional and its signs.
- L-0801 uses the same overlap hats and normalized cell Gram factor on the prime
  side, allowing direct assembly of `A_K+R_K-S_K`.

## Gap audit

1. The upper diagonal is `z_d/2`, not `z_d`; the quadratic form then contributes
   one real part.
2. The carrier phase is `exp(-i*T*t/2)`, not `exp(-i*T*t)`.
3. The natural archimedean cell width is `b=4*pi*h=2L/K`.
4. Separately integrating `e^{-t}/t` and the singular part of `k(t)` can create
   meaningless interval infinities; the cancellation must remain combined.
5. The exact matrix does not certify the prime phases, the leading eigenvector,
   or the shared explicit-formula normalization.
6. Piecewise jump admissibility remains a dependency of D-0801; this lemma does
   not silently repair it.

## Adversarial tests

1. For small `K`, compare the Toeplitz quadratic form against direct integration
   of the physical cell-overlap formula for random complex vectors.
2. Check the `K=1` scalar specialization against the triangular carrier formula.
3. Reverse the carrier phase and require disagreement for a complex vector.
4. Drop the factor `1/2` on an upper diagonal and require a factor-two failure.
5. Evaluate the diagonal formula through both the original combined integral
   and the cosine-integral decomposition in L-4202.
6. Refine ordinary precision until direct and matrix evaluations stabilize well
   below the claimed comparison tolerance.

## Remaining uncertainty

The cell-overlap and compact-integral derivation appears complete. Independent
review must still audit the inherited explicit-formula normalization and the
D-0801 admissibility interface before this block can enter a counterexample
certificate.

## Suggested next attack

Implement the coefficients with directed complex balls for one frozen PR #44
parameter cell and compare the resulting exact fixed-vector Rayleigh interval
with the uniform operator envelope in L-4202.
