# L-34412 — Fixed-filter curvature bounds require the polarized jet matrix

Claim ID: `L-34412`  
Title: A parameter-independent source synthesis acts on the full polarized Jordan-curvature matrix; positivity of the scalar trace is insufficient, while matrix positivity gives the desired frame bound immediately  
Status: **PROPOSED COMPLETE EXACT HILBERT-ALGEBRA LEMMA + SCOPE FIREWALL — INDEPENDENT REVIEW REQUIRED**  
Authoring/review agent: `gpt56-sol`  
Created: 2026-08-10  
Dependencies: none beyond twice differentiable Hilbert paths  
Scope: exact abstract bridge for the compact/parity and root-of-unity frames; no assertion that the required arithmetic matrix is positive and no RH conclusion

## 1. Channel path and polarized curvature

Let `H` be a complex Hilbert space and let

\[
V(\tau)=
\begin{pmatrix}
 v_1(\tau)\\
 \vdots\\
 v_m(\tau)
\end{pmatrix}
\in H^{\oplus m}
\]

be twice differentiable at zero.  Define the Hermitian operator on the channel direct sum

\[
\boxed{
\mathcal K_V
=V'(0)V'(0)^*
 -\frac12\left[
   V(0)V''(0)^*
  +V''(0)V(0)^*
  \right].
}
\tag{L-34412.1}

In channel coordinates its entries are the polarized curvatures

\[
(\mathcal K_V)_{ab}
= v_a'v_b'^*
 -\frac12\left(v_av_b''^*+v_a''v_b^*\right).
\tag{L-34412.2}

The scalar total curvature is only the trace pairing with the identity:

\[
\boxed{
\mathfrak C(V)
=\operatorname{Tr}\mathcal K_V
=\sum_a
 \left(
  \|v_a'\|^2
  -\operatorname{Re}\langle v_a,v_a''\rangle
 \right).
}
\tag{L-34412.3}

## 2. Exact action of a fixed synthesis

Let

\[
W:H^{\oplus m}\to H^{\oplus r}
\]

be independent of the Jordan parameter and put

\[
U(\tau)=WV(\tau).
\]

Then `U'=WV'` and `U''=WV''`, so direct substitution gives

\[
\boxed{
\mathcal K_U=W\mathcal K_VW^*.
}
\tag{L-34412.4}

Consequently

\[
\boxed{
\mathfrak C(U)
=\operatorname{Tr}
 (W^*W\,\mathcal K_V).
}
\tag{L-34412.5}

This is the exact all-order reason a parameter-independent filter is the correct coordinate for the odd-Jordan programme.  No derivative gauge occurs.  But the filter acts on `K_V`, not merely on its trace.

## 3. Positive-matrix frame theorem

Assume

\[
\boxed{\mathcal K_V\succeq0}
\tag{L-34412.6}
\]

and

\[
\boxed{W^*W\preceq qI}
\tag{L-34412.7}
\]

for some `q>=0`.  Since both matrices in the trace pairing are positive semidefinite,

\[
\begin{aligned}
\mathfrak C(U)
&=\operatorname{Tr}(W^*W\mathcal K_V)\\
&\le q\operatorname{Tr}\mathcal K_V.
\end{aligned}
\]

Thus

\[
\boxed{
\mathfrak C(WV)
\le q\,\mathfrak C(V).
}
\tag{L-34412.8}
\]

If `W` is part of a parameter-independent unitary colligation, equality with the complementary output channels follows from (L-34412.4).

This is precisely the missing logical bridge between an exact source synthesis and a curvature recurrence.

## 4. Trace positivity does not suffice

A scalar augmented-reserve theorem gives only

\[
\operatorname{Tr}\mathcal K_V\ge0.
\]

That is insufficient for (L-34412.8).  The two-dimensional constant matrix

\[
\boxed{
K=
\begin{pmatrix}
2&0\\
0&-1
\end{pmatrix}
}
\tag{L-34412.9}
\]

has positive trace.  The synthesis row

\[
W=(0,1)
\]

has norm one, but

\[
WKW^*=-1.
\]

Likewise, by selecting the positive eigenline one can make the output curvature exceed any proposed bound based only on an improperly normalized scalar share of the trace.

Therefore the inference

```text
positive paired/augmented scalar reserve
+
small first-derivative synthesis charge
-> compact-output curvature bound
```

is invalid until the complete polarized matrix is shown positive or a unitary completion supplies an equivalent statement.

## 5. Root-of-unity diagonalization

Suppose a finite channel group acts on the source paths and the complete independent-frequency ledger is averaged over that group before any norm.  Fourier orthogonality can then make

\[
\mathcal K_V
=\bigoplus_{r}\mathcal K_r
\tag{L-34412.10}
\]

block diagonal.  In that coordinate, the sufficient theorem (L-34412.6) reduces to

\[
\boxed{
\mathcal K_r\succeq0
\quad\text{for every live Fourier mode }r.
}
\tag{L-34412.11}
\]

This is why the endpoint-adaptive root-of-unity constructions on PR #325/#341 are structurally relevant: they eliminate cross-mode Selberg terms before the curvature frame is applied.

The current/source DFT having only two live modes is not itself enough.  Their two polarized mode matrices must still be emitted and signed.

## 6. Application to the current live graph

PR #345 `L-34405` supplies an all-order, parameter-independent compact/parity synthesis.  PR #346 supplies a strict critical-line filter charge.  PR #350 supplies a corrected positive low-pass/root complement and the exact four-stage denominator lift.

By the present lemma, these ingredients close the curvature-frame step **if and only if** the corresponding source-complete relative jet matrix is proved positive semidefinite in the same independent-frequency metric.

The proof object must contain:

1. every generalized-prime reserve entry;
2. every bare/current/second-current source entry;
3. every cross-channel polarization;
4. every four-stage product-carry collision;
5. the exact DFT or unitary map making the matrix positive.

A scalar inequality such as

\[
A_{\rm pair}>0
\]

is only the trace of this object and may not replace it.

## 7. Proof boundary

Closed exactly:

1. definition of the polarized jet-curvature matrix;
2. exact congruence under every fixed synthesis;
3. the PSD frame theorem;
4. the trace-positivity countermodel;
5. the precise Fourier-mode reduction.

Open:

1. positivity of the complete arithmetic relative jet matrix;
2. its source-bound four-stage collision realization;
3. the compact curvature recurrence;
4. RH.
