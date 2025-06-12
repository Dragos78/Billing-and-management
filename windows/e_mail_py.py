from email.message import EmailMessage
import ssl
import smtplib

from credential_account_for_sending_email import password, sender

def email_sent(email_receiver, security_code):
	email_sender = sender
	email_password= password


	subject = " Reset password"
	body = f"""
	    Dear user,
	
	You've asked to reset the password of ID:{email_receiver}. To verify this ID belongs to you, 
	please enter the security code below into the security input box on the reset password page:
	
	{security_code}
	
	The security code will expire 3 minutes after the email was sent.
	
	Best regards,                                                  
	"""

	emailmessage = EmailMessage()
	emailmessage["From"] = email_sender
	emailmessage["To"] = email_receiver
	emailmessage["Subject"] = subject
	emailmessage.set_content(body)

	context_1 = ssl.create_default_context()
	try:
		with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context_1) as sm:
			sm.login(email_sender, email_password)
			sm.sendmail(email_sender, email_receiver, emailmessage.as_string())
			from Messages.register_dialog_boxes import successfully_email_set
	except Exception as e:
		from Messages.register_dialog_boxes import error_email_sent
		print(f"Error sending email: {e}")