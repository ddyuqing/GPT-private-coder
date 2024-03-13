import fire
import sys

from private_eval.data import HUMAN_EVAL
from private_eval.evaluation import evaluate_functional_correctness


def entry_point(
    sample_file: str,
    k: str = "1,10,100",
    n_workers: int = 4,
    timeout: float = 3.0,
    problem_file: str = HUMAN_EVAL,
):
    """
    Evaluates the functional correctness of generated samples, and writes
    results to f"{sample_file}_results.jsonl.gz"
    """
    print("sample_file:",sample_file)
    print("k:",k)
    print("n_workers:",n_workers)
    print("timeout:",timeout)
    print("problem_file:",problem_file)
    if isinstance(k,str):
        k = list(map(int, k.split(",")))
    elif isinstance(k,tuple):
        k = list(map(int,k))
    elif isinstance(k,int):
        k = int(k)
    else:
        raise NotImplementedError(f"type(k) is : {type(k)}, expect <list(str)> ,<class 'tuple'> or <class 'int'>")
    results = evaluate_functional_correctness(sample_file, k, n_workers, timeout, problem_file)
    print(results)


def main():
    fire.Fire(entry_point)


sys.exit(main())
