# R-91309 — The explicit all-generation pole-node source vector does not have the model source norm

Claim ID: `R-91309`  
Status: **EXACT NORMALIZATION REFUTATION / ONE-NODE CORRECTION**  
Created: 2026-08-12  
Depends on: `L-91319/L-91320`; elementary expansions at \(s=1\)  
RH status: **unproved**

## 1. The two proposed scalars

The all-generation arithmetic vector of `L-91319` has norm squared

\[
 S_a
 =A_{2a}^{\rm pole}
 \left[\gamma-\frac{\zeta'}{\zeta}(1+2a)\right],
 \qquad
 A_{2a}^{\rm pole}=\frac{\xi(1)}{\xi(1+2a)}.
 \tag{R-91309.1}
\]

At the pole-aligned node

\[
 \eta_a=\frac12+a,
 \tag{R-91309.2}
\]

the zero-factor-independent model ledger of `L-91320` assigns the RH-expected critical-plus-stable norm

\[
 T_a
 =\frac{|\Delta_a(\eta_a)|^{-2}-|\Theta_a(\eta_a)|^2}{2\eta_a},
 \tag{R-91309.3}
\]

where

\[
 \Theta_a(\eta_a)=\frac{\xi(1)}{\xi(1+2a)},
 \qquad
 \Delta_a(z)=b_a(z)^2b_{2a}(z)^2b_{4a}(z)^2,
 \qquad
 b_r(z)=\frac{z-r}{z+r}.
 \tag{R-91309.4}
\]

## 2. Arithmetic source asymptotic

The Laurent expansion

\[
 \frac{\zeta'}{\zeta}(1+\varepsilon)
 =-\frac1\varepsilon+\gamma+O(\varepsilon)
 \tag{R-91309.5}
\]

and \(A_{2a}^{\rm pole}=1+O(a)\) give

\[
 \boxed{
 S_a=\frac1{2a}+O(1)
 \qquad(a\downarrow0).
 }
 \tag{R-91309.6}
\]

## 3. Model norm asymptotic

Put

\[
 q_\xi:=\frac{\xi'(1)}{\xi(1)}
 =1+\frac\gamma2-\frac12\log(4\pi).
 \tag{R-91309.7}
\]

For \(r\in\{1,2,4\}\),

\[
 \log b_{ra}(\eta_a)=-4ra+O(a^2).
 \tag{R-91309.8}
\]

Therefore

\[
 \Delta_a(\eta_a)^{-2}
 =1+112a+O(a^2),
 \tag{R-91309.9}
\]

while

\[
 \Theta_a(\eta_a)^2
 =1-4q_\xi a+O(a^2).
 \tag{R-91309.10}
\]

Since \(2\eta_a=1+2a\),

\[
 \boxed{
 T_a=(112+4q_\xi)a+O(a^2).
 }
 \tag{R-91309.11}
\]

Consequently

\[
 \boxed{
 \frac{S_a}{T_a}
 \sim
 \frac{1}{2(112+4q_\xi)}a^{-2}
 \longrightarrow\infty.
 }
 \tag{R-91309.12}
\]

## 4. Consequence

The explicit vector of `L-91319` cannot, with its declared norm, be mapped isometrically to the critical and deterministic stable outputs of `L-91320` with no auxiliary remainder. The mismatch is present in safe real Xi values and is independent of RH.

This does not refute the one-node model-space theorem. It refutes only the identification of the unrenormalized all-generation source vector as the exhausted model source vector.

A valid one-node route must supply a nontrivial completed normalization or tangent map derived from the common analytic intertwiner. Choosing a scalar afterward to force norm equality is the vacuous fit already rejected by `R-91305`.
