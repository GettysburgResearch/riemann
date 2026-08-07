# L-15433 — Full theta prefix–tail collapse and positive endpoint channel

Claim ID: `L-15433`  
Title: Summing the incomplete-gamma atom split turns every theta boundary–tail cross term into one explicit Volterra primitive and one positive rank-one endpoint channel  
Status: `PROPOSED — COMPLETE THETA/MELLIN IDENTITY; REGULAR TRACE-ZERO TAIL SIGN OPEN`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: the full-theta atom split used by the normalized Volterra model; `L-15422`, `L-15427`, `L-15429`, `M-15408`; Jacobi modularity  
Scope: the complete summed endpoint-prefix plus moving-tail channel, before the remaining trace-zero regular Volterra form  
Related counterexample candidates: none

## 1. Full theta atoms

Use the positive-side Riemann kernel normalization

\[
\Psi(v)=\Phi(v/2),\qquad v\ge0,
\]

and write its absolutely convergent theta-atom expansion in the form

\[
\Psi(v)=\sum_i f_i(v),
\qquad
f_i(v)=a_i e^{\beta_i v-c_i e^v},
\qquad c_i>0.
\tag{L-15433.1}
\]

The coefficients `a_i` may be signed.  Local absolute convergence and the
superexponential tail justify the termwise integrations below first in the
common Mellin half-plane and then by analytic continuation wherever the full
scalar transform is defined.

For

\[
\alpha_i(z)=\beta_i+{iz\over2},
\tag{L-15433.2}
\]

the boundary prefix appearing in the atomwise incomplete-gamma decomposition is

\[
B_i(s,z)
={a_i\over2}c_i^{-\alpha_i(z)}
\int_{c_i}^{c_i e^s}
 y^{\alpha_i(z)-1}e^{-y}\,dy.
\tag{L-15433.3}
\]

Its complementary moving tail is

\[
T_i(s,z)
={a_i\over2}c_i^{-\alpha_i(z)}
\int_{c_i e^s}^{\infty}
 y^{\alpha_i(z)-1}e^{-y}\,dy.
\tag{L-15433.4}
\]

## 2. Eureka: the atom prefixes sum before any Gram is formed

Differentiating (L-15433.3) gives exactly

\[
\partial_s B_i(s,z)
={1\over2}f_i(s)e^{izs/2}.
\tag{L-15433.5}
\]

Since `B_i(0,z)=0`, summing over every theta atom yields

\[
\boxed{
B(s,z):=\sum_iB_i(s,z)
={1\over2}\int_0^s
 \Psi(v)e^{izv/2}\,dv.}
\tag{L-15433.6}
\]

Likewise, summing (L-15433.4) gives

\[
\boxed{
T(s,z):=\sum_iT_i(s,z)
={1\over2}\int_s^\infty
 \Psi(v)e^{izv/2}\,dv.}
\tag{L-15433.7}
\]

Thus the apparently mode-mixing incomplete-gamma prefixes are not an
independent infinite family.  They are the lower and upper pieces of one
ordinary Fourier–Mellin primitive of the full theta kernel.

In particular,

\[
\boxed{
B(s,z)+T(s,z)
={1\over2}\int_0^\infty
 \Psi(v)e^{izv/2}\,dv,}
\tag{L-15433.8}
\]

which is independent of the split point `s`.

## 3. Exact upper/lower Volterra primitives

Let `f` be supported in `[0,L]`, and define

\[
U_f(v)=\int_v^L f(s)\,ds
\quad(0\le v\le L),
\tag{L-15433.9}
\]

\[
L_f(v)=\int_0^{\min(v,L)}f(s)\,ds
\quad(v\ge0),
\tag{L-15433.10}
\]

and

\[
C_f=\int_0^Lf(s)\,ds.
\tag{L-15433.11}
\]

Fubini applied to (L-15433.6) gives

\[
\boxed{
\int_0^LB(s,z)f(s)\,ds
={1\over2}\int_0^L
 \Psi(v)e^{izv/2}U_f(v)\,dv.}
\tag{L-15433.12}
\]

The complementary tail gives

\[
\boxed{
\int_0^LT(s,z)f(s)\,ds
={1\over2}\int_0^\infty
 \Psi(v)e^{izv/2}L_f(v)\,dv.}
\tag{L-15433.13}
\]

Now

\[
U_f(v)+L_f(v)=C_f
\quad(0\le v\le L),
\]

and `L_f(v)=C_f` for `v>L`.  Therefore all four boundary/tail Gram
channels recombine before any estimate:

\[
\boxed{
\int_0^L[B(s,z)+T(s,z)]f(s)\,ds
={C_f\over2}\int_0^\infty
 \Psi(v)e^{izv/2}\,dv.}
\tag{L-15433.14}
\]

On the trace-zero subspace `C_f=0`, the complete summed endpoint channel
cancels exactly.

## 4. The full endpoint branch energy is positive and rank one

For `sigma in {+1,-1}` and `omega>=0`, define the physical prefix and tail
features

