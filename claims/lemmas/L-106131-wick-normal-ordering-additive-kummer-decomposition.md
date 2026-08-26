# L-106131 — Wick normal ordering gives an exact additive/Kummer channel decomposition

Claim ID: `L-106131`  
Programme aliases: `LFAM1.WICK_CENTERED_GAUSS`, `LFAM2.MEAN_ZERO_KUMMER_DEFECT`, `STRESS.ATOMIC_FREE_FAMILY_IDENTITY`  
Status: **PROVED EXACT OPERATOR AND SOURCE IDENTITY**  
Created: 2026-08-25  
Depends on: `L-106020`, `L-106120`; binding correction `R-106131`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

The complete Gauss family is still useful after `R-106131`, but its literal
atomic diagonal must be removed channel by channel before the nonprincipal
family is treated as a new arithmetic statistic.

The resulting identity is exact, keeps every conductor fibre coherent, and
splits the physical additive current into a constant principal mode and a
mean-zero Kummer defect.

## 1. One-prime sign-pair operators

Fix an odd prime `q`. Aggregate nonzero residues modulo sign, so the residue
space has

\[
 m=\frac{q-1}{2}
\]

coordinates. Let `I` be the identity and `J` the all-ones operator on this
space.

The complete nonzero additive square-phase energy has Gram operator

\[
\boxed{
 A_q=qI-J.
}
\tag{L-106131.1}
\]

The principal/quadratic-root channel is the rank-one operator

\[
\boxed{
 C_q=\frac{q+1}{q-1}J,
}
\tag{L-106131.2}
\]

and the complete nonprincipal even-character channel is

\[
\boxed{
 N_q
 =qI-\frac{2q}{q-1}J
 =q\left(I-\frac1mJ\right).
}
\tag{L-106131.3}
\]

Therefore

\[
\boxed{
 A_q=C_q+N_q.
}
\tag{L-106131.4}
\]

The operator `N_q` is `q` times the orthogonal projection onto the mean-zero
sign-pair space. In particular,

\[
N_q\mathbf1=0,
\qquad
N_q\succeq0.
\tag{L-106131.5}
\]

This is the precise sense in which the nonprincipal family sees only
fluctuation away from the principal squareclass mode.

## 2. Source-level Wick normal ordering

Let a complete source member contain atoms `omega` with Hilbert coefficients
`z_omega`. Every additive or multiplicative character feature has modulus
one on one clean atom. Put

\[
 D=\sum_\omega\|z_\omega\|^2.
\tag{L-106131.6}
\]

For any family member `Z`, define

\[
\boxed{
 :\!\|Z\|^2\!:
 =
 \|Z\|^2-D.
}
\tag{L-106131.7}
\]

This is normal ordering with respect to the literal source atoms, before
equal-product or conductor fibres are collapsed.

Let `E_q` be the complete nonzero additive energy, `P_q` the weighted
principal channel and `K_q` the weighted nonprincipal channel. Because the
three atomic weights are respectively

\[
q-1,
\qquad
c_q=\frac{q+1}{q-1},
\qquad
\nu_q=\frac{q(q-3)}{q-1},
\]

with `c_q+nu_q=q-1`, equation (L-106131.4) remains exact after normal ordering:

\[
\boxed{
 E_q^\circ=P_q^\circ+K_q^\circ.
}
\tag{L-106131.8}
\]

A conductor fibre containing only one source atom has

\[
E_q^\circ=P_q^\circ=K_q^\circ=0.
\tag{L-106131.9}
\]

Thus the prime-core singleton fixture of `R-106123` contributes no
dimension to the normal-ordered family.

## 3. Exact off-atomic collision kernel

For two distinct unit residues `x,y`, put

\[
\delta_q^\pm(x,y)
=
\mathbf1_{x\equiv y\pmod q}
+
\mathbf1_{x\equiv-y\pmod q}.
\]

The off-atomic kernels are

