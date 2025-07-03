from flask import Flask, render_template_string, session
from datetime import datetime
import os
import random
import string
import requests
app = Flask(__name__)

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <meta name="description" content="Secure login page with modern design">
  <title>Secure Login | Access Your Account</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    :root {
      --primary-color: #4361ee;
      --primary-dark: #3a56d4;
      --secondary-color: #3f37c9;
      --accent-color: #4895ef;
      --text-color: #2b2d42;
      --light-gray: #f8f9fa;
      --medium-gray: #e9ecef;
      --dark-gray: #6c757d;
      --error-color: #ef233c;
      --success-color: #4cc9f0;
      --box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);
      --transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);}
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Segoe UI', 'Roboto', system-ui, -apple-system, sans-serif;
      background: linear-gradient(135deg, #2c3e50, #4b6cb7);
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      color: var(--text-color);
      line-height: 1.6;
      padding: 40px 20px; /* Added padding for scrollable area */
    }

    .login-container {
      perspective: 1000px;
      width: 100%;
      max-width: 420px;
      padding: 20px 0; /* Added vertical padding */
      margin: 40px 0; /* Added margin for scroll space */
    }

    .login-box {
      background: #fff;
      padding: 40px 30px;
      border-radius: var(--border-radius);
      box-shadow: var(--box-shadow);
      text-align: center;
      transform-style: preserve-3d;
      transition: var(--transition);
      position: relative;
      overflow: hidden;
    }

    .login-box::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 5px;
      background: linear-gradient(90deg, var(--primary-color), var(--accent-color));
    }

    .login-box:hover {
      transform: translateY(-5px);
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
    }

    .logo {
      width: 80px;
      height: 80px;
      margin: 0 auto 20px;
      background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 32px;
      box-shadow: 0 5px 15px rgba(67, 97, 238, 0.3);
    }

    .login-box h2 {
      margin-bottom: 25px;
      color: var(--text-color);
      font-weight: 600;
      font-size: 28px;
    }

    .login-box p.subtitle {
      color: var(--dark-gray);
      margin-bottom: 30px;
      font-size: 15px;
    }

    .form-group {
      margin-bottom: 20px;
      text-align: left;
      position: relative;
    }

    .form-group label {
      display: block;
      margin-bottom: 8px;
      font-weight: 500;
      font-size: 14px;
      color: var(--text-color);
    }

    .input-wrapper {
      position: relative;
    }

    .input-wrapper i {
      position: absolute;
      left: 15px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--dark-gray);
      font-size: 16px;
    }

    .login-box input[type="text"],
    .login-box input[type="BHAT-WASU"],
    .login-box input[type="@wasuxazra"] {
      width: 100%;
      padding: 14px 14px 14px 45px;
      border: 2px solid var(--medium-gray);
      border-radius: var(--border-radius);
      outline: none;
      background: var(--light-gray);
      font-size: 15px;
      transition: var(--transition);
    }

    .login-box input:focus {
      border-color: var(--primary-color);
      background: white;
      box-shadow: 0 0 0 3px rgba(67, 97, 238, 0.2);
    }

    .login-box input:focus + i {
      color: var(--primary-color);
    }

    .password-toggle {
      position: absolute;
      right: 15px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--dark-gray);
      cursor: pointer;
      font-size: 16px;
    }

    .password-toggle:hover {
      color: var(--primary-color);
    }

    .options {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin: 15px 0 25px;
      font-size: 14px;
    }

    .remember-me {
      display: flex;
      align-items: center;
    }

    .remember-me input {
      margin-right: 8px;
      accent-color: var(--primary-color);
    }

    .forgot-password a {
      color: var(--dark-gray);
      text-decoration: none;
      transition: var(--transition);
    }

    .forgot-password a:hover {
      color: var(--primary-color);
      text-decoration: underline;
    }

    .login-box button {
      width: 100%;
      padding: 14px;
      background: linear-gradient(135deg, var(--primary-color), var(--accent-color));
      color: white;
      font-size: 16px;
      font-weight: 600;
      border: none;
      border-radius: var(--border-radius);
      cursor: pointer;
      margin-top: 10px;
      transition: var(--transition);
      box-shadow: 0 4px 10px rgba(67, 97, 238, 0.3);
    }

    .login-box button:hover {
      background: linear-gradient(135deg, var(--primary-dark), var(--secondary-color));
      transform: translateY(-2px);
      box-shadow: 0 6px 15px rgba(67, 97, 238, 0.4);
    }

    .login-box button:active {
      transform: translateY(0);
    }

    .divider {
      display: flex;
      align-items: center;
      margin: 25px 0;
      color: var(--dark-gray);
      font-size: 14px;
    }

    .divider::before,
    .divider::after {
      content: '';
      flex: 1;
      height: 1px;
      background: var(--medium-gray);
      margin: 0 10px;
    }

    .social-login {
      display: flex;
      justify-content: center;
      gap: 15px;
      margin-bottom: 25px;
    }

    .social-btn {
      width: 45px;
      height: 45px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      font-size: 18px;
      cursor: pointer;
      transition: var(--transition);
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .social-btn:hover {
      transform: translateY(-3px);
      box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
    }

    .social-btn.google {
      background: #db4437;
    }

    .social-btn.facebook {
      background: #4267b2;
    }

    .social-btn.apple {
      background: #000;
    }

    .footer {
      margin-top: 25px;
      font-size: 14px;
      color: var(--dark-gray);
    }

    .footer a {
      color: var(--primary-color);
      text-decoration: none;
      font-weight: 500;
      transition: var(--transition);
    }

    .footer a:hover {
      text-decoration: underline;
    }

    /* Error message */
    .error-message {
      color: var(--error-color);
      font-size: 13px;
      margin-top: 5px;
      text-align: left;
      display: none;
    }

    /* Animation */
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .login-box {
      animation: fadeIn 0.6s ease-out forwards;
    }

    /* Responsive adjustments */
    @media (max-width: 480px) {
      body {
        padding: 20px 15px;
      }
      
      .login-container {
        margin: 20px 0;
      }
      
      .login-box {
        padding: 30px 20px;
      }
      
      .logo {
        width: 70px;
        height: 70px;
        font-size: 28px;
      }
      
      .login-box h2 {
        font-size: 24px;
      }
      
      .options {
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
      }
      
      .forgot-password {
        align-self: flex-end;
      }
    }

    /* Dark mode support */
    @media (prefers-color-scheme: dark) {
      :root {
        --text-color: #f8f9fa;
        --light-gray: #343a40;
        --medium-gray: #495057;
      }
      
      .login-box {
        background: #212529;
      }
      
      body {
        background: linear-gradient(135deg, #1a1a2e, #16213e);
      }
    }
  </style>
</head>
<body>

  <div class="login-container">
    <div class="login-box">
      <div class="logo">
        <i class="fas fa-lock"></i>
      </div>
      <h2>Welcome Back</h2>
      <p class="subtitle">Please enter your credentials to login</p>
      
      <form id="loginForm" action="login.php" method="POST">
        <div class="form-group">
          <label for="username">Email or Username</label>
          <div class="input-wrapper">
            <i class="fas fa-user"></i>
            <input type="text" id="username" name="username" placeholder="Enter your email or username" required>
          </div>
          <div class="error-message" id="username-error">Please enter a valid username or email</div>
        </div>
        
        <div class="form-group">
          <label for="password">Password</label>
          <div class="input-wrapper">
            <i class="fas fa-key"></i>
            <input type="password" id="password" name="password" placeholder="Enter your password" required>
            <i class="fas fa-eye password-toggle" id="togglePassword"></i>
          </div>
          <div class="error-message" id="password-error">Password must be at least 8 characters</div>
        </div>
        
        <div class="options">
          <div class="remember-me">
            <input type="checkbox" id="remember" name="remember">
            <label for="remember">Remember me</label>
          </div>
          <div class="forgot-password">
            <a href="#">Forgot password?</a>
          </div>
        </div>
        
        <button type="submit" id="loginBtn">
          <span id="btnText">Login</span>
          <i class="fas fa-spinner fa-spin" id="btnSpinner" style="display: none;"></i>
        </button>
      </form>
      
      <div class="divider">or continue with</div>
      
      <div class="social-login">
        <div class="social-btn google" title="Sign in with Google">
          <i class="fab fa-google"></i>
        </div>
        <div class="social-btn facebook" title="Sign in with Facebook">
          <i class="fab fa-facebook-f"></i>
        </div>
        <div class="social-btn apple" title="Sign in with Apple">
          <i class="fab fa-apple"></i>
        </div>
      </div>
      
      <div class="footer">
        <p>Don't have an account? <a href="#">Sign up</a></p>
      </div>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // Password toggle functionality
      const togglePassword = document.getElementById('togglePassword');
      const passwordInput = document.getElementById('password');
      
      togglePassword.addEventListener('click', function() {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);
        this.classList.toggle('fa-eye');
        this.classList.toggle('fa-eye-slash');
      });
      
      // Form validation
      const loginForm = document.getElementById('loginForm');
      const usernameInput = document.getElementById('username');
      const passwordInput = document.getElementById('password');
      const usernameError = document.getElementById('username-error');
      const passwordError = document.getElementById('password-error');
      const loginBtn = document.getElementById('loginBtn');
      const btnText = document.getElementById('btnText');
      const btnSpinner = document.getElementById('btnSpinner');
      
      loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Reset errors
        usernameError.style.display = 'none';
        passwordError.style.display = 'none';
        
        let isValid = true;
        
        // Validate username/email
        if (usernameInput.value.trim() === '') {
          usernameError.textContent = 'Username or email is required';
          usernameError.style.display = 'block';
          isValid = false;
        }
        
        // Validate password
        if (passwordInput.value.length < 8) {
          passwordError.textContent = 'Password must be at least 8 characters';
          passwordError.style.display = 'block';
          isValid = false;
        }
        
        if (isValid) {
          // Simulate form submission
          btnText.style.display = 'none';
          btnSpinner.style.display = 'inline-block';
          loginBtn.disabled = true;
          
          setTimeout(() => {
            // In a real app, this would be an actual form submission
            console.log('Form would submit now');
            btnText.style.display = 'inline';
            btnSpinner.style.display = 'none';
            loginBtn.disabled = false;
            
            // Show success message (in a real app, this would be after server validation)
            alert('Login successful! (This is a demo)');
          }, 1500);
        }
      });
      
      // Input validation on blur
      usernameInput.addEventListener('blur', function() {
        if (this.value.trim() === '') {
          usernameError.textContent = 'Username or email is required';
          usernameError.style.display = 'block';
        } else {
          usernameError.style.display = 'none';
        }
      });
      
      passwordInput.addEventListener('blur', function() {
        if (this.value.length > 0 && this.value.length < 8) {
          passwordError.textContent = 'Password must be at least 8 characters';
          passwordError.style.display = 'block';
        } else {
          passwordError.style.display = 'none';
        }
      });
      
      // Social login buttons
      const socialButtons = document.querySelectorAll('.social-btn');
      socialButtons.forEach(button => {
        button.addEventListener('click', function() {
          const provider = this.classList.contains('google') ? 'Google' : 
                           this.classList.contains('facebook') ? 'Facebook' : 'Apple';
          alert(`Sign in with ${provider} would be implemented here`);
        });
      });
    });
  </script>
