import os
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# قاعدة بيانات مؤقتة للمنتجات (يمكنك تعديلها وزيادتها لاحقاً)
PRODUCTS = [
    {
        "id": 1,
        "name": "عسل سدر حريبي فاخر",
        "price": "150,000",
        "currency": "ريال",
        "description": "عسل سدر طبيعي 100% من وديان مديرية حريب الحبيبة.",
        "image": "https://images.unsplash.com/photo-1587049352846-4a222e784d38?w=500"
    },
    {
        "id": 2,
        "name": "بن خولاني درجة أولى",
        "price": "25,000",
        "currency": "ريال",
        "description": "بن يمني أصيل محمص ومنقى بعناية فائقة.",
        "image": "https://images.unsplash.com/photo-1514432324607-a09d9b4aefdd?w=500"
    },
    {
        "id": 3,
        "name": "سمن بلدي أصلي",
        "price": "40,000",
        "currency": "ريال",
        "description": "سمن بلدي نقي ومستخلص بالطريقة التقليدية العريقة.",
        "image": "https://images.unsplash.com/photo-1589985270826-4b7bb135bc9d?w=500"
    }
]

# التصميم الموحد للمتجر (HTML + CSS) متوافق تماماً مع الجوال
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>متجر حريب الإلكتروني</title>
    <style>
        :root {
            --primary-color: #2c3e50;
            --accent-color: #d35400;
            --bg-color: #f8f9fa;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--bg-color);
            margin: 0;
            padding: 0;
            color: #333;
        }
        header {
            background-color: var(--primary-color);
            color: white;
            text-align: center;
            padding: 20px 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        header h1 {
            margin: 0;
            font-size: 28px;
        }
        header p {
            margin: 5px 0 0 0;
            opacity: 0.9;
        }
        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 15px;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
        }
        .card {
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            transition: transform 0.3s;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card img {
            width: 100%;
            height: 200px;
            object-fit: cover;
        }
        .card-content {
            padding: 15px;
        }
        .card-title {
            font-size: 20px;
            margin: 0 0 10px 0;
            color: var(--primary-color);
        }
        .card-desc {
            font-size: 14px;
            color: #7f8c8d;
            margin-bottom: 15px;
            line-height: 1.5;
        }
        .card-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .price {
            font-size: 18px;
            font-weight: bold;
            color: var(--accent-color);
        }
        .btn {
            background-color: var(--accent-color);
            color: white;
            border: none;
            padding: 8px 15px;
            border-radius: 5px;
            cursor: pointer;
            text-decoration: none;
            font-weight: bold;
            font-size: 14px;
        }
        .btn:hover {
            background-color: #b33900;
        }
        footer {
            text-align: center;
            padding: 20px;
            margin-top: 40px;
            background-color: #eee;
            color: #666;
            font-size: 14px;
        }
    </style>
</head>
<body>

    <header>
        <h1>مرحباً بك في متجر حريب الإلكتروني</h1>
        <p>أجود المنتجات المحلية بين يديك</p>
    </header>

    <div class="container">
        <h2 style="border-bottom: 2px solid var(--primary-color); padding-bottom: 10px; color: var(--primary-color);">منتجاتنا المتميزة</h2>
        <div class="grid">
            {% for product in products %}
            <div class="card">
                <img src="{{ product.image }}" alt="{{ product.name }}">
                <div class="card-content">
                    <h3 class="card-title">{{ product.name }}</h3>
                    <p class="card-desc">{{ product.description }}</p>
                    <div class="card-footer">
                        <span class="price">{{ product.price }} {{ product.currency }}</span>
                        <a href="https://wa.me/967XXXXXXXXX?text=أريد+طلب+{{ product.name }}" target="_blank" class="btn">اطلب الآن عبر واتساب</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>

    <footer>
        <p>جميع الحقوق محفوظة &copy; 2026 - متجر حريب الإلكتروني</p>
    </footer>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, products=PRODUCTS)

if __name__ == '__main__':
    # جلب المنفذ تلقائياً من Render أو استخدام 5000 كافتراضي
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
