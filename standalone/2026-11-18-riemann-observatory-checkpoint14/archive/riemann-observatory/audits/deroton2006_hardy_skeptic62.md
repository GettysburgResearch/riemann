# Literal and repaired Hardy-iteration formula in de Roton 2006

I checked the image and the raw extraction of the primary PDF's printed p. 440. Its SHA-256 is `6b379ceeead2c10e614bd4be268c9672f0b364fa95799a5474a9479a82f9e445`. The Hardy multiplier in Proposition 6.4 is visibly outside the derivative, both in the proposition and in the last line of its proof. It is not a scope ambiguity introduced by text extraction. The corrected derivative gives the formula printed in Proposition 6.5 and preserves the leading Gram calculation. [Primary published PDF, printed pp. 439–441](../sources/prefix_formula62_generalL/deroton_lower.pdf) · [Independent full-paper reading](prefix_formula62_deroton2006_full_reading.md)

## Literal witness

Write $Hf(t)=t^{-1}\int_0^t f(v)\,dv$ and $U(w)=U_F(w)$. Proposition 6.3 gives $\phi_{w,1}(t)=\partial_w[U(w)t^{-w}]+O(t^{-\varepsilon})$ for fixed $w$ with $0<\varepsilon<\Re w<\min(1,(1+1/d)/2)$. Since $H$ maps $O(t^{-\varepsilon})$ to $O(t^{-\varepsilon})$ for $\varepsilon<1$, the resulting error retains this size. The exact elementary calculation is
$$
H(t^{-w})(t)=\frac{t^{-w}}{1-w},\qquad
H(t^{-w}\log(1/t))(t)=
t^{-w}\left(\frac{\log(1/t)}{1-w}+\frac1{(1-w)^2}\right).
$$
It follows that the difference between $H\phi_{w,1}(t)$ and the printed main term at $L=k=1$ is
$$
\frac{U(w)}{(1-w)^2}t^{-w}+O(t^{-\varepsilon}).
$$
Take $F=\zeta$, $d=1$, $w=1/4$ and $\varepsilon=1/8$. This point lies inside the original $L^2$ range $\Re w<1/2$. Formula (2) gives $U_\zeta(1/4)=\pi^{1/4}\Gamma(1/8)/(3\Gamma(3/8))>0$. Thus the difference is $\frac{16}{9}U_\zeta(1/4)t^{-1/4}+O(t^{-1/8})$, which contradicts the printed $O(t^{-\varepsilon})$ remainder. No zero of zeta or RH assumption is needed for this witness. [Equation (2) and Propositions 6.3–6.4](../sources/prefix_formula62_generalL/deroton_lower.pdf)

## Correct derivative and its use

For compact $w$-sets bounded away from $\Re w=1$, the $w$-derivatives can pass under the Hardy integral using $v^{-\sup\Re w}(1+|\log v|)^k$. Applying $H^L$ to Proposition 6.3 therefore gives the corrected formula
$$
H^L\phi_{w,k}(t)=
\partial_w^k\left[(1-w)^{-L}U_F(w)t^{-w}\right]+O(t^{-\varepsilon})
$$
for $0<t<1$, locally uniformly on compact sets within $\varepsilon<\Re w<\min(1,(1+1/d)/2)$. The $\delta_{0,k}U_F\mathbf 1_{(0,1]}$ contribution in Proposition 6.3 is already $O(t^{-\varepsilon})$ and remains so after each Hardy iteration. The proof's tail bounds survive unchanged for $d\ge1$, with the possible logarithmic factor for $d=1$. Compact-set uniformity suffices for passage to the critical-line limit at each fixed zero. It avoids relying on uniform estimates throughout an unbounded open strip.

Independently, the multiplier of $H$ under the stated Mellin convention is $1/(1-w)$. This follows by integrating first in the outer variable $t$ over $t\ge v$. Hence $I-H$ has multiplier $-w/(1-w)$, and its even power $2m_F$ has multiplier $(w/(1-w))^{2m_F}$. This is the ratio $V_F(w)/U_F(w)$ in Definition 9. Applying the binomial combination of the corrected Hardy formulas gives
$$
(I-H)^{2m_F}\phi_{w,k}(t)
=\partial_w^k[V_F(w)t^{-w}]+O(t^{-\varepsilon}).
$$
After cutting away $0<t<\lambda$, the tail estimates and compact local domination yield the $L^2$ limit as $w$ approaches a fixed critical-line point. This recovers the displayed derivative in Proposition 6.5. For nonprincipal primitive Dirichlet characters, $m_F=0$, so this step uses no nontrivial Hardy iterate at all. [Definition 9 and Proposition 6.5](../sources/prefix_formula62_generalL/deroton_lower.pdf)

The missing Leibniz terms have log degree at most $k-1$, but the same power $t^{-w}$ as the main term. They cannot be absorbed into the remainder printed in Proposition 6.4. With $\Re w=1/2$ and $R=\log(1/\lambda)$, their $L^2([\lambda,1])$ norm is $O(R^{k-1/2})$ for $k\ge1$. The normalization $R^{-k-1/2}$ in Definition 12 reduces this to $O(R^{-1})$. Thus these terms do not change the limiting Gram blocks. For the target pairings the exact corrected formula is available and has the same $k=0$ term. This is a local repair to the printed calculation. It gives no counterexample to the lower theorem. [Propositions 7.1–7.2 and Definition 12](../sources/prefix_formula62_generalL/deroton_lower.pdf)
