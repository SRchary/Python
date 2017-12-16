

#!/usr/bin/env python

import imaplib
import smtplib
from email.parser import HeaderParser
import email
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import config as conf
imap_host = conf.config["imap_cinfig"]["host"]
subject_contain_words = ["You" ,"have" ,"reached" ,"iccid:" ]

def getMsgs(host):
	
	try:
		conn = imaplib.IMAP4_SSL(host)
		conn.login(conf.config["imap_cinfig"]["username"],conf.config["imap_cinfig"]["password"])
		conn.select('Inbox')
		typ, data = conn.search(None,'UNSEEN')
		
		for num in data[0].split():
			is_valied_subject = 0
			#typ, data = conn.fetch(num,'(RFC822)')
			type , data = conn.fetch(num, '(BODY[HEADER.FIELDS (SUBJECT)])')
			
			
			subject = data[0][1]
			subject = subject.replace("Subject:" ,"")
			subject = subject.replace("\r" ,"")
			subject = subject.replace("\n" ,"")
			
			for word in subject_contain_words:
				if word in subject:
					is_valied_subject = 1
				else:
					is_valied_subject = 0
				
			#send mail 
			#print "is valied number "
			#print is_valied_subject
			#print "----------"
			if is_valied_subject:
				
				#if percentage is 100 then call to api
				if "100%" in subject:
					pass
				
				
				#sending mail
				mixed_sub = subject.split("You have reached",1)[1] 
				#print "mixed_sub "
				#print mixed_sub
				#print "----------"
				
				percentage =  mixed_sub.split("%",1)[0] 
				
				#print "percentage "
				#print percentage
				#print "----------"
				
				iccid =  mixed_sub.split("iccid:",1)[1] 
				
				#print "iccid is  "
				#print iccid
				#print "----------"
				send_mail(subject  , percentage  , iccid )
	except Exception:
		invoke_aws(Exception)			
			
def send_mail(subject ="" , percentage =1 , iccid = 1):

	#print percentage
	#print iccid
	try:
		fromaddr = conf.config["smtp_auth"]["smtp_user"]
		toaddr = conf.config["smtp_auth"]["to_email"]
		msg = MIMEMultipart()
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = subject
		
		#body = "Please note that you have reached %i% of your data allowance for the iccid: %i " % (percentage , iccid)
		body = "Please note that you have reached "+str(percentage)+"% of your data allowance for the iccid: "+str(iccid)
		body +=  "\n";
		body +=  "\n";
		body +=  "\n";
		body +=  "Best Regards,";
		body +=  "\n";
		body +=  "Pareteum";
		msg.attach(MIMEText(body, 'plain'))
		
		server = smtplib.SMTP(conf.config["smtp_auth"]["host"], conf.config["smtp_auth"]["port"])
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(conf.config["smtp_auth"]["smtp_user"], conf.config["smtp_auth"]["smtp_password"])
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)			
	except Exception:
		invoke_aws(Exception)
	
	

def invoke_aws(err):
	print err
	exit()

getMsgs(conf.config["imap_cinfig"]["host"])	