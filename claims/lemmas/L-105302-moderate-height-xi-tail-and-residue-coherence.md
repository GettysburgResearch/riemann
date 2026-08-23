# L-105302 — Xi derivative-tail geometry with a `T^(3/2+o(1))` entry order

Claim ID: `L-105302`  
Status: **PROPOSED UNCONDITIONAL ANALYTIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-23  
Depends on: `L-105301`; proposed parent `L-105201--L-105203`; PR #720  
RH status: **not assumed**

## 1. Common two-thirds-height box

Fix `C,H>0` and put

\[
T_M=C\left({M\over\log M}\right)^{2/3}.
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
\]

are real and simple. Uniformly in the same range,

\[
\boxed{
N_m(T_M)
={2w_mT_M\over\pi}+O_C(1).
}
\tag{L-105302.3}

Thus every original-height rectangle `|Re z|<=T`, `|Im z|<=H` is cleared by
all derivative orders

\[
\boxed{
m\ge K T^{3/2}\log(2+T)}
\tag{L-105302.4}

for sufficiently large `T` and a suitable `K=K(C,H)`.

## 2. Cubic model and cellwise Rouché proof

Define

\[
\Theta_m(z)
=w_mz-{\gamma_ms_m^3z^3\over6}.
\tag{L-105302.5}
\]

`L-105301` gives, uniformly on a slightly larger box,

\[
A_m(z)
=e^{-s_m^2z^2/2}e^{i\Theta_m(z)}(1+o(1)),
\qquad
A_m(-z)
=e^{-s_m^2z^2/2}e^{-i\Theta_m(z)}(1+o(1)).
\tag{L-105302.6}
\]

Hence

\[
\Xi^{(m)}(z)
=i^mM_me^{-s_m^2z^2/2}
\left[
 e^{i\Theta_m(z)}(1+o(1))
 +(-1)^me^{-i\Theta_m(z)}(1+o(1))
ight].
\tag{L-105302.7}

The Gaussian factor is nonzero. Since `gamma_m<0`,

\[
\Theta_m'(x)>0
\qquad(x\in\mathbb R).
\]

Moreover, for `z=x+iy` with `|y|<=H`,

\[
\Im\Theta_m(z)
=y\left[
 w_m-{\gamma_ms_m^3\over6}(3x^2-y^2)
\right]
\]

has the sign of `y` for large `m`. Therefore every sine/cosine zero of the
cubic model in the strip is real and simple.

Around each model zero take a disk of radius `delta_M/w_m`, where
`delta_M->0` and the relative saddle error is `o(delta_M)`. Rouché gives one
Xi-derivative zero in every complete disk. Away from the disks, the analytic
phase has a uniform sine/cosine lower bound after the larger exponential is
factored, excluding extra zeros. Conjugation plus multiplicity one forces the
actual disk zero to be real.

The cubic phase changes by only `O_C(1)` across the complete real box:

\[
\sup_{|x|\le T_M}
|\Theta_m(x)-w_mx|=O_C(1).
\tag{L-105302.8}
\]

Counting phase cells therefore gives (L-105302.3).

## 3. Critical residues in a buffered box

Fix `0<C_0<C`. For `m>=M` and every real zero `c` of `Xi^(m+1)` with
`|c|<=C_0(M/log M)^(2/3)`, put

\[
\rho_{m,c}={\Xi^{(m)}(c)\over\Xi^{(m+2)}(c)}.
\tag{L-105302.9}

For the cubic-corrected model

\[
g_m(x)=e^{-s_m^2x^2/2}\chi_m(\Theta_m(x)),
\]

write `q=chi_m'(Theta_m)/chi_m(Theta_m)`. At a critical point,

\[
q={s_m^2x\over\Theta_m'(x)}.
\]

Since `q'=-(1+q^2)` with respect to the phase variable, direct logarithmic
differentiation gives

\[
\boxed{
{g_m''(x)\over g_m(x)}
=-s_m^2-(\Theta_m'(x))^2-s_m^4x^2
+{s_m^2x\Theta_m''(x)\over\Theta_m'(x)}.
}
\tag{L-105302.10}

On the two-thirds box,

\[
\Theta_m'(x)=w_m+o(1),
\qquad
\Theta_m''(x)=o(1),
\tag{L-105302.11}
\]

and every other term in (L-105302.10) is `o(w_m^2)`. The buffered `C^2`
relative approximation therefore yields

\[
\boxed{
\rho_{m,c}=-w_m^{-2}(1+o(1))
}
\tag{L-105302.12}

uniformly over the complete derivative tail. All such residues are negative.

## 4. Residue coherence

Let `R_(m,M)` be the number of the buffered critical points and define

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
\tag{L-105302.13}

uniformly for every `m>=M`. Moreover,

\[
\boxed{
A_{m,M}
={2C_0(M/\log M)^{2/3}\over\pi w_m}(1+o(1)),
\qquad
B_{m,M}
={2C_0(M/\log M)^{2/3}\over\pi w_m^3}(1+o(1)).
}
\tag{L-105302.14}

Thus `RCMV104530` holds with asymptotically optimal margin on the enlarged
box.

## 5. Improved reverse-Rolle entry scale

Combining (L-105302.4) with the cumulative budget of parent `L-105203`, the
terminal high-derivative off-real count in a height-`T` rectangle vanishes at
order

\[
\boxed{r(T)=O(T^{3/2}\log T)=T^{3/2+o(1)},}
\tag{L-105302.15}

rather than `T^(2+o(1))`. The still-open coherence/winding budget now contains
only the first `T^(3/2+o(1))` derivative levels.

## 6. Scope

The theorem remains a high-derivative entry result. It does not control the
moderate-to-fixed derivative ladder and does not prove RH. Crossing the
two-thirds height exponent requires a quartic or full complex-saddle normal
form.
