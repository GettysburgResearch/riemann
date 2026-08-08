# R-24505 — The full stopped-power boundary has macroscopic atomic norm

Claim ID: `R-24505`  
Status: **REFUTED — exact boundary-source lower bound**  
Scope: PR #304 `L-30403` identification of the complete first-generation boundary with a polylogarithmic next-half-scale divisor-source atomic norm  
Issue: #245  
Date: 2026-08-08

## 1. Claim under test

PR #304 proposes to resolve the critical target into stopped powers, retain the
strictly contracting infinite analytic bank, and terminate every finite cutoff
boundary source independently by the adjacent-tree commutator map

\[
\Phi(\sigma)=\sum_m\sigma_m E_{m-1}.
\]

The source-side norm is

\[
\|\sigma\|_{\rm at}=\sum_m\sqrt m\,|\sigma_m|.
\]

The load-bearing assertion in `L-30403.6--L-30403.8` is that the **complete**
first-generation stopped-power boundary, after common-destination
recombination, has polylogarithmic atomic norm at the strict next half endpoint.

That assertion is false. The leading boundary which cancels the infinite
analytic bank already has atomic norm `Omega(X)`.

The adjacent-commutator source map of `L-30402` remains correct. What fails is
the claim that the whole stopped-power boundary is a small source to which it
may be applied independently.

## 2. Exact stopped-power boundary

Put

\[
p(q)=q^{-1/2}
\]

and, for `1<=Y<X`,

\[
p_Y(q)=p(q)\mathbf1_{q\le Y},
\qquad
\ell_Y=\log\frac{Y+1}{Y}.
\]

The exact stopped-power resolution is

\[
w_X(q)=q^{-1/2}\log(X/q)
      =\sum_{Y=1}^{X-1}\ell_Yp_Y(q).
\tag{R-24505.1}
\]

Let `mathscr C` be the infinite shifted central operator

\[
(\mathscr Cp)(q)
=\sum_{k\ge1}
\left[(2kq-1)^{-1/2}-((2k+1)q)^{-1/2}\right]
\tag{R-24505.2}
\]

and `mathscr C_Y` its exact finite restriction to the stopped source `p_Y`.
Define the complete first-generation boundary

