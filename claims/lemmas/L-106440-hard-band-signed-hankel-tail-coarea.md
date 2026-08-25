# L-106440 — The signed Hankel complement has an exact hard-band spectral coarea

Claim ID: `L-106440`  
Status: **PROVED EXACT AT TRACE-CLASS HARDY SCOPE**  
Created: 2026-08-25  
Depends on: `L-105290`, `L-106431`  
RH status: **not assumed**

Work on the upper-half-plane Hardy space with the unitary Fourier transform

\[
\widehat f(\xi)=(2\pi)^{-1/2}\int_{\mathbb R}f(x)e^{-ix\xi}\,dx.
\]

Thus boundary values of `H^2(C_+)` correspond to `L^2(0,infinity)`.  Let `U`
be unimodular with `U-1 in dot H^(1/2)`, and write

\[
\mathfrak u(\xi)=(2\pi)^{-1/2}\widehat U(\xi)
\]

away from the harmless delta mass at zero.  Let `P_H` be the projection onto
positive frequencies `[0,H]` and put `Q_H=I-P_H` on `H^2`.

Define the signed high-frequency complement charge

\[
\boxed{
\Delta_H^{\rm out}(U)
 =\|H_UQ_H\|_{\mathcal S_2}^2
  -\|H_{\overline U}Q_H\|_{\mathcal S_2}^2.
}
\tag{L-106440.1}
\]

## 1. Exact coarea formula

After reflecting the negative output frequency to `x>0`, the Hankel kernels are

\[
K_U(x,y)=\mathfrak u(-x-y),
\qquad
K_{\overline U}(x,y)=\overline{\mathfrak u(x+y)}.
\]

Restricting the input to `y>H` and applying Tonelli gives

\[
\boxed{
\|H_UQ_H\|_{\mathcal S_2}^2
 =\int_H^\infty(\xi-H)|\mathfrak u(-\xi)|^2\,d\xi,
}
\tag{L-106440.2}
\]

\[
\boxed{
\|H_{\overline U}Q_H\|_{\mathcal S_2}^2
 =\int_H^\infty(\xi-H)|\mathfrak u(\xi)|^2\,d\xi.
}
\tag{L-106440.3}
\]

Hence

\[
\boxed{
\Delta_H^{\rm out}(U)
 =\int_H^\infty(\xi-H)
 \left(|\mathfrak u(-\xi)|^2-|\mathfrak u(\xi)|^2\right)d\xi.
}
\tag{L-106440.4}
\]

This is a scalar Fourier asymmetry, not an unspecified model-space trace.

Whenever the displayed integrals are locally absolutely continuous in `H`,

\[
\boxed{
{d\over dH}\Delta_H^{\rm out}
 =-\int_H^\infty
 \left(|\mathfrak u(-\xi)|^2-|\mathfrak u(\xi)|^2\right)d\xi,
}
\tag{L-106440.5}
\]

and for almost every `H`,

\[
\boxed{
{d^2\over dH^2}\Delta_H^{\rm out}
 =|\mathfrak u(-H)|^2-|\mathfrak u(H)|^2.
}
\tag{L-106440.6}
\]

The boundary data are

\[
\Delta_H^{\rm out}\longrightarrow0,
\qquad
(\Delta_H^{\rm out})'\longrightarrow0
\quad(H\to\infty),
\]

and the Fourier degree formula gives

\[
\boxed{
\Delta_0^{\rm out}(U)=-\operatorname{wind}U.
}
\tag{L-106440.7}
\]

Thus the complete adverse index is the zero-band value of a spectral tail
whose curvature is the literal positive-versus-negative Fourier imbalance.

## 2. Finite source frames split into an outer tail and an in-band hole

Let `P` be any finite-rank source projection satisfying `P<=P_H`, and put

\[
R_H=P_H-P.
\]

The orthogonal decomposition `P^perp=Q_H direct-sum R_H` and vanishing of the
off-diagonal trace blocks give

\[
\boxed{
\mathcal D_P(U)
 =\Delta_H^{\rm out}(U)+\Delta_{H,P}^{\rm hole}(U),
}
\tag{L-106440.8}
\]

where `mathcal D_P` is the signed complement of `L-106431` and

\[
\boxed{
\Delta_{H,P}^{\rm hole}(U)
 =\|H_UR_H\|_{\mathcal S_2}^2
  -\|H_{\overline U}R_H\|_{\mathcal S_2}^2.
}
\tag{L-106440.9}
\]

The two terms have different meanings:

```text
outer tail:       Fourier asymmetry above the declared physical bandwidth;
in-band hole:     signed charge of source directions omitted inside that band.
```

An absolute sampling theorem controls both terms separately and is stronger
than necessary.  The signed index requires only their sum.

## 3. Inner phases are automatically favorable

If `U` is inner in `C_+`, then `mathfrak u(-xi)=0` for `xi>0`.  Therefore

\[
\boxed{
\Delta_H^{\rm out}(U)
 =-\int_H^\infty(\xi-H)|\mathfrak u(\xi)|^2d\xi\le0.
}
\tag{L-106440.10}
\]

Moreover `H_U=0`, so (L-106440.9) is also nonpositive for every source frame.
This recovers the projection-independent sign theorem `L-105632` and shows it
frequency by frequency.

For block-diagonal all-pass symbols, all quantities in
(L-106440.1)--(L-106440.9) add exactly over the blocks.

## 4. Strip localization

Suppose `U-1` has boundary continuations at heights `+sigma` and `-sigma`
with the corresponding weighted half-derivative norms finite. Fourier
translation then gives

\[
\boxed{
\begin{aligned}
|\Delta_H^{\rm out}(U)|
\le e^{-2\sigma H}\Bigg[&
 \int_H^\infty(\xi-H)e^{2\sigma\xi}
       |\mathfrak u(-\xi)|^2d\xi\\
&+\int_H^\infty(\xi-H)e^{2\sigma\xi}
       |\mathfrak u(\xi)|^2d\xi
\Bigg].
\end{aligned}
}
\tag{L-106440.11}
\]

Consequently, after the Blaschke factors within distance `sigma` of the real
axis are extracted, the remaining analytic outer tail is exponentially small
at bandwidth `H`.  The only noncompact obstruction is the near-boundary
companion divisor plus the signed in-band hole.

## Scope

The lemma proves the exact spectral normal form and its analytic-strip
localization.  It does not estimate the endpoint-Xi Fourier asymmetry or the
in-band source hole.  Those two explicit quantities form the successor
frontier `T-106440`.