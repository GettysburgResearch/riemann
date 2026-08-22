# L-105206 — Xi derivative-tail real-rooting and residue coherence at height `T^(3/2+o(1))`

Claim ID: `L-105206`  
Status: **PROPOSED UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105205`; PR #720 `L-104516`, `L-104522`  
RH status: **not assumed**

## 1. Common moderate-height box

Fix `H>0`. Put

\[
T_M={M^{2/3}\over(\log M)^{3/4}}.
\tag{L-105206.1}
\]

For all sufficiently large `M`, simultaneously for every integer `m>=M`, all
zeros of `Xi^(m)` in

\[
\boxed{
|\Re z|\le T_M,
\qquad
|\Im z|\le H
}
\tag{L-105206.2}
\]

are real and simple. Uniformly in the same range,

\[
\boxed{
N_m(T_M)
={2w_mT_M\over\pi}+O(1).
}
\tag{L-105206.3}

Thus every original-height rectangle `|Re z|<=T`, `|Im z|<=H` is cleared by
all derivative orders

\[
\boxed{
m\ge K T^{3/2}(\log(2+T))^{9/8}}
\tag{L-105206.4}

for sufficiently large `T` and a suitable `K=K(H)`.

## 2. Rouché proof

`L-105205` gives the relative approximation

\[
A_m(\pm z)
=e^{\pm iw_mz-s_m^2z^2/2}(1+o(1))
\tag{L-105206.5}
\]

uniformly on a slightly larger box.  Therefore

\[
\Xi^{(m)}(z)
=i^mM_me^{-s_m^2z^2/2}
\left[
 e^{iw_mz}+(-1)^me^{-iw_mz}
ight](1+o(1))
\tag{L-105206.6}
\]

in the usual relative two-term sense.

The Gaussian factor is nonzero. Around each sine/cosine model zero take a disk
of radius `delta_M/w_m`, where `delta_M->0` but the relative saddle error is
`o(delta_M)`. Rouché gives exactly one zero in every complete disk. Away from
the disks, factor the larger exponential; the sine/cosine bracket has a
uniform relative lower bound, excluding every additional zero. Conjugation
symmetry and the one-zero count force the disk zero to be real and simple.
Counting the model cells gives (L-105206.3).

## 3. Critical residues in a buffered box

Fix `0<C_0<C_1=1` and apply the preceding proof with outer width `T_M` and
inner width `C_0T_M`.  For `m>=M` and every real zero `c` of `Xi^(m+1)` in the
inner box, put

\[
\rho_{m,c}={\Xi^{(m)}(c)\over\Xi^{(m+2)}(c)}.
\tag{L-105206.7}
\]

For the Gaussian trigonometric model

\[
g_m(x)=e^{-s_m^2x^2/2}\chi_m(w_mx),
\]

at a critical point one has exactly

\[
{g_m(x)\over g_m''(x)}
=-{1\over w_m^2+s_m^2+s_m^4x^2}.
\tag{L-105206.8}
\]

On the moderate box,

\[
{s_m^2+s_m^4x^2\over w_m^2}=o(1)
\tag{L-105206.9}
\]

uniformly for `m>=M`. The `C^2` relative approximation in `L-105205.3`
therefore gives

\[
\boxed{
\rho_{m,c}=-w_m^{-2}(1+o(1))
}
\tag{L-105206.10}
\]

uniformly over every critical point in the buffered box. In particular every
such residue is negative.

## 4. Moderate-height residue coherence

Let `R_(m,M)` be the number of these critical points, and define

\[
A_{m,M}=-\sum_c\rho_{m,c},
\qquad
B_{m,M}=\sum_c\rho_{m,c}^2,
\qquad
\mathfrak C_{m,M}={A_{m,M}^2\over R_{m,M}B_{m,M}}.
\]

Then

\[
\boxed{
\mathfrak C_{m,M}=1-o(1)
}
\tag{L-105206.11}

uniformly for every `m>=M`. Moreover,

\[
\boxed{
A_{m,M}
={2C_0T_M\over\pi w_m}(1+o(1)),
\qquad
B_{m,M}
={2C_0T_M\over\pi w_m^3}(1+o(1)).
}
\tag{L-105206.12

Thus the residue-coherence premise `RCMV104530` is proved with asymptotically
optimal margin on a box whose height is larger by a factor

\[
(M/\log M)^{1/6}(\log M)^{-1/12}
\]

than the natural Gaussian box of `L-105202`.

## 5. Improved reverse-Rolle entry scale

Combining (L-105206.4) with the exact cumulative budget `L-105203`, the
terminal high-derivative off-real count in a height-`T` rectangle vanishes at
order

\[
\boxed{r(T)=T^{3/2+o(1)},}
\tag{L-105206.13

rather than `T^(2+o(1))`. The still-open budget now contains only the first
`T^(3/2+o(1))` derivative levels.

## 6. Scope

The theorem remains a high-derivative entry theorem. It does not bound the
coherence/winding debt in the lower derivative ladder and does not prove RH.
The two-thirds exponent is the endpoint of the relative quadratic saddle
model; crossing it requires a cubic complex-saddle normal form rather than
another Gaussian estimate.
