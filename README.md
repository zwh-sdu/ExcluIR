# ExcluIR: Exclusionary Neural Information Retrieval

This repository provides a benchmark for evaluating the performance of retrieval models specifically in scenarios where users provide explicit indications about the information they wish to exclude from the retrieval results.

## About ExcluIR

In traditional retrieval tasks, the focus is on matching user queries with relevant documents. However, in many real-world scenarios, users are also aware of and can explicitly specify the kind of information they wish to avoid. This benchmark is designed to assess how well retrieval models can understand and apply these exclusionary queries to improve the relevance of the returned results.

For more detailed information about this benchmark, please refer to our paper:

[Link to the Paper](https://example.com/your-paper)

## Getting Started

### Installation

To use this benchmark, you will need Python 3.6 or later. Additionally, depending on the retrieval models you wish to evaluate, you might need specific libraries or frameworks. Please refer to the documentation of those models for detailed requirements.

### Dataset Download

The dataset for this benchmark can be downloaded from the following link:

[Download ExcluIR Dataset](https://drive.google.com/drive/folders/1O7IHuEHgjAHL6FCb8z5-zTI3YCqcA5J1?usp=sharing)

The dataset files should be extracted to the `src/data` directory.

## Evaluating Retrieval Models

To evaluate a retrieval model on this benchmark, follow these steps:

**Prepare Your Model**: Ensure your model is trained and ready for evaluation. If applicable, make sure it is compatible with the provided dataset format.

**Run Evaluation**: We provide the sample evaluation scripts that demonstrate how to evaluate the models from [sentence-transformers](https://huggingface.co/sentence-transformers). You might need to adjust the script based on the specific requirements or output format of your model.

```bash
python bi_eval.py # for bi-encoder models
python cross_eval.py # for cross-encoder models
```

## Citing This Work

If you use this benchmark for your research, please cite our work using the following reference:

```bibtex
@article{YourName2023EliminativeRetrieval,
  title={A Benchmark for Evaluating Eliminative Retrieval Models},
  author={Your Name and Collaborator's Name},
  journal={Journal of Information Retrieval Research},
  year={2023},
  volume={XX},
  number={XX},
  pages={XX-XX},
  doi={XX.XXXX/XXXXXX}
}
```

<!-- ## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--- -->

We hope this benchmark will be a valuable resource for the community and lead to significant advancements in the field of information retrieval.