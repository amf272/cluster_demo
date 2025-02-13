import time

import fire
import submitit
import tqdm.auto as tqdm

import beepseek.train

CPUS_PER_TASK = 1
MEM_PER_TASK = 0.1


def train_model(method="diff_opt", n_epochs=1):
    print(f"training model with method={method} and n_epochs={n_epochs}")
    time.sleep(n_epochs)
    print(f"done training model with method={method} and n_epochs={n_epochs}")
    return method, n_epochs


def main(method="diff_opt", n_epochs=1, use_beepseek=False):
    # alternatively
    if use_beepseek:
        return beepseek.train.complicated_train_model(method=method, n_epochs=n_epochs)
    else:
        return train_model(method=method, n_epochs=n_epochs)


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

    n_epochss = [
        1,
        10,
        15,
    ]

    jobs = []
    with executor.batch():
        for method in methods:
            for n_epochs in n_epochss:
                print(f"submitting {method} {n_epochs}")

                job = executor.submit(
                    main,
                    method=method,
                    n_epochs=n_epochs,
                )
                jobs.append(job)

    for job in tqdm.tqdm(jobs):
        print(job.result())


if __name__ == "__main__":
    """
    Usage:
    python -m scripts.train_models main --method=diff_opt --n_epochs=0.1
    python -m scripts.train_models submit
    """
    fire.Fire()
