# L-106051 — Quadratic root fibres are the two temperature–Kummer squareclass charts

Claim ID: `L-106051`  
Programme aliases: `LFAM1.ROOT_FIBRE_CHARTS`, `LFAM2.KUMMER_PROJECTORS`, `STRESS.OWNER_CLASS_FIBRE`  
Status: **PROVED EXACT SOURCE-PROJECTOR THEOREM**  
Created: 2026-08-24  
Depends on: `L-106050`; `L-106020`, `L-106027`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let `kappa` be a quadratic character on the finite unramified source algebra,
so

\[
\kappa^2=1.
\]

For any character `chi`, the two roots

\[
\chi,
\qquad
\chi\kappa
\]

have the same character square:

\[
(\chi\kappa)^2=\chi^2.
\tag{L-106051.1}
\]

Put

\[
\Gamma_\chi
=
\sigma_{1/2,\chi}*\sigma_{1/2,\chi}
=E_\chi*S_{\chi^2}.
\]

The squared completion is therefore common to the two roots.

## 1. Exact source projectors

Define the coefficient projectors on unramified integers

\[
P_\pm(n)=\frac{1\pm\kappa(n)}2.
\tag{L-106051.2}
\]

Because character twisting is coefficientwise,

\[
\boxed{
\frac{E_\chi\pm E_{\chi\kappa}}2
=P_\pm E_\chi.
}
\tag{L-106051.3}
\]

Multiplying by the common squared completion gives

\[
\boxed{
\frac{\Gamma_\chi\pm\Gamma_{\chi\kappa}}2
=(P_\pm E_\chi)*S_{\chi^2}.
}
\tag{L-106051.4}
\]

Thus the symmetric and antisymmetric combinations of one quadratic root fibre
are literally the square and nonsquare source charts.

## 2. Physical semiprime squareclasses

For a clean physical product

\[
N=P a^2
\]

with the conductor prime absent from `Pa`,

\[
\kappa(N)=\kappa(P)\kappa(a)^2=\kappa(P).
\tag{L-106051.5}
\]

Hence the projector label is exactly the owner quadratic class

\[
\sigma=\kappa(P)\in\{+1,-1\}.
\]

The core `a` remains in the common `chi^2` channel. This proves at full-source
scope the same class split that `L-106027` required for coherent local
occupancy.

## 3. Relation to the additive square phases

The finite Gauss transform of `L-106020` maps the two roots of one even
character `eta=chi^2` to the two additive squareclass charts. In the root basis,

```text
chi and chi*kappa;
```

in the chart basis,

```text
P_+ E_chi and P_- E_chi.
```

The change of basis is the exact two-by-two Hadamard transform. The principal
and quadratic roots are therefore not two independent copies of the native
core; they are the two spectral coordinates needed to reconstruct its two
owner squareclass charts.

For a squarefree product conductor, tensoring (L-106051.3) over its prime
factors gives the `2^omega(q)` local class sectors of `L-106040`.

## 4. Consequence for family architecture

The owner-class index must be retained until after the positive Kummer frame is
applied. Summing the two charts first converts the source back to the full
residue space and destroys the strict local contraction. Conversely, deleting
one quadratic root deletes one source chart and gives zero leverage on the
missing class.

## Scope

This theorem proves an exact source identification. It does not estimate the
coherent assembly of different owner packets, prove a twisted positive
inverse, `SOCM106020`, `CCSOCM106040`, or RH.
