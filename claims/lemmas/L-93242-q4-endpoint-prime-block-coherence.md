# L-93242 — Complete Q4 endpoint energy has a positive prime-block Gram normal form

Claim ID: `L-93242`  
Status: **PROPOSED COMPLETE EXACT FINITE NORMAL FORM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-93240`; PR #474 at `56eeaccb2b041fdf68b6e718bad85032ecbdc66a`, especially `T-93010` and its complete endpoint source  
Scope: the complete actual Q4 endpoint row and its partition by underlying prime base; no unconditional PIG bound and no RH conclusion

## 1. Complete actual source

Use the complete compact-Q4 source of `T-93010`:

\[
c_\circ(m)
=\Lambda(m)
-4\mathbf1_{4\mid m}\Lambda(m/4)
+3(\log4)\sum_{r\ge1}\mathbf1_{m=4^r}.
\tag{L-93242.1}
\]

For every prime \(p\), define its complete prime-base component

\[
\begin{aligned}
c_{\circ,p}(m)
={}&(\log p)\sum_{k\ge1}\mathbf1_{m=p^k}\\
&-4(\log p)\sum_{k\ge1}\mathbf1_{m=4p^k}\\
&+3(\log4)\mathbf1_{p=2}
  \sum_{r\ge1}\mathbf1_{m=4^r}.
\end{aligned}
\tag{L-93242.2}
\]

The four-adic correction is assigned to the base prime \(2\). Then, exactly and coefficient by coefficient,

\[
\boxed{
c_\circ(m)=\sum_pc_{\circ,p}(m).
}
\tag{L-93242.3}
\]

Let

\[
C_{\circ,p}(x)=\sum_{m\le x}c_{\circ,p}(m).
\tag{L-93242.4}
\]

For an endpoint \(N\ge2\) and \(0\le j<N\), define the prime-base row vector by

\[
R_{N,p}(j)
=C_{\circ,p}(N)
-C_{\circ,p}(j)
-C_{\circ,p}(N-j-1).
\tag{L-93242.5}
\]

The complete endpoint row of `T-93010` is therefore

\[
\boxed{
R_N=\sum_{p\le N}R_{N,p}
\quad\text{in }\mathbb R^N.
}
\tag{L-93242.6}
\]

No constant, endpoint, or delayed four-adic term is left outside the prime-base decomposition.

## 2. The entire same-prime diagonal is PIG-sized

For a fixed prime \(p\), let

\[
A_{p,N}=\sum_{m\le N}|c_{\circ,p}(m)|.
\tag{L-93242.7}
\]

The complete tower of powers \(p^k\le N\) has total von-Mangoldt weight at most \(\log N\). The shifted tower \(4p^k\le N\) contributes at most \(4\log N\). For \(p=2\),

\[
3(\log4)\#\{r:4^r\le N\}
\le3\log N.
\]

Consequently

\[
\boxed{
A_{p,N}
\le
\begin{cases}
5\log N,&p\ne2,\\
8\log N,&p=2.
\end{cases}}
\tag{L-93242.8}
\]

Every prefix in (L-93242.5) has magnitude at most \(A_{p,N}\), hence

\[
|R_{N,p}(j)|
\le
\begin{cases}
15\log N,&p\ne2,\\
24\log N,&p=2.
\end{cases}
\tag{L-93242.9}
\]

Define the complete same-prime row diagonal

\[
D_N=\sum_{p\le N}\|R_{N,p}\|_2^2.
\tag{L-93242.10}
\]

There are at most \(N-1\) odd prime labels and one label \(p=2\). Therefore

\[
\begin{aligned}
D_N
&\le
N\left[225(N-1)+576\right]\log^2N\\
&\le\boxed{576N^2\log^2N}.
\end{aligned}
\tag{L-93242.11}
\]

This pays the complete self-correlation of every Euler factor, including all powers, all appearances in the contracted tower, and the entire four-adic correction.

## 3. Positive Gram normal form for the full endpoint square

The endpoint energy has the exact decomposition

\[
\boxed{
\|R_N\|_2^2
=D_N
+2\sum_{p<r}\langle R_{N,p},R_{N,r}\rangle.
}
\tag{L-93242.12}
\]

This partitions the **entire row square** before expanding into zero mode, max kernel, or weighted Goldbach terms. In particular, the large linear pieces retained in `L-93013` are already recombined inside one positive row Gram object; no indefinite termwise partition is needed.

Let

\[
E_N=\|R_N\|_2^2,
\qquad
u_N=\frac{R_N}{\|R_N\|_2}
\]

when \(E_N>0\), and define

\[
a_{p,N}=
\left[\langle R_{N,p},u_N\rangle\right]_+.
\tag{L-93242.13}
\]

Then `L-93240` gives

\[
\sum_pa_{p,N}\ge\sqrt{E_N},
\qquad
\sum_pa_{p,N}^2\le D_N.
\tag{L-93242.14}
\]

Hence

\[
\boxed{
\#\{p:a_{p,N}>0\}
\ge\frac{E_N}{D_N}.
}
\tag{L-93242.15}
\]

If \(J_N\) is a smallest set carrying half of the positive projection, then

\[
\boxed{
|J_N|
\ge\frac{E_N}{4D_N}.
}
\tag{L-93242.16}
\]

The rank-one nonnegative distinct-prime certificate is

\[
\boxed{
2\sum_{p<r}a_{p,N}a_{r,N}
\ge E_N-D_N.
}
\tag{L-93242.17}
\]

Thus any endpoint obstruction exceeding the same-prime budget has one explicit row direction in which a positive distinct-prime correlation survives.

## 4. Normalised PIG consequence

The complete endpoint PIG of `T-93010` is

\[
\mathscr P_\circ(N)
=\frac1{N^2}\|R_N\|_2^2.
\tag{L-93242.18}
\]

Combining (L-93242.11), (L-93242.15), and (L-93242.16) gives

\[
\boxed{
\#\{p:a_{p,N}>0\}
\ge
\frac{\mathscr P_\circ(N)}{576\log^2N},
}
\tag{L-93242.19}
\]

and

\[
\boxed{
|J_N|
\ge
\frac{\mathscr P_\circ(N)}{2304\log^2N}.
}
\tag{L-93242.20}
\]

These are inverse theorems, not upper bounds for \(\mathscr P_\circ(N)\).

## 5. A pure distinct-prime Q4 criterion

Normalize the diagonal and cross terms by

\[
\mathfrak D_\circ(N)=\frac{D_N}{N^2},
\qquad
\mathfrak C_{\ne p}(N)
=\frac{2}{N^2}
  \sum_{p<r}\langle R_{N,p},R_{N,r}\rangle.
\tag{L-93242.21}
\]

Equations (L-93242.11), (L-93242.12), and (L-93242.18) give

\[
\boxed{
\mathscr P_\circ(N)
=\mathfrak D_\circ(N)+\mathfrak C_{\ne p}(N),
\qquad
0\le\mathfrak D_\circ(N)\le576\log^2N.
}
\tag{L-93242.22}
\]

Therefore the complete endpoint PIG is polylogarithmic if and only if the complete distinct-prime Gram correlation is polylogarithmic:

\[
\boxed{
\mathscr P_\circ(N)\ll(\log N)^A
\text{ for some fixed }A
\iff
|\mathfrak C_{\ne p}(N)|\ll(\log N)^{A'}
\text{ for some fixed }A'.
}
\tag{L-93242.23}
\]

The forward implication uses

\[
|\mathfrak C_{\ne p}|
\le\mathscr P_\circ+\mathfrak D_\circ,
\]

and the reverse implication uses (L-93242.22). Thus every one-prime Euler self-correlation is unconditionally removed from the Q4 endpoint gate, without separating the large linear and weighted-Goldbach cancellations.

Conditional on the proposed equivalence in `T-93010`, this becomes the pure distinct-prime criterion

\[
\boxed{
\mathrm{RH}
\iff
|\mathfrak C_{\ne p}(N)|
\ll(\log N)^A
\quad(N\ge2)
\text{ for some fixed }A.
}
\tag{L-93242.24}
\]

This is a reduction of the frozen Q4 criterion, not an unconditional proof of the required cross-prime estimate.

## 6. Conditional consequence of an off-line zero

`T-93010` proposes the following pole-to-energy implication: if \(\zeta(\rho)=0\) with \(\beta=\operatorname{Re}\rho>1/2\), then for every

\[
0<\varepsilon<\beta-\frac12
\]

one cannot have

\[
\mathscr P_\circ(N)
=O\left(N^{2\beta-1-2\varepsilon}\right).
\tag{L-93242.25}
\]

Because \(\mathfrak D_\circ(N)\) is polylogarithmic, (L-93242.22) then forces the same super-polylogarithmic growth in the positive direction for \(\mathfrak C_{\ne p}(N)\) along a sequence. In addition, (L-93242.19) yields

\[
\boxed{
\limsup_{N\to\infty}
\frac{
 \#\{p:a_{p,N}>0\}\,\log^2N
}{N^{2\beta-1-2\varepsilon}}
=\infty.
}
\tag{L-93242.26}
\]

The same statement, with a factor four loss, holds for the minimum half-carrier set \(J_N\). Informally, an off-line zero of depth \(\beta-1/2\) forces coherent participation of

\[
N^{2\beta-1-o(1)}
\]

distinct prime towers along a sequence of Q4 endpoints.

This is compatible with the number of available primes and is not a contradiction. It identifies the deterministic distinct-prime resonance that a Q4 closure theorem must exclude.

## 7. Relation to the weighted-Goldbach frontier

`L-93013` removes same-prime towers from the two quadratic kernels and keeps the large \(C_N,R_1(N)\) cancellation coupled. The present lemma takes a complementary route:

\[
\text{complete endpoint row}
\longrightarrow
\text{prime-base vectors}
\longrightarrow
\text{positive diagonal plus exact cross Gram}.
\]

This automatically keeps every linear, endpoint, max-kernel, and weighted-Goldbach contribution in its correct combination. Expanding (L-93242.12) recovers a distinct-prime correlation, but the positive row-space form supplies an explicit dual direction and a quantitative number of participating prime bases.

## 8. Proof boundary

Established natively in this packet:

- exact prime-base decomposition of the complete actual source and row;
- full same-prime diagonal bound \(D_N\le576N^2\log^2N\);
- exact complete-row Gram split;
- rank-one half-space witness;
- quantitative distinct-prime carrier bounds;
- reduction of the complete endpoint PIG to the pure distinct-prime Gram correlation.

Imported, proposed, and not re-proved here:

- `T-93010` endpoint PIG criterion and pole-to-energy implication.

Open:

- an unconditional polylogarithmic upper bound for \(\mathscr P_\circ(N)\);
- deterministic exclusion of the Q4 prime-block coherence witness;
- RH.
