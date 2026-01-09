from flask import Flask, request, render_template_string
import random
import string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Base64 to Image Converter</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #74ebd5, #ACB6E5);
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
            padding-top: 50px;
        }
        .card {
            background: #fff;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
            max-width: 800px;
            width: 90%;
            text-align: center;
        }
        h1 {
            color: #333;
            margin-bottom: 25px;
        }
        textarea {
            width: 100%;
            min-height: 150px;
            padding: 20px;
            font-family: monospace;
            font-size: 14px;
            border-radius: 12px;
            border: 1px solid #ccc;
            resize: vertical;
            box-sizing: border-box;
            transition: all 0.3s;
        }
        textarea:focus {
            border-color: #4CAF50;
            box-shadow: 0 0 10px rgba(76, 175, 80, 0.3);
            outline: none;
        }
        .note {
            margin-top: 10px;
            font-size: 14px;
            color: #555;
        }
        button {
            margin-top: 20px;
            background: #4CAF50;
            color: white;
            border: none;
            padding: 15px 35px;
            border-radius: 12px;
            cursor: pointer;
            font-size: 16px;
            transition: all 0.3s;
        }
        button:hover {
            background: #45a049;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        .image-result {
            margin-top: 30px;
        }
        .image-result img {
            max-width: 100%;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        .download-btn {
            display: inline-block;
            margin-top: 15px;
            padding: 12px 25px;
            font-size: 16px;
            color: #fff;
            background: #2196F3;
            border-radius: 12px;
            text-decoration: none;
            transition: all 0.3s;
        }
        .download-btn:hover {
            background: #1976D2;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        @media (max-width: 600px) {
            .card {
                padding: 25px;
            }
            button, .download-btn {
                width: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Base64 to Image Converter</h1>
        <form method="POST">
            <textarea name="base64_text" placeholder="Paste your Base64 text here">{{ base64_text }}</textarea>
            <div class="note">Please paste a valid Base64 string here to convert it into an image.</div>
            <br>
            <button type="submit">Show Image</button>
        </form>

        {% if image_data %}
        <div class="image-result">
            <h2>Resulting Image:</h2>
            <img id="result-image" src="{{ image_data }}" alt="Base64 Image">
            <br>
            <a id="download-link" class="download-btn" href="{{ image_data }}" download="{{ random_name }}.png">
                Download Image
            </a>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    base64_text = ""
    image_data = None
    random_name = ""
    if request.method == "POST":
        base64_text = request.form.get("base64_text", "")
        if base64_text:
            if "," in base64_text:
                base64_text = base64_text.split(",")[1]
            image_data = "data:image/png;base64," + base64_text
            random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    return render_template_string(HTML, image_data=image_data, base64_text=base64_text, random_name=random_name)

if __name__ == "__main__":
    app.run(debug=True)
