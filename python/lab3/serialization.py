import json

class FileItem:
	def __init__(self, file_name):
		self.name=file_name

f=FileItem("/home/ibtissem/intilaq_academy/python/lab1/words")
my_dict=dict(doc="my test file", nb_file=1, my_obj_file=f)

class FileEncoder(json.JSONEncoder):
	def default(self, o):
		if hasattr(o,"__class__"):
			return o.__dict__

print(json.dumps(my_dict, cls=FileEncoder))
#output: {"doc": "my test file", "nb_file": 1, "my_obj_file": {"name": "/home/ibtissem/intilaq_academy/python/lab1/words"}}