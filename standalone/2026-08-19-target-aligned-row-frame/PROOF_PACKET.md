# T99320 standalone proof packet

**Scientific status: proposed complete candidate; RH remains unproved pending independent review.**

# L-99320 — Every parabolic component row is a positive rank-one lift of the SHARP target

Claim ID: `L-99320`  
Status: **PROPOSED COMPLETE EXACT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-19  
Frozen parent: PR #641 at `19cd3939a54ccea73b055b3952b5dd7ed638c4fb`  
RH status: **not assumed**

## 1. Canonical row coefficients

For real \(Y\ge1\), put

\[
h_Y(m)=m^{-1/2}\log(Y/m)\mathbf 1_{m\le Y},
\qquad
S_Y(n)=\sum_{m\ge n}h_Y(m),
\]

and

\[
Q_Y(j)=(j+1)\Delta_j^2\!\left[\frac{S_Y(j)}{j-1}\right],
\qquad j\ge2.
\]

Define

\[
A_j=\frac{j+1}{j-1},\qquad
B_j=\frac{(j+1)(j-2)}{j(j-1)},\qquad
C_j=\frac2{j(j-1)}
\]

and

\[
a_{j,m}=
\begin{cases}
A_j,&m=j,\\
-B_j,&m=j+1,\\
C_j,&m\ge j+2,\\
0,&m<j.
\end{cases}
\]

Direct expansion of the second difference gives

\[
\boxed{
Q_Y(j)=\sum_{m\ge j}a_{j,m}h_Y(m).
}
\tag{L-99320.1}
\]

The coefficient \(a_{j,j+1}\) may be negative. The theorem below shows that
after one exact target-aligned transform the complete atom is nevertheless
strictly positive.

## 2. Two target kernels

Put

\[
G(y)=(2\sqrt y-1)\mathbf1_{y\ge1},
\qquad
T(y)=(4\sqrt y-3)\mathbf1_{y\ge1}.
\]

For \(t\ge1\), define

\[
\boxed{
\kappa_j(t)
=
\sum_{j\le m\le t}
\frac{a_{j,m}}{\sqrt m}
\left(2\sqrt{\frac mt}-1\right)
}
\tag{L-99320.2}
\]

and

\[
\boxed{
\eta_j(t)
=
\frac13\sum_{j\le m\le t}
\frac{a_{j,m}}{\sqrt m}
\left(4\left(\frac mt\right)^{3/2}-1\right).
}
\tag{L-99320.3}
\]

Both sums are finite and use the natural one-sided activation convention.

For every \(1\le m\le Y\), direct integration gives

\[
\boxed{
\frac1{\sqrt m}\log\frac Ym
=
\int_m^Y
G(Y/t)\,
\frac1{\sqrt m}
\left(2\sqrt{\frac mt}-1\right)\frac{dt}{t}
}
\tag{L-99320.4}
\]

and independently

\[
\boxed{
\frac1{\sqrt m}\log\frac Ym
=
\int_m^Y
T(Y/t)\,
\frac1{3\sqrt m}
\left(4\left(\frac mt\right)^{3/2}-1\right)\frac{dt}{t}.
}
\tag{L-99320.5}
\]

For (L-99320.5), after \(t=mu\), the integrand expands as

\[
16\sqrt{Y/m}\,u^{-3}
-4\sqrt{Y/m}\,u^{-3/2}
-12u^{-5/2}
+3u^{-1}.
\]

The first three antiderivatives cancel at both endpoints, leaving
\(3\log(Y/m)\).

Finite Fubini and (L-99320.1) therefore give

\[
\boxed{
Q_Y(j)=\int_1^Y G(Y/t)\kappa_j(t)\frac{dt}{t}
}
\tag{L-99320.6}
\]

and

\[
\boxed{
Q_Y(j)=\int_1^Y T(Y/t)\eta_j(t)\frac{dt}{t}.
}
\tag{L-99320.7}
\]

