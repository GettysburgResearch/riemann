# L-91021 — The generalized-Jordan cocycle has an explicit divisor-splitting Stinespring isometry

Claim ID: `L-91021`  
Status: **EXACT SOURCE-SIDE STINESPRING THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-11  
Depends on: `L-91012`  
RH status: **unproved**

## 1. Positive sieve coefficients

For `a>0`, retain

\[
 Q_a(s)=\frac{\zeta(s)}{\zeta(s+2a)}
 =\sum_{n\ge1}\frac{q_a(n)}{n^s},
 \qquad
 q_a(n)=\prod_{p\mid n}(1-p^{-2a})>0.
\]

The shifted cocycle gives

\[
 \boxed{
 q_{a+b}(n)
 =\sum_{de=n}q_a(d)q_b(e)e^{-2a\log e}.
 }
 \tag{L-91021.1}
\]

For every factorization `n=de`, define

\[
 \boxed{
 \pi_{a,b}^{(n)}(d,e)
 =\frac{q_a(d)q_b(e)e^{-2a\log e}}
 {q_{a+b}(n)}.
 }
 \tag{L-91021.2}
\]

Then

\[
 \pi_{a,b}^{(n)}(d,e)>=0,
 \qquad
 \sum_{de=n}\pi_{a,b}^{(n)}(d,e)=1.
 \tag{L-91021.3}
\]

Thus every integer `n` carries a canonical probability distribution on its divisor splittings.

## 2. The divisor isometry

Let `H=ell^2(N)` with standard basis `(e_n)`. Define

\[
 \boxed{
 V_{a,b}e_n
 =\sum_{de=n}
 \sqrt{\pi_{a,b}^{(n)}(d,e)}\,
 e_d\otimes e_e.
 }
 \tag{L-91021.4}
\]

Distinct integers have disjoint product supports in the tensor basis. Hence

\[
 \boxed{V_{a,b}^*V_{a,b}=I_H.}
 \tag{L-91021.5}
\]

This is a concrete Stinespring isometry; no abstract square root or completion theorem is used.

## 3. Exact coherent-vector factorization

For `Re(s)>1/2`, put

\[
 k_{a,s}
 =\sum_{n\ge1}\sqrt{q_a(n)}\,n^{-s}e_n.
 \tag{L-91021.6}
\]

Its norm is finite because

\[
 \|k_{a,s}\|^2=Q_a(2\Re s).
\]

Using (L-91021.2) term by term gives

\[
 \boxed{
 V_{a,b}k_{a+b,s}
 =k_{a,s}\otimes k_{b,s+a}.
 }
 \tag{L-91021.7}
\]

Consequently the positive kernel factorization

\[
 Q_{a+b}(s+\overline w)
 =Q_a(s+\overline w)
  Q_b(s+\overline w+2a)
 \tag{L-91021.8}
\]

is realized by one explicit isometry.

## 4. Vertical phases and logarithmic jets

Let

\[
 D_xe_n=n^{-ix}e_n,
 \qquad
 Le_n=(\log n)e_n.
\]

Since `log(de)=log d+log e`, the divisor isometry obeys

\[
 \boxed{
 V_{a,b}D_x
 =(D_x\otimes D_x)V_{a,b},
 }
 \tag{L-91021.9}
\]

and on the natural finite-support core,

\[
 \boxed{
 V_{a,b}L
 =(L\otimes I+I\otimes L)V_{a,b}.
 }
 \tag{L-91021.10}
\]

Therefore every logarithmic derivative uses the ordinary additive coproduct. In particular,

\[
 V_{a,b}L^2
 =\bigl(L^2\otimes I+2L\otimes L+I\otimes L^2\bigr)V_{a,b},
 \tag{L-91021.11}
\]

so all first- and second-current cross terms are retained automatically.

## 5. Coassociativity

For `a,b,c>0`, both maps

\[
 (V_{a,b}\otimes I)V_{a+b,c},
 \qquad
 (I\otimes V_{b,c})V_{a,b+c}
\]

send `e_n` to the same vector indexed by triples `n=d e f`, with coefficient

\[
 \sqrt{
 \frac{q_a(d)q_b(e)q_c(f)
       e^{-2a\log e}e^{-2(a+b)\log f}}
      {q_{a+b+c}(n)}
 }.
\]

Hence

\[
 \boxed{
 (V_{a,b}\otimes I)V_{a+b,c}
 =(I\otimes V_{b,c})V_{a,b+c}.
 }
 \tag{L-91021.12}
\]

The positive source flow is therefore coassociative at all generations.

## 6. Dyadic specialization

At `b=a`,

\[
 \boxed{
 V_{a,a}k_{2a,s}
 =k_{a,s}\otimes k_{a,s+a}.
 }
 \tag{L-91021.13}
\]

This is exactly the arithmetic dilation required by the dyadic Cauchy gate. The inherited source appears with coefficient one because `V_(a,a)` is an isometry.

## 7. Exact boundary

Closed here:

1. a probability law on every divisor splitting;
2. an explicit coefficient-one Stinespring isometry;
3. coherent-vector factorization of the full positive sieve kernel;
4. exact vertical-phase and logarithmic-generator intertwining;
5. all-order coassociativity.

Still open:

1. continuation of this source isometry from its positive-kernel domain to the completed critical-boundary Weil form;
2. identification of the Cauchy storage factor `Psi_a` as an actual output port of that completed isometry;
3. RH.

The control models on PR #398 show that a source-only continuation is insufficient: the eventual intertwiner must include the exact completed gamma/pole boundary data rather than only the positive Jordan coefficients.
