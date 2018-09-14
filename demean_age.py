import numpy as np
age = np.loadtxt('participants.tsv', skiprows=1, usecols=1)
meanage = sum(age)/len(age)
np.savetxt("demeaned_age.txt", age-meanage)
print("done!")