No continuum approximation, Volterra inversion, anchor mode, knot atom, or
finite/continuum comparison enters these identities.

## 3. Exact positivity of the atoms

Fix \(j\ge2\). On \(j\le t<j+1\),

\[
\kappa_j(t)
=
\frac{A_j}{\sqrt j}
\left(2\sqrt{\frac jt}-1\right)>0
\]

because \(4j>j+1\). Likewise \(\eta_j(t)>0\), since
\(16j^3>(j+1)^3\).

Now let \(N=\lfloor t\rfloor\ge j+1\), and put

\[
R_{j,N}=\sum_{m=j}^N\frac{a_{j,m}}{\sqrt m}.
\]

Two exact telescopes are

\[
\boxed{
\sum_{m=j}^Na_{j,m}=C_jN,
}
\tag{L-99320.8}
\]

\[
\boxed{
\sum_{m=j}^Na_{j,m}m=\frac{C_j}{2}N(N+1).
}
\tag{L-99320.9}
\]

Hence on \(N\le t<N+1\),

\[
\kappa_j(t)
=
C_j\frac{2N}{\sqrt t}-R_{j,N},
\tag{L-99320.10}
\]

\[
\eta_j(t)
=
\frac{C_j}{3}\frac{2N(N+1)}{t^{3/2}}
-\frac13R_{j,N}.
\tag{L-99320.11}
\]

Both are strictly decreasing on the cell, and have the same normalized
right-endpoint lower bound

\[
D_{j,N}
=
\frac{2N}{\sqrt{N+1}}
-\frac{R_{j,N}}{C_j}.
\tag{L-99320.12}
\]

For \(N\ge j+1\),

\[
D_{j,N+1}-D_{j,N}
=
\frac{2(N+1)}{\sqrt{N+2}}
-\frac{2N+1}{\sqrt{N+1}}>0,
\tag{L-99320.13}
\]

because after squaring and clearing positive denominators the difference is
exactly \(3N+2>0\).

At the first complete cell,

\[
\begin{aligned}
D_{j,j+1}
={}&
\frac{2(j+1)}{\sqrt{j+2}}
-\frac{j+1}{2}\sqrt j
+\frac{j-2}{2}\sqrt{j+1}\\
={}&
\frac{2(j+1)}{\sqrt{j+2}}
-\frac32\sqrt j
+\frac{j-2}{2(\sqrt{j+1}+\sqrt j)}\\
>{}&0,
\end{aligned}
\tag{L-99320.14}
\]

since

\[
16(j+1)^2-9j(j+2)=7j^2+14j+16>0.
\]

Therefore

\[
\boxed{
\kappa_j(t)>0,\qquad
\eta_j(t)>0
\quad(t\ge j,\ j\ge2).
}
\tag{L-99320.15}
\]

The negative coefficient at \(m=j+1\) is paid exactly by the first complete
cell; every later activation has positive coefficient \(C_j\).

## 4. Mellin symbols

Initially in their absolute-convergence half-planes,

\[
\widehat G(s)
=
\frac{s+\frac12}{s(s-\frac12)},
\qquad
\widehat T(s)
=
\frac{s+\frac32}{s(s-\frac12)}.
\]

Writing

\[
H_j(z)=\sum_{m\ge j}a_{j,m}m^{-z},
\]

one has

\[
\widehat\kappa_j(s)
=
H_j(s+\tfrac12)\frac{s-\frac12}{s(s+\frac12)}
\]

and

\[
\widehat\eta_j(s)
=
H_j(s+\tfrac12)\frac{s-\frac12}{s(s+\frac32)}.
\]

Thus both products equal \(H_j(s+\frac12)/s^2\), the exact Mellin transform of
\(Q_Y(j)\).

## 5. Scope

The theorem proves an exact positive row atom. It does not assert positivity
of an arbitrary signed target source. Its force is functorial:

```text
one source-faithful positive realization of the scalar target
    automatically lifts through the same coefficients
    to every component row simultaneously.
```


---

