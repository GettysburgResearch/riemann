# Mathematical digest: the weighted-tail determinant proof

```text
Status: SOURCE-FAITHFUL RECONSTRUCTION
Claimed endpoint: Catalan's constant G is irrational
Audit status: REVIEW_PENDING
```

## 1. L-function setting

Catalan's constant is the even Dirichlet beta value

\[
G=\beta(2)=L(2,\chi_{-4})
 =\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k+1)^2}.
\]

The paper contrasts this with the recently proved irrationality of
\(L(2,\chi_{-3})\), but the final proof does not use the
Calegari–Dimitrov–Tang arithmetic-holonomy machinery. Its own mechanism is a
weighted-tail determinant, local valuation saturation, and an archimedean
height estimate.

## 2. Weighted tails and the recurrence

For \(m\ge1\), let

\[
S_{m-1}=\sum_{k=0}^{m-1}\frac{(-1)^k}{(2k+1)^2},
\]

\[
T_m=\sum_{r=0}^{\infty}\frac{(-1)^r}{(2m+2r+1)^2}
    =(-1)^m(G-S_{m-1}),
\]

and

\[
u_m=\frac{T_m}{2m+1}.
\]

The alternating-series estimate gives

\[
0<T_m<\frac1{(2m+1)^2},
\]

and the exact recurrence is

\[
T_m+T_{m+1}=\frac1{(2m+1)^2}.
\]

The extra factor \(1/(2m+1)\) in \(u_m\) is load-bearing: it creates the
Cauchy denominator \(2(i+j)+1\) after the recurrence is inserted.

## 3. The residual matrix and full column rank

Choose positive integers \(B>S\), and put

\[
\Pi_i=\prod_{h=1}^{B}(2(h+i)+1)^2.
\]

For \(0\le a\le S+2\) and \(1\le j\le S\), define

\[
R_{a,j}
 =\sum_{i=0}^{a+2B}
   (-1)^i\binom{a+2B}{i}\Pi_i u_{i+j}.
\]

Theorem 2.1 claims \(\operatorname{rank}R=S\).

The recurrence expresses

\[
T_{i+j}=(-1)^jT_i+
 \sum_{0\le k<j}\frac{(-1)^{j-1-k}}{(2(i+k)+1)^2}.
\]

After multiplication by \(\Pi_i/(2(i+j)+1)\), the second term is a polynomial
in \(i\) of degree at most \(2B-3\). The finite difference of order
\(a+2B\) kills it. Thus each residual is controlled by the tail part.

Suppose a nonzero column vector \(\lambda\) lies in the right kernel and set

\[
f_i=\Pi_i\sum_{j=1}^{S}\lambda_j u_{i+j}.
\]

The vanishing residuals force all Newton coefficients of orders
\(2B,\ldots,2B+S+2\) to vanish. Hence the interpolation polynomial through the
relevant \(f_i\) has degree at most \(2B-1\).

The paper then obtains

\[
f_i=T_iD_\lambda(i)+P_\lambda(i),
\]

where \(\deg D_\lambda\le2B-1\) and
\(\deg P_\lambda\le2B-3\). Let \(A=f-P_\lambda\). The recurrence implies that

\[
K(X)=(2X+3)^2\big(A(X)D_\lambda(X+1)
                    +A(X+1)D_\lambda(X)\big)
      -D_\lambda(X)D_\lambda(X+1)
\]

vanishes at many consecutive nonnegative integers and has an additional
large fixed polynomial divisor. A zero count would force
\(\deg K\ge4B+1\), while construction gives \(\deg K\le4B\), unless
\(K\equiv0\).

If \(K\equiv0\), then \(R=A/D_\lambda\) would satisfy

\[
R(X)+R(X+1)=\frac1{(2X+3)^2}.
\]

After translation this becomes

\[
S_0(z)+S_0(z+1)=\frac1{4z^2}.
\]

No rational function satisfies this: a rightmost pole must be at zero, while
a leftmost pole must be at one. The polynomial case is immediately
impossible because the right side has a pole. This proves full column rank
and yields an \(S\times S\) nonzero minor.

## 4. Newton completion and the fixed scalar

Let \(A\subset\{0,\ldots,S+2\}\) be an \(S\)-element row set with nonzero
minor, and let its complement be \(\{c_1,c_2,c_3\}\). Put

\[
N=2B+S+3.
\]

The undefined symbol `D` in the source is forced to mean \(2B\). The square
matrix \(\widetilde A_B\) has:

1. reference columns \(i^r\), \(0\le r<2B\);
2. target columns \(\Pi_i u_{i+j}\), \(1\le j\le S\);
3. auxiliary Newton columns \(\binom{i}{2B+c_t}\), \(1\le t\le3\).

After the lower-triangular finite-difference transform:

- the reference block is triangular with pivots \(r!\);
- the target block on the remaining rows is \(R\);
- the three auxiliary columns become unit vectors in the omitted residual
  rows.

