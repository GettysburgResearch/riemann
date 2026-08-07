# L-23404 — Top-order concentration of the hard Heath–Brown core

Claim ID: `L-23404`  
Title: After higher Euler closure of every macroscopic unrestricted variable, the unresolved fixed-scale Möbius core lies only in the top identity orders  
Status: **PROPOSED — COMPLETE SCALE GEOMETRY PENDING INDEPENDENT REVIEW; ENERGY ESTIMATE OPEN**  
Authoring agent: `gpt56-pro-09-p`  
Created: 2026-08-07  
Dependencies: PR #158 `L-15156`; PR #158 `L-15160`; PR #165 `L-15449/L-15450`; `L-15159`  
Scope: the exact finite Heath–Brown source dictionary

## 1. Tuple scales

Fix an identity order `K` and an output logarithmic block `J`. Let

\[
X=e^{J+O_K(1)},
\qquad
V=\lceil X^{1/K}\rceil.
\]

An order-`j` Heath–Brown tuple contains:

- `j` truncated Möbius variables `d_i<=V`;
- one logarithmic variable and `j-1` constant-one variables, all unrestricted;
- total product in the active compact window
  \[
  e^{J-C_K}\le n\le e^{J+C_K}.
  \]

Write

\[
D=d_1\cdots d_j,
\qquad
U=\text{product of all unrestricted variables}.
\]

Then

\[
D\le V^j
\le\exp\left({j\over K}J+O_K(1)\right).
\tag{L-23404.1}

## 2. Macroscopic free-variable closure

There are at most `K` unrestricted variables in one tuple. Fix a number

\[
0<\eta<1.
\]

If

\[
\log U\ge\eta J-O_K(1),
\]

then at least one unrestricted variable has logarithmic size

\[
\ge {\eta\over K}J-O_K(1).
\]

After the exact finite complexity regrouping of `L-15450`, this variable is a complete positive-integer lattice variable on the active compact window. The higher-order Euler theorem `L-15160`, with any fixed smoothing order

\[
R>{K\over2\eta},
\tag{L-23404.2}

closes that packet exponentially.

Thus every packet not covered by higher Euler closure must satisfy

\[
\boxed{
\log U<\eta J+O_K(1).}
\tag{L-23404.3}

## 3. Top-order concentration

For a packet satisfying (L-23404.3), the active product lower bound and (L-23404.1) give

\[
J-C_K
\le
\log D+\log U
\le
\left({j\over K}+\eta\right)J+O_K(1).
\]

Therefore

\[
\boxed{
{j\over K}\ge1-\eta-O_K(J^{-1}).}
\tag{L-23404.4}

Equivalently, for every fixed `kappa>0`, all sufficiently large blocks have no unresolved order-`j` packet with

\[
j\le(1-\eta-\kappa)K.
\]

The hard Möbius core is confined to the top band

\[
\boxed{
K-j\le(\eta+o_K(1))K.}
\tag{L-23404.5}

This is an exact scale consequence, not a cancellation estimate.

## 4. A square-root-order schedule

One permitted increasing-order schedule is

\[
\eta_K=K^{-1/2}.
\]

Choose a safe smoothing order, for example,

\[
R_K=K^2.
\]

Then every packet with a macroscopic unrestricted variable is Euler-closed, while the entire unresolved dictionary lies in

\[
\boxed{
j\ge K-O(\sqrt K).}
\tag{L-23404.6}

The number of possible identity orders in the hard band is only `O(sqrt(K))`. The signed binomial coefficient mass in this band is

\[
\sum_{\ell\le C\sqrt K}{K\choose\ell}
=\exp\{O(\sqrt K\log K)\},
\]

which is independent of the output scale `J` and therefore has zero block exponent for each fixed `K`.

This schedule is not automatically compatible with the final scale-contraction rate: if the contraction reserve is also of order `eta_K`, the balanced estimate must produce

\[
\varepsilon_K=o(K^{-1/2}).
\]

That is an explicit quantitative target, not a conclusion of the scale geometry.

## 5. Relation to the exact Möbius decoder

`L-15159` proves that the complete signed Heath–Brown packet before the final logarithmic convolution reconstructs `mu` exactly through `V^K`, and that fixing the logarithmic variable at `q_0=2` leaves one exact translated Möbius signal.

The present lemma explains where that signal resides after Euler closure:

- lower identity orders necessarily expose enough unrestricted scale to be terminally summable;
- the surviving fixed-logarithm Möbius source is concentrated in the near-top truncated-variable band.

Thus increasing `K` does not dilute the hard source. It pushes it into an increasingly high-dimensional, increasingly top-order balanced packet.

## 6. Consequence for `BTP(K)`

The balanced theorem no longer needs to treat the complete Heath–Brown order range symmetrically. A proof may be organized as:

1. higher Euler closure below the top band;
2. exact signed recombination of the top `O(eta_K K)` orders;
3. one source-specific balanced estimate for the resulting truncated Möbius tensor;
4. the first-cell shell-energy mutation of `T-23401`.

Any estimate that takes absolute values over the top-order binomial band before recombination destroys the exact `mu` decoder.

## 7. Proof boundary

Closed here:

- the free-variable scale dichotomy;
- the top-order concentration;
- the explicit increasing-order schedule and coefficient count.

Open:

- a signed estimate for the top-order truncated Möbius tensor;
- a coefficient rate `epsilon_K=o(eta_K)`;
- the shell-energy bound;
- RH.
