# L-33803 — Centered-interval physical fields are predecessor carry rows

Claim ID: `L-33803`  
Title: Every centered-interval physical field at an integer endpoint is exactly one predecessor carry row plus one endpoint coefficient; for the Q=4 Jordan family this places the bare source, current, second current, and reflected product curvature in the same finite row coordinates  
Status: **PROPOSED COMPLETE EXACT FINITE/PHYSICAL PLACEMENT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #339 `L-33802`; PR #337 `L-32710/L-32711`; elementary floor arithmetic  
Scope: exact centered-interval / carry-row placement and polarization; no sign estimate, recurrence, or RH conclusion

## 1. Prefix field and discrete additive defect

Let `c` be any finitely supported real or complex arithmetic sequence and extend its prefix to real arguments by

\[
 C(x)=\sum_{m\le x}c(m),\qquad x\ge0,
\]

with `C(x)=0` for `0<=x<1`.

For an integer endpoint `N>=2` define the unnormalized centered-interval field

\[
 \boxed{
 \mathcal U_c(N,\theta)
 =C(N)-C(N\theta)-C(N(1-\theta)),
 \qquad 0\le\theta\le1.
 }
 \tag{L-33803.1}
\]

For an integer parent `M>=1` define the discrete additive defect

\[
 \boxed{
 \mathcal D_c(M,j)
 =C(M)-C(j)-C(M-j),
 \qquad 0\le j\le M.
 }
 \tag{L-33803.2}
\]

The endpoints of the theta cells have measure zero and may be assigned arbitrarily below.

## 2. Exact predecessor-row identity

Fix `0<=j<=N-1` and

\[
 {j\over N}<\theta<{j+1\over N}.
\]

Then

\[
 \lfloor N\theta\rfloor=j,
 \qquad
 \lfloor N(1-\theta)\rfloor=N-j-1.
\]

Therefore

\[
\begin{aligned}
 \mathcal U_c(N,\theta)
 &=C(N)-C(j)-C(N-j-1)\\
 &=c(N)+C(N-1)-C(j)-C((N-1)-j).
\end{aligned}
\]

Hence, almost everywhere on the `j`th theta cell,

\[
 \boxed{
 \mathcal U_c(N,\theta)
 =c(N)+\mathcal D_c(N-1,j).
 }
 \tag{L-33803.3}
\]

This is an equality, not a Riemann-sum approximation.  The one-unit shift from `N` to `N-1` is forced by the complementary floor identity and is the complete endpoint collar.

## 3. Exact bilinear physical/carry placement

Let `d` be a second arithmetic sequence with prefix `D`.  Integrating cell by cell gives

\[
 \boxed{
 \begin{aligned}
 &\int_0^1
 \mathcal U_c(N,\theta)
 \overline{\mathcal U_d(N,\theta)}\,d\theta\\
 &\qquad={1\over N}
 \sum_{j=0}^{N-1}
 [c(N)+\mathcal D_c(N-1,j)]
 \overline{[d(N)+\mathcal D_d(N-1,j)]}.
 \end{aligned}
 }
 \tag{L-33803.4}
\]

If the critical physical normalization is

\[
 \mathcal P_c(N,\theta)=N^{-1/2}\mathcal U_c(N,\theta),
\]

then

\[
 \boxed{
 \langle\mathcal P_c,\mathcal P_d\rangle_{\theta}
 ={1\over N^2}
 \sum_{j=0}^{N-1}
 [c(N)+\mathcal D_c(N-1,j)]
 \overline{[d(N)+\mathcal D_d(N-1,j)]}.
 }
 \tag{L-33803.5}
\]

Thus the continuous carry-position bilinear form at an integer endpoint is a finite normalized predecessor-row Gram plus a rank-one endpoint collar.

## 4. Dirichlet source specialization

Let `b` be any arithmetic source and put

\[
 c=\mathbf1*b.
\]

Divisor switching gives

\[
 C(M)=\sum_{q\le M}b(q)\left\lfloor{M\over q}\right\rfloor.
\]

