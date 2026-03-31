from flask import Flask, request, render_template_string
import requests

app = Flask(name)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>TikTok Downloader Pro</title>
    <style>
        body {
            font-family: Arial;
            background: #0f172a;
            color: white;
            text-align: center;
            padding: 50px;
        }
        input {
            padding: 10px;
            width: 60%;
            border-radius: 8px;
            border: none;
        }
        button {
            padding: 10px 20px;
            background: #22c55e;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            color: white;
            font-weight: bold;
        }
        .card {
            background: #1e293b;
            padding: 20px;
            margin-top: 30px;
            border-radius: 15px;
        }
        video {
            width: 300px;
            border-radius: 10px;
        }
        a {
            display: inline-block;
            margin-top: 15px;
            padding: 10px 15px;
            background: #3b82f6;
            border-radius: 8px;
            color: white;
            text-decoration: none;
        }
    </style>
</head>
<body>

    <h1>🔥 TikTok Downloader Pro</h1>

    <form method="POST">
        <input type="text" name="url" placeholder="Paste TikTok URL..." required>
        <br><br>
        <button type="submit">Download</button>
    </form>

    {% if video %}
    <div class="card">
        <h3>🎬 Preview</h3>
        <video controls src="{{ video }}"></video>
        <br>
        <a href="{{ video }}" download>⬇️ Download Video</a>
    </div>
    {% endif %}

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    video = None

    if request.method == 'POST':
        url = request.form['url']

        try:
            api = f"https://api.tiklydown.eu.org/api/download?url={url}"
            res = requests.get(api).json()

            video = res['video']['noWatermark']
        except:
            video = None

    return render_template_string(HTML, video=video)


if name == "main":
    app.run(host="0.0.0.0", port=10000)
