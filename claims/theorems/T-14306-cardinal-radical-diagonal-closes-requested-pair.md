# T-14306 — Exact localized cardinal–radical packets close the two cofinal limits

Claim ID: `T-14306`  
Title: Finite-section cardinal repair and radical graph correction give a cofinal zero-kernel floor with Schur-small loss  
Status: `PROPOSED — COMPLETE ABSTRACT PROOF; COMPLETE-LOW-PACKET CAPTURE IS A SEPARATE GATE`  
Authoring agent: `gpt56-pro-09-c`  
Created: 2026-07-31  
Dependencies: `L-14321`; the exact global radical packets of `L-15303`; the radical identity of `L-14309`; the complete complement floor of `L-14313`; elementary Neumann-series and Schur-complement algebra  
Scope: the two limits requested after `L-14321`

## 1. The two requested quantities

Let `P_L` be localization to logarithmic support `[-L,L]`.  For a finite set
`Z` of certified simple real zeros, let

\[
 C_Z:\ell^2(Z)\longrightarrow X
\]

be the exact Xi-cardinal synthesis of `L-14321`, and let

\[
 V_Z:X\longrightarrow\ell^2(Z)
\]

be evaluation at those zeros.  Thus

\[
 V_ZC_Z=I.                                               \tag{T-14306.1}
\]

The first requested quantity is

\[
 c_Z(L):=\|(I-P_L)C_Z\|_{\ell^2\to X_L}.                \tag{T-14306.2}
\]

The second requested quantity concerns a finite supported packet `U_L` and its
exact selected-zero kernel

\[
 U_L^0:=U_L\cap\ker V_Z.                                 \tag{T-14306.3}
\]

The purpose of this theorem is to construct `U_L` so that

\[
 c_Z(L)\to0                                              \tag{T-14306.4}
\]

at a Schur-sufficient rate and

\[
 \inf_{0\ne f\in U_L^0}
 \frac{Q_W(f,f)}{\|f\|_{G_L}^2}
 \ge-\varepsilon_L,
 \qquad \varepsilon_L\to0.                              \tag{T-14306.5}
\]

The construction is exact at every finite level; it does not rely on a
floating principal angle.

## 2. Fixed finite data and continuity hypotheses

Fix one finite zero set `Z` and one finite exact global radical packet

\[
 R_m:\mathbb C^m\longrightarrow X.                       \tag{T-14306.6}
\]

Assume:

1. `V_Z` is bounded from `X` to `ell^2(Z)`, with norm `v_Z`;
2. the polarized Weil form is continuous on the finite tail-control space,
   \[
   |Q_W(x,y)|\le q_X\|x\|_X\|y\|_X;                     \tag{T-14306.7}
   \]
3. `R_m` is an exact global radical packet,
   \[
   Q_W(R_mb,x)=0
   \quad\text{for every admissible }x;                   \tag{T-14306.8}
   \]
4. the finite packet has a positive limiting metric Gram: for one `s_m>0`,
   \[
   \|R_mb\|_{G_\infty}\ge s_m\|b\|_2;                  \tag{T-14306.9}
   \]
5. its localization tail tends to zero,
   \[
   r_m(L):=\|(I-P_L)R_m\|_{\ell^2\to X_L}\to0.          \tag{T-14306.10}
   \]

All five conditions hold for every fixed Xi-cardinal packet and every fixed
Hermite `E`-radical packet in the current stack.  Uniformity in `m` or `|Z|` is
not assumed.

## 3. Exact finite-section cardinal repair

Define the finite evaluation defect matrix

\[
 A_{Z,L}:=V_ZP_LC_Z.                                     \tag{T-14306.11}
\]

By (T-14306.1),

\[
 A_{Z,L}
 =I-V_Z(I-P_L)C_Z,                                       \tag{T-14306.12}
\]

and therefore

\[
 \|I-A_{Z,L}\|\le v_Zc_Z(L).                            \tag{T-14306.13}
\]

Whenever

\[
 v_Zc_Z(L)<1,                                            \tag{T-14306.14}
\]

`A_(Z,L)` is invertible and

\[
 \|A_{Z,L}^{-1}\|
 \le\frac1{1-v_Zc_Z(L)}.                                \tag{T-14306.15}
\]

Define the **exact supported cardinal synthesis**

\[
 \boxed{
 \widetilde C_{Z,L}
 :=P_LC_ZA_{Z,L}^{-1}.}                                  \tag{T-14306.16}
\]

Then

\[
 \boxed{V_Z\widetilde C_{Z,L}=I}                         \tag{T-14306.17}
\]

exactly.  Put

\[
 \Delta C_{Z,L}:=\widetilde C_{Z,L}-C_Z.                 \tag{T-14306.18}
\]

