# L-26704 — Prime-tail queue and exact dipole transport

Claim ID: `L-26704`  
Title: Consecutive-prime incidence blocks repair every ordinary-prime constraint, and the minimal oversupport charge is the maximum upper-tail residual  
Status: **PROPOSED COMPLETE EXACT FINITE LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-08`  
Created: 2026-08-08  
Dependencies: PR #248 `L-24520`; `L-26701`; Bertrand's postulate  
Scope: explicit ordinary-prime positivity-preserving transport; no cofinal charge estimate and no RH conclusion

## 1. Ordered prime residual

Fix an integer `X>=2` and list the ordinary primes

\[
2=p_1<p_2<\cdots<p_N\le X.
\tag{L-26704.1}
\]

Let `b=(b_2,...,b_X)` be any nonnegative benchmark and put

\[
r_i
=v_{p_i}^{(X)}(b)-w_X(p_i),
\qquad
w_X(p)=p^{-1/2}\log(X/p).
\tag{L-26704.2}
\]

Define the old prime-ramp target

\[
P_X=\sum_{p\le X}(\log p)w_X(p).
\tag{L-26704.3}
\]

Choose a prime

\[
X<Y<2X
\tag{L-26704.4}
\]

and put `p_(N+1)=Y`.

For a vector `c` supported through `Y`, write

\[
J_{\mathbb P,X}^{(Y)}(c)
=\sum_{p\le X}(\log p)v_p^{(Y)}(c).
\tag{L-26704.5}
\]

This is the objective of the old prime rows evaluated on the oversupported vector. When `c` is supported through `X`, it agrees with `J_(P,X)(c)`.

The goal is to repair the old prime rows by adding only nonnegative constant blocks. Such a block preserves physical-coordinate nonnegativity and affects no prime-power row other than its prime endpoints.

## 2. Exact queue

Define recursively

\[
C_0=0,
\qquad
\boxed{
C_i=(C_{i-1}+r_i)_+
\quad(1\le i\le N).
}
\tag{L-26704.6}

Equivalently,

\[
\boxed{
C_i
=\max_{1\le k\le i}
\left(\sum_{j=k}^{i}r_j\right)_+.
}
\tag{L-26704.7}

In particular the terminal queue is

\[
\boxed{
\mathcal Q_X(b)
:=C_N
=\max_{1\le k\le N}
\left(\sum_{j=k}^{N}r_j\right)_+.
}
\tag{L-26704.8}

Thus `Q_X(b)` is the maximum positive upper-tail residual.

## 3. Explicit nonnegative interval correction

For `1<=i<=N`, define the positive constant block

\[
h^{(i)}_m
=C_i\mathbf1_{p_i<m\le p_{i+1}}.
\tag{L-26704.9}
\]

Put

\[
\boxed{
h_X=\sum_{i=1}^{N}h^{(i)},
\qquad
\widetilde b=b+h_X,
}
\tag{L-26704.10}

where `b` is extended by zero on `X<m<=Y`.

Clearly

\[
h_X(m)\ge0,
\qquad
\widetilde b_m\ge b_m\ge0
\quad(2\le m\le X),
\qquad
\widetilde b_m\ge0
\quad(X<m\le Y).
\tag{L-26704.11}

The incidence identity of `L-24520` gives, for the block `(p_i,p_(i+1)]`,

\[
\Delta v_{p_i}=-C_i,
\qquad
\Delta v_{p_{i+1}}=+C_i,
\tag{L-26704.12}

and zero change at every other prime power. At old prime `p_i`, the incoming amount is `C_(i-1)` and the outgoing amount is `C_i`. Hence the final old residual is

\[
\boxed{
\widetilde r_i
=r_i+C_{i-1}-C_i
=\min(r_i+C_{i-1},0)
\le0.
}
\tag{L-26704.13}

Therefore

\[
\boxed{
v_{p_i}^{(Y)}(\widetilde b)
\le w_X(p_i)
\qquad(1\le i\le N).
}
\tag{L-26704.14}

Every prime-power row which is not one of the endpoints is unchanged. The only new positive residual is the oversupport-prime charge

\[
\boxed{
v_Y^{(Y)}(\widetilde b)=\mathcal Q_X(b).
}
\tag{L-26704.15}

This is an explicit constraint-dipole flow. No LP solver, Green inversion, or limiting argument is used.

## 4. Minimality of the boundary queue

Consider any transport made from nonnegative constant blocks between increasing prime endpoints, allowing the final endpoint `Y`. Such a block moves one unit of residual from its lower endpoint to its upper endpoint.

For every tail beginning at `p_k`, internal transfers cancel. Therefore the amount eventually exported through `Y` is at least

\[
\left(\sum_{j=k}^Nr_j\right)_+.
\]

Taking the maximum over `k`, every such transport has boundary charge at least `Q_X(b)`. The queue construction attains that value. Hence

\[
\boxed{
\mathcal Q_X(b)
=\text{the minimal oversupport charge among all upward nonnegative prime-dipole transports.}
}
\tag{L-26704.16}

This is the finite max-flow/min-cut theorem for the ordered prime chain.

## 5. Exact objective ledger

For `i<N`, the block `(p_i,p_(i+1)]` changes the old ordinary-prime objective by

\[
C_i\log\frac{p_{i+1}}{p_i}\ge0.
\tag{L-26704.17}

The final block `(p_N,Y]` changes the old-row objective by

\[
-C_N\log p_N,
\]

because the compensating `+C_N` response lies at the new prime `Y`, outside the old objective.

Thus

\[
\boxed{
\begin{aligned}
J_{\mathbb P,X}^{(Y)}(\widetilde b)
={}&J_{\mathbb P,X}(b)
+\sum_{i=1}^{N-1}C_i\log\frac{p_{i+1}}{p_i}
-C_N\log p_N.
\end{aligned}}
\tag{L-26704.18}

Since every old prime row is feasible,

\[
P_X\ge J_{\mathbb P,X}^{(Y)}(\widetilde b).
\]

Dropping the nonnegative internal gains yields

\[
\boxed{
P_X
\ge
J_{\mathbb P,X}(b)
-\mathcal Q_X(b)\log X.
}
\tag{L-26704.19}

For the parabolic seed,

\[
J_{\mathbb P,X}(b_X^{(0)})
\ge4\sqrt X-O(\log^2X),
\]

so a subpower upper-tail queue proves the critical prime-ramp lower bound.

## 6. Scalar comparison

Let

\[
S_k=\sum_{j=k}^{N}r_j.
\]

Partial summation gives

\[
\boxed{
J_{\mathbb P,X}(b)-P_X
=\log p_1\,S_1
+\sum_{k=2}^{N}
\log\frac{p_k}{p_{k-1}}\,S_k.
}
\tag{L-26704.20}

Therefore

\[
\boxed{
\left[J_{\mathbb P,X}(b)-P_X\right]_+
\le
\mathcal Q_X(b)\log X.
}
\tag{L-26704.21}

The logarithmic/von-Mangoldt scalar is a positive weighted average of the same upper-tail queue. The queue theorem is stronger than the scalar inequality but much weaker than controlling every individual residual or a full Green norm.

## 7. Continuum bridge

For the parabolic seed, PR #265 `L-26202` proves the continuum tail inequality

\[
\int_{\theta}^{1}E(u)\,du\le0
\qquad(0<\theta\le1).
\tag{L-26704.22}

The finite queue (L-26704.8) is the exact prime-sampled analogue of the positive part of this tail integral. Thus the remaining theorem is a finite prime/floor transfer of an already nonpositive continuum tail, rather than a generic positive-cover problem.

The certified outer theorem `L-24507` already gives `r_i<=0` for every `p_i>=X/28`. Hence every positive maximizing tail begins below `X/28`.

No claim is made here that the continuum inequality automatically controls the prime-sampled queue. That transfer retains the RH-bearing logarithmic mode and is the new arithmetic target.

## 8. Proof boundary

Closed exactly:

1. the consecutive-prime queue recurrence;
2. an explicit nonnegative interval-block correction;
3. feasibility of every old ordinary-prime row;
4. isolation of one oversupport-prime charge;
5. minimality of that charge among upward prime-dipole transports;
6. the exact objective inequality (L-26704.19);
7. the tail-sum representation of the prime-ramp deficit.

Open:

1. a subpower estimate for `Q_X(b_X^(0))`;
2. a proof-grade finite transfer of continuum tail majorization;
3. the prime-ramp bound and RH.
