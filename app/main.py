
"""
Usage:
    amity create_room (living|office) <room_name>...
    amity add_person <name> (fellow|staff) [<wants_accomodation>]
    amity reallocate_person <name> <new_room_name>
    amity load_people <filename>
    amity save_people
    amity print_allocated_rooms
    amity print_unallocated_rooms
    amity print_allocations [-o <filename>]
    amity print_unallocated [-o <filename>]
    amity print_room_occupants <room_name>
    amity (-i | --interactive)
    amity (-h | --help)
Options:
    -o, --output  Save to a txt file
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""
import cmd
from docopt import docopt, DocoptExit
from amity import *
from pyfiglet import figlet_format
from termcolor import cprint

def docopt_cmd(func):
	"""
	Decorator definition for the app.
	"""
	def fn(self, arg):

		try:
			opt = docopt(fn.__doc__, arg)
		except DocoptExit as e:
			msg = "Invalid Command."

			print(msg)
			print(e)
			return

		except SystemExit:
			return

		return func(self, opt)

	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)
	return fn

amity = Amity()	

class Amity(cmd.Cmd):
	intro = cprint(figlet_format("Amity", font="big"), "yellow", attrs=['bold'])
	print ("    **********User Guide************    ")
	print ("    Command    Description     Parameter")
	
	print ("type --help-- to view commands")
	prompt = "<--Amity-->"

	@docopt_cmd
	def do_create_room(self, arg):
		"""Usage: create_room <room_names> <room_type>"""
		room_names = arg["<room_names>"]
		room_type = arg["<room_type>"]
		for rooms in room_names:
			amity.create_room(rooms, room_type)

	@docopt_cmd
	def do_add_person(self, arg):
		"""Usage: add_person <name> <employee_type> <need_accomodation>"""	
		
		

	@docopt_cmd
	def do_reallocate_employee(self, arg):
		"""Usage: reallocate_employee <>"""
		

	@docopt_cmd
	def	do_print_room_occupants(self):
		"""Usage: print_room_occupants"""
		
		

	@docopt_cmd
	def do_print_allocated_rooms(self):
		"""Usage: print_allocated_rooms"""
		

	@docopt_cmd
	def do_print_unallocated_rooms(self):
		"""Usage: print_unallocated_rooms"""
		

	@docopt_cmd
	def do_load_people(self):
		"""Usage: load_people"""
		

	@docopt_cmd
	def do_save_people(self, arg):
		"""Usage: save_people"""			
		

	
	def do_quit(self, arg):
		"""Exits the application
	    """
		print ("Welcome again!")
		exit()
if __name__ == '__main__':
	Amity().cmdloop()