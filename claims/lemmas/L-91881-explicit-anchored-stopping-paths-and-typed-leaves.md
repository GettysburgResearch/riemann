# L-91881 — The anchored finite source has explicit stopped paths and typed Target-Lorenz leaves

Claim ID: `L-91881`  
Status: **CANDIDATE-COMPLETE ANCHORED COMPILER ON FROZEN STOPPING/AVLT INPUTS — REVIEW REQUIRED**  
Created: 2026-08-16  
Inputs: `L-91362`, `L-91688`, `L-93782`, `L-93783`; review PR #504  
RH status: **unproved**

This theorem supplies the objects that review #504 found missing: the initial native occurrence, the map into the stopping tree, the path weight, the complete owner label and the typed leaf packet.

## 1. Initial anchored occurrence

An initial occurrence is

\[
\alpha=(m,k,\varepsilon),\qquad a_\alpha=\frac1{\sqrt{km}}\log\frac{X}{km},\qquad \varepsilon=\mu(k).
\]

Its coefficient is positive; parity is a label.

## 2. Deterministic stopping tree

Apply the exact `P_61` stopping-line identity to the paired source packet before physical observation. At a node with endpoint `Y`, the outgoing terms are:

```text
the complete finite P61 forcing at Y;
for each d|P61 and least rough prime p>=67 with dp<=Y,
the child at Y/(dp), coefficient (dp)^(-1/2),
and tail-prime index p+.
```

Repeat on each nonterminal child. Endpoint size drops by at least `67` at every rough step, so every path is finite.

A terminal path is

\[
\omega=(m;k;d_0,p_1,d_1,\ldots,p_r,d_r;\varepsilon;c),
\]

with path coefficient

\[
\boxed{\omega_X=a_\alpha\prod_{h=1}^r(d_hp_h)^{-1/2}\prod_{h=0}^r\kappa_h(c_h).}
\tag{L-91881.1}
\]

Each `kappa_h` is the exact nonnegative stopping/causal branch coefficient declared at that node. The product contains every arithmetic coefficient once.

The complete owner label is

```text
anchored cell m;
initial native colour k and parity;
ordered rough history;
unique first rough owner;
P61 divisor at each node;
current/child path;
terminal leaf type.
```

## 3. Terminal finite leaf

At a terminal one-prime leaf, let `E_omega,O_omega` be the complete even and odd positive source packets. Let `u_(omega,e)` be the literal Target-Lorenz coefficients from `L-93783`:

\[
0\le u_{\omega,e}\le1,\qquad \sum_eu_{\omega,e}T_\omega(e)=T_\omega(O).
\]

Use the same coefficients in target, declared score and every component row. Define

\[
U_\omega=\sum_eu_{\omega,e}E_{\omega,e},\qquad \nu_\omega=E_\omega-U_\omega,
\]

\[
B_\omega=R(U_\omega)-R(O_\omega)\ge0,\qquad \sigma_\omega=S(O_\omega)-S(U_\omega)\ge0.
\]

The typed leaf is

\[
\boxed{G_\omega=(\nu_\omega;B_\omega;\sigma_\omega).}
\tag{L-91881.2}
\]

Its exact identities are

\[
T(\nu_\omega)=T(E_\omega)-T(O_\omega),
\]

\[
S(\nu_\omega)=S(E_\omega)-S(O_\omega)+\sigma_\omega,
\]

\[
R(\nu_\omega)+B_\omega=R(E_\omega)-R(O_\omega).
\]

`B_omega` is a current-only physical row with zero source target. It is never sent to a child.

For a terminal root leaf with no rough owner, use the factor-67 root Hall in the same two-sorted form: target-bearing residual source plus a current-only row bonus. Declared score is superordinate, not forced to an impossible target-null positive equality packet.

## 4. Incidence ownership

At every terminal leaf choose any positive incidence coupling whose negative marginal is the complete odd target measure and whose positive marginal is `U_omega`. Then

\[
(\Pi_\omega)_-=O_\omega,\qquad (\Pi_\omega)_+ + \nu_\omega=E_\omega.
\tag{L-91881.3}
\]

Summing (L-91881.3) with the exact path weights (L-91881.1) reconstructs the anchored finite native marginals. Every native occurrence, rough first owner, leaf residual and current row bonus has exactly one owner.

## 5. Actual physical placement

The residual row and bonus are placed at the parent by the exact same-index composition of the path placements. The scalar `omega_X` is applied once, at the entrance to that placement. It is not reapplied by the quantizer or native capacity ledger.

The anchored target is already finite. Its physical quantizer is the identity.

## 6. PR #503 firewall

The infinitesimal row `p_s` is absent from the anchored stopping tree. In particular the witness `(67,15,1005,14)` is compiled through (L-91881.2), not through

\[
p_{1005}(14)-67^{-1/2}p_{15}(14).
\]

```text
initial anchored coefficients        explicit
stopping recursion                   explicit
path weights                         explicit
first owners                         explicit
typed Target-Lorenz leaf             exact on frozen AVLT
synthetic leaf fixture               not used
infinitesimal causal generator       excluded
```