# Simultaneous exceptional-disk collar frontier

Status: **EXPLORATION WITH EXACT FINITE GEOMETRY; XI INPUT OPEN**

Scope: one finite family of exceptional disks and one two-parameter family
of symmetric rectangles.  No Xi minimum-modulus estimate, cofinal passage,
RCMV104530, or RH conclusion is claimed.

Exact dependencies: L/T-105109, L/T/R-105111, L/T/R-105112, and
L/T/R-105113 at checkpoint
`98e76fdd350556b2c659a0a16f7fa4083396527e`.

What was actually run: exact geometric derivation and hostile review, plus
the complete 105100--105113 replay (215/215 focused tests in normal Python
and 215/215 under `-O`).  No zero scan, numerical minimum-modulus search,
or heavy computation was run.

Smallest remaining gap: a source-locked quantitative theorem that produces
simultaneous exceptional disks and usable lower bounds for the two fixed Xi
derivatives at cofinal scale, with enough room and strength to absorb the
actual selector costs.

## 1. Exact simultaneous projection lemma

Let

\[
D_j=\overline D(x_j+iy_j,r_j),
\qquad
S=\sum_{j=1}^N r_j,
\]

and let

\[
T\in(T_0,T_1),
\qquad
\eta\in(\eta_0,\eta_1),
\]

parametrize

\[
\Omega_{T,\eta}
=\{z:|\Re z|<T,\ |\Im z|<\eta\}.
\]

The exact bad projection sets are

\[
B_T=
\bigcup_j
\left([|x_j|-r_j,|x_j|+r_j]\cap(T_0,T_1)\right),
\]

\[
B_\eta=
\bigcup_j
\left([|y_j|-r_j,|y_j|+r_j]\cap(\eta_0,\eta_1)\right).
\]

Indeed, either vertical supporting line \(\Re z=\pm T\) meets \(D_j\)
exactly when

\[
\min(|T-x_j|,|T+x_j|)
=|T-|x_j||\le r_j,
\]

and the horizontal statement is identical.  Therefore every pair in

\[
G_T\times G_\eta,
\qquad
G_T=(T_0,T_1)\setminus B_T,
\quad
G_\eta=(\eta_0,\eta_1)\setminus B_\eta,
\]

has

\[
\partial\Omega_{T,\eta}\cap\bigcup_jD_j=\varnothing.
\]

Because the bad sets are finite unions of relatively closed intervals, the
exact supporting-line criterion is

\[
|B_T|<\Delta_T,
\qquad
|B_\eta|<\Delta_\eta,
\]

where \(\Delta_T=T_1-T_0\) and
\(\Delta_\eta=\eta_1-\eta_0\).  The total-radius relaxation is

\[
|B_T|\le2S,
\qquad
|B_\eta|\le2S.
\]

Hence the clean sufficient condition is

\[
\boxed{\Delta_T>2S,\qquad\Delta_\eta>2S.}
\]

The coefficient two and the strict inequality are sharp using only \(S\):
one radius-\(S\) disk centered at the midpoint of a parameter interval can
meet the corresponding supporting line for every allowed parameter when
that interval has length at most \(2S\).

## 2. Direct quotient consequences

Suppose that on the enclosing region outside the disks one has

\[
|F|\le M_0,
\qquad
|F'|\ge a_1>0,
\qquad
|F''|\ge a_2>0.
\]

On every selected safe boundary \(E=\partial\Omega_{T,\eta}\),

\[
\boxed{
\left\|\frac F{F'}\right\|_E\le\frac{M_0}{a_1},
\qquad
\left\|\frac{F^2}{F'F''}\right\|_E
\le\frac{M_0^2}{a_1a_2}.
}
\]

This formulation does not require \(F\ne0\) on the edge.  At a zero of
\(F\), the raw quotient vanishes while the denominators remain nonzero.
One must not silently rewrite this case through \(L=F'/F\) or
\(A=F''/F\), which are then undefined.

For arbitrary continuous weights, put

\[
I_j(E)=\int_E|W_j|\,|dz|,
\qquad
b_j(E)=\|W_j\|_E.
\]

Since \(\operatorname{len}(E)=4(T+\eta)\),

\[
\int_E\left|W_1\frac F{F'}\right|\,|dz|
\le\frac{M_0}{a_1}I_1(E)
\le4(T+\eta)\frac{M_0}{a_1}b_1(E),
\]

\[
\int_E\left|W_2\frac{F^2}{F'F''}\right|\,|dz|
\le\frac{M_0^2}{a_1a_2}I_2(E)
\le4(T+\eta)\frac{M_0^2}{a_1a_2}b_2(E).
\]

## 3. Selector-domain firewall

The L-105112 repair controls how these inequalities may be specialized.

- If \(W_{j,*}\) is the optimal selector built on this exact selected
  rectangle, then \(|W_{j,*}|=\tau_j\) on \(E\), so
  \(I_j(E)=4(T+\eta)\tau_j\).
- If the selector is optimal on an outer rectangle and \(E\) is an
  intermediate boundary, maximum modulus gives only
  \(\|W_{j,*}\|_E\le\tau_j\), not equality.
- The L-105113 reduced polynomial selectors are fixed outer-manifest
  objects, not same-domain extremals.  Their actual \(I_j(E)\),
  \(b_j(E)\), or a separately proved outer norm remains load bearing.
- Rebuilding a different optimal selector for each intermediate rectangle
  would destroy the fixed-carrier hypothesis used by shell averaging.

## 4. Restricted shell selection

Let

\[
g_T=\Delta_T-|B_T|,
\qquad
g_\eta=\Delta_\eta-|B_\eta|.
\]

When both are positive, the disk-safe parameter set has measure
\(g_Tg_\eta\).  Restricting the L-105113 Tonelli argument to
\(G_T\times G_\eta\) gives, for every prescribed aggregate nonnegative
boundary cost, a common disk-safe rectangle.  Relative to the unrestricted
mean, the crude loss is at most

\[
\boxed{
\kappa=
\frac{\Delta_T\Delta_\eta}{g_Tg_\eta}
\le
\frac{\Delta_T\Delta_\eta}
{(\Delta_T-2S)(\Delta_\eta-2S)}.
}
\]

Raw-event-irregular parameter lines form a null set and may also be removed.
This combines exceptional-disk avoidance with one common prescribed-weight
good rectangle, but it supplies no analytic disk certificate.

## 5. The missing Cartan import

The current tree does not authenticate the Xi specialization.  A usable
next theorem must fix the completed-Xi normalization and derivative index,
then provide on expanded rectangles:

1. explicit upper growth data for \(F=\Xi^{(k-1)}\);
2. simultaneous lower bounds \(a_1,a_2\) for \(F',F''\) outside a stated
   finite disk family;
3. an explicit total-radius budget \(S\) under a declared radius-versus-
   diameter convention;
4. nonzero anchors or another normalization preventing a vacuous
   minimum-modulus bound;
5. complete actual-pole manifests and selector construction on each finite
   outer window;
6. cofinal inequalities making \(\Delta_T,\Delta_\eta>2S\) and absorbing
   \(M_0/a_1\), \(M_0^2/(a_1a_2)\), edge length, and the actual selector
   costs.

Generic order-one growth or a qualitative statement that the exceptional
radius is finite is not enough.  It can yield exponentially large losses
with no comparison to selector conditioning or the residue-moment scale.
The smallest defensible next claim is therefore a source-pinned,
quantitative exceptional-disk certificate for the three fixed functions at
one declared finite window, followed by a separate cofinal absorption
theorem.  Until then, the projection lemma is a routing result, not an Xi
collar estimate.
