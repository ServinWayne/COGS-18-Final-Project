# This test is written for the max_score function. It will check if the function is
# callable and then check that the input score is a intager. I did not write a check
# for the output, because the output will ~always~ be a string as long as the input is a int.
def test_max_score():
    assert callable(max_score)
    assert isinstance(score, int)
    

# This test is written for the run_test function. It will check if the function is
# callable, and then check to see if the input of questions in thus function is a list.
def test_run_test():
    assert callable(run_test)
    assert isinstance(questions, list)


