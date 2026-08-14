# T-91655 — Hardened direct native-row factor-\(67\) resolution proposal

Claim ID: `T-91655`  
Status: **COMPLETE RH PROOF PROPOSAL — INDEPENDENT FROZEN-COMMIT RECONSTRUCTION REQUIRED**  
Created: 2026-08-14  
Normative review target: this theorem together with `L-91668`, `L-91669`, and
the two dependency locks  
Supersedes as conclusion target: `T-91652`, `T-91653`, `T-91654`, and
`L-91667`  
Riemann Hypothesis status: **not accepted before independent reconstruction**

## 1. Exact theorem statement

For every sufficiently large real \(X\), there exists a finite nonnegative
average-binomial row \(d_X=(d_X(j))_{j\ge2}\) such that, for every physical
integer column \(q\ge2\),

\[
 \boxed{
 \Gamma(d_X;q)\le
 w_X(q)
 =
 q^{-1/2}\log(X/q)\mathbf 1_{q\le X},
 }
 \tag{T-91655.1}
\]

\[
 \boxed{
 \Xi(d_X;q)
 \le
 \Omega_X(q)
 =
 w_X(q)-2w_X(4q),
 }
 \tag{T-91655.2}
\]

and

\[
 \boxed{
 \mathcal S_X(d_X)
 \ge4\sqrt X-2\log X.
 }
 \tag{T-91655.3}
\]

Consequently,

\[
 \boxed{\mathrm{RH}.}
 \tag{T-91655.4}
\]

The remainder of this file gives the complete dependency chain and identifies
the exact statement consumed at every arrow.

## 2. Native physical row

For real \(Y\ge1\), define the positive component row

\[
 Q_Y(j)
 =
 (j+1)\Delta^2
 \left[
 \frac{S_Y(j)}{j-1}
 \right],
 \qquad
 S_Y(j)=
 \sum_{m\ge j}
 \frac{\log(Y/m)}{\sqrt m}\mathbf1_{m\le Y}.
 \tag{T-91655.5}
\]

The exact component response identities are

\[
 \Gamma(Q_Y;q)
 =
 q^{-1/2}H(Y/q),
 \tag{T-91655.6}
\]

\[
 \Xi(Q_Y;q)
 =
 q^{-1/2}
 \left[
 H(Y/q)-H(Y/(4q))
 \right],
 \tag{T-91655.7}
\]

where

\[
 H(Z)=\sum_{m\le Z}m^{-1/2}\log(Z/m).
\]

Define the native Möbius row

\[
 \boxed{
 c_X(j)=
 \sum_{n\le X}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j).
 }
 \tag{T-91655.8}
\]

Writing \(r=nm\) and using

\[
 \sum_{n\mid r}\mu(n)=\mathbf1_{r=1},
\]

gives exactly

\[
 \boxed{
 \Gamma(c_X;q)=w_X(q),
 \qquad
 \Xi(c_X;q)=\Omega_X(q).
 }
 \tag{T-91655.9}
\]

This is one common physical row.  The proof never defines a coordinatewise
formal complement of heterogeneous packets.

## 3. Positive realization of the exact native row

`L-91330` splits every native SHARP source atom into two separately labelled
positive paired channels.  `L-91333` gives each channel an exact
nonduplicating least-prime source tree.

`L-91668` applies the explicit finite stopping rule to this tree and proves the
labelled source identity required by `L-91621`.  The signed row observation of
the root tree is exactly (T-91655.8).  Applying the controlled one-prime cocycle
and the no-upward Hall producer separately on each stopped leaf gives

\[
 \boxed{
 c_X
 =
 R_{\rm cur}
 +R_s(c_s)+R_h(c_h)+B_s+B_h,
 }
 \tag{T-91655.10}
\]

with every term on the right coefficientwise nonnegative.  Moreover,

\[
 T(c_s)+T(c_h)=T_{\rm parent},
 \tag{T-91655.11}
\]

and the row-budgeted score of \(c_s,c_h\) is at least the signed parent score.
Therefore

\[
 \boxed{c_X\ge0.}
 \tag{T-91655.12}
\]

There is no nonlinear Hall/tree commutation: the source tree is partitioned
first, Hall is chosen leafwise, and only positive outputs are summed.

## 4. Exact same-index recursion

For a positive typed packet \(P=(\tau,\nu,Y)\), restrict

\[
 \nu^{\rm ch}=\nu|_{\{n\le Y/67\}}
\]

and evaluate it at endpoint \(Y/67\), retaining the same type.  Let
\(R_Y(P)\) and \(R_{Y/67}(P^{\rm ch})\) be the canonical parent and child rows
at the same literal row indices.  Endpoint monotonicity gives

