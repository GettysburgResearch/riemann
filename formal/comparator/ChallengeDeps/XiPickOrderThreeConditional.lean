import Mathlib

namespace ChallengeDeps.XiPickOrderThreeConditional

open Complex Set Filter

/-- Exact endpoint in Platt--Trudgian Theorem 1. -/
def verifiedHeightNat : ℕ := 3000175332800

def verifiedHeight : ℝ := verifiedHeightNat

/-- External publication metadata.  This is data, not a proposition asserting
that the publication theorem is true. -/
structure ExternalSourceLock where
  title : String
  authors : String
  journal : String
  doi : String
  arxiv : String
  artifactIdentifier : String
  artifactHashScope : String
  artifactSHA256 : String
  normalizedStatementSHA256 : String
  deriving DecidableEq, Repr

/-- Canonical external lock for the finite-height theorem.  The SHA-256 is over
the normalized theorem/citation record documented in
`formal/registry/deltas/C_EXTERNAL_SOURCE_LOCKS.tsv`; it is independent of every
local claim-file blob. -/
def plattTrudgianSourceLock : ExternalSourceLock where
  title := "The Riemann hypothesis is true up to 3*10^12"
  authors := "Dave Platt; Tim Trudgian"
  journal := "Bulletin of the London Mathematical Society 53 (2021), 792-797"
  doi := "10.1112/blms.12460"
  arxiv := "2004.09765v1"
  artifactIdentifier := "arXiv:2004.09765v1|DOI:10.1112/blms.12460"
  artifactHashScope :=
    "normalized citation/theorem record C_EXTERNAL_SOURCE_STATEMENTS/EXT.XI.PLATT_TRUDGIAN.2021.txt"
  artifactSHA256 :=
    "2eb547a373c49f56fa4da97284534bc06ee9a71548121a2b15d337cb79832c73"
  normalizedStatementSHA256 :=
    "2eb547a373c49f56fa4da97284534bc06ee9a71548121a2b15d337cb79832c73"

def SourceLockExact (lock : ExternalSourceLock) : Prop :=
  lock = plattTrudgianSourceLock

/-- Standard completed Xi normalization used only to pin the actual function
appearing in the conditional theorem. -/
noncomputable def riemannXi (s : ℂ) : ℂ :=
  (1 / 2 : ℂ) * s * (s - 1) * completedRiemannZeta s

noncomputable def centeredXi (z : ℂ) : ℂ :=
  riemannXi ((1 / 2 : ℂ) + z)

/-- The reviewed node coordinate `F(x)/x`, where
`F(x)=Xi'(x)/Xi(x)`. -/
noncomputable def actualXiNodeP (x : ℝ) : ℝ :=
  ((deriv centeredXi (x : ℂ)) /
    ((x : ℂ) * centeredXi (x : ℂ))).re

noncomputable def actualXiTCoordinate (t : ℝ) : ℝ :=
  actualXiNodeP (Real.sqrt t)

/-- Exact published finite-height statement actually consumed by the review.
Simplicity is deliberately not included because the repaired reserve ledger
retains multiplicity. -/
structure PublishedVerifiedHeightTheorem where
  sourceLock : ExternalSourceLock
  sourceLockExact : SourceLockExact sourceLock
  criticalLineBelowHeight :
    ∀ ρ : ℂ, riemannZeta ρ = 0 → 0 < ρ.im →
      ρ.im ≤ verifiedHeight → ρ.re = 1 / 2

/-- One critical-line zero orbit, with analytic multiplicity retained. -/
structure CriticalOrbit where
  gamma : ℝ
  multiplicity : ℕ
  gamma_pos : 0 < gamma
  one_le_multiplicity : 1 ≤ multiplicity
  zeta_zero :
    riemannZeta ((1 / 2 : ℂ) + Complex.I * gamma) = 0
  multiplicity_eq_analyticOrder :
    analyticOrderNatAt riemannZeta
      ((1 / 2 : ℂ) + Complex.I * gamma) = multiplicity

