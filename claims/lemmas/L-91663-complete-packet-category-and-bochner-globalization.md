# L-91663 — Complete packet category, Bochner globalization, and typed root atoms

Claim ID: `L-91663`  
Status: **PROVED EXACT ABSTRACT TYPE / GLOBALIZATION THEOREM — NATIVE ROOT CAPACITY REMAINS SEPARATE**  
Created: 2026-08-14  
Depends on: finite linearity of the carry, radix-four, score, and boundary maps; `L-91658` for same-index normalization  
RH status: **unproved**

## 1. One packet category for local and global data

Fix an endpoint `X`. Let

\[
\mathscr V_X
=
\mathscr L_X
\oplus \mathbb R^4
\oplus \mathbb R^{\{j\ge2\}}
\oplus \mathbb R^{\{q\ge2\}}\oplus \mathbb R^{\{q\ge2\}}
\oplus \mathbb R^{\{q\ge2\}}\oplus \mathbb R^{\{q\ge2\}}
\oplus \mathbb R^{B_X},
\]

with finite support in every sequence coordinate. A **complete packet datum** is written

\[
\boxed{
P=(\ell;J,T,S,E;q,\Gamma,\Xi;w,\Omega;b).
}
\tag{L-91663.1}
\]

The coordinates mean:

- `ell`: a free provenance label;
- `J`: the benchmark used by the packet deficit;
- `T`: the scalar SHARP-target observation;
- `S`: the declared scalar score observation;
- `E`: the literal component-row score of the distinguished row;
- `q=(q_j)`: the distinguished component row;
- `Gamma=(Gamma_q)`: its ordinary carry response;
- `Xi=(Xi_q)`: its radix-four response;
- `w=(w_q)`: available ordinary capacity;
- `Omega=(Omega_q)`: available radix-four capacity;
- `b`: the direct sum of packet-owned boundary capacities.

The ordinary carry operator `C_X`, detail operator `D_4`, literal score
functional `H_X`, and boundary operator `B_X` are fixed linear maps. A datum is
**compatible** when

\[
\Gamma=C_Xq,\qquad
\Xi=\mathcal D_4\Gamma,\qquad
E=H_X(q).
\tag{L-91663.2}
\]

The scalar observations `T,S` are retained because the finite-window Hall
theorems use them. They are not substituted for vector capacities `w,Omega`.

This single type contains both formerly separate objects:

1. a normalized local packet `P_u`, for which `T,S` are the local kernels and
   `w,Omega` are its complete local response capacities;
2. the native root packet `N_X`, for which `J=J_Lambda(X)`,
   `w=w_X`, and `Omega=D_4 w_X`.

Thus the local and global objects live in one vector space. No coordinate
changes meaning between the two uses.

## 2. Feasible rows and deficit

For a compatible datum `P`, define

\[
\mathcal F_X(P)=
\left\{
d\ge0:
C_Xd\le w,\quad
\mathcal D_4C_Xd\le\Omega,\quad
B_Xd\le b
\right\}.
\tag{L-91663.3}
\]

All inequalities are coordinatewise. The distinguished row `q` is data, not an
implicit extra capacity inequality. It may be used as a proposed feasible
witness only after (L-91663.3) is checked.

The packet deficit is

\[
\boxed{
\Delta_X(P)
=
J-\sup_{d\in\mathcal F_X(P)}H_X(d).
}
\tag{L-91663.4}
\]

The positive part is used when an envelope is formed. Because the defining
maps are linear,

\[
\Delta_X(cP)=c\Delta_X(P)\qquad(c\ge0)
\tag{L-91663.5}
\]

and, whenever `P,Q` have source-disjoint capacity coordinates,

\[
\Delta_X(P+Q)\le\Delta_X(P)+\Delta_X(Q).
\tag{L-91663.6}
\]

Indeed, sums of feasible witnesses are feasible for the sum datum, and scores
add.

## 3. Normalized and arithmetic child embeddings

Let `Y=X/m`. The normalized same-index embedding

\[
U_m:\mathscr V_Y\longrightarrow\mathscr V_X
\]

changes endpoint and provenance labels but leaves every numerical coordinate
unchanged. Arithmetic placement of one unit multiplicative child is

\[
m^{-1/2}U_mP_Y.
\tag{L-91663.7}
\]

An actual child whose coefficient in the parent is already `c` is

\[
cU_mP_Y.
\tag{L-91663.8}
\]

Consequently

\[
\Delta_X(U_mP_Y)=\Delta_Y(P_Y),\qquad
\Delta_X(cU_mP_Y)=c\Delta_Y(P_Y).
\tag{L-91663.9}
\]

This is the normalization convention of `L-91658`. It eliminates the possible
extra factor `m^{-1/2}` in the recursive coefficient.

## 4. Bochner sums of packet data

Let `(A,mu)` be a finite measure space and let `a -> P_a` be a measurable
family of complete packet data whose numerical coordinates are absolutely
integrable. Define

\[
\boxed{
\int_A P_a\,d\mu(a)
}
\tag{L-91663.10}
\]

coordinatewise. Provenance labels are retained as the labelled direct integral.

If `d_a in F_X(P_a)` is a measurable family with integrable row coefficients,
then Tonelli's theorem and positivity of every capacity map give

\[
\boxed{
\int_A d_a\,d\mu(a)
\in
\mathcal F_X\left(\int_A P_a\,d\mu(a)\right).
}
\tag{L-91663.11}
\]

