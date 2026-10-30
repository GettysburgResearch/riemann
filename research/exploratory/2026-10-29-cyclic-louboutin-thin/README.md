# Cyclic transfer in a thinner height range

**Status:** Proposed deduction from published theorems; independent review is requested. The cited Hecke, Dedekind and Stark results are inputs, not reproved. This is a companion to the [cyclic transfer note](../2026-10-29-cyclic-transfer/README.md), with a field-dependent height and no assumption that the fixed field has degree at least seven.

Let `K/k` be finite Galois, `H<=Gal(K/k)` cyclic of order `m>=3`, `M=K^H`, `F=K^(H²)`, and write `D=|disc(K/Q)|`, `d=|disc(M/Q)|`, `d0=|disc(F/Q)|`, `phi=phi(m)` and

```text
T = log D - (m-phi)log d.
```

Let `a=1/15.10` and set

```text
Delta = a phi/T.
```

If `F!=Q`, use the height constraints `|Im(s)|<=0.13` and `|Im(s)|<1/(2 log d0)`. If `F=Q`, use `|Im(s)|<=0.13`. In `Re(s)>1-Delta` subject to the corresponding height constraints, every irreducible Artin L-function of degree at least two and every nonreal one-dimensional factor is holomorphic and nonzero; at most one simple real zero among the real one-dimensional factors can remain. At `s=1`, the trivial factor has its pole and every nontrivial irreducible factor is nonzero. For a Galois extension of `Q` whose group has no quotient of order two, `zeta_K` itself is zero-free in the region, apart from its pole.

If `3` and `4` do not divide `m`, one can replace `a` by `.1149`. If `3` does not divide `m` but `4` divides `m`, one can replace it by `.1004`. These two constants are quoted from Ahn–Kwon in [Zaman (2016), equation (1.1)](https://arxiv.org/html/1502.05679); we have not checked the full original Ahn–Kwon proof. The basic constant and its height are in the [Ahn–Kwon abstract](https://doi.org/10.1016/j.jnt.2014.06.008).

## Proof

Choose a faithful character `lambda` of `H`, let `Q=N f_lambda`, and put `A=d Q`. The conductor–discriminant formula and the `phi` faithful powers of `lambda` give

```text
phi log A <= T.                                               (1)
```

Every power has conductor dividing `f_lambda`, so every nonreal character of `H` has conductor parameter at most `A`. The source Hecke estimates exclude its zeros in the stated region; the order-three input covers every nonreal character, and the sharper constants apply under the stated divisibility restrictions. The tower factorization

```text
zeta_K/zeta_F = product_(chi in H^, ord chi>2) L_M(s,chi)     (2)
```

is therefore holomorphic and nonzero there. Equation (1) shows the proposed width is contained in the individual Hecke rectangle.

For `F!=Q`, Ahn–Kwon's separate Dedekind theorem says `zeta_F` has at most one zero in `Re(s)>1-1/(2 log d0)`, `|Im(s)|<1/(2 log d0)`; any such zero is real and simple. Its bound is automatically wide enough here. If `m` is odd, `F=M`, so `d0=d<=A`. If `m` is even, `F/M` is quadratic and its associated character is a power of `lambda`; its conductor divides `f_lambda`, hence

```text
d0 <= d^2 Q <= (d Q)^2 = A^2,
log d0 <= 2 log A.                                           (3)
```

This also holds in the odd case. From (1), (3) and `a<=.1149`,

```text
Delta <= a/log A <= 2a/log d0 < 1/(2 log d0).                 (4)
```

Thus equation (2) transfers Ahn–Kwon's zero-order conclusion to `zeta_K`. Stark's low-order theorem makes the irreducible Artin factors holomorphic at every point in the region except the pole at 1. Their degree-weighted orders sum to zero or one; factors of degree at least two cannot vanish. At a real exceptional point, conjugate nonreal one-dimensional factors vanish together, so neither can be the lone zero. Classical Brauer–Hecke nonvanishing handles the nontrivial factors at 1.

When `F=Q`, the field inclusions force `M=k=Q` and `H²=H=G`, so `m` is odd. The faithful character is a nontrivial Dirichlet character and `A=Q>=2`. Equation (1) gives `Delta<=.1149/log 2<1/2`. The cited [Platt–Trudgian verification](https://doi.org/10.1112/blms.12460) and the real-axis sign exclude zeros of `zeta_Q` at `|t|<=.13` and `Re(s)>1/2`. Equation (2) then shows `zeta_K` has no zero in the stated region away from its pole. As `G` is cyclic of odd order, its nontrivial irreducibles are nonreal one-dimensional characters, which are directly covered by the Hecke estimate.

If `k=Q` and there is no quotient of order two, the only real one-dimensional factor is `zeta_Q`. We have `A>=2`: when `M!=Q` its discriminant is at least 2, while when `M=Q` the nontrivial faithful Dirichlet character has conductor at least 2. Thus (1) gives `Delta<=.1149/log 2<1/2`. The cited [Platt–Trudgian verification](https://doi.org/10.1112/blms.12460), together with the real-axis sign of `zeta_Q`, excludes its zeros at the stated height, completing the deduction.

For comparison, [Louboutin, Theorem 3](https://doi.org/10.7169/facm/1598), gives the wider Dedekind width `.59110/log d0` at the thinner heights `|t|<=1/(4 log d0)`, and `c2/log d0` on the real axis, where `c2=2(sqrt(2)-1)^2/(1-1/sqrt(5))=0.62075649...`; in each case the possible zero is real and simple. Both Dedekind bounds contain the present Hecke width by (4). For the no-quadratic Galois-over-Q case, Louboutin and Stark also give the independent real-axis width `c2/log D` directly; use the larger applicable width rather than treating this transfer as a universal improvement.

Louboutin's threshold height is `<=1/(4 log d0)`, not the reversed inequality appearing in a secondary summary. The Ahn–Kwon height inequality used in the theorem is strict. No new claim about all heights or the best-known fixed half-plane is made.
