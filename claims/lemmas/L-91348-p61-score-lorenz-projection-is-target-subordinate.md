# L-91348 — The canonical score-Lorenz projection is target-subordinate for every `P_61` one-prime packet

Claim ID: `L-91348`  
Status: **PROPOSED COMPLETE EXACT TWO-LEDGER TRANSPORT THEOREM — DIRECTED CERTIFICATE PROVIDED; INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-13  
Depends on: `L-91345`, `L-91347`; replay `X-91127`; elementary Ferrers transport and Lorenz truncation  
RH status: **unproved**

## 1. Target and score atoms

Let

\[
 P_{61}=\prod_{q\le61}q,
 \qquad p\ge67,
 \qquad1\le y\le67,
 \qquad s=\sqrt p,
 \qquad u=\sqrt y.
\]

For a divisor `d|P_61`, define causally

\[
 K_T(d)=W_\Psi(py,d)-p^{-1/2}W_\Psi(y,d),
\]

\[
 K_S(d)=W_S(py,d)-p^{-1/2}W_S(y,d),
\]

where

\[
 W_\Psi(x,d)=\frac{4\sqrt x}{d}-\frac3{\sqrt d},
 \qquad
 W_S(x,d)=\frac{5\sqrt x}{d}-\frac3{\sqrt d}.
\]

Write

\[
\boxed{
 K_T(d)=4a_d-3b_d,
 \qquad
 K_S(d)=5a_d-3b_d,
}
\tag{L-91348.1}
\]

with

\[
 (a_d,b_d)=
 \begin{cases}
 \left((s-s^{-1})u/d,\ (1-s^{-1})/\sqrt d\right),&d\le y,\\[1mm]
 \left(su/d,\ 1/\sqrt d\right),&y<d\le py,\\[1mm]
 (0,0),&d>py.
 \end{cases}
\tag{L-91348.2}
\]

Every active atom is positive in both ledgers.

## 2. Monotone likelihood ratio

Put

\[
 v_d=\frac{a_d}{b_d}.
\]

Then

\[
 v_d=
 \begin{cases}
 (s+1)\sqrt{y/d},&d\le y,\\
 s\sqrt{y/d},&y<d\le py.
 \end{cases}
\tag{L-91348.3}
\]

The function is strictly decreasing in `d`; at `d=y` it has a downward jump
from `s+1` to `s`.

The target per unit score is

\[
\boxed{
 q_d=\frac{K_T(d)}{K_S(d)}
 =\frac{4v_d-3}{5v_d-3}.
}
\tag{L-91348.4}
\]

Since

\[
 \frac d{dv}\frac{4v-3}{5v-3}
 =\frac3{(5v-3)^2}>0,
\]

one has

\[
\boxed{d_1<d_2\Longrightarrow q_{d_1}>q_{d_2}.}
\tag{L-91348.5}
\]

Thus the ordered source family has a strict monotone likelihood ratio between
target and score.

## 3. Score-currency Ferrers transport

Let `E_S` and `O_S` be the positive score measures on the even- and odd-parity
divisors of `P_61`, carrying masses `K_S(d)`.

The companion replay proves the score analogue of `L-91347`: every active odd
prefix has enough even score capacity within displacement eight.  More
precisely, the nonterminal Hall reserve is greater than `9/5`; terminal prefixes
are positive by the total score theorem `L-91345`.  Hence

\[
\boxed{
 O_S\longrightarrow E_S,
 \qquad e\le o+8,
}
\tag{L-91348.6}
\]

admits a positive Ferrers transport.

Let

\[
 M=\|O_S\|.
\]

Since the signed score is positive, `||E_S||>M`.  Define `U_S` to be the
**leftmost score submeasure** of `E_S` having total mass `M`: all even capacities
strictly below one cutoff `c` are used, a fraction of the capacity at `c` is
used, and every larger even capacity is unused.

The prefix Hall inequalities imply

\[
 U_S(( -\infty,t+8])\ge O_S(( -\infty,t])
\]

for every `t`, so `U_S` itself can be coupled to `O_S` with support `e<=o+8`.

Define the residual positive coefficient measure `nu` by

\[
\boxed{
 \nu(e)=\frac{E_S(e)-U_S(e)}{K_S(e)}\ge0.
}
\tag{L-91348.7}
\]

By construction it represents the signed score exactly:

\[
\boxed{
 \sum_e\nu(e)K_S(e)
 =\sum_{\mu(e)=1}K_S(e)-\sum_{\mu(o)=-1}K_S(o).
}
\tag{L-91348.8}
\]

## 4. Three fixed finite-prefix inequalities

For real `z>=1`, put

\[
 A(z)=\sum_{\substack{d\mid P_{61}\\d\le z}}\frac{\mu(d)}d,
 \qquad
 M(z)=\sum_{\substack{d\mid P_{61}\\d\le z}}\frac{\mu(d)}{\sqrt d},
\tag{L-91348.9}
\]

and

\[
 D(z)=A(z)-\frac{M(z)}{\sqrt z},
 \qquad
 F(z)=zA(z)-\sqrt z\,M(z)=zD(z).
\tag{L-91348.10}
\]

At an activation point the entering contribution to `F` is

