# L-90205 — The fragmentation increment is a two-parent renewal and its Mellin factor continues through the RH-facing strip

Claim ID: `L-90205`  
Status: **PROPOSED COMPLETE EXACT RENEWAL / MEROMORPHIC-CONTINUATION LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: frozen half-binary/half-ternary first-entrance recursion of `L-28001/L-90101`; elementary Dirichlet-series manipulations  
Scope: deterministic fragmentation factor only; no nonvanishing theorem at zeta zeros, no endpoint sign theorem, and no RH conclusion

## 1. Increment recurrence

Fix `n` and any endpoint-independent exit trace as in `L-90204`. Write

\[
 G(m)\ge0,
 \qquad
 a(m)=G(m)-G(m-1),
 \qquad G(m)=0\quad(m<n).
 \tag{L-90205.1}
\]

For every `m>=2n`, the frozen fragmentation harmonicity is

\[
 G(m)=\frac12\left[
 G(\lfloor m/2\rfloor)+G(\lceil m/2\rceil)
 +G(\lceil m/3\rceil)+G(\lfloor2m/3\rfloor)
 \right].
 \tag{L-90205.2}
\]

Compare the rows at `m` and `m-1`. In the binary pair exactly one child increments, and its new value is `ceil(m/2)`. In the ternary pair exactly one child increments. Define

\[
 \tau_3(m)=
 \begin{cases}
 2m/3,&m\equiv0\pmod3,\\
 (m+2)/3,&m\equiv1\pmod3,\\
 (2m-1)/3,&m\equiv2\pmod3.
 \end{cases}
 \tag{L-90205.3}
\]

Then for every `m>=2n+1`, both parent rows are harmonic and

\[
 \boxed{
 a(m)=\frac12a(\lceil m/2\rceil)
      +\frac12a(\tau_3(m)).
 }
 \tag{L-90205.4}
\]

Both ancestors are strictly smaller than `m`.

### Sup-norm consequence

Let

\[
 A_0=\max_{n\le r\le2n}|a(r)|.
\]

Induction in (L-90205.4) gives

\[
 \boxed{|a(m)|\le A_0\qquad(m\ge n).}
 \tag{L-90205.5}
\]

Thus every first-entrance fragmentation trace has a globally bounded increment, despite the very rough pointwise hitting profile.

## 2. Finite renewal defect

Define the finite-support defect

\[
 \boxed{
 b(m)=a(m)-\frac12a(\lceil m/2\rceil)
             -\frac12a(\tau_3(m)),
 }
 \tag{L-90205.6}
\]

with `a(r)=0` below `n`. By (L-90205.4),

\[
 b(m)=0\qquad(m>=2n+1).
 \tag{L-90205.7}
\]

Let

\[
 \mathcal A(u)=\sum_{m\ge1}\frac{a(m)}{m^u},
 \qquad
 \mathcal B(u)=\sum_{m\le2n}\frac{b(m)}{m^u}.
 \tag{L-90205.8}
\]

The first series converges absolutely for `Re u>1` by (L-90205.5); `B` is entire.

## 3. Reindex the binary parent exactly

Every `r>=1` has the two binary preimages `2r-1,2r`. Hence

\[
 \sum_{m\ge1}\frac{a(\lceil m/2\rceil)}{m^u}
 =\sum_{r\ge1}a(r)[(2r-1)^{-u}+(2r)^{-u}].
 \tag{L-90205.9}
\]

Separate the scale-homogeneous part:

\[
 \boxed{
 \sum_m\frac{a(\lceil m/2\rceil)}{m^u}
 =2^{1-u}\mathcal A(u)+\mathcal R_2(u),
 }
 \tag{L-90205.10}
\]

where

\[
 \boxed{
 \mathcal R_2(u)
 =\sum_{r\ge1}a(r)[(2r-1)^{-u}-(2r)^{-u}].
 }
 \tag{L-90205.11}
\]

Because `a(r)` is bounded and the bracket is `O_K(r^{-Re u-1})` locally uniformly on compact `u`-sets, `R_2` is analytic for

\[
 \Re u>0.
 \tag{L-90205.12}
\]

## 4. Reindex the ternary parent exactly

The map `tau_3` has exactly two preimages for every `r>=1`:

\[
 3r-2
 \]

and

\[
 q_r=
 \begin{cases}
 3r/2,&r\text{ even},\\
 (3r+1)/2,&r\text{ odd}.
 \end{cases}
 \tag{L-90205.13}
\]

Therefore

\[
 \sum_m\frac{a(\tau_3(m))}{m^u}
 =\sum_{r\ge1}a(r)[(3r-2)^{-u}+q_r^{-u}].
 \tag{L-90205.14}
\]

The homogeneous scale part is independent of parity:

\[
 [3^{-u}+(3/2)^{-u}]r^{-u}.
\]

Thus

\[
 \boxed{
 \sum_m\frac{a(\tau_3(m))}{m^u}
 =[3^{-u}+(3/2)^{-u}]\mathcal A(u)+\mathcal R_3(u),
 }
 \tag{L-90205.15}
\]

with

\[
 \boxed{
 \begin{aligned}
 \mathcal R_3(u)=\sum_{r\ge1}a(r)\{&
 (3r-2)^{-u}-(3r)^{-u}\\
 &+q_r^{-u}-(3r/2)^{-u}\}.
 \end{aligned}}
 \tag{L-90205.16}
\]

