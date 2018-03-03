import session
import sys
class VM:

	def __init__(self,conn ,name=None, vmhost=None, datacenter=None, vmhost=None, disks={}):
		#whatever else
		self.conn = conn 
		self.name = name
		self.vmdata = vmdata
		self.datacenter = datacenter
		self.vmhost = vmhost
		self.disks = disks

	#static and will return a vm type
	@staticmethod
	def get_vm(conn, name):
		try:
			response = requests.get('https://')
			#build itself (if I can?)
			return VM(conn,)

		except Exception as error:
			print(error, file=sys.stderr)

	def create_vm(self):
		try:
			response = requests.post('https://createvm')

		except Exception as error:
			print(error,file=sys.stderr) 

