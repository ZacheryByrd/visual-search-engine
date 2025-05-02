import torchvision.models as models
import torch.nn as nn

def load_model():
    model = models.resnet18(pretrained=True)
    # Remove the final classification layer to get feature vectors
    model = nn.Sequential(*list(model.children())[:-1])
    model.eval()
    return model