/-- One representative from a reflected off-line pair.  `a>0` selects the
right-side representative and `b>H*` selects positive ordinate above the
verified range. -/
structure ReflectedOffLineOrbit where
  a : ℝ
  b : ℝ
  multiplicity : ℕ
  a_pos : 0 < a
  a_lt_half : a < 1 / 2
  b_above_verified : verifiedHeight < b
  one_le_multiplicity : 1 ≤ multiplicity
  zeta_zero :
    riemannZeta ((1 / 2 : ℂ) + a + Complex.I * b) = 0
  reflected_zeta_zero :
    riemannZeta ((1 / 2 : ℂ) - a + Complex.I * b) = 0
  multiplicity_eq_analyticOrder :
    analyticOrderNatAt riemannZeta
      ((1 / 2 : ℂ) + a + Complex.I * b) = multiplicity
  reflected_multiplicity_eq_analyticOrder :
    analyticOrderNatAt riemannZeta
      ((1 / 2 : ℂ) - a + Complex.I * b) = multiplicity

structure SelectedCriticalReserve where
  orbit : CriticalOrbit
  gamma_le_half_height : orbit.gamma ≤ verifiedHeight / 2

/-- A second-order scalar jet. -/
structure Jet2 where
  value : ℝ
  first : ℝ
  second : ℝ


def jetAdd (f g : Jet2) : Jet2 :=
  ⟨f.value + g.value, f.first + g.first, f.second + g.second⟩


def jetScale (c : ℝ) (f : Jet2) : Jet2 :=
  ⟨c * f.value, c * f.first, c * f.second⟩


def reciprocalEnergy (f : Jet2) : ℝ :=
  f.value * f.second - 2 * f.first ^ 2


def criticalUnitJet (reserve : SelectedCriticalReserve) (t : ℝ) : Jet2 :=
  let V := t + reserve.orbit.gamma ^ 2
  ⟨2 / V, -2 / V ^ 2, 4 / V ^ 3⟩


def criticalOrbitJet (o : CriticalOrbit) (t : ℝ) : Jet2 :=
  jetScale (o.multiplicity : ℝ)
    (let V := t + o.gamma ^ 2
     ⟨2 / V, -2 / V ^ 2, 4 / V ^ 3⟩)


def orbitC (o : ReflectedOffLineOrbit) : ℝ := o.b ^ 2 - o.a ^ 2

def orbitB (o : ReflectedOffLineOrbit) : ℝ := 2 * o.a * o.b

def reserveRadius (reserve : SelectedCriticalReserve) : ℝ :=
  reserve.orbit.gamma ^ 2

def orbitGap (reserve : SelectedCriticalReserve)
    (o : ReflectedOffLineOrbit) : ℝ :=
  orbitC o - reserveRadius reserve

def orbitU (o : ReflectedOffLineOrbit) (t : ℝ) : ℝ := t + orbitC o

def orbitS (reserve : SelectedCriticalReserve)
    (o : ReflectedOffLineOrbit) (t : ℝ) : ℝ :=
  orbitGap reserve o / orbitU o t

def orbitKappa (reserve : SelectedCriticalReserve)
    (o : ReflectedOffLineOrbit) : ℝ :=
  orbitB o ^ 2 / orbitGap reserve o ^ 2

def orbitEpsilon (reserve : SelectedCriticalReserve)
    (o : ReflectedOffLineOrbit) : ℝ :=
  2 * (o.multiplicity : ℝ) * orbitKappa reserve o /
    (1 - orbitKappa reserve o)

def orbitTail (o : ReflectedOffLineOrbit) : ℝ :=
  (o.multiplicity : ℝ) / o.b ^ 2


def offLineOrbitJet (o : ReflectedOffLineOrbit) (t : ℝ) : Jet2 :=
  let m : ℝ := o.multiplicity
  let U := orbitU o t
  let B := orbitB o
  ⟨4 * m * U / (U ^ 2 + B ^ 2),
   4 * m * (B ^ 2 - U ^ 2) / (U ^ 2 + B ^ 2) ^ 2,
   8 * m * U * (U ^ 2 - 3 * B ^ 2) / (U ^ 2 + B ^ 2) ^ 3⟩


