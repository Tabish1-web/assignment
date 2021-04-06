from flask import jsonify,request

from web import db
from web.api import api
from web.models import Contact,Email

@api.route("/",methods=["GET","POST"])
def Index():
    contacts = Contact.query.all()
    data = request.get_json()
    if request.method == "POST":
        contact = Contact(
            username = data["username"],
            first_name = data["first_name"],
            last_name = data["last_name"],
            phone_no = data["phone_no"]
        )
        db.session.add(contact)
        db.session.commit()

        cont = {}
        cont["username"] = contact.username
        cont["first_name"] = contact.first_name
        cont["last_name"] = contact.last_name
        cont["phone_no"] = contact.phone_no
        cont["emails"] = []

        for email in contact.emails:
            cont["emails"].append(f"{email}")

        return jsonify(cont)

    all_list = []
    for contact in contacts:
        cont = {}
        cont["username"] = contact.username
        cont["first_name"] = contact.first_name
        cont["last_name"] = contact.last_name
        cont["phone_no"] = contact.phone_no
        cont["emails"] = []

        for email in contact.emails:
            cont["emails"].append(f"{email}")

        all_list.append(cont)

    return jsonify({"contacts":all_list})

@api.route("/<string:username>",methods=["GET","PUT","DELETE","POST"])
def Single(username):
    data = request.get_json()
    contact = Contact.query.filter_by(username=username).first()
    
    if not contact:
        return jsonify({"message":"contact not found!"})

    if request.method == "POST":
        if "email" in data:
            mail = Email(
                email = data["email"]
            )
            db.session.add(mail)
            contact.emails.append(mail)
            db.session.commit()
        else:
            return jsonify({"message":"please enter email address"})

        cont = {}
        cont["username"] = contact.username
        cont["first_name"] = contact.first_name
        cont["last_name"] = contact.last_name
        cont["phone_no"] = contact.phone_no
        cont["emails"] = []

        for email in contact.emails:
            cont["emails"].append(f"{email}")

        return jsonify(cont)

    if request.method == "PUT":
        if "username" in data:
            contact.username = data["username"]
        if "first_name" in data:
            contact.first_name = data["first_name"]
        if "last_name" in data:
            contact.last_name = data["last_name"]
        if "phone_no" in data:
            contact.phone_no = data["phone_no"]

        db.session.commit()

        return jsonify({"message":"contact updated successfully!"})
    
    if request.method == "DELETE":
        db.session.delete(contact)
        db.session.commit()

        return jsonify({"message":"contact deleted successfully!"})

@api.route("/search")
def Search():
    arg = request.args.get("username")
    contact = Contact.query.filter_by(username=arg).first()

    if contact:
        cont = {}
        cont["username"] = contact.username
        cont["first_name"] = contact.first_name
        cont["last_name"] = contact.last_name
        cont["phone_no"] = contact.phone_no
        cont["emails"] = []

        for email in contact.emails:
            cont["emails"].append(f"{email}")

        return jsonify(cont)
    else:
        return jsonify({"message":"contact not found!"})