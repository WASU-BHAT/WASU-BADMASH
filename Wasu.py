from flask import Flask, render_template_string, session
from datetime import datetime
import os
import random
import string
import requests
app = Flask(__name__)
# 🧠 HTML TEMPLATE
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>🧟𝗕𝗔⃪𝗗⃪𝗠⃪𝗔⃪𝗦⃪𝗛⃪𝗢⃪ 𝗞⃪𝗔⃪ 𝗕⃪𝗔⃪𝗔⃪𝗣⃪ 𝗪⃪𝗔⃪𝗦⃪𝗨⃪ 𝗕⃪𝗛𝗔⃪𝗧⃪🧟</title>
  <style>
    body { font-family: sans-serif; background-color: #f4f4f4; text-align: center; padding: 20px; }
    h2 { color: #ff0000; }
    .timer { font-size: 20px; margin-bottom: 10px; }
    .date { font-weight: bold; margin-bottom: 20px; }
    .box { border: 2px solid #000; border-radius: 10px; padding: 15px; margin: 15px auto; width: 90%; max-width: 500px; background: #fff; }
    .btn { padding: 10px 20px; background: #000; color: white; border: none; border-radius: 6px; margin-top: 10px; display: inline-block; cursor: pointer; }
    .footer { margin-top: 40px; font-size: 14px; }
  </style>
</head>
<body>
  <h2>👿𝗪⃪𝗔⃪𝗦⃪𝗨⃪ 𝗕⃪𝗔⃪𝗗⃪𝗠⃪𝗔⃪𝗦⃪𝗛⃪👿</h2>
  <div class="timer" id="timer">Loading timer...</div>
  <div class="date">📆 𝗟⃪𝗜⃪𝗩⃪𝗘⃪ 𝗗⃪𝗔⃪𝗧⃪𝗘⃪::⪼ {{ current_date }}</div>

  {% for box in boxes %}
  <div class="box">
    <img src="{{ box.image }}" alt="img" width="100%" style="border-radius: 10px;">
    {% if box.text %}<h3>{{ box.text }}</h3>{% endif %}
    {% if box.link %}
      {% if loop.index0 == 0 %}
        <button class="btn" onclick="checkPassword('{{ box.link }}')">{{ box.button }}</button>
      {% else %}
        <a href="{{ box.link }}" class="btn">{{ box.button }}</a>
      {% endif %}
    {% endif %}
  </div>
  {% endfor %}

  <div class="footer">
    <p>
      <a href="/terms">Terms</a> | <a href="/privacy">Privacy</a>
    </p>
    <p>
      <a href="https://www.facebook.com/profile.php?id=61574766223435">Facebook</a> |
      <a href="http://fi9.bot-hosting.net:20566/">WhatsApp</a> |
      <a href="https://github.com/devixayyat/">GitHub</a>
    </p>
    <p>© 2025 𝗕⃪𝗛⃪𝗔⃪𝗧⃪ 𝗪⃪𝗔⃪𝗦⃪𝗨⃪  All RIGHTS RESERVED.</p>
    <p>𝗠⃪𝗔⃪𝗗⃪𝗘⃪ 𝗕⃪𝗬⃪ 𝗕⃪𝗛⃪𝗔⃪𝗧⃪ 𝗪⃪𝗔⃪𝗦⃪𝗨⃪ <b>𝗫⃪ 𝗔⃪𝗭⃪𝗥⃪𝗔⃪</b></p>
  </div>

  <script>
    function updateTimer() {
      const now = new Date();
      const time = now.toLocaleTimeString();
      document.getElementById("timer").innerText = "⌛ 𝗟⃪𝗜⃪𝗩⃪𝗘⃪ 𝗧⃪𝗜⃪𝗠⃪𝗘⃪𝗥⃪::⪼ " + time;
    }
    setInterval(updateTimer, 1000);
    updateTimer();

    function checkPassword(link) {
      const pass = prompt("🎋🛡 ENTER PASSWORD TO ACCESS THIS SERVER 🎋🛡");
      if (pass === "WASU X AZRA") {
        window.location.href = link;
      } else {
        alert("❌ BHAT WASU NY TERE KO REJECT KAR DIYA..😞❤️");
      }
    }
  </script>
</body>
</html>
'''

# 🖼️ ROUTE
@app.route('/')
def home():
    boxes = [   
        {"image": "https://i.ibb.co/yn9xr3LB/6a87e9742d3488e8c4493b0bded43028.jpg", "text": "", "link": "http://fi5.bot-hosting.net:21325", "button": "⊲ 𝗖⃪𝗢⃪𝗡⃪𝗩⃪𝗢⃪ 𝗣⃪𝗔⃪𝗚⃪𝗘⃪ 1 ⊳"},
        {"image": "https://i.ibb.co/yn9xr3LB/6a87e9742d3488e8c4493b0bded43028.jpg", "text": "", "link": "http://de3.bot-hosting.net:22466", "button": "⊲ 𝗖⃪𝗢⃪𝗡⃪𝗩⃪𝗢⃪ 𝗣⃪𝗔⃪𝗚⃪𝗘⃪ 2 ⊳"},
        {"image": "https://i.ibb.co/yn9xr3LB/6a87e9742d3488e8c4493b0bded43028.jpg", "link": "https://uid-finder-re3rry39g-wasu-bhats-projects.vercel.app/", "button": "⊲ 𝗨⃪𝗜⃪𝗗⃪ 𝗙⃪𝗜⃪𝗡⃪𝗗⃪𝗘⃪𝗥⃪⊳"},
        {"image": "https://i.ibb.co/yn9xr3LB/6a87e9742d3488e8c4493b0bded43028.jpg", "link": "https://token-checker-g62eyemfz-wasu-bhats-projects.vercel.app/", "button": "⊲ 𝗧⃪𝗢⃪𝗞⃪𝗘⃪𝗡⃪ 𝗖⃪𝗛⃪𝗘⃪𝗖⃪𝗞⃪𝗘⃪𝗥⃪⊳"},
        {"image": "https://i.ibb.co/Cs9GM32L/1749189275397.jpg", "link": None, "button": None}
    ]
    current_date = datetime.now().strftime("%d %B %Y").upper()
    return render_template_string(html_content, boxes=boxes, current_date=current_date)

# ▶️ RUN
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
