def get_sum(a,b):
    #good luck!
    return sum(range(min(a, b), max(a, b) + 1))

import codewars_test as test


@test.describe('Sum of numbers')
def desc1():
    @test.it('Sample tests')
    def it1():
        test.assert_equals(get_sum(0,1),1)
        test.assert_equals(get_sum(0,-1),-1)
