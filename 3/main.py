import email
import smtplib
import imaplib
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class EMail:
    SMTP_HOST = ""
    SMTP_PORT = 0
    IMAP_HOST = ""
    IMAP_PORT = 0

    def send_message(self, login, password, subject, recipients, message):
        # send message
        msg = MIMEMultipart()
        msg["From"] = login
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.SMTP_HOST, self.SMTP_PORT)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(login, password)
        ms.sendmail(login, ms, msg.as_string())

        ms.quit()
        # send end

    def receive_message(self, login, password, header):
        # receive
        mail = imaplib.IMAP4_SSL(self.IMAP_HOST, self.IMAP_PORT)
        mail.login(login, password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else "ALL"
        result, data = mail.uid("search", None, criterion)
        assert data[0], "There are no letters with current header"
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid("fetch", latest_email_uid, "(RFC822)")
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        # end receive


class GMail(EMail):
    def __int__(self):
        self.SMTP_HOST = "smtp.gmail.com"
        self.SMTP_PORT = 587
        self.IMAP_HOST = "imap.gmail.com"
        self.IMAP_PORT = 993


if __name__ == "__main__":
    gmail = GMail()

    # send message example
    gmail.send_message(
        "login@gmail.com",
        "qwerty",
        "Subject",
        ["vasya@email.com", "petya@email.com"],
        "Message",
    )

    # receive message example
    gmail.receive_message("login@gmail.com", "qwerty", None)
