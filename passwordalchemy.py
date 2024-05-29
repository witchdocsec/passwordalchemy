import rsa
import base64
import lib.db
import lib.parse
import lib.banner

class mainfuncs:
	#generate keyset. first or new
	@staticmethod
	def genkeys(args):
		#generate keypair
		(pubkey, privkey) = rsa.newkeys(2048)
		#if a key is already present
		if args.oldprivatekey:
			with open(args.oldprivatekey,"r") as pemfile:
				oldprivatekey=rsa.PrivateKey._load_pkcs1_pem(pemfile.read())
		#save public key
		with open("pub.pem","w") as pemfile:
				pemfile.write(pubkey._save_pkcs1_pem().decode("utf-8"))
		#if path to save in not specified
		if not args.privatekey:
			print("save this pem to a secure location to decrypt your passwords. If you lose it you can't recover your credentials")
			print(privkey._save_pkcs1_pem().decode("utf-8"))
			print("you can copy and paste it. and leave the prompt blank")
			args.privatekey=input("or we can save it for you here: ")
		#save private key
		with open(args.privatekey,"w") as pemfile:
			pemfile.write(privkey._save_pkcs1_pem().decode("utf-8"))
		#if a key is already present
		if args.oldprivatekey:
			creds=lib.db.fetchall()
		#if creds are present
		try:
			for cred in creds:
				with open(args.privatekey) as pemfile:
					privkey=rsa.PrivateKey._load_pkcs1_pem(pemfile.read())
					pcred=rsa.decrypt(base64.b64decode(cred.ccred),oldprivatekey).decode("utf-8")
					ccred=base64.b64encode(rsa.encrypt(pcred.encode("utf-8"),pubkey)).decode("utf-8")
					lib.db.update(cred.domain,ccred)
		except:
			pass	
	
	#fetch a credential		
	@staticmethod			
	def fetch(args):
		#send to db library fetch function
		ccred=lib.db.fetch(args.domain)
		with open(args.privatekey, "r") as pemfile:
			#load rsa private key
			privkey=rsa.PrivateKey._load_pkcs1_pem(pemfile.read())
			#print credential
			print(rsa.decrypt(base64.b64decode(ccred),privkey).decode("utf-8"))

	#store a credential
	@staticmethod
	def store(args):
		with open("pub.pem","r") as pemfile:
			#load rsa public key
			pubkey=rsa.PublicKey._load_pkcs1_pem(pemfile.read())
			#encrypted credential
			ccred=base64.b64encode(rsa.encrypt(args.password.encode("utf-8"),pubkey)).decode("utf-8")
			#send to db library store function
			print(lib.db.store(args.domain,ccred))

	#update a credential
	@staticmethod
	def update(args):
		with open("pub.pem","r") as pemfile:
			#load rsa public key
			pubkey=rsa.PublicKey._load_pkcs1_pem(pemfile.read())
			#encrypted credential
			ccred=base64.b64encode(rsa.encrypt(args.password.encode("utf-8"),pubkey)).decode("utf-8")
			#send to db update store function
			print(lib.db.update(args.domain,ccred))

if __name__ == "__main__":
	#banner
	lib.banner.banner()
	#command line arguments
	args=lib.parse.parser()
	#get function name from arguments
	if args.command:
		command=getattr(mainfuncs,args.command)
		#execute
		command(args)
