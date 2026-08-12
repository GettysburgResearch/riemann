# L-91340 — The finite reset forcing has a positive score-exact, target-subordinate kernel representation

Claim ID: `L-91340`  
Status: **PROVED EXACT FINITE-WINDOW SOURCE-TYPING THEOREM**  
Created: 2026-08-12  
Depends on: `L-91109`, `L-91320`, `L-91321`, `L-91339`  
RH status: **unproved**

## 1. Target and score atoms

On one reset window put

\[
 W_\Psi(x,n)=\frac{4\sqrt x}{n}-\frac3{\sqrt n},
 \qquad
 W_S(x,n)=\frac{5\sqrt x}{n}-\frac3{\sqrt n}.
\tag{L-91340.1}

Both are positive for `n<=x`. Let

\[
 q_x(n)=\frac{W_\Psi(x,n)}{W_S(x,n)}.
\tag{L-91340.2}

Writing `t=sqrt(x/n)>=1`,

\[
 q_x(n)=\frac{4t-3}{5t-3}.
\]

Since

\[
 \frac d{dt}\frac{4t-3}{5t-3}
 =\frac3{(5t-3)^2}>0,
\]

one has

\[
\boxed{
 e\le o
 \Longrightarrow
 q_x(e)\ge q_x(o).
}
\tag{L-91340.3
}

Thus a smaller integer provides at least as much target per unit endpoint score.

## 2. A strict score-channel Hall margin

Let `H_(1,t)` be the reserve Hall margin of `L-91109` and let `H_(2,t)^0`
be the no-upward equality Hall margin of `L-91320`. The score kernel is the
positive combination

\[
 W_S=2w_2+w_1.
\]

Therefore its no-upward Hall margin is

\[
 \mathcal H_{S,t}
 =2\mathcal H_{2,t}^0+\mathcal H_{1,t}.
\tag{L-91340.4}

The directed corridors give

\[
 \mathcal H_{2,t}^0>-rac9{50},
 \qquad
 \mathcal H_{1,t}>rac{39}{100}.
\]

Hence

\[
\boxed{
 \mathcal H_{S,t}
 >-rac{18}{50}+rac{39}{100}
 =rac3{100}
}
\tag{L-91340.5
}

throughout

\[
 1\le x\le c_0^{-1}
\]

and at every active odd threshold.

By the nested-neighborhood Hall theorem, all odd score demand admits a positive
transport into even score capacity with support

\[
\boxed{e\le o.}
\tag{L-91340.6
}

## 3. Residual positive coefficient measure

Let `t_(o,e)>=0` denote any such transport in **score-mass units**. Thus

\[
 \sum_e t_{o,e}=W_S(x,o)
\]

for every odd atom, while

\[
 \sum_o t_{o,e}\le W_S(x,e)
\]

for every even atom.

Define the residual even score mass

\[
 r_e=W_S(x,e)-\sum_ot_{o,e}\ge0
\]

and the positive coefficient measure

\[
\boxed{
 \nu_x(e)=\frac{r_e}{W_S(x,e)}\ge0.
}
\tag{L-91340.7
}

Then the signed finite forcing score is represented exactly:

\[
\boxed{
 \sum_e\nu_x(e)W_S(x,e)
 =
 \sum_{\mu(e)=1}W_S(x,e)
 -\sum_{\mu(o)=-1}W_S(x,o).
}
\tag{L-91340.8
}

Thus the finite Möbius/parity forcing has been converted into a positive measure
in the kernel class of `L-91339` without losing endpoint score.

## 4. The positive representation is target-subordinate

The target carried by the residual positive measure is

\[
 \sum_e\nu_x(e)W_\Psi(x,e)
 =\sum_er_eq_x(e).
\]

The original signed target forcing is

\[
 \sum_eW_\Psi(x,e)-\sum_oW_\Psi(x,o).
\]

Subtracting and using the score transport,

\[
\begin{aligned}
 &\sum_e\nu_x(e)W_\Psi(x,e)
 -\left(\sum_eW_\Psi(x,e)-\sum_oW_\Psi(x,o)\right)\\
 &\qquad
 =\sum_{o,e}t_{o,e}[q_x(o)-q_x(e)]\le0
\end{aligned}
\]

by (L-91340.3) and `e<=o`. Therefore

\[
\boxed{
 \sum_e\nu_x(e)W_\Psi(x,e)
 \le
 \sum_{\mu(e)=1}W_\Psi(x,e)
 -\sum_{\mu(o)=-1}W_\Psi(x,o).
}
\tag{L-91340.9
}

The unused difference is positive target capacity. No target overdraw occurs.

## 5. Compatibility with divisor and endpoint packets

Each score-transport edge has `e<=o`. As in `L-91320/L-91321`, its coefficient
difference integrates to a nonnegative interval seed and then to nonnegative
endpoint/butterfly packets with exact ordinary-divisor and radix-four
destinations.

The residual measure `nu_x` is already coefficientwise positive. Consequently
the complete finite forcing is represented by

```text
one positive W_Psi/W_S kernel measure nu_x;
positive interval/butterfly transport packets;
unused positive target capacity.
```

All three pieces are admissible in the sum-before-quantize assembly.

## 6. Coefficient-one rough reset

Apply the geometric child identity `L-91339` to the positive measure `nu_x`.
The child measure at endpoint `x/p` has coefficient exactly one in both target
and score. Harmonic slack and activation frontier have score at least target.

Thus the finite forcing source typing needed in `L-91339.6` is supplied on every
factor-54 reset window.

The source measure changes from generation to generation, but it remains inside
the same positive kernel class; no Möbius sign reappears after the Hall
projection.

## 7. Bounded local debt

The score is represented exactly, while the target representation is a
submeasure of the available target. Therefore this finite source typing creates
no positive score loss beyond the already explicit unused target remainder.

All normalized states live in the fixed compact window and the Hall margins are
uniform. The unused target and the finite interval/port corrections are bounded
per generation and are covered by the additive debt allowance of `T-91101`.

No inherited child loss is multiplied by a factor larger than one.

## 8. Proof boundary

```text
positive score-channel Hall margin >3/100          DIRECTED EXACT
no-upward score transport                           EXACT
positive residual coefficient measure               EXACT
finite forcing score represented exactly            EXACT
positive representation target-subordinate          EXACT
interval/butterfly source lift                       AVAILABLE
coefficient-one child split for positive measure     AVAILABLE
bounded local target remainder                       EXACT / FINITE WINDOW
complete reset composition                           NEXT THEOREM
Riemann Hypothesis                                   UNPROVEN
```
