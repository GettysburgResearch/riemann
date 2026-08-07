# L-15160 — Higher-order Euler closure for every packet with one free lattice variable

Claim ID: `L-15160`  
Title: A smooth high-order safe window makes every packet with one unrestricted variable of positive logarithmic scale subexponential, uniformly in its arithmetic prefix  
Status: **PROPOSED EXACT ANALYTIC LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-04-f`  
Created: 2026-08-07  
Dependencies: `L-15155`; the first periodic-Bernoulli argument of PR #165 `L-15449`  
Scope: strengthens terminal Euler closure; it does not estimate packets whose entire macroscopic scale is carried by truncated Möbius variables

## 1. Smooth safe windows of arbitrary Euler order

Let `H` be the compact safe window of `L-15153`. For integers `m>=1` and
`R>=1`, let

\[
 \beta_{R+2}=\mathbf 1_{[0,1]}^{*(R+2)}
\]

and define

\[
 \boxed{
 W_{m,R}=H^{[m]}*\beta_{R+2}.}
 \tag{L-15160.1}
\]

Its bilateral Laplace transform is

\[
 \widehat W_{m,R}(z)
 =\widehat H^{[m]}(z)
  \left({1-e^{-z}\over z}\right)^{R+2}.
 \tag{L-15160.2}
\]

Consequently:

1. `W_(m,R)` is compactly supported and piecewise polynomial;
2. its derivatives through order `R` are absolutely continuous or of bounded
   variation in the form required by Euler summation;
3. its endpoint derivatives through order `R-1` vanish;
4. it retains the prescribed order-`m` zeros at `z=0,1/2`;
5. the added spline factor has zeros only on `Re z=0`, so no open-strip zero is
   introduced;
6. its vertical decay is `O((1+|t|)^(-R-4))` on every fixed strip.

Thus increasing Euler regularity does not change the rightmost-pole invariant.

## 2. One free-variable packet

Let `P` be a polynomial of degree at most `m-1`. For an arithmetic prefix
`A>=1`, put

\[
 \mathcal T_{A,P}(x)
 =\sum_{n>=1}{P(\log n)\over\sqrt{An}}
   W_{m,R}(x-\log(An)).
 \tag{L-15160.3}
\]

Assume the active lattice interval is separated from the initial endpoint; all
finitely many exceptional initial rows are retained separately.

The continuous integral vanishes exactly. Indeed, after
`u=x-log(At)`,

\[
 \int_0^\infty {P(\log t)\over\sqrt{At}}
 W_{m,R}(x-\log(At))dt
 ={e^{x/2}\over A}
 \int e^{-u/2}P(x-\log A-u)W_{m,R}(u)du=0,
 \tag{L-15160.4}
\]

because the half-pole moments through `deg P` vanish.

## 3. Order-`R` Euler remainder

For a compact function with the endpoint regularity above, the periodic
Bernoulli formula gives

\[
 \sum_{n\in\mathbf Z}F(n)-\int_\mathbf R F(t)dt
 ={(-1)^R\over R!}
 \int_\mathbf R \widetilde B_R(t)F^{(R)}(t)dt,
 \tag{L-15160.5}
\]

where `widetilde B_R` is bounded. Apply this to

\[
 F(t)=A^{-1/2}t^{-1/2}P(\log t)
 W_{m,R}(x-\log(At)).
\]

Using

\[
 {d^R\over dt^R}
 =t^{-R}\prod_{j=0}^{R-1}(t{d\over dt}-j),
\]

one obtains, for a constant depending only on `m,R,W`,

\[
 |F^{(R)}(t)|
 \le C_{m,R}A^{-1/2}t^{-R-1/2}
 \sum_{a+b\le R}
 |P^{(a)}(\log t)|
 |W_{m,R}^{(b)}(x-\log(At))|.
 \tag{L-15160.6}
\]

Substitution `u=x-log(At)` in the `L1` norm gives the exact scale factor

\[
 A^{-1/2}t^{-R-1/2}dt
 =A^{R-1}e^{-(R-1/2)x}
  e^{(R-1/2)u}du.
\]

Therefore

\[
 \boxed{
 |\mathcal T_{A,P}(x)|
 \le C_{m,R,W}\,
 A^{R-1}e^{-(R-1/2)x}
 (1+x+|\log A|)^{m+R}.}
 \tag{L-15160.7}
\]

For `R=1` this is the prefix-independent estimate of `L-15449`.

## 4. Summed packet consequence

Suppose a complete signed packet has the form

\[
 \mathcal T_J(x)=\sum_{A\in\mathcal A_J}c_A\mathcal T_{A,P_A}(x),
 \qquad J\le x\le J+1,
 \tag{L-15160.8}
\]

with

\[
 A\le e^{(1-\eta)J+O(1)},
 \qquad \eta>0,
 \tag{L-15160.9}
\]

and fixed-order coefficient/divisor mass

\[
 \sum_{A\in\mathcal A_J}|c_A|
 (1+J+|\log A|)^{m+R}
 \le e^{(1-\eta+o(1))J}.
 \tag{L-15160.10}
\]

Then (L-15160.7) gives

\[
 \boxed{
 \sup_{J\le x\le J+1}|\mathcal T_J(x)|
 \le
 \exp\{(1/2-R\eta+o(1))J\}.}
 \tag{L-15160.11}
\]

In particular, choosing

\[
 R>{1\over2\eta}
\]

makes the complete packet exponentially decaying, hence its block energy is
`exp(-cJ)`.

The conclusion remains valid after exact signed recombination. No rowwise total
variation is required before the common free variable has been summed.

## 5. Application to Heath--Brown packets

Every coefficient tuple of `L-15156` contains `j` unrestricted variables
`q,r_1,...,r_(j-1)`. If one of them carries logarithmic size at least `eta J`,
freeze all remaining variables into `A` and apply the present theorem to that
complete unrestricted-variable lattice.

For fixed identity order there are at most `K` unrestricted variables. Taking,
for example,

\[
 \eta={\delta\over2K}
\]

shows that every tuple for which the unrestricted product carries at least
`delta J/2` is Euler-closed after choosing a finite smoothing order depending
only on `K,delta`.

The only packets not covered are those in which **all** unrestricted variables
together carry less than `delta J/2`; almost the entire output scale is then
carried by the truncated Möbius variables. Those packets are isolated in
`R-15115`.

## 6. Proof boundary

Closed here:

- arbitrary-order smooth compact safe windows;
- the exact order-`R` Euler remainder;
- exponential closure of every packet with one genuinely macroscopic
  unrestricted lattice variable.

Not closed here:

- packets whose macroscopic scale is carried entirely by truncated Möbius
  variables;
- the balanced Möbius core;
- `CP(K)` or RH.
