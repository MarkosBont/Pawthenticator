from huggingface_hub import hf_hub_download
import torch
from torchvision import transforms
from torchvision import models
import torch.nn as nn
from PIL import Image
import torch.nn.functional as F
import json


# Transformations applied to images to scale them and to tensor
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])


def load_model():
    """
    Loads the fine-tuned ResNet50 model from Hugging Face with custom classification head.

    Returns:
        model (torch.nn.Module): A PyTorch model ready for inference.
    """

    # Loading the model (resnet50 with custom FC final layer)
    model = models.resnet50()
    model.fc = nn.Sequential(
        nn.Dropout(p=0.5),
        nn.Linear(model.fc.in_features, 120) # 120 is the number of classes in the dataset
    )

    # Downloading the weights from Hugging Face
    model_path = hf_hub_download(repo_id="markosbont/resnet50-dog-breeds", filename="pytorch_model.bin")
    model.load_state_dict(torch.load(model_path, map_location="cpu"))
    model.eval()

    return model


def determine_breed(image):
    # Loading the class names from the file
    with open("class_names.json", "r") as f:
        class_names = json.load(f)

    model = load_model() # Loading the model

    # Apply transforms
    input_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(input_tensor)  # Gets model predictions for each class
        probabilities = F.softmax(outputs, dim=1)  # Applies softmax to convert logits to probabilities
        top3_probs, top3_indices = torch.topk(probabilities, k=3)

    # Formatting predictions - Stripping random characters and returning the top 3 predictions.
    results = []
    for i in range(3):
        label = class_names[top3_indices[0][i]]
        breed_name = label.split('-')[1]
        breed_name = breed_name.replace('_', ' ')
        breed = breed_name.title()
        confidence = top3_probs[0][i].item()
        results.append((breed, confidence))

    return results

