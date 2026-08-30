# The common-gcd Fourier mode decouples into two one-variable divisor modes

Status: **exact local and global Euler-factor decoupling for the untruncated
gcd-wave Fourier model; critical coupling is absolutely summable; finite
small-prime firewall; no sharp-hyperbola mean estimate, HIGHFARGCDWAVE, HIGHGCDWAVE, RH, or
GRH**

Architecture: **Architecture A only**.

Bounded replay:
[`ffps_gcd_wave_mode_decoupling.py`](ffps_gcd_wave_mode_decoupling.py).
Canonical fixture:
[`ffps_gcd_wave_mode_decoupling.json`](ffps_gcd_wave_mode_decoupling.json).

Frozen inputs are the shared-divisor gcd Gram, high-ray localization, and
shifted-zeta Fourier-mode packets at PR #760 head
`680be76bd31acdd96925d0b73f1a469226a19c9f`.

## 0. Outcome

The high primitive obstruction is

\[
 \sum_g{\kappa_2(g)\over g}
 \sum_{(a,b)=(ab,g)=1}{\mu(a)\mu(b)\over\sqrt{ab}}
 \sum_I\mathcal W_I(ga)\overline{\mathcal W_I(gb)}.
\tag{0.1}
\]

The common gcd `g` has no Möbius sign.  Nevertheless it creates no new
critical Euler obstruction before the sharp height cutoff.

For real Fourier frequencies `xi,eta`, write

\[
 A_p(\xi)=p^{i\xi}+p^{-i\xi},\qquad
 B_p(\eta)=p^{i\eta}+p^{-i\eta},
\tag{0.2}
\]

and define the pairwise-coprime squarefree generating series

\[
\begin{aligned}
 \mathcal G_{\xi,\eta}(s,t)
 =\sum_{g,a,b}{
 \kappa_2(g)\mu(a)\mu(b)
 D_\xi(ga)D_\eta(gb)
 \over g^{s+t}a^sb^t},
\end{aligned}
\tag{0.3}
\]

where `(g,a,b)` are pairwise coprime, squarefree, and prime to `67`.
Its local factor is

\[
 L_p=1-A_px-B_py+\left(1+{2\over p}\right)A_pB_pxy,
 \quad x=p^{-s},\ y=p^{-t}.
\tag{0.4}
\]

The two one-variable divisor modes have local factors

\[
 L_{p,x}=1-A_px,
 \qquad
 L_{p,y}=1-B_py.
\tag{0.5}
\]

Therefore

\[
\boxed{
 L_p=L_{p,x}L_{p,y}+{2\over p}A_pB_pxy.}
\tag{0.6}
\]

Equivalently,

\[
\boxed{
 \mathcal G_{\xi,\eta}(s,t)
 =\mathcal H_{\xi,\eta}(s,t)
 F_\xi(s)F_\eta(t),}
\tag{0.7}
\]

with

\[
 \mathcal H_{\xi,\eta}(s,t)
 =\prod_{p\ne67}
 \left(
 1+{2A_p(\xi)B_p(\eta)p^{-1-s-t}
 \over(1-A_p(\xi)p^{-s})(1-B_p(\eta)p^{-t})}
 \right).
\tag{0.8}
\]

For `p>=5` and `Re(s),Re(t)>=1/2`, both denominators are nonzero because
`2/sqrt(p)<1`, and

\[
 |H_p-1|\ll p^{-2}.
\tag{0.9}
\]

Thus the **critical coupling is absolutely summable**.  After deleting the
finite primes at most `13` together with `67`, the product (0.8) is normal and
nonzero on the closed critical product half-plane.  Those finitely many local
states may be restored as a finite Boolean decomposition.  This is the
**small-prime firewall**.

Call (0.7) `MODE-DECOUPLING`.  It proves that all critical zero response in
the untruncated gcd-wave model lies in two independent one-variable divisor
modes.  The positive common-gcd weight contributes only a harmless convergent
Euler correction.

Combining (0.7) with the free-Lie/Witt packet gives, for every finite depth
`R`,

