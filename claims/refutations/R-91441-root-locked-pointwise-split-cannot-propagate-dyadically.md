# R-91441 — The root-locked pointwise two-channel split cannot propagate down a dyadic recurrence

Claim ID: `R-91441`  
Status: **EXACT COFINAL-PROPAGATION FIREWALL**  
Created: 2026-08-12  
Depends on: `L-91423`, `L-91440`, `T-91005`  
Corrects: any proposal to reuse the pointwise root-locked Jordan split unchanged at `a_*2^{-j}`  
RH status: **unproved**

## 1. Continuous channel already fails after one step

The coefficient of the completed continuous source has sign proportional to

\[
 -R(au)B(u).
\]

By `L-91440`, this has one fixed sign for every `u>0` only at `a=a_*`.
Therefore at the first dyadic child `a_*/2` there is a nonempty interval

\[
 \kappa<u<2\kappa
\]

on which

\[
 R((a_*/2)u)B(u)<0.
\]

The short/long continuous Jordan sectors reappear immediately.

## 2. Prime channel fails by the second step

The threshold for every prime-power coefficient to remain nonnegative is

\[
 a\ge a_{\rm p}=\tau_*/\log2.
\]

`L-91440.8` proves

\[
 a_*/2>a_{\rm p}>a_*/4.
\]

Consequently

\[
 c_{a_*/2}(\log n)>0
 \qquad(n=p^k\ge2),
\]

but

\[
 \boxed{
 c_{a_*/4}(\log2)<0.
 }
\tag{R-91441.1}
\]

The positive prime atomic channel itself therefore loses its sign at depth two.

## 3. What is refuted

The following continuation is impossible:

```text
prove two-channel domination at a_*
-> reuse the same positive-prime / negative-continuous split at a_*/2
-> iterate pointwise to a_*2^{-j}
-> apply T-91005.
```

Both arrows fail: the continuous source loses its single sign at the first
halving, and the atom `n=2` changes sign by the second.

## 4. What survives

The anchor theorem of `L-91423` remains exact and potentially useful. A valid
cofinal argument must instead provide one of:

1. a matrix-valued cocycle that mixes the prime and continuous channels as `a`
   changes;
2. a direct signed Hardy domination at every scale;
3. a scale-integrated Green identity whose boundary terms telescope without
   preserving each pointwise Jordan sign.

The root lock may be an anchor for such a construction, but it is not itself an
iterable positive decomposition.

```text
root-locked anchor sign geometry                    RETAINED EXACT
same split at a_*/2                                 REFUTED
positive prime channel at a_*/4                     REFUTED BY n=2
pointwise dyadic propagation                        IMPOSSIBLE
matrix/nonlocal scale cocycle                       OPEN / RH-BEARING
Riemann Hypothesis                                  UNPROVEN
```
