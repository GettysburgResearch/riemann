# T-107301 — Complete deep nonresonant function-field fibres are closed without family-size loss

Claim ID: `T-107301`  
Programme aliases: `LFAM2.DEEP_SHARED_FIBRE_CLOSURE`, `RIEMANNSTRUCT.TWISTED_PLANCHEREL_EXPORT`  
Status: **PROVED FUNCTION-FIELD SECTOR CLOSURE; INCOMPLETE BOUNDARY AND RESONANCES OPEN**  
Created: 2026-08-30  
Depends on: `L-106213` at PR #751 head `86cac1d64364015ec2cc0f8fbb6fc75dc041c12b`; `L-107301--L-107304`; `R-107301`  
Programme issues: #763, #737, #739  
Number-field RH status: **not assumed; no transfer claimed**

Let \(\mathfrak l\) be an irreducible conductor of degree \(m\) over
\(\mathbf F_q[T]\), and let \(X_{\mathfrak l}\) be its unit squareclass group.
For a complete normalized reduced-core shell of degree \(n\), define the
residue distribution

\[
B_{\mathfrak l,n}(y)
=
\sum_{\substack{d\ {m monic}\\deg d=n\[1mm][d]=y}}
rac{h(d)}{|d|},
	ag{T-107301.1}
\]

where \(h\) is the Boolean half-source coefficient of PR #751 and the clean
condition removes the conductor prime.

For every multiplicative character \(\psi\) on the squareclass group,

\[
oxed{
\widehat B_{\mathfrak l,n}(\psi)
=q^{-n}H_{\overline\psi,n},
}
	ag{T-107301.2}
\]

with \(H_{\psi,n}\) as in `L-106213`.

Put

\[
C_{m,q}=\max_{\substack{\psi\ {m primitive}\\psi
e1}}C_{\psi,q},
\qquad r_\psi\le m-1.
\]

Then `L-106213` and `L-107304` give the rank-free operator estimate

\[
oxed{
\|T_{B_{\mathfrak l,n}}^{m nr}\|_{2	o2}
\le
C_{m,q}(n+1)^{(m-1)/2+2}q^{-n/2}.
}
	ag{T-107301.3}
\]

No factor \(q^m\), \(arphi(\mathfrak l)\), or augmentation rank appears.
This improves the complete-family estimate by diagonalizing the physical
squareclass convolution before summing characters.

If

\[
oxed{
\log_q C_{m,q}
+\left(rac{m-1}{2}+2ight)\log_q(n+1)
\lerac n4,
}
	ag{T-107301.4}
\]

then

\[
oxed{
\|T_{B_{\mathfrak l,n}}^{m nr}\|_{2	o2}\le q^{-n/4}.
}
	ag{T-107301.5}
\]

For two shared conductors and complete core degrees \(n_\ell,n_ho\), the
nonresonant physical pushforward therefore has norm at most

\[
oxed{q^{-(n_\ell+n_ho)/4}}
	ag{T-107301.6}
\]

whenever the two instances of (T-107301.4) hold. Thus every complete deep
nonresonant shared-conductor fibre is unconditionally closed in the
function-field model.

## Remaining exact gates

Define:

```text
LIVEBOUND107301:
  complete the live Boolean/Wick shell and all joint incidence masks to the
  rank-free twisted-convolution fibre, with the signed completion boundary
  having subpower trace/energy;

QRESBIND107300:
  control the explicit quadratic-resonant rows and bind the principal member.
```

Then the function-field route has no other local obstruction.

For the number-field RH route, the conditional chain remains

\[
oxed{
\mathrm{LIVEBOUND}_{107301}
\wedge
\mathrm{QRESBIND}_{107300}
\Longrightarrow
\mathrm{CBKM}_{106130}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
	ag{T-107301.7}
\]

The first two statements are open over the integers. No function-field result
is promoted to a number-field theorem.

```text
complete squareclass Plancherel                 PROVED EXACT
rank-free nonresonant operator norm             PROVED EXACT
complete deep FF nonresonant sector             PROVED
family-size q^m tax at complete scope            REMOVED
LIVEBOUND107301                                  OPEN
quadratic/principal binding                      OPEN
Riemann Hypothesis                              UNPROVED
```
