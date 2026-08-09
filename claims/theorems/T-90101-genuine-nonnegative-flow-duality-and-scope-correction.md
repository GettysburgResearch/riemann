# T-90101 — Genuine nonnegative-throughput duality: superharmonic cuts, internal Green atoms, and the exact scope of the GFEP flow recast

Claim ID: `T-90101` (provisional branch range)  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Depends on: PR #292 `L-28001`; PR #328 `L-32301`; PR #351 `T-90006`  
Scope: exact finite linear algebra/Farkas duality; scope-corrects the word “flow” in `T-90006` without refuting its signed LP theorem; no source sign and no RH conclusion

## 1. Setup and the signed-throughput distinction

Fix `X>=4` and `n>=2`.  Use the notation of `T-90006`:

\[
 W=[n,\min(2n,X+1))\cap\mathbb Z,
 \qquad
 F=[2n,X]\cap\mathbb Z,
 \qquad V=W\sqcup F,
\]

with frozen descending kernel `Q`, source

\[
 S(m)=mR_X(m),
\]

and Laplacian

\[
 (Lh)(m)=h(m)-\sum_{c\ge n}Q(m,c)h(c),
 \qquad m\in F.
\tag{T-90101.1}
\]

Write `Q_FF` and `Q_FW` for the far-to-far and far-to-window blocks.

The LP `(P_n)` in `T-90006` takes

\[
 y\in\mathbb R^F
\]

with **no sign constraint**.  This is an exact signed transshipment problem.  Its dual equality `Lh=0` and harmonic-pixel collapse are correct at that scope.

A physical/combinatorial throughput must instead satisfy

\[
 y\ge0.
\]

Define the genuine nonnegative-throughput feasibility problem

\[
\boxed{
\begin{aligned}
 s_F&:=S_F+Q_{FF}^{\mathsf T}y-y\ge0,\\
 s_W&:=S_W+Q_{FW}^{\mathsf T}y\ge0,\\
 y&\ge0.
\end{aligned}}
\qquad (NF_n)
\tag{T-90101.2}
\]

The additional sign changes the exact cut cone.

## 2. Theorem A — primal characterization

Let the canonical descending Green flow `g` be the unique solution

\[
 g=S_F+Q_{FF}^{\mathsf T}g,
\tag{T-90101.3}
\]

and let

\[
 \Sigma=S_W+Q_{FW}^{\mathsf T}g.
\tag{T-90101.4}
\]

Then

\[
\boxed{
 (NF_n)\text{ is feasible}
 \iff
 g(m)\ge0\ (m\in F)
 \text{ and }
 \Sigma(p)\ge0\ (p\in W).
}
\tag{T-90101.5}
\]

### Proof

Put

\[
 A=I-Q_{FF}^{\mathsf T}.
\]

Because every transition is strictly descending, `A` is triangular with unit diagonal, and

\[
 A^{-1}=I+Q_{FF}^{\mathsf T}+(Q_{FF}^{\mathsf T})^2+\cdots
\tag{T-90101.6}
\]

is a finite entrywise-nonnegative Green matrix.

For a feasible `y`,

\[
 s_F=S_F-Ay=A(g-y),
\]

so

\[
 g-y=A^{-1}s_F\ge0.
\tag{T-90101.7}
\]

Since `y>=0`, this gives `g>=0`.  Moreover

\[
 \Sigma
 =S_W+Q_{FW}^{\mathsf T}g
 =s_W+Q_{FW}^{\mathsf T}(g-y)\ge0.
\tag{T-90101.8}
\]

Conversely, if `g>=0` and `Sigma>=0`, choose `y=g`; then `s_F=0` and `s_W=Sigma`. ∎

For the frozen producer of `L-28001`, the far occupation is

\[
 g(m)=mA_X(m),
 \qquad m\in F.
\tag{T-90101.9}
\]

Thus a true nonnegative flow at threshold `n` requires both the internal producer coefficients and all exit deliveries to be nonnegative.  The signed LP of `T-90006` suppresses the first family because signed `y` can cancel internal deficits.

## 3. Theorem B — the true cut cone is superharmonic

Farkas duality for (T-90101.2) gives the cone

\[
 \mathcal S_n
 =\{h\in\mathbb R^V:h\ge0,\ Lh\ge0\}.
\tag{T-90101.10}
\]

Let

\[
 b=h|_W,
 \qquad
 a=Lh|_F.
\tag{T-90101.11}
\]

Then the map

\[
\boxed{
 h\longmapsto (b,a)
}
\tag{T-90101.12}
\]

is a linear cone isomorphism

\[
 \mathcal S_n\cong
 \mathbb R^{W}_{\ge0}\times\mathbb R^{F}_{\ge0}.
\tag{T-90101.13}
\]

### Proof

Given `h`, (T-90101.11) is nonnegative by definition.  Conversely, given arbitrary `b>=0` and `a>=0`, set `h=b` on `W` and solve in ascending node order

\[
 h(m)=a(m)+\sum_{c\ge n}Q(m,c)h(c),
 \qquad m\in F.
\tag{T-90101.14}
\]

