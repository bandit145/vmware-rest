import requests
import sys
class Session:

	def __init__(self, address, username, password, verify_ssl=True):
		try:
			response = requests.get('https://'+address,auth=(username,password))
			self.authorization = response.headers('vmware-api-session-id')
		except Exception as error:
			print(error, file=sys.stderr)

	def end_session(self):
		try:
			response = requests.post('https://locationtoget rid of key')
		except Exception as error:
			print(error, file=sys.stderr)

	def do_request(self, type, url):
		try:
			response = getattr(requests,type)(url,headers={'content-type':'application/json',
				'vmware-api-session-id':self.authorization})
			return response
		except Exception as error:
			print(error,file=sys.stderr)
