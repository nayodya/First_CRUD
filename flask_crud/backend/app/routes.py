from flask import Blueprint, request, jsonify
from .models import PersonalDetail
from . import db

main = Blueprint("main", __name__)

# Create
@main.route("/api/personal-details", methods=["POST"])
def add_detail():
    data = request.get_json()
    detail = PersonalDetail(
        name=data["name"],
        age=data["age"],
        gender=data.get("gender"),
        phone=data.get("phone"),
        address=data.get("address")
    )
    db.session.add(detail)
    db.session.commit()
    return jsonify({"message": "Detail added successfully"}), 201

# Read all
@main.route("/api/personal-details", methods=["GET"])
def get_details():
    details = PersonalDetail.query.all()
    return jsonify([
        {
            "id": d.id,
            "name": d.name,
            "age": d.age,
            "gender": d.gender,
            "phone": d.phone,
            "address": d.address
        } for d in details
    ])

# Update
@main.route("/api/personal-details/<int:id>", methods=["PUT"])
def update_detail(id):
    data = request.get_json()
    detail = PersonalDetail.query.get_or_404(id)
    detail.name = data.get("name", detail.name)
    detail.age = data.get("age", detail.age)
    detail.gender = data.get("gender", detail.gender)
    detail.phone = data.get("phone", detail.phone)
    detail.address = data.get("address", detail.address)
    db.session.commit()
    return jsonify({"message": "Detail updated successfully"})

# Delete
@main.route("/api/personal-details/<int:id>", methods=["DELETE"])
def delete_detail(id):
    detail = PersonalDetail.query.get_or_404(id)
    db.session.delete(detail)
    db.session.commit()
    return jsonify({"message": "Detail deleted successfully"})