\[
 R_Y(P)-R_{Y/67}(P^{\rm ch})\ge0.
 \tag{T-91655.13}
\]

For any feasible child row \(d_{\rm ch}\), set

\[
 d_Y(P)
 =
 R_Y(P)-R_{Y/67}(P^{\rm ch})+d_{\rm ch}.
 \tag{T-91655.14}
\]

The exact response identities in `L-91559/L-91663` give simultaneously

\[
 \Gamma(d_Y(P);q)\le\Gamma(R_Y(P);q),
 \tag{T-91655.15}
\]

\[
 \Xi(d_Y(P);q)\le\Xi(R_Y(P);q).
 \tag{T-91655.16}
\]

Starting from the finite terminal layer and applying (T-91655.14) upward
constructs a finite nonnegative root row \(d_X\).  At the root,
(T-91655.9) turns (T-91655.15)--(T-91655.16) into
(T-91655.1)--(T-91655.2).

No step uses:

```text
an affine Pascal lift;
a fractional physical column;
a duplicated P_61 block;
a scalar child standing in for a row;
or an inferred residual complement.
```

## 5. Exact root target and score

Put \(t=\log X\).  The equality-density transform `L-26204` satisfies

\[
 (L_*\ast\varrho)(t)=t
 \tag{T-91655.17}
\]

and

\[
 2\int_0^\infty e^{-u/2}L_*(u)\,du=4.
 \tag{T-91655.18}
\]

In the native normalization shared by `L-91556`, `L-91621`, and `L-91622`,
the root equality packet therefore has

\[
 \boxed{
 M_X(P_X^{\rm eq})=\log X,
 \qquad
 J_X(P_X^{\rm eq})=4\sqrt X.
 }
 \tag{T-91655.19}
\]

Target Hall is exact and score-superordinate, so the positive typed packets in
(T-91655.10) retain target \(\log X\) and declared score at least
\(4\sqrt X\).

## 6. The global terminal-mass telescope

At each fixed-\(67\) source restriction, positivity gives

\[
 M_r=M_{r+1}+M_r^{\rm term},
 \qquad
 M_r^{\rm term}\ge0.
 \tag{T-91655.20}
\]

Every source atom belongs to exactly one terminal layer.  Summing
(T-91655.20) over the finite tree yields

\[
 \boxed{
 \sum_{r\ge0}M_r^{\rm term}
 =
 M_0
 =
 \log X.
 }
 \tag{T-91655.21}
\]

This is the decisive global accounting identity.  It rules out both a hidden
leaf-count factor and a hidden depth factor.

For every terminal quotient \(1\le Z<67\), the uniform physical corridor gives

\[
 [J_{\rm term}(Z)-\mathcal S_{\rm term}(Z)]_+
 \le2M_{\rm term}(Z).
 \tag{T-91655.22}
\]

Consequently the complete all-depth terminal deficit is at most

\[
 \boxed{
 2\sum_{r\ge0}M_r^{\rm term}
 =
 2\log X.
 }
 \tag{T-91655.23}
\]

## 7. Nonterminal score transfer

For

\[
 E(Z)=
 \sum_{2\le m\le Z}
 \frac{\log m}{\sqrt m}\log(Z/m),
\]

`L-91666` proves, for every real \(Z\ge67\),

\[
 \boxed{
 E(Z)-E(Z/67)
 \ge
 5\left(\sqrt Z-\sqrt{Z/67}\right).
 }
 \tag{T-91655.24}
\]

This is exactly the row-budgeted declared-score difference, with the same
branch coefficients as the literal row.  Every nonterminal edge therefore has
zero positive score debt.  Hall bonuses have nonnegative literal score.

Combining the exact root score \(4\sqrt X\), zero nonterminal debt, and
(T-91655.23) proves

\[
 \boxed{
 \mathcal S_X(d_X)
 \ge4\sqrt X-2\log X,
 }
\]

which is (T-91655.3).

## 8. No hidden outer assembly

The physical row used in this theorem is only the row constructed through
(T-91655.14).  Historical objects from the older factor-\(54\) architecture,

```text
outer equality B-splines;
quantization collar;
finite/continuum mismatch row;
top omission;
common endpoint port;
```

are not row summands and consume no capacity in `T-91655`.

`L-26204` is used only to identify the exact root target and declared score in
(T-91655.19).  It does not supply a second finite row.  The direct component
rows, Hall bonuses, current differences, and recursive child are the complete
physical ownership ledger.

## 9. Native loss

