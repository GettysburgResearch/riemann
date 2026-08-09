# L-90018 — Every fixed-ratio endpoint shell is a positive-source finite-window test

Claim ID: `L-90018` (provisional branch range)  
Title: A fixed-ratio difference of the prime endpoint has an exact two-level kernel on the same positive occupancy source; for ratios with logarithmic length below two, shell negativity is a positive recent-window payment of one constant old-history charge  
Status: **PROPOSED COMPLETE EXACT SHELL/SOURCE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: `L-90016`; PR #352 `T-90006/T-90007`  
Scope: exact source form of every fixed-ratio shell; no proof of the payment inequality or RH

## 1. Fixed-ratio shell

Let

\[
 a(t)=A(e^t),
 \qquad
 \mathcal Q(t)=\mathcal Q_{\mathbb P}(t),
\]

and retain

\[
 -a(t)=\int_0^t k(t-u)\mathcal Q(u)\,du,
 \qquad
 k(s)=1-{s\over2}.
\tag{L-90018.1}
\]

Fix

\[
 0<c<1,
 \qquad
 L=-\log c>0,
\]

and put

\[
 T_L(t)=a(t)-a(t-L)
\tag{L-90018.2}
\]

for `t>=L`, with the causal convention `a(s)=0` for `s<0`.

PR #352 `T-90007` proves that eventual one-sidedness of `T_L` is equivalent to RH for every fixed `L>0`.

## 2. Exact shell kernel

Subtract the two convolutions in (L-90018.1). After extending the shorter integral by zero,

\[
\boxed{
 -T_L(t)
 =\int_0^t g_L(t-u)\mathcal Q(u)\,du,
}
\tag{L-90018.3}
\]

where

\[
\boxed{
 g_L(s)=
 \begin{cases}
  1-s/2,&0\le s<L,\\[1mm]
  -L/2,&s\ge L.
 \end{cases}}
\tag{L-90018.4}
\]

Indeed, for `s>=L`,

\[
 k(s)-k(s-L)=-L/2.
\]

Thus the complete infinite past is compressed to one constant negative charge; every nonconstant weight lies in the most recent fixed window.

## 3. Recent-window payment law

Write

\[
 C(t)=\int_0^t\mathcal Q(u)\,du.
\]

Equation (L-90018.3) becomes

\[
\boxed{
 -T_L(t)
 =\int_{t-L}^t
  \left(1-{t-u\over2}\right)\mathcal Q(u)\,du
  -{L\over2}C(t-L).
}
\tag{L-90018.5}
\]

If

\[
 0<L\le2,
\]

the complete recent-window kernel is nonnegative. Therefore

\[
\boxed{
 T_L(t)<0
 \iff
 \int_{t-L}^t
  \left(1-{t-u\over2}\right)\mathcal Q(u)\,du
 >{L\over2}C(t-L).
}
\tag{L-90018.6}
\]

For the dyadic shell,

\[
 L=\log2<2,
\]

so the exact RH criterion is:

\[
\boxed{
 \mathrm{RH}
 \iff
 \int_{t-\log2}^t
  \left(1-{t-u\over2}\right)\mathcal Q(u)\,du
 >{\log2\over2}C(t-\log2)
 \quad\text{eventually}.
}
\tag{L-90018.7}

This is the positive-source form of the eventual exact-zero-debt criterion in `T-90006`.

## 4. Critical neutrality

For a pure critical source

\[
 \mathcal Q_0(t)=Ke^{t/2},
\]

the recent-window leading term and the old-history leading term in (L-90018.5) are equal:

\[
 \int_0^L(1-s/2)Ke^{(t-s)/2}\,ds
 =KL e^{(t-L)/2},
\]

while

\[
 {L\over2}\int_{-\infty}^{t-L}Ke^{u/2}\,du
 =KL e^{(t-L)/2}.
\]

Thus the shell kernel annihilates the critical exponential mode exactly. The sign is determined entirely by deviations of the arithmetic source from this neutral growth law.

This is the source-side explanation for all of the following phenomena already isolated elsewhere in the repository:

```text
critical-line zeta modes have coefficient one;
off-line modes grow under scale translation;
the shell has a logarithmic deterministic drift rather than a power main term;
source-blind strict contraction is impossible.
```

## 5. Normalized-source form

Put

\[
 R(t)=e^{-t/2}\mathcal Q(t)>0.
\]

Then (L-90018.5) is

\[
\boxed{
\begin{aligned}
 -e^{-t/2}T_L(t)
 ={}&\int_0^L(1-s/2)e^{-s/2}R(t-s)\,ds\\
 &-{L\over2}
   \int_L^t e^{-s/2}R(t-s)\,ds.
\end{aligned}}
\tag{L-90018.8}

A constant `R` is exactly neutral in the infinite-history limit. Hence a valid proof must show that the source is, in this specific integrated sense, biased toward its recent values. Pointwise monotonicity of `R` is neither asserted nor required.

## 6. Proof-facing recurrence target

The dyadic shell is now reduced to a concrete positive transport problem:

> transport the old source mass in `[0,t-log 2]`, charged uniformly by `(log 2)/2`, into the latest `log 2` window with available capacity `(1-s/2)`.

Any explicit source-bound coupling proving this cofinally closes the dyadic shell, hence the endpoint criterion and RH through PR #352. A source-blind coupling cannot work because the critical exponential state is exactly saturated.

The exact two-exponential cell law and prime jumps of `L-90017` are the preferred finite coordinates for constructing such a coupling.

## 7. Proof boundary

Closed exactly:

1. the fixed-ratio shell kernel;
2. reduction of the entire old history to one constant charge;
3. the positive recent-window payment law for `L<=2`;
4. the dyadic payment criterion;
5. exact neutralization of the critical exponential source;
6. the normalized-source form.

Open:

1. a source-specific recent-window coupling;
2. eventual shell negativity;
3. RH.