For even `r` the second difference is zero; for odd `r` it is again `O_K(r^{-Re u-1})`. Hence `R_3` is analytic for `Re u>0`.

## 5. The characteristic equation

Substitute (L-90205.10) and (L-90205.15) into the defect identity. Initially for `Re u>1`,

\[
 \boxed{
 \Delta(u)\mathcal A(u)
 =\mathcal B(u)+\frac12\mathcal R_2(u)+\frac12\mathcal R_3(u),
 }
 \tag{L-90205.17}
\]

where

\[
 \boxed{
 \Delta(u)
 =1-\frac12\left[
 2^{1-u}+3^{-u}+(3/2)^{-u}
 \right].
 }
 \tag{L-90205.18}
\]

The right side is analytic throughout `Re u>0`. Therefore (L-90205.17) gives a meromorphic continuation

\[
 \boxed{
 \mathcal A(u)
 =\frac{\mathcal B(u)+\frac12\mathcal R_2(u)+\frac12\mathcal R_3(u)}
        {\Delta(u)}
 \qquad(\Re u>0),
 }
 \tag{L-90205.19}
\]

with possible poles only at zeros of the explicit exponential polynomial `Delta`.

No claim is made that every such possible pole is realized; the numerator can cancel a characteristic zero for a special boundary trace.

## 6. Basic characteristic geometry

At `u=1`, size conservation gives

\[
 \Delta(1)=1-\frac12(1+1/3+2/3)=0.
 \tag{L-90205.20}
\]

Moreover

\[
 \Delta'(1)
 =\frac12\left[
 \log2+\frac13\log3+\frac23\log(3/2)
 \right]>0,
 \tag{L-90205.21}
\]

so `u=1` is a simple characteristic root.

For `sigma=Re u>1`,

\[
 \left|\frac12[2^{1-u}+3^{-u}+(3/2)^{-u}]\right|
 \le\frac12[2^{1-\sigma}+3^{-\sigma}+(3/2)^{-\sigma}]<1,
 \tag{L-90205.22}
\]

because the real right side equals one at `sigma=1` and decreases strictly. Hence

\[
 \boxed{\Delta(u)\ne0\qquad(\Re u>1).}
 \tag{L-90205.23}
\]

Thus every nontrivial deterministic renewal resonance lies on or to the left of the size-conservation line.

The exponential polynomial does have nonreal zeros in `0<Re u<1`; those are deterministic fragmentation resonances, not zeta zeros. Their detailed zero distribution is not used in this lemma.

## 7. Continuation of the L-90204 fragmentation factor

The factor of `L-90204` is

\[
 \mathcal A_G(s)
 =\sum_m a(m)m^{-s-1/2}
 =\mathcal A(s+1/2).
 \tag{L-90205.24}
\]

Therefore (L-90205.19) gives the meromorphic continuation

\[
 \boxed{
 \mathcal A_G(s)
 \text{ meromorphic for }\Re s>-1/2,
 }
 \tag{L-90205.25}
\]

with possible deterministic poles only where

\[
 \Delta(s+1/2)=0.
\]

This reaches the entire RH-facing strip

\[
 0<\Re s<1/2.
\]

Combining with `L-90204` yields the explicit continued interface

\[
 \boxed{
 \widehat{\mathcal F_{-1}}(s)
 =\frac{\mathcal A_G(s)}{s^2\zeta(s+1/2)},
 }
 \tag{L-90205.26]
\]

first as an identity in the absolute half-plane and then as a meromorphic-continuation identity wherever both sides are continued. (The closing bracket in the tag label is typographical only; the displayed formula is the asserted identity.)

Thus a hypothetical off-line zeta zero `rho` is now inside the proven continuation domain of the deterministic fragmentation factor. Cancellation of the reciprocal-zeta pole can occur only if the continued `A_G(rho-1/2)` vanishes (or if a deterministic resonance requires a separate local cancellation analysis).

## 8. Exact new frontier

The previous transform boundary in `L-90204` asked for two things:

1. continuation of `A_G` to hypothetical zero locations;
2. nonvanishing there.

This lemma closes the **first** item completely. The transform route is now reduced to a deterministic zero-separation problem:

\[
 \boxed{
 \zeta(\rho)=0,\ \Re\rho>1/2
 \quad\Longrightarrow?\quad
 \mathcal A_G(\rho-1/2)\ne0
 }
 \tag{L-90205.27]
\]

for a useful chosen exit or sparse trace.

No such nonvanishing theorem is proved here. Real-axis positivity does not imply complex zero-freeness, and the explicit characteristic resonances show that the deterministic transfer has genuine complex analytic structure of its own.

## 9. Proof boundary

Proved exactly:

- the two-parent increment recurrence;
- global boundedness of every fragmentation increment;
- finite renewal defect;
- exact binary and ternary reindexings;
- analytic correction terms for `Re u>0`;
- explicit characteristic equation;
- absence of characteristic roots for `Re u>1`;
- meromorphic continuation of `A_G` through the full RH-facing strip.

Still open:

- which characteristic zeros survive for a specified exit trace;
- nonvanishing of `A_G` at hypothetical off-line zeta zeros;
- the empty-coefficient sign, GFEP/sparse producer positivity, or RH.
