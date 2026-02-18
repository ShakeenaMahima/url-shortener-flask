from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, redirect
from datetime import datetime, timedelta
from models.url import URL
from utils.generator import generate_unique_code
from extensions import db


url_bp = Blueprint("url_bp", __name__)

@url_bp.route("/shorten", methods=["POST"])
@jwt_required()
def shorten_url():
    user_id = get_jwt_identity()

    data = request.get_json()

    if not data or "url" not in data:
        return jsonify({"error": "URL is required"}), 400

    original_url = data["url"]

    existing = URL.query.filter_by(original_url=original_url).first()
    if existing:
        return jsonify({
            "shortened_url": f"http://127.0.0.1:5000/{existing.short_code}",
            "clicks": existing.clicks
        })

    short_code = generate_unique_code()

    new_url = URL(
        original_url=original_url,
        short_code=short_code,
        user_id=user_id
    )

    db.session.add(new_url)
    db.session.commit()

    return jsonify({
        "shortened_url": f"http://127.0.0.1:5000/{short_code}",
        "clicks": 0
    })


@url_bp.route("/<short_code>")
def redirect_to_url(short_code):

    url_entry = URL.query.filter_by(short_code=short_code).first()

    if not url_entry:
        return jsonify({"error": "Shortened URL not found"}), 404

    if datetime.utcnow() > url_entry.created_at + timedelta(hours=24):
        return jsonify({"error": "This URL has expired"}), 410

    url_entry.clicks += 1
    db.session.commit()

    return redirect(url_entry.original_url)
