# L-99812 — Every active two-prime SHARP box cube is submodular

Claim ID: `L-99812`  
Status: **PROVED EXACT GLOBAL TWO-PRIME THEOREM**  
Created: 2026-08-20  
Depends on: PR #658 `L-99703`; `L-99811`  
RH status: **not assumed**

Let `Phi(y)=phi(y)` be the normalized factor-67 box potential of `L-99703`, zero extended below one. For primes `67<=p<q`, define

\[
 \Delta_{p,q}\Phi(y)
 :=\Phi(y)-\Phi(y/p)-\Phi(y/q)+\Phi(y/(pq)).
\]

Then

\[
 \boxed{\Delta_{p,q}\Phi(y)<0\qquad(y\ge pq).}
\tag{L-99812.1}
\]

## 1. Deep region

If `y/(pq)>=67`, all four arguments lie in the flat tail

\[
 \Phi(t)=8(1-67^{-1/2})-\frac{3\log67}{\sqrt t},
\]

so

\[
 \Delta_{p,q}\Phi(y)
 =-\frac{3\log67}{\sqrt y}(\sqrt p-1)(\sqrt q-1)<0.
\]

## 2. Active collar

Suppose `pq<=y<67pq` and write `y=pqz`, `1<=z<67`. Then `pz,qz,pqz>=67` while `z<67`. Therefore

\[
 \sqrt z\,\Delta_{p,q}\Phi(pqz)
 =\frac8{\sqrt{67}}\sqrt z-3\log z-8
 +3\log67\left(p^{-1/2}+q^{-1/2}-(pq)^{-1/2}\right).
\tag{L-99812.2}
\]

The prime-dependent bracket is decreasing in each of `p,q`, so its maximum on `67<=p<q` is at `(67,71)`. Thus it suffices to consider

\[
 F(z)=\frac8{\sqrt{67}}\sqrt z-3\log z-8
 +3\log67\left(67^{-1/2}+71^{-1/2}-(67\cdot71)^{-1/2}\right).
\]

Its derivative is

\[
 F'(z)=\frac4{\sqrt{67z}}-\frac3z,
\]

which has the unique zero `z=603/16`. The derivative changes from negative to positive, so the critical point is a minimum. Hence the maximum on `[1,67]` is attained at an endpoint.

Direct elementary estimates give

\[
 F(1)< -4.16<0,
 \qquad
 F(67)<-9.75<0.
\]

(These margins may be certified by outward rational radical/log bounds in replay.) Therefore `F(z)<0` throughout `[1,67]`, proving (L-99812.1).

## 3. Scope

The activation condition `y>=pq` is essential: for `y<pq`, the `pq` source atom is not active and the four-corner cube is not the native two-prime Euler block. Finite tests can show positive formal mixed differences there, but they are irrelevant to the active source cube.

The theorem says every genuinely active two-prime block of the conclusion-complete box kernel has the favorable fixed mixed sign. The remaining question is whether the full many-prime Euler product can be grouped into such blocks without an adverse unpaired one-prime boundary term.
