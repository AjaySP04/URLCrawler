from urllib.parse import urlparse


#: get the domain name for the website used.

def get_sub_domain_name(url = ''):

	try:
		return urlparse(url).netloc
	except Exception as e:
		print("Couldn't find the url location. Error : {}".format(e))
		return ''

def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		return results[-2] + '.' + results[-1]
	except Exception as e:
		return ''

def main():
	url = "https://mail.google.com/mail/u/0/#inbox"
	print(get_domain_name(url))

if __name__ == '__main__':
	main()