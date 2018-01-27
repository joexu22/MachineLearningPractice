# Conda Install Notes
1. Check If Conda Is Installed
```
conda -V
```

2. Update Conda
```
conda update conda
```

3. Create a Virtual Environment
```
conda create -n <yourenvname> <python=x.x> [package]
```

4. Activate Virtual Environment
```
source activate <yourenvname>
```

5. Install Python Packages to Virtual Enviroment
```
conda install -n <yourenvname> [package]
```

6. Deactivate Virtual Environment
```
source deactivate
```

7. Delete Virtual Environment
```
conda remove -n <yourenvname> -all
```