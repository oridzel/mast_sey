
<img src="misc/MAST-SEY_logo_sm.png" width="50%">


MAST-SEY is an open-source Monte Carlo code capable of predicting secondary electron emission using input data generated entirely from first principle (density functional theory) calculations. It utilises the complex dielectric function and Penn's theory for inelastic scattering processes, and relativistic Schrödinger theory by means of partial-wave expansion method to govern elastic scattering. It allows to not only use the momentum independent (q=0) dielectric function but also to include explicitly calculated momentum dependence, as well as to utilise first-principle density of states in secondary electron generation.  
For more detail please refer to the paper which this code accompanies: Maciej P. Polak and Dane Morgan, *MAST-SEY: MAterial Simulation Toolkit for Secondary Electron Yield. A Monte Carlo Approach to Secondary Electron Emission Based On Complex Dielectric Functions*, Comp. Mat. Sci. XXX, xx, (2021) (https://doi.org/10.1016/xx.xx.xx), which is to be cited whenever the code is used.

## Installation

1. Download the source code and compile. Optimal performance is achieved with Intel compilers:
```bash
icc -std=c++11 -g -O3 -o mast_sey mast_sey.cpp
```
Compiling with `gcc` is also possible, although the code works twice slower, version > 6.2 of `gcc` is required:
```bash
g++ -std=c++11 -g -O3 -o mast_sey mast_sey.cpp
```
`-Ofast` and architecture specific optimization flags may be used but the performance is unlikely to get noticeably better.
2. [Download the elsepa code](https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/w4hm5vymym-1.zip) (https://doi.org/10.1016/j.cpc.2004.09.006, https://doi.org/10.1016/j.cpc.2020.107704).
3. Unzip the downloaded `w4hm5vymym-1.zip` file and unpack the file inside:
```bash
unzip w4hm5vymym-1.zip
unzip elsepa-2020.zip
```
4. Move the `elsepa2020.patch` patch inside the `elsepa-2020` directory and apply it:
```bash
cd elsepa-2020
patch < elsepa.patch
```
If for some reason you wish to use the old version of `elsepa` the `elsepa_old.patch` is available too.
5. Compile the patched `elsepa`:
```bash
ifort -o elsepa elscata.f
```
or
```bash
gfortran -o elsepa elscata.f
```
6. Add write permissions to all density files for convenience:
```bash
chmod +w z_*
```
7. Make sure that the necessary files are executable:
```bash
chmod +x /path/to/your/elsepa/elsepa /path/to/your/mastsey/mast_sey /path/to/your/mastsey/getDDCS
```
8. Add the directories containing compiled elsepa and mast_sey to your PATH.
```bash
export PATH=/path/to/your/elsepa:/path/to/your/mastsey:${PATH}
```    

## Usage

The code is executed in two steps:
### The "prepare" step
This step postprocesses the input files to a form convenient for the second step to use. It takes the dielectric function `eps.in` or the energy loss function `elf.in`, and using the parameters contained in `material.in`, prepares the cumulative integrals of cross sections. These results are stored in `inelastic.in` and `elastic.in`. Additionally a file `mfp.plot` is generated, and allows for a convenient plotting of the inelastic and elastic mean free paths, which are generated in this step as well. This step is performed only once for each case.

The command below is an example of how to run the "prepare" step:
```bash
mast_sey prepare -e 1000 100 -i 100 50 -qdep DFT -elastic P DHFS FM
```
The user should be greeted with the default MAST-SEY output screen. It contains the basic info along with a short feedback on the chosen options and files used. If a basic error is detected, it will be displayed here. In all the input values are correct, a progress bar on the bottom should start filling up (although for accurate calculations it may take a while for even the first bar to appear).

These examples showcase most of the capabilities of the code.
They serve as a tutorial for thr code and also allow to reproduce the results presented in the paper which this code accompanies:
Maciej P. Polak and Dane Morgan, *MAST-SEY: MAterial Simulation Toolkit for Secondary Electron Yield. A Monte Carlo Approach to Secondary Electron Emission Based On Complex Dielectric Functions*, Comp. Mat. Sci. XXX, xx, (2021) (https://doi.org/10.1016/xx.xx.xx)

Two material systems are considered: copper and aluminium.

Each directory contains all the neccessary input files and a set of commands that should be executed. It also contains a directory with the calculations already completed, for comparison.

It is highly recommended to execute the code on multiple cores for efficiency. For that users might find particularily helpful the [GNU Parralel](https://www.gnu.org/software/parallel/) software.

