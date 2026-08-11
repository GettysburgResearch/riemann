# T-91201 — The factor-four renewal energy is exactly a one-vector innerness test

Claim ID: `T-91201`  
Status: **PROPOSED COMPLETE EXACT REDUCTION; HARD RANGE REMAINS RH-BEARING**  
Created: 2026-08-12  
RH status: **unproved**

## 1. Suzuki kernel and the target energy

For `omega>0`, let `h_omega` be the inverse-Mellin kernel characterized in a
right half-plane by

\[
 \int_1^\infty h_\omega(x)x^{-s}\,dx
 =\frac{\xi(s-\omega)}{\xi(s+\omega)}.
 \tag{T-91201.1}
\]

Put

\[
 A_\omega(x)=\int_1^x h_\omega(y)\,dy,
 \qquad
 f_\omega(t)=e^{-t/2}A_\omega(e^t)\mathbf1_{t\ge0},
 \tag{T-91201.2}
\]

and

\[
 \Theta_\omega(z)
 =\frac{\xi(\frac12-\omega-iz)}
        {\xi(\frac12+\omega-iz)}.
 \tag{T-91201.3}
\]

The factor-four renewal energy is

\[
 \mathcal I_\omega
 =\int_4^\infty
 \left|2\int_{x/2}^{x}h_\omega(y)dy
       -\int_{x/4}^{x/2}h_\omega(y)dy\right|^2
 \frac{dx}{x^2}.
 \tag{T-91201.4}
\]

## 2. Exact Hardy transform

Let `s=1/2-iz`.  For `Im z` sufficiently large, integration by parts in
(T-91201.1) gives

\[
\begin{aligned}
 \widehat f_\omega(z)
 &=\int_0^\infty f_\omega(t)e^{izt}dt\\
 &=\int_1^\infty A_\omega(x)x^{-s-1}dx\\
 &=\frac1s\int_1^\infty h_\omega(x)x^{-s}dx\\
 &=\boxed{\frac{\Theta_\omega(z)}{\frac12-iz}}.
\end{aligned}
 \tag{T-91201.5}
\]

Thus the target is the causal inverse transform of one fixed outer Hardy vector
multiplied by `Theta_omega`.

## 3. Exact factor-four filter

Let `ell=log 2` and define on `L^2(R)`

\[
 (Sf)(t)=2^{-1/2}f(t-\ell).
 \tag{T-91201.6}
\]

Then `||S||=2^{-1/2}`.  Put

\[
 H(y)=(1-y)(2-y)=2-3y+y^2.
 \tag{T-91201.7}
\]

For `x=e^t` and `t>=2ell`,

\[
\begin{aligned}
 H(S)f_\omega(t)
 &=e^{-t/2}\bigl[2A_\omega(x)-3A_\omega(x/2)+A_\omega(x/4)\bigr]\\
 &=e^{-t/2}\left[
 2\int_{x/2}^{x}h_\omega(y)dy
 -\int_{x/4}^{x/2}h_\omega(y)dy
 \right].
\end{aligned}
 \tag{T-91201.8}
\]

Consequently

\[
 \boxed{
 \mathcal I_\omega
 =\int_{2\ell}^{\infty}|H(S)f_\omega(t)|^2dt.
 }
 \tag{T-91201.9}
\]

Both factors of `H(S)` are boundedly invertible:

\[
 (I-S)^{-1}=\sum_{k\ge0}S^k,
 \qquad
 (2I-S)^{-1}=\frac12\sum_{k\ge0}(S/2)^k.
 \tag{T-91201.10}
\]

Hence

\[
 \|H(S)^{-1}\|
 \le\frac1{(1-2^{-1/2})(2-2^{-1/2})}.
 \tag{T-91201.11}
\]

Since `f_omega` is locally square integrable, (T-91201.9)--(T-91201.11) imply

\[
 \boxed{
 \mathcal I_\omega<\infty
 \iff f_\omega\in L^2(0,\infty).
 }
 \tag{T-91201.12}
\]

## 4. One outer vector detects innerness

The function

