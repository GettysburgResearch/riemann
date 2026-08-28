import Mathlib.NumberTheory.ArithmeticFunction.Moebius
import Mathlib.NumberTheory.ArithmeticFunction.VonMangoldt
import Mathlib.Data.Complex.Basic
import RiemannFormal.Statement.OpenCuts

namespace RiemannFormal.Arithmetic

open scoped ArithmeticFunction.Moebius

/-- Scientific source roles are type indices in the trusted arithmetic layer. -/
inductive SourceRole where
  | nativeSource
  | auxiliaryPositiveSource
  | signedObservation
  | childResponse
  | childCapacity
  deriving DecidableEq, Repr

/-- Bootstrap-compatible unbundled source metadata. New proofs should prefer `Source`. -/
structure TypedSource where
  role : SourceRole
  coefficient : ℕ → ℝ

/-- An arithmetic source whose scientific role is part of its type.

The role index prevents *implicit* substitution of one source sort for another.
The constructor and coefficient projection are public, so the index alone is not
a provenance theorem: code can explicitly extract coefficients and reconstruct
them at another role.  Any conclusion-facing promotion therefore needs a
separate semantic identity or provenance proof. -/
structure Source (role : SourceRole) (R : Type*) [Zero R] where
  coefficient : ArithmeticFunction R

abbrev NativeSource (R : Type*) [Zero R] := Source .nativeSource R
abbrev AuxiliaryPositiveSource (R : Type*) [Zero R] := Source .auxiliaryPositiveSource R
abbrev SignedObservation (R : Type*) [Zero R] := Source .signedObservation R
abbrev ChildResponse (R : Type*) [Zero R] := Source .childResponse R
abbrev ChildCapacity (R : Type*) [Zero R] := Source .childCapacity R

/-- Explicit coefficient reconstruction at another role.  This declaration is
kept visible to record the exact API boundary: role indices block accidental
coercions, not deliberate provenance laundering. -/
def rebuildAtRole {r₁ r₂ : SourceRole} {R : Type*} [Zero R]
    (source : Source r₁ R) : Source r₂ R :=
  ⟨source.coefficient⟩

@[simp]
theorem rebuildAtRole_coefficient {r₁ r₂ : SourceRole} {R : Type*} [Zero R]
    (source : Source r₁ R) :
    (rebuildAtRole (r₂ := r₂) source).coefficient = source.coefficient := rfl

/-- A detector represented by one coefficient family.  The structure records
the data shape expected by a fixed-detector API.  It does not, by itself, prove
that the value was chosen before a hypothetical zero or proof horizon. -/
structure FixedArithmeticDetector (R : Type*) [Zero R] where
  semanticId : String
  coefficient : ArithmeticFunction R

/-- A detector whose coefficients may depend on a complex query. -/
structure MovingArithmeticDetector (R : Type*) [Zero R] where
  semanticId : String
  choose : ℂ → ArithmeticFunction R

/-- The semantic quantifier-order property required of a moving presentation. -/
def MovingArithmeticDetector.QueryIndependent {R : Type*} [Zero R]
    (detector : MovingArithmeticDetector R) : Prop :=
  ∀ z w : ℂ, detector.choose z = detector.choose w

/-- A fixed coefficient family gives a query-independent moving presentation. -/
def FixedArithmeticDetector.asConstantMoving {R : Type*} [Zero R]
    (detector : FixedArithmeticDetector R) : MovingArithmeticDetector R where
  semanticId := detector.semanticId
  choose := fun _ => detector.coefficient

@[simp]
theorem FixedArithmeticDetector.asConstantMoving_queryIndependent
    {R : Type*} [Zero R] (detector : FixedArithmeticDetector R) :
    MovingArithmeticDetector.QueryIndependent detector.asConstantMoving := by
  intro z w
  rfl

/-- A labelled prime occurrence. Distinct labels may project to the same prime. -/
structure PrimeLabel where
  prime : ℕ
  isPrime : prime.Prime
  copy : ℕ

/-- Dilation by an integer scale. This is finite arithmetic data, not a Dirichlet-series operation. -/
def dilation {R : Type*} [Zero R] (q : ℕ) (f : ArithmeticFunction R) :
    ArithmeticFunction R where
  toFun n := if q ∣ n then f (n / q) else 0
  map_zero' := by simp

@[simp]
theorem dilation_apply_of_dvd {R : Type*} [Zero R] (q : ℕ)
    (f : ArithmeticFunction R) {n : ℕ} (h : q ∣ n) :
    dilation q f n = f (n / q) := by
  simp [dilation, h]

@[simp]
theorem dilation_apply_of_not_dvd {R : Type*} [Zero R] (q : ℕ)
    (f : ArithmeticFunction R) {n : ℕ} (h : ¬ q ∣ n) :
    dilation q f n = 0 := by
  simp [dilation, h]

/-- Parity accumulated from a labelled subset. -/
def paritySign (k : ℕ) : ℤ := (-1) ^ k

@[simp]
theorem paritySign_zero : paritySign 0 = 1 := by simp [paritySign]

@[simp]
theorem paritySign_succ (k : ℕ) : paritySign (k + 1) = -paritySign k := by
  simp [paritySign, pow_succ]

/-- The Mathlib Möbius function coerced to rational coefficients. -/
def moebiusQ : ArithmeticFunction ℚ :=
  (ArithmeticFunction.moebius : ArithmeticFunction ℚ)

@[simp]
theorem moebiusQ_eq_zero_of_not_squarefree {n : ℕ} (h : ¬Squarefree n) :
    moebiusQ n = 0 := by
  simp [moebiusQ, ArithmeticFunction.moebius_eq_zero_of_not_squarefree h]

/-- Direct role equality is impossible.  This is only a type-level firewall;
`rebuildAtRole` records why it is not a provenance theorem. -/
@[simp]
theorem native_ne_auxiliary :
    SourceRole.nativeSource ≠ SourceRole.auxiliaryPositiveSource := by decide

@[simp]
theorem response_ne_capacity :
    SourceRole.childResponse ≠ SourceRole.childCapacity := by decide

@[simp]
theorem signedObservation_ne_auxiliaryPositive :
    SourceRole.signedObservation ≠ SourceRole.auxiliaryPositiveSource := by decide

end RiemannFormal.Arithmetic
