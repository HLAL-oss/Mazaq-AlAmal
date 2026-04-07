from flask import Flask, abort, render_template, send_from_directory, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")

WHATSAPP_NUMBER = "00962797757734"

PRODUCTS = [
    {"name": "كيك الصور المطبوعة", "image": "M-1.jpg", "price": "10.00 د.أ"},
    {"name": "قالب كيك مزين", "image": "M-2.jpg", "price": "9.00 د.أ"},
    {"name": "صحن دونات مشكل", "image": "M-3.jpg", "price": "5.00 د.أ"},
    {"name": "كب كيك (القطعة)", "image": "M-4.jpg", "price": "0.50 د.أ"},
    {"name": "إكلير فرنسي", "image": "M-5.jpg", "price": "0.75 د.أ"},
    {"name": "كوكتيل فواكه طبيعي", "image": "M-6.jpg", "price": "1.00 د.أ"},
]


@app.route("/")
def index():
    return render_template(
        "index.html",
        products=PRODUCTS,
        whatsapp_number=WHATSAPP_NUMBER,
    )


@app.route("/assets/<path:filename>")
def assets(filename: str):
    file_map = {
        "header-logo.png": "header-logo.png.png",
        "logo.png": "logo.png.png",
    }
    actual_name = file_map.get(filename, filename)
    try:
        return send_from_directory(".", actual_name)
    except Exception:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)
