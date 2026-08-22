# Consumer contract

Let `f(X)` be one fixed real detector, chosen independently of any hypothetical zero, proof horizon, or later scale. A canonical application must supply all of the following.

## Analytic contract

1. `f` is locally integrable on `[1,infinity)` and has a finite Mellin abscissa.
2. On an initial half-plane its Mellin transform is computed by an absolutely convergent arithmetic expansion.
3. It continues to the needed half-plane in the form
   \[
   \mathcal M f(s)=H(s)+\frac{P(s+\tfrac12)B(s)}{\zeta(s+\tfrac12)},
   \]
   with `H` holomorphic there.
4. The fixed multiplier `P(z)B(z-1/2)` does not vanish at the hypothetical off-critical zero under consideration.
5. Positive-real singularities are removed or separately accounted for.
6. Zero multiplicity and functional-equation reflection are retained.

## One-sided arithmetic contract

Supply one of:

- eventual nonnegativity of `f`;
- a fixed decomposition `f=d+e` with `d>=0` and the Mellin transform of `e` holomorphic in `Re(s)>0`;
- subpower logarithmic negative mass
  \[
  \int_1^T f_-(X)\,\frac{dX}{X}=T^{o(1)}.
  \]

The verified specialized Landau theorem then forbids an uncancelled reciprocal-zeta pole in the relevant half-plane.

## Fixed-object rule

The row, scalar, source normalization, box width, and signed defect must be fixed before introducing a hypothetical zero. A countable family is allowed only when the arithmetic theorem supplies the entire family simultaneously. Choosing the producer after seeing the zero is not allowed.

## Output

The output is a conditional implication to RH. The consumer does not provide the arithmetic hypothesis.
