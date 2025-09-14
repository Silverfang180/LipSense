# LipSense: See What They're Saying! 👄
Ever wonder what someone's saying in a loud room or a silent film? This project is all about teaching a computer to "see" and "hear" with its eyes. We've built a deep learning pipeline that can transcribe spoken words from just watching a person's mouth movements. Think of it as super-powered lip reading!

# 🚀 Why We Built This
- Solve a Real Problem: We wanted to create a tool that could help with accessibility, maybe for those with hearing impairments, or for transcribing historical silent footage.

- Challenge Ourselves: Lip reading is tough! It's the perfect challenge to combine different deep learning techniques: computer vision for seeing the mouth, sequence modeling for understanding the flow of speech, and text prediction to get the final words right.

# Technologies Used 💻
- Python 3.8+
- TensorFlow/Keras
- OpenCV
- CTC (Connectionist Temporal Classification)

# Installation 🚀
1. Clone the repository:
   - git clone https://github.com/Silverfang180/LipSense.git
2. Navigate to the project directory:
   - cd LipSense
3. Install the required dependencies:
   - pip install -r requirements.txt
# 🎬 Let's Get Some Data!
- We trained our model on the GRID  dataset. It's a collection of video clips specifically designed for this kind of project. You'll need to download it and prepare it before you can train the model yourself.
- The dataset is hosted on Google Drive and can be downloaded and extracted automatically using a simple Python script. The gdown package, which handles the download, is included in the requirements.txt file.

  - Find the dataset here:
    - 'https://drive.google.com/uc?id=1YlvpDLix3S-U8fd-gqRwPcWXAXm8JwjL'
  - If google link not available follow step
  -  Download the dataset from the official source:
    - https://www.google.com/search?q=https://www.sheffield.ac.uk/psychology/research/pac/grid-corpus&authuser=2

# 💻 How to Use It
1. Training the Model
  - To train the model on the dataset, run the train.py script. You can customize the training process by specifying the number of epochs and the batch size.
    - python train.py --epochs 50 --batch_size 32
      - Feel free to play around with the numbers!

2. Performing Inference
- Once you have a trained model, you can transcribe speech from a new video file using the inference.py script.
  - python inference.py --video_path "/path/to/your/video.mp4" --output_text "output.txt"
    - The text will be saved in a new file, ready for you to read.

# 🧠 A Peek Under the Hood
Our model is a three-part harmony of different neural networks working together.

- The "Eyes" (CNN): A Convolutional Neural Network (CNN) looks at each video frame and extracts key features of the mouth—the shape, the movement, the details that define a sound.

- The "Memory" (RNN): A Recurrent Neural Network (RNN), like a GRU or LSTM, takes these features and understands them over time. It's the part that remembers what the mouth just did and what it's about to do, piecing together the flow of speech.

- The "Translator" (CTC): The Connectionist Temporal Classification (CTC) layer is the final piece. It takes the sequence from the RNN and turns it into a coherent sentence, even when the mouth movements and the words don't perfectly line up. It's the genius that translates from "lip-talk" to real words.

# 🙏 Want to Help Out?
We'd love your help! If you find a bug, have a cool idea, or just want to make the code better, please open an issue or submit a pull request. This project is a community effort.

# 📄 License
This project is open-source and available under the MIT License. Use it, learn from it, and build something awesome!
