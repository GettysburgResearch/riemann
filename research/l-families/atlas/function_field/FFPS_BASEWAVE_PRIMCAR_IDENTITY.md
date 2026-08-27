# The base divisor wavelet is exactly PRIMCAR

Status: **exact definition-comparison and corrected conditional gate
hierarchy; no analytic estimate and no proof of RH or GRH**

Bounded exact replay:
[`ffps_basewave_primcar_identity.py`](ffps_basewave_primcar_identity.py).
Canonical summary:
[`ffps_basewave_primcar_identity.json`](ffps_basewave_primcar_identity.json).

Frozen sources: the primitive incidence/Carleson and rho-tilt packets at
`b870366141fe8d5f43d5b81f6e50a67d2a888070`. The replay pins their exact
source blobs. This packet repairs the interpretation of definitions already
present at that head; it does not alter those definitions.

## 0. Outcome

For each of the three physical channels `alpha in {0,1,2}`, the coherent
core with `u=1` has only the divisor `r=1`. Therefore

\[
 \boxed{
 \mathcal C^\alpha_{d,1}(I)
 =\mathcal P^0_{67^\alpha,1}(d;I)
 =\mathcal P_I^{(\alpha,0)}(d).}
\tag{0.1}
\]

The first equality is the coherent-core definition. The second is a literal
predicate-by-predicate comparison with the original PRIMCAR panel: the two
sums have the same variables, coefficient, ratio kernel, height set, and
sieve predicate.

Consequently the `u=1` specialization of the one-variable wavelet energy is
not merely analogous to PRIMCAR:

\[
 \boxed{
 \mathcal Y^\alpha_1(D,H)
 =\sum_{I\in\mathscr D_H}\mathcal E_D^{(\alpha,0)}(I).}
\tag{0.2}
\]

Define `BASEWAVE` to be the all-positive-exponent estimate for the left side
of (0.2), uniformly in `D,H` and the three channels. Then **`BASEWAVE` is
exactly `PRIMCAR`**.

The positive `AUXCOLORPRIMCAR` assembly includes this energy with weight

\[
 w(1)={g(1)\over\sqrt1}=1.
\]

Hence

\[
 \boxed{
 \mathfrak X^\alpha_{\rm color}(D,H)
 \ge \mathcal Y^\alpha_1(D,H).}
\tag{0.3}
\]

The corrected conditional gate graph is

\[
 \boxed{
 \begin{aligned}
 \mathrm{AUXCOLORPRIMCAR}
 &\Longrightarrow\mathrm{PRIMCAR}
 \Longrightarrow\mathrm{PRIMLS}\Longrightarrow\mathrm{RH},\\
 \mathrm{WAVEPRIMCAR}
 &\Longrightarrow\mathrm{BASEWAVE}
 (=\mathrm{PRIMCAR})
 \Longrightarrow\mathrm{PRIMLS}\Longrightarrow\mathrm{RH}.
 \end{aligned}}
\tag{0.4}
\]

In particular, `WAVEPRIMCAR -> BASEWAVE` follows by selecting `u=1`
directly. The threshold `eta<1/2` is not used in this implication. That
threshold belongs only to the different argument which sums all cores to
deduce `WAVEPRIMCAR -> AUXCOLORPRIMCAR`.

No estimate named in this packet is proved. Equation (0.4) is a corrected
conditional implication, not a proof of its premise or of RH.

## 1. Predicate-by-predicate comparison

The original panel attached to one aligned finite height set `I` is

\[
 \mathcal P_I^{(\alpha,0)}(d)
 =\sum_{\substack{
 a,b\ {\rm squarefree},\ 67\nmid ab,\ (a,b)=1\\
 (ab,d)=1,\ \max(67^\alpha a,b)\in I}}
 {\mu(a)\mu(b)\over\sqrt{ab}}
 \mathcal R\!\left(\log{67^\alpha a\over b}\right).
\tag{1.1}
\]

The generalized ordinary panel is

\[
 \mathcal P^0_{A,B}(q;I)
 =\sum_{\substack{
 m,n\ {\rm squarefree},\ 67\nmid mn,\ (m,n)=1\\
 (mn,q)=1,\ \max(Am,Bn)\in I}}
 {\mu(m)\mu(n)\over\sqrt{mn}}
 \mathcal R\!\left(\log{Am\over Bn}\right).
\tag{1.2}
\]

At `u=1`, the coherent-core definition has `r=1`, `u/r=1`, and `du=d`:

\[
 \mathcal C^\alpha_{d,1}(I)
 =\sum_{r\mid1}\mathcal P^0_{67^\alpha r,1/r}(d;I)
 =\mathcal P^0_{67^\alpha,1}(d;I).
\tag{1.3}
\]

Substitute

\[
 (A,B,q,m,n)=(67^\alpha,1,d,a,b)
\]

in (1.2). Every part of (1.2) becomes the corresponding part of (1.1):