def qKappa (kappa s : ℝ) : ℝ :=
  1 - kappa + 3 * kappa * s * (2 - s) +
    kappa ^ 2 * s ^ 2 * (3 - 2 * s)

inductive OrbitRepresentative where
  | critical : CriticalOrbit → OrbitRepresentative
  | offLine : ReflectedOffLineOrbit → OrbitRepresentative


def orbitJet : OrbitRepresentative → ℝ → Jet2
  | .critical o, t => criticalOrbitJet o t
  | .offLine o, t => offLineOrbitJet o t

noncomputable def actualXiTJet (t : ℝ) : Jet2 :=
  ⟨actualXiTCoordinate t,
   deriv actualXiTCoordinate t,
   deriv (fun u : ℝ => deriv actualXiTCoordinate u) t⟩


def LocallyUniformlyConvergesOn
    (terms : ℕ → ℝ → ℝ) (limit : ℝ → ℝ) (domain : Set ℝ) : Prop :=
  ∀ K : Set ℝ, IsCompact K → K ⊆ domain →
    ∀ epsilon : ℝ, 0 < epsilon →
      ∃ N : ℕ, ∀ n : ℕ, N ≤ n → ∀ t ∈ K,
        |(∑ k in Finset.range n, terms k t) - limit t| < epsilon

/-- Exact grouped actual-Xi expansion interface.  It states one reflected-orbit
representative convention, analytic multiplicities, the selected reserve term,
and locally uniform convergence of values and the first two derivatives on
`t>1/4`. -/
structure GroupedActualXiC2Expansion where
  orbits : ℕ → OrbitRepresentative
  selectedReserve : SelectedCriticalReserve
  reserveIndex : ℕ
  reserveOccurs :
    orbits reserveIndex = .critical selectedReserve.orbit
  offLineEnumeration : ℕ → ReflectedOffLineOrbit
  offLineComplete :
    ∀ o : ReflectedOffLineOrbit,
      (∃ n : ℕ, orbits n = .offLine o) ↔
        ∃ k : ℕ, offLineEnumeration k = o
  offLineRepresentativeUnique : Function.Injective offLineEnumeration
  otherCriticalEnumeration : ℕ → CriticalOrbit
  otherCriticalComplete :
    ∀ o : CriticalOrbit, o ≠ selectedReserve.orbit →
      (∃ n : ℕ, orbits n = .critical o) ↔
        ∃ k : ℕ, otherCriticalEnumeration k = o
  otherCriticalRepresentativeUnique : Function.Injective otherCriticalEnumeration
  valueConverges :
    LocallyUniformlyConvergesOn
      (fun n t => (orbitJet (orbits n) t).value)
      (fun t => (actualXiTJet t).value) (Set.Ioi (1 / 4))
  firstConverges :
    LocallyUniformlyConvergesOn
      (fun n t => (orbitJet (orbits n) t).first)
      (fun t => (actualXiTJet t).first) (Set.Ioi (1 / 4))
  secondConverges :
    LocallyUniformlyConvergesOn
      (fun n t => (orbitJet (orbits n) t).second)
      (fun t => (actualXiTJet t).second) (Set.Ioi (1 / 4))

/-- The selected orbit is split into one unit of reserve plus the exact
`(m0-1)R0` residual. -/
def CriticalMultiplicityResidual
    (reserve : SelectedCriticalReserve) : Prop :=
  ∀ t : ℝ,
    criticalOrbitJet reserve.orbit t =
      jetAdd (criticalUnitJet reserve t)
        (jetScale ((reserve.orbit.multiplicity : ℝ) - 1)
          (criticalUnitJet reserve t))

/-- Exact scalar meaning that one reflected off-line orbit is paid by its
reviewed share of the selected critical reserve. -/
def OneOrbitPaid (reserve : SelectedCriticalReserve)
    (o : ReflectedOffLineOrbit) (t : ℝ) : Prop :=
  let q := offLineOrbitJet o t
  let r := criticalUnitJet reserve t
  let epsilon := orbitEpsilon reserve o
  0 ≤ reciprocalEnergy
    ⟨q.value + epsilon * r.value,
     q.first + epsilon * r.first,
     q.second + epsilon * r.second⟩

