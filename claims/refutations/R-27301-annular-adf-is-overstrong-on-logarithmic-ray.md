# R-27301 — The annular `L^2` frame is overstrong on the logarithmic ray

Claim ID: `R-27301`  
Title: The Annular Dual Frame bound would force an `X^{-3/2+o(1)}` prime-ramp error in the exact von-Mangoldt direction  
Status: **EXACT SCOPE CORRECTION — ADF RETAINED ONLY AS A STRONG SUFFICIENT ROUTE**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #273  
Parent: draft PR #267 at `6d370d5a8c1a2ab11eb1af0581fe3c605863a757`  
Depends on: PR #267 `L-26101`, `L-26105`; PR #271 `L-26701/L-26702`  
Scope: finite exact inequality; no RH conclusion

## 1. The logarithmic dual direction

Use the canonical annulus

\[
 I_X=\left[\left\lceil\frac X5\right\rceil,
           \left\lfloor\frac{4X}{5}\right\rfloor\right]
\]

and the prime-power divisor-gradient matrix

\[
 A_X(q,j)
 =2\mathbf 1_{q\mid j}
  -\mathbf 1_{q\mid j-1}
  -\mathbf 1_{q\mid j+1}.
\]

For the von-Mangoldt vector

\[
 \lambda_q=\Lambda(q),
\]

the complete prime-power divisor identity gives exactly

\[
\boxed{
 (A_X^*\Lambda)_j
 =2\log j-\log(j-1)-\log(j+1)
 =\log\frac{j^2}{j^2-1}.
}
\tag{R-27301.1}
\]

Let

\[
 \delta_X
 =
 J_X(b_X^{(0)})
 -
 \sum_{q=p^a\le X}
 \frac{\Lambda(q)}{\sqrt q}\log\frac Xq.
\tag{R-27301.2}
\]

Then

\[
 \langle\Lambda,r_X\rangle=\delta_X.
\tag{R-27301.3}
\]

This is the complete prime-ramp discrepancy, not a transverse frame
coordinate.

## 2. Directed annular norm ceiling

For every integer \(j\ge2\),

\[
0<
\log\frac{j^2}{j^2-1}
=
\log\left(1+\frac1{j^2-1}\right)
\le
\frac1{j^2-1}
\le
\frac2{j^2}.
\tag{R-27301.4}
\]

On \(I_X\), \(j\ge X/5\), and there are at most \(X\) indices. Hence,
for \(X\ge10\),

\[
\begin{aligned}
 \|A_X^*\Lambda\|_2^2
 &\le
 \sum_{j\in I_X}\frac4{j^4}\\
 &\le
 X\frac{4\cdot5^4}{X^4}
 =
 \frac{2500}{X^3}.
\end{aligned}
\]

Therefore

\[
\boxed{
 \|A_X^*\Lambda\|_2
 \le 50X^{-3/2}.
}
\tag{R-27301.5}
\]

## 3. Consequence for the annular repair radius

`L-26105` proves the exact Hilbert-Farkas formula

\[
 \mathcal R_X
 =
 \sup_{\substack{\lambda\ge0\\A_X^*\lambda\ne0}}
 \frac{\langle\lambda,r_X\rangle_+}
      {\|A_X^*\lambda\|_2}.
\]

Testing the admissible direction \(\lambda=\Lambda\) and using
(R-27301.5) gives

\[
\boxed{
 \mathcal R_X
 \ge
 \frac{X^{3/2}}{50}(\delta_X)_+.
}
\tag{R-27301.6}
\]

Consequently,

\[
\boxed{
 \mathcal R_X=X^{o(1)}
 \quad\Longrightarrow\quad
 (\delta_X)_+
 \le 50X^{-3/2+o(1)}.
}
\tag{R-27301.7}
\]

The square-screw/Landau consumer needs only

\[
(\delta_X)_+=X^{o(1)}.
\tag{R-27301.8}
\]

Thus `ADF` is quantitatively stronger than the canonical RH-facing scalar
target by a factor \(X^{3/2}\) in its exact near-null direction.  It remains a
valid sufficient theorem, but it should not be described as the unique or
minimal unresolved statement.

## 4. Relation to the affine boundary charge

PR #271 defines the least affine downward charge \(C_X\).  The normalized
von-Mangoldt dual ray gives

\[
\boxed{
 C_X\ge\frac{(\delta_X)_+}{\log X}.
}
\tag{R-27301.9}
\]

Conversely, any annular flow \(F\) produces a benchmark displacement

\[
 b_X^{(0)}(m)-b_F(m)=F_m-F_{m-1},
\]

so

\[
 \max_m(b_X^{(0)}(m)-b_F(m))_+
 \le2\|F\|_\infty
 \le2\|F\|_2.
\]

Taking infima yields

\[
\boxed{C_X\le2\mathcal R_X.}
\tag{R-27301.10}
\]

Therefore

```text
ADF -> affine boundary-charge control -> sharp prime ramp,
```

but the converse is neither asserted nor needed.

## 5. Corrected status

```text
annular Hilbert-Farkas identity       RETAINED EXACT
ADF as a sufficient theorem          RETAINED
ADF as the canonical sole hinge       WITHDRAWN
affine/local charge target            STRICTLY WEAKER INTERFACE
prime-ramp discrepancy                RH-BEARING
RH                                     UNPROVED
```

This is a scope correction, not a counterexample to `ADF`.
