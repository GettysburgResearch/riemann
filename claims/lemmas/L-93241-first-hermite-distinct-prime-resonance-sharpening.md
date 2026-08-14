# L-93241 — First-Hermite negativity forces \(\gg (\log T)^2/q\) distinct prime blocks

Claim ID: `L-93241`  
Status: **PROPOSED COMPLETE SHARPENING ON FROZEN FIRST-HERMITE INPUTS — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Depends on: `L-93240`; PR #392 at `d2387cd21eb891a8801fd122bc8d0ddd7c1c0fc4`, especially `research/external/anthropic-zeta23/proofs/LINEAR_RESOLUTION_FIRST_HERMITE_RIGIDITY.md`; PR #390 at `ea20af8867c3119c23efc27738d343aac2f79362`, especially the coefficient-energy estimate \(V(q)=q+O(\sqrt q)\)  
Scope: the truncated first-Hermite prime polynomial at one carrier; the final deterministic resonance exclusion and RH remain open

## 1. Frozen first-Hermite object

For \(q\ge1\), put

\[
h_q(u)=\left(1-\frac{u^2}{2q}\right)e^{-u^2/(4q)},
\qquad
b_q(n)=\frac{\Lambda(n)}{\sqrt n}h_q(\log n).
\tag{L-93241.1}
\]

Fix \(a>2\) and truncate at \(n\le e^{aq}\):

\[
S_{q,a}(t)=\sum_{n\le e^{aq}}b_q(n)n^{it}.
\tag{L-93241.2}
\]

Group every power of one prime before taking an absolute value:

\[
Y_{p,q,a}(t)
=\sum_{\substack{r\ge1\\p^r\le e^{aq}}}
 b_q(p^r)p^{irt},
\qquad
S_{q,a}(t)=\sum_pY_{p,q,a}(t).
\tag{L-93241.3}
\]

Define the fixed-carrier prime-block diagonal

\[
D_{q,a}(t)=\sum_p|Y_{p,q,a}(t)|^2.
\tag{L-93241.4}
\]

The load-bearing point of this note is that \(D_{q,a}(t)\) is still only \(O(q)\), uniformly in the carrier, despite all interference among powers of one prime.

## 2. The Hermite factor is bounded by one

Put \(x=u^2/(2q)\ge0\). Then

\[
|h_q(u)|=|1-x|e^{-x/2}.
\]

For \(0\le x\le1\) this is at most one. For \(x\ge1\), the function

\[
(x-1)e^{-x/2}
\]

has its maximum at \(x=3\), where it equals \(2e^{-3/2}<1\). Therefore

\[
\boxed{|h_q(u)|\le1.}
\tag{L-93241.5}
\]

## 3. Complete same-prime-tower budget

Let

\[
V(q)=\sum_{n\ge2}|b_q(n)|^2.
\tag{L-93241.6}
\]

By the triangle inequality inside each prime block,

\[
\begin{aligned}
D_{q,a}(t)
&\le
\sum_p\left(
  \sum_{\substack{r\ge1\\p^r\le e^{aq}}}|b_q(p^r)|
\right)^2\\
&\le V(q)+C_{\rm tower},
\end{aligned}
\tag{L-93241.7}
\]

where the off-diagonal tower constant is

\[
\boxed{
C_{\rm tower}
=
\sum_p
\frac{2(\log p)^2p^{-3/2}}
 {(1-p^{-1/2})^2(1+p^{-1/2})}.
}
\tag{L-93241.8}
\]

Indeed, (L-93241.5) gives

\[
|b_q(p^r)|\le(\log p)p^{-r/2},
\]

and, with \(x=p^{-1/2}\),

\[
2\sum_{1\le r<s}x^{r+s}
=
\left(\sum_{r\ge1}x^r\right)^2
-
\sum_{r\ge1}x^{2r}
=
\frac{2x^3}{(1-x)^2(1+x)}.
\tag{L-93241.9}
\]

The constant is finite. A deliberately coarse explicit bound is

\[
\boxed{C_{\rm tower}\le1152.}
\tag{L-93241.10}
\]

To see this, for \(p\ge2\),

\[
1-p^{-1/2}>\frac14,
\]

so the summand in (L-93241.8) is at most

\[
32(\log p)^2p^{-3/2}.
\]

For \(x\ge1\), maximising \((\log x)x^{-1/8}\) gives

\[
\log x\le3x^{1/8}.
\]

Hence

\[
C_{\rm tower}
\le288\sum_{n=2}^{\infty}n^{-5/4}
\le288\int_1^\infty x^{-5/4}\,dx
=1152.
\]

Combining this with the frozen estimate \(V(q)=q+O(\sqrt q)\),

\[
\boxed{
D_{q,a}(t)\le V(q)+1152\ll q+1
}
\tag{L-93241.11}
\]

uniformly in \(a>2\), \(q\ge1\), and \(t\in\mathbb R\).

