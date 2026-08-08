# L-30502 — Exact shift terminalization and the unshifted eta core

Claim ID: `L-30502`  
Title: Every discrete `-1` lattice shift is an exact half-scale divisor source with bounded commutator debt; the only propagated state is the complete unshifted eta convolution  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: PR #280 central first-difference identity; PR #272 adjacent-tree commutators; `L-30501`  
Scope: exact finite producer decomposition and capacity comparison; no RH conclusion

## 1. Shifted and unshifted residuals

Let `r` be a finite real sequence supported on `2,...,N`, extended by zero outside that interval. Define the actual central residual

\[
(\mathcal T_Nr)(q)
=\sum_{k\ge1}
\left[r(2kq-1)-r((2k+1)q)\right]
\tag{L-30502.1}
\]

and the unshifted eta residual

\[
(\mathcal U_Nr)(q)
=\sum_{k\ge1}
\left[r(2kq)-r((2k+1)q)\right].
\tag{L-30502.2}
\]

Both sums are finite. Their exact difference is

\[
\boxed{
(\mathcal E_Nr)(q)
=(\mathcal T_N-\mathcal U_N)r(q)
=\sum_{k\ge1}\left[r(2kq-1)-r(2kq)\right].
}
\tag{L-30502.3}
\]

## 2. The shift is a genuine divisor source

Put

\[
\boxed{
\sigma_r(m)=r(2m-1)-r(2m)
\qquad\left(1\le m\le\left\lfloor\frac{N+1}{2}\right\rfloor\right).
}
\tag{L-30502.4}
\]

Then reindexing `m=kq` gives

\[
\boxed{
(\mathcal E_Nr)(q)
=\sum_{\substack{m\\q\mid m}}\sigma_r(m).
}
\tag{L-30502.5}
\]

Unlike the full cutoff tail rejected in `R-30501`, the one-step shift is therefore an actual finite divisor source at the next half scale.

Let

\[
E_h=T_{h+1}-T_h
\]

be the adjacent central-tree commutator. Define

\[
\boxed{
\Phi_N(r)=\sum_m\sigma_r(m)E_{m-1}.
}
\tag{L-30502.6}
\]

Since `L_q(E_(m-1))=1_(q|m)`, equations (L-30502.5)--(L-30502.6) give

\[
\boxed{
L_q(\Phi_N(r))=(\mathcal E_Nr)(q)
}
\tag{L-30502.7}
\]

for every carry column. The lattice shift can be terminated immediately and exactly.

## 3. Exact modified central stage

Let

\[
a_r(n)=r(n)-r(n+1).
\tag{L-30502.8}
\]

Place `a_r(n)` on the central split `[n,floor(n/2)]`, and call the resulting signed flow `Cen(r)`. The central residual identity of PR #280 is

\[
L(\operatorname{Cen}(r))=r-\mathcal T_Nr.
\tag{L-30502.9}
\]

Combining (L-30502.3) and (L-30502.7),

\[
\boxed{
L\left(\operatorname{Cen}(r)+\Phi_N(r)\right)
=r-\mathcal U_Nr.
}
\tag{L-30502.10}
\]

Thus one exact stage consists of:

```text
central first-difference flow;
+ terminal adjacent-commutator flow for the `-1` shift;
+ propagated unshifted eta residual.
```

No analytic continuation and no separately normed cutoff tail appears.

## 4. Support descent and finite saturation

The unshifted residual satisfies

\[
\operatorname{supp}(\mathcal U_Nr)
\subseteq
\left[2,\left\lfloor\frac N2\right\rfloor\right].
\tag{L-30502.11}
\]

Define recursively

\[
r_0=w_X,
\qquad
r_{j+1}=\mathcal U_{N_j}r_j,
\qquad
N_{j+1}=\left\lfloor\frac{N_j}{2}\right\rfloor.
\tag{L-30502.12}
\]

After at most `ceil(log_2 X)` stages, `r_j=0`. Summing (L-30502.10) gives an exact finite balanced signed flow for the complete critical target.

This producer differs from PR #280's raw central cascade only by consuming every lattice shift immediately instead of propagating it.

## 5. Capacity of the shift source

Put

\[
G_n=\sqrt n\,r(n).
\tag{L-30502.13}
\]

For every `m>=1`,

