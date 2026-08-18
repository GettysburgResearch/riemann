# L-97901 — Exact top-history completion into finitely omitted Euler states

Claim ID: `L-97901`  
Status: **PROVED EXACT OPERATOR AND SOURCE-PARTITION THEOREM**  
Created: 2026-08-18  
Depends on: `L-97900`; PR #590 largest-prime Bellman ownership  
RH status: **not assumed**

Work at one fixed root endpoint, with zero extension below activation. For a
rough prime `q`, let

\[
 (\mathsf T_qf)(Y)=f(Y/q),
 \qquad
 \mathsf E_q=I-q^{-1}\mathsf T_q.
 \tag{L-97901.1}
\]

All dilation operators commute. Let `P=P_X` be the logarithmic cutoff of
`L-97900`, and let `U_P` be the complete cube through `P`.
For a prime `p>P`, define the state immediately before adjoining `p` by

\[
 U_{P,<p}(Y)=
 \prod_{P<q<p}\mathsf E_q\,U_P(Y).
 \tag{L-97901.2}
\]

For a finite set `A` of rough primes, define the fully completed state with the
Euler factors in `A` omitted by

\[
 U^{\widehat A}(Y)=
 \prod_{\substack{q>P\\q\notin A}}
 \mathsf E_q\,U_P(Y).
 \tag{L-97901.3}
\]

Only finitely many factors are active at a fixed endpoint.

Let `\mathcal H_p` denote the active primes greater than `p`, and write
`q_S=prod_(q in S)q`. Then the following identity is exact:

\[
 \boxed{
 U_{P,<p}(Y)=
 \sum_{S\subseteq\mathcal H_p}
 \frac1{q_S}
 U^{\widehat{\{p\}\cup S}}(Y/q_S).
 }
 \tag{L-97901.4}
\]

## Proof

For each `q>p`,

\[
 \mathsf E_q+q^{-1}\mathsf T_q=I.
 \tag{L-97901.5}
\]

Expand the commuting product of the identities (L-97901.5):

\[
 \begin{aligned}
 &\sum_{S\subseteq\mathcal H_p}
 \left(\prod_{q\in S}q^{-1}\mathsf T_q\right)
 \left(\prod_{q\in\mathcal H_p\setminus S}\mathsf E_q\right)
 \left(\prod_{P<q<p}\mathsf E_q\right)U_P\\
 &\hspace{35mm}=
 \left(\prod_{P<q<p}\mathsf E_q\right)U_P.
 \end{aligned}
\]

The summand indexed by `S` is exactly the corresponding term in
(L-97901.4). Every top history is used once, and every omitted factor is named
literally. No repeated-prime source is introduced.

## Growing finite-depth consequence

Put

\[
 K_X=\left\lfloor(\log\log X)^{1/4}\right\rfloor,
 \qquad
 H_X=X^{1/(K_X+2)}.
 \tag{L-97901.6}
\]

If `p>=H_X` and a term in (L-97901.4), evaluated at `Y=X/p`, is active, then

\[
 p q_S\le X/2.
\]

Since every factor in `p q_S` is at least `H_X`, this forces

\[
 \boxed{|S|\le K_X.}
 \tag{L-97901.7}
\]

Thus every owner prime at least `H_X=X^{o(1)}` expands into a full native state
with at most `K_X+1` explicitly omitted Euler factors. Although `K_X` tends to
infinity, all omitted primes tend to infinity much faster, a fact used in
`L-97902`.

## Source meaning

Equation (L-97901.4) is the complement of largest-prime ownership. The original
child contains only primes below its owner. Completing every larger prime and
then selecting the omitted subset reconstructs that child exactly. It is not a
source-blind inverse: the omitted set records every prime already used by the
top history.