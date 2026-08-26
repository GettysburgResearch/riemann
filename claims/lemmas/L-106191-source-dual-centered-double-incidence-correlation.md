# L-106191 — Source-dual rescaling gives an exact centered double-incidence correlation

Claim ID: `L-106191`  
Programme aliases: `LFAM1.SOURCE_DUAL_PHASE_NORMALIZATION`, `LFAM2.CENTERED_DOUBLE_INCIDENCE_KERNEL`, `STRESS.CONDUCTOR_COHERENCE_FIREWALL`  
Status: **PROVED EXACT NORMALIZATION; GLOBAL CORRELATION ESTIMATE OPEN**  
Created: 2026-08-25  
Depends on: `L-106120`, binding `R-106131`, `L-106190`, `T-106140`; corrected conductor warning `L-106123`, `R-106123`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

The Wick-centered additive trace in `T-106140` carries the exterior weight
`g^2 ell rho`. This lemma moves that weight into the source atoms exactly and
identifies the resulting object as a bounded centered double-incidence
correlation. The transformation is useful, but it does **not** by itself pay
the global conductor family: after rescaling, the individual coefficients no
longer contain the two least-prime factors.

## 1. Exact source-dual rescaling

Fix one complete bilateral fibre. Write

\[
 c=\ell u,
 \qquad d=\rho v,
\]

and

\[
 z_\omega(t)
 ={\gamma_\omega(t)\over g^2cd\sqrt{PQ}}
 ={\gamma_\omega(t)\over g^2\ell\rho uv\sqrt{PQ}}.
\tag{L-106191.1}
\]

Define the rescaled atom

\[
\boxed{
 \widetilde z_\omega(t)=g\ell\rho z_\omega(t)
 ={\gamma_\omega(t)\over guv\sqrt{PQ}}.
}
\tag{L-106191.2}
\]

For the physical residue coordinates `x_omega mod ell` and
`y_omega mod rho`, put

\[
\begin{aligned}
 \mathcal W_{h,k}(t)
 &=\sum_\omega z_\omega(t)e_\ell(hx_\omega)e_\rho(ky_\omega),\\
 \widetilde{\mathcal W}_{h,k}(t)
 &=\sum_\omega \widetilde z_\omega(t)
   e_\ell(hx_\omega)e_\rho(ky_\omega),\\
 D(t)&=\sum_\omega|z_\omega(t)|^2,
 \qquad
 \widetilde D(t)=\sum_\omega|\widetilde z_\omega(t)|^2.
\end{aligned}
\]

Since `widetilde W=g ell rho W` and
`widetilde D=g^2 ell^2 rho^2 D`, one has coefficientwise

\[
\boxed{
\begin{aligned}
&g^2\ell\rho
\left[
 \sum_{h=1}^{\ell-1}\sum_{k=1}^{\rho-1}|\mathcal W_{h,k}(t)|^2
 -(\ell-1)(\rho-1)D(t)
\right]\\
&\quad={1\over\ell\rho}
\left[
 \sum_{h=1}^{\ell-1}\sum_{k=1}^{\rho-1}
 |\widetilde{\mathcal W}_{h,k}(t)|^2
 -(\ell-1)(\rho-1)\widetilde D(t)
\right].
\end{aligned}
}
\tag{L-106191.3}
\]

Thus the exterior source-dual factor is exactly the natural
`1/(ell rho)` normalization of the rescaled two-phase family.

## 2. Centered double-incidence kernel

Let

\[
 K_q(a)=\sum_{h=1}^{q-1}e_q(ha)
 =q\mathbf1_{a=0}-1.
\tag{L-106191.4}
\]

Expanding the right side of (L-106191.3), the atomic terms cancel and give

