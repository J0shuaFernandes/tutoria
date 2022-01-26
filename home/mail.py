import smtplib

def send(email, message):
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.connect('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login('tutoria.reset@gmail.com', 'tutoria2001')
	s.sendmail('tutoria.reset@gmail.com', email, message)
	s.quit()