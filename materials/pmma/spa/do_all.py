import os
from multiprocessing import Pool

energies = [20, 25, 30, 35, 40, 45, 50, 100, 250, 500, 750, 900]

def run_mast(i):
	print(energies[i])
	os.system("mast_sey -e {} -m 1000 -ins -vale 40 -nostep > out/e{}.stdout.txt".format(energies[i],energies[i]))


if __name__ == '__main__':
	with Pool(processes=8) as pool:
		pool.map(run_mast, range(len(energies)))

