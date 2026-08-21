# L-93011 — Cycle Debt has exact Bellman envelopes and a bang-bang optimality certificate

Claim ID: `L-93011`  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-14  
Depends on: `L-93010`; PR #272 `L-27205` finite LP duality  
Scope: exact finite primal-dual complementarity and a checker-ready certificate; no cofinal arithmetic estimate or RH conclusion

## 1. Normalized dual potential

Let \(F(1),\ldots,F(X)\) be a Cycle-Debt dual potential, normalized by \(F(1)=0\), and put

\[
 f(n)=\frac{F(n)}{n}.
\tag{L-93011.1}
\]

For an action \(e=(n,j)\), \(n=j+k\), define

\[
 \Delta_f(e)=f(n)-P_ef
 =f(n)-\frac jn f(j)-\frac kn f(k).
\tag{L-93011.2}
\]

Since \(F(j)=jf(j)\),

\[
 n\Delta_f(e)=F(n)-F(j)-F(k).
\tag{L-93011.3}
\]

Therefore the exact dual constraints of `L-27205` are

\[
\boxed{
0\le\Delta_f(e)\le c_e,
\qquad c_e=\frac{\omega_e}{n}.
}
\tag{L-93011.4}
\]

## 2. Statewise Bellman interval

For each parent define two envelopes

\[
 \mathcal L_f(n)=\max_{e:\,p(e)=n}P_ef,
\tag{L-93011.5}
\]

and

\[
 \mathcal U_f(n)=
 \min_{e:\,p(e)=n}(P_ef+c_e).
\tag{L-93011.6}
\]

The complete family of edge inequalities (L-93011.4) is equivalent, state by state, to

\[
\boxed{
\mathcal L_f(n)\le f(n)\le\mathcal U_f(n).
}
\tag{L-93011.7}
\]

Thus every dual potential lies inside one explicit Bellman interval. No edge can be forgotten: the lower envelope is a maximum over all allowed splits and the upper envelope is a minimum over all allowed splits.

## 3. Weak duality in two-channel coordinates

Let \((M^\pm,P^\pm)\) be any feasible two-channel representation from `L-93010`:

\[
s=M^+(I-P^+)-M^-(I-P^-).
\]

Pairing with \(f\) gives

\[
\begin{aligned}
-\langle s,f\rangle
={}&-
\sum_nM_n^+
   \sum_e\pi_n^+(e)\Delta_f(e)\\
&+
\sum_nM_n^-
   \sum_e\pi_n^-(e)\Delta_f(e).
\end{aligned}
\tag{L-93011.8}
\]

Using (L-93011.4),

\[
\boxed{
-\langle s,f\rangle
\le
\sum_nM_n^-
\sum_e\pi_n^-(e)c_e.
}
\tag{L-93011.9}
\]

The left side is the original dual objective \(-\langle r,F\rangle\), and the right side is the exact negative-channel cost.

## 4. Bang-bang complementary slackness

Equality in (L-93011.9) holds if and only if every occupied positive action has zero dual drift and every occupied negative action spends the full capacity drift:

\[
\boxed{
\pi_n^+(e)>0
\Longrightarrow
\Delta_f(e)=0,
}
\tag{L-93011.10}
\]

\[
\boxed{
\pi_n^-(e)>0
\Longrightarrow
\Delta_f(e)=c_e.
}
\tag{L-93011.11}
\]

Because all omitted terms in the weak-duality gap are nonnegative, these conditions are pointwise, not merely averaged.

Equivalently:

- positive mass uses only actions attaining the lower Bellman envelope,
  \[
  P_ef=f(n)=\mathcal L_f(n);
  \]
- negative mass uses only actions attaining the upper Bellman envelope,
  \[
  P_ef+c_e=f(n)=\mathcal U_f(n).
  \]

Consequently

\[
M_n^+>0\Longrightarrow f(n)=\mathcal L_f(n),
\tag{L-93011.12}
\]

\[
M_n^->0\Longrightarrow f(n)=\mathcal U_f(n).
\tag{L-93011.13}
\]

If both channels are occupied at one parent, then necessarily

\[
\boxed{
\mathcal L_f(n)=f(n)=\mathcal U_f(n).
}
\tag{L-93011.14}
\]

This is the local saddle condition created by Pascal-cycle recombination.

## 5. Exact finite optimality certificate

A tuple

\[
\mathcal C=
(M^+,\pi^+,M^-,\pi^-,f)
\]

is an exact global certificate for the Cycle-Debt optimum if it satisfies:

1. \(M^\pm\ge0\) and each occupied \(\pi_n^\pm\) is a probability distribution on allowed splits;
2. the source identity
   \[
   s=M^+(I-P^+)-M^-(I-P^-);
   \]
3. every edge satisfies
   \[
   0\le\Delta_f(e)\le c_e;
   \]
4. every positive support edge satisfies \(\Delta_f(e)=0\);
5. every negative support edge satisfies \(\Delta_f(e)=c_e\).

Then primal and dual values agree exactly:

\[
\boxed{
\mathfrak N(r)
=
\sum_nM_n^-d_{\mathcal G}^{\pi^-}(n)
=-\sum_ns_nf(n).
}
\tag{L-93011.15}
\]

This is a solver-independent proof object. A checker needs only finite arithmetic, complete edge coverage, and exact equality/inequality tests.

Conversely, whenever the signed source equation is feasible, finite LP strong duality and complementary slackness show that every optimum admits such a certificate after splitting each signed edge into its positive and negative channel. The Cycle-Debt target is feasible because the frozen balanced-tree construction supplies a signed solution.

## 6. Constructive interpretation

The optimal policy is not “choose one split ratio.” It is a two-player Bellman geometry controlled by one potential:

```text
positive channel:
    move on lower-envelope / zero-defect actions;

negative channel:
    move on upper-envelope / full-capacity actions;

mixed parent:
    lower and upper envelopes touch exactly.
```

This identifies a sharper source-specific closing target than generic spectral contraction:

> Construct, recursively or asymptotically, one dual potential whose Bellman intervals support a two-channel source decomposition of the critical Möbius divergence with subpower upper-envelope occupation.

The finite-stationary resonance no-go does not address this target.

## 7. Proof boundary

Established exactly:

1. normalized edge-dual constraints;
2. equivalent Bellman-envelope form;
3. weak duality in two-channel coordinates;
4. pointwise bang-bang complementarity;
5. exact finite global optimality certificate;
6. existence of such a certificate at every finite optimum.

Open:

1. an explicit cofinal critical certificate;
2. subpower Cycle Debt;
3. RH.
