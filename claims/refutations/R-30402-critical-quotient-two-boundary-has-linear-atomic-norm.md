# R-30402 — The critical quotient-two boundary has linear next-half atomic norm

Claim ID: `R-30402`  
Title: The raw `x^{-1/2}` finite-cutoff boundary already forces `Omega(N)` square-root atomic norm on the next-half divisor source  
Status: **EXACT HYPOTHESIS-MATCHING REFUTATION OF THE POLYLOG TERMINAL-NORM CLAIM**  
Authoring/review agent: `gpt56-08`  
Created: 2026-08-08  
Frozen target: PR #304 at `78b75fc17e27334a9950018528c1c6e083d74820`, especially `L-30403.6`--`L-30403.9` and `T-30401.4`--`T-30401.8`  
Dependencies: PR #286 `L-28402.2`--`L-28402.8`; elementary comparison of a convergent paired series  
Scope: the critical stopped pure-power channel and any decomposition which terminates its complete cutoff boundary on the declared next-half divisor nodes

## 1. The boundary tested by the frozen proposal

Let

\[
p(x)=x^{-1/2}
\]

and, for an integer endpoint `N`, let

\[
p^{[N]}(n)=p(n)\mathbf1_{n\le N}.
\]

The finite and infinite central operators of PR #286 are

\[
(\mathscr C_Np^{[N]})(q)
=\sum_{k\ge1}
\left[p^{[N]}(2kq-1)-p^{[N]}((2k+1)q)\right]
\]

and

\[
(\mathscr Cp)(q)
=\sum_{k\ge1}
\left[p(2kq-1)-p((2k+1)q)\right].
\]

Their exact cutoff boundary is

\[
\boxed{
h_N(q):=(\mathscr Q_Np)(q)
=(\mathscr Cp)(q)-(\mathscr C_Np^{[N]})(q).
}
\tag{R-30402.1}
\]

The paired series converges, because its `k`th difference is `O_q(k^{-3/2})`.

PR #286 routes every finite cutoff boundary to the next formal endpoint

\[
M=\left\lfloor\frac{N+1}{2}\right\rfloor.
\tag{R-30402.2}
\]

PR #304 then claims that the complete boundary, including the exact Euler remainder, has a divisor-source representation on that next-half state whose square-root atomic norm is polylogarithmic.

## 2. Exact quotient-two formula

Assume

\[
\frac N3<q\le\frac N2
\]

and `N>=12`. Then

\[
\left\lfloor\frac Nq\right\rfloor=2.
\]

The included shifted-even term has `k=1`, while the first omitted shifted-even term has `k=2`. The first omitted odd term has `k=1`. Therefore

\[
\boxed{
\begin{aligned}
h_N(q)
={}&-(3q)^{-1/2}\\
&+\sum_{k=2}^{\infty}
\left[(2kq-1)^{-1/2}-((2k+1)q)^{-1/2}\right].
\end{aligned}}
\tag{R-30402.3}
\]

This is the complete boundary on the full quotient-two band; no asymptotic approximation has entered.

## 3. Uniform negative lower moat

For `q>=2`,

\[
2kq-1\ge\left(2k-\frac12\right)q.
\]

Hence

\[
\sqrt q\,h_N(q)
\le-\frac1{\sqrt3}+S,
\tag{R-30402.4}
\]

where

\[
S=\sum_{k=2}^{\infty}
\left[
\left(2k-\frac12\right)^{-1/2}
-(2k+1)^{-1/2}
\right].
\]

We record a completely elementary bound. The first term satisfies

\[
\frac1{\sqrt{7/2}}-\frac1{\sqrt5}<\frac1{10}.
\tag{R-30402.5}
\]

For `k>=3`, the mean-value theorem gives

\[
\left(2k-\frac12\right)^{-1/2}-(2k+1)^{-1/2}
\le\frac34\left(2k-\frac12\right)^{-3/2}.
\]

Using monotonicity and one integral,

\[
\begin{aligned}
\sum_{k=3}^{\infty}
\left(2k-\frac12\right)^{-3/2}
&\le
\left(\frac{11}{2}\right)^{-3/2}
+
\int_3^\infty
\left(2x-\frac12\right)^{-3/2}dx\\
&=
\left(\frac{11}{2}\right)^{-3/2}
+
\left(\frac{11}{2}\right)^{-1/2}.
\end{aligned}
\]

The rational square comparison

\[
\frac34
\left[
\left(\frac{11}{2}\right)^{-3/2}
+
\left(\frac{11}{2}\right)^{-1/2}
\right]
<\frac{19}{50}
\tag{R-30402.6}
\]

is equivalent after squaring to