\[
 r(z)=\frac1{\frac12-iz}
\]

is outer in `H^2(C_+)`.  Also `|Theta_omega(x)|=1` on the real boundary.
Equation (T-91201.5) and Paley--Wiener therefore give

\[
\boxed{
 f_\omega\in L^2(0,\infty)
 \iff \Theta_\omega\text{ is a meromorphic inner function in }\mathbb C_+.
}
 \tag{T-91201.13}
\]

Indeed, innerness implies `Theta_omega r in H^2`.  Conversely, if the left side
holds, `Theta_omega r` has an `H^2` continuation from the safe half-plane. Since
`r` is outer, `Theta_omega=(Theta_omega r)/r` belongs to the Smirnov class; its
boundary modulus is one, so the Smirnov maximum theorem makes it inner.

Combining (T-91201.12) and (T-91201.13),

\[
\boxed{
 \mathcal I_\omega<\infty
 \iff \Theta_\omega\text{ is meromorphic inner in }\mathbb C_+.
}
 \tag{T-91201.14}
\]

This is the exact status of the requested integral.

## 5. Quantitative inner-case bound

If `Theta_omega` is inner, multiplication by it is isometric on `H^2`.  Let

\[
 g(t)=e^{-t/2}\mathbf1_{t\ge0},
 \qquad \widehat g(z)=r(z).
\]

Since Fourier multiplication commutes with the scalar filter `H(S)`,

\[
 \|H(S)f_\omega\|_2=\|H(S)g\|_2.
\]

But

\[
 H(S)g(t)=
 \begin{cases}
 2e^{-t/2},&0\le t<\ell,\\
 -e^{-t/2},&\ell\le t<2\ell,\\
 0,&t\ge2\ell.
 \end{cases}
\]

Therefore

\[
 \boxed{
 \|H(S)f_\omega\|_2^2
 =4(1-e^{-\ell})+(e^{-\ell}-e^{-2\ell})
 =\frac94.
 }
 \tag{T-91201.15}
\]

In particular,

\[
 \boxed{0\le\mathcal I_\omega\le\frac94.}
 \tag{T-91201.16}
\]

The unfiltered primitive energy is likewise exactly

\[
 \int_1^\infty |A_\omega(x)|^2\frac{dx}{x^2}=1.
 \tag{T-91201.17}
\]

## 6. Unconditional and RH-bearing ranges

The classical Lagarias--Suzuki inequality makes `Theta_omega` inner
unconditionally for

\[
 \omega\ge\frac12.
\]

Hence (T-91201.16) proves the requested integral unconditionally in this range.
Under RH the same innerness holds for every `omega>0`, so (T-91201.16) proves the
integral for every positive `omega` conditional on RH.

For `0<omega<1/2`, an unconditional proof of (T-91201.4) is not a soft renewal
estimate: by (T-91201.14) it is exactly an innerness/zero-free assertion.  If the
denominator of `Theta_omega` has an uncancelled zero in `C_+`, the safe inverse
contains an exponentially growing residue.  The filter `H(S)` cannot kill it,
because its spectral value has modulus `<2^{-1/2}` whereas the roots of `H` are
`1` and `2`; therefore `I_omega=infinity`.

For any predetermined sequence `omega_j downarrow 0`, finiteness for every `j`
forces RH: an off-line zero has only finitely many same-ordinate horizontal
companions, so for all sufficiently small `omega_j` its denominator pole cannot
be cancelled by a zero shifted exactly by `2omega_j`.

## 7. Boundary

```text
Mellin-to-Hardy transform                           EXACT
factor-four annularization                          EXACT
filter bounded invertibility                        EXACT
annular energy < infinity iff one-vector H2          PROPOSED COMPLETE
one-vector H2 iff Theta_omega inner                  PROPOSED COMPLETE
inner-case full filtered norm = 9/4                 EXACT
omega >= 1/2 integral finiteness                     UNCONDITIONAL / EXTERNAL INPUT
0 < omega < 1/2 integral finiteness                  OPEN / INNERNESS-BEARING
all omega_j -> 0                                     RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
