import smtplib
from datetime import datetime
import pytz
import json
import os


# Ensure that time is in SG timezone
def utc_to_time(naive, timezone="Singapore"):
  return naive.replace(tzinfo=pytz.utc).astimezone(pytz.timezone(timezone))

def send_email():
  email = os.environ.get("EMAIL")

  # set up the SMTP server
  now = utc_to_time(datetime.utcnow())
  s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
  s.starttls()
  s.login("auto-temp@outlook.com", "lmaoboi123")

  FROM = "auto-temp@outlook.com"
  TO = email

  SUBJECT = "TTS Posted"
  TEXT = f'''Your temperature was successfully updated on {now.strftime("%B %d, %Y")} at {now.strftime("%H:%M:%S")}. Stay safe from COVID-19!
Please stop the script and do declarations and temperature taking manually if you are not feeling well.
  '''

  message = "Subject: {}\n\n{}".format(SUBJECT, TEXT)

  print("Sending mail")
  s.sendmail(FROM, TO, message)
  s.quit()

if __name__ == "__main__":
  send_email()