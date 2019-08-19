import argparse
import json


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--name", help="Name of the experiment", type=str, required=True)
    parser.add_argument("-oe", "--overwrite-experiment", help="Overwrite existing experiment", action="store_true",
                        required=False)
    parser.add_argument("-s", "--data-sampling-technique", help="Data sampling technique (IID or Non-IID)", type=str,
                        default="iid", required=False)
    parser.add_argument("-w", "--weights-file", help="Weights file path to load", type=str, required=False)
    parser.add_argument("-e", "--global-epochs", help="Number of global (server) epochs", type=int, default=1000,
                        required=False)
    parser.add_argument("-c", "--clients", help="Number of clients", type=int, default=100, required=False)
    parser.add_argument("-f", "--fraction", help="Client fraction to use", type=float, default=0.1,
                        required=False)
    parser.add_argument("-d", "--debug", help="Debugging", action="store_true", required=False)

    parser.add_argument("-lr", "--learning-rate", help="Learning rate", type=float, default=0.15, required=False)
    parser.add_argument("-b", "--batch-size", help="Batch Size", type=int, default=32, required=False)
    parser.add_argument("-ce", "--client-epochs", help="Number of epochs for the clients", type=int, default=1,
                        required=False)
    parser.add_argument("-g", "--gpu", help="GPU to use (-1 is CPU)", type=int, default=0, required=False)
    parser.add_argument("-sum", "--summarizer", help="Weight summarizer to use", type=str, default="avg",
                        required=False)
    args = parser.parse_args()
    return args


def save_args_as_json(args, path):
    with open(str(path), "w") as f:
        json.dump(args.__dict__, f, sort_keys=True, indent=4)
