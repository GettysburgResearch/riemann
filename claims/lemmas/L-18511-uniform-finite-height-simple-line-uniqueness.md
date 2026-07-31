# L-18511 — One finite simple-zero height separates an entire finite packet

Claim ID: `L-18511`  
Title: Uniform Jensen bounds and the Pratt--Robles--Zaharescu--Zeindler simple-line proportion give an algorithmically terminating full-complement frame  
Status: `PROVED FINITE-DIMENSIONAL STRENGTHENING OF L-18507`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: Paley--Wiener; Jensen's formula; Pratt--Robles--Zaharescu--Zeindler  
Scope: citation and finite-height strengthening of `L-18507`  
Related candidates: none

## 1. Correct zero-density input

Let `N_0^*(T)` count simple zeros of zeta on the critical line with ordinate in
`(0,T]`. The required unconditional input is

\[
 \boxed{N_0^*(T)\gg T\log T.}                            \tag{L-18511.1}
\]

A suitable primary source is Pratt--Robles--Zaharescu--Zeindler, *More than
five-twelfths of the zeros of zeta are on the critical line*. Their mollifier
optimization gives an explicit positive proportion of zeros that are simple
and on the critical line. A theorem counting critical-line zeros only with
multiplicity is not sufficient for the distinct uniqueness set used here.

## 2. Uniform Paley--Wiener zero count on a finite packet

Let `W` be a finite-dimensional metric space and let

\[
 J:W\to L^2([-a,a])                                      \tag{L-18511.2}
\]

be injective. Put

\[
 F_w(z)=\int_{-a}^{a}(Jw)(x)e^{-izx}dx.                  \tag{L-18511.3}
\]

Then there is a constant `C_W` such that every nonzero `w in W` satisfies

\[
 \boxed{
 n_{\mathbb R}(F_w;T)
 \le C_W(1+T)}                                           \tag{L-18511.4}
\]

for every `T>=1`, after normalizing `||w||_G=1`. Here `n_R` counts distinct real
zeros in `[-T,T]`.

### Proof

Fix any radius `R_0>0`. The quantity

\[
 p(w)=\max_{|z|\le R_0}|F_w(z)|                           \tag{L-18511.5}
\]

is a norm on `W`: if `p(w)=0`, the entire function `F_w` vanishes on a disk and
therefore identically, so injectivity of the Fourier transform and of `J` gives
`w=0`. Finite-dimensional norm equivalence yields

\[
 p(w)\ge c_W\|w\|_G                                     \tag{L-18511.6}
\]

for one `c_W>0`.

For normalized `w`, choose `z_w` in the disk with
`|F_w(z_w)|>=c_W`. Cauchy--Schwarz and finite-dimensional boundedness of `J`
give

\[
 |F_w(z)|\le C_W' e^{a|\operatorname{Im}z|}.             \tag{L-18511.7}
\]

Apply Jensen's formula in a disk centered at `z_w`, using inner radius
`T+2R_0` and outer radius `2(T+2R_0)`. The interval `[-T,T]` lies in the inner
disk. The logarithmic maximum on the outer circle is `O_W(aT+1)`, while the
central value is bounded below by `c_W`. Since every zero in the inner disk
contributes at least `log 2` to the Jensen integral, (L-18511.4) follows. QED.

## 3. One uniform finite height

By (L-18511.1), choose `T_W` so large that

\[
 N_0^*(T_W)>C_W(1+T_W).                                  \tag{L-18511.8}
\]

If a normalized `F_w` vanished at every simple critical-line zero with
`|gamma|<=T_W`, then it would have more real zeros than allowed by
(L-18511.4). Hence

\[
 \boxed{
 \bigcap_{\substack{|\gamma|\le T_W\\
          \gamma\text{ simple line zero}}}
 \ker \mathcal E_\gamma|_W
 =\{0\}.}                                                \tag{L-18511.9}
\]

Thus one finite height separates the whole packet simultaneously. Ordinary row
elimination extracts exactly `dim W` simple zeros whose evaluation rows form an
isomorphism on `W`.

## 4. Proof-producing search

The theorem gives an algorithmically terminating finite procedure:

1. enumerate simple Hardy-Z sign-change zero intervals with directed arithmetic;
2. certify the corresponding finite total zero count and simplicity gates;
3. append their directed evaluation rows on `W`;
4. stop when a `dim W` square minor excludes zero.

The theorem guarantees termination, although it gives no useful complexity or
conditioning bound. Exact rational/interval LDL on the resulting Gram then
produces the finite `sigma_Z^2>0` of `L-18507`.

## 5. Relationship to the quantitative moat

The uniform finite height closes only the algebraic and algorithmic existence of
a frame. The constants `T_W`, the minor determinant, and the smallest singular
value may deteriorate arbitrarily with the packet. Therefore it does not prove

\[
 B_T+\beta<\Sigma                                         \tag{L-18511.10}
\]

cofinally. `L-18509` identifies collective compactness as one route to a uniform
frame, and `L-18510` identifies a rescaled analytic-profile route yielding a
`c log R` floor.

## 6. Proof boundary

- The finite-height statement and search termination are exact.
- Production use must bind the correct simple-zero theorem and may not cite a
  multiplicity-only critical-line proportion.
- No lower bound for the selected determinant or right-inverse norm is supplied.
- RH is not claimed proved.
