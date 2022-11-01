import  pytest
from main import get_secret_num, get_clues

class TestFuncion:      
    def test_get_secret_num_1(self):
        res = get_secret_num()
        assert len(res) == 3
    def test_get_secret_num_2(self):
         res = get_secret_num()
         res_chec = (res[0] != res[1] != res[2])
         assert res_chec == True 
    
    test_param =[
    ('123','245', 'Pico'),
    ('123','312', 'Pico Pico Pico'),
    ('123','145', 'Fermi'),
    ('123','456', 'Bagels'),
    ('123','156', 'Bagels')]
    @pytest.mark.parametrize('a, b, result', test_param) 
    def test_get_clues(self,a,b,result):
        res = get_clues(a, b)
        assert res == result
    
if __name__ == "__main__":
    pytest.main()
