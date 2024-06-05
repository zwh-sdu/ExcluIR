This dataset comprises two files: `corpus.json` and `test_manual_final.json`.

## Files Description

### 1. corpus.json

- **Type:** List
- **Content:** Each item in the list is a string representing a document.

### 2. test_manual_final.json

- **Type:** List of dictionaries
- **Content:** Each item in the list is a dictionary with three keys:
  - **question0:** The original query from the HotpotQA dataset.
  - **RQ_rewrite:** Exclusive query.
  - **corpus_sub_index:** A list of two integers:
    - The first integer represents the index of a negative document from `corpus.json`.
    - The second integer represents the index of a positive document from `corpus.json`.

## Example

### corpus.json
```json
[
    "Document 1 content...",
    "Document 2 content...",
    "Document 3 content...",
    ...
]
```

### test_manual_final.json
```json
[
    {
        "question0": "Original query",
        "RQ_rewrite": "Exclusive query",
        "corpus_sub_index": [1, 2]  // The negative document is corpus[1] and the positive document is corpus[2]
    },
    {
        "question0": "Original example",
        "RQ_rewrite": "Exclusive query",
        "corpus_sub_index": [0, 3]  // The negative document is corpus[0] and the positive document is corpus[3]
    },
    ...
]
```