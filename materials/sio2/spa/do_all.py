import os
from multiprocessing import Pool

energies = [20, 30, 40, 50, 100, 200, 300, 500, 700, 980]

def run_mast(i):
	print(energies[i])
	os.system("mast_sey -e {} -m 1000 -ins -dos -vale 16 -nostep > out/{}.stdout.txt".format(energies[i],energies[i]))


if __name__ == '__main__':
	with Pool(processes=11) as pool:
		pool.map(run_mast, range(len(energies)))