/-- Exact one-use finite-prefix reserve ledger.  Shares are the reviewed
`2m*kappa/(1-kappa)`, every share is nonnegative, every orbit is paid, the
reciprocal-square tail is explicit, total use is at most one, and the leftover
coefficient is nonnegative. -/
structure ActualXiReserveAllocation
    (grouped : GroupedActualXiC2Expansion) where
  share : ℕ → ℝ
  share_eq :
    ∀ i : ℕ, share i =
      orbitEpsilon grouped.selectedReserve (grouped.offLineEnumeration i)
  share_nonnegative : ∀ i : ℕ, 0 ≤ share i
  tail_nonnegative :
    ∀ i : ℕ, 0 ≤ orbitTail (grouped.offLineEnumeration i)
  share_le_nine_tail :
    ∀ i : ℕ, share i ≤ 9 * orbitTail (grouped.offLineEnumeration i)
  reciprocalSquareTail :
    ∀ N : ℕ,
      (∑ i in Finset.range N, orbitTail (grouped.offLineEnumeration i)) ≤
        2 * (Real.log verifiedHeight + 1) / verifiedHeight
  numericalBudget :
    18 * (Real.log verifiedHeight + 1) / verifiedHeight < 1
  everyOrbitPaid :
    ∀ i : ℕ, ∀ t : ℝ, 1 / 4 < t →
      OneOrbitPaid grouped.selectedReserve (grouped.offLineEnumeration i) t
  totalShare_le_one :
    ∀ N : ℕ, (∑ i in Finset.range N, share i) ≤ 1
  leftover : ℕ → ℝ
  leftover_eq :
    ∀ N : ℕ, leftover N = 1 - ∑ i in Finset.range N, share i
  leftover_nonnegative : ∀ N : ℕ, 0 ≤ leftover N
  oneUse :
    ∀ N : ℕ, leftover N + ∑ i in Finset.range N, share i = 1

/-- Finite Pick data, duplicated on the trusted Mathlib-only side. -/
def pickEntry (x p y q : ℝ) : ℝ := (x * p + y * q) / (x + y)

def pickDet2 (x p y q : ℝ) : ℝ := p * q - pickEntry x p y q ^ 2

def quad2 (a b c x y : ℝ) : ℝ :=
  a * x ^ 2 + 2 * b * x * y + c * y ^ 2

def IsPSD2 (a b c : ℝ) : Prop :=
  ∀ x y : ℝ, 0 ≤ quad2 a b c x y

def quad3 (a b c d e f x y z : ℝ) : ℝ :=
  a * x ^ 2 + 2 * b * x * y + 2 * c * x * z +
    d * y ^ 2 + 2 * e * y * z + f * z ^ 2

def IsPSD3 (a b c d e f : ℝ) : Prop :=
  ∀ x y z : ℝ, 0 ≤ quad3 a b c d e f x y z

def secondDivDiff (t1 t2 t3 y1 y2 y3 : ℝ) : ℝ :=
  y1 / ((t1 - t2) * (t1 - t3)) +
  y2 / ((t2 - t1) * (t2 - t3)) +
  y3 / ((t3 - t1) * (t3 - t2))

/-- A locally uniform convergence statement for a sequence, rather than a
series of terms. -/
def LocallyUniformlyConvergesSequenceOn
    (sequence : ℕ → ℝ → ℝ) (limit : ℝ → ℝ) (domain : Set ℝ) : Prop :=
  ∀ K : Set ℝ, IsCompact K → K ⊆ domain →
    ∀ epsilon : ℝ, 0 < epsilon →
      ∃ N : ℕ, ∀ n : ℕ, N ≤ n → ∀ t ∈ K,
        |sequence n t - limit t| < epsilon

/-- Componentwise finite sum of second-order jets. -/
def jetSumRange (terms : ℕ → ℝ → Jet2) (N : ℕ) (t : ℝ) : Jet2 :=
  ⟨∑ i in Finset.range N, (terms i t).value,
   ∑ i in Finset.range N, (terms i t).first,
   ∑ i in Finset.range N, (terms i t).second⟩

