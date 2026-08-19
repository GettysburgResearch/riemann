# L-99200 — Exact projective prime update for the annular scalar

Claim ID: `L-99200`  
Status: **PROVED EXACT ALGEBRAIC THEOREM**  
Created: 2026-08-19  
Frozen base: PR #614 at `d5b94d7dd8e341dca73c2b5ff899a9adf2d1585f`  
Compared: PR #596, PR #610, PR #621  
RH status: **not assumed**

For a finite squarefree prime product `P` containing the fixed `P_61` base,
let

\[
 F_P(X)=\sum_{d\mid P}{\mu(d)\over\sqrt d}A_*(X/d),
 \qquad
 M_P(X)=\sum_{d\mid P}{1\over\sqrt d}A_*(X/d),
\]

where `A_*` is the positive factor-four `5:3` annular source. Normalize

\[
 s_P(X)={F_P(X)\over\sqrt X},\qquad
 u_P(X)={M_P(X)\over\sqrt X}.
\]

For a new prime `p` not dividing `P`, exact divisor switching gives

\[
\boxed{
 s_{Pp}(X)=s_P(X)-{1\over p}s_P(X/p),
 \qquad
 u_{Pp}(X)=u_P(X)+{1\over p}u_P(X/p).
}
\tag{L-99200.1}
\]

The positive normalized source profile `h_0=A_*/sqrt(X)` is nondecreasing by
PR #610. Consequently every `u_P` is nonnegative and nondecreasing.

Define the oriented projective determinant

\[
\boxed{
 \Delta_{P,p}(X)
 =s_P(X)u_P(X/p)-u_P(X)s_P(X/p).
}
\tag{L-99200.2}
\]

Whenever `u_P(X)>0`, solving (L-99200.2) for the child scalar and substituting
into (L-99200.1) gives

\[
\boxed{
 s_{Pp}(X)
 =\left(1-{u_P(X/p)\over p\,u_P(X)}\right)s_P(X)
  +{\Delta_{P,p}(X)\over p\,u_P(X)}.
}
\tag{L-99200.3}
\]

Because `u_P(X/p)<=u_P(X)`, the first coefficient is at least `1-1/p`.
Thus

\[
 s_P(X)\ge0,\quad \Delta_{P,p}(X)\ge0
 \quad\Longrightarrow\quad s_{Pp}(X)\ge0.
\tag{L-99200.4}
\]

Equation (L-99200.3) is the projective Bellman lift. It identifies the exact
piece of parent--child covariance discarded by every scalar-to-mass aperture.
It is a sufficient mechanism, not an assertion that the determinant is
nonnegative for the Riemann source.

---

# L-99202 — Exact cocycle for a vanishing Euler aperture

Claim ID: `L-99202`  
Status: **PROVED EXACT ALGEBRAIC THEOREM**  
Created: 2026-08-19  
Depends on: `L-99200`; PR #596 aperture asymptotics  
RH status: **not assumed**

Let `kappa_P>0` be a state aperture and set

\[
 D_P(X)=s_P(X)-\kappa_Pu_P(X).
\]

Use the exact Euler update

\[
 \kappa_{Pp}=\kappa_P{p-1\over p+1}.
\]

Then direct substitution into `L-99200.1` gives

\[
\boxed{
 D_{Pp}(X)
 =D_P(X)-{1\over p}D_P(X/p)
  +{2\kappa_P\over p+1}
   \bigl(u_P(X)-u_P(X/p)\bigr).
}
\tag{L-99202.1}
\]

The last term is nonnegative because the normalized unsigned mass is
nondecreasing. The first two terms show the missing hypothesis precisely:
pointwise `D_P>=0` is insufficient; one needs the source-faithful Bellman
inequality

\[
D_P(X)\ge p^{-1}D_P(X/p).
\tag{L-99202.2}
\]

The product aperture therefore does not create a free invariant cone. It
converts the fixed-angle problem into the same cross-scale quotient problem
isolated by PRs #608 and #614.

---

# L-99201 — Prime adjoining lifts the determinant to a multiplicative quadrilateral

Claim ID: `L-99201`  
Status: **PROVED EXACT ALGEBRAIC THEOREM**  
Created: 2026-08-19  
Depends on: `L-99200`  
RH status: **not assumed**

For distinct new primes `p,q`, abbreviate

\[
 s=s_P(X),\quad s_p=s_P(X/p),\quad s_q=s_P(X/q),
 \quad s_{pq}=s_P(X/(pq)),
\]

and similarly for `u`. Define

\[
 \Delta_{P,q}(X)=s u_q-u s_q
\]

and the signed multiplicative quadrilateral

\[
\boxed{
 \Xi_{P;p,q}(X)
 =s u_{pq}+u s_{pq}-s_pu_q-u_ps_q.
}
\tag{L-99201.1}
\]

Expanding the two prime-update formulas gives exactly

\[
\boxed{
 \Delta_{Pp,q}(X)
 =\Delta_{P,q}(X)
  +{1\over p}\Xi_{P;p,q}(X)
  -{1\over p^2}\Delta_{P,q}(X/p).
}
\tag{L-99201.2}
\]

In the positive parity coordinates

\[
 E=u+s,\qquad O=u-s,
\]

the quadrilateral is

\[
\boxed{
 2\Xi_{P;p,q}
 =\bigl(E E_{pq}-E_pE_q\bigr)
  -\bigl(O O_{pq}-O_pO_q\bigr).
}
\tag{L-99201.3}
\]

