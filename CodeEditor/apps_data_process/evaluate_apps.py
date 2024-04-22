from evaluate import load
import json
from collections import defaultdict
import argparse


def main(args):
    apps_metric = load('codeparrot/apps_metric', trust_remote_code=True)
    # to evaluate generations made for all levels for example

    with open(args.code_gens, "r") as json_file:
        data = json.load(json_file)


    if type(data[0]) == list:
        generations = data
    elif type(data[0]) == dict:
        generations = defaultdict(list)
        for d in data:
            if type(d['output']) == list:
                generations[int(d['id'])].extend(d['output'])
            if type(d['output']) == str:
                generations[int(d['id'])].append(d['output'])
                
        sorted_keys = sorted(generations)
        
        print("The tasks to evaluate", sorted_keys)
        
        generations = [generations[k] for k in sorted_keys]
        
    else:
        print("NOT IMPLEMENTED!")

    results = apps_metric.compute(predictions=generations, level="all", k_list=[1,2], count_errors=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate script")
    
    # Add command-line arguments
    parser.add_argument("--code_gens", type=str, help="Description of arg1")
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Call the main function with the parsed arguments
    main(args)