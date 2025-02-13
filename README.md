## Installation
```bash
pip install -e .
```

## Usage
### running a single command interactively (in a shell, on the cluster)

1. start an salloc (working for one day)
```bash
salloc --time=10:00:00 --partition=full --cpus-per-task=2 --mem=1G
```
2. run command
```bash
python -m scripts.train_models main --method=diff_opt --n_epochs=0.1
```

### run single command from slurm (doesn't die if you close your session)
```bash
sbatch –-wrap 'python -m scripts.train_models main --method=diff_opt --n_epochs=10'
```

### run single command from slurm, will die if you close your window or cluster crashes
```bash
srun python -m scripts.train_models main --method=diff_opt --n_epochs=10
```


### submitting jobs with submitit
```bash
python -m scripts.train_models submit
```

### submitting all jobs in commands.txt
```bash
export COMMANDS_FILE=commands.txt; sbatch --array=0-$(($(grep -c "" $COMMANDS_FILE)-1)) run_all_lines.sh
```


## Code invariants
1. imports in this directory should work the same way with or without pip installing
    > don't want to make things in scripts/notebooks look different than elsewhere
2.  imports should work with or without pyproject.toml
    > want to be able to add pyproject.toml as an afterthought without having to refactor stuff
3. imports in this top-level directory should work the same as anywhere else after pip installing
    > after pip installing, can copy script code anywhere / use it as example code for your package
4. things are always run / act as if they are run from the top level directory