# L-99321 — Compact Hall and causal rough splitting lift through one target-aligned row atom

Claim ID: `L-99321`  
Status: **PROPOSED COMPLETE EXACT COMMON-PARENT THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-19  
Depends on: `L-99320`; compact target Hall and target-source identities at the
exact frozen scopes of PRs #620, #632, and #636  
RH status: **not assumed**

## 1. Compact finite-Euler fibre

Let \(P_{61}=\prod_{p\le61}p\). For \(1\le x<67\), define

\[
D_{61,x}(j)
=
\sum_{\substack{k\mid P_{61}\\k\le x}}
\frac{\mu(k)}{\sqrt k}Q_{x/k}(j).
\]

Using `L-99320.7` and finite Fubini,

\[
\boxed{
D_{61,x}(j)
=
\int_1^x
\eta_j(t)\,
\Phi_{61}(x/t)\frac{dt}{t},
}
\tag{L-99321.1}
\]

where

\[
\Phi_{61}(y)
=
\sum_{\substack{k\mid P_{61}\\k\le y}}
\frac{\mu(k)}{\sqrt k}T(y/k).
\tag{L-99321.2}
\]

For fixed \(t\), the bracket is exactly the compact target Hall problem at
parameter \(y=x/t<67\). The frozen directed Hall theorem supplies one target
flow with nonnegative residual target. Since \(\eta_j(t)\ge0\) is independent
of the source colour \(k\), the same flow simultaneously gives the row
identity in every \(j\):

\[
\text{signed row at }t
=
\eta_j(t)\times
\bigl(\text{matched nonnegative target current}
+\text{positive residual target}\bigr).
\tag{L-99321.3}
\]

Thus

\[
\boxed{
D_{61,x}(j)\ge0
\qquad(1\le x<67,\ j\ge2).
}
\tag{L-99321.4}
\]

This uses only target Hall. The normalized component-row profile determinants
and their source-dependent monotonicity are unnecessary.

The Hall flow changes only at finitely many activation values of \(x/t\).
Choose the canonical nested-neighbourhood flow on each cell. It is piecewise
measurable, and finite Tonelli gives one literal common-parent source.

## 2. Causal parent-minus-child current

For a prime \(p\ge67\), \(r=p^{-1/2}\), and \(Y\ge p\),

\[
Q_Y(j)-rQ_{Y/p}(j)
=
\int_1^Y
\eta_j(t)
\Bigl[
T(Y/t)
-r\mathbf1_{t\le Y/p}T(Y/(pt))
\Bigr]\frac{dt}{t}.
\tag{L-99321.5}
\]

If \(t>Y/p\), the bracket is \(T(Y/t)>0\). If \(t\le Y/p\), put
\(z=Y/(pt)\ge1\). Then

\[
\begin{aligned}
T(pz)-p^{-1/2}T(z)
&=
4\sqrt z(\sqrt p-p^{-1/2})
-3(1-p^{-1/2})\\
&\ge
\frac{(\sqrt p-1)(4\sqrt p+1)}{\sqrt p}>0.
\end{aligned}
\tag{L-99321.6}
\]

Therefore

\[
\boxed{
Q_Y(j)-p^{-1/2}Q_{Y/p}(j)>0
\quad(p\ge67,\ Y\ge p,\ j\ge2)
}
\tag{L-99321.7}
\]

whenever the row is active.

Equation (L-99321.5) is source-level: the same target difference multiplies
every row atom. Current, target, and every row use one coefficient list.

## 3. One random key for all rows

At a residual target micro-source with endpoint \(Y\), the exact causal
coefficients satisfy

\[
\alpha_i=r_i\lambda_i,\qquad
\sum_i\alpha_i<67^{-1/2}<1/8.
\]

Cross the target source with one key \(u\in[0,1]\), and assign disjoint
intervals of lengths \(\alpha_i\mathbf1_{t\le Y_i}\) to the children. Since
every row observation is \(\eta_j(t)\) times the same target source, the single
partition gives simultaneously

