# T-108100 — The shared-fibre Wick positive trace descends exactly to an occupancy quotient

Status: **proved exact finite source theorem; positive fixed-fibre restriction closed; global signed conductor recombination, one-place trace, principal binding, RH and GRH remain open**

Branch base: PR #765 head `a30276a5be049749ebb2147f30f000dd5659298b`.

This checkpoint continues the shared-conductor marked-place route after the arbitrary-occupancy identity

\[
B_R=R^*S R-dI
\]

was established on the common \((\ell,\rho)\) fibre.  The previous packet
correctly warned that the *signed* Wick scalar is not determined by residue
aggregation when \(R\) has a kernel, because the literal atom diagonal is then
lost.  The conclusion-facing positive Hodge trace behaves better.

The main result is:

> **For every occupied fixed fibre, the complete positive part of the atom-level
> Wick operator is determined exactly by the residue aggregate and the cell
> multiplicities.  No injectivity of \(R\) is required.  All within-cell
> label/history directions are a pure negative scalar block and therefore
> contribute nothing to the positive trace.**

This is an operator theorem, not a finite-data extrapolation.

## 1. Fixed-fibre notation

Fix distinct odd primes \(\ell,\rho\) and one literal shared conductor fibre
\(\iota=(g,\ell,\rho,\sigma,\tau)\).  Let

\[
\Omega_\iota
\]

be the finite set of literal atoms present in that fibre and let

\[
r_\iota:\Omega_\iota\to\mathcal S_\iota
\]

be the physical residue map onto the **occupied** cell set
\(\mathcal S_\iota\).  Put

\[
(Rz)_a=\sum_{r_\iota(\omega)=a}z_\omega,
\qquad
D=RR^*=\operatorname{diag}(n_a),
\]

where

\[
n_a=\#r_\iota^{-1}(a)>0.
\]

Restrict the centered marked-place kernel to the occupied cells:

\[
S=(H_\ell\otimes H_\rho)_{\mathcal S_\iota},
\qquad
H_q=I-\frac1qJ.
\]

Its diagonal is constant:

\[
S_{aa}
=
d_{\ell,\rho}
=
\left(1-\frac1\ell\right)
\left(1-\frac1\rho\right)
=:d>0.
\]

The exact off-atomic Wick operator is

\[
\boxed{B_R=R^*SR-dI_{\Omega_\iota}.}
\tag{T-108100.1}
\]

All statements tensor unchanged with an arbitrary coefficient Hilbert space.

## 2. The canonical occupancy quotient

Define

\[
U=R^*D^{-1/2}:
\mathbf C^{\mathcal S_\iota}\longrightarrow
\mathbf C^{\Omega_\iota}.
\]

Because \(RR^*=D\),

\[
U^*U=I,
\qquad
\operatorname{ran}U=(\ker R)^\perp.
\]

Thus

\[
\mathbf C^{\Omega_\iota}
=
\operatorname{ran}U\oplus\ker R
\tag{T-108100.2}
\]

canonically and orthogonally.  Put

\[
\boxed{
Q_R=D^{1/2}SD^{1/2}-dI_{\mathcal S_\iota}.
}
\tag{T-108100.3}
\]

### Theorem L-108100 — exact block diagonalization

Under (T-108100.2),

\[
\boxed{
B_R
=
UQ_RU^*
\oplus
\left(-dI_{\ker R}\right).
}
\tag{T-108100.4}
\]

Equivalently,

\[
U^*B_RU=Q_R,
\qquad
B_R|_{\ker R}=-dI.
\]

**Proof.**  The first identity follows from

\[
\begin{aligned}
U^*B_RU
&=
D^{-1/2}R(R^*SR-dI)R^*D^{-1/2}\\
&=
D^{-1/2}(DSD-dD)D^{-1/2}\\
&=
D^{1/2}SD^{1/2}-dI.
\end{aligned}
\]

If \(z\in\ker R\), then \(B_Rz=-dz\).  The two reducing spaces are
orthogonal. \(\square\)

This is the canonical relative object promised by the Gate-0 ontology:

\[
0\longrightarrow\ker R
\longrightarrow\mathbf C^{\Omega_\iota}
\xrightarrow{\,R\,}
\mathbf C^{\mathcal S_\iota}
\longrightarrow0.
\tag{T-108100.5}
\]

The atom-level representation splits into a residue-occupancy quotient and
cellwise standard representations.

## 3. Positive Hodge restriction is residue sufficient

Since \(d>0\), the entire kernel block in (T-108100.4) is negative.  Functional
calculus therefore gives the exact formulas

\[
\boxed{
(B_R)_+=U(Q_R)_+U^*,
}
\tag{T-108100.6}
\]

\[
\boxed{
(B_R)_-=U(Q_R)_-U^*+dP_{\ker R}.
}
\tag{T-108100.7}
\]

Consequently, for every literal coefficient vector \(z\),

\[
\boxed{
\langle z,(B_R)_+z\rangle
=
\left\langle
D^{-1/2}Rz,\,
(Q_R)_+D^{-1/2}Rz
\right\rangle.
}
\tag{T-108100.8}
\]

In particular,

\[
\boxed{
\operatorname{tr}(B_R)_+
=
\operatorname{tr}(Q_R)_+,
\qquad
\operatorname{rank}(B_R)_+
\le|\mathcal S_\iota|.
}
\tag{T-108100.9}
\]

This is stronger than the earlier injectivity criterion, without contradicting
it:

* the full signed scalar \(\langle z,B_Rz\rangle\) still needs the literal
  within-cell diagonal;
* the conclusion-facing **positive** scalar does not;
* all information discarded by \(R\) lies in a strictly negative block.

