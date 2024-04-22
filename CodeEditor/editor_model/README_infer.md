# How to generate with the model and evaluate

Scripts to generate the dataset for editor model.

## 1.Inference

In `CodeEditor/` place your checkpoint folder that contains pretrain files.

In `editor_model/inferConfig` edit the `pretrain_dir` to the checkpoint directory.
Run the script:

```bash
python multi_inferedit_hfai.py --config_file inferConfig/pycodegpt_e11_ngpus.infer.test.json
```

### 2. Get the error message and eval results

In `apps_data_process\`
Replace `<gen_from_llm>` with the output file of the first step and run:

```bash
python apps_data_process/eval_corpus_with_ids_ncpus_fast.py --inp_path <gen_from_llm> --type test
```
