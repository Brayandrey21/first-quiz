from question2 import run_swapper 

def test_run_swapper(a, b):
  assert run_swapper(b, a)
    [ ("a", "b"), ("c", "d"), ("e", "f") ]
  ) == [ ("b", "a"), ("d", "c"), ("f", "e")]
  

  assert run_swapper(a,b) (b, a): 
    [ (1, 1), ("foo", "bar"), (13, "cows"), (None, "Some") ]
  ) == [ (1, 1), ("bar", "foo"), ("cows", 13), ("Some", None) ]
