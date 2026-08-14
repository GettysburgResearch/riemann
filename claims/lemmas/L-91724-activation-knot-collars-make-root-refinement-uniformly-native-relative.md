# L-91724 — Activation-knot collars make the factor-67 root refinement uniformly native-relative

Claim ID: `L-91724`  
Status: **PROVED EXACT COLLAR/REFINEMENT THEOREM ON FROZEN FINITE-CELL INPUTS**  
Created: 2026-08-14  
Frozen parent: PR #476 at `9f16ce483954d4233b68ee09cb6bec47400aa3cc`  
Primary inputs: `L-91107`, `L-91110`, `L-91674`, `L-91689`, `L-91690`, `L-91692`, `L-91723`  
Replay: `X-91724-factor67-knot-collar-relative-refinement`  
RH status: **unproved**

## 1. Why an activation collar is needed

Let `V(x)` be a complete typed root atom and let `c_a(x)>=0` be the
native capacity used to normalize coordinate `a`.  Piecewise Lipschitz
continuity of the unnormalized map does not by itself imply

\[
 \sup_x\frac{|V_{M,a}(x)-V_a(x)|}{c_a(x)}\longrightarrow0
\tag{L-91724.1}
\]

when `c_a` vanishes at an activation point.

The exact scalar model

\[
 V(t)=c(t)=t^2,\qquad 0\le t\le h,
\]

has a Lipschitz atom map.  Its positive linear interpolant between `0` and `h`
is

\[
 V_h(t)=ht.
\]

For `0<t<h`,

\[
 \frac{|V_h(t)-V(t)|}{c(t)}
 =\frac ht-1,
\tag{L-91724.2}
\]

whose supremum is infinite.  Thus the raw Lipschitz argument in `L-91695`
requires an activation-knot repair.

## 2. The actual factor-67 endpoint measure is atomless

The positive equality density on the factor-67 window is

\[
 L(x)=2\sqrt x\sum_{n\le x}\frac{\mu(n)}n
      -\sum_{n\le x}\frac{\mu(n)}{\sqrt n}.
\]

The endpoint quantizer of `L-91110` integrates

\[
 L(X/s)\,\frac{2\,ds}{s}.
\]

With `x=X/s`, the normalized positive endpoint measure is therefore

\[
 \boxed{
 d\nu(x)=\frac{2L(x)}x\,dx,
 \qquad 1\le x<67.
 }
\tag{L-91724.3}
\]

The directed factor-67 density bound is

\[
 0<L(x)<\frac{183}{100}.
\]

Hence

\[
 \boxed{
 0<\frac{d\nu}{dx}<\frac{183}{50}<4.
 }
\tag{L-91724.4}
\]

In particular `nu` is atomless.

Let `S={s_1,...,s_N}` be any finite set of activation knots and put

\[
 U_\eta=\bigcup_{\ell=1}^N(s_\ell-\eta,s_\ell+\eta)\cap[1,67).
\]

Then

\[
 \boxed{
 \nu(U_\eta)
 <\frac{183}{50}\,2N\eta
 <8N\eta.
 }
\tag{L-91724.5}
\]

Thus a finite knot collar can be made to have any prescribed positive mass.

## 3. The complete root typed map has finitely many activation knots

On `1<=x<67`, only finitely many small-divisor source atoms and component
coordinates are active.

Include in `S`:

1. every small-divisor activation `x=k`;
2. every component-row activation `x=jk` and every logarithmic-ramp cell
   boundary used by `Q_(x/k)(j)`;
3. every ordinary, radix-four, boundary and port activation inherited from
   those finitely many rows;
4. the endpoints `1` and `67`.

On every component of `[1,67)\S`:

```text
the active source set is fixed;
every active target atom is strictly positive;
every active native capacity is strictly positive;
every typed atom is a finite algebraic-logarithmic ramp;
the deterministic left-greedy Hall map uses only +, -, min, and division by
positive target atoms.
```

The map `min` is one-Lipschitz, and division is Lipschitz on a compact set
where the denominator is bounded below.  Hence the complete post-Hall typed
fiber

\[
 \mathcal H(x)\in K
\]

is Lipschitz on every closed subcell disjoint from `S`.  Hall basis switches
inside a fixed activation cell do not require additional collars: finite
compositions of `min` preserve Lipschitz continuity.

## 4. Uniform relative refinement away from the knots

Fix `eta>0` and let

\[
 A_\eta=[1,67)\setminus U_\eta.
\]

It is a finite union of compact intervals.  For every active native coordinate
`a`, continuity gives

\[
 m_{\eta,a}
 :=\min_{x\in A_\eta,\ c_a(x)>0}c_a(x)>0.
\]

Let

\[
 m_\eta=\min_a m_{\eta,a}>0
\tag{L-91724.6}
\]

over the finite active coordinate set, and let `L_eta<infinity` be a common
maximum-norm Lipschitz constant for the complete typed map on the retained
cells.

