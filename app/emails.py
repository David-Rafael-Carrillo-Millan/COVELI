from threading import Thread
from flask_mail import Message
from flask import current_app, render_template
from flask_login import current_user


# def confirmacion_compra(mail, usuario, libro):
#     try:
#         message = Message('Confirmacion de compra de libro',
#                             sender = current_app.config['MAIL_USERNAME'],
#                             recipients = ['20213tn051@utez.edu.mx'])
#         message.html = render_template('emails/confirmacion_compra.html', usuario= usuario, libro = libro)
#         mail.send(message) 
#     except Exception as ex:
#         raise Exception(ex)

def confirmacion_compra(app, mail, usuario, libro):
    """Envio email al comprar un libro"""
    try:
        print(f' El usuario es: {usuario.correo_electronico}')
        message = Message('Confirmacion de compra de libro',
                            sender = current_app.config['MAIL_USERNAME'],
                            recipients = [usuario.correo_electronico])
        message.html = render_template('emails/confirmacion_compra.html', usuario= usuario, libro = libro)
        thread = Thread(target=envio_email_async, args=[app, mail, message])
        thread.start()
    except Exception as ex:
        raise Exception(ex)

def confirmacion_registro_usuario(app, mail, correo):
    """Confirmar emial usuario creado"""
    try:
        message = Message('COVELI, confirmacion cuenta creada',
                            sender = current_app.config['MAIL_USERNAME'],
                            recipients = [correo])
        message.html = render_template('emails/confirmacion_cuenta.html')
        thread = Thread(target=envio_email_async, args=[app, mail, message])
        thread.start()
    except Exception as ex:
        raise Exception(ex)

def envio_email_async(app, mail, message):
    with app.app_context():
        mail.send(message)