import numpy as np
age = loadtxt('participants.tsv', skiprows=1, usecols=1)
mean age = sum(age)/len(age)
np.savetxt("demeaned_age.txt", age-mean_age)
print("done!")