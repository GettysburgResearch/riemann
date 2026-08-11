# L-90418 — The PIG mean mode is an inclusive uniform-carry transform

Claim ID: `L-90418`  
Title: The zeroth Fourier/Haar coefficient of every carry field is a positive explicit source kernel equal to the ordinary average-carry row plus one endpoint prefix correction  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Dependencies: `L-90411`, elementary divisor switching; average carry matrix notation of the Pascal/SHARP route  
Scope: exact mean coordinate only; no sign or critical-growth estimate

## 1. Source and prefix forms

Let `f` be supported on `{1,...,N}` and put

\[
 c=\mathbf1*f,
 \qquad
 C(r)=\sum_{m\le r}c(m).
\]

For the carry field `Q_(f,N)` of `L-90416`, its mean is

\[
 \overline Q_{f,N}
 =\int_0^1Q_{f,N}(\theta)d\theta
 =\sum_{m\le N}c(m)\left(\frac{2m}{N}-1\right).
\tag{L-90418.1}
\]

Switch divisors by writing `m=dr`. If

\[
 q=\left\lfloor\frac Nd\right\rfloor,
 \qquad
 r_N(d)=N-qd,
\]

then

\[
 \sum_{r=1}^{q}\left(\frac{2dr}{N}-1\right)
 =\frac{q\,[d-r_N(d)]}{N}.
\]

Therefore

\[
 \boxed{
 \overline Q_{f,N}
 =\sum_{d\le N}f(d)\,\omega_N(d),
 \qquad
 \omega_N(d)
 =\frac{\lfloor N/d\rfloor\,[d-(N\bmod d)]}{N}.
 }
\tag{L-90418.2}
\]

The kernel is nonnegative and satisfies `0<omega_N(d)<=1`. If `d|N`, then `omega_N(d)=1`.

## 2. Exact relation to the average carry matrix

The average number of base-`d` carries in row `N` is

\[
 \beta_{N,d}
 =\frac{
 \lfloor N/d\rfloor
 [d-1-(N\bmod d)]
 }{N+1}.
\tag{L-90418.3}
\]

Comparison with (L-90418.2) gives

\[
 \boxed{
 \omega_N(d)
 =\frac{N+1}{N}\beta_{N,d}
 +\frac1N\left\lfloor\frac Nd\right\rfloor.
 }
\tag{L-90418.4}
\]

Consequently

\[
 \boxed{
 \overline Q_{f,N}
 =\frac{N+1}{N}
   \sum_{d\le N}f(d)\beta_{N,d}
 +\frac1N C(N).
 }
\tag{L-90418.5}
\]

The PIG mean is therefore not an unrelated Fourier artifact. It is the inclusive uniform-Pascal carry row for the same arithmetic source, with one completely explicit endpoint-prefix correction.

## 3. Top-annulus firewall

For

\[
 N/2<d\le N,
\]

one has `floor(N/d)=1` and hence

\[
 \boxed{
 \omega_N(d)=\frac{2d-N}{N}.
 }
\tag{L-90418.6}
\]

Thus the mean retains a positive linear ramp on the complete top source annulus. In the deterministic compact-Q4 source this contains the coherent squarefree Möbius/logarithmic coordinate exposed by the random-Euler comparison. It cannot be removed by a generic endpoint or high-frequency estimate.

## 4. Compact-Q4 specialization

For `f=i_circ` and `c=c_circ=1*i_circ`, equations (L-90418.1) and (L-90418.5) give two exact descriptions of the same scalar:

```text
prefix/Chebyshev coordinate:
    sum c_circ(m)(2m/N-1);

source/Pascal coordinate:
    ((N+1)/N) sum i_circ(d) beta_(N,d)
    +C_circ(N)/N.
```

The first has the zero-safe Mellin transform of `L-90413`. The second shows that any elementary carry or SHARP-style attack must control the actual compact current source, not merely the bare carry matrix.

## 5. Proof boundary

Closed exactly here:

1. positive source-kernel formula for the mean;
2. exact inclusive-carry decomposition;
3. divisor endpoints have unit weight;
4. explicit top-half ramp;
5. exact identification of the PIG mean with one uniform-Pascal current row plus prefix correction.

Open:

1. a critical-growth estimate for this scalar;
2. deterministic PIG;
3. the repaired PIG-to-pole adapter;
4. RH.
