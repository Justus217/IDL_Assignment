import torch
import torch.nn as nn
import torch.optim as optim
import json
from data import get_loaders
import models




def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Prediction executing on device: {device}")
    
    _, _, test_loader = get_loaders(data=config["DATA"], data_path=config["DATA_PATH"], batch_size=config["BATCH_SIZE"])
    
    model_class = getattr(models, config["MODEL"])
    model = model_class(in_channels=config["CHANNELS"], num_classes=config["NUM_CLASSES"], drop_rate=config["DROP_RATE"], activation_str="ReLU").to(device)
    model_save_path = f"./models/{config['MODEL']}_{config['DATA']}_model.pth"
    model.load_state_dict(torch.load(model_save_path, map_location=device))
    print(f"Model loaded from {model_save_path}")
    
    with torch.no_grad():
        model.eval()
        
        all_predictions = []
        all_labels = []
        
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            
            outputs = model(images)
            predictions = torch.argmax(outputs, dim=1)

            all_predictions.extend(predictions.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
        
        # compare predictions with true labels and calculate accuracy
        correct = sum(p == l for p, l in zip(all_predictions, all_labels))
        accuracy = correct / len(all_labels) if all_labels else 0
        print(f"Accuracy: {accuracy.item():.4f}")


if __name__ == "__main__":
    main()