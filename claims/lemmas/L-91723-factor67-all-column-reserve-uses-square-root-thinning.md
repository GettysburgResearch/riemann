# L-91723 — A square-root safety thinning closes every factor-67 interior column

Claim ID: `L-91723`  
Status: **PROVED EXACT ALL-COLUMN REDUCTION ON FROZEN MISMATCH/COLLAR INPUTS**  
Created: 2026-08-14  
Frozen parent: PR #473 at `71d6a859ea741fe035de709e8d10ed37301b778e`  
Depends on: `L-91111`, factor-67 adjacent mismatch bound in `L-91691`, exact inner/outer carry-cell ownership, positive radix-four inverse  
Replay: `X-91723-factor67-all-column-reserve`  
RH status: **unproved**

## 1. The uncovered physical range

Put

\[
 K=K_X=\left\lfloor\frac X{67}\right\rfloor+1.
\tag{L-91723.1}
\]

The compact-reserve theorem on PR #473 proves the relative finite-realization
bound for

\[
 K\le q\le X/4
\]

and handles the terminal annulus `q>X/4` separately. Its displayed
`177/K` estimate does not cover the physical columns

\[
 2\le q<K.
\tag{L-91723.2}
\]

The endpoint collar is supported at seed indices at least `K`, but its carry
response at a smaller column samples multiples `jq>=K`; support localization
alone does not make those columns vanish.

This lemma supplies one uniform all-column estimate and a stronger positive
source thinning which closes (L-91723.2).

## 2. Exact adjacent-cell ownership of the finite mismatch

Let

\[
 \varepsilon_X(n)
 :=E_X(n)-E_X(n+1)
 =d_X^\star(n)-\int_n^{n+1}d_X^\star(t)\,dt.
\tag{L-91723.3}
\]

The factor-67 adjacent estimate of `L-91691` is

\[
 \boxed{
 |\varepsilon_X(n)|
 <\frac{19}{2}n^{-3/2}
 \qquad(n\ge K).
 }
\tag{L-91723.4}
\]

For an ordinary column `q`, define

\[
 M_q=\left\lceil\frac Kq\right\rceil
\]

and assign the exact outer mismatch carry by

\[
 \boxed{
 v_q^{\rm out}(E_X)
 =\sum_{j\ge M_q}\varepsilon_X(jq).
 }
\tag{L-91723.5}
\]

This is not a seed truncation and creates no artificial boundary jump.
The complete carry identity

\[
 v_q(E_X)=\sum_{j\ge1}\varepsilon_X(jq)
\]

is partitioned at the level of its actual adjacent cells:

```text
jq<K       exact inner recursive owner;
jq>=K      one current outer mismatch owner.
```

Thus every local quadrature-error cell has one owner.

## 3. Uniform ordinary mismatch bound

For every integer `M>=1`,

\[
 \sum_{j\ge M}j^{-3/2}<3M^{-1/2}.
\tag{L-91723.6}
\]

Equations (L-91723.4)--(L-91723.6) give, for every `q>=2`,

\[
\begin{aligned}
 |v_q^{\rm out}(E_X)|
 &<\frac{19}{2}q^{-3/2}
   \sum_{j\ge M_q}j^{-3/2}\\
 &<\frac{57}{2}q^{-3/2}M_q^{-1/2}\\
 &\le\frac{57}{2q\sqrt K}.
\end{aligned}
\]

Hence

\[
 \boxed{
 |v_q^{\rm out}(E_X)|
 <\frac{57}{2q\sqrt K}
 \qquad(q\ge2).
 }
\tag{L-91723.7}
\]

For `q>=K`, this is weaker than the retained `q^{-3/2}` estimate. Its purpose
is uniform control below `K`.

## 4. Uniform radix-four mismatch bound

Apply (L-91723.7) at `q` and `4q`. Then

\[
\begin{aligned}
 |\mathcal D_4v_q^{\rm out}(E_X)|
 &\le |v_q^{\rm out}(E_X)|
     +2|v_{4q}^{\rm out}(E_X)|\\
 &<\frac{57}{2q\sqrt K}
    +\frac{57}{4q\sqrt K}.
\end{aligned}
\]

Therefore

\[
 \boxed{
 |\mathcal D_4v_q^{\rm out}(E_X)|
 <\frac{171}{4q\sqrt K}.
 }
\tag{L-91723.8}
\]

## 5. Add the positive B-spline collar

The frozen all-column collar theorem gives

\[
 \boxed{
 |\mathcal D_4v_q(C_X)|
 <\frac{200}{q\sqrt K}
 \qquad(q\ge2).
 }
\tag{L-91723.9}
\]

Combining (L-91723.8) and (L-91723.9),

\[
 \boxed{
 |\mathcal D_4v_q(C_X-E_X^{\rm out})|
 <\frac{971}{4q\sqrt K}.
 }
\tag{L-91723.10}
\]

For every nonterminal column `2<=q<=X/4`,

