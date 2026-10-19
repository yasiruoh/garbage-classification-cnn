# Validation record

- Python syntax checks: 6 source files passed.
- Dependency-free input validation tests: 9 passed; no failures or errors.
- ZIP integrity: checked during packaging.
- Runtime dependency installation: not executed in this environment.
- Model download and end-to-end inference: not executed in this environment.
- Docker build and browser interaction: not executed in this environment.
- Accuracy, robustness, calibration, and clinical/security validation: not measured.

The package contains real inference integrations, not prerecorded predictions.
A passing source check does not certify that upstream checkpoints remain
available or that every dependency combination is compatible. Requirements
use bounded ranges, not a fully resolved and integration-tested lockfile.
