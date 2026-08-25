# L-106110 — All opposite-owner fibres must be amplified before the Gauss square

Claim ID: `L-106110`  
Programme aliases: `LFAM1.DUAL_AMPLIFIED_ROUGH_TAIL`, `LFAM2.ALL_Q_GAUSS_MEMBER`, `STRESS.TWO_SIDED_SOURCE_AMPLIFICATION`  
Status: **PROVED EXACT LINEAR/FAMILY IDENTITY**  
Created: 2026-08-25  
Depends on: `L-106090--L-106093`; `R-106110`; `L-106020`, `L-106027`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Retain the exact least-discrepancy orientation after common-core extraction:

\[
 N=P g^2c^2,
 \qquad
 M=Q g^2d^2,
 \qquad
 (c,d)=1,
 \qquad
 \ell=P^-(c)<P^-(d).
\]

For every clean term, `ell` divides `N` and does not divide `M`; the reduced
opposite core `d` is strictly `ell`-rough.  Let

\[
 Z_{g,\ell,Q,\sigma,h}(t)
\]

be the Q-fixed, left-anchor-amplified scalar field of `L-106093`, with

\[
 \sigma=\kappa_\ell(Q)\in\{+1,-1\},
 \qquad 1\le h<\ell.
\]

Every literal owner, core, shell, carrier, marked-67, Boolean-factorization and
renewal coefficient remains inside this scalar.  In particular the physical
coefficient `Q^{-1/2}` is not removed.

## 1. Dual amplification

Define the complete opposite-owner-amplified member

\[
\boxed{
 \mathcal Z_{g,\ell,\sigma,h}(t)
 =
 \sum_{\substack{Q\\(Q,67\ell)=1\\
                  \kappa_\ell(Q)=\sigma}}
 Z_{g,\ell,Q,\sigma,h}(t).
}
\tag{L-106110.1}
\]

The sum is taken over the literal source fibres before any norm or square.  It
is finite on every physical horizon.

Because the additive phase and every multiplicative Gauss transform are
linear, summing the `Q` fibres commutes exactly with the complete square-phase
family change of basis.

Choose for each even character `eta` modulo `ell` one square root `chi` with
`chi^2=eta`.  Within one fixed quadratic owner class `sigma`, replacing `chi`
by `chi*kappa_ell` multiplies every owner factor by the same scalar `sigma` and
therefore does not change the squared member.  Put

\[
 \mathcal Z_{g,\ell,\sigma,\eta}(t)
 =
 \sum_{\alpha,Q,d}
 \overline{A_\alpha(t)}\,
 B_{\alpha,Q,d}(t)\,
 \chi(Q)\eta(d),
\tag{L-106110.2}
\]

where the sum has exactly the same incidence restrictions as
(L-106110.1).  For `eta=1`, this is the literal untwisted rough-tail amplitude
(up to the constant quadratic-root sign on the `sigma` sector).

## 2. Exact complete-family identity

Applying `L-106020` after the complete `Q` and anchor sums gives

\[
\boxed{
\begin{aligned}
 \sum_{h=1}^{\ell-1}
 |\mathcal Z_{g,\ell,\sigma,h}(t)|^2
={}&
 {\ell+1\over\ell-1}
 |\mathcal Z_{g,\ell,\sigma,1}(t)|^2\\
&+{2\ell\over\ell-1}
 \sum_{\substack{\eta(-1)=1\\\eta\ne1}}
 |\mathcal Z_{g,\ell,\sigma,\eta}(t)|^2.
\end{aligned}
}
\tag{L-106110.3}
\]

No `Q`-dependent weight appears outside the square.  Both sides are
homogeneous of degree two in the complete physical source.

## 3. Exact principal recombination

For every term in the `sigma` sector,

\[
 \sum_{h=1}^{\ell-1}e_\ell(hM)=-1,
\]

because `ell` does not divide `M`.  Hence termwise and therefore after both
amplifications,

\[
\boxed{
 \sum_{h=1}^{\ell-1}
 \mathcal Z_{g,\ell,\sigma,h}(t)
 =-\mathcal Z_{g,\ell,\sigma,0}(t).
}
\tag{L-106110.4}
\]

The principal member in (L-106110.3) is exactly this unphased amplitude.  The
sharp embedding is

\[
\boxed{
 |\mathcal Z_{g,\ell,\sigma,0}(t)|^2
 \le {\ell-1\over\ell+1}
 \sum_{h=1}^{\ell-1}
 |\mathcal Z_{g,\ell,\sigma,h}(t)|^2.
}
\tag{L-106110.5}
\]

Thus the native principal rough-tail current is embedded with no conductor or
opposite-owner dimension loss.

## 4. Exact source-order statement

The legal order is

```text
complete left-anchor sum
  AND complete opposite-owner sum
  -> one additive family member
  -> Gauss/even-character decomposition
  -> one square.
```

Either order

```text
square at fixed anchor;
square at fixed Q;
```

can create a nonphysical fibre count.  Equation (L-106110.3) is the exact
source-faithful replacement.

## Scope

This theorem proves the dual-amplified family identity and principal
individualization.  It does not estimate the resulting hybrid moment.  The
natural source-dual moment and its implication to the Boolean incidence
current are `L-106111` and `T-106110`.
