# T-90502 — Pole-null Fredholm and heat-trace equivalences for RH

Claim ID: `T-90502`  
Status: **FULL EXACT EQUIVALENCE PROPOSAL — PRIME-SIDE SIGN THEOREM OPEN; INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: `L-90505`, `L-90506`, `L-90507`; Xi-cardinal capture on PR #365  
Scope: one explicit pole-null trace-class completion

Fix `1/2<a<c`, use the Cauchy–Sobolev completion `J_(a,c)`, and let

\[
 A_{a,c}^{(0)}
\]

be the trace-class Weil operator projected to the two pole-null constraints. Define

\[
 D_{a,c}^{(0)}(t)
 =\det(I+tA_{a,c}^{(0)}),
\]

\[
 \Theta_{a,c}(\beta)
 =\operatorname{tr}
 (e^{-\beta A_{a,c}^{(0)}}-I),
\]

and

\[
 H_d^{(0)}
 =\bigl(
 \operatorname{tr}[(A_{a,c}^{(0)})^{i+j+1}]
 \bigr)_{0\le i,j\le d}.
\]

Then the following are equivalent:

\[
 \boxed{
 \begin{aligned}
 &\text{(i) RH;}\\
 &\text{(ii) }A_{a,c}^{(0)}\succeq0;\\
 &\text{(iii) }D_{a,c}^{(0)}(t)>0\quad(t>0);\\
 &\text{(iv) }\Theta_{a,c}(\beta)\le0\quad(\beta>0);\\
 &\text{(v) }\operatorname{tr}
 [A_{a,c}^{(0)}e^{-\beta A_{a,c}^{(0)}}]\ge0
 \quad(\beta>0);\\
 &\text{(vi) }H_d^{(0)}\succeq0\quad(d\ge0).
 \end{aligned}}
 \tag{T-90502.1}
\]

If RH is false, the number of positive zeros of `D^(0)`, counted with multiplicity, equals the number of distinct reflected off-line pairs. Equivalently, the pole-free unprojected form has negative index exactly two more than that number:

\[
 n_-(Q)=2+n_-(A_{a,c}^{(0)}).
 \tag{T-90502.2}
\]

The prime-side form of the projected operator contains no pole term and is the exact Lévy–prime competition

\[
\begin{aligned}
 W(f,f)={}&
 \int_0^\infty
 \frac{e^{-y/2}}{1-e^{-2y}}
 \|f-T_yf\|_2^2\,dy\\
 &+2\pi\mu(0)\|f\|_2^2
 -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \Re\langle f,T_{\log n}f\rangle,
\end{aligned}
 \tag{T-90502.3}
\]

subject only to the two explicit pole-null constraints.

Therefore any one of the following would prove RH:

```text
pole-null Lee–Yang theorem:
    D_(a,c)^(0)(t)>0 for t>0;

heat-pressure theorem:
    Theta_(a,c)(beta)<=0 for beta>0;

all-order prime-word theorem:
    tr[A^(0) exp(-beta A^(0))]>=0 for beta>0;

fixed-index theorem:
    the unprojected pole-free form Q has negative index exactly two.
```

The fixed-index formulation is the sharpest conceptual compression:

```text
two negative directions are forced by the known poles at s=0,1;
every additional negative direction is exactly one off-line zero pair.
```

No unconditional proof of any displayed closing theorem is claimed.
