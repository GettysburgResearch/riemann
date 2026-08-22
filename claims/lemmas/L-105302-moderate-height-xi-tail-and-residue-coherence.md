# L-105302 — Xi derivative-tail geometry with a `T^(3/2+o(1))` entry order

Claim ID: `L-105302`  
Status: **PROPOSED UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105301`; proposed parent `L-105201--L-105203`; PR #720  
RH status: **not assumed**

## 1. Common moderate-height box

Fix `H>0` and put

\[
T_M={M^{2/3}\over(\log M)^{3/4}}.
\tag{L-105302.1}
\]

For all sufficiently large `M`, simultaneously for every integer `m>=M`, all
zeros of `Xi^(m)` in

\[
\boxed{
|\Re z|\le T_M,
\qquad
|\Im z|\le H
}
\tag{L-105302.2}

are real and simple. Uniformly in the same range,

\[
\boxed{
N_m(T_M)
={2w_mT_M\over\pi}+O(1).
}
\tag{L-105302.3}

Thus every original-height rectangle `|Re z|<=T`, `|Im z|<=H` is cleared by
all derivative orders

\[
\boxed{
m\ge K T^{3/2}(\log(2+T))^{9/8}}
\tag{L-105302.4}

for sufficiently large `T` and a suitable `K=K(H)`.

## 2. Cellwise Rouché proof

`L-105301` gives

\[
A_m(\pm z)
=e^{\pm iw_mz-s_m^2z^2/2}(1+o(1))
\tag{L-105302.5}
\]

uniformly on a slightly larger box. Hence

\[
\Xi^{(m)}(z)
=i^mM_me^{-s_m^2z^2/2}
\left[
 e^{iw_mz}(1+o(1))
 +(-1)^me^{-iw_mz}(1+o(1))
ight].
\tag{L-105302.6}

The Gaussian factor is nonzero. Around each sine/cosine model zero take a disk
of radius `delta_M/w_m`, where `delta_M->0` and the relative saddle error is
`o(delta_M)`. Rouché gives exactly one zero per complete disk. Away from the
disks, factor the larger exponential; the model bracket has a uniform relative
lower bound and excludes every additional zero. Conjugation symmetry and the
multiplicity-one count force every disk zero to be real and simple. Counting
model cells gives (L-105302.3).

## 3. Critical residues in a buffered box

Fix `0<C_0<1`. For `m>=M` and every real zero `c` of `Xi^(m+1)` with
`|c|<=C_0T_M`, put

\[
\rho_{m,c}={\Xi^{(m)}(c)\over\Xi^{(m+2)}(c)}.
\tag{L-105302.7}

For the Gaussian trigonometric model

\[
g_m(x)=e^{-s_m^2x^2/2}\chi_m(w_mx),
\]

one has at every model critical point

\[
{g_m(x)\over g_m''(x)}
=-{1\over w_m^2+s_m^2+s_m^4x^2}.
\tag{L-105302.8}

On the moderate box,

\[
{s_m^2+s_m^4x^2\over w_m^2}=o(1)
\tag{L-105302.9}
\]

uniformly. The `C^2` approximation in `L-105301` therefore yields

\[
\boxed{
\rho_{m,c}=-w_m^{-2}(1+o(1))
}
\tag{L-105302.10}

uniformly over the complete derivative tail and every buffered critical point.
All such residues are negative.

## 4. Residue coherence

Let `R_(m,M)` be the number of these critical points and define

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
\tag{L-105302.11}

uniformly for every `m>=M`. Moreover,

\[
\boxed{
A_{m,M}
={2C_0T_M\over\pi w_m}(1+o(1)),
\qquad
B_{m,M}
={2C_0T_M\over\pi w_m^3}(1+o(1)).
}
\tag{L-105302.12}

Thus `RCMV104530` holds with asymptotically optimal margin on the moderate
height box.

## 5. Improved reverse-Rolle entry scale

Combining (L-105302.4) with the cumulative budget of parent `L-105203`, the
terminal high-derivative off-real count in a height-`T` rectangle vanishes at
order

\[
\boxed{r(T)=T^{3/2+o(1)},}
\tag{L-105302.13}

rather than `T^(2+o(1))`. The still-open coherence/winding budget now contains
only the first `T^(3/2+o(1))` derivative levels.

## 6. Scope

The theorem remains a high-derivative entry result. It does not control the
moderate-to-fixed derivative ladder and does not prove RH. The two-thirds
height exponent is the endpoint of the relative quadratic saddle model;
crossing it requires a cubic complex-saddle normal form.