\[
 \mu(d)\left(\frac dd-\frac{\sqrt d}{\sqrt d}\right)=0,
\]

so `F` is continuous.

The exact directed replay over all `2^18` divisor states proves:

\[
\boxed{
 D(c^-)>\frac3{40}
 \qquad\text{at every divisor cutoff }c\ge2,
}
\tag{L-91348.11}

\[
\boxed{-1\le A(z)\le1,}
\tag{L-91348.12}

and, on every activation cell,

\[
\boxed{
 F'(z)=A(z)-\frac{M(z)}{2\sqrt z}>\frac1{40}.
}
\tag{L-91348.13}

Therefore `F` is strictly increasing on `[1,infinity)`.

The least retained margins are

```text
D(c-) > 0.0777554756 at c=91;
F'(z) > 0.0277320851 on the cell beginning at 31.
```

## 5. Prefix determinant

Let `c` be a possible lower-tail cutoff and write

\[
 P_T(c^-)=\sum_{d<c}\mu(d)K_T(d),
 \qquad
 P_S(c^-)=\sum_{d<c}\mu(d)K_S(d).
\]

Using (L-91348.1), direct cancellation gives

\[
\boxed{
 P_T(c^-)K_S(c)-P_S(c^-)K_T(c)
 =3\bigl(A_<b_c-B_<a_c\bigr),
}
\tag{L-91348.14}

where

\[
 A_<=\sum_{d<c}\mu(d)a_d,
 \qquad
 B_<=\sum_{d<c}\mu(d)b_d.
\]

### Case 1: `c<=y`

All prefix atoms and the cutoff atom are in the inner regime.  Equation
(L-91348.14) is a positive scalar multiple of

\[
 A(c^-)-\frac{M(c^-)}{\sqrt c}=D(c^-)>0.
\tag{L-91348.15}
\]

### Case 2: `c>y`

Put `A_c=A(c^-)`, `M_c=M(c^-)`, `A_y=A(y)` and `M_y=M(y)`.  Exact summation of
(L-91348.2) gives

\[
 A_<=u\left[sA_c-\frac{A_y}{s}\right],
 \qquad
 B_<=M_c-\frac{M_y}{s}.
\]

Since the cutoff atom is in the frontier regime, the sign of
(L-91348.14) is the sign of

\[
 E(s)=sD(c)+\frac{M_y}{\sqrt c}-\frac{A_y}{s}.
\tag{L-91348.16}
\]

The atom is active only when `c<=s^2y`, so

\[
 s\ge s_0:=\sqrt{c/y}.
\]

Moreover

\[
 E'(s)=D(c)+\frac{A_y}{s^2}
 >\frac3{40}-\frac1{67}>0
\tag{L-91348.17}
\]

by (L-91348.11)--(L-91348.12).  Thus `E` is minimized at `s=s_0`.  There

\[
\boxed{
 E(s_0)=\frac{F(c)-F(y)}{\sqrt{cy}}>0
}
\tag{L-91348.18}
\]

because `c>y` and `F` is strictly increasing.

Hence in all cases

\[
\boxed{
 P_T(c^-)K_S(c)-P_S(c^-)K_T(c)>0.
}
\tag{L-91348.19}

## 6. Lorenz projection is target-subordinate

Let `q_c=K_T(c)/K_S(c)`.  The used score measure `U_S` and odd score measure
`O_S` have equal total mass.  Therefore

\[
 \int q\,d(U_S-O_S)
 =\int(q-q_c)\,d(U_S-O_S).
\tag{L-91348.20}
\]

Below `c`, the used measure equals the full even score capacity, and the
contribution is exactly

\[
 P_T(c^-)-q_cP_S(c^-)>0
\]

by (L-91348.19).  At `c` the integrand vanishes.  Above `c`, `U_S=0`, while
`q-q_c<0`; hence the contribution of `-O_S` is nonnegative.  Consequently

\[
\boxed{
 \int q\,dU_S\ge\int q\,dO_S.
}
\tag{L-91348.21}

Equivalently, the residual positive measure uses no more target than the signed
one-prime packet:

\[
\boxed{
 \sum_e\nu(e)K_T(e)
 \le
 \sum_{\mu(e)=1}K_T(e)-\sum_{\mu(o)=-1}K_T(o).
}
\tag{L-91348.22}

Thus the same canonical positive object is:

```text
score-exact;
target-subordinate;
source-faithful under a displacement-eight Ferrers transport.
```

## 7. Remaining row statement

The theorem closes the common target/score source typing.  It does not yet prove
that the same lower-tail cancellation is subordinate in every exact component
row.  `L-91346` proves the full signed inherited row has a strict `>1/500`
reserve; the remaining task is to prove the row analogue of the Lorenz prefix
determinant or charge the bounded displacement-eight row defect to that reserve.

```text
score-currency shift-eight Hall                     DIRECTED/EXACT
monotone target/score likelihood ratio              EXACT
three finite prefix inequalities                    DIRECTED/EXACT
canonical score-exact residual measure              EXACT
target subordination of the same measure            EXACT
common target/score source typing                    CLOSED
common exact-row subordination                       OPEN
activation/frontier row composition                  OPEN
Riemann Hypothesis                                   UNPROVEN
```
