import math
import unittest
import random 


def wallis(i):
    n=1
    temp = 1.0
    while(n<=i):
        temp *= float((4*n*n)/((4*n*n)-1))
        
        n=n+1

    return temp*2

def monte_carlo(i):
    ar_s=0
    ar_c=0
    for j in range(i):
        x = random.random()
        y = random.random()
        dist = math.dist(x,y)
        if(dist<=1):
            ar_c = ar_c + 1
        else:
            ar_s = ar_s + 1

    return 4*(ar_c/ar_s)
        

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        



if __name__ == "__main__":
    unittest.main()