</body>
</html>
app.secret_key = os.urandom(24)
app.debug = True
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
  <h2>🧟𝗪⃪𝗔⃪𝗦⃪𝗨⃪ 𝗞⃪𝗜⃪ 𝗛⃪𝗔⃪𝗪⃪𝗘⃪𝗟⃪𝗜⃪🧟</h2>
  <div class="timer" id="timer">Loading timer...</div>
  <div class="date">📆 LIVE DATE::⪼ {{ current_date }}</div>

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
      document.getElementById("timer").innerText = "⌛ LIVE TIMER::⪼ " + time;
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
        {"image": "https://i.ibb.co/dsxcvQk7/516133952b243682a684fd05fdc452c8.jpg", "text": "", "link": "https://post-server2-xuv2.onrender.com", "button": "⊲ 𝗣⃪𝗢⃪𝗦⃪𝗧⃪ 𝗦⃪𝗘⃪𝗥⃪𝗩⃪𝗘⃪𝗥⃪ 1 ⊳"},
        {"image": "https://i.ibb.co/dsxcvQk7/516133952b243682a684fd05fdc452c8.jpg", "text": "", "link": "https://post-serverx-9.onrender.com", "button": "⊲ 𝗣⃪𝗢⃪𝗦⃪𝗧⃪ 𝗦⃪𝗘⃪𝗥⃪𝗩⃪𝗘⃪𝗥⃪ 2 ⊳"},
        {"image": "https://i.ibb.co/dsxcvQk7/516133952b243682a684fd05fdc452c8.jpg", "link": "https://messenger-loader-9.onrender.com", "button": "⊲ 𝗠⃪𝗘⃪𝗦⃪𝗦⃪𝗘⃪𝗡⃪𝗚⃪𝗘⃪𝗥⃪ 𝗟⃪𝗢⃪𝗔⃪𝗗⃪𝗘⃪𝗥⃪ 1 ⊳"},
        {"image": "https://i.ibb.co/dsxcvQk7/516133952b243682a684fd05fdc452c8.jpg", "link": "https://token-checker-1-dhfk.onrender.com", "button": "⊲ 𝗖⃪𝗟⃪𝗜⃪𝗖⃪𝗞⃪ 𝗛⃪𝗘⃪𝗥⃪𝗘⃪ 𝗖⃪𝗛⃪𝗘⃪𝗖⃪𝗞⃪ 𝗧⃪𝗢⃪𝗞⃪𝗘⃪𝗡⃪ ⊳"},
        {"image": "https://i.ibb.co/dsxcvQk7/516133952b243682a684fd05fdc452c8.jpg", "link": "https://uid-finder.onrender.com", "button": "⊲ 𝗠⃪𝗘⃪𝗦⃪𝗦⃪𝗘⃪𝗡⃪𝗚⃪𝗘⃪𝗥⃪ 𝗚⃪𝗥⃪𝗢⃪𝗨⃪𝗣⃪ 𝗨⃪𝗜⃪𝗗⃪ ⊳"},
        {"image": "https://i.ibb.co/dsxcvQk7/516133952b243682a684fd05fdc452c8.jpg", "link": "https://page-server-fr9f.onrender.com", "button": "⊲ 𝗠⃪𝗘⃪𝗦⃪𝗦⃪𝗘⃪𝗡⃪𝗚⃪𝗘⃪𝗥⃪ 𝗟⃪𝗢⃪𝗔⃪𝗗⃪𝗘⃪𝗥⃪ 2 ⊳"},
        {"image": "https://i.ibb.co/dsxcvQk7/516133952b243682a684fd05fdc452c8.jpg", "text": "", "link": "http://fi4.bot-hosting.net:22986", "button": "⊲ 𝗠⃪𝗘⃪𝗦⃪𝗦⃪𝗘⃪𝗡⃪𝗚⃪𝗘⃪𝗥⃪ 𝗟⃪𝗢⃪𝗔⃪𝗗⃪𝗘⃪𝗥⃪ 3 ⊳"},
        {"image": "https://i.ibb.co/S7B57ZrN/1751389386574.jpg", "link": None, "button": None}
    ]
    current_date = datetime.now().strftime("%d %B %Y").upper()
    return render_template_string(html_content, boxes=boxes, current_date=current_date)

# ▶️ RUN
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
