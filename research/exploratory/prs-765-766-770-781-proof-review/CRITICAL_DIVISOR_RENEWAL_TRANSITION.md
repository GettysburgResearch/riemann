# Critical divisor-renewal transition at `J^2/k`

**Status:** proposed source-specific asymptotic theorem; independent proof review required.  
**Depends on:** `POINCARE_FRAME_ENDPOINT_LADDER_PART_I.md` and Part II.  
**RH/GRH:** RH and GRH remain unproved.

The recentered determinant ladder survives throughout
`J=o(k/log k)`, but strict zero--pole separation is controlled by a smaller
finite-block coupling.  This note derives that coupling exactly when

\[
\frac{J^2}{k}\longrightarrow\tau\in(0,\infty)
\tag{DR0}
\]

and the flag offset `h=J-i` is fixed.

The outcome is an explicit divisor-renewal polynomial `g_h(tau)`.  Its zeros
are the leading-order merger resonances of adjacent determinant clusters.
This proves that the fixed-depth coefficient `S_h=sigma_{-1}(h)` cannot be
used uniformly through the square-root scale.

---

## 1. Scaling and exact source block

Take even weights `k` and integers `J=J(k)` such that

\[
J\to\infty,
\qquad
J=o(k/\log k),
\qquad
J^2/k\to\tau\in(0,\infty).
\tag{DR1}
\]

Fix `h>=1` and put

\[
i=J-h.
\]

Work in the recentered disc about the exact one-mode zero
`chat_{k,J}` from PF25.  Eliminate the far block `W_{2J+1}`, every mode above
`J`, and the intermediate modes `i+1,...,J-1`, using the exact source Schur
operations.  The final real two-by-two block is

\[
\begin{pmatrix}
a_{h,J}&b_{h,J}\\
b_{h,J}&d_{h,J}
\end{pmatrix}.
\tag{DR2}
\]

Part II shows that the diagonal entries and the derivative of the deepest
entry are unaffected at leading order by the unequal-energy Schur
corrections:

\[
\frac{a_{h,J}}{A_i}
\longrightarrow\frac{h}{24\tau},
\tag{DR3}
\]

