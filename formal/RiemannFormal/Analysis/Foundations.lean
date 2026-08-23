import RiemannFormal.Upstream
import Mathlib.Analysis.MellinTransform

open Complex Set

namespace RiemannFormal.Analysis

/-- Real-valued detector on the positive multiplicative axis. -/
abbrev Detector := ℝ → ℝ

/-- A detector bundled with the semantic ID fixed by the reviewed registry. -/
structure FixedDetector where
  semanticId : String
  value : Detector

/-- The open right half-plane used by the shifted Mellin consumers. -/
def rightHalfPlane : Set ℂ := {s | 0 < s.re}

/-- An open vertical strip. -/
def verticalStrip (a b : ℝ) : Set ℂ := {s | a < s.re ∧ s.re < b}

/-- A singularity is nonremovable when no analytic germ exists at the point. -/
def NonremovableAt (F : ℂ → ℂ) (s₀ : ℂ) : Prop := ¬ AnalyticAt ℂ F s₀

/-- Eventual nonnegativity on the positive axis, with the threshold explicit. -/
def EventuallyNonnegative (f : Detector) : Prop :=
  ∃ X₀ : ℝ, 1 ≤ X₀ ∧ ∀ x : ℝ, X₀ ≤ x → 0 ≤ f x

/-- Positive part of a real detector. -/
def positivePart (f : Detector) (x : ℝ) : ℝ := max (f x) 0

/-- Negative mass density of a real detector. -/
def negativePart (f : Detector) (x : ℝ) : ℝ := max (-f x) 0

@[simp] theorem positivePart_nonneg (f : Detector) (x : ℝ) : 0 ≤ positivePart f x := by
  simp [positivePart]

@[simp] theorem negativePart_nonneg (f : Detector) (x : ℝ) : 0 ≤ negativePart f x := by
  simp [negativePart]

/-- Pointwise Jordan decomposition of a real detector. -/
theorem detector_eq_positivePart_sub_negativePart (f : Detector) (x : ℝ) :
    f x = positivePart f x - negativePart f x := by
  by_cases h : 0 ≤ f x
  · simp [positivePart, negativePart, h]
  · have h' : f x ≤ 0 := le_of_not_ge h
    simp [positivePart, negativePart, h, h']

end RiemannFormal.Analysis
