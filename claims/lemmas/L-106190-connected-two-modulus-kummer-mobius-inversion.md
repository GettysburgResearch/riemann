# L-106190 — Connected two-modulus Kummer–Möbius inversion cancels the frame dimension

Claim ID: `L-106190`  
Programme aliases: `LFAM1.CONNECTED_KUMMER_CUMULANT`, `LFAM2.TWO_COORDINATE_RESIDUE_MOBIUS`, `STRESS.ATOMIC_FREE_FAMILY_COMBINATION`  
Status: **PROVED EXACT HILBERT-VALUED IDENTITY**  
Created: 2026-08-25  
Depends on: additive orthogonality; `L-106120`; binding corrections `R-106124`, `R-106131`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

This is the canonical, disambiguated home of the connected two-coordinate
identity. Its first filename used `L-106131`, colliding with the binding
Wick-normal-ordering lemma. The renumbering changes no mathematics.

Let `ell` and `rho` be distinct odd primes. Let `(z_i)` be a finite packet in
a complex Hilbert space, with residue coordinates

\[
 x_i\in\mathbf F_\ell,
 \qquad y_i\in\mathbf F_\rho.
\]

Define

\[
 T=\left\|\sum_i z_i\right\|^2
\tag{L-106190.1}
\]

and the three residue-cell Grams

\[
\begin{aligned}
 C_\ell&=\sum_{x_i=x_j}\langle z_i,z_j\rangle,\\
 C_\rho&=\sum_{y_i=y_j}\langle z_i,z_j\rangle,\\
 C_{\ell\rho}&=\sum_{\substack{x_i=x_j\\y_i=y_j}}
 \langle z_i,z_j\rangle.
\end{aligned}
\tag{L-106190.2}
\]

Each is nonnegative, being a sum of squared residue-cell vectors.

## 1. Complete nonzero two-phase energy

Put

\[
 F_{h,k}=\sum_i z_i e_\ell(hx_i)e_\rho(ky_i),
 \qquad 1\le h<\ell,\quad1\le k<\rho,
\]

and

\[
 E_{11}=\sum_{h=1}^{\ell-1}\sum_{k=1}^{\rho-1}\|F_{h,k}\|^2.
\]

Two applications of additive orthogonality give

\[
\boxed{
 E_{11}=\ell\rho C_{\ell\rho}-\ell C_\ell-\rho C_\rho+T.
}
\tag{L-106190.3}
\]

Hence Möbius inversion on the Boolean lattice of the two phase coordinates
gives

\[
\boxed{
 T=E_{11}+\ell C_\ell+\rho C_\rho-\ell\rho C_{\ell\rho}.
}
\tag{L-106190.4}
\]

This is an exact signed identity, not an inequality obtained by subtracting
unrelated positive bounds.

## 2. Equivalent one-phase form

Let

\[
 E_{10}=\sum_{h=1}^{\ell-1}\left\|\sum_i z_i e_\ell(hx_i)\right\|^2
\]

and define `E_01` analogously. Then

\[
 E_{10}=\ell C_\ell-T,
 \qquad E_{01}=\rho C_\rho-T,
\]

so (L-106190.3) is equivalently

\[
\boxed{
 T=\ell\rho C_{\ell\rho}-E_{11}-E_{10}-E_{01}.
}
\tag{L-106190.5}
\]

## 3. Atomic-free connected form

Put

\[
 D=\sum_i\|z_i\|^2.
\]

The atomic contributions are

\[
 T_{\rm at}=D,
 \qquad (C_\ell)_{\rm at}=(C_\rho)_{\rm at}
 =(C_{\ell\rho})_{\rm at}=D,
\]

and

\[
 (E_{11})_{\rm at}=(\ell-1)(\rho-1)D.
\]

Define

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
 T^\circ=E_{11}^\circ+\ell C_\ell^\circ+\rho C_\rho^\circ
 -\ell\rho C_{\ell\rho}^\circ.
}
\tag{L-106190.6}
\]

The atomic coefficient before centering is

\[
 (\ell-1)(\rho-1)+\ell+\rho-\ell\rho=1,
\]

and is zero after centering. Thus the large frame dimension identified by
`R-106124` and `R-106131` is cancelled coefficientwise rather than estimated.

## 4. Kummer/character meaning

For a packet supported on the two declared Kummer squareclass sectors,
`E_11` is exactly the complete positive even-character tensor frame of
`L-106120`. The collision Grams are the one-coordinate and joint physical
squareclass ledgers. Therefore (L-106190.4) says

```text
principal physical member
  = complete nonzero tensor frame
    + two one-coordinate collision ledgers
    - joint collision ledger.
```

The negative joint term is indispensable. Bounding all four ingredients
separately by positive majorants reintroduces the conductor-family dimension
which the identity cancels.

## 5. Scope

The lemma repairs the exact normalization and removes the false atomic burden
of the full positive tensor moment. It does not estimate the connected
off-atomic combination (L-106190.6). Its application to the bilateral Boolean
source is `T-106130`. The distinct Wick-centered complete-family identity is
canonical `L-106131` and feeds `T-106140`.
