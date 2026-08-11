# L-91109 — The factor-\(54\) window has a positive parity-shadow automaton

Claim ID: `L-91109` (provisional research range)  
Title: Möbius signs on the certified reset window split into two positive squarefree-parity measures; the reserve admits a monotone odd-to-even transport, the equality state admits a transport with at most one integer of upward displacement, and every prime above \(53\) enters the next contracted generation  
Status: **PROPOSED COMPLETE EXACT FINITE TRANSPORT / AUTOMATON THEOREM — DIRECTED CERTIFICATE PROVIDED, INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-11  
Depends on: `L-91106`–`L-91108`; elementary Hall transport on a Ferrers graph  
Scope: exact finite-window parity transport and all-scale automaton decomposition; no finite carry lift and no RH conclusion

## 1. Positive squarefree parity measures

For \(a\in\{1,2\}\), \(x\ge1\), and a squarefree integer \(n\le x\), put
\[
\boxed{
 w_a(x,n)
 =\frac1{\sqrt n}
 \left(a\sqrt{\frac xn}-1\right)
 =\frac{a\sqrt x}{n}-\frac1{\sqrt n}.
}
\tag{L-91109.1}

These weights are nonnegative. For \(a=1\), equality occurs only at \(n=x\in\mathbb N\); for \(a=2\) they are strictly positive.

Define the positive even- and odd-parity measures
\[
\boxed{
 \mathsf E_a^x
 =\sum_{\substack{n\le x\; n\ {m squarefree}\\\omega(n)\ {m even}}}
 w_a(x,n)\delta_n,
}
\tag{L-91109.2}
\]
\[
\boxed{
 \mathsf O_a^x
 =\sum_{\substack{n\le x\; n\ {m squarefree}\\\omega(n)\ {m odd}}}
 w_a(x,n)\delta_n.
}
\tag{L-91109.3}

Since \(\mu(n)=(-1)^{\omega(n)}\) on squarefree integers,
\[
 \|\mathsf E_a^x\|-\|\mathsf O_a^x\|
 =a\sqrt x\,B(x)-A(x).
\tag{L-91109.4}

Thus
\[
\boxed{
 \|\mathsf E_1^x\|-\|\mathsf O_1^x\|=R(x),
 \qquad
 \|\mathsf E_2^x\|-\|\mathsf O_2^x\|=L(x).
}
\tag{L-91109.5}

The signed critical states have become differences of explicit positive finite measures.

## 2. A nested-neighborhood transport lemma

Let positive demands \(d(o)\) be placed at ordered odd nodes \(o\), and positive capacities \(c(e)\) at ordered even nodes \(e\). Fix an integer displacement \(\delta\ge0\), and allow an edge
\[
 o\longrightarrow e
 \quad\Longleftrightarrow\quad
 e\le o+\delta.
\tag{L-91109.6}

The neighborhoods are nested. Therefore a nonnegative transport of every demand into the capacities exists if and only if
\[
\boxed{
 \sum_{o\le t}d(o)
 \le
 \sum_{e\le t+\delta}c(e)
 \qquad\text{for every demand threshold }t.
}
\tag{L-91109.7}

### Proof

Necessity is immediate. For sufficiency, process demands in increasing order and fill the available capacities in increasing order. At threshold \(t\), every processed demand can use exactly the capacity prefix \(e\le t+\delta\); (L-91109.7) says that prefix never runs out. This is the continuous-mass version of Hall's theorem for a Ferrers bipartite graph. ∎

The resulting left-greedy transport is canonical and monotone.

## 3. Exact reserve shadow on the reset window

Let \(c_0\) be the crossing in `L-91106`, and put
\[
 X_0=c_0^{-1}=54.2191279\ldots .
\]

For the reserve channel \(a=1\), define the Hall margins
\[
\boxed{
 \mathcal H_{1,t}(x)
 =
 \sum_{\substack{e\le t\\\mu(e)=1}}w_1(x,e)
 -
 \sum_{\substack{o\le t\\\mu(o)=-1}}w_1(x,o).
}
\tag{L-91109.8}

The exact checker `X-91102` proves
\[
\boxed{
 \mathcal H_{1,t}(x)>\frac{39}{100}
}
\tag{L-91109.9}
for every \(1\le x\le X_0\) and every active odd squarefree threshold \(t\le x\).

By Section 2 with \(\delta=0\), there exists a positive transport
\[
\boxed{
 \pi_R^x:\mathsf O_1^x\longrightarrow\mathsf E_1^x
}
\tag{L-91109.10}
whose support satisfies
\[
\boxed{
 e\le o.
}
\tag{L-91109.11}

Every odd squarefree atom is therefore paid by even squarefree mass at a no-larger integer. The unspent even capacity has total mass exactly \(R(x)\).

## 4. One-step equality shadow

For the equality channel \(a=2\), define
\[
\boxed{
 \mathcal H_{2,t}^{+}(x)
 =
 \sum_{\substack{e\le\min(t+1,\lfloor x\rfloor)\\\mu(e)=1}}w_2(x,e)
 -
 \sum_{\substack{o\le t\\\mu(o)=-1}}w_2(x,o).
}
\tag{L-91109.12}

The directed checker proves
\[
\boxed{
 \mathcal H_{2,t}^{+}(x)>\frac{11}{100}
}
\tag{L-91109.13}
throughout the same window and for every active odd threshold.

Consequently there is a positive transport
\[
\boxed{
 \pi_L^x:\mathsf O_2^x\longrightarrow\mathsf E_2^x
}
\tag{L-91109.14}
with support
\[
\boxed{
 e\le o+1.
}
\tag{L-91109.15}

The total unspent capacity is exactly \(L(x)\).

The displacement \(+1\) is sharp for this monotone-prefix architecture: the stricter graph \(e\le o\) first loses feasibility near \(x=38.8\). This sharpness statement is finite reconnaissance and is not needed for the theorem.

Thus the equality state requires only one adjacent-integer correction beyond a monotone parity coupling.

## 5. Why the certificate is finite and exact

On one arithmetic cell \(N\le x<N+1\), the active squarefree set is fixed and every Hall margin has the form
\[
\boxed{
 \mathcal H(x)=C\sqrt x-D,
}
\tag{L-91109.16}
where \(C\in\mathbb Q\) and \(D\) is a finite rational linear combination of square roots of integers.

Therefore its minimum on the cell occurs at one endpoint. The checker uses directed rational square-root enclosures and verifies both one-sided cell endpoints for all
\[
 N\le54
\]
and all active thresholds. No floating LP or approximate max-flow calculation is used in the proof object.

Only the squarefree integers at most \(54\) occur:
\[
\begin{aligned}
\mu=+1:&\quad
1,6,10,14,15,21,22,26,33,34,35,38,39,46,51,\\
\mu=-1:&\quad
2,3,5,7,11,13,17,19,23,29,30,31,37,41,42,43,47,53.
\end{aligned}
\tag{L-91109.17}

The reset parity problem is therefore a 33-atom positive transport, not an unbounded Möbius sum.

## 6. Least-prime positive automaton

Let \(p_j\) be the \(j\)-th prime and set \(P^-(1)=\infty\). For \(a\in\{1,2\}\), define
\[
 E_j^{(a)}(x)
 =\sum_{\substack{n\le x\;n\ {m squarefree}\\P^-(n)\ge p_j,\;\omega(n)\ {m even}}}
 w_a(x,n),
\tag{L-91109.18}
\]
\[
 O_j^{(a)}(x)
 =\sum_{\substack{n\le x\;n\ {m squarefree}\\P^-(n)\ge p_j,\;\omega(n)\ {m odd}}}
 w_a(x,n).
\tag{L-91109.19}

Every nontrivial squarefree integer has a unique least prime. Therefore
\[
\boxed{
 E_j^{(a)}(x)
 =\phi_a(x)
 +\sum_{\substack{k\ge j\\p_k\le x}}
 p_k^{-1/2}O_{k+1}^{(a)}(x/p_k),
}
\tag{L-91109.20}
\]
\[
\boxed{
 O_j^{(a)}(x)
 =\sum_{\substack{k\ge j\\p_k\le x}}
 p_k^{-1/2}E_{k+1}^{(a)}(x/p_k),
}
\tag{L-91109.21}
where
\[
 \phi_a(x)=a\sqrt x-1.
\]

In vector form, with
\[
 \mathbf P_j^{(a)}=\binom{E_j^{(a)}}{O_j^{(a)}},
 \qquad
 S=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
\[
\boxed{
 \mathbf P_j^{(a)}(x)
 =\binom{\phi_a(x)}0
 +\sum_{\substack{k\ge j\\p_k\le x}}
 p_k^{-1/2}S\mathbf P_{k+1}^{(a)}(x/p_k).
}
\tag{L-91109.22}

Every matrix and every state on the right is nonnegative. Möbius sign is only the final parity functional
\[
 (1,-1)\mathbf P_1^{(a)}.
\]

## 7. Only sixteen primes remain inside one generation

The primes at most \(53\) are
\[
 2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53.
\]
The next prime is \(59\), and
\[
\boxed{
 \frac1{59}<c_0.
}
\tag{L-91109.23}

Hence every transition in (L-91109.22) with \(p_k\ge59\) satisfies
\[
\boxed{
 \frac{x}{p_k}<c_0x.
}
\tag{L-91109.24}

It enters the next contracted reset generation immediately.

All noncontracted transitions are carried by the finite acyclic 16-prime parity automaton. Equivalently, if
\[
 P_{53}=\prod_{p\le53}p,
\]
then
\[
\boxed{
 \mathbf P_1^{(a)}(x)
 =\sum_{d\mid P_{53}}
 d^{-1/2}S^{\omega(d)}
 \mathbf P_{17}^{(a)}(x/d),
}
\tag{L-91109.25}
where terms with \(d>x\) vanish and \(p_{17}=59\).

This formula is a finite positive transfer matrix followed by a tail whose first nontrivial transition contracts scale by more than \(54\).

## 8. Connection to endpoint butterflies

The reserve shadow uses no upward movement. The equality shadow uses only
\[
 o\mapsto e\le o+1.
\]

`L-91105` proves that every endpoint martingale butterfly has a positive seed on exactly two adjacent integers. Thus the only displacement required by the finite parity transport is exactly the displacement generated by the compact endpoint packet.

This is the first exact source-level match between:

```text
squarefree parity cancellation in the equality state
and
adjacent endpoint shadow packets in the carry cone.
```

The remaining lift must preserve divisor destinations and endpoint weights, but it no longer needs an unbounded transport graph.

## 9. New finite reset target

The cone-preserving reset in `T-91101` can now be attacked as a finite state problem:

1. use the 33-atom parity shadows (L-91109.10) and (L-91109.14);
2. realize every zero- or one-step displacement by adjacent positive seed packets;
3. propagate the 16-prime positive automaton within the generation;
4. send every \(p\ge59\) branch to the contracted residual state;
5. prove one coefficient-one capacity and score ledger.

No prime-density, Mertens, zero-free-region, or global equality-weight estimate remains in this finite interface.

## 10. Proof boundary

Closed exactly, subject to review:

1. positive squarefree-parity state decomposition;
2. the nested-neighborhood Hall criterion;
3. monotone reserve transport with certified margin;
4. one-step equality transport with certified margin;
5. the finite 33-atom support list;
6. the positive least-prime parity automaton;
7. the 16-prime/contracted-tail split;
8. exact support alignment with adjacent butterfly seeds.

Still open:

1. a divisor-capacity-faithful lift of the parity shadow;
2. nonnegative endpoint weights after the lift;
3. coefficient-one transfer to the next generation;
4. bounded score debt;
5. RH.
