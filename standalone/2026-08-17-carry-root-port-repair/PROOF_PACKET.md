# Carry root-port separator and repair packet

**Scientific status: RH remains unproved.**


---

# R-95300 — PICR is impossible by the exact dyadic root separator

Claim ID: `R-95300`  
Status: **PROPOSED COMPLETE EXACT REFUTATION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Frozen parent: PR #562 at `9537096f498c7ee0ca2141394f43f0a2f704cce4`  
Scope: integer square-root hinges and carry realizations using only splits whose children are at least two

## 1. Root source

Put

\[
b_2=(\varepsilon-\delta_2)*\mu.
\]

Since \(1*\mu=\varepsilon\),

\[
1*b_2=\varepsilon-\delta_2.
\tag{R-95300.1}
\]

For real \(x\ge0\), define

\[
G_2(x)
=
\sum_{q\le x}b_2(q)\left\lfloor\frac{x}{q}\right\rfloor.
\]

Divisor switching gives

\[
\boxed{
G_2(0)=0,\qquad G_2(1)=1,\qquad G_2(x)=0\quad(x\ge2).
}
\tag{R-95300.2}
\]

For a split \(e=(n,j)\), \(n=j+k\), its carry column is

\[
\chi_e(q)
=
\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac kq\right\rfloor.
\]

If both children are at least two, then

\[
\boxed{
\sum_q b_2(q)\chi_e(q)
=
G_2(n)-G_2(j)-G_2(k)
=
0.
}
\tag{R-95300.3}
\]

Therefore every signed interior carry flow, not merely every nonnegative one,
has zero \(b_2\)-response.

## 2. The critical hinge has nonzero response

For an integer endpoint \(T\ge2\), put

\[
h_T(q)
=
q^{-1/2}-T^{-1/2},
\qquad 2\le q\le T,
\]

and define

\[
\rho_T
=
\sum_{q=2}^{T}
b_2(q)
\left(q^{-1/2}-T^{-1/2}\right).
\tag{R-95300.4}
\]

Write \(q=2^em\), \(m\) odd. Then

\[
b_2(2^em)=
\begin{cases}
\mu(m),&e=0,\\
-2\mu(m),&e=1,\\
\mu(m),&e=2,\\
0,&e\ge3.
\end{cases}
\tag{R-95300.5}
\]

The values vanish unless \(m\) is squarefree.

Let \(\operatorname{sf}(n)\) be the squarefree kernel. Square roots of distinct
squarefree integers are linearly independent over \(\mathbb Q\).

If \(\operatorname{sf}(T)\ne2\), the only nonzero \(b_2(q)\) term in
(R-95300.4) with radical \(\sqrt2\) is \(q=2\), and its coefficient is

\[
\frac{b_2(2)}{\sqrt2}=-\sqrt2.
\]

The endpoint term has radical \(\sqrt{\operatorname{sf}(T)}\), so it cannot
cancel this coefficient.

If \(\operatorname{sf}(T)=2\) and \(T\ge7\), then \(T\ge8\). The only nonzero
\(b_2(q)\) term with radical \(\sqrt6\) is \(q=6\), and

\[
\frac{b_2(6)}{\sqrt6}
=
\frac{\sqrt6}{3}.
\]

The endpoint term again lies in the \(\sqrt2\) radical class.

Hence

\[
\boxed{\rho_T\ne0\qquad(T\ge7).}
\tag{R-95300.6}
\]

## 3. Refutation

Every signed interior realization would have zero \(b_2\)-response by
(R-95300.3), while the critical hinge has response \(\rho_T\ne0\). Therefore

\[
\boxed{
T\ge7
\Longrightarrow
h_T\text{ has no signed interior realization.}
}
\tag{R-95300.7}
\]

A fortiori the `PICR` statement in `T-95270` is false.

This refutation does not affect:

```text
the 5:3 bottom-contact identity;
the positive Julia compression;
the scalar interval on the positive two-leaf cone.
```

It refutes only the proposed entry of the unmodified hinge into the
root-free interior cone.


---

# L-95300 — Multiples Möbius inversion gives one exact minimal root port

Claim ID: `L-95300`  
Status: **PROPOSED COMPLETE EXACT FINITE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `R-95300`; the quarter-balanced signed-span geometry of PR #538

## 1. Carry load to node divergence

