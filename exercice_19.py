import numpy as np

np.random.seed(123)
n = np.random.randint(0, 20, 20)

# 4 élèves × 5 matières
grades = n.reshape((4, 5))
print(grades, '\n\n')

# la note moyenne par élève
print(f"Note moyenne par élève : { grades.mean(axis=1) }")

# la note moyenne par matière
print(f"Note moyenne par matière : { grades.mean(axis=0) }")

# La note globale
print(f"La note globale : { (grades.mean(axis=1)).mean() }")

# la note maximale pour chaque élève
for i in range(grades.shape[0]):
    print(f"La note maximale de l'élève {i} est : {max(grades[i, :])}")

print()
# la note minimale pour chaque élève
for i in range(grades.shape[0]):
    print(f"La note minimale de l'élève {i} est : {min(grades[i, :])}")