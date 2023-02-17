import email
import email.parser
import email.policy
import re
import string

import html2text


#
# Get subject, date, from and body as text from email RFC822 style string
#
def email2Text(rfc822mail):
    # parse the message
    msg_data = email.message_from_bytes(rfc822mail, policy=email.policy.default)

    mail_value = {}

    # Get From, Date, Subject
    mail_value["from"] = header_decode(msg_data.get("From"))
    mail_value["date"] = header_decode(msg_data.get("Date"))
    mail_value["subject"] = header_decode(msg_data.get("Subject"))

    # print( mail_value["date"] )
    # print( mail_value["from"] )
    # print( mail_value["subject"] )

    # Get Body
    # print("--- body ---")
    mail_value["body"] = []
    if msg_data.is_multipart():
        for part in msg_data.walk():
            ddd = msg2bodyText(part)
            if ddd is not None:
                mail_value["body"].append(ddd)
    else:
        # print("--- single ---")
        ddd = msg2bodyText(msg_data)
        mail_value["body"].append(ddd)

    return mail_value


#
# get body text from a message (EmailMessage instance)
#
def msg2bodyText(msg):
    ct = msg.get_content_type()
    cc = msg.get_content_charset()  # charset in Content-Type header
    cte = msg.get("Content-Transfer-Encoding")
    # print("part: " + str(ct) + " " + str(cc) + " : " + str(cte))

    # skip non-text part/msg
    if msg.get_content_maintype() != "text":
        return None

    # get text
    ddd = msg.get_content()

    # html to text
    if msg.get_content_subtype() == "html":
        try:
            ddd = html2text.html2text(ddd)
        except:
            print("error in html2text")

    return ddd


def header_decode(header):
    hdr = ""
    for text, encoding in email.header.decode_header(header):
        if isinstance(text, bytes):
            text = text.decode(encoding or "us-ascii")
        hdr += text
    return hdr


def remove_hyperlink(word):
    return re.sub(r"http\S+", "", word)


def to_lower(word):
    result = word.lower()
    return result


def remove_number(word):
    result = re.sub(r"\d+", "", word)
    return result


def remove_punctuation(word):
    result = word.translate(str.maketrans(dict.fromkeys(string.punctuation)))
    return result


def remove_whitespace(word):
    result = " ".join(word.split())
    return result


def replace_newline(word):
    return word.replace("\n", " ").replace("\r", " ")


def clean_up_pipeline(text):
    text = str(text)
    cleaning_utils = [
        remove_hyperlink,
        replace_newline,
        to_lower,
        remove_number,
        remove_punctuation,
        remove_whitespace,
    ]
    for func in cleaning_utils:
        try:
            text = " ".join([func(word) for word in text.split()])
        except:
            print(f"text: {text}")

    return text
