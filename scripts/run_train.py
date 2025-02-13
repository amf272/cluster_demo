import time

import fire
import submitit
import tqdm.auto as tqdm

CPUS_PER_TASK = 1
MEM_PER_TASK = 0.1


def train_model(method="diff_opt", learning_rate=1):
    print(f"training model with method={method} and learning_rate={learning_rate}")
    time.sleep(learning_rate)
    print(f"done training model with method={method} and learning_rate={learning_rate}")
    return method, learning_rate


def main(method="diff_opt", learning_rate=1):
    return train_model(method, learning_rate)


def submit():
    executor = submitit.AutoExecutor(folder="submitit_logs/job_%A")
    executor.update_parameters(
        slurm_partition="full",
        name="mloptic",
        timeout_min=300,
        cpus_per_task=CPUS_PER_TASK,
        mem_gb=MEM_PER_TASK,
        gpus_per_node=0,
        # slurm_output="%A_%a.out",
        # slurm_error="%A_%a.err",
    )
    methods = [
        "pass_through",
        "diff_opt",
    ]

    learning_rates = [
        1,
        10,
        15,
    ]

    jobs = []
    with executor.batch():
        for method in methods:
            for learning_rate in learning_rates:
                print(f"submitting {method} {learning_rate}")

                job = executor.submit(
                    main,
                    method=method,
                    learning_rate=learning_rate,
                )
                jobs.append(job)

    for job in tqdm.tqdm(jobs):
        print(job.result())


if __name__ == "__main__":
    """
    Usage:
    python -m scripts.run_train main --method=diff_opt --learning_rate=0.1
    python -m scripts.run_train submit
    """
    fire.Fire()