\[
\alpha_i Q_{Y_i}(j)
\]

in every row. Its complement gives the exact positive current in
(L-99321.5). Repeat with a fresh key at every child. Since

\[
Y'\le Y/67+1,
\]

the tree is finite at each root.

## 4. Rank-one common-parent principle

Let \(\mathcal S\) be a finite signed target source for which the frozen
target-only Hall/causal construction gives one nonnegative labelled measure
\(\nu\). Then for every \(j\ge2\),

\[
\boxed{
\mathcal S[Q_Y(j)]
=
\int Q_Y(j)\,d\nu\ge0,
}
\tag{L-99321.8}
\]

with the same source labels and coefficients in all rows.

The component-row common-parent problem is rank one over the scalar target.
No additional row transport gate remains.

## 5. Scope firewall

This theorem does not prove the compact target Hall inequalities, the exact
root target-source identity, or the finite endpoint calibration. It proves
that once those target-only inputs are supplied, the complete row lift is
automatic and exact. Score and ordinary/radix-four capacities are outside this
fixed-row theorem.


---

# L-99322 — The target-aligned lift closes the actual fixed-row identity modulo the bounded calibration ledger

Claim ID: `L-99322`  
Status: **PROPOSED COMPLETE COMPOSITION THEOREM — ACTUAL LEDGER REVIEW REQUIRED**  
Created: 2026-08-19  
Depends on: `L-99320/L-99321`; PR #641 `L-99240/L-99241`; PR #638 boundary
audit; PR #632 random-key theorem  
RH status: **not assumed**

Fix one row \(j\ge2\).

## 1. Positive source part

Apply `L-99321` on every retained compact endpoint fibre in the exact root
source registry. Integrate the target-aligned row source over the positive
retained endpoint measure, and resolve only residual \(\alpha\)-children.

Let \(D_X(j)\) be the sum of all current and terminal observations. Then

\[
\boxed{D_X(j)\ge0.}
\tag{L-99322.1}
\]

The construction is literal:

```text
one target Hall flow at each target parameter;
one positive row atom eta_j(t);
one random-key child partition;
one owner for every micro-source;
only alpha-children recurse.
```

The normalized-row Hall bonus of PR #636 is not used. It is replaced by the
target factorization in `L-99321`.

## 2. Exact signed calibration

Define \(C_Y(j)\) at a typed node as the exact difference between the finite
native row contribution and the retained positive source contribution. It
contains, with actual signs:

1. retained-cell finite/continuum discrepancy;
2. activation-knot atoms;
3. the two homogeneous Volterra boundary modes;
4. finitely many anchored low-endpoint cells;
5. source-owned omissions not assigned to the positive target tree.

This definition gives the exact local identity

\[
\boxed{
E_Y(j)=J_Y(j)+(E_YT_Y)(j)+C_Y(j).
}
\tag{L-99322.2}
\]

The target-aligned lift proves that \(J_Y(j)\) and \(E_YT_Y(j)\) arise from
one source. PR #638 proves that the distributional boundary ledger has only
finitely many knot atoms and two homogeneous modes. PR #641 gives

\[
|C_Y(j)|\le B_j
\tag{L-99322.3}
\]

uniformly in the endpoint and provenance label.

## 3. Resolution

The child operator is nilpotent at a fixed root. Therefore

\[
\boxed{
c_X(j)=D_X(j)+\mathfrak E_X(j),
}
\tag{L-99322.4}
\]

where

\[
D_X(j)=J_X(I-T_X)^{-1}s_X\ge0
\]

and

\[
\mathfrak E_X(j)=C_X(I-T_X)^{-1}s_X.
\]

Only \(\alpha\)-children recurse and their total coefficient is below \(1/8\).
The compact root mass is finite, so

\[
\boxed{
|\mathfrak E_X(j)|\le K_j<\infty
}
\tag{L-99322.5}
\]

uniformly in \(X\).

## 4. Repaired interface

The actual identity required by PR #641 is now explicit:

