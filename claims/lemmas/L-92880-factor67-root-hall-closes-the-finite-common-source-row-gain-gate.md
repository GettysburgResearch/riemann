# L-92880 — Factor-67 root Hall closes the finite common-source row-gain gate

Claim ID: `L-92880`
Status: **PROVED EXACT COMPILATION ON THE FROZEN ROOT-HALL AND PROFILE INPUTS — INDEPENDENT RECONSTRUCTION REQUIRED**
Created: 2026-08-15
Primary inputs: `L-91690`, `L-91682`, `L-91674`
RH status: **unproved at this claim**

## 1. Root window and one source flow

Put

\[
K_X=\left\lfloor\frac X{67}\right\rfloor+1.
\]

For every retained endpoint-frame coordinate `s>=K_X`, set `x=X/s`. Then

\[
1\le x<67.
\]

Only squarefree divisors of `P_61` occur in the root Hall problem. For a causal source node `k<=x`, define

\[
T_x(k)=\frac{4\sqrt{x/k}-3}{\sqrt k},\qquad
S_x(k)=\frac{5\sqrt{x/k}-3}{\sqrt k},
\]

and, for every active component row `2<=j<=66`,

\[
A_{x,j}(k)=\frac{Q_{x/k}(j)}{\sqrt k}.
\]

The frozen prefix theorem in `L-91690` gives one deterministic nonnegative no-upward target transport

\[
t_x(o,e)\ge0,
\qquad t_x(o,e)>0\Longrightarrow e\le o,
\]

satisfying

\[
\sum_e t_x(o,e)=T_x(o),
\qquad
\sum_o t_x(o,e)\le T_x(e).
\]

Define the unused positive coefficient

\[
\nu_x(e)=1-\frac{1}{T_x(e)}\sum_o t_x(o,e)\in[0,1].
\]

Each source occurrence is used exactly once: in one matched pair or in the residual coefficient `nu_x(e)`.

## 2. Target exactness

Conservation of the transported target gives

\[
\boxed{
\sum_{k\le x}\mu(k)T_x(k)
=
\sum_{\mu(e)=1}\nu_x(e)T_x(e).
}
\tag{L-92880.1}
\]

Thus the residual positive source is target-exact, not merely subordinate.

## 3. The same flow is score-superordinate

For `z>=1`,

\[
f(z)=\frac{5z-3}{4z-3}
\]

has

\[
f'(z)=-\frac{3}{(4z-3)^2}<0.
\]

If `e<=o`, then `sqrt(x/e)>=sqrt(x/o)` and therefore

\[
\frac{S_x(e)}{T_x(e)}
\le
\frac{S_x(o)}{T_x(o)}.
\]

Using the same target flow in the score coordinate yields

\[
\boxed{
\sum_{\mu(e)=1}\nu_x(e)S_x(e)
\ge
\sum_{k\le x}\mu(k)S_x(k).
}
\tag{L-92880.2}
\]

No second Hall transport and no source-mass-to-signed-loss inference is used.

## 4. The same flow gives every component-row bonus

Put

\[
\rho_{x,j}(k)=\frac{A_{x,j}(k)}{T_x(k)}
=
\frac{Q_{x/k}(j)}{4\sqrt{x/k}-3}.
\]

The frozen target-normalized profile theorem says that

\[
Y\mapsto\frac{Q_Y(j)}{4\sqrt Y-3}
\]

is increasing on its causal support. Therefore `e<=o` implies

\[
\rho_{x,j}(e)\ge\rho_{x,j}(o).
\]

Define

\[
B_{x,j}
=
\sum_{o,e}t_x(o,e)
\bigl[\rho_{x,j}(e)-\rho_{x,j}(o)\bigr]\ge0.
\]

Then

\[
\boxed{
\sum_{k\le x}\mu(k)A_{x,j}(k)
=
\sum_{\mu(e)=1}\nu_x(e)A_{x,j}(e)+B_{x,j}
}
\tag{L-92880.3}
\]

simultaneously for every declared component row. The row bonus is target-null and remains current-owned.

## 5. Positive endpoint integration

Preserve the endpoint label, small-divisor Hall label, rough first-owner label and current/child label. Positive integration and `L-91674` preserve (L-92880.1)–(L-92880.3) in target, score, rows and ordinary responses at `q` and `4q`; radix-four detail is formed only afterward.

Thus Gate A is closed by one common source flow on the complete finite root domain.

## 6. Boundary

```text
root domain x<67                              exact
one target Hall flow                          exact on frozen prefix theorem
target equality                               exact
score superordination                         exact
all declared component-row bonuses            exact / nonnegative
positive endpoint integration                 formal exact / L-91674
stopped-leaf Hall                             not used
Lorenz determinant campaign                   not used
finite realization and native correction      L-92881
Riemann Hypothesis                            unproved
```