Therefore

\[
\det\widetilde A_B=\pm F_B\det R[A,J],
\qquad
F_B=\prod_{r=0}^{2B-1}r!.
\]

Dividing row \(i\)'s reference and auxiliary entries by \(\Pi_i\) produces a
new determinant

\[
\widehat q_B
 =\pm\frac{F_B\det R[A,J]}{\prod_{i=0}^{N-1}\Pi_i}.
\]

It is nonzero. If \(G=a/q\in\mathbb Q\), then all \(u_m\) are rational, so
\(\widehat q_B\in\mathbb Q^\times\).

Let \(H_B^{\min}\) be the positive denominator of \(q^S\widehat q_B\).
Then

\[
0\ne q^S H_B^{\min}\widehat q_B\in\mathbb Z.
\]

The remainder of the proof tries to make this integer smaller than one.

## 5. Pascal-Cauchy factorization

The matrix \(qR[A,J]\) factors as

```text
Pascal matrix × diagonal tail/clearing matrix × Cauchy matrix.
```

Cauchy-Binet gives

\[
q^S\det R[A,J]=\sum_{|I|=S}\Xi_I.
\]

For \(I=\{i_1<\cdots<i_S\}\), the Pascal alternant contributes

\[
\det\!\left[\binom{a+2B}{i_\nu}\right]
 =
\frac{V(I)\Psi_A(I)\prod_{a\in A}(a+2B)!}
     {\prod_{i\in I}i!(N-1-i)!},
\]

up to sign, where \(\Psi_A(I)\in\mathbb Z\). The Cauchy determinant contributes

\[
\det\!\left[\frac1{2(i_\nu+j)+1}\right]
 =
\pm
\frac{2^{S(S-1)}V(I)V(J)}
{\prod_{\nu,j}(2(i_\nu+j)+1)}.
\]

Thus every summand has **two** copies of \(V(I)\). This doubles the collision
valuation

\[
v_p(V(I)^2)
 =2\sum_{\nu\ge1}\sum_{r\bmod p^\nu}
   \binom{n_{p^\nu,r}(I)}2.
\]

The three surplus Newton rows also control the otherwise omitted Pascal
factor. If \(A^c=\{c_1,c_2,c_3\}\), the alternant quotient has total
\(I\)-degree

\[
\sum_{t=1}^3c_t-3\le3S.
\]

This gives a natural route to the needed
\(\log|\Psi_A(I)|=O(B\log B)=o(B^2)\) bound, but that bound is not stated in
the v1 proof.

## 6. Local prime-power layers

For \(Q=p^\nu\) odd, the paper defines:

- a denominator layer \(a_{Q,B}\);
- a complete local summand layer \(\lambda^A_Q(I)\);
- its minimum
  \(m^A_{Q,B}=\min_{|I|=S}\lambda^A_Q(I)\).

The tail denominators satisfy

\[
v_p(qT_{i+1})
 \ge -2\sum_{\nu\ge1}\mathbf1_{p^\nu\le2i+1}.
\]

Together with the factorials, clearing products, Cauchy denominator, and the
double Vandermonde, this gives

\[
v_p(\Xi_I)\ge\sum_{\nu\ge1}\lambda^A_{p^\nu}(I),
\]

and therefore

\[
v_p(q^S\det R[A,J])
 \ge\sum_{\nu\ge1}m^A_{p^\nu,B}.
\]

This is a lower bound on the determinant valuation obtained without assuming
that one Cauchy-Binet term dominates the sum.

## 7. The same-scalar positive-part bridge

Theorem 5.1 aims to prove, in the final regime \(S\le B/20\),

\[
a_{Q,B}\ge m^A_{Q,B}
\]

for every odd prime power \(Q\).

It uses the test set \(I=\{0,\ldots,S-1\}\). The remaining inequality is
reduced to a collision estimate involving

\[
\Phi_Q(n)=\sum_{r=0}^{n-1}\left\lfloor\frac rQ\right\rfloor.
\]

Balanced residue occupancy minimizes collision counts, yielding the sufficient
inequality

\[
2\big(\Phi_Q(3B+3)-\Phi_Q(2B+3)-\Phi_Q(B)\big)
 \ge \Phi_Q(2B+S+3)+2\Phi_Q(S).
\]

The paper proves this from

\[
0\le
\Phi_Q(n)-\left(\frac{n^2}{2Q}-\frac n2\right)
\le\frac Q8
\]

and the restriction \(S\le B/20\).

Combining local saturation with the valuation lower bound gives

\[
\log H_B^{\min}
 \le
 \sum_{\substack{p\ {\rm odd}\\\nu\ge1}}
 \big(a_{p^\nu,B}-m^A_{p^\nu,B}\big)\log p.
\]

This is the central structural achievement: it bounds the denominator of the
**same determinant scalar** later bounded at the real place.

