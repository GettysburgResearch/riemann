# L-102733 — The centered radial cost is a sublinear source gauge

Claim ID: `L-102733`  
Status: **PROVED EXACT COMPOSITION THEOREM**  
Created: 2026-08-23  
Depends on: `L-102731--L-102732`; `T-102760`  
RH status: **not assumed**

For a carrier-subtracted filtered disk triple

\[
 v=(A,B,C),
\]

where `C=P_0^circ`, define

\[
 \mathfrak R(v)
 =
 \inf
 \left\{
 \frac{255}{64}\lambda+\frac1{16}(C+\eta):
 \lambda,\eta\ge0,
 \begin{pmatrix}
 A+\lambda&B\\
 B&C+\eta-\lambda/4
 \end{pmatrix}\succeq0
 \right\}.
 \tag{L-102733.1}
\]

The lower-right PSD condition implies `C+eta>=lambda/4`, so every admissible
cost is nonnegative.

## 1. Positive homogeneity

For `t>=0`, scaling a feasible pair `(lambda,eta)` by `t` gives a feasible pair
for `tv` with cost multiplied by `t`. Therefore

\[
 \boxed{\mathfrak R(tv)=t\mathfrak R(v).}
 \tag{L-102733.2}
\]

## 2. Subadditivity

Let `(lambda_i,eta_i)` be feasible for `v_i=(A_i,B_i,C_i)`.  Adding the two PSD
matrices shows that

\[
 (\lambda_1+\lambda_2,\eta_1+\eta_2)
\]

is feasible for `v_1+v_2`.  The costs add exactly. Hence

\[
 \boxed{
 \mathfrak R(v_1+v_2)
 \le
 \mathfrak R(v_1)+\mathfrak R(v_2).
 }
 \tag{L-102733.3}
\]

Thus `mathfrak R` is a convex, sublinear gauge on the exact filtered source
coordinates.

## 3. A deterministic norm bound

Choose

\[
 \lambda=|A|+|B|+4|C|,
\]

and

\[
 \eta=|B|+|C|+\lambda/4.
\]

Then

\[
 A+\lambda\ge|B|,
\]

and

\[
 C+\eta-\lambda/4=C+|C|+|B|\ge|B|.
\]

The resulting matrix is PSD because its two diagonal entries are at least
`|B|`. Therefore

\[
 \boxed{
 \mathfrak R(A,B,C)
 \le
 4|A|+\frac{65}{16}|B|+\frac{129}{8}|C|.
 }
 \tag{L-102733.4}
\]

## 4. Exact source-region functoriality

Suppose the literal carrier-recombined tangent source has a one-use partition

\[
 v=
 v_{\rm square}
 +v_{\rm pp}
 +v_{\rm same}
 +v_{\rm act}
 +v_{\rm bal}.
\]

Then

\[
 \boxed{
 \mathfrak R(v)
 \le
 \sum_{\mathcal R}\mathfrak R(v_{\mathcal R}).
 }
 \tag{L-102733.5}
\]

No S-lemma slack or affine carrier is copied between regions.

By (L-102733.4), every region whose three centered coordinates have
polylogarithmic `L1` cost automatically has polylogarithmic radial cost.  The
results already proved on PR #719 therefore remove:

```text
squared completion;
higher prime powers;
same-product factor pairs;
duplicate owner representations;
same-owner square cores;
finite activation and gauge-transfer terms.
```

The only region not discharged by the existing bounds is the
carrier-recombined, distinct-product, different-owner balanced block.

Consequently `RSC102760` is equivalent, modulo polylogarithmic closed regions,
to the same physical cross-owner block isolated by `PHDNC102710` and
`HDNC102703`.