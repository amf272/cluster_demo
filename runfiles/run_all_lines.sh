#!/bin/bash

#SBATCH --job-name=job_array_example
#SBATCH --output=logs/example/%A_%a.out
#SBATCH --error=logs/example/%A_%a.err
#SBATCH --time=01:00:00  # Adjust time as needed
#SBATCH --mem=4G  # Adjust memory as needed
#SBATCH --cpus-per-task=1  # Adjust CPU count as needed

# run this with
# export COMMANDS_FILE=runfiles/commands.txt; sbatch --array=0-$(($(grep -c "" $COMMANDS_FILE)-1)) runfiles/run_all_lines.sh
# Read the command from the file corresponding to this job array index
CMD=$(sed -n "$(($SLURM_ARRAY_TASK_ID + 1))p" $COMMANDS_FILE)

echo "Running command: $CMD"
eval "$CMD"
