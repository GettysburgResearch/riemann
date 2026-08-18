## Purpose

Continue PR #603 at exact head
`1dac3eeccb5a01183067c00722d92fbcf2df12c5` and attack its surviving
critical bounded-remainder correlation rather than bounding the bounded
`P_61` remainder term by absolute values.

This draft publishes the work summarized in
[review #4960295595](https://github.com/gfreund123/riemann/pull/603#pullrequestreview-4960295595).
The handoff used `T98030`--`T98032`; publication maps those identifiers
mechanically to `T98040`--`T98042` because the remote already contained a
`98030` publication branch. Two packet-serialization carriage returns were
also restored to their intended literal TeX `\\rm` sequences. No
mathematical statement was changed; Markdown hard breaks were normalized to
explicit `<br>` tags.

**RH remains unproved.** This successor proves an exact Stieltjes transfer for
the complete normalized annular base, shows that the full source is governed
by one continuous Dickman profile plus the prime-measure discrepancy, and uses
the classical Vinogradov--Korobov zero-free region to enlarge the unconditional
positive corridor by many orders of magnitude.

## Exact transfer

Put

```text
h(x)=b(x)/sqrt(x),
A_z(t)=sum_(m<=t, P^-(m)>=z) mu(m)/m.
```

The native state has the exact source-faithful representation

```text
F(Y,z)/sqrt(Y) = integral_[1,Y] A_z(Y/x) dh(x).
```

The complete `P_61` profile has finite exponentially weighted variation:

```text
integral exp(eta log x) |dh(x)| < infinity   (eta<1/2),
lim h(x)=a_*=12 product_(p<=61)(1-1/p)>0.
```

Thus the bounded nonhomogeneous base remainder is not a separate unsigned
error. It is part of one fixed finite-variation source measure.

## Continuous full-base model

For `L=log z`, `u=log Y/L`, define

```text
C_L(u)=integral rho(u-log(x)/L) dh(x),
```

with `rho(v)=0` for `v<0`. Uniform Dickman ratio bounds and the exponential
variation of `h` give

```text
C_L(u)=a_* rho(u) [1+O(log(u+2)/L)].
```

The first logarithmic moment is explicit. If `B_61(s)` is the Mellin transform
of the base and

```text
B_61(s)=a_*/(s-1/2)+J_*+O(s-1/2),
```

then

```text
J_*=2.06957018038713144617... > 0,
-integral log(x) dh(x)=J_*.
```

## Mesoscopic positive corridor

The exact PR #603 measure comparison, with the classical
Vinogradov--Korobov prime-reciprocal discrepancy, gives

```text
|F(Y,z)/sqrt(Y)-C_L(u)|
 <= C u exp[-c L^(3/5)(log L)^(-1/5)].
```

Consequently there is an absolute `c0>0` such that

```text
u <= c0 (log Y)^(3/8) (loglog Y)^(-3/4)
```

implies `F(Y,z)>0` uniformly for all sufficiently large `Y`.

This strictly contains PR #603's corridor
`u <= (1-epsilon)loglog(Y)/logloglog(Y)`.

## Exact boundary

```text
complete-base Stieltjes transfer             PROVED EXACT
exponentially weighted variation             PROVED
continuous full-base Dickman profile         PROVED POSITIVE
finite Mellin part J_*                        IDENTIFIED / POSITIVE
VK discrete-to-continuous comparison          PROVED ON CLASSICAL INPUT
mesoscopic Dickman corridor                   PROVED POSITIVE
critical bounded-remainder correlation        OPEN BEYOND CORRIDOR
GPC67 / RH                                    UNPROVED
```

## Replay

```bash
python3 experiments/X-98040-dickman-stieltjes/verify.py
sha256sum -c T98040_CONTENT_SHA256SUMS
```

Expected:

```text
PASS_T98040_DICKMAN_STIELTJES_CORRIDOR
```
