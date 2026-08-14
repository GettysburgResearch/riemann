# First-Hermite and Q4 revival: prime-block coherence after complete same-prime removal

Status: **PROPOSED REVIEWABLE MATHEMATICS — RH UNPROVED**  
Date: 2026-08-15  
Contribution type: two-route research packet with exact finite checker  
Base intended for publication: `main` at `9c7538559d7f56c2914b39aed5a1fb3fbf7ce131`

## 1. Live reconnaissance

At the start of this pass:

```text
main:
9c7538559d7f56c2914b39aed5a1fb3fbf7ce131

latest proposal:
PR #481, factor-67 common-parent repair

latest review:
PR #482, exact-head rejection of #481
```

PR #482 leaves the current factor closure blocked at the concrete common-parent and full correction-demand ledger. No post-#392 PR was found advancing the First-Hermite heat lane. The Q4 route had been revived in PR #474, but its surviving arithmetic burden was still described as a signed distinct-prime correlation after termwise same-prime removal.

I therefore chose:

1. the required First-Hermite heat lane;
2. the complete Q4 endpoint / weighted-Goldbach lane.

The common idea is to group **all powers and all channel appearances of one prime before estimating anything**. This produces one Hilbert vector per prime base. The complete same-prime diagonal is then paid exactly, and every remaining obstruction is a distinct-prime Gram correlation with a canonical rank-one half-space witness.

## 2. Exact frozen sources

### First-Hermite

```text
PR #390 head:
ea20af8867c3119c23efc27738d343aac2f79362

source:
research/external/anthropic-zeta23/proofs/FIRST_HERMITE_LARGE_VALUES.md

PR #392 head:
d2387cd21eb891a8801fd122bc8d0ddd7c1c0fc4

source:
research/external/anthropic-zeta23/proofs/LINEAR_RESOLUTION_FIRST_HERMITE_RIGIDITY.md
```

Imported inputs are the exact first-Hermite polynomial, the implication

\[
\mathcal M(q,t)<0\Longrightarrow |S_{q,a}(t)|\gg\log T,
\]

the coefficient energy

\[
V(q)=q+O(\sqrt q),
\]

and the linear-resolution range of PR #392.

### Q4

```text
PR #474 head:
56eeaccb2b041fdf68b6e718bad85032ecbdc66a

sources:
claims/theorems/T-93010-completed-q4-endpoint-pig-is-directly-rh-equivalent.md
claims/lemmas/L-93013-q4-same-prime-tower-correlations-are-pig-sized.md
```

For comparison with the older Fourier/Goldbach coordinates:

```text
PR #386 head:
66e60006bedbababefae22ad8f88f06753139a2b

source:
claims/lemmas/L-90703-q4-innovation-is-singular-cosine-energy-and-goldbach-correlation.md
```

`T-93010` remains proposed and unreviewed. Every RH-equivalent statement in this packet that uses it is explicitly conditional on that frozen theorem.

## 3. Common finite theorem — `L-93240`

For a finite family \((v_p)\) in a real or complex Hilbert space, put

\[
V=\sum_pv_p,
\qquad E=\|V\|^2,
\qquad D=\sum_p\|v_p\|^2.
\]

Then

\[
E=D+2\sum_{p<r}\operatorname{Re}\langle v_p,v_r\rangle.
\]

Taking the obstruction's own direction \(u=V/\|V\|\) and positive projections

\[
a_p=[\operatorname{Re}\langle v_p,u\rangle]_+
\]

gives

\[
\sum_pa_p\ge\sqrt E,
\qquad
\sum_pa_p^2\le D.
\]

Therefore:

\[
\#\{p:a_p>0\}\ge\frac ED,
\]

and any minimum set carrying half of the positive projection has cardinality at least

\[
\frac{E}{4D}.
\]

The projected blocks also furnish the nonnegative rank-one certificate

\[
2\sum_{p<r}a_pa_r\ge E-D.
\]

This is elementary, but it is the correct inverse form for both dormant routes: pay every one-prime tower in \(D\), then attack only the distinct-prime witness.

## 4. First-Hermite advance — `L-93241`

Write the truncated polynomial as

\[
S_{q,a}(t)=\sum_pY_{p,q,a}(t),
\]

where \(Y_{p,q,a}\) contains every power \(p^r\le e^{aq}\).

The new point is a uniform fixed-carrier bound for the **complete** prime-block diagonal:

\[
D_{q,a}(t):=\sum_p|Y_{p,q,a}(t)|^2
\le V(q)+C_{\rm tower}.
\]

The Hermite factor satisfies \(|h_q(u)|\le1\), and the tower cross terms sum to

\[
C_{\rm tower}
=
\sum_p
\frac{2(\log p)^2p^{-3/2}}
 {(1-p^{-1/2})^2(1+p^{-1/2})}
\le1152.
\]

Hence

\[
D_{q,a}(t)\ll q+1
\]

uniformly in the carrier and truncation parameter.

If \(H=|S_{q,a}(t)|\), the common lemma gives

\[
\#\{\text{prime blocks with positive obstruction projection}\}
\ge\frac{H^2}{V(q)+1152}.
\]

On the frozen negative-centre implication \(H\gg\log T\),

\[
\boxed{
\mathcal M(q,t)<0
\Longrightarrow
\gg\frac{(\log T)^2}{q+1}
\text{ distinct aligned prime bases}.
}
\]

This removes the factor \(O(q)\) lost in PR #392 when prime-power coordinates were selected first and only afterward collapsed by base prime. At \(q\asymp\log\log T\), the forced resonance is now

\[
\gg\frac{(\log T)^2}{\log\log T},
\]

not \(\gg(\log T)^2/(\log\log T)^2\).