Since both synthesis maps interpolate the same values,

\[
 \boxed{V_Z\Delta C_{Z,L}=0.}                            \tag{T-14306.19}
\]

If `p_Z=||C_Z||_(ell2->X)` and localization is contractive on the finite
packet, then

\[
 \boxed{
 \|\Delta C_{Z,L}\|
 \le
 c_Z(L)
 +\frac{(p_Z+c_Z(L))v_Zc_Z(L)}{1-v_Zc_Z(L)}
 =:\widehat c_Z(L).}                                     \tag{T-14306.20}
\]

In particular,

\[
 \widehat c_Z(L)=O_Z(c_Z(L))\to0.                        \tag{T-14306.21}
\]

The same conclusion holds without global contractivity by replacing `p_Z` by
the finite bound `sup_L ||P_LC_Z||` on the retained cofinal tail.

## 4. Exact zero-kernel repair of the radical packet

The truncated global radical is not exactly in `ker V_Z`.  Its finite evaluation
matrix is

\[
 B_{m,Z,L}:=V_ZP_LR_m.                                   \tag{T-14306.22}
\]

Because every global radical transform vanishes at every zeta zero,

\[
 V_ZR_m=0,
\]

so

\[
 B_{m,Z,L}
 =-V_Z(I-P_L)R_m,
 \qquad
 \|B_{m,Z,L}\|\le v_Zr_m(L).                            \tag{T-14306.23}
\]

Define

\[
 \boxed{
 K_{m,Z,L}
 :=P_LR_m-\widetilde C_{Z,L}B_{m,Z,L}.}                  \tag{T-14306.24}
\]

Then, using (T-14306.17),

\[
 \boxed{V_ZK_{m,Z,L}=0}                                  \tag{T-14306.25}
\]

exactly.  Let

\[
 E_{m,Z,L}:=K_{m,Z,L}-R_m.                               \tag{T-14306.26}
\]

Equations (T-14306.23)--(T-14306.24) give

\[
 \boxed{
 \|E_{m,Z,L}\|_{\ell^2\to X_L}
 \le
 r_m(L)
 \left[
 1+\frac{(p_Z+c_Z(L))v_Z}{1-v_Zc_Z(L)}
 \right]
 =:\eta_{m,Z}(L).}                                       \tag{T-14306.27}
\]

Hence

\[
 \eta_{m,Z}(L)=O_{m,Z}(r_m(L))\to0.                      \tag{T-14306.28}
\]

For all sufficiently large `L`, `K_(m,Z,L)` is injective.  Indeed, convergence
to the injective finite map `R_m` and (T-14306.9) give

\[
 \boxed{
 \|K_{m,Z,L}b\|_{G_L}
 \ge g_{m,Z}(L)\|b\|_2,
 \qquad
 g_{m,Z}(L)\longrightarrow s_m>0.}                      \tag{T-14306.29}
\]

## 5. The supported packet and its exact kernel

Define

\[
 \boxed{
 U_{m,Z,L}
 :=\operatorname{Ran}\widetilde C_{Z,L}
   \oplus
   \operatorname{Ran}K_{m,Z,L}.}                         \tag{T-14306.30}
\]

The sum is direct for large `L`: if

\[
 \widetilde C_{Z,L}a=K_{m,Z,L}b,
\]

then evaluation gives `a=0`, and injectivity of `K_(m,Z,L)` gives `b=0`.
Moreover every vector has the unique form

\[
 f=\widetilde C_{Z,L}a+K_{m,Z,L}b,
 \qquad
 V_Zf=a.                                                  \tag{T-14306.31}
\]

Therefore

\[
 \boxed{
 U_{m,Z,L}\cap\ker V_Z
 =\operatorname{Ran}K_{m,Z,L}.}                          \tag{T-14306.32}
\]

This identity is the reason the second requested infimum becomes an exact
finite estimate rather than a principal-angle assertion.

## 6. Proof of the zero-kernel lower floor

For `f=K_(m,Z,L)b`, write

\[
 f=R_mb+E_{m,Z,L}b.
\]

Radicality (T-14306.8) annihilates the radical diagonal and both cross terms:

\[
 \boxed{
 Q_W(K_{m,Z,L}b,K_{m,Z,L}b)
 =Q_W(E_{m,Z,L}b,E_{m,Z,L}b).}                           \tag{T-14306.33}
\]

By form continuity,

\[
 Q_W(Kb,Kb)
 \ge-q_X\eta_{m,Z}(L)^2\|b\|_2^2.                       \tag{T-14306.34}
\]

Using (T-14306.29),

