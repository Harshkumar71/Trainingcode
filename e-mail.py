import smtplib
try:
    server = smtplib.SMTP(host = 'smtp.gmail.com',port = 587)
    server.starttls()
    recever_email = input("enter your email")
    sender_email = 'harshkumar0342@gmail.com'
    password = 'ccbp wpyj ulqo hppy'
    server.login(sender_email,password=password)
    subject = input("what is your problem")
    body = input("thoda details me btaoo")
    message = f"subject:{subject}\n\n{body}"
    server.sendmail(sender_email,recever_email,message)
    print("mene mail send kar diya h")
    server.quit()
except Exception  as e:
    print("mail send nhi huiiii")    