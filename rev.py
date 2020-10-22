import smtplib
sender_email = "parassingh016jan@gmail.com"
rec_email = "kartikey1108@gmail.com"
password = input(str("plzz enter your password : "))
message = "hlo , this was sent by using python"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("login successfill")
server.sendmail(sender_email, rec_email, message)
print ("email has been sent to ", rec_email)