# T-106590 — Macroscopic endpoint height collapses to one shallow companion correlation

Claim ID: `T-106590`  
Status: **UNCONDITIONAL HEIGHT/LOCALIZATION THEOREMS + ONE FIXED SHALLOW-CORRELATION GATE**  
Created: 2026-08-25  
Updated: 2026-08-25  
Depends on: Selberg's zero-density theorem; `L-106500--L-106514`; `L-106591`; finite model-space factorization; pinned `R_5/N>997/1000-o(1)` input  
RH status: **unproved**

This packet is deliberately numbered outside the independently occupied
`T-106550` spectral-pressure namespace.

## 1. Unconditional horizontal first moment

For zeta zeros `rho=beta+i gamma`, counted with multiplicity, define

\[
\mathfrak h_\zeta(T)
 =\sum_{T<\gamma\le2T}
  \left|\beta-\frac12\right|.
\]

Functional-equation symmetry gives

\[
\boxed{
\mathfrak h_\zeta(T)
 =2\int_{1/2}^{1}N(\sigma;T,2T)\,d\sigma.
}
\tag{T-106590.1}

Selberg's uniform density estimate

\[
N(\sigma,X)
 \ll X^{1-\frac14(\sigma-1/2)}\log X
\]

therefore yields

\[
\boxed{
\mathfrak h_\zeta(T)=O(T)=o(N(T,2T)).
}
\tag{T-106590.2}

In the centered Xi variable this is the total vertical-height mass of the Xi
zero divisor in the dyadic real window.

For fixed `A>0`, the same estimate gives

\[
N\!\left(\frac12+{A\over\log T};T,2T\right)
 \ll e^{-A/4}N(T,2T).
\tag{T-106590.3}

Thus every power-sized off-line population is forced into the natural
`1/log T` strip.

## 2. Exact finite height and model-space facts

For a polynomial `p`, differentiator compression and Ky Fan's principle give

\[
\mathfrak h_+(p^{(k)})\le\mathfrak h_+(p).
\tag{T-106590.4}

The matrix determinant lemma gives the finite-alpha companion bounds

\[
\begin{aligned}
\mathfrak h_+(p+i\lambda p')&\le\mathfrak h_+(p),\\
\mathfrak h_+(p-i\lambda p')&\le\mathfrak h_+(p)+\lambda\deg p.
\end{aligned}
\tag{T-106590.5}

For a reduced finite endpoint symbol

\[
U=\omega B_+\overline{B_-}
\]

factor the denominator inner function by height,

\[
B_-=B_{\le\eta}B_{>\eta}.
\]

The model space splits orthogonally and the exact all-pass charge obeys

\[
\boxed{
\|H_U\|_{S_2}^2
 =\mathcal C_{\le\eta}(U)+\mathcal C_{>\eta}(U),
\qquad
\mathcal C_{>\eta}(U)
 \le{\sum_{B_-(a+iy)=0}y\over\eta}.
}
\tag{T-106590.6}

Here

\[
\mathcal C_{\le\eta}(U)
 =\|P_{K_{B_{\le\eta}}}T_{B_+}\|_{S_2}^2
\]

is the literal confluent Cauchy canonical-correlation defect of the shallow
denominator and numerator inner factors.

## 3. The cofinal endpoint-height row is closed

`L-106591` uses the freedom to choose the positive companion shift separately
on each regular dyadic window.  Rouché continuity as `lambda_T->0`, Selberg's
Xi height bound, the half-strip bound for Xi derivatives, and the pinned
fifth-derivative proportion give

\[
\boxed{
\sum_{B_{-,T}(a+iy)=0}y
\le
 \left({3\over4000}+o(1)\right)N(T,2T).
}
\tag{T-106590.7}

The zero multiset, common factors, multiplicities, finite-window endpoints and
confluent events are retained in the regular-window exhaustion.  Therefore the
former statement `ENDLOC106590` is **proved**.

For every fixed `eta>0`,

\[
\boxed{
{\mathcal C_{>\eta}(U_T)\over N(T,2T)}
\le {3\over4000\eta}+o(1).
}
\tag{T-106590.8}

## 4. One fixed shallow-correlation gate for ninety percent

Take

\[
\eta={1\over100}.
\]

Then every denominator direction above height `0.01` costs at most

\[
{3\over40}N+o(N).
\]

Define

\[
\boxed{
\mathfrak C_{\rm sh}(T)
 =\left\|
 P_{K_{B_{-,T}^{\le1/100}}}T_{B_{+,T}}
 \right\|_{S_2}^2.
}
\tag{T-106590.9}

and define

```text
SHALLOWCORR106591:

limsup_(T->infinity)
  C_sh(T)/N(T,2T)
< 11/500.
```

Since

\[
{3\over40}+{11\over500}={97\over1000},
\]

one obtains

\[
\|H_{U_{5,\lambda_T}}\|_{S_2}^2
 <\left({97\over1000}-o(1)\right)N(T,2T).
\]

The fifth-endpoint winding identity and

\[
{R_5(T,2T)\over N(T,2T)}>{997\over1000}-o(1)
\]

therefore prove

\[
\boxed{
\mathrm{SHALLOWCORR}_{106591}
\Longrightarrow
\liminf_{T\to\infty}
 {N_0(T,2T)\over N(T,2T)}>0.9.
}
\tag{T-106590.10}

More generally, any fixed `eta>3/388` is admissible with threshold

\[
{97\over1000}-{3\over4000\eta}.
\tag{T-106590.11}

For a `95%` conclusion, taking `eta=1/50` leaves the exact shallow allowance

\[
{47\over1000}-{3\over80}={19\over2000}.
\]

## 5. Relation to the formerly open targets

The shallow term in (T-106590.9) is the only portion of the following targets
not paid by the new height theorem:

```text
RESGRAM106450;
HBSIG/HBRT106451;
CANONCORR106530;
ORIENTEDANGLE106540.
```

Thus those formulations have not been proved in full, but their macroscopic,
deep-pole, and endpoint-localization components are now closed.

## 6. Binding microscopic firewall

For `c>1`,

\[
F_n(z)=c+\cos(nz)
\]

has a positive even Fourier source, no real zeros, and a completely
real-rooted fifth derivative.  Its zeros are

\[
{(2k+1)\pi\over n}
 \pm i{\operatorname{arcosh}c\over n}.
\]

On every fixed real interval, zero count is `Theta(n)` while total vertical
height is `O(1)`.  Hence height mass, source positivity, a thin zero strip,
and fifth-derivative real-rootedness do not control the microscopic topological
units.

A proof of `SHALLOWCORR106591` must use genuinely Xi-specific microscopic
information: endpoint-companion canonical correlation, near-line repulsion,
the literal arithmetic source, or the equivalent oriented phase-angle mean.

```text
Selberg horizontal first moment O(T)             PROVED UNCONDITIONALLY
window-adapted endpoint height <=3/4000 N         PROVED
all deep companion charge above fixed eta        PROVED PAID
ENDLOC106590                                      PROVED
SHALLOWCORR106591 <11/500                         OPEN / RECORD-BEARING
ninety percent / density one / RH                 UNPROVED
```