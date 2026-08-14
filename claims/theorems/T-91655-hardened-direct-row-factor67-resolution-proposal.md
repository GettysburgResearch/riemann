# T-91655 — Hardened one-use equality/direct-row factor-\(67\) resolution proposal

Claim ID: `T-91655`  
Status: **COMPLETE RH PROOF PROPOSAL — INDEPENDENT FROZEN-COMMIT RECONSTRUCTION REQUIRED**  
Created: 2026-08-14  
Normative review target: this theorem together with `L-91668`, corrected
`L-91669`, `R-91658`, the dependency manifest, and the final lock  
Supersedes as conclusion target: `T-91652`, `T-91653`, `T-91654`, and the first
hardening draft of this file  
Riemann Hypothesis status: **not accepted before independent reconstruction**

## 1. Exact theorem statement

For every sufficiently large real \(X\), the frozen construction produces a
finite nonnegative average-binomial row \(d_X=(d_X(j))_{j\ge2}\) such that, for
every physical integer column \(q\ge2\),

\[
 \boxed{
 \Gamma(d_X;q)\le
 w_X(q)=q^{-1/2}\log(X/q)\mathbf1_{q\le X},
 }
 \tag{T-91655.1}
\]

\[
 \boxed{
 \Xi(d_X;q)\le
 \Omega_X(q)=w_X(q)-2w_X(4q),
 }
 \tag{T-91655.2}
\]

and

\[
 \boxed{
 \mathcal S_X(d_X)
 \ge4\sqrt X-C_1\log X-C_2
 }
 \tag{T-91655.3}
\]

for effective absolute constants \(C_1,C_2\).  Consequently the native loss is
\(O(\log X)=o(\log^2X)\), and the frozen endpoint chain gives the proposed
conclusion

\[
 \boxed{\mathrm{RH}.}
 \tag{T-91655.4}
\]

No named open theorem is an antecedent.  Every mathematical input is frozen by
path and Git blob SHA, and the exact statement consumed is recorded in the
dependency manifest.

## 2. Equality score front door without a global sign assumption

`L-26204/L-91557` give the exact continuum equality datum with physical score

\[
 \boxed{J_{\rm eq}(X)=4\sqrt X.}
 \tag{T-91655.5}
\]

The reciprocal-zeta equality weight \(L_*\) is signed globally.  This proposal
does not assume otherwise.  `L-91107` proves only the finite-window positivity

\[
 \boxed{
 L_*(u)>0.3186
 \quad
 0\le u\le\log(c_0^{-1}),
 \qquad
 c_0=0.01844367547104\ldots .
 }
 \tag{T-91655.6}
\]

At each scale \(X\), this supplies one positive outer equality window beginning
at \(K=\lceil c_0X\rceil\).  The inner state is passed to a new contracted
generation; \(L_*\) is not extended beyond the certified window.

`L-91110/L-91111/L-91114/L-91115` construct one nonnegative endpoint-frame
realization, one quantization, one collar/mismatch safety factor, and one fixed
top omission.  `L-91320` supplies the corrected one-use `P_61/67` boundary
reserve where needed.  Their complete one-generation score charge is bounded
by an effective absolute constant, and none is copied to a child.

## 3. Exact native row and labelled source entry

For real \(Y\ge1\), define the positive component row \(Q_Y\) as in
`L-91559`, and set

\[
 c_X(j)=
 \sum_{n\le X}\frac{\mu(n)}{\sqrt n}Q_{X/n}(j).
 \tag{T-91655.7}
\]

Möbius convolution gives exactly

\[
 \boxed{
 \Gamma(c_X;q)=w_X(q),
 \qquad
 \Xi(c_X;q)=\Omega_X(q).
 }
 \tag{T-91655.8}
\]

`L-91330` gives an atomwise positive two-channel representation and `L-91333`
gives the nonduplicating least-prime source tree.  `L-91668` explicitly
discharges the source-identity antecedent in `L-91621`, proves unique ownership
of every active squarefree source, and identifies the observed root row with
(T-91655.7).

