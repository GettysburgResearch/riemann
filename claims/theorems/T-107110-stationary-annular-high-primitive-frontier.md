# T-107110 — Stationary annular high-primitive frontier

**Claim ID:** `T-107110`  
**Status:** unconditional detector and range reductions; final signed estimate open  
**Date:** 2026-08-31  
**RH:** unproved

The moving finite-feature annular criterion of `T-107100` has a stationary
counterpart with a fixed compact ratio-67 kernel.

For

\[
\Lambda_{67}(v)=\left(1-{|v|\over\log67}\right)_+,
\]

define

\[
\mathfrak Q_{67}(X)
 =\max_{Y\le X}
 \sum_{\substack{m,n\le Y\\67\nmid mn}}
 {\mu(m)\mu(n)\over\sqrt{mn}}
 \Lambda_{67}\!\left(\log{m\over n}\right).
\]

Then

\[
\boxed{
\limsup_{X\to\infty}
{\log(1+\mathfrak Q_{67}(X))\over\log X}
=2\Theta-1.
}
\tag{T-107110.1}
\]

Consequently

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\mathfrak Q_{67}(X)=X^{o(1)}.
}
\tag{T-107110.2}
\]

The same exponent is obtained with the literal beta coefficients. The
unconditional Vinogradov--Korobov estimate gives the inherited
stretched-exponential saving.

Fix any `A>0` and put

\[
R_Y=(\log(eY))^A.
\]

By `L-107112`,

\[
\mathfrak Q_{67}(Y)
 =\mathcal H_A(Y)+Y^{o(1)},
\]

where

\[
\boxed{
\begin{aligned}
\mathcal H_A(Y)
={}&\sum_{\substack{d\le Y/R_Y\\d\ {m sf},\ 67\nmid d}}{1\over d}
\sum_{\substack{R_Y<a,b\le Y/d\\
(a,b)=1,\ (ab,67d)=1}}
 {\mu(a)\mu(b)\over\sqrt{ab}}
 \Lambda_{67}\!\left(\log{a\over b}\right).
\end{aligned}}
\tag{T-107110.3}
\]

The compact kernel automatically imposes

\[
67^{-1}\le a/b\le67.
\]

Thus

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\max_{Y\le X}|\mathcal H_A(Y)|=X^{o(1)}.
}
\tag{T-107110.4}
\]

The final target is one assembled, signed, high-primitive common-core
interference. It contains:

```text
no moving Poisson grid;
no low primitive rays;
no diagonal;
no terminal common-core tail;
no separately squared exceptional 67 channels.
```

It retains the literal Möbius signs, pairwise coprimality and every common-core
interaction before any positive corewise norm is formed.

## Revised Architecture A

```text
native beta
  -> stable 67-free central source
  -> stationary shifted-annulus coarea
  -> fixed triangular ratio-67 kernel
  -> absolute removal of shallow rays and terminal cores
  -> H_A high-primitive signed interference
  -> RH.
```

Every arrow before `H_A` is proved. The estimate in (T-107110.4) remains open
and RH-bearing.

## Exact status

```text
stationary q-adic coarea                    PROVED EXACT
fixed triangular positive kernel            PROVED EXACT
zero-abscissa exponent 2 Theta-1             PROVED
literal beta / 67-free equivalence           PROVED
shallow primitive rays                       PROVED POLYLOG
terminal common cores                        PROVED POLYLOG
high-primitive interference H_A              OPEN / RH-EQUIVALENT
Riemann Hypothesis                           UNPROVEN
```