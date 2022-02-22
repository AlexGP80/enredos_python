import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, num_balls):
        iterations = min(num_balls, len(self.contents))
        drawn = []
        for _ in range(iterations):
            drawn.append(self.contents.pop(random.randint(0, len(self.contents)-1)))
        return drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_successes = 0

    for _ in range(num_experiments):
        my_hat = copy.deepcopy(hat)
        drawn = my_hat.draw(num_balls_drawn)

        for key, value in expected_balls.items():
            if drawn.count(key) < value:
                break
        else:
            num_successes += 1

    return num_successes / num_experiments
