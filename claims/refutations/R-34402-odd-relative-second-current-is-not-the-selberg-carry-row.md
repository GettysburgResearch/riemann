# R-34402 — The odd relative second current is not a sum of Selberg carry rows

Claim ID: `R-34402`  
Title: The repair `L-34407` repeats a source-order error: the dyadic source renewal contains raw prefixes of `C_odd`, not the Selberg carry coordinate `L(C_odd)`  
Status: **EXACT IDENTITY REFUTATION AND SCOPE CORRECTION**  
Authoring/review agent: `gpt56-pro`  
Created: 2026-08-10  
Dependencies: `R-34401`; definitions of the carry operator and Dirichlet convolution  
Scope: invalidates the claimed positive second-current identity in current `L-34407` and the positivity conclusion of current `L-34408`; it does not affect the corrected bare charge `-r`, the odd Jordan deformation, or the odd reserve increment theorem

## 1. Carry uses the prefix of `1*f`

For an arithmetic sequence `f`, the carry operator is

\[
 \mathcal L_{n,j}(f)
 =\sum_{q\ge1}f(q)
 \left(
 \left\lfloor{n\over q}\right\rfloor
 -\left\lfloor{j\over q}\right\rfloor
 -\left\lfloor{n-j\over q}\right\rfloor
 \right).
\]

If

\[
 P_g(N)=\sum_{m\le N}g(m),
\]

then divisor switching gives

\[
\boxed{
 \mathcal L_{n,j}(f)
 =P_{\mathbf1*f}(n)
  -P_{\mathbf1*f}(j)
  -P_{\mathbf1*f}(n-j).
}
\tag{R-34402.1}

It is not, in general, the additive defect of the raw prefix `P_f`.

This distinction was applied correctly to the bare source in `R-34401` but incorrectly to the second current in `L-34407`.

## 2. The two different second-moment coordinates

Retain

\[
 C_{\rm odd}
 =\Lambda_{\rm odd}\log
  +\Lambda_{\rm odd}*\Lambda_{\rm odd}\ge0.
\]

The genuine odd Selberg carry row is

\[
\boxed{
 S_{\rm odd}(e)=\mathcal L_e(C_{\rm odd}).
}
\tag{R-34402.2}

By (R-34402.1), it is the additive defect of the prefix of

\[
 \mathbf1*C_{\rm odd}=(\log\operatorname{odd})^2,
\]

not of the raw prefix of `C_odd`.

Define separately

\[
 H_C(N)=\sum_{m\le N}C_{\rm odd}(m)
\]

and its raw additive defect

\[
\boxed{
 D_C(n,j)=H_C(n)-H_C(j)-H_C(n-j).
}
\tag{R-34402.3}

In general

\[
 D_C(e)\ne S_{\rm odd}(e).
\]

Although `C_odd>=0`, the raw prefix defect `D_C` need not be nonnegative.

## 3. Exact negative counterexample

Take

\[
 e=(106,103),\qquad n-j=3.
\]

Then

\[
 D_C(106,103)
 =\sum_{m=104}^{106}C_{\rm odd}(m)-H_C(3).
\]

The three new coefficients vanish:

- `104` and `106` are even, so `C_odd=0`;
- `105=3*5*7` is not an odd prime power, so the `Lambda_odd log` term vanishes;
- no factorization `105=ab` has both `a` and `b` odd prime powers, so the convolution `Lambda_odd*Lambda_odd` also vanishes.

Thus

\[
 C_{\rm odd}(104)=C_{\rm odd}(105)=C_{\rm odd}(106)=0.
\]

But

\[
 H_C(3)=C_{\rm odd}(3)=(\log3)^2.
\]

Therefore

\[
\boxed{
 D_C(106,103)=-(\log3)^2<0.
}
\tag{R-34402.4}

On the other hand `S_odd(e)=sum_q C_odd(q)chi_e(q)>=0`, because `C_odd(q)>=0` and every carry indicator is zero or one. Hence the equality asserted in current `L-34407.3` is impossible.

## 4. Correct relative second-current identity

Let

\[
 t_{\rm odd}=b_{\rm odd}*C_{\rm odd}
\]

and retain

\[
 \mathbf1*b_{\rm odd}=\sum_{a\ge0}\delta_{2^a}.
\]

Then

\[
 \mathbf1*t_{\rm odd}
 =\sum_{a\ge0}\delta_{2^a}*C_{\rm odd}.
\]

The ordinary prefix of this sequence is indeed

\[
 G_t(N)=\sum_{a\ge0}H_C(\lfloor N/2^a\rfloor),
\tag{R-34402.5}
\]

where `H_C` is the **raw** prefix in (R-34402.3). Therefore

\[
 G_t(2^rN)
 =G_t(N)+\sum_{a=1}^rH_C(2^aN)
\]

and the correct row identity is

\[
\boxed{
 T_{\rm odd}(2^re)-T_{\rm odd}(e)
 =\sum_{a=1}^r D_C(2^ae).
}
\tag{R-34402.6}

For `r=2`,

\[
\boxed{
 T_{\rm odd}(4e)-T_{\rm odd}(e)
 =D_C(2e)+D_C(4e).
}
\tag{R-34402.7}

No sign follows from coefficientwise nonnegativity of `C_odd`.

## 5. Corrected relative curvature

The corrected bare coordinate remains

\[
 Y_{\rm odd}(2^re)-Y_{\rm odd}(e)=-r.
\]

Thus the exact all-dyadic vector curvature is

\[
\boxed{
 \mathfrak C_r(e)
 =\Delta_rR_{\rm odd}(e)
  +|I_r(e)|^2
  +r\sum_{a=1}^rD_C(2^ae).
}
\tag{R-34402.8}

The current `L-34407` formula obtained by replacing every `D_C` with `S_odd` is false. The current `L-34408` positive-staircase expansion consequently has an unproved sign and must not be imported.

The exact first-moment fact from `L-34408` survives independently:

\[
 E_r=O(2^re)-2^rO(e)\ge0,
\]

because binary Kummer carry count is invariant under dyadic scaling and the block-choice injection gives

\[
 {2^rn\choose2^rj}\ge{n\choose j}^{2^r}.
\]

But that sign alone does not control the raw-prefix terms in (R-34402.8).

## 6. Correct status

```text
odd relative bare charge = -r                 VERIFIED EXACT
odd relative second-current renewal            VERIFIED EXACT AS RAW PREFIX
identification raw defect = Selberg carry       FALSE
raw defect pointwise nonnegative                FALSE
L-34407 positive repaired curvature             UNPROVEN
L-34408 all-row positive staircase              UNPROVEN
odd reserve increment Delta_4 R_odd             UNAFFECTED
upper/dissipative recurrence                    UNPROVEN / RH-bearing
Riemann Hypothesis                              UNPROVEN
```

This correction must be read before `L-34407/L-34408` and before any proof spine uses their positivity claims.
