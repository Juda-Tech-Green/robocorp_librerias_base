from RPA.Email.ImapSmtp import ImapSmtp
import os


class EmailKeywords:
    def __init__(self, gmail_account, gmail_password):
        self.email = ImapSmtp(smtp_server="smtp.gmail.com",
                              smtp_port=587)
        self.account = gmail_account
        self.password = gmail_password
        
    def _authorize(self):
        self.email.authorize(account=self.account, password=self.password)

    def enviar_email_de_texto(self,
                        recipient_email,
                        mail_subject,
                        mail_body,
                        mail_attachments=None):
        self._authorize()
        self.email.send_message(
            sender=self.account,
            recipients=recipient_email,
            subject=mail_subject,
            body=mail_body,
            attachments=mail_attachments
        )
        print(f"Email de texto enviado a {recipient_email}")

    def enviar_html_email_con_imagen(self,
                                     recipient_email,
                                     mail_subject,
                                     mail_body,
                                     image_file_path):
        self._authorize()
        self.email.send_message(
            sender=self.account,
            recipients=recipient_email,
            subject=mail_subject,
            body=mail_body,
            html=True,
            images=image_file_path
        )
        print(f"Email con html e imagen enviado a {recipient_email}")

    def guardar_adjunto_donde_sujeto_contiene(self, mail_subjetc_to_search,out_dir):        
        self._authorize()

        email_list = self.email.list_messages(f'SUBJECT "{mail_subjetc_to_search}"')

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        
        for email in email_list:
            if email.get("Has-Attachments"):
                self.email.save_attachment(
                    email,
                    target_folder=out_dir,
                    overwrite=True
                )
            
            print(f"Adjunto guardado del correo: {email['Subject']}")

    