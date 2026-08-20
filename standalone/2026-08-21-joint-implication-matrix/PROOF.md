# A joint implication matrix for the quadratic and minimal-wavelet routes

## Abstract

Two recent RH programs appear to terminate in different hard estimates: a
critical quadratic activation deficit and a compact ordinary-Mobius wavelet
cross-core.  We prove that these are not independent terminal objects.  An
exact distributional identity makes them the continuous and atomic inputs of
one compact beta-wavelet.  We then prove a positive-operator absorption
principle in matrix form.  It allows two estimates, neither of which closes
alone, to close jointly whenever their Perron coupling is strictly
subcritical.  The arithmetic cross estimates needed to instantiate that
matrix remain open; RH is not proved.

## 1. Source and kernels

Let

\[
T(x)=(4\sqrt x-3)1_{x\ge1},\qquad
\beta=(\varepsilon-\delta_{67})*\mu.
\]

Define `h_beta`, `H_2`, `E_2`, the activation measure `A_beta`, the dilation
operators `S_a`,

\[
P_2=(I-\sqrt2S_2)(I-S_2)^2,
\]

and logarithmic integration `J` as in L-101101.

## 2. Distributional bridge

In logarithmic coordinate `u=log X`, the square of the SHARP kernel satisfies

\[
(D-1)T^2=\delta_0+3T.
\]

Convolution with the literal beta source gives

\[
(D-1)E_2=C_2\delta_0-\mathcal A_\beta-3h_\beta.
\]

Applying `JP_2` yields

\[
3G_\beta=C_2JP_2\delta_0-JP_2\mathcal A_\beta-JP_2(D-1)E_2.
\]

The calibration is compact.  Every activation atom and every source
coefficient is retained.

## 3. Why this is an AND gate

Set

\[
\mathcal A=-\tfrac13JP_2\mathcal A_\beta,
\quad
\mathcal Q=-\tfrac13JP_2(D-1)E_2,
\quad
\mathcal C=\tfrac{C_2}{3}JP_2\delta_0.
\]

Then `G_beta=C+A+Q`.  The quadratic lane is naturally adapted to `Q`; the
largest-prime/Vaughan lane is naturally adapted to `A`.  Taking absolute
values before this split is composed destroys their signed compensation.

## 4. Matrix absorption

Let positive operators `K_ij` obey L1 mass bounds `m_ij` and put

\[
g_i=f_i+\sum_jK_{ij}f_j.
\]

The identity `(f_j)_+=f_j+(f_j)_-` gives

\[
 n\le r+b+Mn,
\]

where `n` and `r` are negative-mass vectors and `b` is the signed flux vector.
If `rho(M)<1`, then

\[
 n\le(I-M)^{-1}(r+b).
\]

For two channels the exact condition is

\[
a<1,\quad d<1,\quad bc<(1-a)(1-d).
\]

No row is required to close by itself.

## 5. Conditional closure

Suppose the two bridge-channel negative masses satisfy

\[
\binom{Q(Y)}{A(Y)}
\le
\begin{pmatrix}a&b\\c&d\end{pmatrix}
\binom{Q(Y)}{A(Y)}+Y^{o(1)}\binom11
\]

with a fixed subcritical nonnegative matrix.  Matrix absorption gives
`Q(Y)+A(Y)=Y^{o(1)}`.  Since `C` is compact,

\[
\int_1^Y(G_\beta)_-\,dX/X=Y^{o(1)}.
\]

The Mellin transform is

\[
\frac{(1-67^{-(s+1/2)})(s+3/2)
(1-\sqrt2\,2^{-s})(1-2^{-s})^2}
{s^2(s-1/2)\zeta(s+1/2)}.
\]

All finite factors are nonzero at translated off-line zeros.  The frozen
negative-mass Landau theorem and the functional equation therefore imply RH.

## 6. Repository interpretation

Adaptive Euler squaring is the best current source for a strict quadratic
self-budget.  The zero-moment largest-prime/Vaughan analysis is the best
current source for the activation cross-budget.  Their exact constants have
not yet been proved on the common bridge channels.  This is the remaining
middle estimate.

## 7. Status

The distributional identity, matrix theorem, detector interface, and
conditional implication are proved.  The subcritical arithmetic coupling
matrix is open.  The Riemann Hypothesis remains unproved.
