# R-93022 - Positive scale-four source ownership does not control the Q4 principal mean

Claim ID: `R-93022`  
Status: **EXACT SCOPE FIREWALL / NO-GO FOR A SOURCE-BLIND FULL-ROW TRANSFER**  
Created: 2026-08-16  
Corrects: any inference from `L-93022` that positive source coefficients alone bound the complete endpoint PIG  
Depends on: `L-93022`; `L-93018`; elementary finite row geometry  
Scope: the endpoint fibres of the positive scale-four source; no refutation of a source-specific aggregate theorem

## 1. One atom already has a macroscopic principal channel

Retain

\[
 h_m(x)
 =
 \mathbf1_{m\le x}
 -
 2\mathbf1_{2m\le x}
\]

and

\[
 Z_{m,N}(j)
 =
 h_m(N)-h_m(j)-h_m(N-j-1).
\]

Assume \(N\ge4m\). Then

\[
 h_m(N)=-1.
\]

If

\[
 2m\le j
 \quad\text{and}\quad
 2m\le N-j-1,
\]

both children also have value \(-1\), and therefore

\[
 \boxed{Z_{m,N}(j)=1.}
 \tag{R-93022.1}
\]

There are exactly \(N-4m\) such coordinates. Consequently

\[
 \boxed{
 \|Z_{m,N}\|_2^2\ge N-4m.
 }
 \tag{R-93022.2}
\]

For a fixed source atom \(m\), the full row norm grows linearly with the
endpoint.

Thus no inequality of the form

\[
 \|Z_{m,N}\|_2^2
 \le C\,\mathcal R(m)
 \tag{R-93022.3}
\]

can hold uniformly in \(N\) when the proposed reserve
\(\mathcal R(m)\) depends only on the local source atom. Positivity and
source ownership do not remove the constant interior channel.

## 2. Exact compact transverse remainder

Define

\[
 E_{m,N}(j)=Z_{m,N}(j)-1.
 \tag{R-93022.4}
\]

When \(N\ge4m\), (R-93022.1) shows that \(E_{m,N}\) is supported on the two
boundary collars

\[
 j<2m
 \quad\text{or}\quad
 N-j-1<2m.
 \tag{R-93022.5}
\]

Hence

\[
 |\operatorname{supp}E_{m,N}|\le4m.
 \tag{R-93022.6}
\]

Since \(h_m\in\{-1,0,1\}\),

\[
 |E_{m,N}(j)|\le4,
\]

and therefore

\[
 \boxed{
 \|E_{m,N}\|_2^2\le64m.
 }
 \tag{R-93022.7}
\]

The scale-four transfer is thus capacity-faithful **after** the constant
principal channel is retained separately.

## 3. Every atom has a controlled mean-zero part

For arbitrary \(m\le N\), let

\[
 \overline Z_{m,N}
 =
 \frac1N\sum_{j=0}^{N-1}Z_{m,N}(j).
 \tag{R-93022.8}
\]

The fibre changes value only at

\[
 m,\quad 2m,\quad N-m,\quad N-2m
\]

up to endpoint shifts. If \(m\le N/4\), use (R-93022.7). If \(m>N/4\),
then \(N<4m\), and the trivial amplitude bound gives

\[
 \boxed{
 \|Z_{m,N}-\overline Z_{m,N}\mathbf1\|_2^2
 \le144m.
 }
 \tag{R-93022.9}
\]

Thus every positive source atom has one scalar principal coordinate and one
finite transverse packet with an explicit local capacity.

## 4. Aggregate consequence and its limit

The exact positive row decomposition becomes

\[
\begin{aligned}
R_N
={}&
\left[
 \sum_{m\le N}\Lambda_+(m)\overline Z_{m,N}
\right]\mathbf1\\
&+
\sum_{m\le N}\Lambda_+(m)
\left[
 Z_{m,N}-\overline Z_{m,N}\mathbf1
\right].
\end{aligned}
\tag{R-93022.10}
\]

The scalar coefficient in the first line is exactly the endpoint mean
\(M_\circ(N)\). Therefore

\[
 \boxed{
 R_N
 =
 M_\circ(N)\mathbf1+R_N^\perp,
 \qquad
 \langle R_N^\perp,\mathbf1\rangle=0.
 }
 \tag{R-93022.11}
\]

Equation (R-93022.9) supplies an atomwise transverse capacity ledger.
It does not by itself control the norm of the positive sum
\(R_N^\perp\): the fibres are nested and need a source-specific Gram,
Carleson, or martingale estimate.

Most importantly, the principal scalar cannot be discarded or absorbed into
a local reserve. By `L-93018/T-93011`, a square-root/polylogarithmic bound for
that scalar is already the complete RH-bearing Q4 theorem.

## 5. Hardy boundary firewall retained

The infinite backward Hardy inverse reconstructs the prefix from
\(M_\circ\) only after proving

\[
 C_\circ(N)=o(N).
\]

The positive source representation does not make this boundary automatic:
\(\Psi_+(N)\) itself has a linear main term. The cancellation occurs in

\[
 C_\circ(N)=\Psi_+(N)-2\Psi_+(N/2),
\]

and the unconditional PNT remains the required boundary theorem.

Thus neither of the following shortcuts is valid:

```text
positive Lambda_+  => bounded Q4 mean;
positive Lambda_+  => boundary-free Hardy inversion.
```

## 6. Corrected transfer target

The legitimate positive-transfer theorem has two independent outputs:

```text
principal output:
    M_circ(N), retained exactly;

transverse output:
    source-owned mean-zero fibres with atomwise norm <=144m.
```

A complete closure must either:

1. prove a source-specific aggregate estimate for the transverse Gram and a
   square-root bound for the principal scalar; or
2. couple the principal scalar to the Cycle-Debt root face before either
   coordinate is estimated separately.

The first atomwise step is closed in `L-93023`. The aggregate and cross-route
steps remain open.

## 7. Proof boundary

Established exactly:

- the constant interior channel;
- the macroscopic one-atom norm lower bound;
- the compact boundary remainder for \(N\ge4m\);
- the uniform mean-zero atomwise bound;
- the exact identification of the aggregate principal coefficient with
  \(M_\circ(N)\);
- the persistence of the Hardy boundary requirement.

Not established:

- an aggregate transverse Gram bound;
- a principal/root coupling;
- the Q4 mean estimate;
- RH.