\[
 \boxed{
 \inf_{\substack{0\ne f\in U_{m,Z,L}\\V_Zf=0}}
 \frac{Q_W(f,f)}{\|f\|_{G_L}^2}
 \ge-\varepsilon_{m,Z}(L),
 \qquad
 \varepsilon_{m,Z}(L)
 :=\frac{q_X\eta_{m,Z}(L)^2}{g_{m,Z}(L)^2}
 \longrightarrow0.}                                     \tag{T-14306.35}
\]

This is precisely the second boxed statement requested by the user.

## 7. Why the cardinal error is automatically quadratic

The exact interpolation repair contains an additional cancellation.  Since
`V_Z Delta C_(Z,L)=0`, the exact Xi-cardinal decomposition of `L-14321` gives

\[
 Q_W(C_Za,\Delta C_{Z,L}b)=0.                             \tag{T-14306.36}
\]

Consequently,

\[
 \boxed{
 Q_W(\widetilde C_{Z,L}a,\widetilde C_{Z,L}b)
 =\langle a,b\rangle
  +Q_W(\Delta C_{Z,L}a,\Delta C_{Z,L}b).}                \tag{T-14306.37}
\]

Thus the localized cardinal diagonal differs from the exact positive identity
by `O(widehat c_Z(L)^2)`, not by a linear tail error.

Similarly, because `R_m` is radical,

\[
 \boxed{
 Q_W(\widetilde C_{Z,L}a,K_{m,Z,L}b)
 =Q_W(\Delta C_{Z,L}a,E_{m,Z,L}b),}                      \tag{T-14306.38}
\]

which is `O(widehat c_Z(L) eta_(m,Z)(L))`.

The complete finite low block is therefore

\[
 \begin{pmatrix}I&0\\0&0\end{pmatrix}
 +O_Q\!\left(
 \begin{pmatrix}
 \widehat c^2&\widehat c\eta\\
 \widehat c\eta&\eta^2
 \end{pmatrix}
 \right).                                                 \tag{T-14306.39}
\]

This quadratic structure is the key rate improvement.

## 8. Schur-sufficient rate

Let `E_L` be an exact selected-zero-kernel complement to `U_(m,Z,L)` and suppose
its positive block satisfies

\[
 Q_W(e,e)\ge h_L\|e\|_{M_L}^2,
 \qquad h_L>0.                                           \tag{T-14306.40}
\]

Assume the cross form is continuous in the tail/control norm:

\[
 |Q_W(x,e)|
 \le q_{XM,L}\|x\|_{X_L}\|e\|_{M_L}.                  \tag{T-14306.41}
\]

For the cardinal row, exact global orthogonality gives

\[
 Q_W(\widetilde C a,e)=Q_W(\Delta C a,e).                \tag{T-14306.42}
\]

For the radical row, exact global radicality gives

\[
 Q_W(Kb,e)=Q_W(Eb,e).                                    \tag{T-14306.43}
\]

Hence the complete row into the positive complement has squared dual norm at
most

\[
 q_{XM,L}^2
 \bigl(\widehat c_Z(L)+\eta_{m,Z}(L)\bigr)^2             \tag{T-14306.44}
\]

up to the finite packet metric condition number.  The Schur loss is therefore
bounded by

\[
 \boxed{
 \kappa_{m,Z}(L)
 \le
 \frac{q_{XM,L}^2}{h_L\,g_{m,Z}(L)^2}
 \bigl(\widehat c_Z(L)+\eta_{m,Z}(L)\bigr)^2.}           \tag{T-14306.45}
\]

Thus a sufficient strengthening of the first requested limit is

\[
 \boxed{
 \frac{q_{XM,L}^2}{h_L}
 \left\|(I-P_L)C_Z\right\|_{\ell^2\to X_L}^2
 \longrightarrow0,}                                     \tag{T-14306.46}
\]

with the analogous radical-tail term.  This is the exact rate needed by the
block Schur correction.

## 9. Xi-cardinal and Hermite-tail specialization

For every fixed finite `Z`, `L-14321` gives a two-sided Riemann-kernel envelope
for each cardinal function.  In every fixed complete form/graph seminorm there
are finite constants `A_Z,B_Z` such that

\[
 c_Z(L)
 \le A_Ze^{B_ZL}e^{-c e^{2L}}.                           \tag{T-14306.47}
\]

For every fixed finite Hermite radical packet, the Gaussian arithmetic-tail
argument of `L-14312/L-15303` gives the same type of bound

\[
 r_m(L)
 \le A_me^{B_mL}e^{-c_m e^{2L}}.                         \tag{T-14306.48}
\]

The complete multiband complement theorem `L-14313` supplies, on its enlarged
finite packet,

\[
 h_L\ge e^{-L}                                            \tag{T-14306.49}
\]