\[
\begin{aligned}
\sqrt m\,|\sigma_r(m)|
&=\sqrt m\left|
\frac{G_{2m-1}}{\sqrt{2m-1}}
-
\frac{G_{2m}}{\sqrt{2m}}
\right|\\
&\le
|G_{2m-1}-G_{2m}|
+rac{|G_{2m}|}{m}.
\end{aligned}
\tag{L-30502.14}
\]

The second estimate follows from the exact difference formula for reciprocal square roots; the displayed constant one is deliberately conservative.

Therefore

\[
\boxed{
\sum_m\sqrt m\,|\sigma_r(m)|
\le
\sum_{n=2}^{N-1}|G_{n+1}-G_n|
+2\sum_{n=2}^{N}\frac{|G_n|}{n}.
}
\tag{L-30502.15}
\]

Using `||E_h||_(omega,1)<=24sqrt(h+1)` from `L-30402`,

\[
\boxed{
\mathcal N_\omega(\Phi_N(r))
\le24\left[
\operatorname{TV}(G)
+2\sum_n\frac{|G_n|}{n}
\right].
}
\tag{L-30502.16}
\]

This is an exact cancellation-preserving capacity bound for the lattice shift.

## 6. Central-edge debt uses the same normalized variation

The negative capacity of the central first-difference flow obeys

\[
\mathcal N_\omega(\operatorname{Cen}(r))
\le2\sum_n\sqrt n\,[r(n+1)-r(n)]_+.
\tag{L-30502.17}
\]

Since

\[
\sqrt n\,[r(n+1)-r(n)]_+
\le
|G_{n+1}-G_n|
+rac{|G_{n+1}|}{2n},
\]

we obtain

\[
\boxed{
\mathcal N_\omega(\operatorname{Cen}(r))
\le
2\operatorname{TV}(G)
+\sum_n\frac{|G_n|}{n}.
}
\tag{L-30502.18}

Thus both parts of the exact stage are controlled by one discrete critical variation functional

\[
\boxed{
\mathcal V_N(r)
=\operatorname{TV}(\sqrt n\,r(n))
+2\sum_{n=2}^{N}\frac{|\sqrt n\,r(n)|}{n}.
}
\tag{L-30502.19}
\]

For one stage,

\[
\boxed{
\mathcal N_\omega\left(\operatorname{Cen}(r)+\Phi_N(r)\right)
\le50\,\mathcal V_N(r).
}
\tag{L-30502.20}
\]

## 7. Exact eta-convolution representation of the propagated state

Suppose

\[
r(n)=n^{-1/2}G(\log(N/n))
\]

with `G(t)=0` for `t<0`. Put `t=log(N/q)`. Then

\[
\begin{aligned}
\sqrt q\,(\mathcal U_Nr)(q)
&=\sum_{m\ge2}(-1)^m m^{-1/2}
G(t-\log m)\\
&=(\beta*G)(t),
\end{aligned}
\tag{L-30502.21}
\]

where `beta` is the critical eta comb of `L-30501`. The finite endpoint is already enforced by the causal condition `G(t)=0` for negative `t`; there is no separate cutoff source.

After replacing `N` by `floor(N/2)`, the next normalized profile is a translate and restriction of `beta*G`. Translation and restriction do not increase the weighted `L^1` jet norms of `L-30501`.

This identifies the genuine propagated core:

\[
\boxed{
\text{unshifted eta convolution }\beta*G,
}
\tag{L-30502.22}
\]

while every discrete `-1` shift is paid terminally by (L-30502.16).

## 8. Correct proof frontier

The exact finite proof problem is no longer a cutoff-source manifest. It is the direct critical-variation estimate

\[
\boxed{
\sum_j\mathcal V_{N_j}(r_j)=X^{o(1)}
\quad\text{for}\quad
r_{j+1}=\mathcal U_{N_j}r_j.
}
\tag{L-30502.23}
\]

`L-30501` supplies a strict cancellation-preserving weighted-jet reserve for the continuum eta convolution. Equation (L-30502.21) shows that this is the correct source, with endpoint causality retained.

No reviewer reconstruction is hidden in this lemma: all finite source and flow maps through (L-30502.22) are explicit. Estimate (L-30502.23) is not claimed here.

## 9. Proof boundary

Closed exactly:

1. divisor-source factorization of the discrete shift;
2. terminal adjacent-commutator realization;
3. modified exact finite central stage;
4. support-halving saturation;
5. capacity bound by normalized discrete variation;
6. exact causal eta-convolution representation of the propagated state.

Open:

1. the cofinal critical-variation estimate (L-30502.23);
2. Cycle Debt and RH.