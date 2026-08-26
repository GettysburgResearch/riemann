# PR #751 normalization and frontier consolidation

Date: 2026-08-25  
Branch: `research/gpt56-pro/106000-cvxd-lfamily-hybrid-moments`  
Prepared against head: `356fbf29e958e2ea067bfe5ef912b1f68d0334c6`  
Parent scientific source: PR #719 at `ec6635b4c7dcd08fe433b7ae7e1d9a8c9495dfcc`  
Status: **repair packet; independent review required; RH unproved**

## 1. Repository repair

The branch contained two distinct claims using `L-106131`:

- Wick normal ordering and additive/Kummer decomposition;
- connected two-modulus Kummer--Möbius inversion.

The Wick lemma remains canonical `L-106131`, because it is the binding input to
`R-106131` and `T-106140`. The connected identity is moved to `L-106190`.
`T-106130`, `T-106140` and `R-106124` are updated to name the correct claim.

The PR's recorded base commit is an ancestor of the head, but the named parent
branch has since advanced and diverged. This packet does not blindly merge the
moving parent. It records the exact scientific parent SHA so `T-102990` and
its source lineage cannot be silently replaced.

## 2. Atomic normalization repair

For Hilbert-valued atoms with residue coordinates modulo distinct primes
`ell,rho`, `L-106190` proves

\[
 E_{11}=\ell\rho C_{\ell\rho}-\ell C_\ell-\rho C_\rho+T
\]

and therefore

\[
 T=E_{11}+\ell C_\ell+\rho C_\rho-\ell\rho C_{\ell\rho}.
\]

After subtracting atomic diagonals,

\[
 T^\circ=E_{11}^\circ+\ell C_\ell^\circ+
 \rho C_\rho^\circ-\ell\rho C_{\ell\rho}^\circ.
\]

The frame coefficient cancels through

\[
 (\ell-1)(\rho-1)+\ell+\rho-\ell\rho=1.
\]

The negative joint-collision term is essential. Four separate positive bounds
would reintroduce the false conductor-family dimension.

## 3. Exact source-dual additive coordinate

For a bilateral fibre write

\[
 c=\ell u,\qquad d=\rho v,\qquad
 z_\omega={\gamma_\omega\over g^2\ell\rho uv\sqrt{PQ}}.
\]

`L-106191` defines

\[
 \widetilde z_\omega=g\ell\rho z_\omega
 ={\gamma_\omega\over guv\sqrt{PQ}}
\]

and proves that the complete Wick-centered additive fibre is exactly

\[
\sum_{\omega\ne\omega'}
 \widetilde z_\omega\overline{\widetilde z_{\omega'}}
 \left(\mathbf1_{x_\omega=x_{\omega'}}-{1\over\ell}\right)
 \left(\mathbf1_{y_\omega=y_{\omega'}}-{1\over\rho}\right).
\]

This yields an exact equivalent gate

```text
WCCORR106191 <=> WCADD106140.
```

The two centered incidence factors are bounded by one, and the literal atomic
diagonal is absent coefficientwise.

## 4. The overreach that was rejected before push

The rescaled coefficient satisfies only

\[
 |\widetilde z_\omega|^2
 \ll Y^{o(1)}(g^2u^2v^2PQ)^{-1}.
\]

For prime reduced cores `c=ell,d=rho`, one has `u=v=1`; the coefficient then
has no decay in either conductor. Since power-many conductor pairs are
compatible with the live family (`R-106123`), the global rescaled source energy
is not automatically subpower.

Accordingly this packet does **not** claim that equal-product or
source-blind free energy closes `WCADD`. It records the exact split

\[
 \mathfrak C_{\rm SD}=\mathfrak C_{\rm EQ}+\mathfrak C_{\rm DIST}
\]

and the stronger sufficient diagnostics

```text
WCEQ106191 AND WCDIST106191 -> WCCORR106191 = WCADD106140.
```

Both diagnostics remain open. Cancellation between them remains allowed in
the canonical `WCADD/WCCORR` gate.

## 5. Consolidated implication graph

```text
minimal principal route:
  CBKM106130
    -> M_CK(Y)=Y^o(1)
    -> BCI102990
    -> RH

complete-family route:
  WCCORR106191 (= WCADD106140)
    AND WCKUM106140
      -> principal moment = Y^o(1)
      -> M_CK(Y)=Y^o(1)
      -> BCI102990
      -> RH

exact Boolean/Wick half-source route:
  WKSFSC106150
    -> BCI102990
    -> RH

ordinary reflection route:
  REFSIG106150 <=> SFSC106150
    -> WKSFSC106150
    -> BCI102990
    -> RH
```

Binding `R-106150` corrects the first ordinary analytic-square formulation:
the exact Boolean source is a normal-ordered/Wick square. Ordinary Mellin
self-convolution remains sufficient only modulo the parent's closed
repeated-label contraction ledger.

No equivalence is asserted between `CBKM106130`, the family conjunction, and
the half-source gates. They are separate source-faithful routes to the same
parent consumer.

## 6. Remaining boundary

```text
L-106190 connected two-coordinate inversion       PROVED EXACT
L-106191 source-dual centered correlation          PROVED EXACT
complete-frame atomic multiplicity                 CORRECTED EXACT
principal atomic diagonal                          PROVED SUBPOWER

CBKM106130                                         OPEN
WCCORR106191 = WCADD106140                         OPEN
WCEQ106191 / WCDIST106191                         OPEN DIAGNOSTICS
WCKUM106140                                        OPEN
WKSFSC106150 / SFSC106150 / REFSIG106150          OPEN
BCI102990                                          OPEN
Riemann Hypothesis                                 UNPROVED
```
