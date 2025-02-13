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

    > want to be able to pip install as an afterthought without having to refactor stuff
2.  imports should work with or without pyproject.toml
    > want to be able to add pyproject.toml as an afterthought without having to refactor stuff
3. imports in this top-level directory should work the same as anywhere else after pip installing
    > after pip installing, can copy script code anywhere / use it as example code for your package
4. things are always run / act as if they are run from the top level directory
5. readily "deployable" as a python package by deleting all experiment files (scripts, notebooks, etc)
    > don't put package-specific code in side "project" (beepseek), nothing inside beepseek should import/depend on scripts / notebooks / top-level stuff etc
6. avoid hardcoded paths in "project" files (inside beepseek)
7. generally should be flexible, the same exact code should work with / without pyproject, with / without pip install, with / without slurm, and be intuitive based on the directory structure
8. should be quick to onboard someone
    > should be able to quickly get same exact environment / same exact files as your collaborators, some things like data linking instructions should be in the readme