from docker import Client


class DockerManager:
	
	def __init__(self):
		
		try:
			self.cli = Client(base_url="tcp://192.168.0.2:2376", version='auto')
		except Exception as e:
			raise Exception(e)

 	def getContainers(self, todos=True):

		try:
			return [ c for c in self.cli.containers(all=todos) ]
		except Exception as e:
			raise Exception(e)

if __name__ == '__main__':
	try: 

		manager = DockerManager()

		for c in manager.getContainers():
			print c

	except Exception as e:
		print "Falhou: %s" % e

# 	for c in cli.containers():
# 		print c

# except Exception as e:
# 	print e