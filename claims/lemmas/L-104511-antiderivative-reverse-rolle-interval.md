# L-104511 — Exact antiderivative interval: a sharp converse to Rolle

Claim ID: `L-104511`  
Status: **PROVED EXACT**  
Created: 2026-08-22  
RH status: **not assumed**

Let `q` be a real polynomial of degree `n-1` with `n-1` simple real zeros

\[
c_1<\cdots<c_{n-1}.
\]

Fix one antiderivative `Q`, and write every antiderivative as

\[
p_C(x)=Q(x)+C.
\]

The points `c_j` are exactly the extrema of `p_C`. Split them into local
maxima `M` and local minima `m`.

Define

\[
C_- = \max_{c\in M}[-Q(c)],
\qquad
C_+ = \min_{c\in m}[-Q(c)],
\tag{L-104511.1}
\]

with an empty maximum interpreted as `-infinity` and an empty minimum as
`+infinity`.

Then

\[
\boxed{
p_C\text{ has }n\text{ simple real zeros}
\iff C_-<C<C_+.
}
\tag{L-104511.2}
\]

At an endpoint of the closed interval, one double real zero occurs. Outside
the closed interval, every failed extremum creates one nonreal conjugate pair
according to `L-104500`.

## Proof

A local maximum of a real-rooted polynomial must be positive and a local
minimum must be negative. These conditions are exactly

\[
Q(c)+C>0\quad(c\in M),
\qquad
Q(c)+C<0\quad(c\in m),
\]

which are equivalent to (L-104511.2).

Conversely, if all extrema have the correct signs, then the values at
successive extrema alternate in sign. Together with the two polynomial tails,
there is exactly one zero in each of the `n` monotonicity intervals. Hence all
zeros are real and simple.

## Lobe-area form

For consecutive critical points,

\[
Q(c_{j+1})-Q(c_j)=\int_{c_j}^{c_{j+1}}q(t)\,dt.
\tag{L-104511.3}
\]

Thus the admissible interval is determined by alternating partial sums of the
signed lobe areas of `q`. This is the exact form of Levinson's reverse-Rolle
intuition:

```text
real-rooted derivative
+ one explicit integration-constant interval
<=> real-rooted parent.
```

For the Xi ladder, the constants are not adjustable: parity and the moments
`Xi^(k)(0)` select them. The remaining problem is to prove that these native
constants lie in the corresponding intervals, or to exclude the last failed
interval through the Pick/phase formulation.
