# R-26202 — A rank-one parity Gram cannot contract unequal channel multipliers

Claim ID: `R-26202`  
Title: The proposed finite parity-Gram shortcut is necessarily indefinite unless the two transition multipliers agree  
Status: **EXACT SCOPE REFUTATION**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Scope: refutes the naive rank-one diagonal-transition reduction floated after `L-26212`; it does not refute a complete independent-frequency source Gram with boundary and carry channels

## 1. Abstract rank-one obstruction

Let

\[
v=\begin{pmatrix}v_+\\v_-\end{pmatrix}\in\mathbb C^2,
\qquad
G=vv^*,
\]

and let

\[
T=\operatorname{diag}(a,b).
\]

Then

\[
T^*GT=ww^*,
\qquad
w=\begin{pmatrix}\overline a\,v_+\\\overline b\,v_-\end{pmatrix}.
\]

For two rank-one Hermitian forms in dimension two,

\[
\det(vv^*-ww^*)=-|\det(v,w)|^2.
\]

Here

\[
\det(v,w)=v_+v_-(\overline b-\overline a),
\]

so

\[
\boxed{
\det(G-T^*GT)
=-|v_+v_-|^2|a-b|^2.
}
\tag{R-26202.1}
\]

Consequently, whenever

\[
v_+v_-\ne0,
\qquad
a\ne b,
\]

the matrix `G-T^*GT` has negative determinant and is indefinite. In particular, no inequality

\[
G-T^*GT\succeq\eta G
\qquad(\eta\ge0)
\]

can hold.

An explicit negative direction is obtained by taking

\[
x=(-\overline{v_-},\overline{v_+})^T.
\]

Then `v^*x=0`, while

\[
w^*x=(b-a)\overline{v_+v_-},
\]

and therefore

\[
\boxed{
x^*(G-T^*GT)x=-|a-b|^2|v_+v_-|^2<0.}
\tag{R-26202.2}
\]

## 2. Application to the parity frame

The parity analysis vector is

\[
v(z)=\begin{pmatrix}p(z)\\p(-z)\end{pmatrix},
\qquad
p(z)=(1-z)(1-2z)(1-\sqrt2z)^2.
\]

Away from the finite local-zero sets, both coordinates are nonzero. Any proposed diagonal transition whose two channel multipliers differ therefore fails the rank-one test identically.

This includes the tentative reduction in which a factor-five transition was represented by two unequal scalar channel multipliers and the physical parity Gram was replaced by `v(z)v(z)^*`.

## 3. A second exact correction: quotient cells are not powers of one dyadic variable

If

\[
z=2^{-s},
\]

the quotient ratios `2,3,4` have multipliers

\[
2^{-s}=z,
\qquad
3^{-s},
\qquad
4^{-s}=z^2.
\]

The ratio-three channel is not `z^3`. Thus the polynomial

\[
z^2+z^3+z^4
\]

does not encode the factor-five cells `2,3,4` in the `z=2^{-s}` variable.

Moreover, the actual transition is a source-bound carry/reflected object, not an arbitrary diagonal multiplication on the rank-one parity frame.

## 4. Surviving scope

This refutation does **not** rule out:

1. the full two-frequency physical matrix of PR #241;
2. the exact annular physical/carry isometry of PR #268;
3. a parity-channel Gram containing independent physical rows rather than one rank-one vector;
4. a coupled boundary/transverse Schur complement;
5. a source-complete recurrence retaining all cross terms.

It rules out only the shortcut

```text
rank-one parity frame
+ unequal diagonal transition
-> positive contraction.
```

## 5. Proof boundary

Closed exactly:

- determinant identity (R-26202.1);
- explicit negative direction (R-26202.2);
- rejection of the naive finite parity contraction;
- correction of the `2,3,4` multiplier encoding.

Open:

- the complete source-image annular estimate;
- the banked transition/collar recurrence;
- RH.
