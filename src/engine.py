from functools import lru_cache

REPO = "kendrickfff/my_resnet50_garbage_classification"
FILENAME = "resnet50_garbage_classification.pth"

LABELS = [
    "battery",
    "biological",
    "brown-glass",
    "cardboard",
    "clothes",
    "green-glass",
    "metal",
    "paper",
    "plastic",
    "shoes",
    "trash",
    "white-glass",
]


@lru_cache(maxsize=1)
def load_model():
    import torch
    from torch import nn
    from torchvision import models
    from huggingface_hub import hf_hub_download

    model = models.resnet50(weights=None)
    model.fc = nn.Linear(model.fc.in_features, len(LABELS))

    model_path = hf_hub_download(
        repo_id=REPO,
        filename=FILENAME,
    )

    state = torch.load(
        model_path,
        map_location="cpu",
        weights_only=True,
    )

    model.load_state_dict(state, strict=True)
    model.eval()

    return model


def transform_image(image):
    from torchvision import transforms

    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225],
        ),
    ])

    return transform(image.convert("RGB")).unsqueeze(0)


def predict(image, threshold=0.35):
    import torch
    from src.validation import threshold_value

    threshold = threshold_value(threshold)

    with torch.inference_mode():
        scores = (
            load_model()(transform_image(image))
            .softmax(dim=1)[0]
            .tolist()
        )

    probabilities = dict(
        zip(
            LABELS,
            [round(float(score), 6) for score in scores],
        )
    )

    label = max(probabilities, key=probabilities.get)

    result = {
        "label": label,
        "score": probabilities[label],
        "scores": probabilities,
        "review_required": probabilities[label] < threshold,
        "model": REPO,
    }

    return result, None
