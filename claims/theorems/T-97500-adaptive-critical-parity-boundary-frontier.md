# T-97500 — Small-prime critical cube and the large-prime adaptive parity frontier

Claim ID: `T-97500`  
Status: **UNCONDITIONAL REDUCTION; CONCLUSION-PRODUCING LARGE-PRIME THEOREM OPEN**  
Created: 2026-08-17  
Inputs: PR #576; `L-97500`; `R-97500`; `L-97501`; PR #547 consumer  
RH status: **unproved**

The exact portfolio after the source hardening is as follows.

1. The complete `P_61` annular `5:3` base is nonnegative and has the directed
   bias `1/42<=F/M<=1/8`.
2. The natural rough source has exact parity recursion `(I+R)\mathcal F=b`.
3. No fixed even-depth current can be positive eventually.
4. A contractive operator `A` replaces the natural source only if its current
   contains the all-depth residual `b-(R-A)\mathcal F`.
5. At every admissible rough state, an exact source-complete small-prime cube of
   growing depth `O(log log log X)` is strictly positive.

For a state with endpoint `X` and least allowed rough prime `p_0`, choose
`Z_X` and the even depth `L_X(p_0)` as in `L-97501`.  Split the exact natural
current

\[
 C_{L_X(p_0),p_0}(X)
 =\mathcal S_{p_0}(X)+\mathcal L_{p_0}(X),
 \tag{T-97500.1}
\]

where `mathcal S` is the proven positive small-prime cube and `mathcal L`
contains precisely those histories of length `<L_X(p_0)` having at least one
rough prime greater than `Z_X`.  Both terms retain literal first ownership,
activation, coefficient and cumulative parity.

Define `LAPBR67` (Large-prime Adaptive Parity Boundary, factor 67) to be

\[
 \boxed{
 \mathcal L_{p_0}(X)\ge0
 }
 \tag{T-97500.2}
\]

for every admissible state with sufficiently large endpoint.  The finitely many
smaller states are evaluated directly; when no rough prime is active, positivity
is exactly the base theorem `L-97400`.

If `LAPBR67` holds, then every adaptive even-depth current in (T-97500.1) is
nonnegative.  The exact expansion is

\[
 \mathcal F_v=C_v+
 \sum_{\substack{h:\ |h|=L_v}}
 w_h\,\mathcal F_{v_h},
 \qquad w_h\ge0,
 \tag{T-97500.3}
\]

because `L_v` is even.  Every descendant has strictly smaller endpoint.
Finite induction on the remaining rough rank therefore gives
`\mathcal F_v>=0` at every state, including the root.

The root scalar is the annular quantity

\[
 \mathcal A_X=5[c_X(2)-c_{X/4}(2)]
             +3[c_X(3)-c_{X/4}(3)].
\]

Its Mellin transform is

\[
 (1-4^{-s})\left[
 \frac6{s^2}-
 \frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}
 \right],
 \qquad z=s+\frac12,
\]

whose finite numerator is zero-free in `Re z>0`.  Landau therefore gives

\[
 \boxed{\mathrm{LAPBR67}\Longrightarrow\mathrm{RH}.}
\]

`LAPBR67` is a strictly sharper source-explicit descendant of `GABPT`: the
entire small-prime, growing-order, activation-correct cube has already been
proved positive.  Only currents meeting a rough prime larger than
`(log X)^{1/4}` remain.

```text
natural/thinned residual identity          PROVED EXACT
PR #566 natural M-matrix premise            FALSE
PR #566 contractive source equation         UNPROVEN / RESIDUAL OMITTED
all fixed even depths                       FALSE
exact small-prime adaptive cube             PROVED POSITIVE
LAPBR67                                     OPEN / RH-BEARING
Riemann Hypothesis                          UNPROVEN
```
