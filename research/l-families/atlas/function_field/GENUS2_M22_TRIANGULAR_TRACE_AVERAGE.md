# Genus-two M22 triangular trace average

Status: **PROVED** by exact character-sum algebra for every odd prime power.

Scope: let \(q\) be an odd prime power and let \(\mathcal H_5(q)\) be the
monic squarefree quintics in \(\mathbf F_q[T]\). No finite field, curve, or
family member is enumerated. The replay is
`genus2_m22_triangular_trace_average.py`; its artifact is
`genus2_m22_triangular_trace_average.json`.

Exact dependencies: the 20 M22 signatures are locked to
`genus2_second_moment_reduction.json`. The primitive conductor averages and
composite-denominator deletion convention are locked to the independently
proved B3 packet `GENUS2_B3_PRIMITIVE_TRACE_AVERAGE.md`. The lower moments
are locked to `GENUS2_MOMENT_IDENTITY.md`.

## 1. The theorem

For every odd prime power \(q\),

\[
\boxed{
 \sum_{D\in\mathcal H_5(q)}a_D^2b_D^2
 =q(q-1)(q+1)
  \left(5q^5-19q^4+29q^3-5q^2-21q-3\right).
}
\tag{1}
\]

Since \(\#\mathcal H_5(q)=q^4(q-1)\),

\[
\boxed{
 \mathbb E[a_D^2b_D^2]
 =\frac{(q+1)(5q^5-19q^4+29q^3-5q^2-21q-3)}{q^3}.
}
\tag{2}
\]

This closes the `M22-TRIANGULAR-TRACE-AVERAGE` target from the high-weight
channel packet. It is a symbolic all-field identity, not a continuation
fitted to \(q=3,5,7\).

## 2. Why the B3 primitive lemma is exactly reusable

Expanding

\[
 a_D^2b_D^2
 =\sum_{L_1,L_2\in\mathcal M_1}
   \sum_{f_1,f_2\in\mathcal M_2}
   \left(\frac{D}{L_1L_2f_1f_2}\right)
\tag{3}
\]

again produces monic degree-six denominators supported only on linear and
irreducible-quadratic primes. The squarefree sieve is unchanged:

\[
 S_5(h)
 =C_5(h)-(q-l)C_3(h)
  +\left(\binom{l+1}{2}+k-ql\right)C_1(h).
\tag{4}
\]

Only the tuple weights change. B3 had three ordered monic-quadratic slots;
M22 has two ordered monic-linear and two ordered monic-quadratic slots.

The composite-denominator convention remains load-bearing. An even exponent
does not remove the local zero on multiples of that prime. Such a prime stays
in the deletion set

\[
 L_h(u)=L_{r(h)}(u)
 \prod_{P\in E(h)}
 \left(1-\left(\frac P{r(h)}\right)u^{\deg P}\right).
\tag{5}
\]

Consequently each M22 row depends on exactly the same conductor-type sums
already proved in B3:

\[
 \sum_r s_1(r),\qquad
 \sum_r s_1(r)^2,\qquad
 \sum_r s_2(r),\qquad
 \sum_r p_1(r),\qquad
 \sum_r p_2(r),
\]

together with the same degree-two and marked degree-four deletion sums. No
new primitive average is guessed, sampled, or fitted.

## 3. Exhausting the 20 signatures

The source-locked signature ledger has radical-degree census

\[
 (4,8,5,3)
 \quad\text{in degrees}\quad
 (0,2,4,6).
\]

Its weighted type-count polynomials sum coefficientwise to \(q^6\), the
number of ordered choices of two monic linears and two monic quadratics. The
rowwise squarefree-sieve contributions group as follows.

| \(\deg r\) | contribution to \(\sum_Da_D^2b_D^2\) |
|---:|---:|
| 0 | \(6q^8-32q^7+97q^6-219q^5+407q^4-579q^3+504q^2-184q\) |
| 2 | \(63q^5-559q^4+1897q^3-2801q^2+1400q\) |
| 4 | \(8q^7-87q^6+354q^5-367q^4-1463q^3+4132q^2-2577q\) |
| 6 | \(-q^8+5q^7+14q^6-184q^5+469q^4+147q^3-1814q^2+1364q\) |

Their coefficientwise sum is

\[
 5q^8-19q^7+24q^6+14q^5-50q^4+2q^3+21q^2+3q,
\]

which factors as the right side of (1). The JSON retains all 20 row-level
\(C_1,C_3,C_5,S_5\) polynomials and tuple weights.

## 4. Triangular character consequences

The exact pointwise identity is

\[
\begin{aligned}
 R_{22}
 &=\chi_{0,3}+\chi_{2,2}\\
 &=\frac{a_D^2b_D^2}{q^3}
   -\frac{3a_D^2b_D}{q^2}
   -\frac{a_D^4}{q^2}
   +\frac{5a_D^2}{q}-1.
\end{aligned}
\tag{6}
\]

Substituting (1) and the proved \(a_D^2b_D,a_D^4,a_D^2\) moments gives

\[
\boxed{
 \mathbb E[R_{22}]
 =\frac{q^4+2q^3-q^2-4q-3}{q^6}.
}
\tag{7}
\]

The source-locked B3 theorem proves

\[
 \mathbb E[\chi_{0,3}]=\frac{q^4-2q-1}{q^6}.
\]

Subtracting it from (7) gives the second high-weight character:

\[
\boxed{
 \mathbb E[\chi_{2,2}]
 =\frac{2q^3-q^2-2q-2}{q^6}.
}
\tag{8}
\]

Since \(\chi_{2,2}\) has weight six, the marked-Weierstrass stack trace is

\[
\boxed{
 T_{2,2}(q)
 =\frac{q^3}{q(q-1)}
   \sum_{D\in\mathcal H_5(q)}\chi_{2,2}(U_D)
 =2q^3-q^2-2q-2.
}
\tag{9}
\]

## 5. Replay and boundaries

From the successor worktree root:

```text
python research/l-families/atlas/function_field/genus2_m22_triangular_trace_average.py --check
python -O research/l-families/atlas/function_field/genus2_m22_triangular_trace_average.py --check
python -m unittest tests.test_genus2_m22_triangular_trace_average
python -O -m unittest tests.test_genus2_m22_triangular_trace_average
```

The producer uses exact `Fraction` polynomial algebra. It consumes 20
signature atoms and seven primitive conductor types under a declared cap of
4096 complete-polynomial operations plus input atoms.

This is an exact finite-field family moment. It proves no memberwise sign and
makes no external novelty, motive, Euler-product, RH, or GRH claim. The
smallest invalidating point is a failure of the source-locked primitive sign
inventories, one of the 20 slot weights, the squarefree sieve (4), or the
triangular identity (6).
