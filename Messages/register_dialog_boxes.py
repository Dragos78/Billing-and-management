from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton


def show_dialog(parent, title, message):
    dialog = QDialog(parent)
    dialog.setWindowTitle(title)

    layout = QVBoxLayout()

    message_label = QLabel(message)
    layout.addWidget(message_label)

    button = QPushButton("OK")
    layout.addWidget(button)
    button.clicked.connect(dialog.accept)

    dialog.setLayout(layout)
    dialog.exec()


def user_type_empty(parent):
    show_dialog(parent, "Error", "Please select a user type.")


def first_name_empty(parent):
    show_dialog(parent, "Error", "Please enter your first name.")


def last_name_empty(parent):
    show_dialog(parent, "Error", "Please enter your last name.")


def e_mail_empty(parent):
    show_dialog(parent, "Error", "Please enter your e-mail.")


def e_mail_validator(parent):
    show_dialog(parent, "Error", "Please enter a valid e-mail address.")


def password_empty(parent):
    show_dialog(parent, "Error", "Please enter a password.")


def password_complexity(parent):
    show_dialog(parent, "Error", "Password must contain at least 8 characters, one uppercase letter, one number, and one special character.")


def confirm_password_empty(parent):
    show_dialog(parent, "Error", "Please confirm your password.")


def password_check(parent):
    show_dialog(parent, "Error", "Passwords do not match.")


def email_exists(parent):
    show_dialog(parent, "Error", "An account with this email already exists.")


def successfully_info(parent):
    show_dialog(parent, "Success", "You have successfully registered!")

def successfully_email_set(parent):
    show_dialog(parent, "Succes", "The e-mail has been sent!")

def error_email_sent(parent):
    show_dialog(parent, "Error", "Error sending email!")
