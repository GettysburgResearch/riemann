# Source provenance ledger

Agent: `gpt56-03`  
Snapshot: 2026-07-22

## Inspection levels

- **FULL-TEXT** — theorem statement and surrounding definitions inspected in
  an author manuscript, arXiv HTML/PDF, or open publisher full text.
- **PRIMARY-ABSTRACT** — publisher or author abstract inspected; enough for the
  exact claim quoted here, but not for proof details.
- **METADATA** — title, author, venue, pages, DOI or stable locator inspected;
  no theorem wording is imported solely from this level.
- **LATER-PRIMARY-RESTATEMENT** — the original paper was located, but exact
  wording used here was checked in a later research paper that explicitly
  restates the theorem.
- **UNVERIFIED** — not located or insufficiently checked.  Such an entry must
  not support a theorem card.

## Ledger

| Key | Work | Located source | Inspection | Statement used |
|---|---|---|---|---|
| `Robin1984` | Robin, divisor-sum criterion | journal metadata; exact criterion restated in Lagarias 2002 and Choie et al. 2007 | LATER-PRIMARY-RESTATEMENT | RH iff `sigma(n)<e^gamma n log log n` for all `n>5040` |
| `Lagarias2002` | elementary harmonic criterion | arXiv:math/0008177 full text and journal metadata | FULL-TEXT | `sigma(n)<=H_n+e^{H_n}log H_n`, equality only `n=1` |
| `ChoieLichiardopolMoreeSole2007` | structural Robin restrictions | Numdam/Journal HTML and metadata | FULL-TEXT/PRIMARY-ABSTRACT | any Robin counterexample has strong divisibility/form restrictions |
| `Nicolas1983` | primorial Euler-phi criterion | publisher metadata; exact statement checked in later primary treatments | LATER-PRIMARY-RESTATEMENT | RH iff `N_k/phi(N_k)>e^gamma log log N_k` for all `k>=2` |
| `Li1997` | Li positivity criterion | ScienceDirect publisher page and abstract | PRIMARY-ABSTRACT plus Bombieri--Lagarias exact restatement | nonnegative/positive Li sequence criterion |
| `BombieriLagarias1999` | Li zero sum and arithmetic formula | publisher metadata and exact abstract | PRIMARY-ABSTRACT | `lambda_n=sum_rho[1-(1-1/rho)^n]`, positivity criterion, relation to Weil |
| `Weil1952` | explicit-formula positivity | bibliographic record and later primary discussion | METADATA | historical attribution only; exact normalization deliberately not imported |
| `Bombieri2000` | finite Weil quadratic functional | EUDML journal record and abstract | PRIMARY-ABSTRACT | positivity equivalent to RH; finite restrictions studied |
| `Speiser1935` | derivative-zero criterion | Springer/EUDML metadata; theorem restated by later primary papers | LATER-PRIMARY-RESTATEMENT | RH iff no nonreal `zeta'` zero left of the critical line |
| `BaezDuarte2003` | discrete Nyman--Beurling | arXiv:math/0202141 PDF/HTML | FULL-TEXT | `chi` belongs to closure of span of `rho(1/(kx))` |
| `GriffinOnoRolenZagier2019` | Jensen polynomial criterion/asymptotics | arXiv:1902.07321 and PNAS full text | FULL-TEXT | Pólya--Jensen equivalence and eventual fixed-degree hyperbolicity |
| `GriffinOnoRolenThornerTrippWagner2022` | effective xi Jensen bounds | arXiv:1910.01227 full HTML and journal metadata | FULL-TEXT | `RH_m(T)` implies hyperbolicity for `d<=floor(T)^2` |
| `deBruijn1950` | heat-flow real-zero monotonicity | Duke DOI/metadata and Rodgers--Tao historical statement | LATER-PRIMARY-RESTATEMENT | historical threshold precursor |
| `Newman1976` | existence of `Lambda` | Proc. AMS metadata and Rodgers--Tao exact restatement | LATER-PRIMARY-RESTATEMENT | all zeros of `H_t` real iff `t>=Lambda` |
| `RodgersTao2020` | `Lambda>=0` | Cambridge open abstract and arXiv:1801.05914 | FULL-TEXT/PRIMARY-ABSTRACT | exact `H_t`, `Phi`, threshold statement, `Lambda>=0` |
| `DelegliseNicolas2019` | bounded-prime-sum criterion | Cambridge publisher page and abstract | PRIMARY-ABSTRACT | RH iff `log h(n)<sqrt(li^{-1}(n))` for every `n>=1` |
| `DelegliseNicolas2013` | algorithms for `h(n)` | arXiv:1207.0603 | PRIMARY-ABSTRACT | definition and existence of large-`n` algorithms |
| `Turing1953` | zero-count certification | publisher metadata/DOI | METADATA | infrastructure reference only |
| `Booker2006` | generalized Turing method | arXiv:math/0507502 and journal metadata | PRIMARY-ABSTRACT | infrastructure reference only |
| `PlattTrudgian2021` | rigorous zero-height verification | Wiley publisher page and arXiv:2004.09765 | PRIMARY-ABSTRACT | every zero through height `3*10^12` is on-line and simple |
| `Johansson2017` | Arb interval arithmetic | arXiv:1611.02831, IEEE metadata, Arb/FLINT documentation | FULL-TEXT/PRIMARY-ABSTRACT | rigorous midpoint-radius infrastructure |
| `Farmer2020` | Jensen route warning | arXiv:2008.07206 | PRIMARY-ABSTRACT | strategic warning, not a theorem dependency |

## Exact locator policy

The BibTeX file stores DOI and arXiv locators.  A DOI resolves the bibliographic
record; it does not imply that the full article was inspected.  Inspection
level is therefore recorded separately here.

For a theorem import, cite both:

1. the original work, when located; and
2. the actually inspected source that fixes the wording/normalization, when
   that is a later paper.

This is especially important for Robin, Nicolas, Speiser, Weil, and Newman.

## Citation failure protocol

When an agent cannot confirm a reference:

1. write `UNVERIFIED` in the claim;
2. state exactly what is missing (existence, metadata, theorem number,
   normalization, or proof);
3. do not allocate a theorem ID whose statement depends on the missing item;
4. open a source-audit issue if the result is blocking;
5. preserve the search terms and near matches in the session report.

A plausible title or remembered theorem number is not a citation.
