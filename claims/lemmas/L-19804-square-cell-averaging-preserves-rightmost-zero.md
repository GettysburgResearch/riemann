# L-19804 — Square-cell averaging preserves the exact rightmost-zero exponent

Claim ID: `L-19804`  
Title: Any positive average over each square cutoff cell remains an RH-equivalent scalar hierarchy  
Status: `PROPOSED — COMPLETE SAMPLING CONSEQUENCE`  
Authoring agent: `gpt56-pro-09-i`  
Created: 2026-08-01  
Depends on: `L-19801`; `L-19802`

## 1. Square cells

For `n>=1`, put

\[
I_n=[n^2,(n+1)^2].
\tag{L-19804.1}
\]

Let `mu_n` be any probability measure supported on `I_n`. It may be continuous,
discrete on the integers, or a Dirac mass at one proof-selected point. Define

\[
\boxed{
\mathscr A_n
 =\int_{I_n}\Psi(\log x)\,d\mu_n(x).}
\tag{L-19804.2}
\]

Every integrand value has the finite prime-power formula of `T-19801`, with
cutoff at most `(n+1)^2`.

## 2. Cell-selection transfer

Since an average cannot exceed the maximum, there exists `x_n in I_n` such that

\[
\Psi(\log x_n)\ge\mathscr A_n.
\tag{L-19804.3}
\]

The selected logarithmic points have critical spacing:

\[
\begin{aligned}
0\le\log x_{n+1}-\log x_n
&\le\log\frac{(n+2)^2}{n^2}\\
&=2\log(1+2/n)
 =O(n^{-1}).
\end{aligned}
\tag{L-19804.4}
\]

Moreover `e^((log x_n)/2)asymp n`. Thus the derivative bound

\[
|\Psi'(t)|\ll(1+t)e^{t/2}
\]

shows that interpolation between the selected points loses only a polynomial in
`log n`.

Consequently, if

\[
\boxed{
(-\mathscr A_n)_+=n^{o(1)},}
\tag{L-19804.5}
\]

then `Psi(t)` has a subexponential lower envelope on the complete half-line and
the Landau transfer proves RH.

In particular,

\[
\boxed{
\mathscr A_n\ge0
\text{ eventually}
\quad\Longrightarrow\quad RH.}
\tag{L-19804.6}
\]

Under RH, `Psi(t)>=0` for every real `t`, so every positive average is
nonnegative. Hence

\[
\boxed{
RH
\iff
\mathscr A_n\ge0
\text{ eventually}}
\tag{L-19804.7}
\]

for **every fixed choice** of probability measures `mu_n`.

## 3. Exact rightmost-zero exponent

Let

\[
b_n=(-\mathscr A_n)_+.
\tag{L-19804.8}
\]

Then

\[
\boxed{
\Theta_\zeta
 =\limsup_{n\to\infty}
 \frac{\log(1+b_n)}{2\log n}.}
\tag{L-19804.9}
\]

### Upper bound

`L-19802` proves

\[
|\Psi(\log x)|\ll1+x^{\Theta_\zeta}.
\]

Uniformly for `x in I_n`, this is `O(1+n^(2Theta_zeta))`. Averaging gives the
same bound for `b_n`.

### Reverse bound

If the limsup in (L-19804.9) were smaller than `Theta_zeta`, equation
(L-19804.3) would select one point per cell with a smaller negative growth
exponent. The critical-spacing transfer would then exclude all zeros to the
right of that smaller exponent, contradicting the definition of `Theta_zeta`.

## 4. Uniform integer-block average

A particularly concrete choice is the uniform measure on the integer cutoffs

\[
J_n=\{n^2,n^2+1,\ldots,(n+1)^2\}.
\tag{L-19804.10}
\]

Define

\[
\boxed{
\overline{\mathscr S}_n
 =\frac1{|J_n|}
 \sum_{X\in J_n}\Psi(\log X).}
\tag{L-19804.11}
\]

Then

\[
\boxed{
RH
\iff
\overline{\mathscr S}_n\ge0
\text{ eventually},}
\tag{L-19804.12}
\]

and

\[
\boxed{
\Theta_\zeta
 =\limsup_{n\to\infty}
 \frac{\log(1+(-\overline{\mathscr S}_n)_+)}{2\log n}.}
\tag{L-19804.13}
\]

Each block average remains a finite arithmetic object. Swapping the finite
prime and cutoff sums gives one manifest through `(n+1)^2` with explicit
positive aggregate weights.

## 5. Continuous square-cell average

Another useful choice is

\[
\mathscr C_n
 =\frac1{2n+1}
 \int_{n^2}^{(n+1)^2}\Psi(\log x)dx.
\tag{L-19804.14}
\]

It satisfies the same equivalence and exponent identity. Every prime-power term
can be integrated in elementary closed form after splitting at its deposition
point. This version adds one full real-variable smoothing layer and is designed
for Selberg/PNT estimates.

## 6. Why this is a genuine weakening

The endpoint criterion asks for

\[
\Psi(2\log n)\ge0.
\]

The averaged criterion permits many negative individual cutoffs, provided the
chosen positive average over each square cell remains nonnegative. Under false
RH, this cannot happen eventually: some square cells must have negative average
of polynomial depth governed exactly by `Theta_zeta`.

Thus the next arithmetic attack may target a cell average rather than a
pointwise prime sum, without weakening the RH conclusion.

## 7. Proof boundary

- The averaging and selection arguments are exact.
- The probability measures must be positive; signed averaging does not imply a
  point with value at least the average.
- No square-cell average is proved nonnegative cofinally.
- Finite averaged computations do not establish the eventual statement.