/-- One off-line orbit together with exactly its allocated share of the selected
critical reserve. -/
def paidOffLineBlock
    (grouped : GroupedActualXiC2Expansion)
    (allocation : ActualXiReserveAllocation grouped)
    (i : ℕ) (t : ℝ) : Jet2 :=
  jetAdd (offLineOrbitJet (grouped.offLineEnumeration i) t)
    (jetScale (allocation.share i) (criticalUnitJet grouped.selectedReserve t))

/-- Exact finite-prefix regrouping: the unspent reserve, the retained
`(m0-1)R0` residual, the paid off-line blocks, and the other critical orbits.
The one-use identity in `allocation` prevents reserve duplication. -/
def regroupedActualXiPrefix
    (grouped : GroupedActualXiC2Expansion)
    (allocation : ActualXiReserveAllocation grouped)
    (N : ℕ) (t : ℝ) : Jet2 :=
  jetAdd
    (jetScale (allocation.leftover N) (criticalUnitJet grouped.selectedReserve t))
    (jetAdd
      (jetScale ((grouped.selectedReserve.orbit.multiplicity : ℝ) - 1)
        (criticalUnitJet grouped.selectedReserve t))
      (jetAdd
        (jetSumRange (paidOffLineBlock grouped allocation) N t)
        (jetSumRange
          (fun i u => criticalOrbitJet (grouped.otherCriticalEnumeration i) u)
          N t)))

/-- Exact external C2 assembly still required after the finite reserve algebra.
It no longer assumes final actual-Xi curvature.  Instead it states that the
source-faithful paid prefixes above have nonnegative finite curvature and
converge, componentwise through two derivatives (and hence in curvature), to
the concrete actual-Xi jet. -/
structure RegroupedActualXiC2Approximation
    (grouped : GroupedActualXiC2Expansion)
    (allocation : ActualXiReserveAllocation grouped) : Prop where
  prefixEnergyNonnegative :
    ∀ N : ℕ, ∀ t : ℝ, 1 / 4 < t →
      0 ≤ reciprocalEnergy (regroupedActualXiPrefix grouped allocation N t)
  valueConverges :
    LocallyUniformlyConvergesSequenceOn
      (fun N t => (regroupedActualXiPrefix grouped allocation N t).value)
      (fun t => (actualXiTJet t).value) (Set.Ioi (1 / 4))
  firstConverges :
    LocallyUniformlyConvergesSequenceOn
      (fun N t => (regroupedActualXiPrefix grouped allocation N t).first)
      (fun t => (actualXiTJet t).first) (Set.Ioi (1 / 4))
  secondConverges :
    LocallyUniformlyConvergesSequenceOn
      (fun N t => (regroupedActualXiPrefix grouped allocation N t).second)
      (fun t => (actualXiTJet t).second) (Set.Ioi (1 / 4))

/-- Canonical packet conclusion through size three.  It records one-node
nonnegativity, all three two-node principal packets, and the full three-node
packet.  It deliberately does not assert positive definiteness. -/
structure ActualXiPickPSDThroughThree (x1 x2 x3 : ℝ) : Prop where
  one1 : 0 ≤ actualXiNodeP x1
  one2 : 0 ≤ actualXiNodeP x2
  one3 : 0 ≤ actualXiNodeP x3
  pair12 :
    IsPSD2 (actualXiNodeP x1)
      (pickEntry x1 (actualXiNodeP x1) x2 (actualXiNodeP x2))
      (actualXiNodeP x2)
  pair13 :
    IsPSD2 (actualXiNodeP x1)
      (pickEntry x1 (actualXiNodeP x1) x3 (actualXiNodeP x3))
      (actualXiNodeP x3)
  pair23 :
    IsPSD2 (actualXiNodeP x2)
      (pickEntry x2 (actualXiNodeP x2) x3 (actualXiNodeP x3))
      (actualXiNodeP x3)
  triple :
    IsPSD3 (actualXiNodeP x1)
      (pickEntry x1 (actualXiNodeP x1) x2 (actualXiNodeP x2))
      (pickEntry x1 (actualXiNodeP x1) x3 (actualXiNodeP x3))
      (actualXiNodeP x2)
      (pickEntry x2 (actualXiNodeP x2) x3 (actualXiNodeP x3))
      (actualXiNodeP x3)