Consequently its additive defect is exactly the carry image of `b`:

\[
 \boxed{
 \mathcal D_{\mathbf1*b}(M,j)
 =\sum_{q\le M}b(q)\chi_{M,q}(j)
 =:\mathcal L_{M,j}(b).
 }
 \tag{L-33803.6}
\]

Equations (L-33803.3)--(L-33803.5) become

\[
 \boxed{
 \mathcal U_{\mathbf1*b}(N,\theta)
 =(\mathbf1*b)(N)+\mathcal L_{N-1,j}(b)
 }
 \tag{L-33803.7}
\]

on the `j`th theta cell.

This is the exact general physical-to-carry placement for a source-convolved centered-interval field.  It retains the source coefficient `b` and creates only the explicit endpoint coefficient `(1*b)(N)`.

## 5. Möbius boundary: physical placement is exactly coefficient one

Take

\[
 b=\mu.
\]

Then

\[
 \mathbf1*\mu=\varepsilon.
\]

For every `N>=2`, the endpoint collar vanishes:

\[
 (\mathbf1*\mu)(N)=0.
\]

Moreover, for parent `N-1`,

\[
 \mathcal L_{N-1,j}(\mu)
 =\begin{cases}
 0,&j=0,N-1,\\
 -1,&1\le j\le N-2.
 \end{cases}
\]

Therefore

\[
 \boxed{
 \int_0^1|\mathcal U_{\varepsilon}(N,\theta)|^2d\theta
 ={N-2\over N}.
 }
 \tag{L-33803.8}
\]

This is exactly the row energy `B_mu(N-1)` of PR #334 `L-32408`, since

\[
 \mathcal B_\mu(N-1)={(N-1)-1\over(N-1)+1}={N-2\over N}.
\]

Hence the previously separate statement

```text
fully synthesized Mobius carry boundary is coefficient-one absorbed
```

has an exact centered-interval physical placement with no unknown transference operator and no asymptotic collar.

## 6. Q=4 Jordan family

Retain PR #339's positive Jordan deformation

\[
 J_{4,\tau}=A_4(s-\tau)/A_4(s)
\]

and source-convolved family

\[
 K_{4,\tau}=b_4*J_{4,\tau}.
\]

Since

\[
 \mathbf1*b_4=e_4,
\]

the physical centered-interval coefficient is exactly

\[
 \boxed{
 c_{4,\tau}=\mathbf1*K_{4,\tau}=e_4*J_{4,\tau},
 }
 \tag{L-33803.9}
\]

which is the finite coefficient family of `L-33802.15`.

For one predecessor row `e=(N-1,j)` put

\[
 k_e(\tau)=\mathcal L_e(K_{4,\tau}).
\]

Then the physical field at the integer endpoint is exactly

\[
 \boxed{
 \mathcal U_{c_{4,\tau}}(N,\theta)
 =c_{4,\tau}(N)+k_e(\tau)
 }
 \tag{L-33803.10}
\]

on the `j`th theta cell.

At `tau=0`, PR #339 / PR #337 give

\[
 K_{4,0}=b_4,
 \qquad
 K'_{4,0}=q_4,
 \qquad
 K''_{4,0}=t_4,
\]

so define the explicit endpoint collars

\[
 \gamma_0(N)=e_4(N),
 \qquad
 \gamma_1(N)=c_4(N)=(e_4*\Lambda_4)(N),
 \qquad
 \gamma_2(N)=(e_4*C_4)(N).
 \tag{L-33803.11}
\]

Using the row coordinates of `L-32711`,

\[
 Y_e=\mathcal L_e(b_4),
 \quad
 Q_e=\mathcal L_e(q_4),
 \quad
 T_e=\mathcal L_e(t_4),
\]

we obtain the simultaneous exact placement