\[
b_{\sigma,\omega,f}(v)
={1\over2}\Psi(v)e^{\sigma\omega v/2}
 U_f(v)\mathbf 1_{[0,L]}(v),
\tag{L-15433.15}
\]

\[
t_{\sigma,\omega,f}(v)
={1\over2}\Psi(v)e^{\sigma\omega v/2}L_f(v).
\tag{L-15433.16}
\]

Equations (L-15433.9)--(L-15433.11) give the pointwise identity

\[
\boxed{
b_{\sigma,\omega,f}(v)+t_{\sigma,\omega,f}(v)
={C_f\over2}\Psi(v)e^{\sigma\omega v/2}.}
\tag{L-15433.17}
\]

Hence, for two tests `f,g`, the sum of the boundary Gram, tail Gram, and both
cross Grams is

\[
\boxed{
\left\langle b_{\sigma,\omega,g}+t_{\sigma,\omega,g},
             b_{\sigma,\omega,f}+t_{\sigma,\omega,f}
\right\rangle
={C_f\overline{C_g}\over4}
 \int_0^\infty\Psi(v)^2e^{\sigma\omega v}\,dv.}
\tag{L-15433.18}
\]

Subtracting the minus branch from the plus branch gives

\[
\boxed{
\begin{aligned}
&\left\langle b_{+,\omega,g}+t_{+,\omega,g},
                  b_{+,\omega,f}+t_{+,\omega,f}\right\rangle\\
&\quad-
 \left\langle b_{-,\omega,g}+t_{-,\omega,g},
                  b_{-,\omega,f}+t_{-,\omega,f}\right\rangle\\
&={C_f\overline{C_g}\over2}
 \int_0^\infty\Psi(v)^2\sinh(\omega v)\,dv.
\end{aligned}}
\tag{L-15433.19}
\]

The scalar coefficient is nonnegative.  Thus the complete endpoint channel is
an explicit positive rank-one form.  No boundary–tail cross term remains to be
bounded separately.

This is the full-theta analogue of the singular Cauchy-to-trace transmutation in
`L-15427`: the singular and regular prefixes are coordinates of one endpoint
trace, not losses to be charged against the Volterra tail.

## 5. Jacobi modular normalization and the exact endpoint constant

Define

\[
\mathcal B(t)
=e^{t/2}\sum_{n\ge1}e^{-\pi n^2e^{2t}}.
\tag{L-15433.20}
\]

Jacobi modularity gives

\[
\boxed{
\mathcal B(t)-\mathcal B(-t)=-\sinh(t/2).}
\tag{L-15433.21}
\]

Therefore

\[
\boxed{\mathcal B'(0)=-{1\over4}.}
\tag{L-15433.22}
\]

In the normalization of the original Riemann kernel,

\[
\boxed{
\Phi(t)=\left(\partial_t^2-{1\over4}\right)\mathcal B(t).}
\tag{L-15433.23}
\]

The odd modular defect in (L-15433.21) is annihilated by this operator, which
makes the evenness of `Phi` automatic.

For every `L>0`, two integrations by parts give

\[
\boxed{
\begin{aligned}
\int_0^L\Phi(t)e^{izt}\,dt
={}&e^{izL}[\mathcal B'(L)-iz\mathcal B(L)]\\
&+{1\over4}+iz\mathcal B(0)\\
&-(z^2+1/4)\int_0^L\mathcal B(t)e^{izt}\,dt.
\end{aligned}}
\tag{L-15433.24}
\]

The complementary tail is

\[
\boxed{
\begin{aligned}
\int_L^\infty\Phi(t)e^{izt}\,dt
={}&-e^{izL}[\mathcal B'(L)-iz\mathcal B(L)]\\
&-(z^2+1/4)\int_L^\infty\mathcal B(t)e^{izt}\,dt.
\end{aligned}}
\tag{L-15433.25}
\]

The moving endpoint terms cancel exactly in their sum.  The surviving fixed
constant `1/4` is forced by modularity, rather than selected by a numerical
normalization.

## 6. Consequence for the full RH attack

The endpoint/prefix problem in `M-15408` is closed at the level of the complete
summed theta channel:

```text
all atom prefixes + all atom tails + all four cross Grams
    = one positive rank-one endpoint trace.
```

Accordingly, a proof of the original `K_0`/Loewner positivity cannot fail in a
hidden incomplete-gamma prefix or a missing boundary cross term.  After the
rank-one trace is separated, the only surviving RH-bearing object in this
route is the trace-zero regular Volterra form.

This materially sharpens the target but does not prove that regular form
positive.  In particular, it does not imply `K_0>=0`, the physical metric
identity of `L-15423`, or RH.

## 7. Proof boundary

- Equations (L-15433.5)--(L-15433.19) are exact Fubini and incomplete-gamma
  identities in the full theta model.
- Equations (L-15433.21)--(L-15433.25) are exact consequences of Jacobi
  modularity and integration by parts.
- The positive rank-one statement concerns the complete endpoint trace channel;
  it must not be substituted for the remaining trace-zero regular tail.
- The next theorem must control that regular tail in the original physical
  metric, not merely in an isomorphic quotient norm.