Apply the exact native cocycle and the frozen no-upward Hall transport separately
on each stopped leaf.  The complete parent row is

\[
 R_{\rm parent}
 =R_{\rm pre}+R_s(c_s)+R_h(c_h)+B_s+B_h,
 \tag{T-91655.9}
\]

with every term nonnegative, exact target use, and score superordination.  Hall
is never commuted through the rough tree.

## 4. One-use current realization

The endpoint-frame equality producer and the arithmetic row in Section 3 are
two representations/stages of the same normalized root equality datum.  They
are not added as independent capacity copies.

At one generation, the following are current-owned and used once:

```text
positive outer equality window;
one global endpoint quantization;
width-three collar;
finite/continuum mismatch and one safety factor;
fixed top omission and terminal annulus;
corrected boundary port, if invoked;
Hall target-null row bonuses.
```

All current terms are summed before the recursive child is inserted.  The
normalization bridge and score comparison are the frozen theorem `L-91557`; the
explicit arithmetic ownership is `L-91668`.  A discrepancy between those two
root data is an immediate falsifier.

## 5. Exact same-index child replacement

Restrict both positive Hall residual sources to their canonical fixed-\(67\)
child and let \(R_{\rm ch}\) be its complete canonical row.  For an arbitrary
feasible child row \(d_{\rm ch}\), define after the complete current sum

\[
 \boxed{
 d_X=R_{\rm parent}-R_{\rm ch}+d_{\rm ch}.
 }
 \tag{T-91655.10}
\]

`L-91559/L-91663` prove

\[
 d_X\ge0,
 \tag{T-91655.11}
\]

\[
 \boxed{
 \Gamma(d_X;q)
 =\Gamma(R_{\rm parent};q)-\Gamma(R_{\rm ch};q)
 +\Gamma(d_{\rm ch};q)
 \le\Gamma(R_{\rm parent};q),
 }
 \tag{T-91655.12}
\]

\[
 \boxed{
 \Xi(d_X;q)
 =\Xi(R_{\rm parent};q)-\Xi(R_{\rm ch};q)
 +\Xi(d_{\rm ch};q)
 \le\Xi(R_{\rm parent};q).
 }
 \tag{T-91655.13}
\]

The child remains at the same literal row indices.  There is no affine lift,
fractional column, duplicated small-prime block, scalar child surrogate, source
fraction multiplying an unrelated signed loss, or formal residual complement.

## 6. Exhaustive physical capacity proof

The parent capacity is verified by the exhaustive partition

```text
q<K:          exact inherited bulk reproduction and native child identity;
K<=q<=X/4:   L-91114 mismatch-plus-collar safety inequality;
X/4<q<X:     L-91115 fixed top-omission inequality;
q>=X:        triangular zero.
```

The four ranges establish the complete current parent response.  Equations
(T-91655.12)--(T-91655.13) replace the canonical child without increasing it.
Therefore

\[
 \boxed{
 \Gamma(d_X;q)\le w_X(q),
 \qquad
 \Xi(d_X;q)\le\Omega_X(q)
 \quad(q\ge2).
 }
 \tag{T-91655.14}
\]

This is one simultaneous inequality for the fully summed physical row, not an
inference from a table of separately feasible objects.

## 7. Score ledger

For a nonterminal quotient \(Z\ge67\), `L-91666` proves globally

\[
 \boxed{
 E(Z)-E(Z/67)
 \ge5(\sqrt Z-\sqrt{Z/67}).
 }
 \tag{T-91655.15}
\]

The same coefficients \(1-p^{-1}\) and \(p^{-1}\) occur in the literal row and
row-budgeted score.  Hence every nonterminal current component-row difference
pays the complete inherited score difference with coefficient one.

At a terminal quotient,

\[
 [J_{\rm term}-\mathcal S_{\rm term}]_+
 \le2M_{\rm term},
 \tag{T-91655.16}
\]

and `L-91554` gives the independent fixed-Euler sourcewise bound.  Source
disjointness means terminal target is spent once over all leaves.  Thus there is
no hidden leaf-count factor.

The one-use analytic/discrete current debt is bounded by an effective absolute
constant per generation.  There are at most

