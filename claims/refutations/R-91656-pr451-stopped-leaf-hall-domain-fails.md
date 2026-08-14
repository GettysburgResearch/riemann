# R-91656 — PR #451 stopped-leaf Hall closure fails on the permitted leaf \(p=67,y=13\)

Claim ID: `R-91656`  
Status: **EXACT REFUTATION OF THE UNIVERSAL STOPPED-LEAF HALL ASSERTION**  
Created: 2026-08-14  
Reviewed proposal: PR `#451` at `f41797c91497dc462f549a127d8494bbe4ccde2f`  
Refutes: universal use of `L-91621.12`, and therefore the universal positive Hall row identity `L-91663.9`  
Retains: `L-91663.1--.8` and the conditional same-index replacement algebra `L-91663.11--.13`  
RH status: **unproved**

## 1. The imported Hall certificate has a bounded parameter window

The imported theorem `L-91550` defines

\[
\mathcal H_{\alpha,t}(x)
=
\alpha\sqrt{x}\,A_t-B_t,
\]

where

\[
A_t=\sum_{n\le t}\frac{\mu(n)}n,
\qquad
B_t=\sum_{n\le t}\frac{\mu(n)}{\sqrt n}.
\]

Its exact checker is hard-coded with

```python
WINDOW_RIGHT = 55
```

and proves the Hall inequalities only for `1 <= x < 55`.

## 2. The stopped leaf uses the parent parameter \(py\), not the child parameter \(y\)

`L-91621` permits stopped leaves

\[
p\ge67,\qquad 1\le y<67,
\]

with complete one-prime parent row

\[
R_v^{\rm par}(j)
=
\sum_{d\mid P_{61}}
\frac{\mu(d)}{\sqrt d}Q_{py/d}(j).
\]

For the survival branch put `r=p^{-1/2}`. The pointwise target atom from `L-91560/L-91562` is

\[
(1-r)\left[2(r+2)\sqrt{\frac{py}{d}}-(r+3)\right].
\]

After restoring the common source coefficient `d^{-1/2}`, the signed prefix through a negative threshold `t` is the positive scalar `(1-r)(r+3)` times

\[
\boxed{
\mathcal H_{\alpha_s,t}(py)
=
\alpha_s\sqrt{py}\,A_t-B_t,
\qquad
\alpha_s=\frac{2(r+2)}{r+3}.
}
\]

Thus the imported Hall parameter is `x=py`. Replacing it by `y` changes the target atoms and is not licensed by the literal-row cocycle.

## 3. Exact counterexample

Take

\[
p=67,\qquad y=13,\qquad py=871,\qquad t=13.
\]

Since `mu(13)=-1`, this is an active negative Hall threshold. Exactly,

\[
A_{13}
=
\sum_{n\le13}\frac{\mu(n)}n
=
-\frac{2323}{30030}.
\]

Also

\[
B_{13}
=
1-\frac1{\sqrt2}-\frac1{\sqrt3}-\frac1{\sqrt5}
+\frac1{\sqrt6}-\frac1{\sqrt7}
+\frac1{\sqrt{10}}-\frac1{\sqrt{11}}-\frac1{\sqrt{13}}.
\]

With

\[
\alpha_s
=
\frac{2(2+1/\sqrt{67})}{3+1/\sqrt{67}},
\]

the directed exact replay `X-91664` proves

\[
\boxed{
-2.140
<
\alpha_s\sqrt{871}\,A_{13}-B_{13}
<
-2.139.
}
\]

The physical branch prefactor

\[
(1-1/\sqrt{67})(3+1/\sqrt{67})
\]

is strictly positive, and the replay gives the physical survival prefix near `-5.86384`. Hence the necessary Hall prefix condition fails:

\[
\boxed{
\mathcal H_{\alpha_s,13}(871)<0.
}
\]

There is therefore no no-upward survival-target transport satisfying `L-91621.12` on this permitted stopped leaf.

## 4. Infinite counterfamily

For fixed `y=13`, write `u=sqrt(p)`. Then

\[
\alpha_s(p)\sqrt p
=
g(u)
=
\frac{2u(1+2u)}{1+3u},
\]

and

\[
g'(u)
=
\frac{2+8u+12u^2}{(1+3u)^2}>0.
\]

Because `A_13<0`, the normalized Hall margin

\[
\sqrt{13}\,A_{13}g(\sqrt p)-B_{13}
\]

is strictly decreasing in `p`. Since it is already negative at `p=67`, the same failure holds for every rough prime `p>=67`. The corresponding parent endpoints `13p` are unbounded, so the defect cannot be absorbed into a larger finite base.

## 5. Proof-DAG consequence

The universal implication

```text
complete stopped leaf
 -> no-upward Hall transport
 -> positive residual source + positive row bonus
```

fails at its first arrow. Therefore the following statements are false as universal claims:

\[
\texttt{L-91621.12},
\qquad
\texttt{L-91621.16--.21},
\qquad
\texttt{L-91663.9}
\]

when applied to all stopped leaves in the stated domain.

Consequently `L-91665/T-91653` do not obtain the positive parent row required by

\[
d_X=R_{\rm parent}-R_{\rm ch}+d_{\rm ch}.
\]

The direct response identity itself remains valid once a genuine positive parent/child decomposition is supplied.

## 6. Surviving mathematics

This refutation does **not** affect:

1. the exact component responses
   \[
   \Gamma_Y(q)=q^{-1/2}H(Y/q),
   \qquad
   \Xi_Y(q)=q^{-1/2}[H(Y/q)-H(Y/(4q))];
   \]
2. the Möbius collapse
   \[
   \Gamma(c_X;q)=w_X(q),
   \qquad
   \Xi(c_X;q)=\Omega_X(q);
   \]
3. the conditional same-index replacement inequalities;
4. the source-disjoint least-prime partition before Hall;
5. the corrected `P_61` normalization
   \[
   \prod_{q\le61}(1+q^{-1})<14/3.
   \]

## 7. Required redesign

Extending `X-91550` from `55` to `67` cannot repair the route, because the actual Hall parameter `py` is unbounded and the prefix is genuinely negative. A successor must replace the producer, for example by proving one of:

```text
a joint survival-hazard transport;
a new exact normalization whose Hall parameter is genuinely y;
an upward-edge transport with an independent literal-row positivity theorem;
a direct non-Hall positivity theorem for the complete stopped packet.
```

```text
stopped-leaf domain p>=67, 1<=y<67             RETAINED
survival Hall parameter                         EXACTLY py
prefix at p=67,y=13,t=13                        STRICTLY NEGATIVE
universal stopped-leaf no-upward Hall            FALSE
global Hall/Fubini positive-row identity          FALSE AS STATED
native response and conditional replacement       RETAINED
T-91653 complete RH composition                   REFUTED
Riemann Hypothesis                                UNPROVEN
```
