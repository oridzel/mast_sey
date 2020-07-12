
<img src="MAST-SEY_logo_sm.png" width="50%">

MAST-SEY is an open-source Monte Carlo code capable of predicting secondary electron emission using input data generated entirely from first principle (density functional theory) calculations. It utilises the complex dielectric function and Penn's theory for inelastic scattering processes, and relativistic Schrödinger theory by means of partial-wave expansion method to govern elastic scattering. It allows to not only use the momentum independent (q=0) dielectric function but also to include explicitly calculated momentum dependence, as well as to utilise first-principle density of states in secondary electron generation. 

## Installation

Download the source code and compile with `gcc`, version > 6.2 of `gcc` is recommended.
```bash
g++ -std=c++11 -g -O3 -o mast_sey_v25 mast_sey_v25_binary.cpp
```
1. Extract all the files to a convenient location
2. Add that location to your PATH:
```bash
export PATH=${PATH}:/complete/path/to/your/mast_sey
```    
    - you can add that line to your .bashrc of you dont want to execute it each time
3. If files are not executable make them executable:
```bash
chmod +x mast_sey_vXX mast_sey_prep elddcs
```

## Usage

The code is executed in two steps:
1. "prepare" stage:
This step postprocesses the input files to a form convenient for the second step to use. It takes the dielectric function `eps.in` or the energy loss function `elf.in`, and using the parameters contained in `material.in`, prepares the cumulative integrals of cross sections. These results are stored in `inelastic.in` and `elastic.in`. Additionally a file `mfp.plot` is generated, and allows for a convenient plotting of the inelastic and elastic mean free paths, which are generated in this step as well. This step is performed only once for each case.

The command below is an example of how to run the "prepare" step:
```bash
mast_sey -e 1000 100 -i 100 50 -qdep DFT P DHFS FM
```



```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

In this case
The `examples` directory containes all the neccesare file 
## Contributing


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
