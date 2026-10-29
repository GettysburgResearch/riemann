/- Generated candidate; uncompiled; requires the count-source overlay. -/
import Submissions.arvi_density.Return.Formulas
set_option autoImplicit false
set_option linter.unnecessarySeqFocus false
namespace QRH.ArviDensity.Return
noncomputable section
def admission33_00_coefficients : Fin 1 → Fin 2 → ℝ := ![![(14665458/192583:ℝ), (14072875/192583:ℝ)]]
theorem admission33_00_identity (δ p : ℝ) : admissionGuard .C131 δ p 0 =
 Record12518109.Bernstein.bsum 0 1 (562915/770332:ℝ) admission33_00_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_00_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_00_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 0 := by
 rw [admission33_00_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_00_coefficients]
def admission33_01_coefficients : Fin 1 → Fin 2 → ℝ := ![![(9658300/192583:ℝ), (9258300/192583:ℝ)]]
theorem admission33_01_identity (δ p : ℝ) : admissionGuard .C131 δ p 1 =
 Record12518109.Bernstein.bsum 0 1 (92583/192583:ℝ) admission33_01_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_01_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_01_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 1 := by
 rw [admission33_01_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_01_coefficients]
def admission33_02_coefficients : Fin 1 → Fin 2 → ℝ := ![![(3131400614/120364375:ℝ), (120444661/4814575:ℝ)]]
theorem admission33_02_identity (δ p : ℝ) : admissionGuard .C131 δ p 2 =
 Record12518109.Bernstein.bsum 0 1 (120444661/481457500:ℝ) admission33_02_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_02_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_02_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 2 := by
 rw [admission33_02_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_02_coefficients]
def admission33_03_coefficients : Fin 2 → Fin 3 → ℝ := ![![(80709097700/192583:ℝ), (472072315600/577749:ℝ), (229997822500/577749:ℝ)], ![(78800011000/192583:ℝ), (460677620500/577749:ℝ), (224331587500/577749:ℝ)]]
theorem admission33_03_identity (δ p : ℝ) : admissionGuard .C131 δ p 3 =
 Record12518109.Bernstein.bsum 1 2 (17946527/46219920:ℝ) admission33_03_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_03_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_03_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 3 := by
 rw [admission33_03_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_03_coefficients]
def admission33_04_coefficients : Fin 2 → Fin 3 → ℝ := ![![(7159352104916/120364375:ℝ), (22045625536/192583:ℝ), (10599130168/192583:ℝ)], ![(1494524095801/24072875:ℝ), (23028441124/192583:ℝ), (11080908812/192583:ℝ)]]
theorem admission33_04_identity (δ p : ℝ) : admissionGuard .C131 δ p 4 =
 Record12518109.Bernstein.bsum 1 2 (1324891271/24072875000:ℝ) admission33_04_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_04_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_04_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 4 := by
 rw [admission33_04_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_04_coefficients]
def admission33_05_coefficients : Fin 2 → Fin 3 → ℝ := ![![(22387823673411/481457500:ℝ), (443994424937/4814575:ℝ), (35202311073/770332:ℝ)], ![(1994204826123/48145750:ℝ), (316555666153/3851660:ℝ), (31387206995/770332:ℝ)]]
theorem admission33_05_identity (δ p : ℝ) : admissionGuard .C131 δ p 5 =
 Record12518109.Bernstein.bsum 1 2 (6277441399/154066400000:ℝ) admission33_05_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_05_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_05_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 5 := by
 rw [admission33_05_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_05_coefficients]
