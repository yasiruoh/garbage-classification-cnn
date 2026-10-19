import math
from collections import Counter

def check_bytes(data, limit=25 * 1024 * 1024):
    if not isinstance(data, bytes) or not data:
        raise ValueError("Input must contain nonempty bytes.")
    if len(data) > limit:
        raise ValueError(f"Input exceeds {limit // (1024*1024)} MB limit.")
    return data

def threshold_value(value):
    value = float(value)
    if not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError("Threshold must be between zero and one.")
    return value

def count_labels(detections):
    return dict(Counter(row["label"] for row in detections))

def validate_rows(rows, features):
    if not rows:
        raise ValueError("No records supplied.")
    if not features or len(set(features)) != len(features):
        raise ValueError("Feature names must be unique and nonempty.")
    output = []
    for row in rows:
        if set(row) != set(features):
            raise ValueError("CSV columns must exactly match the model feature schema.")
        values = [float(row[name]) for name in features]
        if not all(math.isfinite(v) for v in values):
            raise ValueError("Features must contain finite numeric values.")
        output.append(values)
    return output