Thus it is the difference of two positive-channel multiplicative Monge
curvatures. A two-scale determinant is not a Markov state: adjoining one more
prime necessarily requests all four quotient corners. Iterating this identity
reconstructs the complete squarefree quotient cube, in agreement with PR
#614's `Omega(sqrt N)` exact-state theorem.

---

# R-99200 — The first live rough prime defeats both naive vanishing aperture and determinant closure

Claim ID: `R-99200`  
Status: **PROVED DIRECTED COUNTERCERTIFICATE + EXACT ALGEBRAIC FIREWALL**  
Created: 2026-08-19  
Frozen arithmetic source: PR #587 at `8a0f074c5b96600b461fdd6e23b47ee2162c4a70`  
RH status: **not assumed**

## 1. Live `p=67`, `X=184` vanishing-aperture failure

For the complete `P_61` annular source, PR #587 proves

\[
F_{61}(184)=10.693579648773829950805315504985\ldots,
\]

\[
M_{61}(184)=445.857603542602836315578077301107\ldots.
\]

At the child endpoint

\[
Y={184\over67}\in(2,3),
\]

only the positive `m=2` source is active, so signed and unsigned child rows
coincide. Its contribution to the unnormalized parent update is exactly

\[
 c={15\over\sqrt{134}}\log{92\over67}
 =0.410893778550441347504657291360\ldots.
\]

Hence

\[
F_{61\cdot67}(184)=F_{61}(184)-c,
\qquad
M_{61\cdot67}(184)=M_{61}(184)+c.
\]

The Euler aperture obtained from `1/42` is

\[
\kappa_{61\cdot67}={1\over42}{66\over68}={11\over476}.
\]

Directed rational enclosures give

\[
\boxed{
F_{61\cdot67}(184)-{11\over476}M_{61\cdot67}(184)
<-0.03024<0.
}
\tag{R-99200.1}
\]

Equivalently,

\[
{F_{61\cdot67}(184)\over M_{61\cdot67}(184)}
=0.02304147824000120345\ldots
<{11\over476}.
\]

Thus the most natural state-dependent Euler aperture already fails at the
first rough prime. The scalar itself remains positive.

## 2. The live projective determinant is negative

At the same child, `s_{61}(Y)=u_{61}(Y)>0`, while
`F_{61}(184)<M_{61}(184)`. Therefore

\[
\boxed{
\Delta_{61,67}(184)
=u_{61}(Y)\bigl(s_{61}(184)-u_{61}(184)\bigr)<0.
}
\tag{R-99200.2}
\]

So the sufficient determinant cone of `L-99200` is not the missing theorem.

## 3. Abstract two-scale invariance is false

Take four quotient corners with unit masses and signed coordinates

\[
s=s_p=s_q=1,\qquad s_{pq}=0.
\]

Then all scalar coordinates are nonnegative,

\[
\Delta_q(X)=0,
\qquad
\Delta_q(X/p)=1,
\qquad
\Xi_{p,q}(X)=-1.
\]

After adjoining `p`, the scalar at `X` is still `1-1/p>0`, but

\[
\boxed{
\Delta_{Pp,q}(X)=-{1\over p}-{1\over p^2}<0.
}
\tag{R-99200.3}
\]

Thus even nonnegative scalars, monotone masses and nonnegative input
projective determinants do not form an invariant two-scale cone. The four
quotient corners are genuinely load bearing.

---

# M-99200 — Projective quotient-profile closure program

The prime update is not controlled by a scalar angle. It is a projective
update whose missing term is the determinant

\[
\Delta_{P,p}(X)=s_P(X)u_P(X/p)-u_P(X)s_P(X/p).
\]

This makes parent--child covariance explicit. The live `p=67, X=184` state
makes this determinant negative, and the next update requires the four-corner
quadrilateral. A fixed two-scale repair is therefore closed.

A continuation must retain the complete quotient profile and prove one of:

1. the critical projective maximum principle `s_P(X)>=p^{-1}s_P(X/p)`;
2. a source-prescribed multiplicative-cube Bellman barrier;
3. PR #621's owner-martingale embedding before the source index is collapsed.

The hereditary Dickman corridor of PRs #608/#614 supplies the terminal region.
The low-prime critical block cannot be compressed to one aperture or one
determinant.

---

# T-99200 — Projective Bellman lift and multiplicative-quadrilateral frontier

Status: **UNCONDITIONAL STRUCTURAL ADVANCE; RH-BEARING PRODUCER OPEN**

For the native normalized signed/unsigned annular profiles:

1. every prime update has the exact projective decomposition above;
2. the state-dependent Euler-aperture defect has the exact cocycle above;
3. every determinant update has the exact four-corner law above;
4. the product Euler aperture is false on the live source at `(p,X)=(67,184)`;
5. the live determinant is negative there;
6. no abstract two-scale determinant cone is invariant under prime adjoining.

Therefore the first nonlinear compression beyond the scalar is insufficient.
The exact future-prime state must retain the multiplicative quotient grid, or
an equivalent source-level conditional expectation.

```text
projective prime update                     PROVED EXACT
vanishing-aperture defect cocycle            PROVED EXACT
multiplicative quadrilateral update          PROVED EXACT
live product-aperture counterexample         PROVED DIRECTED
live determinant sign                        PROVED EXACT
abstract two-scale invariance                REFUTED EXACT
full quotient-profile / OMCE producer        OPEN / RH-BEARING
Riemann Hypothesis                           UNPROVEN
```