```text
finite native row
=
target-aligned positive current
+ target-aligned positive children
+ signed source-owned calibration.
```

No calibration term is asserted positive. No Volterra anchor is promoted into
the positive source. The row identity is formed before Mellin transformation.

## 5. Reconstruction boundary

The sole imported arithmetic assertion is the target-only compact Hall/root
source ledger at its frozen scope. A failure there rejects the candidate.
There is no longer an independent component-row, normalized-profile,
endpoint-nesting, or row-coupling obligation.


---

# R-99320 — Positive row atoms do not by themselves prove the target source positive

Claim ID: `R-99320`  
Status: **EXACT TYPE FIREWALL**  
Created: 2026-08-19

Let \(\eta_j(t)>0\) be the atom of `L-99320`. For an arbitrary signed scalar
source \(f(t)\),

\[
\int\eta_j(t)f(t)\frac{dt}{t}
\]

need not be nonnegative. Taking \(f=-\mathbf1_I\) on any interval \(I\) gives a
strictly negative row.

The implication used by the candidate is exactly

\[
\text{one source-faithful positive target decomposition}
\Longrightarrow
\text{one positive common row decomposition},
\]

not

\[
\eta_j\ge0
\Longrightarrow
\text{every signed Möbius target is positive}.
\]

This forbids:

- dropping the compact target Hall theorem;
- replacing the exact root target ledger by its total mass;
- taking absolute values before source ownership;
- treating bounded signed calibration as positive source;
- claiming RH from the kernel factorization alone.


---

# T-99320 — Target-aligned rank-one common-parent component-row RH candidate

Claim ID: `T-99320`  
Status: **PROPOSED COMPLETE UNCONDITIONAL PROOF CANDIDATE — HOSTILE REVIEW REQUIRED**  
Created: 2026-08-19  
Base: PR #641 at `19cd3939a54ccea73b055b3952b5dd7ed638c4fb`  
RH status: **not established by publication**

## 1. Single new mechanism

Every component row has the exact factorization

\[
Q_Y(j)=\int_1^Y T(Y/t)\eta_j(t)\frac{dt}{t},
\qquad
\eta_j(t)>0.
\]

The source scalar is exactly the same SHARP target used by compact Hall and the
causal target tree. At fixed \(t\), every source colour has the same normalized
row vector \((\eta_j(t))_j\).

Consequently:

```text
target Hall automatically transports every component row;
one target random key automatically partitions every row child;
every causal parent-minus-child row is positive pointwise;
no normalized-row determinant or coordinatewise coupling is needed.
```

## 2. Complete chain

Freeze the compact target Hall and target-source registry at their exact PR
#620/#632/#636 scopes.

`L-99321` lifts that target source to every physical component row.
`L-99322` forms the actual row identity and keeps all finite/continuum, knot,
boundary and anchored calibration data signed. PR #641's fixed-row bound gives

\[
c_X(j)=D_X(j)+\mathfrak E_X(j),
\qquad
D_X(j)\ge0,
\qquad
\mathfrak E_X(j)=O_j(1).
\tag{T-99320.1}
\]

For fixed \(j\), write

\[
H_j(z)=\sum_{m\ge j}a_{j,m}m^{-z}
=C_j\zeta(z)+P_j(z).
\]

Finite Fubini gives initially for \(\Re s>1/2\)

\[
\boxed{
\int_1^\infty c_X(j)X^{-s-1}\,dX
=
\frac{C_j}{s^2}
+
\frac{P_j(s+1/2)}
{s^2\zeta(s+1/2)}.
}
\tag{T-99320.2}
\]

The bounded calibration transform is holomorphic in \(\Re s>0\). Hence the
same reciprocal-zeta pole occurs in the Mellin transform of the nonnegative
surrogate \(D_X(j)\).

For fixed \(z\) with \(0<\Re z<1\),

\[
\boxed{
P_j(z)
=
-\frac{z(z+1)}{1-z}j^{-z-1}
+o_z(j^{-\Re z-1}).
}
\tag{T-99320.3}
\]