\[
\frac{d_{h,J}'(\widehat c_{k,J})}{A_J}
\longrightarrow\frac1{288\tau}.
\tag{DR4}
\]

The only nontrivial leading renormalization occurs in the cross
`b_{h,J}/A_J`.

---

## 2. Limiting triangular divisor block

Index the intermediate source modes by their distance from `J`:

\[
m_r=J-r,
\qquad r=1,\ldots,h-1.
\]

Column-scale the period block by `A_{m_r}`.  At
`c=chat_{k,J}+o(1)`, the diagonal limit is

\[
\frac{T_{m_r}(c)}{A_{m_r}}
\longrightarrow\frac{r}{24\tau}.
\tag{DR5}
\]

For `r>s`, the source arithmetic cross has limit

\[
\frac{H_{m_r,m_s}}{A_{m_s}}
\longrightarrow S_{r-s},
\tag{DR6}
\]

whereas the reverse column-scaled entry contains

\[
\frac{A_{m_r}}{A_{m_s}}
\le
\exp\!\left[-c(r-s)k/J\right]
\longrightarrow0.
\tag{DR7}
\]

The Poincare-frame residual and both deep eliminations are
superpolynomially smaller.  Thus the limiting intermediate matrix is lower
triangular:

\[
\mathcal C_{rs}(\tau)
=
\begin{cases}
 r/(24\tau),&r=s,\\
 S_{r-s},&r>s,\\
 0,&r<s.
\end{cases}
\tag{DR8}
\]

The row coupling from mode `i=J-h` to `m_r` tends to `S_{h-r}` and the
column coupling from `m_r` to `J` tends to `S_r`.

---

## 3. Renewal recurrence

Let `y_r(tau)` solve the limiting triangular system

\[
\frac{r}{24\tau}y_r
+
\sum_{s=1}^{r-1}S_{r-s}y_s
=S_r,
\qquad r\ge1.
\tag{DR9}
\]

The effective cross after eliminating the first `h-1` modes is

\[
g_h(\tau)
=S_h-
\sum_{r=1}^{h-1}S_{h-r}y_r.
\tag{DR10}
\]

Applying DR9 at `r=h` gives the equivalent identity

\[
g_h(\tau)=\frac{h}{24\tau}y_h.
\tag{DR11}
\]

Define

\[
S(z)=\sum_{r\ge1}S_rz^r,
\qquad
\Phi(z)=\int_0^z\frac{S(t)}t\,dt
=
\sum_{r\ge1}\frac{S_r}{r}z^r.
\tag{DR12}
\]

Since

\[
S_r=\sum_{d|r}\frac1d,
\]

one also has the exact Lambert-series form

\[
\boxed{
\Phi(z)
=-\sum_{d\ge1}\frac{\log(1-z^d)}{d^2}.
}
\tag{DR13}
\]

For `Y(z)=sum_{r>=1}y_rz^r`, recurrence DR9 becomes

\[
zY'(z)+24\tau S(z)Y(z)=24\tau S(z).
\tag{DR14}
\]

With `Z=1-Y`,

\[
zZ'(z)+24\tau S(z)Z(z)=0,
\qquad Z(0)=1.
\]

Therefore

\[
Z(z)=\exp[-24\tau\Phi(z)],
\qquad
Y(z)=1-\exp[-24\tau\Phi(z)].
\tag{DR15}
\]

Combining DR11 and DR15 yields the closed form

\[
\boxed{
 g_h(\tau)
 =-rac{h}{24\tau}
 [z^h]\exp[-24\tau\Phi(z)].
}
\tag{DR16}
\]

For every fixed `h`, this is a real polynomial in `tau` of degree `h-1`,
with

\[
g_h(0)=S_h.
\tag{DR17}
\]

---

## 4. Critical coupling theorem

### Theorem 4.1

Under DR1, for every fixed `h>=1`, uniformly for `c` in an `o(1)` real
neighborhood of the `J`-th cluster,

\[
\boxed{
\frac{b_{h,J}(c)}{A_J}
\longrightarrow g_h(\tau).
}
\tag{DR18}
\]

#### Proof

Write the finite source Schur correction exactly as

\[
\frac{b_{h,J}}{A_J}
=
S_h-u^T C^{-1}v+o(1),
\tag{DR19}
\]

where `C` is the column-scaled intermediate period block,
`u_r=S_{h-r}+o(1)`, and `v_r=S_r+o(1)`.  Equations DR5--DR8 give entrywise
convergence of this fixed-size matrix to `mathcal C(tau)`, whose diagonal is
nonzero.  Hence its inverse converges.  The limiting Schur expression is
DR10, and DR16 identifies it with `g_h(tau)`. ∎

The theorem is local in fixed `h`; it does not replace the uniform
subcritical theorem PF60 when `h` grows with `J`.

---

## 5. Critical gap and residue laws

Assume first

\[
g_h(\tau)\ne0.
\tag{DR20}
\]

Then the exact mean-value identity PF57 and DR3--DR4 give strict interlacing
and

\[
\boxed{
 c_{J-h,J}-c_{J-h+1,J}
 =
 \frac{6912\tau^2}{h}
 g_h(\tau)^2
 \frac{A_J}{A_{J-h}}
 (1+o(1)).
}
\tag{DR21}
\]

The right-hand `s`-residue satisfies

\[
\boxed{
\operatorname{Res}_{s}Q_{J-h}
=
\frac{288\tau A_J}{k}
 g_h(\tau)^2(1+o(1))
=
\frac{288J^2A_J}{k^2}
 g_h(\tau)^2(1+o(1)).
}
\tag{DR22}
\]

As `tau->0`, DR17 turns DR21--DR22 into the fixed-depth formulas with
`S_h^2`.

If

\[
g_h(\tau)=0,
\tag{DR23}
\]

then

\[
 b_{h,J}=o(A_J),
\]

and the zero--pole gap and residue are smaller than the scales displayed in
DR21--DR22.  The present theorem does **not** assert exact finite-`k`
cancellation at a resonance.  A second-order expansion is required there.

Thus the finite set

\[
\mathcal R_h
=\{\tau>0:g_h(\tau)=0\}
\tag{DR24}
\]

is the leading merger-resonance set at offset `h`.

---

## 6. First exact coupling polynomials

The closed form gives

\[
g_1(\tau)=1,
\tag{DR25}
\]

\[
g_2(\tau)=\frac32-24\tau,
\tag{DR26}
\]

\[
g_3(\tau)=\frac43-54\tau+288\tau^2,
\tag{DR27}
\]

\[
g_4(\tau)=
\frac74-rac{209}{3}\tau+864\tau^2-2304\tau^3,
\tag{DR28}
\]

\[
g_5(\tau)=
\frac65-rac{185}{2}\tau+1450\tau^2
-8640\tau^3+13824\tau^4.
\tag{DR29}
\]

In particular, the first resonance is exact:

\[
\boxed{g_2(1/16)=0.}
\tag{DR30}
\]

So for the quotient two levels above the active mode, the leading direct
coupling and the one intermediate Schur path cancel when
`J^2/k ->1/16`.  This is an analytic phase transition, not a numerical
pattern.

No assertion is made that every `g_h` has only real roots, that the positive
roots are simple, or that distinct offsets have disjoint resonance sets.
The first polynomials are displayed as consequences of DR16, not as an
extrapolated root law.

---

## 7. Subcritical uniformity revisited

For small `tau`, recurrence DR9 gives

\[
y_r=\frac{24\tau}{r}S_r+O(\tau^2).
\]

The elementary convolution estimate PF59 and triangular Neumann inversion
imply, uniformly for `h<=L`,

\[
g_h(\tau)=S_h+O(\tau\log(L+2))
\tag{DR31}
\]

whenever `tau log(L+2)=o(1)`.  This is exactly condition PF58 and proves that
the strict subcritical theorem is the small-coupling side of the same
renewal law.

The square-root scale is therefore not merely where an old error bound
fails.  It is where the source Schur paths contribute at leading order.

---

## 8. Toward the full critical operator

For offsets `r` that grow while `J^2/k->tau`, the limiting column-scaled
matrix is the lower-triangular divisor operator

\[
(\mathcal L_\tau x)_r
=
\frac{r}{24\tau}x_r
+
\sum_{s<r}S_{r-s}x_s.
\tag{DR32}
\]

Its generating-function resolvent is the first-order differential operator

\[
z\frac d{dz}+24\tau S(z),
\tag{DR33}
\]

with integrating factor

\[
\exp[24\tau\Phi(z)].
\]

Since

\[
\Phi(z)
=\zeta(2)\log\frac1{1-z}+O(1)
\qquad(z\to1^-),
\tag{DR34}
\]

its boundary behavior is governed by the exponent `24 tau zeta(2)`.
A future all-offset theorem should formulate the quotient ladder through
this resolvent rather than a Jacobi matrix guessed from finite determinants.

---

## 9. Scope and stop conditions

New in this note:

* the triangular critical block DR8;
* the exact renewal recurrence DR9;
* the Lambert-series integrating factor DR13--DR16;
* the critical coupling limit DR18;
* the modified gap and residue laws DR21--DR22;
* the resonance mechanism, including the exact first value `tau=1/16`.

Imported:

* the source Poincare frame and recentered determinant theorem;
* the exact arithmetic cross `S_h`;
* the source Schur identities and reflection.

Not claimed:

* exact cancellation at a resonance for finite `k`;
* a complete root classification of `g_h`;
* a uniform fixed-`tau` theorem for offsets growing with `J`;
* a self-adjoint Jacobi realization;
* critical-line purity, RH, or GRH.

At a resonance, relative gap and residue asymptotics must stop.  Finite
experiments may guide the next scaling, but cannot replace the missing
second-order source expansion.