Moreover,

\[
H_X\left(\int_A d_a\,d\mu(a)\right)
=
\int_A H_X(d_a)\,d\mu(a).
\tag{L-91663.12}
\]

For a finite simple family, (L-91663.6) and homogeneity yield

\[
\Delta_X\left(\int_A P_a\,d\mu(a)\right)
\le
\int_A\Delta_X(P_a)\,d\mu(a).
\tag{L-91663.13}
\]

General nonnegative families follow by monotone simple approximation. For
signed benchmark coordinates, apply the same argument to the positive
capacity coordinates while integrating the benchmark exactly. Therefore

\[
\boxed{
\left[
\Delta_X\left(\int_A P_a\,d\mu(a)\right)
\right]_+
\le
\int_A[\Delta_X(P_a)]_+\,d\mu(a).
}
\tag{L-91663.14}
\]

This is the missing local-to-global packet theorem at the abstract level.

## 5. Explicit root-fiber labels

Let

\[
K=\lceil c_0X\rceil,\qquad
I_X=[K+2,X-W-2],
\qquad W=10000,
\]

and put `x=X/s`. On `I_X`, every active quotient lies in the fixed window

\[
1\le x<c_0^{-1}<55.
\tag{L-91663.15}
\]

Use the finite positive measure

\[
d\tau_X(s)=\frac{2\,ds}{s}.
\tag{L-91663.16}
\]

For every active residual Hall node `e`, define the normalized free atom

\[
\boxed{
\widehat A_{X;s,e}^{(67)}
=
\bigl(s,e,67;\mathsf A_{x,e}\bigr),
\qquad x=X/s,
}
\tag{L-91663.17}
\]

where the complete numerical local datum is

\[
\mathsf A_{x,e}
=
\left(
J_{x,e},
W_\Psi(x,e),
W_S(x,e),
H(Q_{x/e}),
e^{-1/2}Q_{x/e},
C(e^{-1/2}Q_{x/e}),
\mathcal D_4C(e^{-1/2}Q_{x/e}),
w_{x,e},
\Omega_{x,e},
b_{x,e}
\right).
\tag{L-91663.18}
\]

The superscript `(67)` means that future least-prime provenance starts at 67;
the finite small-prime block is not reintroduced. Equation (L-91663.18)
specifies the row, score, ordinary response, detail response, and boundary
coordinates. Thus the symbol in (L-91663.17) no longer has any of the three
ambiguous meanings

\[
P_{X/e},\qquad
e^{-1/2}U_eP_{X/e},\qquad
\text{an unnamed integrated packet}.
\]

It is a normalized labelled local datum. Its actual global coefficient is
supplied by the outer measure, Hall residual, and the separately stated
positive realization operator.

Let `0<=nu_x(e)<=1` be the residual coefficients of the local Hall transport.
The free integrated certificate is

\[
\boxed{
\widehat Z_X
=
\int_{I_X}
\sum_{e\in E_x}
\nu_x(e)\widehat A_{X;s,e}^{(67)}
\,d\tau_X(s).
}
\tag{L-91663.19}
\]

Its physical realization is, by definition,

\[
\boxed{
R_X\widehat Z_X
=
\int_{I_X}
\sum_{e\in E_x}
\nu_x(e)\,
\mathscr I_{X,s}\mathsf A_{x,e}
\,d\tau_X(s),
}
\tag{L-91663.20}
\]

where `I_(X,s)` is the complete linear outer realization: endpoint-frame
insertion, sum-before-quantize martingale B-spline lift, and the packet-owned
boundary channels. Every numerical coordinate of (L-91663.20) is an explicit
Bochner integral. A proof that this realized datum fits the residual native
capacity is a separate theorem, not part of the definition.

## 6. Correct integrated certificate-mass bound

Give every normalized free atom in (L-91663.17) unit coefficient mass. Since
there are fewer than 55 active nodes and `nu_x(e)<=1`,

\[
\widehat m(\widehat Z_X)
\le
54\,\tau_X(I_X).
\tag{L-91663.21}
\]

Also,

\[
\tau_X(I_X)
=
2\log\frac{X-W-2}{K+2}
<
2\log(c_0^{-1})
<
2\log55
<
10.
\tag{L-91663.22}
\]

Hence

\[
\boxed{
\widehat m(\widehat Z_X)<540.
}
\tag{L-91663.23}
\]

The former bound `<=54` was a count of local residual coefficients before
integration. It was not the mass of a fully typed global certificate. The
correct global statement is still an absolute bound, which is all the packet
envelope requires.

One may instead normalize `tau_X` to probability mass and retain the number 54;
then its normalizing factor must appear in every benchmark, capacity, score, and
deficit coordinate. Equation (L-91663.23) avoids that hidden convention.

## 7. Exact scope

This theorem proves:

```text
one complete local/global packet category              EXACT
same-index child normalization                         EXACT
Bochner feasibility and deficit subadditivity          EXACT
explicit meaning of each root fiber atom               EXACT
local Hall family becomes a typed global certificate   EXACT
integrated certificate mass <540                       EXACT
```

It does not prove:

```text
R_X Z_X is a source-disjoint subdatum of N_X;
N_X-R_X Z_X has nonnegative capacities;
the summed current row fits those residual capacities;
the current benchmark-score debt is uniformly bounded.
```

Those four statements are precisely the native-root capacity theorem.