Thus same-cell collisions, histories, Boolean decorations and owner labels may
be aggregated before taking the positive Hodge trace, provided they remain
inside one literal shared conductor fibre and their cell multiplicities are
retained.

## 4. Exact fibre variance debt

Let

\[
\bar z_a=\frac1{n_a}\sum_{r(\omega)=a}z_\omega.
\]

The orthogonal kernel projection satisfies

\[
\boxed{
\|P_{\ker R}z\|^2
=
\sum_{a\in\mathcal S_\iota}
\sum_{r(\omega)=a}|z_\omega-\bar z_a|^2.
}
\tag{T-108100.10}
\]

Hence the part discarded by residue aggregation is exactly

\[
\boxed{
-d
\sum_a\sum_{r(\omega)=a}|z_\omega-\bar z_a|^2.
}
\tag{T-108100.11}
\]

There is no hidden positive history debt.  This is the precise fixed-fibre
version of “integrate/aggregate before taking the positive Hodge square.”

## 5. Relative trace balance

Because \(S_{aa}=d\),

\[
\operatorname{tr}(R^*SR)
=
\operatorname{tr}(SD)
=
d|\Omega_\iota|.
\]

Therefore

\[
\boxed{\operatorname{tr}B_R=0.}
\tag{T-108100.12}
\]

On the quotient,

\[
\boxed{
\operatorname{tr}Q_R
=
d\left(|\Omega_\iota|-|\mathcal S_\iota|\right)
=
d\dim\ker R.
}
\tag{T-108100.13}
\]

The quotient trace is exactly the opposite of the negative standard-fibre
trace.  Equivalently,

\[
\operatorname{tr}(Q_R)_+
=
d\dim\ker R+\operatorname{tr}(Q_R)_-.
\tag{T-108100.14}
\]

This gives a finite relative Euler/Hodge balance:

```text
within-cell standard representations:  pure negative mass -d;
residue occupancy quotient:            equal compensating total trace;
full Wick operator:                     traceless.
```

It does **not** imply that the positive quotient trace is small.  It identifies
the only place where it can live.

## 6. Functoriality and the partial-Frobenius occupancy obstruction

Let a candidate marked-place operation induce a cell permutation

\[
\sigma:\mathcal S_\iota\to\mathcal S_{\iota'}
\]

with

\[
P_\sigma^*S_{\iota'}P_\sigma=S_\iota.
\]

A bijection

\[
\varphi:\Omega_\iota\to\Omega_{\iota'}
\]

lifts it source-faithfully exactly when

\[
r_{\iota'}\circ\varphi=\sigma\circ r_\iota.
\tag{T-108100.15}
\]

Then

\[
R_{\iota'}P_\varphi=P_\sigma R_\iota,
\qquad
P_\varphi^*B_{R_{\iota'}}P_\varphi=B_{R_\iota},
\tag{T-108100.16}
\]

and the quotient operators are unitarily conjugate.

### Theorem L-108101 — orbitwise occupancy criterion

For a fixed cell permutation \(\sigma\), a bijective atom lift satisfying
(T-108100.15) exists **if and only if**

\[
\boxed{
n_a=n_{\sigma(a)}
\quad\text{for every occupied cell }a.
}
\tag{T-108100.17}
\]

Necessity is cardinality.  For sufficiency, choose arbitrary bijections between
the equally sized fibres \(r^{-1}(a)\) and \(r^{-1}(\sigma(a))\), consistently
around each orbit.

Thus the first finite obstruction to a literal partial-Frobenius lift is not
mysterious sheaf theory: it is orbitwise occupancy invariance.  If it fails,
no bijective source lift exists.  If it holds, the finite source representation
and its positive quotient are equivariant; geometric realization and uniform
trace bounds remain separate questions.

Cell-preserving history permutations have \(\sigma=1\).  They act trivially on
the quotient and only on the negative standard-fibre block.

## 7. What this closes and what remains

This checkpoint closes the fixed-fibre positive-restriction problem:

```text
arbitrary atom multiplicity                 retained exactly
within-cell collision/history directions   pure negative scalar block
positive atom-level Wick trace              exact occupancy-quotient trace
injectivity of residue aggregation          unnecessary for positive trace
fixed-fibre label-to-residue restriction    closed
partial-Frobenius finite lift obstruction   orbitwise occupancy equality
```

It does not close:

```text
native live occupancy census;
signed recombination between conductor/history fibres;
construction of a global partial-Frobenius sheaf or complex;
ONEPLACEWEIL / ONEPLACETRACE / RELTRACE;
Kummer mixed channels;
principal binding;
RH or GRH.
```

The next conclusion-facing object is now strictly smaller.  For every live
fibre one must estimate only

\[
\boxed{
\left(
D_\iota^{1/2}
(H_\ell\otimes H_\rho)_{\mathcal S_\iota}
D_\iota^{1/2}
-d_{\ell,\rho}I
\right)_+,
}
\tag{T-108100.18}
\]

then recombine those quotient currents with their literal signed conductor
coefficients **before** an outer absolute value.

The old atom-level positive restriction and the apparent injectivity barrier
are no longer open.

## Replay boundary

The bounded replay verifies the rational block identities, trace balance,
history gauge, two arbitrary-occupancy fixtures and the orbitwise lift
criterion.  A pure-Python Jacobi diagonalization checks the positive-part
functional-calculus identity as a deterministic regression witness only.

```text
PASS_T108100_SHARED_FIBRE_POSITIVE_QUOTIENT
```

No finite replay proves global occupancy, trace estimates, principal binding,
RH or GRH.