\[
 \boxed{
 \begin{aligned}
 \mathcal U_{c_{4,0}}&=\gamma_0(N)+Y_e,\\
 \partial_\tau\mathcal U_{c_{4,\tau}}|_0
 &=\gamma_1(N)+Q_e,\\
 \partial_\tau^2\mathcal U_{c_{4,\tau}}|_0
 &=\gamma_2(N)+T_e.
 \end{aligned}
 }
 \tag{L-33803.12}
\]

The bare source, RH-sensitive current, and second current therefore live in exactly the same predecessor carry row as the source-bound augmented reserve of `L-32711`.  No source relabeling or quotient approximation remains in this placement.

## 7. Product-source curvature in predecessor-row coordinates

Let

\[
 \mathscr E_N(\tau)
 =\int_0^1|\mathcal P_{c_{4,\tau}}(N,\theta)|^2d\theta.
\]

Equation (L-33803.5) gives

\[
 \mathscr E_N(\tau)
 ={1\over N^2}
 \sum_{j=0}^{N-1}
 |c_{4,\tau}(N)+k_{(N-1,j)}(\tau)|^2.
 \tag{L-33803.13}
\]

Differentiate twice at zero.  All coefficients are real at `tau=0`, hence

\[
 \boxed{
 \begin{aligned}
 \mathscr E_N''(0)
 ={2\over N^2}\sum_{j=0}^{N-1}
 \Big(&[\gamma_1(N)+Q_j]^2\\
 &+[\gamma_0(N)+Y_j][\gamma_2(N)+T_j]\Big),
 \end{aligned}
 }
 \tag{L-33803.14}
\]

where `Y_j,Q_j,T_j` are the Q=4 row coordinates at parent `N-1`.

By `L-33802`, the left side is exactly the localized reflected **product-source block** at this endpoint.  Therefore (L-33803.14) is an explicit finite predecessor-row placement of the product block, including every endpoint collar.

Likewise the localized individual higher-current/bare-source term is

\[
 \boxed{
 2\operatorname{Re}\langle\mathcal P_{t_4},\mathcal P_{b_4}\rangle_	heta
 ={2\over N^2}\sum_{j=0}^{N-1}
 [\gamma_2(N)+T_j][\gamma_0(N)+Y_j].
 }
 \tag{L-33803.15}
\]

Subtracting (L-33803.15) from (L-33803.14) recovers, with no hidden source map,

\[
 \boxed{
 2\|\mathcal P_{q_4}\|_\theta^2
 ={2\over N^2}\sum_{j=0}^{N-1}[\gamma_1(N)+Q_j]^2.
 }
 \tag{L-33803.16}
\]

This is the finite predecessor-row form of the source-convolved reflected identity.

## 8. What this closes

The following placement questions are now exact at integer endpoints:

1. centered-interval physical fields versus carry rows;
2. the fully reconstructed Möbius unweighted boundary;
3. Q=4 bare/current/second-current fields;
4. the source-convolved product-source Jordan curvature;
5. the individual higher-current/bare-source cross term;
6. their subtraction to the true RH-sensitive current square.

The only mismatch is the explicit endpoint collar `gamma_r(N)`, never an unspecified physical operator.

## 9. What remains open

This theorem is a placement theorem, not the missing RH estimate. In particular it does not prove:

1. a sign for `mathscr E_N''(0)`;
2. `|Q_4^phys|^2 <= C S_4`;
3. that the rowwise augmented reserve `R+Q^2-YT` dominates the endpoint-collared physical curvature;
4. a coefficient-one block recurrence;
5. RH.

A future completion can now attack those inequalities directly in the finite predecessor-row coordinates `(Y,Q,T,P,S)` without an additional physical-to-carry transference step.

## 10. Proof boundary

Closed exactly, subject to review:

- the predecessor-row floor identity;
- the general bilinear physical/carry formula;
- the Dirichlet source specialization;
- exact physical placement of the synthesized Möbius boundary;
- simultaneous Q=4 placement of `b_4,q_4,t_4`;
- exact predecessor-row product-curvature formula;
- exact predecessor-row individual-term formula;
- exact current-square subtraction.

Open: every conclusion-producing inequality and RH.