Equivalently, with

\[
\mathfrak C^{\rm heat}_{\ne p}
=2\sum_{p<r}\operatorname{Re}
 \left(Y_{p,q,a}(t)\overline{Y_{r,q,a}(t)}\right),
\]

one has exactly

\[
|S_{q,a}(t)|^2=D_{q,a}(t)+\mathfrak C^{\rm heat}_{\ne p},
\]

so a negative carrier forces

\[
\mathfrak C^{\rm heat}_{\ne p}\gg(\log T)^2.
\]

All same-prime interference is now outside the final gate.

## 5. Q4 advance — `L-93242` and `T-93243`

Start from the complete actual endpoint source

\[
c_\circ(m)
=\Lambda(m)
-4\mathbf1_{4\mid m}\Lambda(m/4)
+3(\log4)\sum_{r\ge1}\mathbf1_{m=4^r}.
\]

The packet decomposes it coefficientwise as

\[
c_\circ(m)=\sum_pc_{\circ,p}(m),
\]

assigning the complete four-adic correction to the base prime \(2\). The corresponding endpoint row splits exactly:

\[
R_N=\sum_{p\le N}R_{N,p}
\quad\text{in }\mathbb R^N.
\]

For \(p\ne2\), the total absolute source mass is at most \(5\log N\); for \(p=2\), it is at most \(8\log N\). Therefore the complete same-prime row diagonal obeys

\[
\boxed{
D_N:=\sum_p\|R_{N,p}\|_2^2
\le576N^2\log^2N.
}
\]

This includes every power, every contracted appearance, every endpoint contribution, and the full four-adic gauge. The entire endpoint square now has the positive Gram form

\[
\|R_N\|_2^2
=D_N+2\sum_{p<r}\langle R_{N,p},R_{N,r}\rangle.
\]

Unlike a termwise split of the max and Goldbach kernels, this decomposition automatically preserves the large linear cancellations identified in `L-93013`.

Define the normalized pure distinct-prime functional

\[
\mathfrak C_{\ne p}(N)
=
\frac{2}{N^2}
\sum_{p<r}\langle R_{N,p},R_{N,r}\rangle.
\]

Then exactly

\[
\mathscr P_\circ(N)
=\frac{D_N}{N^2}+\mathfrak C_{\ne p}(N),
\qquad
0\le\frac{D_N}{N^2}\le576\log^2N.
\]

Thus:

\[
\boxed{
\mathscr P_\circ(N)\text{ is polylogarithmic}
\iff
|\mathfrak C_{\ne p}(N)|\text{ is polylogarithmic}.
}
\]

Conditional on the proposed criterion `T-93010`, `T-93243` therefore gives

\[
\boxed{
\mathrm{RH}
\iff
|\mathfrak C_{\ne p}(N)|\ll(\log N)^A
\text{ for some fixed }A.
}
\]

This closes the same-prime-removal problem for the frozen Q4 endpoint route. It does **not** prove the remaining cross-prime estimate.

The rank-one inverse theorem additionally gives

\[
\#\{p:\langle R_{N,p},R_N/\|R_N\|\rangle>0\}
\ge
\frac{\mathscr P_\circ(N)}{576\log^2N}.
\]

Conditional on the off-line pole-to-energy clause of `T-93010`, a zero of real part \(\beta>1/2\) therefore forces coherent participation of

\[
N^{2\beta-1-o(1)}
\]

distinct prime towers along a sequence of endpoints.

## 6. Exact replay

The retained checker is

```text
experiments/X-93240-prime-block-coherence/verify.py
```

Arithmetic class:

```text
EXACT_RATIONAL
```

Replay:

```bash
cd experiments/X-93240-prime-block-coherence
python3 verify.py --json /tmp/verification.json
cmp /tmp/verification.json results/verification.json
sha256sum -c SHA256SUMS
```

Expected verdict:

```text
PASS_X_93240_PRIME_BLOCK_COHERENCE
```

The current deterministic record contains:

```text
1,205  exact Hilbert-space fixtures
    6  rational prime-phase blocks
   95  complete Q4 endpoint fixtures
4,655  Q4 source coefficients
  144  same-tower algebra checks
    3  adversarial mutations detected
```

The checker does not authenticate the analytic inputs imported from PRs #390, #392, or #474. It checks only the native finite algebra and exact source decompositions in this packet.

## 7. Smallest remaining gates

### Heat

Prove a one-carrier deterministic theorem excluding the rank-one witness

\[
\sum_p
\left[
\operatorname{Re}
\left(e^{-i\theta}Y_{p,q,a}(t)\right)
\right]_+
\gg\log T
\]

with \(\gg(\log T)^2/(q+1)\) distinct prime bases, at a prescribed \(t\in[T,2T]\). Another average-density theorem does not cross this quantifier.

### Q4

Prove the pure distinct-prime endpoint estimate

\[
|\mathfrak C_{\ne p}(N)|
\ll(\log N)^A.
\]

The singular cosine-antiderivative and weighted-Goldbach forms are now alternate expansions of this same row-space cross functional. The complete same-prime diagonal requires no further arithmetic theorem.

## 8. Scientific verdict

The packet produces two unconditional finite reductions and one conditional Q4 criterion. It does not prove or disprove RH.

Its main contribution is a common endgame language:

```text
complete arithmetic object
    -> group every power/channel by prime base
    -> pay the full same-prime diagonal
    -> expose one pure distinct-prime Gram correlation
    -> extract a canonical rank-one half-space witness.
```

For First-Hermite this gains one full factor of \(q\) in the distinct-prime inverse theorem. For Q4 it removes the entire same-prime sector from the frozen RH-bearing endpoint criterion.
