# R-106131 — The complete Gauss-family atomic ledger carries the full phase cardinality

Claim ID: `R-106131`  
Programme aliases: `LFAM1.GAUSS_ATOMIC_LEDGER`, `LFAM2.CONDUCTOR_DIMENSION_FIREWALL`, `STRESS.FAMILY_NORMALIZATION_REPAIR`  
Status: **PROVED EXACT NORMALIZATION FIREWALL; THE COMPLETE-MOMENT ATOMIC CLAIMS IN `L-106112` AND `L-106121` ARE CORRECTED**  
Created: 2026-08-25  
Depends on: `L-106020`, `L-106110--L-106112`, `L-106120--L-106121`; `R-106123`  
Programme issues: #743, #736, #737  
RH status: **unproved**

The complete one- and two-conductor family identities are correct. Their
atomic-diagonal ledgers were not.

The first diagonal calculations in `L-106112` and `L-106121` inserted the
external source-dual weights `g^2 ell` and `g^2 ell rho`, but omitted the total
weight of all additive phases, equivalently all even-character channels. The
omitted factors are exactly `ell-1` and `(ell-1)(rho-1)`.

All formulas below concern odd prime conductors, the scope of the Gauss identity
`L-106020`. Any fixed prime-2 sector remains in the finite low-prime ledger
and cannot repair an error occurring for every unbounded odd conductor.

## 1. Exact one-prime weight sum

For an odd prime `q`, the complete even-character weights are

\[
 w_q(\mathbf1)=\frac{q+1}{q-1},
 \qquad
 w_q(\eta)=\frac{2q}{q-1}
 \quad
 (\eta\ne\mathbf1,\ \eta(-1)=1).
\]

There are `(q-3)/2` nonprincipal even characters. Hence

\[
\boxed{
 w_q(\mathbf1)
 +\sum_{\substack{\eta(-1)=1\\\eta\ne\mathbf1}}w_q(\eta)
 =q-1.
}
\tag{R-106131.1}
\]

This is also forced by the additive side: one source atom contributes modulus
one to each of the `q-1` nonzero additive phases.

Let

\[
 D=\sum_\omega\|z_\omega\|^2
\]

be the literal atomic diagonal of one complete source member. Then

\[
\boxed{
 \sum_{h=1}^{q-1}|Z_h|^2
 \quad\hbox{has atomic part}\quad
 (q-1)D.
}
\tag{R-106131.2}
\]

The principal/quadratic-root channel contributes only

\[
\boxed{
 \frac{q+1}{q-1}D,
}
\tag{R-106131.3}
\]

while the complete nonprincipal channel contributes

\[
\boxed{
 \nu_qD,
 \qquad
 \nu_q
 =q-1-\frac{q+1}{q-1}
 =\frac{q(q-3)}{q-1}.
}
\tag{R-106131.4}
\]

Thus almost all of the atomic conductor dimension lies in the uncentered
nonprincipal moment.

## 2. Correction to the one-conductor moment

For the source atom of `L-106112`,

\[
 z_\omega(t)
 =
 \frac{\gamma_\omega(t)}
 {g^2cd\sqrt{PQ}},
\]

the atomic contribution to the **complete** dual-amplified moment of
`L-106111` is

\[
\boxed{
 g^2\ell(\ell-1)|z_\omega(t)|^2,
}
\tag{R-106131.5}
\]

not `g^2 ell |z_omega|^2`.

The calculation in the first `L-106112.2--L-106112.3` is nevertheless valid,
up to the bounded factor `(ell+1)/(ell-1)`, for the
**principal/quadratic-root channel alone**:

\[
 g^2\ell\frac{\ell+1}{\ell-1}|z_\omega(t)|^2.
\tag{R-106131.6}
\]

Consequently:

```text
principal atomic diagonal of DAPRIN106111    retained subpower;
complete M_DA atomic diagonal                not proved there;
uncentered DAFAM/DAKUM atomic diagonal       dimension-bearing.
```

The exact family identity and the implication from a genuinely subpower
complete moment remain valid. Only the claimed unconditional diagonal input
to that moment is corrected.

## 3. Exact bilateral weight sum

For two distinct odd prime conductors,

\[
\boxed{
 \sum_{\eta,\theta}
 w_\ell(\eta)w_\rho(\theta)
 =
 (\ell-1)(\rho-1).
}
\tag{R-106131.7}
\]

Thus one complete bilateral atom contributes

\[
\boxed{
 g^2\ell\rho(\ell-1)(\rho-1)|z_\omega(t)|^2
}
\tag{R-106131.8}
\]

to the full tensor moment of `L-106121`, rather than
`g^2 ell rho |z_omega|^2`.

Put

\[
 c_q=\frac{q+1}{q-1}.
\]

The principal--principal atomic contribution is only

\[
\boxed{
 g^2\ell\rho\,c_\ell c_\rho |z_\omega(t)|^2,
}
\tag{R-106131.9}
\]

and the calculation in the first `L-106121.6--L-106121.8` correctly pays this
principal--principal diagonal because `c_ell c_rho<=4`.

The remaining atomic mass is distributed among the mixed and double
nonprincipal channels:

\[
\begin{aligned}
{\rm PP}:&\quad c_\ell c_\rho,\\
{\rm mixed}:&\quad c_\ell\nu_\rho+\nu_\ell c_\rho,\\
{\rm NN}:&\quad \nu_\ell\nu_\rho.
\end{aligned}
\tag{R-106131.10}
\]

Their sum is `(ell-1)(rho-1)`.

## 4. Why rescaling the family does not repair the ledger

Dividing each additive or character member by `sqrt(q-1)` divides its atomic
diagonal by `q-1`, but recovering the native principal member multiplies the
principal embedding by the same factor. Likewise, any source-dual Cauchy
weight whose reciprocal sum over conductors is subpower reinstates the missing
conductor factor.

Therefore the issue is structural:

```text
positive square of each conductor fibre
  -> conductor-dimensional atomic trace;

coherent source before the conductor square
  -> no such trace, but no positive fibre decomposition.
```

This is the same local-fibre/global-family distinction isolated by
`R-106123`.

## 5. Binding consequence

```text
L-106110 and L-106120 family identities                    RETAINED EXACT
L-106111 and L-106121 conditional source domination        RETAINED EXACT
L-106112 owner Wick factorization                           RETAINED EXACT
L-106121 bilateral owner Wick factorization                 RETAINED EXACT

first L-106112 complete atomic-diagonal claim               CORRECTED TO PRINCIPAL ONLY
first L-106121 complete tensor atomic-diagonal claim         CORRECTED TO PP ONLY
unmodified uncentered DAFAM/DAKUM diagonal                  OPEN / DIMENSION-BEARING
unmodified uncentered mixed and NN tensor diagonals         OPEN / DIMENSION-BEARING
```

The correct way to keep the useful family decomposition without charging the
already-closed literal diagonal once for every character is exact Wick
normal ordering. That identity is `L-106131`; the repaired implication matrix
is `T-106140`.

This refutation does not prove that any particular uncentered nonprincipal
moment has a power lower bound for the full arithmetic source. It proves that
the published subpower atomic-diagonal arguments do not apply to those moments
and identifies the exact omitted factor.
