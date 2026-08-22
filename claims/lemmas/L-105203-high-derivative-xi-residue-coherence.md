# L-105203 — Xi critical residues are asymptotically monochromatic throughout the growing high-derivative band

Claim ID: `L-105203`  
Status: **PROVED FROM THE UNIFORM TILTED-FOURIER SADDLE MODEL**  
Created: 2026-08-23  
Depends on: PR #720 `L-104517`; `L-104522--L-104523`  
RH status: **not assumed**

Fix

\[
0<\eta<1,
\qquad H>0,
\]

and let `T_N>=1` satisfy

\[
T_N\sqrt{\frac{\log N}{\eta N}}\longrightarrow0.
\tag{L-105203.1}
\]

Use the tilted moments and saddles of `L-104517`:

\[
M_m=\int_0^\infty u^m\Phi(u)\,du,
\qquad
w_m=\frac12\log m+O(\log\log m).
\]

For `eta N<=m<=N`, write

\[
\Xi^{(m)}(z)
=i^mM_m\bigl[A_m(z)+(-1)^mA_m(-z)\bigr].
\tag{L-105203.2}
\]

Let

\[
\epsilon_N=
\sup_{\substack{\eta N-1\le m\le N+1\\
|\Re z|\le T_N,\ |\Im z|\le H}}
\left|e^{-iw_mz}A_m(z)-1\right|.
\tag{L-105203.3}
\]

The uniform saddle theorem gives

\[
\epsilon_N\longrightarrow0,
\qquad
\sup_{\eta N\le m\le N}|w_{m+1}-w_m|=O_\eta(N^{-1}).
\tag{L-105203.4}
\]

Put

\[
\delta_N=\epsilon_N+\frac{T_N}{N}.
\tag{L-105203.5}
\]

Then `delta_N->0`.

## 1. Uniform critical-residue asymptotic

Let

\[
\eta N+1\le m\le N-1
\]

and let `c` be any zero of `Xi^(m)` in `[-T_N,T_N]`. PR #720 proves that all
such zeros are real and simple. Define

\[
\rho_{m,c}
=\frac{\Xi^{(m-1)}(c)}{\Xi^{(m+1)}(c)}
\tag{L-105203.6}
\]

and

\[
\alpha_m=\frac{M_{m-1}}{M_{m+1}}>0.
\tag{L-105203.7}
\]

Then, uniformly in the whole band and over every such zero,

\[
\boxed{
\rho_{m,c}
=-\alpha_m\bigl(1+O_\eta(\delta_N)\bigr).
}
\tag{L-105203.8}

### Proof

For even `m`, after division by `2i^mM_m`, (L-105203.2) is

\[
\cos(w_mz)+O(\epsilon_Ne^{w_m|\Im z|});
\]

for odd `m`, after division by `2i^(m+1)M_m`, it is

\[
\sin(w_mz)+O(\epsilon_Ne^{w_m|\Im z|}).
\]

On the real axis, every zero `c` therefore satisfies

\[
\operatorname{dist}
\bigl(w_mc,\ \text{the corresponding cosine/sine zero lattice}\bigr)
=O(\epsilon_N).
\tag{L-105203.9}
\]

Moreover

\[
(w_{m\pm1}-w_m)c=O_\eta(T_N/N).
\tag{L-105203.10}
\]

The normalized adjacent derivatives consequently evaluate at `c` as the two
complementary trigonometric functions with common magnitude

\[
1+O_\eta(\delta_N)
\]

and opposite derivative-chain sign. Restoring the moment amplitudes gives
(L-105203.8).

The same concentration also yields

\[
\frac{M_{m+1}}{M_m}=w_m(1+o_\eta(1)),
\qquad
\frac{M_m}{M_{m-1}}=w_m(1+o_\eta(1)),
\]

so

\[
\boxed{
\alpha_m=w_m^{-2}(1+o_\eta(1)).
}
\tag{L-105203.11
}

## 2. First and second residue moments

Let

\[
R_m(T_N)=\#\{c\in[-T_N,T_N]:\Xi^{(m)}(c)=0\}.
\]

Put

\[
\mathcal M_{1,m}(T_N)
=-\sum_c\rho_{m,c},
\qquad
\mathcal M_{2,m}(T_N)
=\sum_c|\rho_{m,c}|^2.
\]

Equation (L-105203.8) gives

\[
\boxed{
\mathcal M_{1,m}(T_N)
=\alpha_mR_m(T_N)
\bigl(1+O_\eta(\delta_N)\bigr),
}
\tag{L-105203.12}

and

\[
\boxed{
\mathcal M_{2,m}(T_N)
=\alpha_m^2R_m(T_N)
\bigl(1+O_\eta(\delta_N)\bigr).
}
\tag{L-105203.13}

In particular all critical residues in the band are negative for sufficiently
large `N`; every real critical point is Rolle-generating.

## 3. Coherence tends to one

The residue coherence of `L-104523` satisfies

\[
\boxed{
\inf_{\eta N+1\le m\le N-1}
\mathfrak C_m(T_N)
=1-O_\eta(\delta_N).
}
\tag{L-105203.14}

A completely explicit lower bound follows whenever

\[
\left|\frac{\rho_{m,c}}{-\alpha_m}-1\right|\le\delta<1:
\]

\[
\boxed{
\mathfrak C_m(T_N)
\ge\left(\frac{1-\delta}{1+\delta}\right)^2.
}
\tag{L-105203.15}

Thus `RCMV104530` holds unconditionally throughout the high derivative band,
with the transfer constant

\[
\boxed{
2\mathfrak C_m(T_N)-1=1-O_\eta(\delta_N).
}
\tag{L-105203.16}

## 4. Meaning and scope

This theorem validates the residue-coherence mechanism on a growing Xi window
and a constant-fraction derivative band. It improves the high-band theorem by
identifying the actual inverse-curvature distribution, not only its zero
count.

It does not descend to a fixed derivative order. Any full cascade must control
how the monochromatic residue carrier deforms after leaving the saddle band.
The Poisson--Bézout localizer of `L-105200--L-105202` is designed to make that
deformation a zero-free-axis boundary problem plus explicit entire
interpolation and nonreal-critical corrections.
