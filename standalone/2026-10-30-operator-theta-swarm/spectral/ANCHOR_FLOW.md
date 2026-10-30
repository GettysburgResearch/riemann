# Exact anchor transport through one boundary row

Status: proposed elementary operator component, with a complete finite proof.

Scope: the exact xi covariance matrices in `MOVING_ANCHOR_THEOREM.md`; the algebra also applies to any analytic source composed with the same Cayley map. This is a transport identity and a sufficient quantitative continuation condition, not a proof of the required sign.

Dependencies: the definitions of the source, Cayley map and covariance matrix in the companion proof. The finite algebra below is derived directly. No zero table, RH assumption, or moment estimate enters.

What was run: `verify_anchor_flow.py` checks the full finite matrix identity over rational numbers for different coefficient vectors and sizes, its trace, and a deliberately corrupted boundary term. These checks exercise the identity, not the actual unbounded xi source.

Smallest remaining gap: an upper bound for the potentially decreasing contribution of the actual transported boundary matrix, small enough to preserve a positive lower bound while the ratio N/a becomes unbounded. For decreasing a this is the positive part of the forward derivative.

## 1. A source-preserving differential identity

Let

\[
 f(s)=\xi'(s)/\xi(s),\qquad
 s_a(z)=\tfrac12+a\frac{1+z}{1-z},\qquad a>\tfrac12.
\]

Use the normalization

\[
 f(s_a(z))=g_0(a)+2\sum_{n\ge1}g_n(a)z^n,
 \qquad G_N(a)=(g_{|j-k|}(a))_{j,k=0}^N.
\]

Thus \(G_N=T_N/(2a)\) in the companion proof. The expansions and all differentiations are local at z=0, whose source point is greater than one. No analyticity across hypothetical zeros is assumed.

The chain rule gives the exact identity

\[
 a\partial_a f(s_a(z))
 =\frac{1-z^2}{2}\partial_z f(s_a(z)).
\tag{1}
\]

Comparing coefficients yields

\[
 a g_0'(a)=g_1(a),\qquad
 a g_n'(a)=\frac{(n+1)g_{n+1}(a)-(n-1)g_{n-1}(a)}2
 \quad(n\ge1).
\tag{2}
\]

The n=1 term contains no g_0 contribution. The recurrence retains the next coefficient; dropping it would change the source.

## 2. Finite transport and its complete boundary term

Let \(e_0,\ldots,e_N\) be the standard basis and define the real skew-symmetric matrix

\[
 K_Ne_j=\tfrac{j+1}{2}e_{j+1}-\tfrac j2 e_{j-1},
\]

where a basis vector outside 0,...,N is omitted. Let

\[
 r_N(a)=(g_{N+1}(a),g_N(a),\ldots,g_1(a))^T,
\]

\[
 B_N(a)=\frac{N+1}{2}
       \big(e_Nr_N(a)^*+r_N(a)e_N^*\big).
\]

**Theorem.** With \(\tau=\log a\),

\[
 \frac{d}{d\tau}G_N(a)
   =K_N^*G_N(a)+G_N(a)K_N+B_N(a).
\tag{3}
\]

In particular the discrepancy between finite transport and the exact derivative has rank at most two and is supported in the last row and column.

**Proof.** For the corresponding untruncated expression, the (j,k) entry is

\[
 \tfrac{j+1}{2}g_{|j+1-k|}-\tfrac j2g_{|j-1-k|}
 +\tfrac{k+1}{2}g_{|j-k-1|}-\tfrac k2g_{|j-k+1|}.
\]

If j=k this equals g_1. If j-k=n>=1, it is
\([(n+1)g_{n+1}-(n-1)g_{n-1}]/2\). The opposite triangle follows by symmetry. These are exactly (2). The only omitted terms occur at j=N or k=N; their sum is B_N, including both contributions when j=k=N. This proves (3).

The trace is a useful normalization check:

\[
 \frac{d}{d\tau}\operatorname{tr}G_N=(N+1)g_1
 =\operatorname{tr}B_N.
\tag{4}
\]

## 3. Geometric meaning and a literal continuation bound

The orthonormal Laguerre functions in the companion proof satisfy

\[
 u_{j,a}(t)=\sqrt{2a}\,e^{-at}L_j(2at),\qquad
 a\partial_a u_{j,a}
   =\frac{j+1}{2}u_{j+1,a}-\frac j2u_{j-1,a}.
\tag{5}
\]

This follows from \(xL'_j=j(L_j-L_{j-1})\) and
\(xL_j=(2j+1)L_j-(j+1)L_{j+1}-jL_{j-1}\), or directly from their finite coefficients. Thus the internal part of (3) changes the finite basis by a unitary rotation. The coupling to the next Laguerre function is the entire boundary term. It is not an omitted prime tail or a free parameter.

Fix \(\tau_0\), put \(U(\tau)=\exp((\tau-\tau_0)K_N)\), and define
\(\widetilde G(\tau)=U(\tau)G_N(e^\tau)U(\tau)^*\). Since \(K_N^*=-K_N\), (3) gives

\[
 \widetilde G'(\tau)=U(\tau)B_N(e^\tau)U(\tau)^*.
\tag{6}
\]

Consequently, for \(\tau_1<\tau_0\),

\[
 \widetilde G(\tau_1)=G_N(e^{\tau_0})
 -\int_{\tau_1}^{\tau_0}U(v)B_N(e^v)U(v)^*\,dv.
\tag{7}
\]

Let \(M_+\) denote the positive part of a Hermitian matrix. A sufficient quantitative bound for downward anchor continuation is

\[
 \left\|\int_{\tau_1}^{\tau_0}
 U(v)(B_N(e^v))_+U(v)^*\,dv\right\|
 <\lambda_{\min}(G_N(e^{\tau_0})).
\tag{8}
\]

Indeed \(B_N\le(B_N)_+\), so (7) and (8) imply positivity at the lower anchor. The sign in (8) matters: when a decreases, the positive part of the forward derivative is the possible loss. For upward continuation, the negative part is the possible loss.

The companion unconditional theorem supplies
\(G_N(a_0)>I/12\) when \(a_0\ge100(N+1)\). Proving the left side of (8) below 1/12 along a sequence of lower anchors \(a_N\ge1\) with \(N/a_N\to\infty\) would establish the positivity required by the companion RH criterion. This bound is not established here.

For a normalized eigenvector v of a simple eigenvalue lambda of G_N, the internal commutator has zero expectation, so

\[
 \frac{d\lambda}{d\tau}=(N+1)\Re\big(\overline{v_N}\,r_N^*v\big).
\tag{9}
\]

At a multiple eigenvalue the derivatives are the eigenvalues of the restriction of B_N to its eigenspace. Neither case has an automatic sign.

## 4. Why elementary positivity does not propagate for free

For a real vector r with r_N=g_1, the at-most-two nonzero eigenvalues of B_N are

\[
 \frac{N+1}{2}\big(g_1\pm\|r\|_2\big).
\tag{10}
\]

If any other coordinate of r is nonzero, one is positive and one is negative. Even a positive g_1 and a positive trace in (4) therefore do not make the boundary matrix positive semidefinite. An absolute estimate
\(\|B_N\|\le(N+1)\|r_N\|\) is valid, but can lose the orientation and cancellation visible in (7). A successful use of the flow must control the actual next-row coupling and its rotation, or construct a better source-faithful budget for it.

This transport formula supplies a concrete further attack on the scalar innovation problem. It does not convert the available large-anchor positive matrices into a proof at fixed anchor.
