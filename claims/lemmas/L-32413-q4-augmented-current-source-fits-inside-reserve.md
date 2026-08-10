# L-32413 — The true Q=4 pole current and unweighted inverse source fit simultaneously inside the Kummer reserve

Claim ID: `L-32413`  
Title: On cofinal quarter-balanced rows, any fixed augmented energy consisting of the correctly typed Q=4 pole current plus the omitted unweighted inverse-source charge is paid by the same Selberg–Kummer reserve with arbitrarily large leftover slack  
Status: **PROPOSED COMPLETE UNCONDITIONAL COFINAL THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-s`  
Created: 2026-08-09  
Dependencies: `L-32405`, `L-32412` (true physical current); PR #337 `L-32706` (unweighted source collar)  
Scope: source-complete one-row/row-measure budget; complete independent-frequency product placement remains separate

## 1. The three row quantities

For a quarter-balanced split `n=j+k`, retain

\[
P_4(n,j),\qquad S_4(n,j),\qquad
\mathcal R_4(n,j)=P_4(n,j)^2-S_4(n,j)>0
\]

from `L-32405`.

Let

\[
Q_4^{\rm phys}(n,j)
\]

be the correctly typed centered-interval pole current of `L-32412`.

Let

\[
Y_4(n,j)
\]

be the carry charge of the omitted unweighted Q=4 inverse source `b_4`. PR #337 `L-32706` proves exactly

\[
Y_4(n,j)=3\bigl(
 \lfloor\log_4j\rfloor
 +\lfloor\log_4k\rfloor
 -\lfloor\log_4n\rfloor
\bigr)-1.
\tag{L-32413.1}
\]

## 2. The physical-current ratio vanishes

`L-32412` proves

\[
\boxed{
\sup_{n/4\le j\le3n/4}
{ |Q_4^{\rm phys}(n,j)|^2\over\mathcal R_4(n,j)}
\longrightarrow0.
}
\tag{L-32413.2}

This is the prime-sensitive part of the theorem.

## 3. The unweighted-source ratio also vanishes

On a quarter-balanced row, both children are between `n/4` and `3n/4`. Put

\[
r=\lfloor\log_4 n\rfloor.
\]

Equation (L-32413.1) immediately gives the uniform upper bound

\[
\boxed{|Y_4(n,j)|\le3r+1\le3\log_4 n+1.}
\tag{L-32413.3}

(`L-32706` gives the much sharper sign/collar geometry, but only the logarithmic size is needed here.)

On the other hand `L-32405` gives, cofinally and uniformly on the same balanced cone,

\[
\mathcal R_4(n,j)>{1\over20}P_4(n,j)^2
\]

and

\[
P_4(n,j)\ge {n\over4}\log2.
\]

Hence

\[
\boxed{
\mathcal R_4(n,j)
\ge {n^2\log^22\over320}
}
\tag{L-32413.4}

for all sufficiently large balanced rows. Combining (L-32413.3)--(L-32413.4),

\[
\boxed{
\sup_{n/4\le j\le3n/4}
{ |Y_4(n,j)|^2\over\mathcal R_4(n,j)}
\longrightarrow0.
}
\tag{L-32413.5}

No prime estimate enters this second limit.

## 4. Source-complete augmented reserve

Fix any constant `M>0`. From (L-32413.2) and (L-32413.5),

\[
\boxed{
\sup_{n/4\le j\le3n/4}
{ |Q_4^{\rm phys}(n,j)|^2+M|Y_4(n,j)|^2
 \over\mathcal R_4(n,j)}
\longrightarrow0.
}
\tag{L-32413.6}

Therefore, for every fixed `0<delta<1`, there is a finite `N_(M,delta)` such that for every `n>=N_(M,delta)` and every quarter-balanced split,

\[
\boxed{
|Q_4^{\rm phys}(n,j)|^2
+M|Y_4(n,j)|^2
+S_4(n,j)
\le
P_4(n,j)^2-(1-\delta)\mathcal R_4(n,j).
}
\tag{L-32413.7}

Equivalently, after simultaneously paying the true RH-sensitive current, the complete unweighted inverse-source boundary with any preassigned finite weight `M`, and the full Selberg forcing, a positive fraction `(1-delta)` of the Kummer reserve remains unused.

There is no rowwise double spending: both physical quantities are charged to the explicit remainder `R_4=P_4^2-S_4` after `S_4` is paid.

## 5. Row-measure form

Let `nu(n,j)>=0` be any finite measure supported on cofinal quarter-balanced rows. Summing (L-32413.7) gives

\[
\boxed{
\begin{aligned}
&\sum\nu |Q_4^{\rm phys}|^2
+M\sum\nu |Y_4|^2
+\sum\nu S_4\\
&\qquad\le
\sum\nu P_4^2
-(1-\delta)\sum\nu\mathcal R_4.
\end{aligned}}
\tag{L-32413.8}

Thus any independent-frequency localization whose exact source map produces a nonnegative row measure in these same coordinates may carry both the pole current and the unweighted boundary inside one Hermitian budget.

The finitely many parents below `N_(M,delta)` remain a finite base/collar table. PR #337 further localizes every *negative* unweighted source row to a child of size at most fifteen, so no cofinal adverse source sector is hidden in that finite table.

## 6. What this advances

The outstanding Q=4 reflected problem previously had two separate possible leaks:

```text
true pole-sensitive physical current;
omitted unweighted inverse-source boundary.
```

They are no longer separate asymptotic burdens. At row scope they fit simultaneously, with any fixed relative weighting, inside the source-matched Kummer reserve and leave a strict cofinal slack.

The remaining theorem is therefore algebraic/global rather than another arithmetic estimate:

> identify the complete source-convolved two-frequency reflected block with a nonnegative measure over these same balanced rows, plus the explicit unitary scattering terminal state and finite collars.

This lemma does **not** assert that identification.

## 7. Proof boundary

Closed here, subject to review:

1. vanishing current/reserve ratio (imported at correct source type);
2. vanishing unweighted-source/reserve ratio;
3. simultaneous augmented current+source+Selberg absorption for any fixed source weight;
4. finite nonnegative row-measure summation with positive leftover reserve.

Open:

1. exact source-convolved independent-frequency row-measure placement;
2. composition with the Q=4 unitary scattering terminal state into a coefficient-one block recurrence;
3. RH.
