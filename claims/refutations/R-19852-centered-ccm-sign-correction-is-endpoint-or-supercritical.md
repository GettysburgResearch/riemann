# R-19852 — Centered CCM sign correction is either endpoint anchored or supercritical in degree

Claim ID: `R-19852`  
Status: **PROVED EXACT PHASE FIREWALL + ASYMPTOTIC BANDWIDTH FIREWALL**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-12  
Dependencies: centered/unshifted Fourier phase adapter; `L-19872`; the zero count `N(T)=O(T log T)`; the energy argument of `R-19851`  
Scope: closes the direct scalar sign-Darboux escape from the non-ground CCM counterexample  
Nonclaim: matrix-valued and anisotropic symmetrizer mechanisms remain open

## 1. Centered phase

Let

\[
 I_L=[-L/2,L/2],
 \qquad
 d_k={2\pi k\over L},
 \qquad -N\le k\le N,
 \qquad H={2\pi N\over L}.
 \tag{R-19852.1}
\]

Let `f` be a real centered source and put

\[
 a_k=\widehat f(d_k).
 \tag{R-19852.2}
\]

After translating `I_L` to `[0,L]`, the exact CCM coefficient vector is

\[
 \boxed{\xi_k=(-1)^ka_k.}
 \tag{R-19852.3}
\]

The factor `(-1)^k` is load bearing.  In particular, making all raw samples
`a_k` positive makes the CCM vector alternate; it does not place it in the
positive cone of `L-19871`.

## 2. Minimal polynomial correction

Assume no selected sample is zero.  Let `Z_H` be the number of intervals
`(d_k,d_(k+1))` in which the raw samples change sign.  The rephased samples
`xi_k` change sign in every other interval, namely in exactly

\[
 2N-Z_H
 \tag{R-19852.4}
\]

of the `2N` adjacent gaps.

Indeed,

\[
 \operatorname{sgn}(\xi_k\xi_{k+1})
 =-\operatorname{sgn}(a_ka_{k+1}).
 \tag{R-19852.5}
\]

By the minimality theorem `L-19872`, every real polynomial `M` satisfying

\[
 M(d_k)\xi_k>0
 \tag{R-19852.6}
\]

for all selected modes has degree at least

\[
 \boxed{\deg M\ge2N-Z_H.}
 \tag{R-19852.7}
\]

If `a_k` are samples of `Xi` or of a real-zero-divided Xi quotient, the number
of raw sign-changing gaps is at most the number of odd real zeros in `[-H,H]`,
and hence

\[
 Z_H=O(H\log H).
 \tag{R-19852.8}
\]

Therefore, on every moving-Hardy schedule with

\[
 L/\log H\longrightarrow\infty,
 \tag{R-19852.9}
\]

one has

\[
 \boxed{
 \deg M
 \ge {HL\over\pi}-O(H\log H)
 =(1-o(1)){HL\over\pi}.}
 \tag{R-19852.10}
\]

Thus the exact centered phase costs essentially one real root per Fourier
lattice gap.

## 3. Supercritical energy

Choose the minimal corrector, with every root in its forced lattice gap.  All
its roots lie in `[-H,H]`; write `d=deg M`.  Under (R-19852.9),

\[
 {d\over H}\longrightarrow\infty.
 \tag{R-19852.11}
\]

The proof of `R-19851` applies verbatim, with `d` in place of `d_H`: for the
multiplied Xi target

\[
 F_M(t)=M(t)\Xi(t),
 \]

\[
 {\int_d^{2d}|F_M(t)|^2dt
  \over\int_{|t|\le H}|F_M(t)|^2dt}
 \ge
 c\,d^{9/2}\log d
 \exp\!\left[
  2d\log{d\over4H}-\pi d
 \right]
 \longrightarrow\infty.
 \tag{R-19852.12}
\]

Hence the polynomial which corrects the centered CCM phase moves the target
far beyond the very cutoff on which positivity was imposed.  This is stronger
than the raw-sign inflation in `R-19851`.

## 4. The unique zero-free phase correction

A zero-free exponential can pay the alternating phase without polynomial
roots.  If

\[
 E_c(z)=e^{icz}
 \]

satisfies

\[
 E_c(d_k)=(-1)^k
 \tag{R-19852.13}
\]

for every integer `k`, then

\[
 {2\pi c\over L}\equiv\pi\pmod{2\pi},
 \]

so

\[
 \boxed{c\equiv L/2\pmod L.}
 \tag{R-19852.14}
\]

Thus the minimal zero-free correction is exactly a half-interval translation.

## 5. Endpoint anchoring has a fixed loss

Let `r` be a nonzero even source in `L2(R)`.  Translating its transform by the
phase `e^{izL/2}` moves the physical source from the center of `[0,L]` to one
endpoint.  The zero extension retained on `[0,L]` is then `r 1_[0,L]` up to
orientation.  Since `r` is even,

\[
 \|r\mathbf1_{(-\infty,0)}\|_2^2
 ={1\over2}\|r\|_2^2.
 \tag{R-19852.15}
\]

As `L->infinity`, the positive tail beyond `L` vanishes, but the negative
half-line does not.  Therefore

\[
 \boxed{
 \liminf_{L\to\infty}
 \|r-r\mathbf1_{[0,L]}\|_2
 \ge {1\over\sqrt2}\|r\|_2>0.}
 \tag{R-19852.16}
\]

The same lower bound holds in every Hardy norm dominating ordinary `L2`.
Thus the zero-free phase correction destroys centered target convergence by
placing half of the source outside the interval.

## 6. Dichotomy

For a scalar sign-groundification of a centered Xi-like target on the complete
Fourier lattice, the two direct mechanisms are:

```text
real-rooted polynomial correction
  -> degree asymptotic to H L / pi
  -> multiplied target escapes the cutoff;

zero-free exponential correction
  -> half-interval translation
  -> fixed endpoint truncation loss.
```

Neither mechanism supplies the moving-Hardy relative approximation needed to
recover `Xi`.

This explains why the exact finite construction `L-19871/L-19872` does not
complete obligation 2 when combined with the centered target rate `L-19868`.

## 7. Proof boundary

- The centered phase identity, degree lower bound and endpoint loss are exact.
- The energy inflation uses the same standard zeta inputs as `R-19851`.
- The theorem does not exclude matrix-valued Darboux colligations, nonuniform
  node systems with a new completeness theorem, or the source-bound anisotropic
  symmetrizer of `L-19869`.
- No RH conclusion is claimed.
