# R-29001 — Fixed source-independent Abel escalation fails through order eight

Claim ID: `R-29001`  
Title: Exact binary–ternary producer witnesses reject the generic, second-, third-, and higher fixed-prefix positivity mechanisms through order eight  
Status: **EXACT SCOPE REFUTATION AND STRATEGIC FIREWALL**  
Authoring agent: `gpt56-pro-09-r`  
Created: 2026-08-08  
Frozen targets: PR #279 and the fixed-order Abel descendants of the binary–ternary producer  
Dependencies: PR #247 `L-23810/L-23811`; exact integer/Fraction recurrence  
Scope: refutes the listed ambient fixed-order mechanisms; does not refute positivity of the actual logarithmic target

## 1. Producer

For a target `w(2),...,w(X)`, let

\[
 U(m)=\sum_{k\le X/m}\mu(k)w(mk),
 \qquad
 r(m)=U(m)-U(m+1),
\]

and let `A_X(n)` be the exact descending binary–ternary producer

\[
\begin{aligned}
 A_X(n)=r(n)+\frac12\sum_{m>n}A_X(m)
 [&\mathbf1_{\lceil m/3\rceil=n}
  +\mathbf1_{m-\lceil m/3\rceil=n}\\
  &+\mathbf1_{\lfloor m/2\rfloor=n}
  +\mathbf1_{m-\lfloor m/2\rfloor=n}].
\end{aligned}
\tag{R-29001.1}

Repeated children retain their multiplicity.

For an Abel order `r>=1`, define the cumulative target

\[
\boxed{
 w_Q^{(r)}(q)
 =\binom{Q-q+r-1}{r-1}\mathbf1_{2\le q\le Q}.
}
\tag{R-29001.2}

## 2. Exact negative witnesses

Standard-library integer and `Fraction` arithmetic gives:

```text
second prefix
  X=60, Q=59, n=11
  A_X(n) = -13/16

third prefix
  X=Q=520, n=15
  A_X(n) = -91/256

fourth prefix
  X=Q=8000, n=23
  A_X(n) = -1168054960769/4096

fifth prefix
  X=Q=50000, n=21
  A_X(n) = -276224146188972518125/524288

sixth prefix
  X=Q=200000, n=19
  A_X(n) = -6675044750726111601348609105/4194304

seventh prefix
  X=Q=500000, n=31
  A_X(n) = -16746203761072984278127054633069029/8388608

eighth prefix
  X=Q=1000000, n=351
  A_X(n) = -1626263344550423356494876852927609539/65536
```

The generic positive-target mechanism already fails at `X=8`: taking only
`w(4)=1` gives `A_X(3)=-1`.

The order-three and order-four witnesses independently agree with the corrected
status now recorded on PR #279.  The higher witnesses show that simply adding a
few more source-independent cumulative integrations does not repair the
mechanism.

## 3. Exact disposition

```text
generic producer-kernel positivity              REFUTED
second cumulative producer positivity            REFUTED
third cumulative producer positivity             REFUTED
fourth through eighth fixed-prefix positivity    REFUTED
complete monotonicity of x^(-1/2)log(X/x)         RETAINED
positivity of the actual logarithmic producer     OPEN / NOT DISPROVED
adaptive source-complete recombination            OPEN
RH                                                 UNPROVED
```

An endpoint collar cannot repair the listed witnesses when the negative row is
an interior row of the cumulative kernel.

## 4. Strategic consequence

A valid completion cannot be based on a fixed ambient Abel order plus complete
monotonicity of the target.  It must use at least one of:

1. the actual source before replacing it by an ambient cone;
2. an order or partition adapted to the source and scale, with a complete
   first-cell firewall;
3. full ancestry recombination through Pascal cycles;
4. the atomized reflected energy and endpoint-tree mechanism of
   `L-29001`--`T-29001`.

## 5. Proof boundary

The displayed negative rational values are exact finite counterexamples to the
corresponding universal positivity claims.  They do not establish that every
fixed order fails, nor do they establish a negative value for the actual
critical logarithmic target.