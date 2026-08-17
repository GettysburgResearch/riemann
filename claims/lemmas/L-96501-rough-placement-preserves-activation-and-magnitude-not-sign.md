# L-96501 - Rough-prime placement preserves row activation and coefficient magnitude, while parity contributes a sign cocycle

Claim ID: `L-96501`
Status: **PROVED EXACT SOURCE/ACTIVATION FUNCTOR THEOREM**
Created: 2026-08-17
RH status: **unproved**

For a squarefree source atom `k` at endpoint `X`, row `j` observes

\[
k^{-1/2}Q_{X/k}(j).
\]

If `p|k` is moved into the ordered rough history, the child endpoint and index
are `X/p` and `k/p`. Exactly

\[
\boxed{\frac{X/p}{k/p}=\frac Xk,}
\tag{L-96501.1}
\]

so every causal activation indicator `1_(X/k>=j)` is unchanged. Also

\[
\boxed{p^{-1/2}(k/p)^{-1/2}=k^{-1/2}.}
\tag{L-96501.2}
\]

Thus arbitrary rough histories preserve the same component-row atom and all
activation boundaries. However, each rough prime exchanges the even and odd
source channels. After a history `h`,

\[
\boxed{\text{signed coefficient}=(-1)^{|h|}k^{-1/2}.}
\tag{L-96501.3}
\]

Hence the activation concern does not create the failure in PR #550: activation
and coefficient magnitude are correct. The omitted interface is the sign in
(L-96501.3).
