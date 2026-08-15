# M-93250 — Review protocol for the centered-Q4 cubic closure packet

Claim ID: `M-93250`  
Status: **METHODOLOGY / ADVERSARIAL REVIEW CHECKLIST**  
Created: 2026-08-15  
Scope: PR successor to #483; no mathematical conclusion beyond the referenced claims

## 1. Frozen graph

Review against these exact objects:

```text
PR #483
87bd7ad2127f98b6141b4c03355556f2b95f6404

PR #474
0a7e95a6d22f4bed9bbfa4e04b632b2c5827b53b

PR #392
d2387cd21eb891a8801fd122bc8d0ddd7c1c0fc4

PR #390
ea20af8867c3119c23efc27738d343aac2f79362

PR #383
d764be15bd8ea902ad260484eab44d19a9e82175
```

`R-90412` on PR #383 is normative: the macroscopic critical Selberg input formerly used by `L-90419` is not unconditional. Nothing in this packet imports that input.

The factor-67 proposal/review stack #488/#489 and descendants is not a dependency.

## 2. Review order

1. `L-93250`
2. `T-93251`
3. `L-93252`
4. `T-93253`
5. `R-93254`
6. `T-93255`
7. `X-93250`
8. report and handoff

## 3. Load-bearing reconstruction tests

### Endpoint convention

On the cell \(j/N<\theta<(j+1)/N\), independently verify

\[
\lfloor N(1-\theta)\rfloor=N-j-1.
\]

Replacing it by \(N-j\) must break the exact cubic projection.

### Weight and normalization

Verify

\[
w(x)=x(1-x)-1/6,\quad
\int_0^1w=0,\quad
\int_0^1w^2=1/180.
\]

Check that

\[
\mathscr V_\circ
={1\over N}\int|Q-M|^2
\]

rather than \(\int|Q-M|^2\). The factor \(N/180\) in
`L-93250.12` depends on this convention.

### Riesz kernel

Recompute

\[
K(x)=2\int_0^xw
={x(1-x)(2x-1)\over3}
\]

and the exact finite identity

\[
\int_0^1wQ_{\circ,N}
=\sum_mc_\circ(m)K(m/N).
\]

### Mellin multiplier

Independently multiply denominators in

\[
\int_0^1K(x)x^{s-1}dx
={s-1\over3(s+1)(s+2)(s+3)}.
\]

Check every possible cancellation at a nontrivial zero:

```text
s=1                         boundary only;
1-4^(1-s)=0                 forces Re(s)=1;
1-4^(-s)=0                  forces Re(s)=0;
s=-1,-2,-3                  outside the critical strip.
```

### Endpoint interpolation

Reconstruct the bound

\[
\sum_{m\le N}m|c_\circ(m)|\ll N^2
\]

from the ordinary Chebyshev estimate and the shifted/four-adic terms. Verify that \(\|K'\|_\infty\le1/3\).

### Prime-block diagonal

Confirm

\[
\|K\|_\infty^2=1/972
\]

and combine it with the frozen tower mass

\[
\sum_pA_{p,N}^2\le80N\log(2N)
\]

to obtain \(20N\log(2N)/243\).

### Mean-free Fourier reduction

Center each prime row before taking the Gram split. Check that centering changes only the zero Fourier coordinate and that the constants from `L-93015` sum to

\[
720+744=1464.
\]

## 4. Required hostile mutations

The checker must reject at least:

1. \(N-j\) in place of \(N-j-1\);
2. a changed cubic coefficient;
3. a non-mean-zero weight;
4. deletion of one prime-base source term;
5. the claim that block cardinality alone bounds coherence.

## 5. Computation boundary

The retained checker is `EXACT_RATIONAL`. It authenticates:

- finite endpoint/cell identities for arbitrary rational sources;
- the rational Mellin numerator identity;
- exact centering and Cauchy inequalities;
- formal prime-base source partitions;
- diagonal inequalities on exact finite fixtures;
- synthetic coherence firewalls and mutations.

It does not authenticate:

- the explicit formula for zeta;
- the von Koch implication;
- the frozen First-Hermite large-value theorem;
- the analytic tower estimates imported from `L-93015`;
- CPBD;
- RH.

## 6. Smallest invalidating statements

The packet fails if any one of the following is false:

1. `L-93250.16`;
2. `L-93250.17`;
3. the pole survives in `L-93250.19`;
4. integer endpoint control fails to extend to real \(X\);
5. centered PIG does not imply the cubic square-root bound;
6. `L-93015` does not apply after centering;
7. the same-prime cubic diagonal exceeds the stated tower bound.

A reviewer should attempt these failures before reviewing the broader route interpretation.
