# PIG continuation: bridge/Haar localization, radix-four scale flow, and the inclusive mean row

Date: 2026-08-11  
Branch: `research/gpt56-pro/90410-pig-fourier-rademacher`  
Parent: PR #383  
Status: **new exact finite theorems; deterministic PIG and RH remain unproved**

## Executive result

The previous pass diagonalized the compact-Q4 PIG Gram in additive Fourier coordinates and proved that every mode outside a `sqrt(N)` major arc is already at PIG size. This continuation supplies an independent spatial diagonalization.

For every source prefix coefficient `c`, the continuous carry field is the symmetric bridge

```text
R_j=C(N)-C(j)-C(N-j-1),
R_j-R_(j-1)=c(N-j)-c(j).
```

Every standard Haar coefficient is exactly

```text
[one triangular source window
 - its reflected triangular source window] / sqrt(2 ell).
```

The entire Haar tree through half-length `sqrt(N)` is bounded generically by the coefficient `ell^2` mass. For the actual compact-Q4 coefficient this gives unconditional normalized cost `O(log N)`. Fewer than `sqrt(N)` coarse coefficients remain.

On every aligned interval the Q4 coefficient itself obeys the exact scale recurrence

```text
H_circ(N;u,ell)
 =H_Lambda(N;u,ell)
  -8 H_Lambda(N/4;u/4,ell/4)
  +H_4adic(N;u,ell).
```

The atom term has only `O(log^2 N)` total energy. The dyadic Haar tree therefore splits into two radix-four state chains without proliferating source species.

Finally, the mean coefficient has the exact source formula

```text
mean Q_(f,N)
 =sum_(d<=N) f(d)
   floor(N/d)[d-(N mod d)]/N.
```

This positive kernel equals the ordinary uniform average-carry row plus one explicit endpoint-prefix correction. Thus the zero-safe PIG mean is also one inclusive Pascal current row.

## 1. Exact bridge/Haar theorem

For `N=2^M` and `c=1*f`, define

```text
Q(theta)=C(N)-C(floor(N theta))-C(floor(N(1-theta))).
```

On cell `j`, the value is `R_j`. Haar Parseval gives

```text
integral |Q|^2
 =|mean R|^2
  +(1/N) sum_(u,ell) |H_(u,ell)|^2.
```

If

```text
w_ell(t)=min(t,2ell-t),
T_(u,ell)=sum_(1<=t<2ell) w_ell(t)c(u+t),
```

then exactly

```text
H_(u,ell)
 =[T_(u,ell)-T_(N-u-2ell,ell)]/sqrt(2ell).
```

The square mass of the triangle is `(2ell^3+ell)/3`. Summing disjoint standard intervals and dyadic scales gives

```text
sum_(ell<=L,u)|H_(u,ell)|^2
 <=4L^2 sum_(m<N)|c(m)|^2.
```

For `c=c_circ`, the right side at `L=sqrt(N)` is `O(N^2 log N)`. Haar Parseval divides by `N`, and PIG divides by the parent `N`, leaving `O(log N)`.

## 2. Coarse-Haar gate

Modulo the proved fine bound, endpoint PIG is equivalent to

```text
|mean R_N|^2
 +(1/N) sum_(ell>sqrt(N),u)|H_(u,ell)|^2
 << log^B N
```

in PIG-normalized units.

There are fewer than `sqrt(N)` coarse coefficients. In triangular form this is

```text
sum_(ell>sqrt(N),u)
 |T_(u,ell)(c_circ)-T_(N-u-2ell,ell)(c_circ)|^2
 /(2ell N).
```

This is the spatial counterpart of the Fourier major-mode gate. It replaces global additive characters by local equal-width triangular prime windows.

## 3. Q4 state compatibility

For `D4 a(m)=4 1_(4|m)a(m/4)`, aligned triangular windows satisfy

```text
T_(u,ell)(D4 a)=16 T_(u/4,ell/4)(a).
```

After Haar normalization the factor is eight. Hence

```text
c_circ=Lambda-D4 Lambda+a4
```

produces the exact two-chain scale relation above. The large factor is not called a contraction; it is the correct critical Q4 normalization.

## 4. Mean/Pascal identity

For `q=floor(N/d)` and `r=N mod d`, divisor switching yields

```text
omega_N(d)=q(d-r)/N,
mean Q_(f,N)=sum f(d)omega_N(d).
```

With

```text
beta_(N,d)=q(d-1-r)/(N+1),
```

one has

```text
omega_N(d)=((N+1)/N) beta_(N,d)+q/N.
```

Therefore

```text
mean Q_(f,N)
 =((N+1)/N) sum f(d)beta_(N,d)
  +C(N)/N.
```

For `d>N/2`, `omega_N(d)=2d/N-1`. The top source annulus survives with a positive ramp. This explains simultaneously:

- why the mean has a zero-safe Mellin transform;
- why a generic endpoint estimate cannot discard it;
- why the PIG mean, SHARP/average-carry, and top-annulus Möbius firewalls meet at the same scalar.

## 5. What this does and does not change

Closed:

```text
complete spatial PIG diagonalization;
fine Haar tree at PIG scale;
exact local triangular arithmetic coordinates;
exact Q4 radix-four Haar state relation;
harmless four-adic atom;
mean = inclusive uniform carry row + prefix correction.
```

Still open:

```text
mean critical-growth estimate;
coarse triangular-prime square function;
deterministic PIG;
PR #371's repaired global PIG-to-pole adapter;
RH.
```

The result is not an unconditional RH proof. It gives two complementary exact major-mode coordinates and identifies the mean as a direct bridge to the elementary Pascal programme.

## 6. Replay

```bash
cd experiments/X-90416-pig-haar
python3 -m py_compile verify.py
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
```

Expected verdict:

```text
PASS_X_90416_PIG_HAAR_LOCALIZATION
```
