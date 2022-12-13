import os
from multiprocessing import Pool

energies = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,21,22,23,24,25,30,40,50]

def run_mast(i):
	print(energies[i])
	os.system("mast_sey -e {} -m 1000 -ins -dos -vale 40 > out/e{}.stdout.txt".format(energies[i],energies[i]))


if __name__ == '__main__':
	with Pool(processes=8) as pool:
		pool.map(run_mast, range(len(energies)))