\[
\begin{aligned}
 \mathcal G_{\xi,\eta}(s,t)
 ={}&\mathcal H_{\xi,\eta}(s,t)
 E_{R,\xi}(s)E_{R,\eta}(t)\\
 &\times
 \prod_{n\le R}\prod_{a+b=n}
 \zeta^{(67)}(ns-i(a-b)\xi)^{-\ell_{a,b}}\\
 &\times
 \prod_{n\le R}\prod_{a+b=n}
 \zeta^{(67)}(nt-i(a-b)\eta)^{-\ell_{a,b}}.
\end{aligned}
\tag{0.10}
\]

The corrections `E_R` are normal for `Re(s),Re(t)>1/(R+1)` and the mixed
factor `H` is already normal at the critical boundary.

This does not prove the sharp wavelet estimate.  The **sharp hyperbola cutoff**
breaks multiplicativity and becomes a Perron/Fourier integral of the factors
in (0.10).  The remaining target is a joint shifted-mode mean estimate for
two one-variable reciprocal-zeta/Witt towers, with the dyadic height blocks
and endpoint removal retained.

## 1. Local proof

At one prime there are exactly four admissible states:

```text
absent: 1;
in a:   -A_p x;
in b:   -B_p y;
in g:   (1+2/p) A_p B_p x y.
```

The product of the one-variable local factors has the same first three states
and cross coefficient `A_pB_pxy`.  Their difference is precisely
`(2/p)A_pB_pxy`, proving (0.6).

No asymptotic formula or cancellation theorem enters.

## 2. Critical convergence

For `sigma=Re(s), tau=Re(t)>=1/2`,

\[
 |A_pp^{-s}|\le2p^{-1/2},\qquad
 |B_pp^{-t}|\le2p^{-1/2}.
\tag{2.1}
\]

For every sufficiently large prime the denominators in (0.8) are uniformly
bounded below, while its numerator is at most `8p^(-1-sigma-tau)<=8p^-2`.
Hence the tail logarithm converges absolutely and uniformly.  Removing a
fixed finite set makes every local perturbation smaller than one, so the tail
product is nonzero.

The finite local factors can vanish only on an explicitly finite set of prime
states.  They cannot create a growing conductor or height loss.

## 3. Exact remaining analytic gate

A smoothed upper-height condition is represented by Mellin/Perron shifts
`u,v`; the two Fourier-expanded wavelets then contain

\[
 \mathcal G_{\xi,\eta}(1/2+u,1/2+v).
\tag{3.1}
\]

By (0.7), this is a convergent coupling times

\[
 F_\xi(1/2+u)F_\eta(1/2+v).
\tag{3.2}
\]

Thus a faithful next theorem is a mean-square or signed bilinear estimate for
the two one-variable modes over the joint Fourier/Perron measure, uniform in
the high balanced gcd sector.  Unsmoothing must then restore the exact dyadic
block endpoints.

A pointwise bound for every `xi,eta,u,v,g` is much stronger than necessary.
The target remains the assembled signed block sum.

**HIGHFARGCDWAVE remains open.**

## 4. Scope firewall

- `MODE-DECOUPLING` concerns the untruncated multiplicative Fourier model.
- The coupling correction is harmless, but each one-variable mode remains
  RH-sensitive.
- The sharp hyperbola and dyadic endpoint operators are not multiplicative.
- Normal convergence does not bound reciprocal zeta factors near zeros.
- No Architecture B input is used.

**No shifted-mode mean theorem, HIGHGCDWAVE, OFFGCDWAVE, COREAGG, PRIMCAR, RH,
or GRH is proved.  RH and GRH remain unproved.**

## 5. Proof ledger

| statement | grade |
|---|---|
| local four-state factor (0.4) | **PROVED EXACT** |
| local decoupling (0.6) | **PROVED EXACT** |
| global absolute-domain identity (0.7) | **PROVED** |
| critical normal convergence of `H` | **PROVED** |
| small-prime firewall | **PROVED** |
| sharp hyperbola shifted-mode estimate | **NOT PROVED** |
| RH / GRH | **NOT PROVED** |

## 6. Bounded replay

```text
python -B research/l-families/atlas/function_field/ffps_gcd_wave_mode_decoupling.py --check
python -B -O research/l-families/atlas/function_field/ffps_gcd_wave_mode_decoupling.py --check
python -B -m unittest tests.test_ffps_gcd_wave_mode_decoupling
python -B -O -m unittest tests.test_ffps_gcd_wave_mode_decoupling
```