The elementary parabolic benchmark bound in `L-91557` is

\[
 \boxed{
 J_\Lambda(X)<4\sqrt X+4\log X.
 }
 \tag{T-91655.25}
\]

Define

\[
 \mathfrak L_X(d_X)
 =
 J_\Lambda(X)-\mathcal S_X(d_X).
\]

Equations (T-91655.3) and (T-91655.25) give the explicit bound

\[
 \boxed{
 \mathfrak L_X(d_X)<6\log X.
 }
 \tag{T-91655.26}
\]

In particular,

\[
 \mathfrak L_X(d_X)=o(\log^2X).
 \tag{T-91655.27}
\]

## 10. Finite dual

The average-binomial score identity is

\[
 G_j=\sum_{q=p^a}\Lambda(q)\beta_{jq}.
 \tag{T-91655.28}
\]

Since \(d_X\ge0\) and is ordinarily feasible,

\[
 \begin{aligned}
 \mathcal S_X(d_X)
 &=
 \sum_jd_X(j)G_j\\
 &=
 \sum_{q=p^a}\Lambda(q)
 \sum_jd_X(j)\beta_{jq}\\
 &\le
 \sum_{q=p^a}\Lambda(q)w_X(q).
 \end{aligned}
 \tag{T-91655.29}
\]

Thus the complete prime-power parabolic gap satisfies

\[
 \boxed{
 F_\Lambda(X)\le\mathfrak L_X(d_X)<6\log X.
 }
 \tag{T-91655.30}
\]

No asymptotic or interchange is used in this finite step.

## 11. Prime-only endpoint

The frozen prime-power separation theorem gives

\[
 \boxed{
 F_\Lambda(X)-A(X)
 =
 c_\square\log^2X+o(\log^2X),
 }
 \tag{T-91655.31}
\]

where

\[
 \boxed{
 c_\square=
 \frac{-1-\zeta(1/2)}4>0.
 }
 \tag{T-91655.32}
\]

Combining (T-91655.30)--(T-91655.32),

\[
 A(X)
 \le
 6\log X-c_\square\log^2X+o(\log^2X)<0
 \tag{T-91655.33}
\]

for every sufficiently large \(X\).

## 12. Mellin–Landau conclusion

The frozen prime-endpoint theorem identifies the Mellin transform of
\(A(e^t)\).  Every nontrivial zero \(\rho\) of \(\zeta\) contributes a genuine
uncancelled singularity at

\[
 z=\rho-\frac12.
 \tag{T-91655.34}
\]

Eventual negativity of \(A(e^t)\), Landau's theorem for one-sign Laplace
transforms, and the functional equation exclude every zero with
\(\Re\rho>1/2\), and hence every zero with \(\Re\rho<1/2\).  Therefore every
nontrivial zero lies on the critical line, proving the proposed conclusion
(T-91655.4).

## 13. Dependency closure

The exact dependency manifest is

```text
integration/2026-08-14/t91655-dependency-manifest.json
```

It records, for each load-bearing claim:

```text
claim ID;
path;
Git blob SHA;
the exact statement consumed;
status;
and the shortcut which would falsify its use.
```

The external transform and endpoint claims are frozen to both source commits
and blob SHAs.  The parent and final supplement locks must be read
conjunctively.

## 14. Exact falsifiers

Reject the proposal immediately if any of the following occurs:

```text
L-91333 does not supply the labelled source identity used by L-91621;
the observed labelled root row is not exactly c_X;
one source atom appears in two stopped or terminal labels;
a frozen Hall prefix or normalized-row cell fails;
Hall is commuted through the rough tree;
the target normalization in L-26204 and L-91556 differs;
the root target is not log X;
terminal masses do not telescope to at most log X;
terminal declared-minus-literal debt exceeds 2T;
L-91666 fails at one real Z>=67;
a child changes row indices;
one ordinary or detail column is overdrawn;
a historical outer/collar/port row is added to d_X;
the finite dual has the opposite inequality;
the prime-square coefficient or Landau sign is reversed.
```

## 15. Status boundary

```text
source-partition antecedent                         explicitly discharged
native row response                                 exact
positive native-row realization                     exact on frozen Hall inputs
same-index arbitrary-child assembly                 exact
root target                                         log X, explicit
root declared score                                 4 sqrt(X), explicit
all-depth terminal debt                             <=2 log X
final physical score                                >=4 sqrt(X)-2 log X
native loss                                         <6 log X
finite dual                                         exact
prime-square/Landau chain                           frozen / reconstruct
full theorem                                        complete proposal
Riemann Hypothesis                                  not accepted before review
```
