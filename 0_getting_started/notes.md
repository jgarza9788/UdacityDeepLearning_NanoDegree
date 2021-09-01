# notes

## creating an environment
```CMD/TERMINAL
conda create -n <NAME> python=<version>
```
```CMD/TERMINAL
conda create -n example python=3
```

conda create -n VacasaAlert python=3.9

## use environment
```CMD/TERMINAL
source activate <NAME>
```
```CMD/TERMINAL
source activate example
```

## deleting environment
```CMD/TERMINAL
conda env remove -n ENV_NAME
```
```CMD/TERMINAL
conda env remove -n VacasaAlert
```

## list environments
```CMD/TERMINAL
conda info --envs
```

## install packages/modules
```CMD/TERMINAL
conda install numpy pandas matplotlib
```
```CMD/TERMINAL
conda install jupyter notebook
```
```CMD/TERMINAL
conda install PACKAGE_NAME
```

## remove package
```CMD/TERMINAL
conda remove PACKAGE_NAME
```

## update package
```CMD/TERMINAL
conda update package_name
```

## search packages
```CMD/TERMINAL
conda search '*beautifulsoup*'
```

## list packages
```CMD/TERMINAL
conda list
```

## create and add packages to environment
```CMD/TERMINAL
conda create -n env_name [python=X.X] [LIST_OF_PACKAGES]
```

## exit environment
``` CMD/TERMINAL
# For  conda 4.6 and later versions on Linux/macOS/Windows, use
conda deactivate
#For conda versions prior to 4.6 on Linux/macOS, use 
source deactivate
#For conda versions prior to 4.6 on Windows, use 
deactivate
```

## exporting environment
```CMD/TERMINAL
conda env export
```
```CMD/TERMINAL
conda env export > environment.yaml
```

```CMD/TERMINAL
conda env create -f environment.yaml 
# create an environment with the name environment.yaml
```

