# L-91381 — Every rough Euler factor is an exact survival–shell convexification

Claim ID: `L-91381`  
Status: **PROVED EXACT PACKET IDENTITY**  
Created: 2026-08-14  
RH status: **unproved**

## 1. Typed endpoint packets

Let `F_X` be any endpoint packet whose source, benchmark, component row,
ordinary capacity, radix-four capacity, boundary ports and literal entropy are
linear in the packet.  For a prime `p`, define the scale operator

\[
 (A_pF)_X=F_{X/p}
\]

with causal zero extension, and put

\[
 r_p=p^{-1/2}.
\]

The rough Euler factor is `I-r_p A_p`.

## 2. Exact convexification

The elementary identity

\[
\boxed{
 I-r_pA_p=(1-r_p)I+r_p(I-A_p)
}
\tag{L-91381.1}
\]

holds as an identity of typed packets.  Thus

\[
\boxed{
 (I-r_pA_p)F_X
 =(1-r_p)F_X+r_p\,[F_X-F_{X/p}].
}
\tag{L-91381.2}
\]

Both coefficients are nonnegative and sum to one.  The two output packets are:

```text
survival packet: F_X;
shell packet:    F_X-F_(X/p).
```

No physical coordinate is normalized separately, and no hidden source
coefficient is reinterpreted as an endpoint-loss coefficient.

## 3. Iterated form

Let

\[
 F_{i+1}=((1-r_i)I+r_iB_i)F_i,
 \qquad B_i=I-A_{p_i}.
\]

Expanding by the last shell time gives

\[
\boxed{
 F_{k+1}=\omega_0F_1+
 \sum_{i=1}^k\omega_i B_iF_i,
}
\tag{L-91381.3}
\]

where

\[
 \omega_0=\prod_{h=1}^k(1-r_h),
 \qquad
 \omega_i=r_i\prod_{h=i+1}^k(1-r_h).
\tag{L-91381.4}
\]

The weights telescope:

\[
\boxed{
 \omega_0+\sum_{i=1}^k\omega_i=1.
}
\tag{L-91381.5}
\]

The shell packet in the `i`-th term is the shell of the actual intermediate
packet `F_i`, not a shell of the original packet.  This distinction is needed
for correctness.

## 4. Consequence for deficits

If the packet deficit is positively homogeneous and subadditive, then

\[
\boxed{
 \Delta(F_{k+1})
 \le \omega_0\Delta(F_1)
 +\sum_{i=1}^k\omega_i\Delta(B_iF_i).
}
\tag{L-91381.6}
\]

Therefore a uniform deficit theorem for every intermediate shell does not
accumulate over the number of rough primes.  The weights form a probability
vector.

## 5. Boundary

This lemma is algebra only.  It does not prove that the shell packets possess
nonnegative physical rows or uniformly bounded deficit.

```text
survival–shell packet identity          EXACT
last-shell probability weights          EXACT
no accumulation under uniform bounds    EXACT
uniform shell producer                   OPEN
Riemann Hypothesis                       UNPROVEN
```
