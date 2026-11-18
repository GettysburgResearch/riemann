-- Independent finite integer certificate for the pressure-aware boundary bound.
-- Data: MIT-licensed839-v1 certificate inputs; see experiments/inputs/839_first_window/PROVENANCE.json.
-- This checks integer knot inequalities, NOT the analytic/local/global/zeta theorem.
import Std
set_option maxRecDepth 1000000
set_option maxHeartbeats 5000000
namespace ObservatoryBoundary

def knots : List (List (List Int)) := [[[0, 0, 186, 976, 0, 0, 0, 0, (-1914), (-1005), 0, 0, 0, 0], [0, 0, 334, 1483, 0, 0, 0, 0, 0, (-920), (-264), 0, 0, 0], [0, 0, 2026, 2124, 0, 0, 0, 0, 0, (-432), 0, 0, 0, 0]], [[0, 0, (-736), (-177), 0, 0, 0, 0, 124, 0, 0, 0, 0, 0], [0, 0, 0, (-495), 0, 0, 0, 0, 0, 524, 111, 0, 0, 0], [0, 0, (-924), (-11), 0, 0, 0, 0, 0, 0, 773, 0, 0, 0]], [[0, 0, 550, (-799), 0, 0, 0, 0, 1790, 1005, 0, 0, 0, 0], [0, 0, (-334), (-988), 0, 0, 0, 0, 0, 396, 153, 0, 0, 0], [0, 0, (-1102), (-2113), 0, 0, 0, 0, 0, 432, (-773), 0, 0, 0]], [[0, 0, 550, (-799), 0, 0, 0, 0, 1790, 1005, 0, 0, 0, 0], [0, 0, (-334), (-988), 0, 0, 0, 0, 0, 396, 153, 0, 0, 0], [0, 0, (-1102), (-2113), 0, 0, 0, 0, 0, 432, (-773), 0, 0, 0]], [[0, 0, (-736), (-177), 0, 0, 0, 0, 124, 0, 0, 0, 0, 0], [0, 0, 0, (-495), 0, 0, 0, 0, 0, 524, 111, 0, 0, 0], [0, 0, (-924), (-11), 0, 0, 0, 0, 0, 0, 773, 0, 0, 0]], [[0, 0, 186, 976, 0, 0, 0, 0, (-1914), (-1005), 0, 0, 0, 0], [0, 0, 334, 1483, 0, 0, 0, 0, 0, (-920), (-264), 0, 0, 0], [0, 0, 2026, 2124, 0, 0, 0, 0, 0, (-432), 0, 0, 0, 0]]]
def knot (r ty k : Nat) : Int := ((knots[r]?.getD [])[ty]?.getD [])[k]?.getD 0
def part (q ty k : Nat) : Int := ((List.range (q+1)).map (fun r => knot r ty k)).foldl (· + ·) 0

def shapeOK : Bool := knots.length == 6 && knots.all (fun rows => rows.length == 3 && rows.all (fun row => row.length == 14))
def endpointsOK : Bool := (List.range 6).all (fun r => (List.range 3).all (fun ty =>
  decide (knot r ty 0 = 0 ∧ knot r ty 1 = 0 ∧ knot r ty 13 = 0)))
def pressureKnotsOK : Bool := (List.range 5).all (fun q => (List.range 3).all (fun ty =>
  (List.range 13).all (fun j => let k := j+1
    decide (40 * part q ty k ≤ 6219 * (Int.ofNat (5-q)) * (5 * (Int.ofNat k)-4) ∧
      -(40 * part q ty k) ≤ 6219 * (Int.ofNat (q+1)) * (5 * (Int.ofNat k)-4)))))
def smallChainsOK : Bool := (List.range 6).all (fun j => let m := Int.ofNat (j+1)
  decide (694330*m-317169*(m-1) ≤ 2580135))

theorem shape_checked : shapeOK = true := by decide
theorem endpoints_checked : endpointsOK = true := by decide
theorem pressure_knots_checked : pressureKnotsOK = true := by decide
theorem small_chains_checked : smallChainsOK = true := by decide
theorem constant_checked : (12*69433-51*6219 : Int) = 516027 := by decide
#print axioms shape_checked
#print axioms endpoints_checked
#print axioms pressure_knots_checked
#print axioms small_chains_checked
#print axioms constant_checked
end ObservatoryBoundary
