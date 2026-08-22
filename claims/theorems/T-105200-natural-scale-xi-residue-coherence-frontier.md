# T-105200 — Natural-scale Xi residue coherence and the corrected low-order boundary

Claim ID: `T-105200`  
Status: **MAJOR PROPOSED UNCONDITIONAL HIGH-TAIL ADVANCE; LOW-ORDER LEVINSON GATE OPEN**  
Created: 2026-08-23  
Updated: 2026-08-23  
Base: PR #723 live checkpoint `fd3ef43a6964e502f00ad906482eae5b3c544fba`  
Depends on: `L-105200--L-105208`; `R-105200--R-105201`; `T-105210`; PRs #716, #720, #723  
RH status: **unproved**

## 1. Proposed unconditional high-derivative theorem

For every fixed `C,H>0`, put

\[
T_M=C\sqrt{M\over\log M}.
\]

The positive Xi Fourier saddle has a uniform complex Gaussian limit on the
complete natural box. Consequently, for all sufficiently large `M`:

1. every zero of every `Xi^(m)`, `m>=M`, in
   `|Re z|<=T_M`, `|Im z|<=H` is real and simple;
2. the zero count is
   \[
   N_m(T_M)={2w_mT_M\over\pi}+O_C(1);
   \]
3. every derivative-ratio residue at a real zero of `Xi^(m+1)` in a buffered
   inner box satisfies
   \[
   {\Xi^{(m)}(c)\over\Xi^{(m+2)}(c)}
   =-w_m^{-2}(1+o(1));
   \]
4. the associated residue coherence is `1-o(1)`, uniformly over `m>=M`.

Thus `RCMV104530` holds with asymptotically optimal margin throughout the
complete high derivative tail. Equivalently, a rectangle of original height
`T` is cleared by derivative orders of the natural size

\[
\boxed{m\asymp T^2\log T.}
\]

These analytic statements are proposed complete mathematics pending
independent review; the exact replay does not machine-prove them.

## 2. Exact first and second contour fluxes

PR #723 supplies the exact second-moment window flux

\[
B_{2,F}
={1\over2\pi i}
\int_{\partial\Omega}{F(z)^2\over F'(z)F''(z)}\,dz.
\]

`L-105204` supplies its first-moment companion

\[
B_{1,F}
={1\over2\pi i}
\int_{\partial\Omega}{F(z)\over F'(z)}\,dz.
\]

Together they give the exact finite-window coherence formula

\[
\mathfrak C_F
=
{(-B_{1,F}+C_{1,F})_+^2
\over
R_F(B_{2,F}-C_{2,F}-D_F)},
\tag{T-105200.1}
\]

where the two `C` terms are the nonreal critical corrections and `D_F` is the
adjacent-derivative residue debt.

For `F=Xi^(m)` in the natural high derivative tail, `L-105205` proposes

\[
C_{1,F}=C_{2,F}=0,
\qquad
D_F=o(R_F/w_m^4),
\]

and

\[
\boxed{
B_{1,F}=-{R_F\over w_m^2}(1+o(1)),
\qquad
B_{2,F}={R_F\over w_m^4}(1+o(1)).
}
\tag{T-105200.2}
\]

Thus the high-tail residue theorem is also an asymptotic evaluation of the
exact oriented window fluxes.

## 3. Binding correction to the cumulative budget

The earlier version promoted

\[
\mathcal D_r
=O_r
+2\sum_{j<r}R_j(1-\mathfrak C_j)
+\sum_{j<r}(B_j+W_j-1)
\]

as the next low-order producer.  `R-105201` proves the exact identity

\[
\boxed{
\mathcal D_r
=O_0+2\sum_{j<r}
\left[R_j(1-\mathfrak C_j)-E_j\right].
}
\tag{T-105200.3}
\]

It is the desired off-real zero count plus nonnegative coherence slack.
Therefore `CRDB105200<2` remains a correct sufficient condition, but the
ledger itself does not estimate the actual low-order descent.  The natural
high-tail theorem removes `O_r`; it does not control the fixed low-order
horizontal argument.

## 4. Corrected low-order frontier

`L-105206` proves that all adjacent derivative-level horizontal arguments and
top charges telescope to one endpoint quotient

\[
{\xi+\lambda\xi'
 \over
 \xi^{(r)}+\lambda\xi^{(r+1)}}.
\tag{T-105200.4}
\]

Thus the boundary obstruction is one classical Levinson auxiliary numerator
relative to one high derivative denominator.

The new unconditional fixed-order input is:

1. `L-105207`: all Xi Laguerre defects form one all-order
   exterior-square Fourier Gram
   \[
   [\Lambda_{a_i+a_j}(t_j-t_i)]\succeq0;
   \]
2. `L-105208`: every low-order companion has strict line-averaged
   Hermite--Biehler dominance and an exact positive amplitude-weighted phase
   sum rule.

These theorems prove that the low-order source orientation is correct before
height localization.  They do not control the continued argument at one fixed
ordinate.

The revised conclusion-facing theorem is `HLOC105210` of `T-105210`: upgrade
the exact translation-invariant/averaged Fourier positivity to the same-height
horizontal argument at the last defective level.  Together with exclusion of
a positive-residue last event, the exact `L-104518--L-104521` last-defect
transport would imply RH.

## 5. Exact boundary

```text
natural-scale complex Gaussian saddle          PROPOSED COMPLETE
half-infinite derivative-tail real-rooting     PROPOSED COMPLETE
natural order T^2 log T high entry              PROPOSED COMPLETE
high-tail residue coherence -> 1                PROPOSED COMPLETE
exact first and second window fluxes            PROVED EXACT
high-tail two-flux asymptotics                  PROPOSED COMPLETE
CRDB as independent low-order producer          REFUTED
all derivative arguments -> one endpoint ratio PROVED EXACT
all-order exterior-square Xi Gram               PROVED UNCONDITIONALLY
mean low-order HB orientation                   PROVED UNCONDITIONALLY
HLOC105210 fixed-height localization            OPEN / RH-BEARING
last positive-residue exclusion                 OPEN / RH-BEARING
Riemann Hypothesis                              UNPROVED
```

This draft remains the dedicated continuation workspace for the actual
low-order Levinson attack.
