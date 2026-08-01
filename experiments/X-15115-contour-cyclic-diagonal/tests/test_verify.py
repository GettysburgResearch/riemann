import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from verify import verify

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads((ROOT/"certificates/cyclic-order4.json").read_text())
    def test_pass(self):
        self.assertEqual(verify(copy.deepcopy(self.data))["status"],
                         "CERTIFIED_CONTOUR_CYCLIC_OBJECT_AND_DIAGONAL_GAP")
    def bad(self,mut):
        d=copy.deepcopy(self.data); mut(d)
        with self.assertRaises(ValueError):verify(d)
    def test_wrong_moment(self):self.bad(lambda d:d["orders"].__setitem__("4",0))
    def test_wrong_direct(self):self.bad(lambda d:d.__setitem__("order_four_direct",0))
    def test_wrong_disconnected(self):self.bad(lambda d:d.__setitem__("order_four_disconnected",0))
    def test_false_compatible(self):self.bad(lambda d:d.__setitem__("one_contour_order_four_compatible",0))
    def test_alt_not_distinct(self):self.bad(lambda d:d.__setitem__("one_contour_order_four_alternative",d["order_four_direct"]))
    def test_bad_majorant(self):self.bad(lambda d:d.__setitem__("series_majorant",2))
    def test_bad_radius(self):self.bad(lambda d:d.__setitem__("series_radius",1))
    def test_singular_basis(self):self.bad(lambda d:d.__setitem__("basis_change",[[1,1],[1,1]]))
    def test_nonpositive_gram(self):self.bad(lambda d:d.__setitem__("gram",[[1,2],[2,1]]))
    def test_boolean(self):self.bad(lambda d:d["gram"][0].__setitem__(0,True))
if __name__=="__main__":unittest.main()
