# L-91803 — Interval-natural product-system morphisms preserve radial spectral type

Claim ID: `L-91803`  
Status: **PROVED EXACT TYPE-I PRODUCT-SYSTEM MODULE THEOREM**  
Created: 2026-08-13  
Depends on: elementary direct-integral and symmetric-Fock functoriality  
RH status: **unproved**

## 1. Diffuse source product system

Let

\[
 \mathfrak h_{m src}
 =L^2((0,R),dr;\mathfrak k_r)
\]

and let

\[
 \Gamma_s(\mathfrak h_{m src})
\]

be its symmetric Fock space.  For a Borel set `I subset (0,R)`, let

\[
 P_I=M_{\mathbf1_I}
\]

be the one-particle radial projection.  The corresponding Fock factorization
is

\[
 \Gamma_s(\mathfrak h_{m src})
 \cong
 \Gamma_s(P_I\mathfrak h_{m src})
 \otimes
 \Gamma_s(P_{I^c}\mathfrak h_{m src}).
\]

The radial spectral measure of every one-particle vector is absolutely
continuous with respect to `dr`.

## 2. A target with an atomic depth sector

Let

\[
 \mathfrak h_{m tgt}
 =\mathfrak h_{\rm ac}
  \oplus
  \bigoplus_{d\in\mathcal D}\mathfrak h_d,
\]

where `h_ac` is a direct integral over `dr` and the summands `h_d` are located
at point depths `d`.  Let `Q_I` be the spectral projection

\[
 Q_I
 =Q_I^{\rm ac}
  \oplus
  \bigoplus_{d\in I}I_{\mathfrak h_d}.
\]

## 3. Interval-natural one-particle maps

Let

\[
 T:\mathfrak h_{\rm src}\longrightarrow\mathfrak h_{\rm tgt}
\]

be bounded and suppose that it is local for every radial interval:

\[
\boxed{
 TP_I=Q_IT
 \qquad\text{for every Borel }I\subset(0,R).
}
\tag{L-91803.1}
\]

Then for every atom `d in D`,

\[
 Q_{\{d\}}T
 =TP_{\{d\}}
 =0,
\]

because `P_{\{d\}}=0` on the diffuse source.  Hence

\[
\boxed{
 \operatorname{ran}T
 \subseteq\mathfrak h_{\rm ac}.
}
\tag{L-91803.2}
\]

No atomic target coordinate can be populated.

This is the module form of the spectral theorem: a bounded
`L^infinity((0,R),dr)`-module map preserves the Lebesgue spectral type.

## 4. Product-system naturality implies module locality

Suppose instead that a Fock-space isometry

\[
 \mathcal W:
 \Gamma_s(\mathfrak h_{\rm src})
 \longrightarrow
 \Gamma_s(\mathfrak h_{\rm tgt})
\]

preserves the vacuum and is natural under every interval factorization:

```text
source factors over I and I^c;
target factors over I and I^c;
W is the tensor product of its two restrictions.
```

Then the restriction of `W` to the one-particle sector satisfies
(L-91803.1).  To see this, a one-particle vector supported in `I` is the
coefficient of first order in the exponential vector

\[
 \operatorname{Exp}(\varepsilon f)
 \otimes\Omega_{I^c}.
\]

Interval naturality keeps its first-order image inside the target `I` factor.
The same argument for `I^c` gives equality of the projections.

Therefore

\[
\boxed{
 \text{an interval-natural Fock morphism cannot create a positive-depth atom.}
}
\tag{L-91803.3}

## 5. Why dyadic naturality alone is not enough

Locality only for one fixed dyadic grid does not imply (L-91803.1) for every
Borel set.  An atom can be hidden inside one dyadic cell and carried by that
cell's source factor.

It is enough to have locality for a generating family whose mesh tends to
zero and which separates every depth, for example all dyadic grids with all
translations, or all half-open rational intervals.  Strong continuity then
extends the projection relation to the full Borel algebra.

## 6. Zeta interpretation

The arithmetic radial source of `L-91800` is a type-I diffuse product system.
The crossed-zero depth operator of `L-91801` supplies the target atomic
summands.  Therefore a completed source-to-model colligation which is natural
for every horizontal subinterval cannot populate any off-line hyperbolic port.

The remaining burden is not a numerical estimate.  It is to prove that the
completed arithmetic/model map is genuinely interval natural, rather than
only a global isometry after all radial generations have been summed.

## 7. Exact boundary

```text
diffuse source product system                    EXACT
atomic target depth sector                       EXACT ABSTRACT SETUP
Borel-module map preserves spectral type         EXACT
interval-natural Fock morphism -> module map      EXACT
one fixed dyadic grid sufficient                  FALSE
completed zeta interval naturality                OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVED
```