Let \(w(q)\) be finitely supported on physical columns \(q\ge2\), and put
\(w(1)=0\). Define

\[
R_w(m)
=
\sum_{d\ge1}\mu(d)w(md),
\tag{L-95300.1}
\]

where the sum is finite, and

\[
r_w(m)=R_w(m)-R_w(m+1).
\tag{L-95300.2}
\]

Then

\[
\boxed{
w(q)=\sum_{n\ge q}r_w(n)\left\lfloor\frac nq\right\rfloor.
}
\tag{L-95300.3}
\]

Indeed, the right side is

\[
\sum_{a\ge1}R_w(aq),
\]

and Möbius inversion on the divisibility poset gives (L-95300.1).

The node source conserves size:

\[
\boxed{
\sum_{n\ge1}n\,r_w(n)=w(1)=0.
}
\tag{L-95300.4}
\]

Its root coordinate is exactly

\[
\boxed{
r_w(1)
=
\sum_{q\ge2}b_2(q)w(q)
=:\rho(w).
}
\tag{L-95300.5}
\]

## 2. Signed interior span, reconstructed

For every \(n\ge4\), the balanced split

\[
n=\lfloor n/2\rfloor+\lceil n/2\rceil
\]

has children at least two and is quarter-balanced. Recursion reduces every
basis vector \(e_n\), modulo interior split divergences, to a combination of
\(e_2,e_3\).

At parent six, compare the two legal trees

\[
6\longrightarrow3+3
\]

and

\[
6\longrightarrow2+4\longrightarrow2+2+2.
\]

Their difference gives the exact relation

\[
3e_2-2e_3
\]

inside the interior split span. Thus the quotient of the node space by
interior split divergences is one-dimensional, measured by total size.
Consequently

\[
\boxed{
r(1)=0,\quad \sum_nnr(n)=0
\Longrightarrow
r\text{ is a signed quarter-balanced interior divergence.}
}
\tag{L-95300.6}
\]

## 3. One root edge spans the missing quotient

Let

\[
\gamma=\chi_{3,1}.
\]

On physical columns,

\[
\boxed{\gamma(q)=\mathbf1_{q=3}.}
\tag{L-95300.7}
\]

Moreover,

\[
\langle b_2,\gamma\rangle=b_2(3)=-1.
\tag{L-95300.8}
\]

For arbitrary \(w\), define

\[
w^\circ=w+\rho(w)\gamma.
\tag{L-95300.9}
\]

Then

\[
\langle b_2,w^\circ\rangle=0.
\]

By (L-95300.4) and (L-95300.6), \(w^\circ\) has a signed interior
realization. Therefore

\[
\boxed{
w=w^\circ-\rho(w)\gamma,
}
\tag{L-95300.10}
\]

where:

```text
w^circ       is signed interior-realizable;
-rho(w)γ     is one boundary root port on 3 -> 1+2.
```

The root-port coefficient is unique, because the interior quotient has
dimension one.

## 4. Positive two-channel realization

Split the signed interior realization into its positive and negative edge
parts. Equation (L-95300.10) then gives a positive two-channel representation
of every physical carry target. The root edge belongs to the positive channel
when \(\rho(w)\le0\), and to the negative channel when \(\rho(w)>0\).

This is an exact positive matrix/two-colour replacement for the false
single-channel PICR statement. It does not prove a one-channel positive
realization.


---

# L-95301 — The critical root port is an adjacent-dyadic Mertens flux

Claim ID: `L-95301`  
Status: **PROPOSED COMPLETE EXACT ANALYTIC REDUCTION — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `R-95300/L-95300`

Let

\[
\rho_T
=
\sum_{q\le T}b_2(q)
\left(q^{-1/2}-T^{-1/2}\right),
\]

with the \(q=1\) physical column omitted as above, and put

\[
B_2^\circ(T)=\sum_{2\le q\le T}b_2(q).
\]

Since \(b_2=(\varepsilon-\delta_2)*\mu\),

\[
\boxed{
B_2^\circ(T)=M(T)-M(T/2)-1,
}
\tag{L-95301.1}
\]

where \(M(x)=\sum_{n\le x}\mu(n)\).

The entering hinge at \(q=T+1\) vanishes, so

\[
\boxed{
\rho_{T+1}-\rho_T
=
\left[M(T)-M(T/2)-1\right]
\left(T^{-1/2}-(T+1)^{-1/2}\right).
}
\tag{L-95301.2}
\]

