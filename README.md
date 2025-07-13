# Pawthenticator - Dog Breed Identifier

**Pawthenticator** is a web app built with Streamlit that uses a fine-tuned ResNet-50 model to predict dog breeds from user-uploaded images.

**Live demo:** [Live Demo Link](https://pawthenticator.streamlit.app/)

---

## Features

- Upload any photo containing a dog
- Predicts:
  - **One breed** if confidence is **90% or higher**
  - **Top 3 breeds** (ranked by confidence) if confidence is **below 90%**
- Each prediction includes a link to learn more about the breed

---

## How It Works

1. Visit the app: [https://pawthenticator.streamlit.app/](https://pawthenticator.streamlit.app/)
2. Upload a photo of a dog from your device
3. Click **"Determine Breed"**
4. View the predicted breed(s) and follow the provided links to learn more

---

## Model Details

- **Architecture**: ResNet-50
- **Training**: Fine-tuned in Google Colab
- **Weights**: Hosted on Hugging Face
- **Interface**: Built and deployed using Streamlit


---

## Local Development (Optional)

To run the app locally:

```bash
git clone https://github.com/yourusername/pawthenticator.git
cd pawthenticator

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
streamlit run app.py
```

---

## License

This project is licensed under the MIT License.