\[
\boxed{
\mathcal B_X(q)
=\sum_{Y=1}^{X-1}\ell_Y
\left[(\mathscr Cp)(q)-(\mathscr C_Yp_Y)(q)\right].
}
\tag{R-24505.3}

Since

\[
\sum_{Y=1}^{X-1}\ell_Y=\log X
\]

and finite central propagation is linear,

\[
\boxed{
\mathcal B_X(q)
=\log X\,(\mathscr Cp)(q)
-(\mathscr C_Xw_X)(q).
}
\tag{R-24505.4}

This identity includes every stopped endpoint, every first-omitted term, and the
exact common tail. No asymptotic estimate or source choice has entered.

## 3. A positive boundary on the outer prime band

Assume `X` is even and let `p` be a prime satisfying

\[
\frac X3<p\le\frac X2.
\tag{R-24505.5}

In the finite central operator only the first shifted-even argument lies below
the endpoint:

\[
2p-1\le X,
\qquad
3p>X,
\qquad
4p-1>X.
\]

Therefore

\[
\boxed{
(\mathscr C_Xw_X)(p)=w_X(2p-1).
}
\tag{R-24505.6}

Every summand in (R-24505.2) is positive, so the first pair gives

\[
(\mathscr Cp)(p)
\ge
(2p-1)^{-1/2}-(3p)^{-1/2}
>
\frac\delta{\sqrt p},
\tag{R-24505.7}

where

\[
\delta=\frac1{\sqrt2}-\frac1{\sqrt3}>0.
\]

For all sufficiently large `X`, condition (R-24505.5) gives

\[
2p-1>\frac X2
\]

and hence

\[
0\le w_X(2p-1)
\le\frac{\log2}{\sqrt p}.
\tag{R-24505.8}

Combining (R-24505.4)--(R-24505.8),

\[
\boxed{
\mathcal B_X(p)
\ge
\frac{\delta\log X-\log2}{\sqrt p}.
}
\tag{R-24505.9}

Thus, after enlarging the endpoint threshold,

\[
\boxed{
\mathcal B_X(p)
\ge
\frac{\delta}{2}\frac{\log X}{\sqrt p}
\qquad
\left(\frac X3<p\le\frac X2,\ p\text{ prime}\right).
}
\tag{R-24505.10}

The boundary is not a small endpoint derivative on this band. It is the
macroscopic term which almost cancels the infinite analytic bank.

## 4. Atomic-norm lower bound

PR #286 routes every boundary destination to the strict next endpoint

\[
X^+=\left\lfloor\frac{X+1}{2}\right\rfloor.
\]

Suppose a divisor source `sigma` supported at that endpoint realizes the
complete boundary:

\[
\mathcal B_X(q)
=\sum_{\substack{m\le X^+\\q\mid m}}\sigma_m.
\tag{R-24505.11}

For a prime `p` in (R-24505.5), the only multiple of `p` not exceeding `X^+`
is `p` itself. Therefore

\[
\boxed{\sigma_p=\mathcal B_X(p).}
\tag{R-24505.12}

Consequently

\[
\begin{aligned}
\|\sigma\|_{\rm at}
&\ge
\sum_{X/3<p\le X/2}\sqrt p\,|\sigma_p|\\
&\ge
\frac\delta2\log X
\left[\pi(X/2)-\pi(X/3)\right].
\end{aligned}
\tag{R-24505.13}

The prime number theorem gives

\[
\pi(X/2)-\pi(X/3)
\sim\frac{X}{6\log X}.
\]

Hence

\[
\boxed{
\|\sigma\|_{\rm at}=\Omega(X).
}
\tag{R-24505.14}

This contradicts every bound of the form

\[
\|\sigma\|_{\rm at}=O((\log X)^A).
\]

The same argument survives any fixed-factor oversupport. Distinct primes in the
band cannot share one source node of size `O(X)`, and

\[
\sum_{q\mid m}|\sigma_m|
\]

still pays at least `sqrt(p)|mathcal B_X(p)|` for each band prime.

## 5. What went wrong in the proposed composition

The first-generation divisor-switch estimate in PR #286 controls the **small
finite jet remainder after the leading analytic/boundary cancellation has been
retained**. It cannot be identified with the atomic norm of the entire stopped
boundary (R-24505.3).

The leading boundary is large because

\[
\log X\,\mathscr Cp
\]

and

\[
\mathcal B_X
\]

nearly cancel to produce the finite residual `mathscr C_X w_X`. Terminating
`mathcal B_X` independently by a signed commutator discards that relative
cancellation and incurs macroscopic negative capacity.

Therefore the step

```text
contracted positive analytic bank
+ independently terminated complete boundary source
-> polylogarithmic Cycle Debt
```

is invalid.

A valid repair must do one of the following before taking negative capacity:

1. bind the leading boundary to actual descendant central capacity in the
   analytic flow;
2. recombine analytic and boundary flows on common edges;
3. subtract the leading relative source and apply the commutator only to the
   genuinely small jet/collar remainder;
4. prove a different signed shell/cycle cancellation.

This is exactly the source-flow capacity issue which PR #303 had isolated.

## 6. Exact scope

Refuted:

- PR #304 `L-30403.6--L-30403.9` when `sigma_a` is declared to be the complete
  first-generation stopped-power boundary;
- the resulting separate-boundary proof of polylogarithmic Cycle Debt;
- `T-30401` as a completed proof in its current composition.

Retained:

- the adjacent-tree commutator identity;
- the `O(sqrt m)` capacity bound for one divisor atom;
- logarithmic cost for an already isolated actual shifted pair;
- the `6/7` analytic bulk contraction;
- finite Euler/Peano jet algebra;
- the possibility of a **relative** analytic-boundary cancellation or a smaller
  terminal remainder theorem;
- the Cycle-Debt consumer;
- RH as an open problem.

## 7. Finite directed mutation

`X-24505` certifies the band lower bound using outward-rounded arithmetic. At
`X=10^6` there are `12,873` primes in `(X/3,X/2]`, and the sum of the rigorous
per-prime lower bounds in (R-24505.9), after multiplication by `sqrt(p)`, exceeds

\[
21349.32569214549.
\]

The linear asymptotic conclusion is proved by (R-24505.13)--(R-24505.14); the
finite computation is a mutation and normalization check only.
