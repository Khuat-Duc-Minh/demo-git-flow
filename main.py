"""main.py
Wire the flow together: generate -> sort -> find
"""
import argparse
from gen_data import generate_data
from sort_data import sort_data
from find_data import binary_search
import random

def main(n: int, min_v: int, max_v: int, method: str, target: int | None, seed: int | None):
    data = generate_data(n=n, min_v=min_v, max_v=max_v, seed=seed)
    print(f"Generated {len(data)} values (first 20): {data[:20]}")


    sorted_data = sort_data(data, choice=method)
    print(f"Sorted (first 20): {sorted_data[:20]}")


    if target is None:
        # pick a random target from the list (or one outside)
        target = random.choice(sorted_data) if sorted_data else None


    if target is None:
        print("No data to search.")
        return


    idx = binary_search(sorted_data, target)
    if idx >= 0:
        print(f"Found target {target} at index {idx} (0-based)")
    else:
        print(f"Target {target} not found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="gen -> sort -> find demo")
    parser.add_argument("--n", type=int, default=50)
    parser.add_argument("--min", dest="min_v", type=int, default=0)
    parser.add_argument("--max", dest="max_v", type=int, default=100)
    parser.add_argument("--method", type=str, default="bubble", help="sort method: bubble, quick, merge")
    parser.add_argument("--target", type=int, default=None)
    parser.add_argument("--seed", type=int, default=None)
    args = parser.parse_args()


    main(args.n, args.min_v, args.max_v, args.method, args.target, args.seed)