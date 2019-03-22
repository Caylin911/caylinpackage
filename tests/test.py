from mypackage import myFunction

def test_bubble_sort():
    """
    make sure top_n works correctly
    """

    assert myFunction.bubble_sort([8, 3, 2, 7, 4]) == [8, 7, 4, 3, 2], 'incorrect'
    assert myFunction.bubble_sort([10, 1, 12, 9, 2]) == [12, 10, 9, 2, 1], 'incorrect'
    assert myFunction.bubble_sort([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1], 'incorrect'

def test_merge_sort():
    """
    make sure top_n works correctly
    """

    assert myFunction.merge_sort([8, 3, 2, 7, 4]) == [8, 7, 4, 3, 2], 'incorrect'
    assert myFunction.merge_sort([10, 1, 12, 9, 2]) == [12, 10, 9, 2, 1], 'incorrect'
    assert myFunction.merge_sort([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1], 'incorrect'

def test_quick_sort():
    """
    make sure top_n works correctly
    """

    assert myFunction.quick_sort([8, 3, 2, 7, 4]) == [8, 7, 4, 3, 2], 'incorrect'
    assert myFunction.quick_sort([10, 1, 12, 9, 2]) == [12, 10, 9, 2, 1], 'incorrect'
    assert myFunction.quick_sort([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1], 'incorrect'

def test_sum_array():
    """
    make sure top_n works correctly
    """

    assert myFunction.sum_array([8, 3, 2, 7, 4]) == 24, 'incorrect'
    assert myFunction.sum_array([10, 1, 12, 9, 2]) == 34, 'incorrect'
    assert myFunction.sum_array([1, 2, 3, 4, 5]) == 15, 'incorrect'

def test_fibonacci():
    """
    make sure top_n works correctly
    """

    assert myFunction.fibonacci(3) == 2, 'incorrect'
    assert myFunction.fibonacci(2) == 1, 'incorrect'
    assert myFunction.fibonacci(5) = 3, 'incorrect'

def test_factorial():
    """
    make sure top_n works correctly
    """

    assert myFunction.factorial(4) == 24, 'incorrect'
    assert myFunction.factorial(8) == 40320, 'incorrect'
    assert myFunction.factorial(3) == 6, 'incorrect'

def test_reverse():
    """
    make sure top_n works correctly
    """

    assert myFunction.reverse('word') == ('drow'), 'incorrect'
    assert myFunction.reverse('I am caylin') == ('I ma nilyac'), 'incorrect'
    assert myFunction.reverse('working') == ('gnikrow'), 'incorrect'
