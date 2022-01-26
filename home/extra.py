"""
def reset_password(request):
	otp = randint(100000, 999999)
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.connect('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login('tutoria.reset@gmail.com', 'tutoria2001')
	message = "127.0.0.1/reset_password_confirm\nOTP:{}".format(otp)
	s.sendmail('tutoria.reset@gmail.com', "joshferns19@gmail.com", message)
	s.quit()
	if request.method == 'GET':
		print(request.GET)
	return render(request, 'reset_password.html')	

def reset_password_done(request):
	return render(request, 'reset_password_done.html')

def reset_password_confirm(request):
	return render(request, 'reset_password_confirm.html')

def reset_password_complete(request):
	return render(request, 'reset_password_complete.html')
"""