| datum | generalized `u=1` panel | original panel |
|---|---|---|
| arithmetic support | `m,n` squarefree and 67-free | `a,b` squarefree and 67-free |
| primitive support | `(m,n)=1` | `(a,b)=1` |
| sieve | `(mn,d)=1` | `(ab,d)=1` |
| height | `max(67^alpha m,n) in I` | `max(67^alpha a,b) in I` |
| ratio | `R(log(67^alpha m/n))` | `R(log(67^alpha a/b))` |
| coefficient | `mu(m)mu(n)/sqrt(mn)` | `mu(a)mu(b)/sqrt(ab)` |

This proves (0.1) term by term. There is no limit, asymptotic replacement,
or norm inequality in the proof.

## 2. The one-variable wavelet at `u=1`

The exact color-to-wavelet identity is

\[
 \mathcal C^\alpha_{d,u}(I)
 =\sum_{\substack{M\ {\rm squarefree},\ 67\nmid M\\
                    (M,u)=1,\ (uM,d)=1}}
 {\mu(M)\over\sqrt M}\mathcal W_I^\alpha(uM).
\tag{2.1}
\]

Putting `u=1` gives

\[
 \mathcal C^\alpha_{d,1}(I)
 =\sum_{\substack{M\ {\rm squarefree},\ 67\nmid M\\(M,d)=1}}
 {\mu(M)\over\sqrt M}\mathcal W_I^\alpha(M).
\tag{2.2}
\]

Expanding

\[
 \mathcal W_I^\alpha(M)
 =\sum_{a\mid M}
 \mathcal R\!\left(\log{67^\alpha a^2\over M}\right)
 1_{\max(67^\alpha a,M/a)\in I}
\]

and writing `b=M/a` reproduces (1.1). Squarefree `M` makes `a,b`
squarefree and coprime; conversely every pair in (1.1) has the unique product
`M=ab`. Thus the wavelet and primitive-panel expansions agree term by term,
not only after summation.

Now substitute (2.2) into the definition of `Y`:

\[
 \begin{aligned}
 \mathcal Y^\alpha_1(D,H)
 &=\sum_{\substack{d\le D\ {\rm squarefree}\\67\nmid d}}{1\over d}
   \sum_{I\in\mathscr D_H}|\mathcal C^\alpha_{d,1}(I)|^2\\
 &=\sum_{I\in\mathscr D_H}\mathcal E_D^{(\alpha,0)}(I),
 \end{aligned}
\]

which proves (0.2).

## 3. Positive containment and the corrected hierarchy

All core weights in the color energy are positive and the `u=1` weight is
one. Selecting that summand proves (0.3). Therefore an
`AUXCOLORPRIMCAR` estimate in all three physical channels proves the exact
three-channel `PRIMCAR` estimate. The frozen Carleson packet already proves

\[
 \mathrm{PRIMCAR}\Longrightarrow\mathrm{PRIMLS}
 \Longrightarrow\mathrm{RH}.
\]

Combining those implications proves the first line of (0.4). The second line
uses only the `u=1` instance of the uniformly quantified `WAVEPRIMCAR`
statement. It does not sum over cores and therefore pays no outer Euler
product.

Since the rho packet proves
`RAYPRIMCAR -> AUXCOLORPRIMCAR`, its corrected conditional route also reads

\[
 \mathrm{RAYPRIMCAR}\Longrightarrow\mathrm{AUXCOLORPRIMCAR}
 \Longrightarrow\mathrm{PRIMCAR}\Longrightarrow\mathrm{RH}.
\]

This strengthens the logical significance of the open gates. It proves none
of their estimates.

## 4. Scope firewalls

1. `COLORPRIMCAR` is only the `D=1` specialization. It does not by itself
   supply the finite-`D` harmonic energy required by PRIMCAR.
2. `AUXCOLORPRIMCAR` controls PRIMCAR as a complete positive energy. This
   does not mean it separately estimates every biased-Boolean spectral
   coordinate.
3. Uniform `WAVEPRIMCAR` is stronger than needed for this implication. Its
   single `u=1` instance is already exactly PRIMCAR.
4. The `eta<1/2` restriction remains correct for summing all `u` with the
   outer weight. It is irrelevant to selecting `u=1`.
5. No PRIMCAR, PRIMLS, AUXCOLORPRIMCAR, WAVEPRIMCAR, RH, or GRH estimate is
   proved here.

## 5. Bounded exact replay

The replay authenticates the frozen source blobs and then, for all three
physical channels, exhausts small squarefree/67-free primitive pairs,
several squarefree sieve values, and a family of exact integer-height sets.
It checks:

- equality of the original and generalized `u=1` predicates;
- equality of their formal normalized term signatures;
- equality after expanding the `u=1` divisor wavelet by `M=ab`;
- equality of bounded exact rational probe energies;
- `w(1)=1` and the corrected implication metadata.

The rational probe is only a coefficient-independent authentication of the
term bijection. The theorem itself uses the literal coefficient and kernel
shown in Sections 1--2. No floating point, zeta-zero census, growing family,
or asymptotic inference is used.

```text
python -B research/l-families/atlas/function_field/ffps_basewave_primcar_identity.py --check
python -B -O research/l-families/atlas/function_field/ffps_basewave_primcar_identity.py --check
python -B -m unittest tests.test_ffps_basewave_primcar_identity
python -B -O -m unittest tests.test_ffps_basewave_primcar_identity
```