\[
\boxed{
 A_q(x,y)=q\,\delta_q^\pm(x,y)-1,
}
\tag{L-106131.10}
\]

\[
\boxed{
 C_q(x,y)=\frac{q+1}{q-1},
}
\tag{L-106131.11}
\]

and

\[
\boxed{
 N_q(x,y)
 =q\,\delta_q^\pm(x,y)-\frac{2q}{q-1}.
}
\tag{L-106131.12}
\]

They satisfy `A_q=C_q+N_q` pair by pair.

The constant negative background in (L-106131.12) is load-bearing. Keeping
only the strict collision indicator would no longer be the nonprincipal
character moment.

## 4. Bilateral tensor decomposition

For the bilateral member of `L-106120`, let the two physical squareclass
coordinates be

\[
X=Pc^2\pmod\rho,
\qquad
Y=Qd^2\pmod\ell.
\]

The complete additive operator is

\[
A_\ell\otimes A_\rho.
\]

Using (L-106131.4),

\[
\boxed{
\begin{aligned}
A_\ell\otimes A_\rho
={}&
C_\ell\otimes C_\rho\\
&+C_\ell\otimes N_\rho\\
&+N_\ell\otimes C_\rho\\
&+N_\ell\otimes N_\rho.
\end{aligned}
}
\tag{L-106131.13}
\]

These four terms are exactly:

```text
principal--principal;
principal--nonprincipal;
nonprincipal--principal;
nonprincipal--nonprincipal.
```

Let `D_(ell,rho)` be the literal atomic sum of one complete bilateral fibre.
Define

\[
\begin{aligned}
\mathcal A_{\ell,\rho}^\circ
={}&
\sum_{h=1}^{\ell-1}\sum_{k=1}^{\rho-1}
|\mathcal W_{h,k}|^2
-(\ell-1)(\rho-1)D_{\ell,\rho},\\
\mathcal P_{\ell,\rho}^\circ
={}&
c_\ell c_\rho
\left(
|\mathcal W_{\mathbf1,\mathbf1}|^2-D_{\ell,\rho}
\right),
\end{aligned}
\tag{L-106131.14}
\]

and let `mathcal K_(ell,rho)^circ` be the sum of the three mixed/double
nonprincipal channels, with `D_(ell,rho)` subtracted separately from every
weighted character square.

Then

\[
\boxed{
\mathcal A_{\ell,\rho}^\circ
=
\mathcal P_{\ell,\rho}^\circ
+
\mathcal K_{\ell,\rho}^\circ.
}
\tag{L-106131.15}
\]

No positivity is asserted after normal ordering. The identity is a signed
off-atomic trace identity.

## 5. Interaction with the corrected physical-squareclass geometry

The nonprincipal part in (L-106131.15) retains exactly the collision varieties
of `T-106121` and `L-106126`:

\[
Pc^2\equiv\pm P'c'^2\pmod\rho,
\qquad
Qd^2\equiv\pm Q'd'^2\pmod\ell.
\]

After owner quadratic-class splitting, each strict collision is supported on
two or four linear core lines. Normal ordering removes only the literal atom
`omega=omega'`; it does not remove:

```text
different source atoms with the same physical squareclass;
strict Kummer collision lines;
the centered constant background;
mixed principal/nonprincipal interactions.
```

Inherited equal-product, repeated-label and shared-owner renewals may still be
removed at their already-proved scope.

## 6. Why this is the correct family repair

The uncentered positive nonprincipal moments pay one atomic trace for every
character and every conductor. The normal-ordered identity instead compares
two genuinely different off-atomic measurements of the same physical source:

```text
additive centered-divisor measurement;
multiplicative Kummer/Dirichlet-L measurement.
```

Their difference is the principal off-atomic squareclass mode.

The global conclusion-facing composition is `T-106140`. It is essential
there that all conductor fibres are summed with their signs before an absolute
value is taken. Applying absolute values fibre by fibre recreates the
dimension obstruction of `R-106123`.