Every hypothetical off-line zero therefore survives in some sufficiently
large fixed row. Landau's theorem applied to \(D_X(j)\ge0\) excludes the pole
at \(s=\rho-\frac12\); the functional equation excludes the reflected
half-plane.

This gives the proposed conclusion

\[
\boxed{\mathrm{RH}.}
\]

## 3. Interface audit

The candidate no longer uses:

```text
positive Volterra anchors;
positive activation-knot atoms;
normalized component-row Hall profiles;
endpoint monotonicity as a child-coupling theorem;
literal score or 4sqrt(X);
ordinary/radix-four capacity;
safe-point thinning;
prime-square moat.
```

The first and only imported arithmetic producer is:

> the source-faithful compact target Hall plus exact target-source random-key
> tree on the frozen root registry.

Every component-row interface after that producer is proved by
`L-99320`–`L-99322`.

## 4. Scientific boundary

The new rank-one theorem and fixed-row analytic consumer are proposed complete
mathematics. Because the conclusion would prove RH, the frozen target source
registry and every Hall/source coefficient require independent reconstruction.

```text
target-aligned positive row atom              PROVED EXACT
compact Hall lift to all rows                 PROPOSED COMPLETE
causal common-parent lift                     PROPOSED COMPLETE
actual row identity modulo bounded defect     PROPOSED COMPLETE
fixed-row pole preservation                   PROPOSED COMPLETE
accepted proof of RH                          NO
Riemann Hypothesis                            UNPROVEN PENDING REVIEW
```


---

# M-99320 — Hostile reconstruction protocol

Review in this order:

1. Expand \(Q_Y(j)\) directly and verify \(A_j,-B_j,C_j\).
2. Integrate both elementary target kernels term by term.
3. Check the first activation cell, both exact coefficient telescopes, the
   first complete cell, and the increment \(3N+2\).
4. At fixed \(t\), verify that the compact source bracket is exactly the
   target Hall problem at parameter \(x/t\), including every activation cutoff.
5. Verify the causal target difference separately on \(t\le Y/p\) and
   \(t>Y/p\).
6. Confirm that one random key, not one per row, creates all children.
7. Reconstruct the signed calibration identity before applying its bound.
8. Rebuild the fixed-row Mellin transform and large-\(j\) numerator asymptotic.
9. Treat the target Hall/root registry as the first imported arithmetic gate.
10. Do not represent publication as acceptance of RH.

Immediate falsifiers:

```text
one t,j with eta_j(t)<=0;
one missing activation convention;
one Hall coefficient depending on j;
one causal row coefficient different from its target coefficient;
one calibration term silently inserted into positive source;
one recursive coefficient outside the alpha children;
one off-line zero canceled by every P_j;
one claim that the replay proves the frozen Hall theorem or RH.
```


---

# Research report — target-aligned rank-one row frame

The latest portfolio had converged to one stubborn interface: an exact common
parent had to carry the target source and every component row with the same
coefficients, while the Volterra audit exposed signed boundary and knot data.

The new factorization diagonalizes that interface. Every canonical row is a
positive Mellin convolution of the same SHARP target with one row atom
\(\eta_j\). Although the raw row expansion has a negative \(j+1\) coefficient,
the transformed atom is strictly positive; its cell minima form an increasing
sequence with exact increment controlled by \(3N+2\).

At fixed integration coordinate, the compact source is literally the target
Hall problem at a rescaled parameter. The same Hall flow transports all rows
simultaneously. The factor-67 causal parent-minus-child is a positive target
difference times the same row atom, so one random key also transports every
child row.

The remaining finite/continuum and Volterra data stay in PR #641's bounded
signed fixed-row ledger. They need not be positive and cannot cancel a
reciprocal-zeta pole.

The complete candidate graph is therefore much smaller. Its sole imported
arithmetic producer is the compact target Hall/root source registry. RH is not
treated as established until that source ledger and the analytic consumer are
independently reconstructed.
