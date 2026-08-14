# Full direct-row closure attack

## Executive result

The old standalone packet was not a full proof proposal: it deliberately left
`GRRT` and `CFFP` open. The present pass found and completed a third architecture,
the direct native-row route.

The decisive replacement is:

\[
 c_X=R_{\rm pre}+R_s(c_s)+R_h(c_h)+B_s+B_h\ge0,
\]

where `c_X` is the exact native equality row and

\[
 \Gamma(c_X)=w_X,
 \qquad
 \Xi(c_X)=\Omega_X.
\]

After restricting the positive residual sources to the common endpoint `X/67`,
let `R_ch` be their canonical child row and insert an arbitrary child packing
`d_ch` at the same row indices. Then

\[
 d_X=c_X-R_{ch}+d_{ch}\ge0,
\]

and, after the whole current row is summed,

\[
 \Gamma(d_X)=w_X-\Gamma(R_{ch})+\Gamma(d_{ch})\le w_X,
\]

\[
 \Xi(d_X)=\Omega_X-\Xi(R_{ch})+\Xi(d_{ch})\le\Omega_X.
\]

This is the componentwise native-root certificate requested by the reviews of
PRs #443 and #450. It does not define a complement and infer feasibility; it
constructs a positive row and displays the residual inequalities.

## New score theorem

The previous direct-row packet contained only an index for its fixed-67 score
inequality. The present pass proves the complete theorem

\[
 E(Y)-E(Y/67)
 \ge5(\sqrt Y-\sqrt{Y/67}),
 \qquad Y\ge67.
\]

The proof contains:

```text
base: F(67)>3.2764007195549669;
finite derivative corridor: 402 cells, minimum >22.1747542920858;
analytic tail start: Y=469, base >131.798262054325;
monotone analytic derivative thereafter.
```

Thus every nonterminal current component-row difference pays the complete
row-budgeted native score difference with coefficient one.

## One-use ownership

Root-only objects are current and used once:

```text
outer equality producer;
one global B-spline quantization;
width-three collar;
finite/continuum mismatch;
interior safety factor;
fixed top omission and terminal packet;
corrected P61/67 common port;
Hall target-null row bonuses.
```

The recursive child owns only its canonical child capacities. It receives no
small-prime block, collar, mismatch, omission, or root port.

## Recurrence and conclusion

The complete proposed recurrence is

\[
 \mathfrak L_X
 \le\mathfrak L_{X/67+C_0}+C_{reset}.
\]

Hence

\[
 \mathfrak L_X=O(\log X)=o(\log^2X).
\]

Ordinary feasibility gives

\[
 F_\Lambda(X)\le\mathfrak L_X.
\]

The prime-square asymptotic then forces eventual negativity of the prime-only
endpoint, and the Mellin–Landau theorem yields RH.

## Exact status

```text
all named mathematical arrows in the direct-row architecture  supplied
new fixed-67 theorem                                         proved
algebra replay                                                passed
expensive frozen Hall/outer/port inputs                       not rerun here
full theorem                                                  complete proposal
RH                                                            pending review
```

The phrase “complete proposal” means there is no longer a theorem symbol such as
`GRRT` or `CFFP` left as an antecedent. It does not mean the imported finite
certificates have already received independent acceptance. A reviewer should
start from `standalone/2026-08-14-full-direct-row-closure/README.md` and follow
the reconstruction order there.
