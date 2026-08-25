# T-105480 — F1 Hardy–Gram and signed near-collision frontier

Claim ID: `T-105480`

Status: **MAJOR UNCONDITIONAL HILBERT COMPRESSION; ONE SOURCE-SPECIFIC OFF-DIAGONAL ESTIMATE OPEN**

This theorem continues `T-105470` on durable PR #730 and freezes the latest
canonical Boolean/half-source lineages on PRs #719 and #751.

## 1. One optional square route to the terminal Hardy gate

Let

\[
\delta_m=\Delta_2W(m)=H_K(m+)/4.
\]

Define

```text
F1GRAM105480:
  sum_(M<=m<=2M) |delta_m|^2/m = M^(o(1))
  on every frozen dyadic source block.
```

`L-105480` proves

\[
\boxed{
\mathrm{F1GRAM}_{105480}
\Longrightarrow
\mathrm{F1HARDY}_{105470}.
}
\tag{T-105480.1}
\]

The continuous logarithmic L2 norm of the fixed derivative-outer current is
uniformly equivalent to this discrete square, because the current is affine in
`sqrt(X)` on every integer cell and the endpoint jump square is
`M^(-1+o(1))`.

## 2. Exact positive Gram and diagonal removal

The square is

\[
\mathcal E_M
=\sum_{n,r}a_n\overline{a_r}G_M(n,r),
\]

where

\[
G_M(n,r)
=\frac1{16}\sum_{m=M}^{2M}
\frac{K_L(m/n)K_L(m/r)}m.
\]

`G_M` is positive semidefinite and vanishes unless

\[
1/8<n/r<8.
\]

The diagonal is subpower.  Put

\[
\mathcal N_M
=\sum_{n\ne r}a_n\overline{a_r}G_M(n,r).
\]

Define

```text
F1HCNC105481:
  (N_M)_+ = M^(o(1)).
```

Then

\[
\boxed{
\mathrm{F1HCNC}_{105481}
\Longleftrightarrow
\mathrm{F1GRAM}_{105480}.
}
\tag{T-105480.2}
\]

The premise is signed and oriented.  Neither the absolute off-diagonal nor a
termwise-positive pair theorem is required.

## 3. Mellin/Nyman coordinate

With `k(u)=K_L(e^u)` and

\[
A(t)=\sum_na_nn^{-it},
\]

`L-105482` gives

\[
\boxed{
\int_0^\infty|H_K(X)|^2\frac{dX}{X}
=\frac1{2\pi}\int_{\mathbb R}
|\widehat k(t)|^2|A(t)|^2dt.
}
\tag{T-105480.3}
\]

This is the compact multiplicative Nyman norm of the canonical physical
source polynomial.  The kernel autocorrelation is supported on ratio-eight
near collisions.

## 4. Positive critical analytic-square coordinate

The current PR #719 head `e56c981e2d0639a988f8f54aa362724eb00d9131`
proves that the critical-weighted half-kernel has the strictly positive Fourier
factor `r_A(t)` and that the complete Boolean current has analytic-square
amplitude

\[
\mathscr Q_U(t)
=\int_0^1(1-\theta)S_{U,\theta}(t)^2d\theta.
\]

`L-105483` combines that normalization with this checkpoint.  For one frozen
finite source packet,

\[
\boxed{
\mathrm{F1ASQ2}_{105483}:
\quad
M^{1/2}\int_{\mathbb R}
 |P(1/4+it)|^2r_A(t)^4|\mathscr Q_U(t)|^2dt=M^{o(1)}
}
\tag{T-105480.4}
\]

is equivalent to `F1GRAM105480` when the fixed finite collection of generated
output blocks is included, and is sufficient on any selected block.

Moreover

\[
|\mathscr Q_U(t)|^2
\le\frac12\int_0^1(1-\theta)|S_{U,\theta}(t)|^4d\theta,
\]

so the corresponding Beta-weighted half-source fourth moment
`F1FOURTH105483` implies `F1ASQ2_105483`.  This is a legitimate stronger
source-specific route; it is not a replacement of the analytic square by a
modulus square in the sharp `L1` sign theorem.

## 5. The exact implication matrix

Combining this checkpoint with `T-105470` and the frozen source-safe consumer
chain gives

\[
\boxed{
\begin{aligned}
\mathrm{F1HCNC}_{105481}
&\Longleftrightarrow\mathrm{F1GRAM}_{105480}\\
&\Longrightarrow\mathrm{F1HARDY}_{105470}\\
&\Longleftrightarrow\mathrm{F1VAR}_{105460}\\
&\Longleftrightarrow\mathrm{REFSIG}_{106150}\\
&\Longleftrightarrow\mathrm{SFSC}_{106150}\\
&\Longrightarrow\mathrm{WKSFSC}_{106150}\\
&\Longrightarrow\mathrm{BCI}_{102990}\\
&\Longrightarrow\mathrm{RH}.
\end{aligned}}
\tag{T-105480.5}
\]

A second sufficient entry is

\[
\boxed{
\mathrm{F1FOURTH}_{105483}
\Longrightarrow
\mathrm{F1ASQ2}_{105483}
\Longleftrightarrow
\mathrm{F1GRAM}_{105480}.
}
\tag{T-105480.6}
\]

Only the identities and arrows before an explicitly open premise are proved.

## 6. Binding source-blind obstruction

`R-105480` constructs critical-size coefficients with unit source energy but
Gram energy at least `cM`.  Therefore the diagonal/source norm cannot control
physical restriction by any universal F1 Hodge, Schur, or Bessel inequality.

This dovetails with the latest frozen `L-106191`: after source-dual rescaling,
the `u=v=1` least-prime conductor family loses both conductor denominators.
The canonical equal-pair gauge preserves owner weights and removes artificial
star/cycle debt, but it does not make different physical products orthogonal.

A valid completion must exploit at least one of the exact signed structures
which survive physical collapse:

```text
the least-prime Calderón difference L-106132;
the connected Kummer–Möbius current T-106130;
the Wick-centered additive/Kummer conjunction T-106140;
the same-half-source reflection current T-106150;
or an equivalent source-specific near-collision theorem.
```

## Exact boundary

```text
Hardy l1 from weighted square                         PROVED EXACT
continuous/discrete square equivalence                PROVED
positive ratio-eight Gram                             PROVED EXACT
diagonal Gram                                         PROVED SUBPOWER
square = positive signed off-diagonal                 PROVED EXACT
Mellin–Plancherel/Nyman form                          PROVED EXACT
positive critical analytic-square weight              PROVED EXACT
half-source fourth moment -> F1 Gram                   PROVED EXACT
source-blind frame/Schur closure                      REFUTED LINEARLY

F1FOURTH105483 / F1ASQ2_105483                        OPEN / RH-BEARING
F1HCNC105481 / F1GRAM105480                           OPEN / RH-BEARING
F1HARDY105470 / F1VAR105460                           OPEN / RH-BEARING
BCI102990                                             OPEN / RH-BEARING
Riemann Hypothesis                                    UNPROVED
```

The surviving square route is now one explicit source-specific signed
near-collision estimate.  It is optional—the sharper L1 Hardy gate remains the
canonical endpoint—but it exposes exactly what any Hilbert/F1 completion must
prove and exactly why source-free positivity cannot prove it.
