# L-27303 — Prime-incidence blocks reduce the neutral lift to one suffix charge

Claim ID: `L-27303`  
Title: The least proper-power-neutral upward transport charge is the maximum positive suffix of the ordinary-prime residual  
Status: **PROPOSED COMPLETE EXACT FINITE ALGEBRA**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #273  
Depends on: PR #248 `L-24520`; `L-27301/L-27302`; PR #271 boundary lift  
Scope: explicit constructive reduction; no asymptotic tail bound and no RH claim

## 1. Ordered prime residual

Let

\[
p_1<p_2<\cdots<p_N\le X
\]

be the ordinary primes through \(X\), and put

\[
r_i
=
v_{p_i}(b_X^{(0)})
-
\frac1{\sqrt{p_i}}\log\frac X{p_i}.
\tag{L-27303.1}
\]

Choose one prime \(p_{N+1}=Y>X\), for example by Bertrand's postulate.

## 2. Positive prime-incidence blocks

For \(1\le i\le N\) and \(f_i\ge0\), define the positive block

\[
h^{(i)}_m
=
f_i\mathbf1_{p_i<m\le p_{i+1}}.
\tag{L-27303.2}
\]

PR #248 `L-24520` gives exactly

\[
\Delta v_{p_i}=-f_i,
\qquad
\Delta v_{p_{i+1}}=+f_i,
\tag{L-27303.3}
\]

and

\[
oxed{
\Delta v_q=0
\qquad(q=p^a,\ a\ge2).
}
\tag{L-27303.4}
\]

The last identity holds because both endpoints are ordinary primes. Thus every
nonnegative combination of these blocks is automatically neutral on all proper
prime powers.

Put \(f_0=0\).  The residual left at \(p_i\le X\) is

\[
\boxed{
s_i=r_i+f_{i-1}-f_i.
}
\tag{L-27303.5}
\]

The exterior endpoint receives the charge \(f_N\).

## 3. Greedy construction

Define recursively

\[
\boxed{
f_i=(r_i+f_{i-1})_+,
\qquad 1\le i\le N.
}
\tag{L-27303.6}
\]

Then

\[
s_i=\min(0,r_i+f_{i-1})\le0.
\tag{L-27303.7}
\]

Hence the positive correction

\[
h=\sum_{i=1}^Nh^{(i)}
\tag{L-27303.8}
\]

makes every ordinary-prime row through \(X\) feasible and changes no proper
prime-power row.

Induction in (L-27303.6) gives the closed form

\[
\boxed{
f_i
=
\max_{1\le k\le i}
\left(\sum_{j=k}^{i}r_j\right)_+.
}
\tag{L-27303.9}
\]

In particular, the exterior charge is

\[
\boxed{
C_X^{\uparrow}
:=f_N
=
\max_{1\le k\le N}
\left(\sum_{j=k}^{N}r_j\right)_+.
}
\tag{L-27303.10}
\]

## 4. Exact optimality among upward prime blocks

Let \(g_i\ge0\) be any other collection of consecutive-prime block amounts
whose terminal residuals satisfy

\[
r_i+g_{i-1}-g_i\le0.
\]

Then

\[
g_i\ge r_i+g_{i-1}
\]

and \(g_i\ge0\).  Induction gives

\[
g_i\ge f_i
\qquad(1\le i\le N).
\]

Therefore

\[
\boxed{
g_N\ge C_X^{\uparrow}.}
\tag{L-27303.11}
\]

So (L-27303.10) is not merely a greedy upper bound. It is the exact least
boundary charge among all nonnegative upward prime-incidence transports.

## 5. Objective orientation

Each internal block has positive physical objective increment

\[
J_X(h^{(i)})
=f_i\log\frac{p_{i+1}}{p_i}\ge0.
\tag{L-27303.12}
\]

Because of proper-power neutrality, the same increment is seen by the
ordinary-prime objective. The only loss is the exterior boundary charge at
\(Y\).  The affine lift of PR #271 therefore yields

\[
\boxed{
P_X
\ge
J_{\mathbb P,X}(b_X^{(0)})
-C_X^{\uparrow}\log Y.
}
\tag{L-27303.13}
\]

Consequently the finite tail theorem

\[
\boxed{
C_X^{\uparrow}=X^{o(1)}
}
\tag{PTC}
\]

implies the sharp prime ramp and RH.

## 6. Continuum model

PR #265 `L-26202` proves for the continuum parabolic defect \(E\) that

\[
\int_\theta^1E(u)\,du\le0
\qquad(0<\theta\le1).
\tag{L-27303.14}
\]

Equation (L-27303.10) is the exact ordinary-prime finite analogue of this tail
majorization. The continuum transport has zero exterior charge. The remaining
arithmetic theorem is precisely that prime sampling and finite-difference
errors enlarge the maximum suffix by only \(X^{o(1)}\).

This comparison is motivational, not a proof of (PTC): transferring the
continuum tail inequality to the prime-supported residual at subpower error is
the RH-bearing step.

## 7. Correct proof boundary

```text
positive prime-block construction        PROPOSED COMPLETE
proper-power neutrality                  PROPOSED COMPLETE EXACT
least boundary charge formula            PROPOSED COMPLETE EXACT
continuum tail majorization               INHERITED / PROPOSED COMPLETE
finite prime suffix charge X^o(1)         OPEN / RH-BEARING
RH                                       UNPROVED
```
