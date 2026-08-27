# M-105416 — Hostile review contract for the oriented phase / anchor-flow frontier

Claim ID: `M-105416`  
Status: **REVIEW PROTOCOL**  
Created: 2026-08-24  
RH status: **unproved**

## Required review order

1. Verify the alpha sign convention

   ```text
   E_alpha=F'-alpha F,
   M_alpha=E_alpha/E_(-alpha),
   d_alpha log M_alpha|_0=-2F/F'.
   ```

2. In the even case, verify the central branch factor

   ```text
   M_alpha^sharp
     = M_alpha (z-c_(-alpha))/(z-c_alpha)
   ```

   and the tangent `-2(F/F'-rho_0/z)`.
3. Differentiate the meromorphic primitive `Psi_(q,a)` and check every power
   and denominator.
4. Recompute separately:

   ```text
   anchor residue       = q^T A q;
   noncentral zero flow = -q^T C q;
   total contour flow   = q^T(A-C)q.
   ```

5. Verify that the outer-phase maximum-principle theorem assumes all critical
   poles real and nonpositive-residue before it is invoked.
6. Check the small pole semicircles, cofinal outer-boundary lower bound and
   strong minimum-principle step.
7. Confirm that the resulting Herglotz representation has a nonnegative affine
   coefficient and positive paired Stieltjes atoms.
8. Retain all multiplicity/common-zero and canonical-exhaustion interfaces of
   `T-105220`.

## Load-bearing signs

At a simple critical point,

\[
c_\alpha'(0)=\rho_c.
\]

For a pair `+-c` and an even inverse-power test,

\[
2\rho_cK(c)=-W_cs_c^aq(s_c)^2.
\]

Thus the oriented noncentral zero motion is **negative critical consumption**.
The source anchor must be added before it becomes the boundary reserve.

On the outer boundary,

\[
\partial_\alpha\arg M_\alpha^\sharp|_0
=-2\operatorname{Im}\widehat m_F.
\]

The desired phase velocity is nonpositive.

## Scope firewall

The following implications are not claimed:

```text
finite shifted-zero samples -> OPG105417;
source coefficient sign alone -> OPG105417;
terminal high-derivative phase -> low-order phase without transport;
CRVH105330 alone -> BRP105220;
SOPV105416 already proved for Xi.
```

The exact achievement is the identification and scalar harmonic reduction.
The Xi phase estimate and the complete critical sign remain open.

## Replay boundary

The exact replay uses rational polynomial fixtures. It authenticates:

- odd anchor plus zero-flow decomposition;
- even central regularization;
- polynomial-square primitive powers;
- shifted critical velocities;
- exact polynomial outer remainders.

It does not evaluate Xi, authenticate the moving saddle, prove a cofinal outer
phase sign, perform low-order descent, or prove RH.

## Scientific boundary

```text
anchor-renormalized spectral-flow identity       PROVED EXACT
signed-pole harmonic reduction                   PROVED EXACT
ZCAP as first oriented-flow test                 PROVED EXACT
all-packet boundary gate as scalar outer phase   PROVED UNDER CRVH
CRVH105330                                       OPEN
SOPV105416 / OPG105417                           OPEN
Riemann Hypothesis                               UNPROVEN
```