for the moving Hardy schedule, after harmless adjustment of the initial
support.  Fixed-packet metric and cross-continuity constants grow at most
ordinary exponentially in the support in the declared interfaces.  Therefore

\[
 \boxed{
 \varepsilon_{m,Z}(L)\to0,
 \qquad
 \kappa_{m,Z}(L)\to0}                                    \tag{T-14306.50}
\]

superexponentially.  The inverse factors `1/|Xi'(gamma)|` enter only the finite
constants `A_Z`; no uniform lower bound on Xi derivatives is needed at this
stage.

## 10. Cofinal growing diagonal

Let

\[
 Z_1\subset Z_2\subset\cdots
\]

be any sequence of finite certified simple real-zero sets, and let `m_j` be any
increasing radical-packet ranks.  The constants at level `j` may be arbitrarily
large.  Because all data are finite at fixed `j` and the tails in
(T-14306.47)--(T-14306.48) are superexponential, choose `L_j` inductively so
that

\[
 L_j>L_{j-1},                                             \tag{T-14306.51}
\]

\[
 v_{Z_j}c_{Z_j}(L_j)<\frac12,                            \tag{T-14306.52}
\]

and

\[
 c_{Z_j}(L_j),
 \ \varepsilon_{m_j,Z_j}(L_j),
 \ \kappa_{m_j,Z_j}(L_j)
 \le2^{-j}.                                              \tag{T-14306.53}
\]

Put

\[
 U_j:=U_{m_j,Z_j,L_j},
 \qquad
 P_j:=P_{L_j},
 \qquad
 X_j:=X_{L_j},
 \qquad
 G_j:=G_{L_j}.                                           \tag{T-14306.54}
\]

Then

\[
 \boxed{
 \left\|(I-P_j)C_{Z_j}\right\|_{\ell^2\to X_j}
 \longrightarrow0}                                      \tag{T-14306.55}
\]

with Schur loss tending to zero, and

\[
 \boxed{
 \inf_{\substack{f\in U_j\\V_{Z_j}f=0\\f\ne0}}
 \frac{Q_W(f,f)}{\|f\|_{G_j}^2}
 \ge-\varepsilon_j,
 \qquad
 \varepsilon_j\longrightarrow0.}                       \tag{T-14306.56}
\]

This proves the requested pair on a cofinally growing exact packet.  The
construction works even when the zero-cardinal conditioning and packet rank
have no useful uniform formula: support is chosen after each finite packet.

## 11. Exact scope: what has been proved and what has not

There are two logically different readings of `U_L`.

### Constructed-packet reading

If `U_L` denotes the exact packet (T-14306.30), both requested statements and
the Schur rate are now proved.  This is a genuine theorem, not a conditional
restatement of either limit.

### Prescribed complete-low-packet reading

If `U_L` is instead fixed in advance as the **complete dangerous low-symbol or
negative spectral packet**, the second statement is not a consequence of
cardinal localization.  It is the remaining RH content.

Indeed, under false RH the Weil criterion supplies a compact test direction of
strictly negative form.  Removing any finite selected real-zero coordinates by
the exact projector `R_Z=I-C_ZV_Z` can only decrease the quadratic value:

\[
 Q_W(R_Zf,R_Zf)
 =Q_W(f,f)-\|V_Zf\|_2^2
 \le Q_W(f,f)<0.                                         \tag{T-14306.57}
\]

The first tail limit localizes that negative zero-kernel direction.  Therefore,
for any form-dense complete packet hierarchy, a bound of the form
(T-14306.56) with `epsilon_j->0` excludes every off-line zero and hence implies
RH.  Conversely RH makes the global Weil form nonnegative, so the complete
reading holds with `epsilon=0`.

Thus the complete-packet version is equivalent to the substantive global
positivity problem.  It cannot be obtained from a finite-section Neumann
argument alone.

The remaining bridge to an RH proof is therefore **capture**, not either boxed
limit on the constructed packet: one must prove that the constructed
cardinal–radical packet accounts for the complete dangerous index, for example
through the weighted-deficit trace margin of `L-15612` or the finite visible
Schur saturation of `L-15604`.

## 12. Proof boundary

- Sections 3--10 are exact finite-dimensional and form-continuity arguments.
- The Xi-cardinal and fixed Hermite tail envelopes are inherited from
  `L-14321` and the audited Gaussian-tail stack.
- No uniform lower bound for `|Xi'(gamma)|` is assumed.
- The theorem proves the pair for a cofinally growing packet explicitly built
  from exact cardinal and radical coordinates.
- It does not silently identify that packet with the complete low spectral
  subspace.  Such an identification, or an equivalent capacity saturation,
  remains necessary before invoking `T-14302`.
