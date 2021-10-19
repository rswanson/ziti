class Model: 
    def __init__(self):
        self.answer = 42
    
    def main(self):
        return self

def test_model():
    model = Model()
    assert model.answer == 42