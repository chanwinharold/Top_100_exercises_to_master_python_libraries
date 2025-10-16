import numpy as np

scores = np.random.randint(0, 100, 100)

q1 = np.percentile(scores, 25)
q2 = np.percentile(scores, 50)
q3 = np.percentile(scores, 75)

scores.sort()

print(scores)
print(q1)
print(q2)
print(q3)
print(scores[-5:])





