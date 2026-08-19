# L-99031 — Dividing out survival reveals a discounted Bellman law for literal-score debt

Claim ID: `L-99031`  
Status: **PROPOSED COMPLETE EXACT THEOREM**  
Created: 2026-08-19  
Parent: `L-99021`; strengthens the score interface in `L-99024`  
RH status: **not assumed**

## 1. Packet defect

Let `P` be a positive residual-source packet with declared score `S(P)`,
literal physical-row score `H(P)`, target mass `m(P)`, and active rough primes

\[
 67\le p_1<\cdots<p_k,\qquad r_i=p_i^{-1/2}.
\]

Write

\[
 \delta(P)=S(P)-H(P).
\tag{L-99031.1}
\]

The Hall row sort is excluded: it has no declared score, has nonnegative literal
score, and never enters a child.

## 2. Exact causal decomposition

Put

\[
 s_i=\prod_{h\le i}(1-r_h),\qquad
 \lambda_i=r_is_{i-1},\qquad
 \alpha_i=r_i\lambda_i.
\]

With `C_i(P)=P-r_iU_iP_i`, the exact causal identity is

\[
 P=s_kP+\sum_i\lambda_iC_i(P)+\sum_i\alpha_iU_iP_i.
\tag{L-99031.2}
\]

Declared score and literal score are both linear on this identity. Same-index
placement preserves both. Therefore

\[
 \delta(P)=s_k\delta(P)+\sum_i\lambda_i\delta(C_i(P))
 +\sum_i\alpha_i\delta(P_i).
\tag{L-99031.3}
\]

The edge theorem `L-99021.5`, extended by positive linearity over source atoms,
says exactly

\[
 \boxed{\delta(C_i(P))\le0.}
\tag{L-99031.4}
\]

## 3. The survival-resolvent identity

If the packet has at least one active rough prime, then

\[
 1-s_k=\sum_i\lambda_i>0.
\]

Define

\[
 \pi_i=\frac{\lambda_i}{1-s_k},\qquad \sum_i\pi_i=1.
\tag{L-99031.5}
\]

Rearranging (L-99031.3) gives the exact identity

\[
\boxed{
 \delta(P)=\sum_i\pi_ir_i\delta(P_i)
  +\sum_i\pi_i\delta(C_i(P)).
}
\tag{L-99031.6}
\]

The second term is nonpositive. Consequently

\[
\boxed{
 \delta_+(P)
 \le\sum_i\pi_ir_i\delta_+(P_i)
 \le\frac1{\sqrt{67}}\sup_i\delta_+(P_i).
}
\tag{L-99031.7}
\]

The self-survival packet has disappeared. Equation (L-99031.6) is a discounted
Bellman law, not a branching mass estimate.

## 4. Target-normalized form

Same-index child placement is target nonexpansive:

\[
 m(P_i)\le m(P).
\tag{L-99031.8}
\]

For `m(P)>0`, put `e(P)=delta_+(P)/m(P)`. Then

\[
\boxed{
 e(P)\le\sum_i\pi_ir_i\frac{m(P_i)}{m(P)}e(P_i)
 \le\frac1{\sqrt{67}}\sup_i e(P_i).
}
\tag{L-99031.9}
\]

Thus arbitrary rough-prime lists, varying child masses, and arbitrary branching
width are harmless. No leaf count appears.

Iterating along the Markov kernel `pi_i` until the terminal stopping time `tau`
gives

\[
\boxed{
 \delta_+(P)\le
 \mathbb E_P\!\left[
   \left(\prod_{h<\tau}p_h^{-1/2}\right)\delta_+(P_\tau)
 \right].
}
\tag{L-99031.10}
\]

## 5. Terminal debt is at most twice target mass

At a terminal quotient `1<=Y<67`,

\[
 S(Y)=5\sqrt Y-3,\qquad T(Y)=4\sqrt Y-3,
\]

while the literal entropy `E(Y)` is nonnegative. Since

\[
 2T(Y)-S(Y)=3(\sqrt Y-1)\ge0,
\]

one has without computation

\[
\boxed{
 [S(Y)-E(Y)]_+\le S(Y)\le2T(Y).
}
\tag{L-99031.11}
\]

Hence every terminal packet satisfies

\[
 \delta_+(P_\tau)\le2m(P_\tau).
\tag{L-99031.12}
\]

Combining target nonexpansivity with optional stopping, every packet satisfies

\[
 \boxed{\delta_+(P)\le2m(P),}
\tag{L-99031.13}
\]

and every nonterminal packet satisfies

\[
 \boxed{\delta_+(P)\le\frac2{\sqrt{67}}m(P).}
\tag{L-99031.14}
\]

## 6. Integrated factor-67 root

Apply the theorem fibrewise to the positive Hall residual-source sort and then
integrate. Tonelli is legitimate because target masses and positive defects are
nonnegative. `L-99030` gives total root target mass below `16`. Therefore

\[
\boxed{
 \delta_{\rm arithmetic}^{+}<32.
}
\tag{L-99031.15}
\]

The Hall row bonus has nonnegative literal score and can only improve the bound.

This estimate is independent of the number of rough primes, number of leaves,
prime values, path depths, child grouping, and any artificial deterministic
division by `67`.

## 7. Mutation firewalls

The proof fails immediately if:

1. the factor `1-s_k` is not divided out;
2. a current difference has positive declared-minus-literal debt;
3. the Hall row bonus is exported to a child;
4. child target mass is enlarged by placement;
5. a terminal packet is assigned more than twice its target as score debt.

`X-99030` includes exact rational mutations for the first two failures.

```text
causal coefficient identity                    exact
survival-resolvent Bellman identity            exact
arbitrary rough-prime path contraction         exact
terminal debt / target <=2                     elementary exact
integrated arithmetic debt <32                 exact on L-99030 measure
fixed-67 level telescope                       unnecessary
Riemann Hypothesis                             unproved
```