Thus the exact root-port evolution is one adjacent-dyadic Mertens flux.

For the continuous endpoint function

\[
\rho(x)
=
\sum_{2\le q\le x}
b_2(q)
\left(q^{-1/2}-x^{-1/2}\right),
\]

one has initially for \(\Re z>1/2\)

\[
\boxed{
\int_1^\infty\rho(x)x^{-z-1}\,dx
=
\frac{1}{2z(z+1/2)}
\left[
\frac{1-2^{-z-1/2}}{\zeta(z+1/2)}
-1
\right].
}
\tag{L-95301.3}
\]

The \(-1\) is the mandatory deleted-column-one correction.

Every hypothetical zeta zero with real part greater than \(1/2\) creates a
nonreal pole in the positive \(z\)-half-plane; the finite dyadic numerator
cannot cancel it. Hence eventual one-sign control of the root port is already
an RH-producing theorem by Landau.

The root port is therefore not a harmless boundary term. It is the exact
arithmetic mode that PICR attempted to suppress.


---

# T-95300 — Corrected carry programme after the PICR separator

Claim ID: `T-95300`  
Status: **CORRECTED CONDITIONAL PROGRAMME — RH UNPROVED**  
Created: 2026-08-17  
Depends on: `R-95300`, `L-95300`, `L-95301`; retained exact results of PR #562

## Corrected architecture

For the square-root hinge,

\[
h_T=h_T^\circ-\rho_T\gamma,
\qquad
\gamma=\chi_{3,1},
\qquad
\langle b_2,h_T^\circ\rangle=0.
\]

The exact signed-span theorem realizes \(h_T^\circ\) in the interior. The
boundary coefficient \(-\rho_T\) is unavoidable and unique.

A valid one-channel positive construction must therefore prove both:

1. the root-port orientation
   \[
   \rho_T\le0;
   \]
2. a nonnegative interior realization of the root-neutral remainder
   \[
   h_T^\circ=h_T+\rho_T\gamma.
   \]

The first condition alone is already RH-bearing by `L-95301`. The second
cannot be inferred from signed span, root neutrality, or Julia-column
positivity.

## Surviving conclusion

PR #562's exact \(5{:}3\) terminalization and Julia reserve remain valid on any
genuine positive interior packet. What is withdrawn is the claim that the
unmodified hinge can enter that packet.

```text
PICR                                         FALSE
one-dimensional root quotient               CLOSED
minimal boundary root port                  CLOSED
signed transverse realization               CLOSED
positive two-channel realization            CLOSED
root-port one-sign                          OPEN / RH-BEARING
positive root-neutral interior realization  OPEN
Riemann Hypothesis                          UNPROVEN
```


---

# M-95300 — Hostile review protocol for the carry root-port correction

Review in this order:

1. `R-95300`: recompute \(1*b_2\), the interior annihilator and the radical
   noncancellation.
2. `L-95300`: check multiples Möbius inversion, size conservation, the
   six-node relation and the root edge \(\gamma=\chi_{3,1}\).
3. `L-95301`: check the endpoint increment and deleted-column-one Mellin term.
4. `T-95300`: ensure no one-channel positivity is inferred from the signed or
   two-channel constructions.

Immediate falsifiers:

```text
one interior edge with nonzero b2 response;
one T>=7 with rho_T=0;
an incorrect q=1 physical column;
a root-port coefficient different from -rho(w);
a claim that rho_T has an unconditional eventual sign;
a claim that two-channel positivity proves one-channel PICR.
```


---

# Carry correction after the PICR falsifier

The interior carry cone has an exact one-dimensional quotient. Its dual is the
dyadic source \(b_2\), and the square-root hinge has a nonzero coordinate in
that quotient for every integer endpoint \(T\ge7\).

The correct decomposition is

\[
h_T=h_T^\circ-\rho_T\chi_{3,1},
\]

where the transverse component has a signed interior realization and the
second term is one unavoidable boundary root port.

The root coefficient evolves by

\[
\rho_{T+1}-\rho_T
=
[M(T)-M(T/2)]
[T^{-1/2}-(T+1)^{-1/2}],
\]

so its eventual sign is already a reciprocal-zeta/Mertens theorem.

The strongest unconditional replacement for PICR is a positive two-channel
root-port realization. A one-channel positive completion remains open.