\[
 1+\left\lceil\frac{\log X}{\log67}\right\rceil
 \tag{T-91655.17}
\]

generations.  Combining the exact root equality score, nonterminal coefficient
one transfer, terminal target telescope, and current debt yields

\[
 \boxed{
 \mathcal S_X(d_X)
 \ge4\sqrt X-C_1\log X-C_2.
 }
 \tag{T-91655.18}
\]

No claim of an absolute all-depth score loss is used.

## 8. Native loss and finite dual

`L-91557` proves

\[
 J_\Lambda(X)<4\sqrt X+4\log X.
 \tag{T-91655.19}
\]

Hence

\[
 \mathfrak L_X(d_X)
 :=J_\Lambda(X)-\mathcal S_X(d_X)
 =O(\log X)=o(\log^2X).
 \tag{T-91655.20}
\]

The finite average-binomial/von-Mangoldt identity and ordinary feasibility give

\[
 \boxed{
 F_\Lambda(X)
 \le\mathfrak L_X(d_X)
 =o(\log^2X).
 }
 \tag{T-91655.21}
\]

No asymptotic interchange occurs in this finite dual step.

## 9. Prime-square drift and Landau

The frozen prime-power separation theorem gives

\[
 F_\Lambda(X)-A(X)
 =
 \frac{-1-\zeta(1/2)}4\log^2X
 +o(\log^2X),
 \tag{T-91655.22}
\]

with positive coefficient.  Equation (T-91655.21) forces eventual negativity
of \(A(X)\).

The frozen prime-endpoint Mellin theorem supplies a genuine uncancelled
singularity at \(z=\rho-1/2\) for every nontrivial zero \(\rho\).  Eventual
one-sign, Landau's theorem, and the functional equation exclude every zero off
the critical line, giving (T-91655.4).

## 10. Dependency closure and mandatory review order

The controlling manifest is

```text
integration/2026-08-14/t91655-dependency-manifest.json
```

Review in this order:

1. `R-91658`: verify that only finite-window, not global, positivity of `L_*`
   is used.
2. `L-91107/L-91110/L-91114/L-91115`: reconstruct the endpoint-frame current
   realization and all four physical column ranges.
3. `L-91668`: reconstruct labelled arithmetic ownership and equality with the
   exact native row.
4. `L-91550/L-91560/L-91562/L-91621`: rerun Hall, native cocycle, and leafwise
   Fubini.
5. `L-91559/L-91663`: check same-index arbitrary-child replacement.
6. `L-91666`: rerun the global fixed-\(67\) score theorem.
7. Corrected `L-91669`: audit the one-use current/recursive ledger and terminal
   mass firewall.
8. `L-91557` and the external endpoint chain: verify the score front door,
   benchmark, finite dual, prime-square coefficient, Mellin pole, and Landau
   sign.

## 11. Exact falsifiers

Reject the proposal immediately if any of the following occurs:

```text
global positivity of L_* is assumed;
L_* is used outside the certified first 54.2 quotient cells;
the continuum equality datum and finite c_X datum have different normalization;
one current endpoint packet is quantized twice or copied to a child;
one arithmetic source has two owners;
Hall is commuted through the rough tree;
the endpoint/current realization and c_X are charged as independent copies;
the complete current row is not summed before child subtraction;
one physical column range is omitted or overdrawn;
C_cur depends on X or on the number of leaves;
terminal debt is charged per leaf or per depth;
L-91666 fails;
a child changes literal row indices;
the finite dual, prime-square coefficient, Mellin pole, or Landau sign reverses.
```

## 12. Status boundary

```text
finite-window equality-weight positivity             frozen / exact
one-use endpoint/current realization                 frozen / reconstruct
labelled arithmetic source entry                      explicit / L-91668
leafwise Hall and same-index replacement              exact on frozen inputs
nonterminal score transfer                            exact / L-91666
all-depth score debt                                  O(log X)
finite dual and endpoint chain                        frozen / reconstruct
full theorem                                          complete proposal
Riemann Hypothesis                                    not accepted before review
```
