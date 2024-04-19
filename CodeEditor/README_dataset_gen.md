# How to generate the dataset

Scripts to generate the dataset for editor model.

## 1. LLM generation

In `apps_data_process/` run the script bellow to generate initial code generations. Replace `<PRETRAIN>` with your choice of pretrained model.

```bash

python example_script.py --num_tasks <#tasks> --model_ckpt <PRETRAIN> --tokenizer <PRETRAIN> --n_samples <#generations_per_task>
ex:
python example_script.py --num_tasks 598 --model_ckpt deepseek-ai/deepseek-coder-1.3b-instruct --tokenizer deepseek-ai/deepseek-coder-1.3b-instruct --n_samples 1
```

### 2. Get the error message

For APPS dataset:

Replace `gen_from_llm` with the output from step 1.

```bash
python apps_data_process/eval_corpus_with_ids_ncpus_fast.py --inp_path <gen_from_llm> --type test
```


### 3. Edit Dataset Construction

The scripts are in `CodeEditor/generate_datasets/`

Replace TODO in `model_output_path = "TODO" ` with the output file path from step 1 in in 'generate_datasets_for_edit_humaneval.py' file.
Replace TODO in `eval_results_path = "TODO"` with the output file path from step 2 in in 'generate_datasets_for_edit_humaneval.py' file.

Run the script below to generate the dataset needed for CodeEditor model.

For APPS dataset:

```
python generate_datasets_for_edit_humaneval.py
```
