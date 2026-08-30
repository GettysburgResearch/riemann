# T-108420 — Positive rectangle gluing and pushforward no longer form an independent obstruction

Claim ID: `T-108420`  
Status: **EXACT POSITIVE-SCOPE GLUING THEOREM; ARITHMETIC SPECTRAL ESTIMATE AND RH OPEN**  
Created: 2026-08-31  
Depends on: `T-108410`, `L-108420`, `L-108421`, `R-108420`  
RH/GRH status: **unproved**

Decompose each grouped live shared-conductor fibre into source-authorized
positive rectangular pieces `a`. Let `N_a` be the mass of a piece and let

\[
\mathcal V_{L,a},\qquad\mathcal V_{R,a}
\]

be its one-sided nonprincipal character energies from `L-108412`. Put

\[
N=\sum_aN_a,
\qquad
w_a={N_a\over N},
\]

and let `B_mask` be the exact positive-trace payment for the live completion
boundary.

Define

\[
\boxed{
\mathfrak G_{\rm mix}(X)
=
2\sum_{\iota}
N_\iota
\sqrt{
\sum_{a\subset\iota}
{N_a\over N_\iota}
\left(
\mathcal V_{L,a}+
\mathcal V_{R,a}
\right)
}
+
\mathfrak B_{\rm mask}(X).
}
\tag{T-108420.1}
\]

Name the conclusion-facing premise

```text
FROBMIX108420:
  mathfrak G_mix(X)=X^o(1)
```

at the frozen connected-Kummer normalization.

## 1. Exact implication

`L-108420` proves that squared Hellinger distance is subadditive under
positive source gluing and contractive under deterministic physical
pushforward. `L-108421` therefore gives

\[
\boxed{
\mathrm{FROBMIX}_{108420}
\Longrightarrow
\mathrm{FROBHELL}_{108400}.
}
\tag{T-108420.2}
\]

At this positive-quotient scope the earlier abstract gate

```text
RECTGLUE107300
```

is closed: overlapping rectangular pieces and collisions under the physical
map incur no additional debt beyond the weighted source-piece Hellinger
energies already displayed in (T-108420.1).

## 2. Remaining arithmetic chain

The complete number-field chain is now

\[
\boxed{
\mathrm{FROBMIX}_{108420}
\wedge
\mathrm{QRESBIND}_{107300}
\Longrightarrow
\mathrm{FROBHELL}_{108400}
\wedge
\mathrm{QRESBIND}_{107300}
\Longrightarrow
\mathrm{LIVEBOUND}_{107301}
\Longrightarrow
\mathrm{CBKM}_{106130}
\Longrightarrow
\mathrm{BCI}_{102990}
\Longrightarrow
\mathrm{RH}.
}
\tag{T-108420.3}
\]

`FROBMIX108420` is a weighted one-sided multiplicative-character variance
theorem plus the explicit live-mask boundary. `QRESBIND107300` contains the
at-most-three quadratic/constant resonance rows, endpoints and principal
binding.

## 3. Scope firewall

The positive gluing theorem applies only after exact source-authorized signed
recombination. `R-108420` shows that applying it to the absolute values of
principal and Kummer pieces before cancellation can turn a zero signed current
into positive mass.

```text
positive Hellinger mixture subadditivity       PROVED EXACT
physical pushforward contraction               PROVED EXACT
positive rectangle gluing                       CLOSED
signed-current rectangle gluing                 REQUIRES PRIOR RECOMBINATION
FROBMIX108420                                    OPEN
QRESBIND107300                                   OPEN
RH / GRH                                         UNPROVED
```