def admission33_06_coefficients : Fin 2 → Fin 4 → ℝ := ![![(283755606795938923944/34306595997325:ℝ), (2458457686359269458232/102919787991975:ℝ), (94597113754725349456/4116791519679:ℝ), (30309041078513642000/4116791519679:ℝ)], ![(58135804316218970684/6861319199465:ℝ), (503881416097452272452/20583957598395:ℝ), (96981888350301800080/4116791519679:ℝ), (31086639727794728000/4116791519679:ℝ)]]
theorem admission33_06_identity (δ p : ℝ) : admissionGuard .C131 δ p 6 =
 Record12518109.Bernstein.bsum 1 3 (15154520539256821/205839575983950000:ℝ) admission33_06_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_06_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_06_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 6 := by
 rw [admission33_06_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_06_coefficients]
def admission33_07_coefficients : Fin 2 → Fin 3 → ℝ := ![![(11083767666502479616/69540397291875:ℝ), (853204916452537828/2781615891675:ℝ), (16407625735929230/111264635667:ℝ)], ![(2110838111501222351/13908079458375:ℝ), (162338070717079208/556323178335:ℝ), (15594024459767450/111264635667:ℝ)]]
theorem admission33_07_identity (δ p : ℝ) : admissionGuard .C131 δ p 7 =
 Record12518109.Bernstein.bsum 1 2 (311880489195349/2225292713340000:ℝ) admission33_07_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_07_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_07_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 7 := by
 rw [admission33_07_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_07_coefficients]
def admission33_08_coefficients : Fin 2 → Fin 4 → ℝ := ![![(407350029674357469992742533/1112646356670000000000:ℝ), (385378006974998606401908111/370882118890000000000:ℝ), (21854373627813580638287591/22252927133400000000:ℝ), (18341576808614597104517/59341139022400000:ℝ)], ![(250240495667653077997002101/445058542668000000000:ℝ), (239923692114066612568848067/148352847556000000000:ℝ), (6898916414716063507179151/4450585426680000000:ℝ), (14689915796147448846239/29670569511200000:ℝ)]]
theorem admission33_08_identity (δ p : ℝ) : admissionGuard .C131 δ p 8 =
 Record12518109.Bernstein.bsum 1 3 (18341576808614597104517/5934113902240000000000000:ℝ) admission33_08_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_08_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_08_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 8 := by
 rw [admission33_08_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_08_coefficients]
def admission33_09_coefficients : Fin 2 → Fin 4 → ℝ := ![![(7686961583842837077853/2781615891675000:ℝ), (1873284608802135384199/231801324306250:ℝ), (1752168017529049034179/222529271334000:ℝ), (1516732702129316931/593411390224:ℝ)], ![(5556226499557665286157/2225292713340000:ℝ), (5410432067544032721399/741764237780000:ℝ), (315937641048114801119/44505854266800:ℝ), (1365824926975806265/593411390224:ℝ)]]
theorem admission33_09_identity (δ p : ℝ) : admissionGuard .C131 δ p 9 =
 Record12518109.Bernstein.bsum 1 3 (273164985395161253/11868227804480000000:ℝ) admission33_09_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_09_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_09_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 9 := by
 rw [admission33_09_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_09_coefficients]
def admission33_10_coefficients : Fin 3 → Fin 4 → ℝ := ![![(206994169999834/4814575:ℝ), (593424739162334/4814575:ℝ), (67947264411050/577749:ℝ), (21575735503550/577749:ℝ)], ![(77853646659548/962915:ℝ), (222773191147048/962915:ℝ), (127275764243000/577749:ℝ), (40324322670500/577749:ℝ)], ![(7260999547614/192583:ℝ), (20729398901364/192583:ℝ), (19689533767500/192583:ℝ), (6221183013750/192583:ℝ)]]
theorem admission33_10_identity (δ p : ℝ) : admissionGuard .C131 δ p 10 =
 Record12518109.Bernstein.bsum 2 3 (4976946411/1540664000000:ℝ) admission33_10_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_10_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_10_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 10 := by
 rw [admission33_10_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_10_coefficients]