Choose a mesh which does not cross `U_eta` or an activation knot and has
maximum cell width `h`.  On one mesh interval `[a,b]`, put

\[
 \theta=\frac{b-x}{b-a}
\]

and define the positive barycentric refinement

\[
 \boxed{
 \mathcal H_h(x)
 =\theta\mathcal H(a)+(1-\theta)\mathcal H(b)\in K.
 }
\tag{L-91724.7}
\]

If `u=x-a`, `v=b-x`, and `u+v=h`, then

\[
 \theta u+(1-\theta)v=\frac{2uv}{h}\le\frac h2.
\]

Therefore

\[
 \|\mathcal H_h(x)-\mathcal H(x)\|_\infty
 \le\frac{L_\eta h}{2}.
\tag{L-91724.8}
\]

Inactive coordinates vanish throughout the cell.  For every active coordinate,

\[
 \boxed{
 \frac{|(\mathcal H_h-\mathcal H)_a(x)|}{c_a(x)}
 \le\frac{L_\eta h}{2m_\eta}.
 }
\tag{L-91724.9}
\]

Consequently, for every `epsilon>0`, choosing

\[
 h\le\frac{2m_\eta\epsilon}{L_\eta}
\tag{L-91724.10}
\]

gives a positive refinement with uniform native-relative error at most
`epsilon` on the retained root window.

## 5. One-use source realization

Equation (L-91724.7) is a positive Markov pushforward of the endpoint
parameter.  Each original endpoint mass is split into at most two neighboring
mesh fibers with nonnegative weights summing to one.

Because the mesh never crosses an activation collar:

```text
the small-divisor source labels are unchanged inside a mesh cell;
each mesh fiber is Hallized with one deterministic common transport;
all row, ordinary, detail, score and port coordinates move together;
no source mass is copied;
the collar mass U_eta is declared unused positive source.
```

Thus the refinement is a source-owned positive packet, not an independent
coordinate approximation.

The collar is removed before the current/child split.  Positive omission
therefore preserves the mass-weighted child contraction of `L-91694`.

## 6. Quantitative payment from the all-column reserve

Let

\[
 r_K=\frac1{\sqrt K+130}
\tag{L-91724.11}
\]

be the strict normalized detail reserve of `L-91723`, valid in every
nonterminal physical column.

Let `C` be the complete bounded one-use observation/correction map.  A
conservative use of the fixed-window Hall stability theorem pays at most

\[
 \delta_X
 =10152\|C\|\epsilon_X
\tag{L-91724.12}
\]

for a pre-Hall atom refinement.  Direct interpolation of the complete
post-Hall fiber only improves this constant.

Choose the retained-cell mesh so that

\[
 \boxed{
 \epsilon_X
 <\frac{1}
 {2\cdot10152\|C\|(\sqrt K+130)}
 }
\tag{L-91724.13}
\]

when `C` is nonzero.  Then

\[
 \delta_X<\frac{r_K}{2},
\]

and the realized packet retains the strict all-column reserve

\[
 \boxed{
 s_X^{\rm final}(q)>
 \frac{\Omega_X(q)}{2(\sqrt K+130)}
 \qquad(2\le q\le X/4).
 }
\tag{L-91724.14}
\]

The terminal omission is unchanged or improved, because both the knot collar
and the square-root safety factor remove positive source before realization.

## 7. Score cost can be made vanishing

Let the complete score of a mass-one root packet be bounded by

\[
 A\sqrt X+B
\]

on the frozen factor-67 frame.  Since `nu` is atomless, choose the collar radius
so that its removed mass is at most

\[
 \beta_X
 \le\frac{X^{-2}}{A\sqrt X+B+1}.
\tag{L-91724.15}
\]

Then the collar score loss is below `X^-2`.

Include the score coordinate in the retained-cell typed norm and choose the
mesh additionally so that the integrated interpolation score error is below
`X^-2`.  The total new score cost is therefore `o(1)`.

Combined with the absolute `<4290` square-root-thinning cost of `L-91723`, the
native endpoint deficit remains

\[
 4\log X+C+o(1)=o(\log^2X).
\tag{L-91724.16}
\]

## 8. Scope

This theorem repairs the relative-refinement step.  It does not independently
reconstruct the frozen factor-67 Hall inequalities, adjacent mismatch
constant, collar response theorem, common port, terminal omission, direct
integral, or endpoint-to-RH consumer.

```text
raw global Lipschitz -> relative convergence          FALSE / R-91724
factor-67 endpoint measure atomless, density <4       EXACT
finite activation collars have arbitrary small mass   EXACT
positive cellwise relative refinement                 EXACT
one-use source ownership of refinement                EXACT
all-column reserve pays amplified error               EXACT CONDITIONAL
additional score cost                                 o(1)
full frozen SONTR dependency reconstruction           STILL REQUIRED
Riemann Hypothesis                                    UNPROVEN
```
