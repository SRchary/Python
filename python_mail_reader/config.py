config = {

"imap_cinfig":{
		"username": "sr27631@gmail.com",
		"password": "your mail password",
		"host": "imap.gmail.com",
		"port": 993,
		"tls": True,
		"connTimeout": 10000,
		"authTimeout": 5000, 
		"debug": "console.log",


		"mailbox": "INBOX", 

		"markSeen": True,
		"fetchUnreadOnStart": True, 
		"mailParserOptions": {"streamAttachments": True},
		"attachments": True, 
		"attachmentOptions": { "directory": "attachments/" }
 
	},
	
	"smtp_auth" :{
		
		"host": "smtp.gmail.com",
        "port": 587,
		"starttls":True,
        "secure": False, 
		"smtp_user": "sr27631@gmail.com",
		"smtp_password": "your mail password",
		"to_email": "tomail@gmail.com",
		
		
		
	}

}




