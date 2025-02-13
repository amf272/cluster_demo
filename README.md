## Installation
```bash
pip install -e .
```

## Usage
running a single command interactively (in a shell, on the cluster)
```bash
python -m scripts.train_models main --method=diff_opt --n_epochs=0.1
```

submitting jobs to slurm
```bash
python -m scripts.train_models submit
```

submitting all jobs in commands.txt
```bash
export COMMANDS_FILE=commands.txt; sbatch --array=0-$(($(grep -c "" $COMMANDS_FILE)-1)) run_all_lines.sh
```


## Invariants
- imports in this directory should work the same way with or without pip installing
    - don't want to make things in scripts/notebooks look different than elsewhere
- imports in this top-level directory should work the same as anywhere else after pip installing
    - after pip installing, can copy script code anywhere / use it as example code for your package
- 
