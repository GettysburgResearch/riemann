# L-91108 — The equality weight and SHARP scalar form a two-state square-root renewal

Claim ID: `L-91108` (provisional research range)  
Title: The endpoint equality weight and one continuous Möbius reserve satisfy parallel positive renewals; the all-depth SHARP scalar is exactly their positive linear combination, and the complete factor-\(54.2\) reset window lies strictly inside their common positive cone  
Status: **PROPOSED COMPLETE EXACT TWO-STATE / FINITE-WINDOW THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Date: 2026-08-11  
Depends on: `L-91107`; PR #347 `L-32314`; finite Möbius identities  
Scope: exact state factorization and finite-window positivity; no global sign theorem and no RH conclusion

## 1. Three Möbius prefixes

For real \(x\ge1\), put
\[
 A(x)=\sum_{n\le x}\frac{\mu(n)}{\sqrt n},
 \qquad
 B(x)=\sum_{n\le x}\frac{\mu(n)}n.
\tag{L-91108.1}
\]

Retain the endpoint equality weight of `L-91107`,
\[
\boxed{
 L(x)=2\sqrt x\,B(x)-A(x),
}
\tag{L-91108.2}
\]
and define the continuous reserve
\[
\boxed{
 R(x)=\sqrt x\,B(x)-A(x).
}
\tag{L-91108.3}

The all-depth SHARP scalar of PR #347 is
\[
\boxed{
 \Psi(x)=4\sqrt x\,B(x)-3A(x).
}
\tag{L-91108.4}

The three states satisfy the exact algebra
\[
\boxed{
 \Psi(x)=L(x)+2R(x).
}
\tag{L-91108.5}

Thus the critical SHARP sign is a positive combination of the endpoint equality state and one additional reserve.

## 2. The reserve is continuous and has a positive-integral form

At an integer \(N\), both \(\sqrt xB(x)\) and \(A(x)\) jump by
\[
 \frac{\mu(N)}{\sqrt N}.
\]
Their difference is therefore continuous:
\[
\boxed{
 R\in C([1,\infty)).
}
\tag{L-91108.6}

Between consecutive integers, \(A,B\) are constant and
\[
\boxed{
 R'(x)=\frac{B(x)}{2\sqrt x}.
}
\tag{L-91108.7}

Partial summation gives
\[
 A(x)
 =\sqrt x\,B(x)
 -\frac12\int_1^x\frac{B(t)}{\sqrt t}\,dt.
\]
Hence
\[
\boxed{
 R(x)=\frac12\int_1^x\frac{B(t)}{\sqrt t}\,dt.
}
\tag{L-91108.8}

In particular, no arithmetic jump remains in \(R\); all parity impulses have been integrated once.

## 3. Exact differential factorization of SHARP

From (L-91108.7),
\[
 \sqrt x\,B(x)=2xR'(x).
\]
Using \(A=\sqrt xB-R\),
\[
\boxed{
 \Psi(x)=2xR'(x)+3R(x)
 =\frac2{\sqrt x}\frac d{dx}
 \left[x^{3/2}R(x)\right].
}
\tag{L-91108.9}
on every open arithmetic cell. Since \(R\) is continuous, the final expression has no delta mass at the knots and agrees with the right-derivative convention of `L-32314`.

Equivalently,
\[
\boxed{
 \Psi(x)\ge0
 \iff
 x^{3/2}R(x)\text{ is nondecreasing}.
}
\tag{L-91108.10}

This is the continuous-state form of all-depth SHARP. It should not be confused with monotonicity of the discontinuous equality weight \(L\).

## 4. Parallel positive renewal equations

`L-91107` proves
\[
\boxed{
 \sum_{d\le x}\frac1{\sqrt d}L(x/d)
 =2\sqrt x-1.
}
\tag{L-91108.11}

The reserve satisfies the companion identity
\[
\boxed{
 \sum_{d\le x}\frac1{\sqrt d}R(x/d)
 =\sqrt x-1.
}
\tag{L-91108.12}

Indeed, substituting (L-91108.3),
\[
\begin{aligned}
&\sum_{d\le x}d^{-1/2}R(x/d)\\
&=\sum_{dn\le x}
 \frac{\mu(n)}{\sqrt{dn}}
 \left(\sqrt{\frac{x}{dn}}-1\right)\\
&=\sum_{m\le x}\frac1{\sqrt m}
 \left(\sqrt{\frac xm}-1\right)
 \sum_{n\mid m}\mu(n)\\
&=\sqrt x-1.
\end{aligned}
\]

Thus the vector state
\[
\boxed{
 \mathbf U(x)=\binom{L(x)}{R(x)}
}
\tag{L-91108.13}
obeys one positive diagonal renewal with positive forcing:
\[
\boxed{
 \sum_{d\le x}d^{-1/2}\mathbf U(x/d)
 =
 \binom{2\sqrt x-1}{\sqrt x-1}.
}
\tag{L-91108.14}

The RH-bearing output is the positive functional
\[
\boxed{
 \Psi=(1,2)\mathbf U.
}
\tag{L-91108.15}

The sign difficulty is therefore not hidden in an indefinite output matrix. It lies in propagating the positive cone of the two renewal states beyond the certified reset window.

## 5. Mellin symbols

For \(\Re s>1/2\), direct one-term integration gives
\[
\boxed{
 \int_1^\infty R(x)x^{-s-1}\,dx
 =\frac1{2s(s-\frac12)\zeta(s+\frac12)}.
}
\tag{L-91108.16}

The equality weight has symbol
\[
\boxed{
 \int_1^\infty L(x)x^{-s-1}\,dx
 =\frac{s+\frac12}
 {s(s-\frac12)\zeta(s+\frac12)}.
}
\tag{L-91108.17}

Their positive combination gives
\[
 \frac{s+\frac32}
 {s(s-\frac12)\zeta(s+\frac12)},
\]
which is exactly the transform of \(\Psi\) in PR #347.

Thus \(L\) and \(R\) split the critical numerator \(s+3/2\) into two positive-state channels.

Global eventual one-sign of either nontrivial channel is conclusion-producing; no such global sign is asserted.

## 6. Directed positivity on the reset window

Let \(c_0\) be the one-crossing constant of `L-91106`:
\[
 0.01844367547103<c_0<0.01844367547105.
\]
Then
\[
 1\le x\le c_0^{-1}<54.2192.
\]

The directed certificate `X-91102` already proves
\[
\boxed{
 L(x)>0.3186
 \qquad(1\le x\le c_0^{-1}).
}
\tag{L-91108.18}

The same cell-endpoint calculation gives
\[
\boxed{
 R(1)=0,
 \qquad
 R(x)>\sqrt2-1>0.4142
 \quad(2\le x\le c_0^{-1}).
}
\tag{L-91108.19}

On \(1<x<2\), the exact first cell has
\[
 R(x)=\sqrt x-1>0.
\]
Therefore
\[
\boxed{
 \mathbf U(x)\in\mathbb R_{\ge0}^2
 \qquad(1\le x\le c_0^{-1}),
}
\tag{L-91108.20}
with strict interior positivity away from \(x=1\).

Consequently
\[
\boxed{
 \Psi(x)>0
 \qquad(1\le x\le c_0^{-1}).
}
\tag{L-91108.21}

This finite-window SHARP positivity is consistent with, but much weaker in depth than, the separately proved outer-\(255/256\) finite SHARP theorem. Its value is the exact alignment with the endpoint equality-reset crossing and the shared two-state recurrence.

## 7. The reset programme in two-state form

A factor-\(54.2\) reset should not attempt to preserve the raw Möbius prefixes \(A,B\) separately. It should propagate the positive state
\[
 (L,R)
\]
and the positive output \(L+2R\).

The proposed all-generation mechanism is:

```text
within one reset window:
    realize the positive equality state L by endpoint-shadow packets;
    retain the continuous reserve R as the capacity/curvature budget;

at the inner splice:
    recombine the quotient collars by compact butterflies;
    transfer the residual pair (L,R) to the contracted scale;

across generations:
    use only the positive renewal forcing and the output L+2R;
    prove a coefficient-one cone recurrence with bounded collar debt.
```

If a reset operator preserves the cone \(\mathbb R_{\ge0}^2\) and incurs \(O(1)\) score debt per generation, the scale contracts by more than \(54\), so the total debt is \(O(\log X)\). PR #352 then converts this to RH.

The cone-preserving reset operator remains open.

## 8. Proof boundary

Closed exactly, subject to review:

1. continuity and integral representation of \(R\);
2. the factorization \(\Psi=L+2R\);
3. the differential identity through \(x^{3/2}R\);
4. the two parallel positive renewal equations;
5. the critical Mellin-symbol split;
6. strict two-state positivity on the full reset window;
7. the positive-cone formulation of the remaining recurrence.

Still open:

1. a finite collar map preserving the \((L,R)\) cone;
2. a coefficient-one factor-\(54\) state recurrence;
3. bounded per-generation score debt;
4. RH.
