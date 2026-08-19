# T-99700 — Canonical scalar/native-source proof spine and the tilted-owner closure contract

Claim ID: `T-99700`  
Status: **UNCONDITIONAL SYNTHESIS + CONDITIONAL RH THEOREM; ONE GLOBAL GATE OPEN**  
Created: 2026-08-20  
Frozen base: PR #653 at `e928fd615d753882706bb88c51b717bd8d4a86ba`  
RH status: **unproved**

## 1. Exact scalar consumer

Define

\[
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1},
\qquad
\beta(n)=\mu(n)-\mathbf1_{67\mid n}\mu(n/67),
\]

and

\[
h(x)=\sum_{n\le x}\frac{\beta(n)}{\sqrt n}T(x/n).
\]

Then

\[
\widehat h(s)=
\frac{(1-67^{-(s+1/2)})(s+3/2)}
{s(s-1/2)\zeta(s+1/2)}.
\tag{T-99700.1}
\]

Every off-line zeta zero survives, while the continuation is analytic at every
positive real point. By `L-99700`, either an eventually nonnegative zero-free
logarithmic smoothing of `h`, or subpower logarithmic negative mass of `h`,
implies RH.

## 2. Exact native source

For every finite rough-prime state, `L-99701` gives both the sequential
first-owner identity

\[
\prod_i(I-r_iU_i)
=s_kI+\sum_i\lambda_i(I-U_i)
 \prod_{j>i}(I-r_jU_j),
\tag{T-99700.2}
\]

and the symmetric homotopy

\[
\prod_i(I-r_iU_i)
=sI+
\int_0^1\sum_i r_i(I-U_i)
 \prod_{j\ne i}K_{j,t}\,dt.
\tag{T-99700.3}
\]

Both reproduce every native coefficient and cumulative parity. The contracted
alpha-child identity does not.

## 3. Exact tilted owner flow

For `tau>=0`, put

\[
h_\tau(x)=
\sum_{n\le x}\frac{\beta(n)}{n^{\tau+1/2}}T(x/n).
\]

With `g(n)=v_67(n)+1`, `L-99702` proves

\[
T(x)=\sum_{d\le x}
\frac{g(d)}{d^{\tau+1/2}}h_\tau(x/d),
\tag{T-99700.4}
\]

and

\[
\partial_\tau h_\tau(x)
=
\sum_{q\le x}
\frac{\Lambda_g(q)}{q^{\tau+1/2}}
 h_\tau(x/q).
\tag{T-99700.5}
\]

Define

\[
\mathcal W_+(x)=
\int_0^\infty\sum_{q\le x}
\frac{\Lambda_g(q)}{q^{\tau+1/2}}
(h_\tau(x/q))_+\,d\tau.
\]

Then

\[
\boxed{h_-(x)\le[\mathcal W_+(x)-T(x)]_+.}
\tag{T-99700.6}
\]

## 4. The single closure contract

Define

\[
\boxed{
\mathrm{TOCE67}(X):
\quad
\int_1^X[\mathcal W_+(x)-T(x)]_+\frac{dx}{x}
=X^{o(1)}.
}
\tag{T-99700.7}
\]

If `TOCE67` holds, (T-99700.6) gives subpower logarithmic negative mass for
`h`; (T-99700.1) and Landau then give RH. Hence

\[
\boxed{\mathrm{TOCE67}\Longrightarrow\mathrm{RH}.}
\tag{T-99700.8}
\]

The coefficient budget available to attack this contract is

\[
\int_0^\infty
\sum_{2\le n\le X}
\frac{\beta(n)^2}{g(n)n^{1+2\tau}}\,d\tau
\le2+\log\log X.
\tag{T-99700.9}
\]

But `L-99703` proves that the within-chain owner martingale has zero quadratic
variation on squarefree fibres. Thus (T-99700.9) does not by itself imply
(T-99700.7). The missing theorem is specifically a source-root/boundary
Carleson embedding.

## 5. Interfaces removed or fenced

```text
score / all-column capacity / prime-square chain      not used
Volterra anchors and knot ledger                       not used
Hall and RN common-parent tree                         not used by consumer
contracted alpha child = native Euler source           refuted
bounded calibration pays missing native coefficient   refuted
ordinary Doob energy implies parity cancellation       refuted
absolutely positive Euler smoothing                    cancels detector
large-row zero-dependent selection                     replaced by fixed scalar
```

## 6. Scientific verdict

```text
scalar reciprocal-zeta consumer             PROVED
native first-owner identities                PROVED
symmetric native homotopy                    PROVED
tilted renewal and owner flow                PROVED
critical tilt-energy budget                  PROVED
TOCE67 owner-boundary embedding              OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVED
```

This is the most compressed conclusion-complete spine supported by the live
repository. It is not an accepted or completed proof of RH until `TOCE67` is
proved.
