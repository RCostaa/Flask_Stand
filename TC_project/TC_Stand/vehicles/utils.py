import secrets, os
from PIL import Image
from flask import current_app
from flask_login import current_user
from flask_mail import Message
from TC_Stand import mail

def send_email(form):
    msg = Message(form.subject.data, sender=current_user.email, 
                    recipients=[form.recipient.data])

    msg_body = f"""This message was sent by the user {current_user.username} via TC_Stand.
Please reply to his email: {current_user.email}.\n\n"""

    msg_body += form.body.data

    msg.body = msg_body

    mail.send(msg)

def save_vehicle_picture(pic, size):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(pic.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, "static/vehicle_pics", picture_fn)
    
    output_size = (size[0], size[1])
    i = Image.open(pic)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

