# L-106131 — Connected two-modulus Kummer–Möbius inversion cancels the frame dimension

Claim ID: `L-106131`  
Programme aliases: `LFAM1.CONNECTED_KUMMER_CUMULANT`, `LFAM2.TWO_COORDINATE_RESIDUE_MOBIUS`, `STRESS.ATOMIC_FREE_FAMILY_COMBINATION`  
Status: **PROVED EXACT HILBERT-VALUED IDENTITY**  
Created: 2026-08-25  
Depends on: additive orthogonality; `L-106120`; binding correction `R-106124`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

Let `ell` and `rho` be distinct odd primes.  Let `(z_i)` be a finite packet in
a complex Hilbert space, and attach residue coordinates

\[
 x_i\in\mathbf F_\ell,
 \qquad
 y_i\in\mathbf F_\rho.
\]

Define the principal norm

\[
 T=\left\|\sum_i z_i\right\|^2
\tag{L-106131.1}
\]

and the three residue-cell Grams

\[
\begin{aligned}
 C_\ell
 &=\sum_{x_i=x_j}\langle z_i,z_j\rangle,\\
 C_\rho
 &=\sum_{y_i=y_j}\langle z_i,z_j\rangle,\\
 C_{\ell\rho}
 &=\sum_{\substack{x_i=x_j\\y_i=y_j}}
   \langle z_i,z_j\rangle.
\end{aligned}
\tag{L-106131.2}
\]

Each is nonnegative: it is a sum of squared residue-cell vectors.

## 1. Complete nonzero two-phase energy

Put

\[
 F_{h,k}=\sum_i z_i e_\ell(hx_i)e_\rho(ky_i),
 \qquad
 1\le h<\ell,
 \quad1\le k<\rho,
\]

and

\[
 E_{11}=\sum_{h=1}^{\ell-1}
         \sum_{k=1}^{\rho-1}\|F_{h,k}\|^2.
\]

Two applications of additive orthogonality give

\[
\boxed{
 E_{11}
 =\ell\rho C_{\ell\rho}
  -\ell C_\ell
  -\rho C_\rho
  +T.
}
\tag{L-106131.3}
\]

Therefore Möbius inversion on the Boolean lattice of the two phase
coordinates yields

\[
\boxed{
 T
 =E_{11}
  +\ell C_\ell
  +\rho C_\rho
  -\ell\rho C_{\ell\rho}.
}
\tag{L-106131.4}
\]

This is an exact signed identity.  It is not an inequality obtained by
subtracting unrelated positive bounds.

## 2. Equivalent one-phase form

Let

\[
 E_{10}=\sum_{h=1}^{\ell-1}
 \left\|\sum_i z_i e_\ell(hx_i)\right\|^2,
\]

and define `E_01` analogously.  Then

\[
 E_{10}=\ell C_\ell-T,
 \qquad
 E_{01}=\rho C_\rho-T.
\]

Combining these equations with (L-106131.3) gives the alternative exact form

\[
\boxed{
 T=\ell\rho C_{\ell\rho}-E_{11}-E_{10}-E_{01}.
}
\tag{L-106131.5}
\]

The two displays are the same inclusion--exclusion identity in collision and
Fourier coordinates.

## 3. Atomic-free connected form

Put

\[
 D=\sum_i\|z_i\|^2.
\]

The atomic contributions are

\[
\begin{aligned}
 T_{\rm at}&=D,\\
 (C_\ell)_{\rm at}
 &=(C_\rho)_{\rm at}
 =(C_{\ell\rho})_{\rm at}=D,\\
 (E_{11})_{\rm at}
 &=(\ell-1)(\rho-1)D.
\end{aligned}
\]

Define the off-atomic centered quantities

\[
\begin{aligned}
 T^\circ&=T-D,\\
 C_\ell^\circ&=C_\ell-D,
 \qquad C_\rho^\circ=C_\rho-D,
 \qquad C_{\ell\rho}^\circ=C_{\ell\rho}-D,\\
 E_{11}^\circ&=E_{11}-(\ell-1)(\rho-1)D.
\end{aligned}
\]

Then

\[
\boxed{
 T^\circ
 =E_{11}^\circ
  +\ell C_\ell^\circ
  +\rho C_\rho^\circ
  -\ell\rho C_{\ell\rho}^\circ.
}
\tag{L-106131.6}
\]

The atomic coefficient on the right is

\[
 (\ell-1)(\rho-1)+\ell+\rho-\ell\rho=1,
\]

before centering, and zero after centering.  Thus the large frame dimension in
`R-106124` cancels coefficientwise rather than being estimated.

## 4. Kummer/character meaning

For a packet supported on the two declared Kummer squareclass sectors,
`E_11` is exactly the complete positive even-character tensor frame of
`L-106120`.  The collision Grams `C_ell`, `C_rho` and `C_(ell rho)` are the
one-coordinate and joint physical-squareclass collision ledgers.

Consequently (L-106131.4) says:

```text
principal physical member
  = complete nonzero tensor frame
    + two one-coordinate collision ledgers
    - joint collision ledger.
```

The negative joint term is indispensable.  Bounding all four ingredients
separately by positive majorants reintroduces the conductor-family dimension
which this identity cancels.

## 5. Scope

The lemma repairs the exact normalization and removes the false atomic burden
of the full positive tensor moment.  It does not estimate the connected
off-atomic combination (L-106131.6).  Its application to the literal bilateral
Boolean source and the resulting open theorem are `T-106130`.
