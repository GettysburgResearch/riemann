# A power-source obstruction for the natural selected norm

Status: proposed arithmetic counterexample; independently reviewed against the pinned source contracts and residue-mask identities, but not formally verified. No zero-free region is proved. Novelty has not been checked against the literature.

Scope: the abstract *natural-row*, arbitrary-ideal-slot operator interface of [tracker PR #93](https://github.com/GTimG/QuasiRiemannTracker/pull/93) at head `70c4d642c4c6263a09bf0f3930a74e2aa7c99f00`. The example does not address its squarefree-only selected norm or the narrower physical prime-slot interface. It does not refute the existing PR93 estimate, which is used with slope bounded strictly above `1/2`.

Dependencies: standard ideal counting in the Eisenstein field and the prime ideal theorem (or Dirichlet's theorem with the prime number theorem for primes `1 mod 3`); ordinary sextic residue-symbol multiplicativity and its coprime zero extension. We use the source convention `idealRowHom`. Its `map_pow` in the source ideal, `idealRowHom_argument_pow` and sixth-power mask identity are in the pinned OpenAI baseline. The zero mask is retained below.

## Statement

At endpoint slot slope `delta=1/2`, no uniform bound of the following stronger shape can hold for every abstract natural selected family and every ordinary dual source set:

```
selectedNorm(rows, sources) <= C * Z^epsilon * (L + Y^q * L^(1/2))
```

when `q<1/3`, even if a positive slot-width lower bound and an arbitrarily small fixed early mesh are required. Here `rowNorm(u)<=Y`, all ordinary source ideals have norm at most `L`, and `C` is independent of the growing parameter `Z`, with the remaining dependencies and order of choices as in the abstract source interface. This is only a lower restriction on a potential improvement of the exponent `1-delta`; it does not rule out the endpoint exponent `q=1/2`.

## Construction and proof

Fix `q<1/3` and choose `0<epsilon<1/3-max(q,0)`. Let the admissible early mesh be any positive number. After the mesh is fixed choose one width `w>0` below it, with `w<2/3`, and a positive width lower bound no larger than `w`. Set `Y=Z` and `X=Z^w`. For large `Z`, let `F` consist of the rows `u=pi^3`, one for each good prime ideal `(pi)` of norm in `[Y^(1/3)/2,Y^(1/3)]`, choosing one fixed primary generator per ideal. Then `rowNorm(u)<=Y`; each `u` is nonzero and sixth-power-free because its sole prime valuation is three. Distinct prime norms yield distinct rows, and the prime ideal theorem gives

```
#F >> Y^(1/3)/log Y.
```

For the sole slot take as sources the distinct square ideals `I=J^2`, where `J` runs over all nonzero ideals coprime to the fixed bad primes above 2 and 3 with `N(J)<=sqrt(X)`. Thus `N(I)<=X<=2 Z^w`. Let `n` be their number. Elementary ideal counting gives `n >= c sqrt(X)` for one constant `c>0` independent of `Z`. Assign each slot coefficient `sqrt(Cslot/n)`, with a fixed `Cslot>=1/c`. The coefficient squared mass is exactly `Cslot`.

For all sufficiently large `Z`, each row prime has norm greater than every `N(J)` because `w/2<1/3`. Hence `J` is coprime to `pi`. By multiplicativity in both arguments, the natural zero mask and the sixth-power identity,

```
idealRowHom(pi^3,J^2) = idealRowHom(pi,J)^6 = 1.
```

The slot polynomial is therefore `sqrt(Cslot*n)` on every row; its square is at least `sqrt(X)=Z^(w/2)`. This is precisely the aggregate selection hypothesis at slope `delta=1/2` for the one slot, including its width.

For the dual ordinary source set choose the unit ideal alone, `L=1`. Its matrix entry is one at every row, so the squared Euclidean operator norm is exactly `#F`. The proposed upper bound would give

```
Y^(1/3)/log Y << C Z^epsilon (1+Y^q),   Y=Z,
```

contradicting `epsilon<1/3-max(q,0)`. Constants may depend on `w`, `Cslot` and the fixed arithmetic data, since those are fixed before `Z` grows. This completes the counterexample at the explicitly stated scope.

## Interface warning

The slot ideals here are *squares of arbitrary good ideals*, not the prime ideals of an actual physical slot. Their presence is permitted by the broader `SelectedSlotData.Bounded` interface and by the natural aggregate contract; it is not automatically permitted by the narrower prime-only detector. A proof that uses that additional arithmetic support may evade this example. Likewise, the argument does not imply saturation of the squarefree-only operator bound or any constraint on zeros of an L-function.

## General power-row obstruction

The same argument gives a family of necessary exponent constraints. Fix `r` in `{1,2,3,4,5}` and let `d=6/gcd(6,r)`. Replace the cube rows by `u=pi^r`, and the square slot ideals by `J^d`. These rows remain sixth-power-free, and for supported `J` coprime to `pi`,

```
idealRowHom(pi^r,J^d) = idealRowHom(pi,J)^(rd) = 1.
```

There are `>> X^(1/d)` such source ideals with norm at most `X`, and the same normalized coefficients give squared slot amplitude at least `X^(1/d)`. Thus any selection slope `delta<=1/d` is realized. Choose the early width `w` sufficiently small that `w/d<1/r`; then all selected good row primes of norm about `Y^(1/r)` are coprime to the source ideals, with `Y=Z` and `X=Z^w`. The unit dual source again makes the operator norm squared equal to the number of rows, `>>Y^(1/r)/log Y`. Consequently any uniform estimate of the corresponding abstract shape

```
selectedNorm <= C Z^epsilon (L + Y^q L^delta)
```

at `L=1`, for every small fixed positive `epsilon`, requires `q>=1/r`. Taking the strongest of these five examples gives

| Slot-slope range | Necessary exponent |
|---|---|
| `0 <= delta <= 1/6` | `q >= 1` |
| `1/6 < delta <= 1/3` | `q >= 1/2` |
| `1/3 < delta <= 1/2` | `q >= 1/3` |

For the first row the examples use prime `u=pi` and do satisfy the row-squarefree condition, but their slot sources are still sixth-power ideals rather than prime slots. The other ranges use non-squarefree, sixth-power-free natural rows. These are necessary conditions only: they do not assert attainability of the indicated exponent or settle any estimate above slope one half.

## Quantified version and normalizations

Let `K=Q(sqrt(-3))`, `O=Z[omega]`, and let `chi(u,I)` be the source's `idealRowHom` for a nonzero ideal `I`. On ideals supported away from primes above `2` and `3`, it is multiplicative in both the element argument and the ideal, is zero on non-coprime inputs, and its sixth power is one on coprime inputs. These identities are not asserted at the bad primes; every slot ideal in the construction is supported away from them. For the dual source `I=O`, the source's `map_one` gives `chi(u,O)=1` for every row.

Fix `r` and `d` as above, `0<=delta<=1/d`, and any real `q<1/r`. Choose a fixed `epsilon` satisfying `0<epsilon<1/r-max(q,0)`. Even granting the proposed estimate its full quantifiers, the challenger proceeds as follows: after an arbitrary positive mesh `mesh0` is supplied, select a fixed `w` with `0<w<min(mesh0, d/r)` and choose the fixed lower slot width `wmin=w/2`. Select an admissible fixed coefficient-mass bound `Cslot` sufficiently large. Then let `Z` tend to infinity through the positive reals (or just integers), with `Y=Z`, `X=Z^w` and `L=1`. In the source contract take `A=1` and any fixed `P>=4`; thus `1<=Y<=Z^A` and `1<=L<=Z^P`. This works for every choice of `mesh0`; no width, coefficient-mass bound or lower slot width varies with `Z`. The ratio `w/d<1/r` guarantees `X^(1/d)=o(Y^(1/r))`, so no row prime divides any slot ideal.

For an elementary lower bound on slot ideals, the lattice `{a+b omega: a,b in Z}` has `>>R` points of norm at most `R` in a fixed residue class coprime to `6`; every nonzero principal ideal has at most six unit generators. Hence there are `>>R` supported principal ideals `J` with `N(J)<=R`. Unique factorization of nonzero ideals makes `J -> J^d` injective. With `R=X^(1/d)`, the number `n` of slot sources is at least `c X^(1/d)` for a constant `c>0`. Set all coefficients equal to `sqrt(Cslot/n)` with `Cslot>=1/c`. The finite coefficient mass is exactly `Cslot` and the slot polynomial has square `Cslot*n>=X^(1/d)>=X^delta`. In the individual-slot formulation, set its declared energy to `delta*w`; in the aggregate formulation this is exactly the one-slot product condition.

For each large `Z`, the prime number theorem in the progression `1 mod 3` gives `>>Y^(1/r)/log Y` distinct rational primes `p` in `[Y^(1/r)/2,Y^(1/r)]`. Each splits as `p=pi*conj(pi)`, and a fixed choice of good generator `pi` gives `u=pi^r` with `rowNorm(u)=p^r<=Y`. Its ideal is sixth-power-free because `1<=r<=5`; distinct `p` give distinct rows. As all `N(J)<p`, no slot ideal is divisible by `(pi)`. The coprime sixth-power mask therefore gives the claimed constant slot value on *every* row. Finally the single-column dual-source matrix with source `O` has all entries one, so its squared operator norm is the number of rows. If the supposed estimate were uniform with `L=1`, it would imply

```
Y^(1/r)/log Y << C Z^epsilon (1+Y^q),  Y=Z,
```

which is impossible by the strict choice of `epsilon`. The implicit and displayed constants may depend on the fixed mesh, width, coefficient bound and arithmetic conventions, but none may depend on `Z`. This is a precise counterexample for the broad source class; the physical detector's prime-only slots form a smaller class and are not covered.

## Interaction with the PR94 bottleneck

The PR94 return's method-specific obstruction examined in [`../2026-10-29-arvi-return/fixed-face-obstruction.md`](../2026-10-29-arvi-return/fixed-face-obstruction.md) uses zero-detector parameter `delta_zero=223/500` and the maximal normalized amplitude ratio `p=1/2`. The source's physical amplitude bins have `g_i<=delta_zero/2` up to their explicitly allocated small binning error, and the squared slot response uses exponent `2*g_i`. Thus, as those errors are chosen sufficiently small, the PR93 selected-norm inlet demanding squared slope at least `500001/1000000` cannot be invoked in this bin: even its largest allowed slope is close to `223/500<1/2`. The separate PR93 high-density policy also has a lower density cutoff above `223/500`.

A specific open analytic target is the *same* all-source selected estimate currently proved above one half, extended at the single slope `sigma=223/500`:

```
selectedNorm <= C Z^epsilon * (L + Y^(1-sigma) L^sigma).
```

It would still need the early mesh, natural root and common-mask quantifiers, the detector-count bridge, and the complete physical-return checks. The proof mechanism in PR93 does not extend directly: with `r=(1-sigma)/sigma>1`, its scalar recurrence has `e_n=sigma+r^n` and diverges rather than contracts. In fact for a general starting exponent `e_0`, the recurrence gives `e_n-sigma=r^n(e_0-sigma)`, so a starting exponent above `sigma` never approaches it. This is a statement about that recurrence only; it neither disproves the single-slope target nor yields a new zero-free region.

Conversely, the power-row construction above rules out the claimed all-source exponent law for every `0<sigma<=1/6`, since there `q=1-sigma<1` while the supported sixth-power slot ideals force `q>=1`. Thus any extension below one half must have a restricted range or additional source hypotheses. The `sigma=223/500` target is not excluded by this example: its predicted exponent `277/500` exceeds the natural-row lower obstruction `1/3`.

For scale only, the unit-source consequence of that hypothetical target at `sigma=223/500` gives a selected-core count exponent at most `277/500=0.554`, up to arbitrary losses. At the fixed PR94 obstruction point the existing C-branch exponent is `137478360780643/225606975000000 = 0.609371056815...`, a difference of `0.055371056815...`. Substituting this count *at that one point* into the existing row expression would lower its row exponent by approximately `0.03347` at `h=0.806`. This is only a conditional sensitivity check: the actual bin-to-selected-core adapter, all other amplitude bins, physical error terms and the full return would still need proof. In particular it is not a claimed zero-free region or a statement that the final boundary improves by that amount.
