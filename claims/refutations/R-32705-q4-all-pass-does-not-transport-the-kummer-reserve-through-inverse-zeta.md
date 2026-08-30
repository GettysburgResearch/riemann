# R-32705 — The Q=4 all-pass state does not transport the Kummer reserve through the inverse-zeta source

Claim ID: `R-32705`  
Status: **EXACT SCOPE FIREWALL — PREVENTS A FALSE COMPOSITION OF THE NEW Q=4 THEOREMS**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-09  
Dependencies: PR #325 `L-32404/L-32406/L-32405`; corrected physical coordinate `R-32403/L-32708`  
Scope: distinguishes local Euler all-pass transport from inverse-zeta source convolution; no refutation of the Q=4 route itself

## 1. Three different fields

For the Q=4 Dirichlet system put

\[
 A_4(s)=\frac{\zeta(s)}{E_4(s)},
 \qquad
 B_4(s)=A_4(s)^{-1}=\frac{E_4(s)}{\zeta(s)},
\]

where

\[
 E_4(s)=\frac{1-4^{1-s}}{1-4^{-s}}.
\]

Let

\[
 L_4(s)=-\frac{A_4'}{A_4}(s)
\]

be the positive generalized-prime logarithmic derivative and retain the atomized carry multiplier `N_theta(s)`.

There are three distinct transforms:

1. the generalized-prime carry field
   \[
   \boxed{\mathcal P_4(s,\theta)=\zeta(s)L_4(s)N_\theta(s);}
   \tag{R-32705.1}
   \]
2. the RH-sensitive source-convolved Q=4 current
   \[
   \boxed{\mathcal V_4(s,\theta)=E_4(s)L_4(s)N_\theta(s);}
   \tag{R-32705.2}
   \]
3. the ordinary logarithmic-derivative pole current
   \[
   \boxed{\mathcal U(s,\theta)
   =-\frac{\zeta'}{\zeta}(s)N_\theta(s).}
   \tag{R-32705.3}
   \]

The balanced Selberg–Kummer reserve `R_4=P_4^2-S_4` of PR #325 belongs to the first field, not directly to the third.

## 2. Source convolution contains the full inverse-zeta factor

The exact ratio of the source-convolved current to the generalized-prime carry field is

\[
 \boxed{
 \frac{\mathcal V_4}{\mathcal P_4}
 =B_4(s)=\frac{E_4(s)}{\zeta(s)}.
 }
\tag{R-32705.4]

(The closing bracket in the tag is typographical only.)

Writing `s=1/2+z`, PR #325 `L-32406` normalizes

\[
 \phi_4(z)=\frac12E_4(1/2+z),
\]

so

\[
 \boxed{
 B_4(1/2+z)
 =\frac{2\phi_4(z)}{\zeta(1/2+z)}.
 }
\tag{R-32705.5}

On the critical boundary `|phi_4(it)|=1`, but `1/zeta(1/2+it)` is precisely the principal RH-bearing multiplier. Therefore multiplication by `B_4` is **not** a unitary all-pass operation on the generalized-prime carry field.

Any argument of the form

```text
large positive Kummer reserve
+ Q=4 all-pass unitarity
=> reserve transports unchanged to the RH-sensitive source
```

omits the factor `1/zeta` and is invalid.

## 3. What the all-pass identity actually transports

PR #325 derives

\[
 \boxed{
 \mathcal V_4
 =\phi_4\mathcal U
  +\phi_4'N_\theta.
 }
\tag{R-32705.6]

Thus the all-pass state transports the **ordinary reciprocal-zeta pole current** `U` to the Q=4 pole current `V`, up to one deterministic gauge.

This is the correct unitary statement. It says nothing by itself about the pole-blind generalized-prime Kummer field `P_4` or its macroscopic reserve.

In particular, the finite-block scattering identity

\[
 \sum\|u_k\|^2
 =\sum\|y_k\|^2+\|x_K\|^2
\]

is an energy identity for the `U -> phi_4 U` channel. It is not an identity

\[
 \text{Kummer reserve}\to\text{Q=4 source reserve}.
\]

## 4. Why corrected current-to-reserve absorption is still useful

`L-32708` proves in the correctly typed physical coordinate that

\[
 \frac{|Q_4^{\rm phys}(n,j)|^2}{R_4(n,j)}\to0
\]

uniformly on the quarter-balanced cone. This is a genuine source-specific transference theorem.

But it is an **inequality comparing the actual source-convolved current with a pole-blind positive reserve**. It does not state that the reserve is already available with the correct sign in the global RH energy budget.

To use that inequality in a proof one still needs the exact source-convolved reflected accounting which places `R_4` as dissipative slack before or during the inverse-zeta convolution. That is precisely the open step identified on PR #325.

## 5. Bare source carry image is also pole-blind

`L-32709` proves

\[
 B_4(s)\zeta(s)N_\theta(s)=E_4(s)N_\theta(s),
\]

so after a pure carry window the **bare** inverse-source leg becomes deterministic and polylogarithmic.

This is correct but it cannot replace the RH-sensitive physical boundary before carry cancellation: multiplying by the carry factor `zeta(s)` has intentionally removed every nontrivial-zeta pole.

Thus `L-32709` is a useful boundary-factor estimate only inside a source-convolved identity whose other leg retains the pole. It is not a stand-alone principal-boundary estimate.

## 6. Exact remaining bridge

The valid Q=4 architecture is therefore

```text
ordinary reciprocal-zeta pole current U
   -- exact all-pass + gauge -->
Q=4 pole current V
   -- source-specific inequality -->
balanced Selberg-Kummer reserve R_4
```

plus one **separate** theorem proving that the complete reflected/source-convolved Selberg identity makes that reserve available without double spending and leaves only the unitary terminal state at lower logarithmic scale.

The missing theorem cannot be replaced by:

- all-pass unitarity alone;
- pointwise `V^2 <= delta R_4` alone;
- the deterministic carry image of the bare source alone;
- the macroscopic positivity of `R_4` alone.

## 7. Disposition

```text
Q=4 all-pass state                         RETAINED EXACT
Q=4 balanced Kummer reserve                RETAINED EXACT
correct physical current/reserve ratio     RETAINED
bare source carry field polylog            RETAINED AT POLE-BLIND SCOPE
all-pass transports Kummer reserve         FALSE
reflected reserve accounting               OPEN / RH-BEARING
RH                                         UNPROVED
```