def admission33_11_coefficients : Fin 2 → Fin 3 → ℝ := ![![(3396966196913535628/23180132430625:ℝ), (783618278173623292/2781615891675:ℝ), (5017455700166782/37088211889:ℝ)], ![(645011710742459783/4636026486125:ℝ), (148642460011065512/556323178335:ℝ), (4753644602834330/37088211889:ℝ)]]
theorem admission33_11_identity (δ p : ℝ) : admissionGuard .C131 δ p 11 =
 Record12518109.Bernstein.bsum 1 2 (475364460283433/3708821188900000:ℝ) admission33_11_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_11_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_11_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 11 := by
 rw [admission33_11_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_11_coefficients]
def admission33_12_coefficients : Fin 1 → Fin 1 → ℝ := ![![(74999/20000000:ℝ)]]
theorem admission33_12_identity (δ p : ℝ) : admissionGuard .C131 δ p 12 =
 Record12518109.Bernstein.bsum 0 0 (74999/20000000:ℝ) admission33_12_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_12_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_12_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 12 := by
 rw [admission33_12_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_12_coefficients]
def admission33_13_coefficients : Fin 1 → Fin 1 → ℝ := ![![(39497419417/2000000000000:ℝ)]]
theorem admission33_13_identity (δ p : ℝ) : admissionGuard .C131 δ p 13 =
 Record12518109.Bernstein.bsum 0 0 (39497419417/2000000000000:ℝ) admission33_13_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_13_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_13_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 13 := by
 rw [admission33_13_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_13_coefficients]
def admission33_14_coefficients : Fin 1 → Fin 1 → ℝ := ![![(1/2:ℝ)]]
theorem admission33_14_identity (δ p : ℝ) : admissionGuard .C131 δ p 14 =
 Record12518109.Bernstein.bsum 0 0 (1/2:ℝ) admission33_14_coefficients (11/25:ℝ) (9/20:ℝ) (49/100:ℝ) (1/2:ℝ) δ p := by
 norm_num [admissionGuard,lowerM,upperM,naturalM,derivativeD,derivativeA,derivativeC,derivativeU,derivativeJ,V,D,A,C0,Z,U,oldD,oldC,countJ,countN,countT,RN,MN,DJ,branchB,branchL,branchCap,branchZ,isCap,c,h,theta,ell,x,y,kappa,dm,dp,d0,physicalB,physicalLambda,physicalCap,countCB,countCL,countCap,capPB,capPL,capPC,countNewB,countNewL,naturalK,sMinus,mMinus,reserve,numeratorCap,Record12518109.Bernstein.bsum,Record12518109.Bernstein.bterm,admission33_14_coefficients,Fin.sum_univ_succ] <;> ring
theorem admission33_14_pos {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) : 0 < admissionGuard .C131 δ p 14 := by
 rw [admission33_14_identity]
 apply Record12518109.Bernstein.bsum_pos (by norm_num) _ hδ hp
 intro i j
 fin_cases i <;> fin_cases j <;> norm_num [admission33_14_coefficients]
theorem admission33_all {δ p : ℝ} (hδ : δ ∈ Set.Icc (11/25:ℝ) (9/20:ℝ))
 (hp : p ∈ Set.Icc (49/100:ℝ) (1/2:ℝ)) (j : Fin 15) : 0 < admissionGuard .C131 δ p j := by
 fin_cases j
 · exact admission33_00_pos hδ hp
 · exact admission33_01_pos hδ hp
 · exact admission33_02_pos hδ hp
 · exact admission33_03_pos hδ hp
 · exact admission33_04_pos hδ hp
 · exact admission33_05_pos hδ hp
 · exact admission33_06_pos hδ hp
 · exact admission33_07_pos hδ hp
 · exact admission33_08_pos hδ hp
 · exact admission33_09_pos hδ hp
 · exact admission33_10_pos hδ hp
 · exact admission33_11_pos hδ hp
 · exact admission33_12_pos hδ hp
 · exact admission33_13_pos hδ hp
 · exact admission33_14_pos hδ hp
end
end QRH.ArviDensity.Return
