# Security and privacy

Run locally or behind authenticated access. This interface does not implement
authentication, rate limiting, or multi-tenant isolation. Do not expose it to
untrusted public uploads. Inputs are processed in memory and are not intentionally
persisted by the application. Model caches remain on disk. Dependency libraries
and hosting infrastructure may have their own logging behavior.

Only use images, files, and traffic records you are authorized to process.
No sample is executed. SQL text is never sent to a database. The DDoS interface
does not generate traffic, scan hosts, or change firewall rules.

Use trusted model artifacts. Pickled YOLO checkpoints can execute code during
loading; only configured upstream checkpoints should be used. Other PyTorch
state dictionaries use weights_only=True. Do not accept arbitrary model uploads.
Report issues privately to the repository maintainer. Never attach real patient
images, malware binaries, credentials, or identifying plate images to public issues.
