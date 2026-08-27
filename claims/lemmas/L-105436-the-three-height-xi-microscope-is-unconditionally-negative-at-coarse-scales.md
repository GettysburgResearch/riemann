# L-105436 — The three-height Xi microscope is unconditionally negative at coarse scales

Claim ID: `L-105436`  
Status: **PROVED UNCONDITIONALLY FROM THE SAFE-HALF-PLANE BELL ASYMPTOTIC — INDEPENDENT REVIEW REQUESTED**  
Created: 2026-08-24  
Depends on: `L-105430`, `L-105435`  
RH status: **not assumed**

Fix one derivative order `r>=0` and use

\[
m_r(z)={\Xi^{(r)}(z)\over\Xi^{(r+1)}(z)}
\]

and the three-height field

\[
\mathcal P_r(a,h)
=-{3\over2}\Im m_r(a+ih)
+{6\over5}\Im m_r(a+2ih)
-{3\over10}\Im m_r(a+3ih).
\]

Then there is `H_r^*>0` such that

\[
\boxed{
\mathcal P_r(a,h)<0
\qquad(a\in\mathbb R,\ h\ge H_r^*).
}
\tag{L-105436.1}

The inequality is uniform in the real centre.

## 1. Three safe-line logarithmic derivatives

Put

\[
s_j={1\over2}+jh-ia,
\qquad j=1,2,3,
\]

and

\[
L_j={\xi'\over\xi}(s_j).
\]

The Bell-polynomial calculation of `L-105430` gives

\[
\boxed{
\Im m_r(a+jih)
=\Re {1\over L_j}
+O_r(|L_j|^{-3}).
}
\tag{L-105436.2}

Uniform Stirling and the absolutely convergent zeta series give

\[
L_j
={1\over2}\Log {s_j\over2\pi}+O(1),
\tag{L-105436.3}
\]

uniformly for `h` large and all real `a`.

Let

\[
\Lambda={1\over2}\Log {s_1\over2\pi}.
\]

Since `|s_j/s_1|` lies between fixed positive constants and the arguments
remain in the right half-plane,

\[
\boxed{L_j=\Lambda+O(1)}
\tag{L-105436.4}
\]

uniformly in `a,h,j`. Moreover

\[
\Re\Lambda\longrightarrow\infty
\]

uniformly as `h->infinity`, while `|Im Lambda|<=pi/4+O(1/Re Lambda)`. Hence

\[
\boxed{
\Re {1\over\Lambda}
\ge {c\over|\Lambda|}>0.
}
\tag{L-105436.5}

## 2. The coefficient sum supplies the sign

From (L-105436.2)--(L-105436.4),

\[
\Im m_r(a+jih)
=\Re {1\over\Lambda}
+O_r(|\Lambda|^{-2})
\tag{L-105436.6}
\]

for all three heights. Since

\[
-{3\over2}+{6\over5}-{3\over10}=-{3\over5},
\]

one obtains

\[
\boxed{
\mathcal P_r(a,h)
=-{3\over5}\Re {1\over\Lambda}
+O_r(|\Lambda|^{-2}).
}
\tag{L-105436.7}

Equation (L-105436.5) makes the main term dominate uniformly once `h` is
large. This proves (L-105436.1).

A quantitative form is

\[
\boxed{
\mathcal P_r(a,h)
\le
-{c_r\over
 \log(3+\sqrt{a^2+h^2})}
}
\tag{L-105436.8}

for `h>=H_r^*`, after reducing `c_r`.

## 3. Interpretation

`L-105435` shows that

\[
\rho_c=\lim_{h\downarrow0}h\mathcal P_r(c,h).
\]

The present theorem proves the desired sign at the opposite end of the scale
axis. Therefore the complete Xi critical-sign problem is now a scalar
scale-descent problem:

```text
coarse scale h>=H_r^*        strictly negative unconditionally;
fine scale h down to zero    open;
residue sign                 fine-scale limit.
```

No determinant or selected critical point occurs in the coarse theorem.

## 4. Scope

Negativity at large `h` does not propagate backward under smoothing without an
additional variation-diminishing or scale-monotonicity theorem. The quartic
separator in `R-105430` can have favorable coarse behaviour while retaining a
positive fine-scale residue. The missing scale-descent mechanism remains
RH-bearing.