/-- Exact external/analytic input package for the repaired theorem.  Every
field is a mathematical proposition about the locked publication, actual Xi,
the grouped C2 expansion, the source-specific reserve ledger, or the scalar
consequences needed by the finite determinant proof. -/
structure ActualXiOrderThreeInputs where
  verified : PublishedVerifiedHeightTheorem
  grouped : GroupedActualXiC2Expansion
  residual : CriticalMultiplicityResidual grouped.selectedReserve
  reserve : ActualXiReserveAllocation grouped
  diagonalPositive :
    GroupedActualXiC2Expansion → ∀ x : ℝ, 0 < x → 0 < actualXiNodeP x
  orderTwoPSD :
    (∀ ρ : ℂ, riemannZeta ρ = 0 → 0 < ρ.im →
      ρ.im ≤ verifiedHeight → ρ.re = 1 / 2) →
    GroupedActualXiC2Expansion →
      ∀ x y : ℝ, 0 < x → 0 < y →
        IsPSD2 (actualXiNodeP x)
          (pickEntry x (actualXiNodeP x) y (actualXiNodeP y))
          (actualXiNodeP y)
  distinctPairDetPositive :
    (∀ ρ : ℂ, riemannZeta ρ = 0 → 0 < ρ.im →
      ρ.im ≤ verifiedHeight → ρ.re = 1 / 2) →
    GroupedActualXiC2Expansion →
      ∀ x y : ℝ, 0 < x → 0 < y → x ^ 2 ≠ y ^ 2 →
        0 < pickDet2 x (actualXiNodeP x) y (actualXiNodeP y)
  paidC2Approximation :
    RegroupedActualXiC2Approximation grouped reserve
  reciprocalCurvature :
    SourceLockExact verified.sourceLock →
    (∀ ρ : ℂ, riemannZeta ρ = 0 → 0 < ρ.im →
      ρ.im ≤ verifiedHeight → ρ.re = 1 / 2) →
    (grouped' : GroupedActualXiC2Expansion) →
    CriticalMultiplicityResidual grouped'.selectedReserve →
    (allocation : ActualXiReserveAllocation grouped') →
    RegroupedActualXiC2Approximation grouped' allocation →
    (∀ t : ℝ, 1 / 4 < t → 0 ≤ reciprocalEnergy (actualXiTJet t)) →
      ∀ x1 x2 x3 : ℝ, 0 < x1 → 0 < x2 → 0 < x3 →
        x1 ^ 2 ≠ x2 ^ 2 → x1 ^ 2 ≠ x3 ^ 2 → x2 ^ 2 ≠ x3 ^ 2 →
        secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
          (1 / actualXiNodeP x1) (1 / actualXiNodeP x2)
          (1 / actualXiNodeP x3) ≤ 0
  companionCurvature :
    GroupedActualXiC2Expansion →
      ∀ x1 x2 x3 : ℝ, 0 < x1 → 0 < x2 → 0 < x3 →
        x1 ^ 2 ≠ x2 ^ 2 → x1 ^ 2 ≠ x3 ^ 2 → x2 ^ 2 ≠ x3 ^ 2 →
        secondDivDiff (x1 ^ 2) (x2 ^ 2) (x3 ^ 2)
          (x1 ^ 2 * actualXiNodeP x1)
          (x2 ^ 2 * actualXiNodeP x2)
          (x3 ^ 2 * actualXiNodeP x3) ≤ 0

/-- Exact full comparator statement: every positive packet is PSD through
sizes one, two, and three, including repeated nodes.  No order-four or
positive-definite assertion is present. -/
def ChallengeStatement : Prop :=
  ∀ inputs : ActualXiOrderThreeInputs,
    ∀ x1 x2 x3 : ℝ, 0 < x1 → 0 < x2 → 0 < x3 →
      ActualXiPickPSDThroughThree x1 x2 x3

end ChallengeDeps.XiPickOrderThreeConditional