\[
\frac{1521}{10648}<\frac{361}{2500}.
\]

Thus

\[
S<\frac1{10}+\frac{19}{50}=\frac{12}{25}.
\tag{R-30402.7}
\]

Also

\[
\frac1{\sqrt3}>\frac47,
\]

because `49>48`. Combining the bounds,

\[
\frac1{\sqrt3}-S
>\frac47-\frac{12}{25}
=\frac{16}{175}
>\frac1{12}.
\]

Therefore every integer in the quotient-two band satisfies

\[
\boxed{
h_N(q)<-\frac1{12\sqrt q}
\qquad\left(\frac N3<q\le\frac N2\right).
}
\tag{R-30402.8}
\]

## 4. Uniqueness on the next-half divisor state

Let a divisor-source vector `sigma=(sigma_m)_(2<=m<=M)` reproduce the complete boundary:

\[
\boxed{
h_N(q)=\sum_{\substack{m\le M\\q\mid m}}\sigma_m
\qquad(2\le q\le M).
}
\tag{R-30402.9}
\]

For every

\[
q>\frac M2,
\]

the only multiple of `q` not exceeding `M` is `m=q`. Hence

\[
\boxed{\sigma_q=h_N(q)\qquad(q>M/2).}
\tag{R-30402.10}
\]

Every integer `q` with `N/3<q<=N/2` lies in this upper half of the next-half state. Consequently

\[
\begin{aligned}
\|\sigma\|_{\rm at}
&:=\sum_{m=2}^{M}\sqrt m\,|\sigma_m|\\
&\ge
\sum_{N/3<q\le N/2}
\sqrt q\,|h_N(q)|\\
&>\frac1{12}
\#\left\{q\in\mathbb Z:\frac N3<q\le\frac N2\right\}.
\end{aligned}
\tag{R-30402.11}
\]

For `N>=42`, the count is at least `N/7`. Thus

\[
\boxed{
\|\sigma\|_{\rm at}>\frac{N}{84}.
}
\tag{R-30402.12}
\]

The lower bound is unconditional and already occurs in the first critical pure-power boundary.

## 5. Finite Euler transformation cannot remove the lower bound

PR #286 writes the same complete boundary as a finite jet list plus an exact Euler remainder. Suppose each emitted component is converted into a next-half divisor source `sigma^(r)` and all components are included exactly. Then

\[
\sum_r\sigma^{(r)}=\sigma
\]

by uniqueness of the divisor-source transform on `m<=M`. Therefore

\[
\boxed{
\sum_r\|\sigma^{(r)}\|_{\rm at}
\ge
\left\|\sum_r\sigma^{(r)}\right\|_{\rm at}
=\|\sigma\|_{\rm at}
>\frac N{84}.
}
\tag{R-30402.13}
\]

No fixed Euler order, positive Peano representation, or common-destination recombination can turn the complete next-half atomic ledger into `O(log^B N)` while retaining the exact remainder.

The obstruction is not a missing estimate. It is the unique upper-half divisor coordinate of the quotient-two boundary.

## 6. Hypothesis match with PR #304

The lower bound directly contradicts the simultaneous claims that:

1. every complete critical finite-cutoff boundary is represented as a divisor source on the strict next-half endpoint;
2. the exact Euler remainder is included;
3. the source is terminated through `Phi(sigma)` and charged by
   \[
   \sum_m\sqrt m|\sigma_m|;
   \]
4. the total boundary atomic norm is polylogarithmic.

These are precisely `L-30403.1`--`L-30403.9` and the boundary step of `T-30401`.

Allowing source nodes above the next-half endpoint, retaining a coherent boundary state instead of taking atomic variation, or recombining the boundary with the physical prime field would define a different theorem and require a new Cycle-Debt normalization.

## 7. Correct structural conclusion

The quotient-two boundary cannot be paid as a cheap terminal divisor source. It must remain coherent.

This is the same large channel independently isolated as:

```text
quotient cells 2/3/4 in the factor-five source;
the endpoint-neighbor null rows of the Selberg--Kummer reserve;
the pole-preserving prime-annulus commutator;
the full carry-position Jensen-defect frame.
```

The analytic `6/7` bulk contraction may remain useful, but the critical quotient-two boundary must be propagated in a signed or quadratic pole-preserving state rather than terminated by its square-root atomic variation.

## 8. Verdict

```text
adjacent-commutator source identity          retained exact
24 sqrt(m) single-source capacity bound      retained exact
critical shifted individual-fiber estimate  retained locally
polylog complete next-half atomic norm       FALSE
terminal boundary closure T-30401            REJECTED AS PROOF
Riemann Hypothesis                            UNPROVED
```