## 4. Sharpened deterministic inverse theorem

Assume

\[
H:=|S_{q,a}(t)|>0,
\qquad
e^{i\theta}=\frac{S_{q,a}(t)}{|S_{q,a}(t)|}.
\]

For every prime block define

\[
A_p=
\left[
\operatorname{Re}\left(e^{-i\theta}Y_{p,q,a}(t)\right)
\right]_+.
\tag{L-93241.12}
\]

Applying `L-93240` in the one-dimensional complex Hilbert space gives

\[
\sum_pA_p\ge H,
\qquad
\sum_pA_p^2\le V(q)+1152.
\tag{L-93241.13}
\]

Therefore the number of prime bases with positive block projection satisfies

\[
\boxed{
\#\{p:A_p>0\}
\ge
\frac{H^2}{V(q)+1152}.
}
\tag{L-93241.14}
\]

If \(J\) is a smallest set of prime bases carrying half of the positive projection,

\[
\sum_{p\in J}A_p\ge\frac H2,
\]

then

\[
\boxed{
|J|\ge\frac{H^2}{4(V(q)+1152)}.
}
\tag{L-93241.15}
\]

Moreover the nonnegative rank-one distinct-prime certificate obeys

\[
\boxed{
2\sum_{p<r}A_pA_r
\ge H^2-(V(q)+1152).
}
\tag{L-93241.16}
\]

If \(A_p>0\), at least one prime-power term in (L-93241.3) has positive projection after the same rotation. Thus one may select one power of each of the distinct prime bases in (L-93241.14), and all selected coordinates lie in the same open half-plane.

The complete scalar square also has the exact pure-prime split

\[
|S_{q,a}(t)|^2
=D_{q,a}(t)+\mathfrak C^{\rm heat}_{\ne p}(q,a,t),
\qquad
\mathfrak C^{\rm heat}_{\ne p}
=2\sum_{p<r}\operatorname{Re}
 \left(Y_{p,q,a}(t)\overline{Y_{r,q,a}(t)}\right).
\tag{L-93241.16a}
\]

Hence

\[
\boxed{
\mathfrak C^{\rm heat}_{\ne p}(q,a,t)
\ge H^2-(V(q)+1152).
}
\tag{L-93241.16b}
\]

Every same-prime Euler self-correlation is therefore paid inside a uniformly \(O(q)\) diagonal. Any first-Hermite obstruction of size \(H\) is, up to that diagonal, a genuinely distinct-prime correlation.

## 5. Consequence for a negative first-Hermite centre

PR #392 proves on its frozen inputs that, for \(t\in[T,2T]\), \(L=\log T\), and the stated linear-resolution range,

\[
\mathcal M(q,t)<0
\quad\Longrightarrow\quad
|S_{q,a}(t)|\ge cL
\tag{L-93241.17}
\]

for an absolute \(c>0\) after increasing the threshold height.

Equations (L-93241.11), (L-93241.14), and (L-93241.15) therefore give

\[
\boxed{
\mathcal M(q,t)<0
\quad\Longrightarrow\quad
\#\{\text{distinct aligned prime bases}\}
\gg_a\frac{L^2}{q+1}.
}
\tag{L-93241.18}
\]

The same lower bound holds for the minimum number of prime blocks needed to carry half of the positive projection, up to an absolute factor four.

At the terminal scale \(q\asymp\log\log T\), one negative carrier must therefore coordinate

\[
\boxed{
\gg
\frac{(\log T)^2}{\log\log T}
}
\tag{L-93241.19}
\]

distinct prime bases in one common half-plane.

PR #392 obtained only \(\gg L^2/q^2\) distinct primes because it first selected prime-power coordinates and then divided by the maximum number \(O(q)\) of powers belonging to one prime. Paying the full same-prime tower in (L-93241.7) removes that loss.

## 6. What remains

This is a deterministic strengthening, not the final resonance exclusion. It proves that any surviving carrier is supported by a positive distinct-prime block correlation of size \(\gg L^2\), after every one-prime tower has been paid inside \(D_{q,a}(t)\).

The remaining theorem must use the special phases

\[
e^{it\log p}
\]

and the first-Hermite block polynomials to exclude that one prescribed-carrier half-space alignment. Another density or moment estimate alone still does not remove a single exceptional point.

## 7. Proof boundary

Established natively in this packet:

- \(|h_q|\le1\);
- the uniform complete same-prime-tower budget;
- the explicit constant \(C_{\rm tower}\le1152\);
- the \(H^2/(q+1)\) distinct-prime block inverse theorem;
- the rank-one distinct-prime cross certificate.

Imported from frozen predecessors:

- the exact first-Hermite formula;
- negative centre \(\Rightarrow |S_{q,a}(t)|\gg\log T\);
- \(V(q)=q+O(\sqrt q)\);
- the linear-resolution range.

Open:

- deterministic exclusion of the aligned prime blocks;
- pointwise first-Hermite positivity;
- RH.
