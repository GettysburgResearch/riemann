# L-106442 — Signed all-pass tail: exact Fourier and residue-Gram normal form

Claim ID: `L-106442`  
Status: **PROVED EXACT FOR RATIONAL ALL-PASS SYMBOLS; CONFLUENT EXTENSION INCLUDED**  
Created: 2026-08-25  
Depends on: `L-105290`, `L-106430--L-106431`  
RH status: **not assumed**

Let `U` be a scalar rational all-pass function on the compactified real line,
normalized by `U(infinity)=1`, with no real pole.  Use the unitary Fourier
transform and identify upper-half-plane Hardy space with `L^2(0,infinity)`.
Let `P_H` be the projection onto input frequencies `[0,H]` and
`Q_H=I-P_H`.

Write

\[
A_-=H_U^*H_U,
\qquad
A_+=H_{\overline U}^*H_{\overline U}.
\]

## 1. Exact signed Fourier tail

For `xi>0`, write

\[
u_-(\xi)=\widehat{U-1}(-\xi),
\qquad
u_+(\xi)=\widehat{U-1}(\xi).
\]

Direct integration of the Hankel kernels gives

\[
\boxed{
\operatorname{tr}(Q_HA_-Q_H)
 =\int_H^\infty(\xi-H)|u_-(\xi)|^2\,d\xi,
}
\tag{L-106442.1}

\[
\boxed{
\operatorname{tr}(Q_HA_+Q_H)
 =\int_H^\infty(\xi-H)|u_+(\xi)|^2\,d\xi.
}
\tag{L-106442.2}

Hence the signed complement in `T-106430` is

\[
\boxed{
\Delta_H(U)
 =\int_H^\infty(\xi-H)
  \bigl(|u_-(\xi)|^2-|u_+(\xi)|^2\bigr)\,d\xi.
}
\tag{L-106442.3}

The complete index decomposes as

\[
\boxed{
-\operatorname{wind}U
 =\int_0^\infty\min(\xi,H)
  \bigl(|u_-(\xi)|^2-|u_+(\xi)|^2\bigr)\,d\xi
 +\Delta_H(U).
}
\tag{L-106442.4}

This is the continuous Paley--Wiener form of the discrete identity

\[
\Delta_N(U)
 =\sum_{n>N}(n-N)(|U_{-n}|^2-|U_n|^2).
\tag{L-106442.5}

It makes explicit why absolute coverage is unnecessary: only a signed
high-frequency asymmetry remains.

## 2. Toeplitz-commutator firewall

Unimodularity gives

\[
A_--A_+
 =T_UT_U^*-T_U^*T_U.
\tag{L-106442.6}

For a finite low-frequency projection, the off-diagonal Toeplitz blocks do
not by themselves equal the signed complement.  The compressed tail Toeplitz
operator retains the same Fredholm index.  In the circle model,

\[
\Delta_N
 =-\operatorname{wind}U
  +\|Q_NT_UP_N\|_{\mathcal S_2}^2
  -\|P_NT_UQ_N\|_{\mathcal S_2}^2.
\tag{L-106442.7}

Thus dropping the compressed-tail index would incorrectly prove that a finite
source band controls every all-pass winding.  Equation (L-106442.3), not the
off-diagonal block alone, is the controlling formula.

## 3. Residue Cauchy--exponential Gram

Let `P_+` and `P_-` be the poles of `U` in the upper and lower half-planes,
with simple residues `r_z`.  For upper-half-plane points define

\[
K_H^+(z,w)
 =\frac{\exp\{-H[-i(z-\overline w)]\}}
       {[-i(z-\overline w)]^2},
\tag{L-106442.8}

and for lower-half-plane points define

\[
K_H^-(z,w)
 =\frac{\exp\{-H[i(z-\overline w)]\}}
       {[i(z-\overline w)]^2}.
\tag{L-106442.9}

Both kernels are positive semidefinite: they are Gram kernels of the functions

\[
\sqrt{\xi-H}\,e^{iz\xi}\mathbf 1_{\xi>H}
\]

in the upper case and their lower-half-plane analogues in the lower case.
Residue calculus gives

\[
\boxed{
\Delta_H(U)
 =\sum_{z,w\in P_+}r_z\overline{r_w}K_H^+(z,w)
  -\sum_{z,w\in P_-}r_z\overline{r_w}K_H^-(z,w).
}
\tag{L-106442.10}

For a pole of multiplicity `r`, replace the single exponential by its first
`r` polynomial-exponential jets; equivalently, differentiate the kernel in
`z` and `overline w`.  Equation (L-106442.10) remains exact with the complete
principal-part coefficient vector.  Near collisions are therefore retained
as confluent Cauchy blocks rather than estimated by separation.

## 4. Source-literal endpoint residues

For the endpoint symbol

\[
U_{0,K}=N_K/D_K
\]

of `L-106440`, every simple pole `z` satisfies

\[
\boxed{
\operatorname{Res}_z U_{0,K}
 ={N_K(z)\over D_K'(z)}
 ={2i\lambda
   \bigl(F(z)F^{(K+1)}(z)-F'(z)F^{(K)}(z)\bigr)
  \over D_K'(z)}.
}
\tag{L-106442.11
}

Thus the signed tail is one explicit difference of two positive residue Grams
whose residue vector is the literal endpoint exterior-square source.  There is
no unspecified contour remainder in this normal form.

## 5. Scope

The theorem converts `SIGNEDTAIL106430` and its even-endpoint successors into
an explicit pole-versus-pole residue Gram estimate.  It proves neither the
favorable sign nor the required fixed constant.  Source-blind absolute values
would discard the very cancellation exposed by (L-106442.10).