All children are smaller, so the solution exists uniquely and is nonnegative.  It has boundary `b` and Laplacian `a`. ∎

For `p in W`, let `H_p` be the harmonic exit pixel of `T-90006`:

\[
 H_p|_W=e_p,
 \qquad LH_p=0.
\]

For `r in F`, let `K_r` be the internal Green-charge potential:

\[
 K_r|_W=0,
 \qquad LK_r=e_r.
\tag{T-90101.15}
\]

Probabilistically, `K_r(m)` is the descending-chain Green/hitting weight from `m` to `r` before absorption in `W` or below `n`.  The cone decomposition is

\[
\boxed{
 h=\sum_{p\in W}b(p)H_p
   +\sum_{r\in F}a(r)K_r.
}
\tag{T-90101.16}
\]

Consequently the extreme rays of the true cut cone are exactly

```text
boundary exit pixels H_p
+
internal Green charges K_r.
```

The harmonic-pixel simplex of `T-90006` is the exposed face `a=0` selected by allowing signed throughput.

## 4. Theorem C — atomic Green pairing and exact Farkas alternative

For every `h in S_n`, the Green identity of `T-90006` becomes

\[
\boxed{
 \langle S,h\rangle
 =\sum_{p\in W}b(p)\Sigma(p)
  +\sum_{r\in F}a(r)g(r).
}
\tag{T-90101.17}
\]

Therefore

\[
 (NF_n)\text{ feasible}
 \iff
 \langle S,h\rangle\ge0
 \quad\text{for every }h\in\mathcal S_n,
\tag{T-90101.18}
\]

and checking all superharmonic cuts is exactly equivalent to checking the atomic coordinates in (T-90101.5).

### Proof

Substitute `b=h|_W` and `a=Lh` into `T-90006`, Lemma 2:

\[
 \langle S,h\rangle
 =\sum_p\Sigma(p)h(p)+\sum_rg(r)(Lh)(r).
\]

This is (T-90101.17).  Since `(b,a)` ranges over the full nonnegative orthant, nonnegativity for every cut is equivalent to coordinatewise nonnegativity of `(Sigma,g)`, agreeing with Theorem A. ∎

This is an exact max-flow/min-cut statement for the proportional-routing system with genuine nonnegative throughput.  It is still a frozen-ratio network: there is one scalar throughput per far node and no freedom to alter the prescribed child proportions.

## 5. Theorem D — threshold cuts return

For an integer `k>=n`, put

\[
 h_k(m)=\mathbf1_{m\ge k}.
\tag{T-90101.19}
\]

Then `h_k>=0` and

\[
 (Lh_k)(m)
 =\begin{cases}
 0,&m<k,\\[1mm]
 \mathbb P_m(Z_1<k),&m\ge k,
 \end{cases}
\tag{T-90101.20}
\]

so `h_k in S_n`.  Its atomic decomposition gives the exact threshold-cut identity

\[
\boxed{
 \sum_{m\ge k}S(m)
 =\sum_{p\in W,\,p\ge k}\Sigma(p)
  +\sum_{m\in F}g(m)\mathbb P_m(Z_1<k).
}
\tag{T-90101.21}
\]

Thus threshold indicators are valid superharmonic cuts of the nonnegative-throughput problem.  They are not harmonic and hence are excluded from the signed-throughput dual of `T-90006`.

The precise scope correction is therefore:

```text
T-90006: no threshold certificates in the signed-throughput LP      CORRECT
T-90101: threshold cuts exist in the genuine y>=0 flow problem       PROVED
```

This does not refute the pixel-minimum theorem of `T-90006`; it identifies which notion of flow that theorem solves.

## 6. The surviving induction architecture

Equation (T-90101.9) gives a clean descending induction interpretation.  When proving `A_X(n)>=0`, every internal atom `K_r` with `r>=2n` is a larger-node producer coordinate.  If those coordinates have already been established, the unresolved cuts at scale `n` lie on the boundary.

However the actual consumer is not the full boundary orthant.  By `L-32301`,

\[
 nA_X(n)=\sum_{p\in W}h_n(p)\Sigma_{X,n}(p)
\tag{T-90101.22}
\]

uses only `p=n`, one or two ternary contacts near `3n/2`, and `p=2n-1`.  Therefore:

```text
coordinatewise GFEP                         sufficient but stronger;
true nonnegative flow at threshold n        GFEP + all internal producers;
producer induction step                     one sparse boundary functional.
```

The exact flow recast should hence target the sparse functional (T-90101.22), unless a construction genuinely needs every exit coordinate.

## 7. Boundary

Proved exactly here:

1. the feasibility criterion (T-90101.5) for nonnegative throughput;
2. the superharmonic cut cone and its complete atomic decomposition;
3. the exact Green pairing/Farkas alternative;
4. restoration of threshold cuts at the physically relevant scope;
5. the distinction between full GFEP and the sparse producer consumer.

Not proved here:

1. positivity of `g`, `Sigma`, or the sparse functional for the critical Möbius source;
2. a nonnegative flow with variable routing policy or general balanced fragmentation;
3. GFEP, producer positivity, or RH.
