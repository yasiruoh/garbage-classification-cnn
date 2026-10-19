# Garbage Classification CNN

ResNet50 convolutional classification across twelve waste categories.

## Application

- Streamlit interface with explicit input validation and error handling.
- Structured JSON results and configurable review threshold.
- Local processing; no input upload to an inference service.
- Docker configuration and GitHub Actions source checks.
- Separate inference module and dependency-light validation tests.

## Run

Python 3.11 is the target environment. From the extracted repository folder:

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
streamlit run app.py
```

Open the local address printed by Streamlit. Dependency installation and first-use model retrieval require internet access. A GPU is not required by the application code; CPU inference can be resource intensive.

## Model backend

The selected pretrained checkpoint is retrieved automatically on first inference and cached by Hugging Face. Internet access and sufficient disk/memory are required for that first download. No local fitting step is required for the default backend.

Pretrained model development belongs to the credited upstream authors. This repository implements the application and integration; it does not claim original model fitting, published benchmark results, or clinical/security certification.

## Docker

```bash
docker build -t garbage-classification-cnn .
docker run --rm -p 8501:8501 garbage-classification-cnn
```

Bind to localhost or add authenticated access before sharing a deployment. Model caches in a disposable container are not persistent unless a volume is configured.

## Validation

```bash
python -m compileall -q app.py src tests
python -m unittest discover -s tests -v
```

See `VALIDATION.md` for the exact checks performed on this package. Source checks are not model-accuracy or full deployment validation. No measured accuracy is claimed for this integration.

## Scope and limitations

Twelve categories are supported. The checkpoint expects one principal waste object per image. Mixed piles and out-of-distribution objects may be misclassified. Recycling policies vary locally; this application does not prescribe bin colors.

## Repository layout

```text
app.py                 Web interface
src/engine.py          Inference backend
src/validation.py      Input and schema validation
tests/                 Validation unit tests
models/                Artifact documentation
requirements.txt       Runtime dependencies
Dockerfile             Container configuration
.github/workflows/     Automated source checks
```

## GitHub publication

Extract this ZIP and upload the contents of its project folder into a separate repository. Do not upload the ZIP as the repository source. Runtime model caches, user inputs, and generated outputs are excluded by `.gitignore`. No GitHub account access or publication is performed by this package.

## Licensing and credits

Original application code is MIT licensed. Model and dependency licenses remain separate. See `THIRD_PARTY.md`, `LICENSE`, and `SECURITY.md`.
