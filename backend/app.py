from flask import Flask, request, jsonify
from flask_cors import CORS
from PIL import Image
from search_engine import find_similar_images  # handles image matching

app = Flask(__name__)
CORS(app)  # Allow cross-origin from frontend

@app.route('/')
def home():
    return "Visual Search Engine Backend is Running!"

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Convert the uploaded file to a PIL image
        img = Image.open(file.stream).convert('RGB')

        # Run similarity search (returns top 5 results with index + label)
        results = find_similar_images(img)

        # Build the response using index-based image paths
        matches = []
        for match in results:
            idx = match['index']
            label = match['label']
            matches.append({
            'image_url': f'/cifar_samples/{idx}.png',
            'label': label,
            'class_name': match['class_name']
            })


        return jsonify({'matches': matches})

    except Exception as e:
        print(f"Error processing image: {e}")
        return jsonify({'error': 'Image processing failed'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