\[
\boxed{
\begin{aligned}
&{1\over\ell\rho}
\left[
 \sum_{h,k}|\widetilde{\mathcal W}_{h,k}|^2
 -(\ell-1)(\rho-1)\widetilde D
\right]\\
&\quad=\sum_{\omega\ne\omega'}
 \widetilde z_\omega\overline{\widetilde z_{\omega'}}
 \left(\mathbf1_{x_\omega=x_{\omega'}}-{1\over\ell}\right)
 \left(\mathbf1_{y_\omega=y_{\omega'}}-{1\over\rho}\right).
\end{aligned}
}
\tag{L-106191.5}
\]

Each centered incidence factor has modulus at most one. The literal diagonal
is absent coefficientwise; it is not bounded after an independent conductor
sum. Equation (L-106191.5) is the normalized additive coordinate of the
connected collision algebra in `L-106190`.

## 3. Exact global rewrite of the additive gate

Let `mathfrak C_SD(Y)` be the complete source recombination, Mellin integral
and dyadic sum of the right side of (L-106191.5), with exactly the same fibre
labels and order of summation as `mathfrak A^circ(Y)` in `T-106140`. Then

\[
\boxed{
 \mathfrak C_{\rm SD}(Y)=\mathfrak A^\circ(Y).
}
\tag{L-106191.6}
\]

Define

```text
WCCORR106191:
  with the complete source/conductor recombination performed before the
  absolute value,

      |C_SD(Y)| = Y^o(1).
```

The identity proves

\[
\boxed{
 \mathrm{WCCORR}_{106191}
 \Longleftrightarrow
 \mathrm{WCADD}_{106140}.
}
\tag{L-106191.7}
\]

This is a change to the exact target, not a proof of the target.

## 4. Why a source-blind energy estimate is invalid

The rescaled coefficient satisfies only

\[
 |\widetilde z_\omega(t)|^2
 \ll Y^{o(1)}{1\over g^2u^2v^2PQ}.
\tag{L-106191.8}
\]

When `c=ell` and `d=rho`, one has `u=v=1`; the individual coefficient then
has no decay in either phase prime. `L-106123` and `R-106123` already prove
that power-many conductor pairs are compatible with the live family. Hence
neither

\[
 \sum_{\iota,\omega}|\widetilde z_{\iota,\omega}|^2=Y^{o(1)}
\]

nor a source-blind Schur/Cauchy estimate of (L-106191.5) follows from the
literal coefficient bound. Any such assertion would reproduce the invalid
fixed-fibre-to-global promotion corrected by `R-106123`.

The bounded kernel in (L-106191.5) therefore isolates the real issue:
**coherent cancellation across the least-prime conductor family**.

## 5. Exact equal/distinct-output decomposition

Let `nu(omega)` denote the complete physical-output label used by the parent
balanced-Vaughan/equal-product partition. Split (L-106191.5) exactly into

```text
EQ:    nu(omega)=nu(omega'), omega!=omega';
DIST:  nu(omega)!=nu(omega').
```

After the complete global recombination write

\[
 \boxed{
 \mathfrak C_{\rm SD}
 =\mathfrak C_{\rm EQ}+\mathfrak C_{\rm DIST}.
 }
\tag{L-106191.9}
\]

Define the stronger diagnostic gates

```text
WCEQ106191:    |C_EQ(Y)|   = Y^o(1);
WCDIST106191:  |C_DIST(Y)| = Y^o(1).
```

Then

\[
\boxed{
 \mathrm{WCEQ}_{106191}\wedge\mathrm{WCDIST}_{106191}
 \Longrightarrow
 \mathrm{WCCORR}_{106191}
 \Longleftrightarrow
 \mathrm{WCADD}_{106140}.
}
\tag{L-106191.10}
\]

The converse is not asserted: cancellation between `EQ` and `DIST` is allowed
in the canonical gate.

Parent `L-102883` pays the unrescaled stopped-Vaughan free energy and its
equal-product collapse. Transferring that theorem to `C_EQ` requires an
additional least-prime/cofactor occupancy argument compatible with the
rescaling (L-106191.2). It is not automatic, because the dangerous
`u=v=1` conductor family has lost both least-prime denominators. This file
therefore does not mark `WCEQ106191` closed.

## 6. Boundary

```text
source-dual rescaling                              PROVED EXACT
centered double-incidence expansion                PROVED EXACT
literal atomic cancellation                        PROVED EXACT
WCCORR106191 = WCADD106140                         PROVED EXACT
source-blind rescaled free-energy estimate         INVALID / NOT CLAIMED
WCEQ106191 equal-output occupancy                  OPEN
WCDIST106191 distinct-output coherence             OPEN
WCKUM106140 centered Kummer defect                 OPEN
Riemann Hypothesis                                 UNPROVED
```