\[
 \Omega_X(q)=\frac{\log4}{\sqrt q}
 >\frac4{3\sqrt q}.
\]

Consequently,

\[
 \frac{|\mathcal D_4v_q(C_X-E_X^{\rm out})|}
      {\Omega_X(q)}
 <\frac{2913}{16\sqrt{qK}}
 \le\frac{2913}{16\sqrt{2K}}.
\tag{L-91723.11}
\]

The exact integer-square comparison

\[
 2913^2=8485569
 <8520192=2(16\cdot129)^2
\]

proves

\[
 \boxed{
 \frac{|\mathcal D_4v_q(C_X-E_X^{\rm out})|}
      {\Omega_X(q)}
 <\frac{129}{\sqrt K}
 \qquad(2\le q\le X/4).
 }
\tag{L-91723.12}
\]

This includes every physical column below `K`.

## 6. One stronger positive source thinning

Replace the factor `K/(K+178)` by

\[
 \boxed{
 \tau_K=\frac{\sqrt K}{\sqrt K+130}.
 }
\tag{L-91723.13}
\]

Apply `tau_K` once to the complete labelled positive parent measure before the
single global quantizer. Since the ideal common-parent packet uses at most the
native detail target, (L-91723.12) gives

\[
\begin{aligned}
 \Xi_{\rm realized}(q)
 &<
 \tau_K\left(1+\frac{129}{\sqrt K}\right)\Omega_X(q)\\
 &=
 \frac{\sqrt K+129}{\sqrt K+130}\Omega_X(q).
\end{aligned}
\]

Therefore every nonterminal physical column has the explicit strict reserve

\[
 \boxed{
 s_X(q)>
 \frac1{\sqrt K+130}\Omega_X(q)>0
 \qquad(2\le q\le X/4).
 }
\tag{L-91723.14}
\]

The positive radix-four inverse gives ordinary feasibility from the same
one-use detail slack.

## 7. The terminal proof is only improved

For `K>=2`,

\[
 \tau_K\le\frac K{K+178}.
\tag{L-91723.15}
\]

Indeed, after cancelling positive factors this is equivalent to

\[
 178\sqrt K\le130K,
\]

whose square follows from

\[
 178^2\le2\cdot130^2.
\]

Thus the new scaling retains no more endpoint mass than the scaling used in the
PR #473 terminal proof. The existing top-omission margin

\[
 5033X^{-3/2}-4452X^{-3/2}
 =581X^{-3/2}
\]

is therefore preserved or increased. Columns above the retained endpoint
support still have exactly zero response.

## 8. Bounded score cost

The unthinned root-Hall packet is score-superordinate to the equality score
`4sqrt(X)`. Hence scaling it by `tau_K` creates equality-score loss at most

\[
\begin{aligned}
 4\sqrt X(1-\tau_K)
 &=
 4\sqrt X\frac{130}{\sqrt K+130}\\
 &<
 520\sqrt{\frac XK}.
\end{aligned}
\tag{L-91723.16}
\]

Since `K>X/67`,

\[
 \sqrt{\frac XK}<\sqrt{67}<\frac{33}{4}.
\]

Therefore

\[
 \boxed{
 4\sqrt X(1-\tau_K)<4290.
 }
\tag{L-91723.17}
\]

The all-column repair has one absolute score cost. It does not consume a
`log^2 X` term.

## 9. Provenance and recursive mass

The thinning is one scalar applied once to the already labelled common parent
measure. The removed fraction is unused positive source. It is not a signed
correction and is not assigned to a child.

Scaling the exact current/child identity by one common positive scalar
preserves:

```text
one source owner per atom;
one common port;
one finite correction packet;
the same causal coefficient list;
sum_b alpha_b < 1/8.
```

No child receives a second collar, mismatch, omission, taper or port.

## 10. Consequence on the frozen SONTR stack

On the frozen PR #473 root-Hall, first-owner, terminal-omission and common-port
inputs, equations (L-91723.14)--(L-91723.17) replace the range-restricted
finite-realization reserve by an explicit all-column reserve. The complete
native deficit remains

\[
 J_\Lambda(X)-\operatorname{Score}(d_X)
 \le4\log X+C
 =o(\log^2X)
\]

for a larger absolute constant `C`.

This is a repair of the finite-realization clause. It does not independently
reconstruct the full root-Hall, direct-integral mass normalization, common-port,
endpoint-dual or Mellin--Landau inputs.

## 11. Exact boundary

```text
adjacent mismatch ownership across q<K             EXACT
all-q ordinary mismatch O((q sqrt K)^-1)           EXACT
all-q detail mismatch <171/(4q sqrt K)             EXACT
collar+mismatch relative error <129/sqrt K          EXACT
one-use sqrt-K thinning and strict reserve          EXACT
terminal omission proof preserved                   EXACT
additional equality-score cost <4290                EXACT
full frozen SONTR dependency reconstruction         STILL REQUIRED
Riemann Hypothesis                                  UNPROVEN
```
