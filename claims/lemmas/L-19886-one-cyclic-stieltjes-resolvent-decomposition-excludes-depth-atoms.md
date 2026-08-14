# L-19886 — One cyclic Stieltjes resolvent decomposition excludes positive-depth atoms

Claim ID: `L-19886`  
Status: **PROPOSED EXACT SCALAR SPECTRAL-TYPE THEOREM — PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-09-x`  
Created: 2026-08-14  
Depends on: uniqueness of the Stieltjes transform; `L-91313`; `L-91801`; `L-19884`  
RH status: **unproved**

## 1. Positive scalar depth measures

Let

\[
 \mu_{\rm ar},\qquad
 \mu_{\rm mod},\qquad
 \mu_{\rm aux}
\]

be locally finite positive Borel measures on `[0,infinity)` satisfying the
usual Stieltjes integrability

\[
 \int_0^\infty\frac{d\mu(x)}{1+x}<\infty.
\tag{L-19886.1}
\]

Assume the arithmetic measure is diffuse on positive depths:

\[
 \mu_{\rm ar}(\{d\})=0
 \qquad(d>0).
\tag{L-19886.2}
\]

Write the model measure as

\[
 \mu_{\rm mod}
 =\mu_{\rm cont}
 +\sum_{d>0}h_d\delta_d,
 \qquad h_d\ge0.
\tag{L-19886.3}

In the Xi application, the positive atoms are the one-node charges of crossed
off-line zeros.

## 2. One scalar resolvent identity

Suppose that for every `q>0`,

\[
\boxed{
 \int_0^\infty\frac{d\mu_{\rm ar}(x)}{q+x}
 =
 \int_0^\infty\frac{d\mu_{\rm mod}(x)}{q+x}
 +
 \int_0^\infty\frac{d\mu_{\rm aux}(x)}{q+x}.
}
\tag{L-19886.4}

Equivalently, the difference between the arithmetic and visible-model
resolvents is itself a Stieltjes function with one explicit positive auxiliary
measure.

No operator-valued interval identity is assumed.

## 3. Uniqueness of the positive measure

Put

\[
 \nu=\mu_{\rm ar}-\mu_{\rm mod}-\mu_{\rm aux}.
\]

Equation (L-19886.4) says that the Stieltjes transform of the signed locally
finite measure `nu` vanishes on `(0,infinity)`.  The transform is analytic on
`C minus (-infinity,0]`.  The identity theorem and the Stieltjes inversion
formula give

\[
\boxed{
 \mu_{\rm ar}
 =\mu_{\rm mod}+\mu_{\rm aux}
}
\tag{L-19886.5}
\]

as Borel measures.

The same conclusion follows without complex inversion by using

\[
 \frac1{q+x}=\int_0^\infty e^{-t(q+x)}dt
\]

and uniqueness twice for Laplace transforms.

## 4. Diffuse source kills every positive model atom

Evaluate (L-19886.5) on a singleton `{d}` with `d>0`.  Positivity gives

\[
 0
 =\mu_{\rm ar}(\{d\})
 =\mu_{\rm mod}(\{d\})+
  \mu_{\rm aux}(\{d\}).
\]

Therefore

\[
\boxed{h_d=0\qquad(d>0).}
\tag{L-19886.6}

Thus a single scalar Stieltjes decomposition already has the same
spectral-type consequence as intervalwise operator domination.

## 5. One Cauchy node detects every hyperbolic atom

Fix one interior half-plane node `eta>0`.  For an off-line zero

\[
 \zeta=d+i\gamma,
 \qquad d>0,
\]

`L-91801/L-91313` give the strictly positive scalar charge

\[
\boxed{
 g_\eta(\zeta)
 =\log\frac{(\eta+d)^2+\gamma^2}
              {(\eta-d)^2+\gamma^2}>0.
}
\tag{L-19886.7}

Hence the one-node model depth measure has the atomic part

\[
 \sum_\zeta m_\zeta g_\eta(\zeta)\delta_{d_\zeta}.
\tag{L-19886.8}

If (L-19886.4) holds for this one node, (L-19886.6) forces every coefficient in
(L-19886.8) to vanish.  Therefore there is no crossed off-line zero.

No density of carrier packets and no all-node operator theorem is needed after
the scalar source measure has been identified.

## 6. Concrete arithmetic source measure

`L-19884` supplies the native-defect component

\[
 d\nu_a^{\rm def}(x)
 =e^{-ax}\Delta(e^x)dx,
\tag{L-19886.9}
\]

which is absolutely continuous.  The realized-row component has the analogous
positive density

\[
 d\nu_a^{\rm row}(x)
 =e^{-ax}\mathcal H(d_{e^x})dx.
\tag{L-19886.10}
\]

Their sum is exactly the safe prime logarithmic-derivative measure because

\[
 -\frac{\zeta'}{\zeta}\!\left(a+\frac12\right)
 =a^2\int_0^\infty e^{-ax}
  [\mathcal H(d_{e^x})+\Delta(e^x)]dx.
\tag{L-19886.11}
\]

The eta, gamma/pole and compact-bridge sections already have positive diffuse
Laplace densities.  Thus every proposed arithmetic term in the scalar
completed source is diffuse; no positive-depth atom is introduced on the
source side.

## 7. Reduced passive producer

The remaining passive theorem can now be weakened from a complete operator or
all-packet model allocation to the following one-node identity.

> **Cyclic Scalar Resolvent Identification (`CSRI_(a,eta)`).**  Construct the
> completed arithmetic measure from the native row/defect and explicit
> archimedean channels, construct the critical/stable/hyperbolic one-node model
> measure at `eta`, and prove the Stieltjes identity (L-19886.4) for every
> `q>0` with one positive auxiliary measure.

If `CSRI_(a_j,eta)` holds for one sequence `a_j downarrow0`, every crossed-zero
atom at every positive depth is excluded, and functional-equation symmetry
gives RH.

This is strictly weaker than `DGGC_a`: it proves only one cyclic scalar
resolvent equality, not a full operator module map.

## 8. Firewall

An inequality of Stieltjes transforms is insufficient.  A diffuse measure can
have a larger resolvent than a point mass without dominating that point mass as
a measure.  The difference in (L-19886.4) must itself be represented by an
explicit positive Stieltjes measure.

Likewise, equality at finitely many `q` values is only a truncated moment
certificate.  Identity on an interval, or an analytic identity determining the
complete Stieltjes transform, is required.

## 9. Boundary

```text
positive resolvent decomposition -> measure equality      EXACT
one diffuse arithmetic measure -> no positive model atom   EXACT
one Cauchy node sees every off-line zero                    EXACT
native row/defect source measures diffuse                  EXACT
CSRI_(a,eta) completed one-node identity                    OPEN / RH-BEARING
DGGC_a full operator identity                               STRONGER / INDEPENDENT
Riemann Hypothesis                                          UNPROVED
```
