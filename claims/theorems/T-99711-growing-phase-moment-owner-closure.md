# T-99711 — Growing phase-moment owner closure

Claim ID: `T-99711`  
Status: **CONCLUSION-COMPLETE REDUCTION; OFF-DIAGONAL OWNER PACKING OPEN**  
Created: 2026-08-20  
Depends on: `L-99710`--`L-99714`; PR #653 negative-mass Landau theorem  
RH status: **unproved**

For a dyadic block

\[
2^L\le x<2^{L+1},
\]

let `M_L` be (L-99714.5), let `Phi_(M_L)` be the growing zero-moment compact
kernel, and put

\[
\mathscr W_{x,L}(w)
=
\sum_n{\beta(n)\over\sqrt n}
 \Phi_{M_L}(x/n)n^{-w}.
\tag{T-99711.1}
\]

Choose

\[
\tau_x=(\log\log x)^{-1}
\]

and define

\[
\boxed{
\mathscr Q_L(x)
=
\int_{\mathbb R}P_{\tau_x}(\gamma)
 |\mathscr W_{x,L}(-\tau_x+i\gamma)|^2d\gamma.
}
\tag{T-99711.2}
\]

Poisson point evaluation gives

\[
|(I-S)^{M_L}W(x)|\le\mathscr Q_L(x)^{1/2}.
\tag{T-99711.3}
\]

## 1. The diagonal is already subpower

The kernel bound and support from `L-99714` give

\[
|\Phi_{M_L}(y)|\le 2^{M_L}\|\Phi\|_\infty,
\qquad
1\le y\le2^{M_L+3}.
\]

Since `|beta(n)|<=2`,

\[
\begin{aligned}
\mathscr D_L(x)
&:=
\sum_n{\beta(n)^2\over n}
 |\Phi_{M_L}(x/n)|^2 n^{2\tau_x}\\
&\ll
x^{2\tau_x}4^{M_L}
\sum_{x/2^{M_L+3}<n\le x}{1\over n}\\
&\ll
x^{2\tau_x}4^{M_L}(M_L+1)
=x^{o(1)}.
\end{aligned}
\tag{T-99711.4}

Thus no diagonal or same-source power loss remains.  The entire open estimate is
the phase-sensitive off-diagonal owner correlation.

## 2. Single remaining theorem

> **Growing Phase-Moment Owner Carleson estimate (`GPMOC99710`).** Uniformly
> over dyadic blocks,
> \[
> \int_{2^L}^{2^{L+1}}
> \mathscr Q_L(x)^{1/2}{dx\over x}
> =2^{o(L)}.
> \tag{T-99711.5}
> \]

If (T-99711.5) holds, then (T-99711.3) gives subpower logarithmic negative mass
for `(I-S)^(M_L)W` on each block.  The positive inverse in `L-99714` has mass
`2^(o(L))`, so `W` itself has subpower logarithmic negative mass.  `L-99713`
then supplies the zero-safe Mellin transform, and the negative-part Landau
theorem gives RH.

Hence

\[
\boxed{\mathrm{GPMOC99710}\Longrightarrow\mathrm{RH}.}
\tag{T-99711.6}
\]

## 3. Why this is strictly smaller than prior frontiers

The surviving packet has all of the following simultaneously:

```text
fixed compact ratio after base filtering;
subpower ratio width after growing moments;
M_L exact logarithmic moments equal to zero;
subpower forward and inverse filter masses;
adaptive Poisson phase gap at every native owner edge;
subpower left-strip inflation;
subpower coefficient diagonal;
exact native beta coefficients and duplicated-67 owners.
```

PR #580's generic balanced Type-II form did not have the owner spectral gap.
PR #655's owner Gram did not remove the power-sized SHARP tail or low-frequency
kernel modes.  The present synthesis removes both deficiencies before the
cross terms are estimated.

## 4. Hostile boundary

The theorem does not follow from a source-blind large sieve: frequencies
`log n` may be separated by `O(1/x)` inside the compact annulus.  It must use
the exact owner disintegration, or an equivalent multiplicative tent packing,
before summing the source labels.

```text
compact zero-safe conclusion packet          PROVED
blockwise growing safe moment tower           PROVED
subpower inverse and support width             PROVED
adaptive phase-owner spectral gap              PROVED
diagonal contribution                          SUBPOWER / PROVED
GPMOC99710 off-diagonal owner packing           OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVEN
```