import argparse
def parser():
	parser = argparse.ArgumentParser(description="passwordalchemy args")
	subparse=parser.add_subparsers(dest="command")

	fetchparser=subparse.add_parser("fetch")
	fetchparser.add_argument("-pk","--privatekey",required=True, help="path to private key pem file")
	fetchparser.add_argument("-d", "--domain",required=True)

	storeparser=subparse.add_parser("store")
	storeparser.add_argument("-d", "--domain",required=True)
	storeparser.add_argument("-p", "--password",required=True)

	updateparser=subparse.add_parser("update")
	updateparser.add_argument("-d", "--domain",required=True)
	updateparser.add_argument("-p", "--password",required=True)

	gkparser=subparse.add_parser("genkeys")
	gkparser.add_argument("-pk","--privatekey")
	gkparser.add_argument("-opk","--oldprivatekey")

	args = parser.parse_args()
	return args