# T-108330 — Exact Xi tails and every current saddle input permit arbitrarily many low-order defects

Claim ID: `T-108330`  
Status: **PROVED ANALYTIC NO-GO THEOREM; CURRENT LOCAL-SOURCE ROUTE RETIRED**  
Created: 2026-08-31  
Depends on: the standard positive Xi Fourier kernel; the saddle and source-frequency interfaces imported on PRs #765, #767 and #773  
RH status: **unproved**

## 1. Statement

Let

\[
\Xi(t)=\int_{\mathbb R}\Phi_\Xi(u)e^{itu}\,du,
\qquad \Phi_\Xi(u)>0,
\]

use the standard full-line Xi kernel. For every integer `M>=1` there is an
even, strictly positive, smooth Fourier kernel

\[
\widetilde\Phi_M\in C^\infty(\mathbb R),
\qquad
\widetilde\Phi_M(u)=\Phi_\Xi(u)
\quad (|u|>L_M),
\tag{T-108330.1}
\]

whose cosine transform

\[
F_M(t)=\int_{\mathbb R}\widetilde\Phi_M(u)e^{itu}\,du
\]

has a compact real interval `I_M` on which

```text
F_M has no real zero;
F_M' has at least M simple zeros;
every one of those zeros is an upward zero of F_M'/F_M;
the multiplicity-sensitive reverse–Rolle defect is at least 2M.
```

At the same time `F_M` retains all of the following asymptotic inputs used by
the current Xi source/saddle programmes:

1. the exact Xi Fourier tail outside one compact set;
2. the complete high-derivative saddle concentration and growing-window
   cosine limit, with the same leading saddle and width;
3. for every fixed positive odd endpoint order `K`, the same
   source-frequency concentration, carrier-adapted limit `1/(2K)`, and
   near-adapted-scale law as the actual Xi kernel.

Consequently no theorem whose hypotheses consist only of

```text
positive smooth Fourier source;
exact Xi tail outside a compact set;
high-derivative saddle concentration and real-rooted entry;
all fixed-odd carrier-adapted source constants;
```

can prove `XI31MINPHASE108310`, `XI31WIND108320`, a fixed positive percentage,
or RH. A conclusion requires a genuinely global Xi input, such as the
safe-line prime phase with its full argument-principle boundary ledger, not
another local source-concentration estimate.

## 2. Construction

Fix an even nonnegative `C-infinity` probability density `beta` supported on
`[-h,h]`, where

\[
h={1\over8},
\qquad
B(t)=\int\beta(u)e^{itu}\,du.
\]

On the real axis,

\[
B(t)\ge1-{h^2t^2\over2},
\qquad
|B'(t)|\le h,
\qquad
|B''(t)|\le h^2.
\tag{T-108330.2}
\]

Choose an integer

\[
n\ge64M
\]

and put

\[
q_n(t)=2+\cos(nt),
\qquad
F_M(t)=\Xi(t)+B(t)q_n(t).
\tag{T-108330.3}
\]

Its Fourier kernel is

\[
\boxed{
\widetilde\Phi_M(u)
=
\Phi_\Xi(u)
+2\beta(u)
+{1\over2}\beta(u-n)
+{1\over2}\beta(u+n).
}
\tag{T-108330.4}
\]

It is smooth, even and strictly positive, and agrees exactly with the Xi
kernel for `|u|>n+h`.

## 3. At least `M` literal wrong extrema

Take

\[
I_M=[0,2\pi M/n]
\]

and

\[
t_j={(2j+1)\pi\over n},
\qquad 0\le j<M.
\]

Let `delta=1/4` and

\[
J_j=[t_j-\delta/n,t_j+\delta/n].
\]

The intervals are pairwise disjoint and lie in the interior of `I_M`.
Since `n>=64M` and `pi<4`, throughout `I_M`

\[
ht\le {1\over64},
\qquad
B(t)>{31\over32}.
\tag{T-108330.5}
\]

The standard Xi kernel and `Xi(i/2)=1/2` give the elementary real bounds

\[
|\Xi(t)|\le{1\over2},
\qquad
|\Xi'(t)|\le1,
\qquad
|\Xi''(t)|\le4.
\tag{T-108330.6}
\]

Because `q_n>=1`, equations (T-108330.5)--(T-108330.6) imply

\[
F_M(t)>{31\over32}-{1\over2}>0
\qquad(t\in I_M).
\tag{T-108330.7}
\]

At the two endpoints of `J_j`, use

\[
\sin(1/4)>{1\over5},
\qquad
\cos(1/4)>{31\over32}.
\]

Then

\[
F_M'(t_j-\delta/n)<0,
\qquad
F_M'(t_j+\delta/n)>0.
\tag{T-108330.8}
\]

Indeed the main term `B q_n'` has magnitude at least `31n/160`, while
`|B'q_n|+|Xi'|<=3/8+1`.

For `t in J_j`,

\[
q_n''(t)\ge {31\over32}n^2,
\qquad
|q_n'(t)|\le {n\over4}.
\]

Hence

\[
\begin{aligned}
F_M''(t)
&=B''q_n+2B'q_n'+Bq_n''+\Xi''\\
&\ge {31\over32}n^2-{n\over16}-4-{3\over64}>0.
\end{aligned}
\tag{T-108330.9}
\]

Thus every `J_j` contains exactly one simple zero `c_j` of `F_M'`, and
`F_M'/F_M` crosses upward there. Each contributes exactly two units to the
reverse–Rolle defect. Therefore

\[
\boxed{
\mathfrak R_{I_M}(F_M)\ge2M,
\qquad
N_{I_M}(F_M)=0.
}
\tag{T-108330.10}
\]

## 4. Why all current local asymptotics survive

Let `L>n+h`. Since the Xi kernel is strictly positive on
`[2L,2L+1]`, its `k`-th moment is bounded below by `c_L(2L)^k`, while the
compact perturbation in (T-108330.4) contributes at most `C_LL^k`.
Consequently its relative contribution is `O_L(2^{-k})`. The same estimate
holds after multiplication by every fixed polynomial weight and by the
moderate-deviation exponential weights used in the high-derivative saddle
proof. Therefore the saddle location, variance, Gaussian tails and growing
real-zero window are unchanged.

For the fixed-odd source-frequency limit, the compact perturbation can enter
one convolution factor only when `|d|=xi+O_M(1)`. The unchanged Xi factor is
then evaluated at frequency `xi+O_M(1)` and is superexponentially smaller
than the central product at `d=0`. The all-real Xi tail estimate therefore
gives an exponentially negligible relative correction, with every fixed
polynomial or exponential difference weight. Hence the carrier-adapted limit
`1/(2K)` and its fixed-`K` concentration law are unchanged.

These are the same compact-perturbation estimates used in the reviewed
actual-kernel firewall on PR #765, now with an arbitrary number of certified
low-order defects.

## 5. Disposition

The exact companion and winding identities on PR #777 remain valid and useful
conclusion coordinates. What is retired is the attempted implication

```text
local positive Xi-source asymptotics
        -> endpoint-31 winding or minority phase.
```

The next viable theorem must use a global arithmetic phase or an exact
individual-Xi contour mechanism not shared by the family (T-108330.4).

```text
arbitrarily many low-order defects              PROVED
exact Xi tail retained                           PROVED
high-derivative saddle retained                  PROVED
all fixed-odd source constants retained          PROVED
local-source package -> winding                  REFUTED
XI31WIND108320                                   OPEN
more than 90 percent                             UNPROVED
RH                                               UNPROVED
```