For \(p=2\), the clearing products are odd and the residual entries are
2-integral after multiplication by \(q\). The positive-part denominator
contribution is exactly zero.

## 8. Ideal-row stability

The actual square completion has upper row index

\[
U=2B+S+2,
\]

while the clean limiting model uses

\[
U_0=2B+S-1.
\]

Lemma 5.5 claims that replacing one by the other changes each local minimum
and denominator layer by

\[
O(1+B/Q)
\]

and changes the logarithmically weighted total by \(o(B^2)\).

The local replacement argument is plausible: only three rows are added, and a
minimizer using them can be exchanged with unused common rows. For a complete
proof one needs explicit constants, a correct linear support cutoff, and
uniform control of the Pascal alternant and real-place terms.

## 9. Small odd prime powers

Set \(\rho=S/B\), eventually \(\rho=1/20\), and \(t=Q/B\). The paper derives a
limiting marginal ladder and a quantile functional \(K_v\). The local density
has a singular coefficient

\[
A_\rho=2\rho-\frac{\rho^2}{2}.
\]

After subtracting \(A_\rho/t\), the finite odd-prime correction is

\[
I_{\rm odd}
 =\rho^2\int_0^1
 \left[
 -\frac52\zeta(2,1+v)+Q_0(v)\zeta(3,1+v)
 \right]\,dv.
\]

At \(\rho=1/20\), the paper claims the directed enclosure

\[
-0.006276744728100982604597600317605549
 < I_{\rm odd}
 < -0.006276744728100982604597600317605548.
\]

Thus

\[
c_{\rm odd}=-I_{\rm odd}
 =0.006276744728100982604597600317605548503\ldots.
\]

The breakpoint set has 238 raw cells and 178 merged formulas. The paper
describes a rational outward-rounding certificate using recurrence shifts and
Euler-Maclaurin expansions through \(B_{24}\), but the actual table is absent.

## 10. Middle primes

For \(S<p<B\), only the first p-adic layer contributes asymptotically. Each
residue class has ordered base costs \(c_{r,k}\), and choosing its \(k\)-th
element costs

\[
\mu_{r,k}=c_{r,k}+2(k-1).
\]

The minimum is obtained by selecting the lowest total \(S\) marginal levels.
After scaling \(p/B=t\), the paper obtains a piecewise affine density
\(E_\rho(t)\). For \(\rho=1/20\),

\[
\Lambda_{\rm mid}
 =\int_{1/20}^{1}E_{1/20}(t)\,dt
\]

is claimed to equal exactly

\[
\frac{
33042423784278900654572890582560690565493664595111
}{
187362234062518051579626183549876762148305272280000
}
\]

and hence

\[
\Lambda_{\rm mid}
 =0.1763558379286482956996630430101674632453\ldots.
\]

The source says the exact partition has 235 affine cells, but does not include
the partition.

## 11. Large primes

For \(B<p<(2+\rho)B\), the local density simplifies to seven linear pieces.
Direct integration gives the improvement over the raw Cauchy-tail baseline:

\[
\Delta_{>B}=\frac23\rho+\frac12\rho^2.
\]

At \(\rho=1/20\),

\[
\Delta_{>B}=\frac{83}{2400}.
\]

Higher prime powers in the middle and large ranges contribute only \(o(B^2)\).

## 12. The final same-scalar ledger

The paper invokes

\[
\sum_{p^\nu\le x}\frac{\log p}{p^\nu}
 =\log x-\gamma+o(1)
\]

and the PNT scaling limit

\[
\frac1B\sum_{p^\nu\le cB}(\log p)f(p^\nu/B)
 \longrightarrow\int_0^c f(t)\,dt.
\]

Proposition 9.5 claims

\[
\log H_B^{\min}+\log|\widehat q_B|
 \le
 \left(
 \frac{39}{200}
 +c_{\rm odd}
 -\Lambda_{\rm mid}
 -\frac{83}{2400}
 \right)B^2+o(B^2).
\]

The exact arithmetic gives a negative coefficient smaller than

\[
-0.00966242652523235.
\]

Assuming \(G=a/q\in\mathbb Q\), let

\[
N_B=q^S H_B^{\min}\widehat q_B.
\]

Then \(N_B\in\mathbb Z\setminus\{0\}\), while

\[
\log|N_B|
 \le S\log q-\delta_0B^2+o(B^2)\to-\infty.
\]

For large \(B\), this gives \(0<|N_B|<1\), a contradiction.

## 13. What is genuinely new if correct

The novelty is not merely a better rational approximant. It is the exact
coordination of four layers around one scalar:

1. recurrence-driven nonvanishing;
2. Pascal-Cauchy determinant geometry;
3. local prime-power saturation of the determinant denominator;
4. an archimedean estimate whose leading terms cancel against the same local
   denominator baseline.

This “same-scalar” discipline is the main reusable mechanism.
