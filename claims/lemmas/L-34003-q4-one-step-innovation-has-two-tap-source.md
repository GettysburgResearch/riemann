# L-34003 — The one-step Q=4 current innovation has a two-tap inverse source

Claim ID: `L-34003`  
Title: Removing one radix-four delayed copy from the Q=4 Euler–Blaschke current collapses the infinite source comb to a two-tap main-pole-killing source, up to one explicit delayed bare-source gauge  
Status: **PROPOSED COMPLETE EXACT DIRICHLET/PHYSICAL LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #325 Q=4 Euler–Blaschke system; `q_4=B_4'=b_4*Lambda_4`; ordinary Dirichlet differentiation  
Scope: exact source renewal and physical innovation identity; no energy estimate or RH conclusion

## 1. Compact one-step source

Retain

\[
 B_4(s)
 ={1-4^{1-s}\over(1-4^{-s})\zeta(s)}.
\]

Define

\[
\boxed{
 B_\circ(s)
 =(1-4^{-s})B_4(s)
 ={1-4^{1-s}\over\zeta(s)}.
}
\tag{L-34003.1}
\]

At coefficient level

\[
\boxed{
 b_\circ=(\varepsilon-\delta_4)*b_4.
}
\tag{L-34003.2}
\]

Since `1*b_4=e_4` and the local generating function of `e_4` is

\[
 {1-4x\over1-x},
 \qquad x=4^{-s},
\]

one gets the exact collapse

\[
\boxed{
 \mathbf1*b_\circ
 =(\varepsilon-\delta_4)*e_4
 =\varepsilon-4\delta_4.
}
\tag{L-34003.3}
\]

Thus the infinite four-adic inverse-source comb becomes one two-tap source after one radix-four difference.

## 2. Positive inverse and generalized primes

The inverse Dirichlet series is

\[
\boxed{
 A_\circ(s)
 ={\zeta(s)\over1-4^{1-s}}.
}
\tag{L-34003.4}
\]

Every Dirichlet coefficient is positive. At the prime two, with `z=2^{-s}`,

\[
 {1\over(1-z)(1-4z^2)}
 =\sum_{k\ge0}a_\circ(2^k)z^k,
\]

and explicitly

\[
\boxed{
 a_\circ(2^k)
 =\sum_{r=0}^{\lfloor k/2\rfloor}4^r
 ={4^{\lfloor k/2\rfloor+1}-1\over3}>0.
}
\tag{L-34003.5}
\]

Odd-prime local coefficients are the ordinary zeta coefficients, so multiplicativity gives `a_circ(n)>0` for all `n`.

Its generalized-prime sequence is

\[
\boxed{
 \Lambda_\circ(n)
 =\Lambda(n)
  +(\log4)\sum_{r\ge1}4^r\mathbf1_{n=4^r}
 \ge0.
}
\tag{L-34003.6}
\]

The numerator `1-4^(1-s)` has zeros only on `Re(s)=1`; hence it does not cancel a nontrivial zeta zero.

## 3. Bare carry source is favorable away from three endpoint contacts

From (L-34003.3), the divisor-prefix potential is

\[
 D_\circ(x)
 =\sum_{m\le x}(\mathbf1*b_\circ)(m)
 =\begin{cases}
 0,&0\le x<1,\\
 1,&1\le x<4,\\
 -3,&x\ge4.
 \end{cases}
\tag{L-34003.7}
\]

Therefore the bare source charge of a split `n=j+k` is

\[
 Y_\circ(n,j)
 =D_\circ(n)-D_\circ(j)-D_\circ(k).
\tag{L-34003.8}
\]

For every nontrivial split with `n>=4`:

```text
j,k >=4              -> Y_circ=+3;
exactly one child <4 -> Y_circ=-1;
both children <4     -> Y_circ=-5.
```

Consequently

\[
\boxed{
Y_\circ(n,j)<0\Longrightarrow\min(j,k)\le3.
}
\tag{L-34003.9}
\]

The adverse unweighted source is a fixed three-contact endpoint collar.

## 4. Exact current innovation identity

Let

\[
 q_4=B_4'=b_4*\Lambda_4=-b_4\log
\]

and

\[
 q_\circ=B_\circ'=-b_\circ\log.
\]

Differentiate (L-34003.1). Since

\[
 {d\over ds}(1-4^{-s})=(\log4)4^{-s},
\]

one obtains

\[
 q_\circ
 =(\log4)\,\delta_4*b_4
  +(\varepsilon-\delta_4)*q_4.
\]

Equivalently,

\[
\boxed{
 (\varepsilon-\delta_4)*q_4
 =q_\circ-(\log4)\delta_4*b_4.
}
\tag{L-34003.10}
\]

Thus the one-step current innovation is a genuine compact-source logarithmic current plus one explicit delayed bare-source gauge.

## 5. Critical physical recurrence

Let `P_f(x)` denote any fixed physical logarithmic localization of an arithmetic coefficient sequence `f` in the usual critical normalization

\[
 P_f(x)=\sum_n{f(n)\over\sqrt n}H(x-\log n),
\]

where `H` is the declared physical window. Then convolution by `delta_4` is exactly a delay by `log4` with critical amplitude `1/2`:

\[
 P_{\delta_4*f}(x)
 ={1\over2}P_f(x-\log4).
\]

Equation (L-34003.10) therefore becomes

\[
\boxed{
 P_{q_4}(x)
 -{1\over2}P_{q_4}(x-\log4)
 =P_{q_\circ}(x)
 -{\log4\over2}P_{b_4}(x-\log4).
}
\tag{L-34003.11}
\]

PR #337 already places the bare `b_4` physical field in a deterministic/polylogarithmic channel. Hence the only RH-sensitive innovation in (L-34003.11) is the compact-source current `q_circ`.

## 6. Relation to the reserve-increment programme

At aligned integer rows, the physical innovation

\[
 Q_4^{\rm phys}(4n,4j)-Q_4^{\rm phys}(n,j)
\]

is the additive-prefix/carry realization of the left side of (L-34003.10). Therefore the radix-four reserve increment of `L-34002` and the compact-source current `q_circ` live on the identical scale step.

A proof that the compact-source current is absorbed by the new reserve created at that step would give the desired coefficient-one recurrence. This absorption is not asserted here.

## 7. Proof boundary

Closed exactly:

1. compact source `B_circ=(1-4^(1-s))/zeta`;
2. two-tap divisor source `1*b_circ=epsilon-4delta_4`;
3. positive inverse and generalized-prime coefficients;
4. three-contact adverse bare collar;
5. exact current innovation identity (L-34003.10);
6. critical physical delay recurrence (L-34003.11).

Open:

1. a source-complete Selberg/Hermitian estimate for `q_circ`;
2. domination by the radix-four reserve increment;
3. RH.
