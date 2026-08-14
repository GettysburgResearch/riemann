# L-93010 — Cycle Debt is exactly a positive two-channel Markov-control problem

Claim ID: `L-93010`  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: PR #272 at `fa787eed202aef67b2a4e23a64aeedfb05f93645`, especially `L-26205` and `L-27205`; PR #335 at `188bd0362c3a9f88adcbcf5298bf8eeade4016cf`, especially `L-33107` and `L-33108`  
Scope: exact finite reformulation of the full signed Cycle-Debt LP; no cofinal estimate, PIG estimate, or RH conclusion

## 1. Setup

Fix an endpoint \(X\), a balanced split family, and one action

\[
e=(n,j),\qquad n=j+k,
\]

at each allowed parent \(n\). Its size-biased selected-child kernel is

\[
P_e(a)=\frac{j}{n}\mathbf 1_{a=j}
      +\frac{k}{n}\mathbf 1_{a=k},
\tag{L-93010.1}
\]

with the two terms added when \(j=k\). Let

\[
\omega_e>0
\]

be the exact carry-capacity weight of `L-27205`, and normalize the one-unit Markov cost by

\[
 c_e=\frac{\omega_e}{n}.
\tag{L-93010.2}
\]

Let \(r=(r_n)\) be any size-conserving node divergence and put

\[
 s_n=nr_n.
\tag{L-93010.3}
\]

The Cycle-Debt primal is

\[
\mathfrak N(r)
=
\min_{d}
\sum_e\omega_e(-d_e)_+,
\qquad
\partial d=r,
\tag{L-93010.4}
\]

where \(d_e\in\mathbb R\) is a signed split coefficient.

## 2. Positive and negative action masses

For every signed flow define

\[
 x_e^+=n(d_e)_+,
 \qquad
 x_e^-=n(-d_e)_+.
\tag{L-93010.5}
\]

At one parent put

\[
 M_n^+=\sum_{e:\,p(e)=n}x_e^+,
 \qquad
 M_n^-=
 \sum_{e:\,p(e)=n}x_e^-.
\tag{L-93010.6}
\]

When \(M_n^\pm>0\), normalize

\[
 \pi_n^\pm(e)=\frac{x_e^\pm}{M_n^\pm}
\tag{L-93010.7}
\]

and let

\[
 P_n^\pm=\sum_e\pi_n^\pm(e)P_e.
\tag{L-93010.8}
\]

If \(M_n^\pm=0\), choose any allowed row; it is multiplied by zero.

Thus \(M^+\) and \(M^-\) are nonnegative occupation rows, while \(P^+\) and \(P^-\) are ordinary descending Markov kernels.

## 3. Exact two-channel occupation equation

For a child \(a\), an action mass \(x_e^\pm=n(d_e)_\pm\) contributes

\[
 x_e^\pm P_e(a)=a(d_e)_\pm
\]

whenever \(a\) is one of the two children. Multiplying the node-divergence equation by the child size therefore gives exactly

\[
\boxed{
 s=M^+(I-P^+)-M^-(I-P^-).
}
\tag{L-93010.9}
\]

This is the full signed fragmentation equation, not a bound and not a relaxation.

Conversely, suppose nonnegative rows \(M^\pm\) and descending policies \(\pi^\pm\) satisfy (L-93010.9). Put

\[
 d_e=\frac{M_{p(e)}^+\pi_{p(e)}^+(e)
            -M_{p(e)}^-\pi_{p(e)}^-(e)}{p(e)}.
\tag{L-93010.10}
\]

Reversing the preceding calculation gives \(\partial d=r\).

The two policy channels may put mass on the same action. Cancelling the common amount preserves (L-93010.9) and weakly decreases the negative cost. Hence every minimizing two-channel representation can be chosen with disjoint positive and negative action supports at each parent.

## 4. Exact cost identity

For the representation induced by a signed flow, the supports are already disjoint and

\[
\begin{aligned}
\sum_e\omega_e(-d_e)_+
&=\sum_e c_e x_e^-\\
&=\sum_n M_n^-
   \sum_{e:\,p(e)=n}\pi_n^-(e)c_e.
\end{aligned}
\tag{L-93010.11}
\]

Define the negative-policy capacity drift

\[
 d_{\mathcal G}^{\pi^-}(n)
 =\sum_e\pi_n^-(e)c_e
 =\frac1n\sum_e\pi_n^-(e)\omega_e.
\tag{L-93010.12}
\]

It is exactly the normalized policy drift of the capacity potential from `L-33108`.

For completeness, both inequalities behind the optimization identity are exact:

- every signed flow produces disjoint channels with the same source and the same cost, so the two-channel minimum is at most the original minimum;
- every feasible channel pair reconstructs a signed flow whose negative-edge cost is at most the channel cost, so the original minimum is at most the two-channel minimum.

We obtain the equality

\[
\boxed{
\mathfrak N(r)
=
\min_{
\substack{M^\pm\ge0,\;\pi^\pm\\
 s=M^+(I-P^+)-M^-(I-P^-)}
}
\sum_n M_n^-d_{\mathcal G}^{\pi^-}(n).
}
\tag{L-93010.13}
\]

Thus the **full cycle-optimized signed problem**, not merely one chosen-policy upper bound, is one positive two-colour Markov-control problem:

```text
positive occupation channel: free;
negative occupation channel: charged by exact capacity drift;
source equation: difference of the two descending Green divergences.
```

## 5. Relation to the one-policy theorem

`L-33108` fixes one policy \(P\) and uses the signed occupation

\[
M=s(I-P)^{-1}
\]

to obtain

\[
\mathfrak N(r)
\le
\sum_n(-M_n)_+d_{\mathcal G}^{P}(n).
\]

Equation (L-93010.13) is strictly more flexible. It allows the positive and negative channels to use different state-dependent policies and exactly represents arbitrary Pascal-cycle recombination. The old bound is recovered by taking

\[
M^+=M_+,
\qquad
M^-=M_-,
\qquad
P^+=P^-=P.
\]

## 6. Why this is a useful closure interface

The finite stationary no-gap theorem applies to one fixed atomic policy. It does not apply to (L-93010.13), because:

1. the two signs may use different policies;
2. each policy may depend on the parent state;
3. positive and negative destinations recombine before the objective is evaluated;
4. all variables remain nonnegative after doubling the state space.

A future proof can therefore seek a positive two-colour coupling rather than a signed edge flow. The exact remaining asymptotic theorem is:

> For the critical Möbius source \(s^{(X)}\), construct feasible channels in (L-93010.13) with charged negative occupation \(X^{o(1)}\).

By `L-27205`, that theorem implies the sharp prime ramp and RH. It is not proved here.

## 7. Proof boundary

Established exactly:

1. signed edge flow \(\leftrightarrow\) two nonnegative occupation channels;
2. exact source equation (L-93010.9);
3. exact reconstruction of a signed fragmentation;
4. cancellation of overlapping channel mass;
5. exact equality of Cycle Debt with the two-channel control cost;
6. inclusion of the one-policy Green bound as a special case.

Open:

1. subpower negative-channel cost for the critical Möbius source;
2. Cycle Debt;
3. RH.
