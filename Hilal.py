from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Render ve diğer sunucular için portu dinamik olarak alır, 
    # yerelde ise 5000 portunu kullanır.
    port = int(os.environ.get("PORT", 5000))
    # host='0.0.0.0' dış dünyadan ve telefondan erişim için zorunludur.
    app.run(host='0.0.0.0', port=port, debug=True)