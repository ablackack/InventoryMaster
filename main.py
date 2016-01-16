from tkinter import *
from tkinter import ttk
import json


class InventoryMaster:
	def callback(self, val1=None):
		if self.item_dept_value.get() != "" and self.item_type_value.get() != "" and self.item_cases_value.get() != "":
			self.set_id()

	def set_id(self):
		prefix = self.get_prefix()
		suffix = self.get_suffix()
		x = self.read_config()
		lfd_id = x['counter']
		case = self.get_case()

		id_string = prefix + "-" + lfd_id + "-" + suffix + "/" + case
		print(id_string)
		self.item_id['text'] = id_string

	def read_config(self):
		with open("__config.json") as jdata:
			data = json.load(jdata)
			jdata.close()
			return data

	def write_config(self, wdata):
		with open("__config.json") as jsond:
			json.dump(wdata, jsond, sort_keys=True)

	def get_suffix(self):
		suf = self.item_type_value
		suf_str = suf.get()
		x = self.read_config()
		suffix_value = x['types'][suf_str]
		print("Suffix: " + suffix_value + " - " + suf_str)
		return suffix_value

	def get_prefix(self):
		pre = self.item_dept_value
		pre_str = pre.get()
		x = self.read_config()
		prefix_value = x['depts'][pre_str]
		print("Prefix: " + prefix_value + " - " + pre_str)
		return prefix_value

	def get_case(self):
		cas = self.item_cases_value
		cas_str = cas.get()
		x = self.read_config()
		case_value = x['cases'][cas_str]
		print("Case: " + case_value + " - " + cas_str)
		return case_value

	def show_gui(self):
		root = Tk()
		root.geometry()
		root.wm_title("InventoryMaster")
		root.configure(width=500, height=500)

		# add window elements
		# description
		lbitem_desc = Label(root, text="Bezeichnung:")
		lbitem_desc.place(x=2, y=2)

		item_desc = Entry(root)
		item_desc.place(x=100, y=2, width=200)

		# details
		lbitem_details = Label(root, text="Details:")
		lbitem_details.place(x=2, y=25)

		item_details = Entry(root)
		item_details.place(x=100, y=25, width=200)

		# id
		lbitem_id = Label(root, text="ID:")
		lbitem_id.place(x=320, y=2)

		self.item_id = Label(root, text="00-000000-00/00")
		self.item_id.place(x=340, y=2)

		# type
		self.item_type_value = StringVar()
		x = self.read_config()
		types = []
		for a in x['types']:
			types.append(a)

		types.sort()

		lbitem_type = Label(root, text="Typ:")
		lbitem_type.place(x=2, y=48)

		item_type = ttk.Combobox(root, values=types, textvariable=self.item_type_value)
		item_type.bind("<<ComboboxSelected>>", self.callback)
		item_type.place(x=100, y=48, width=200)

		# department
		self.item_dept_value = StringVar()
		x = self.read_config()
		depts = []
		for a in x['depts']:
			depts.append(a)

		depts.sort()

		lbitem_dept = Label(root, text="Abteilung:")
		lbitem_dept.place(x=2, y=71)

		item_dept = ttk.Combobox(root, values=depts, textvariable=self.item_dept_value)
		item_dept.bind("<<ComboboxSelected>>", self.callback)
		item_dept.place(x=100, y=71, width=200)

		# storage
		self.item_cases_value = StringVar()
		x = self.read_config()
		cases = []
		for a in x['cases']:
			cases.append(a)

		cases.sort()

		lbitem_storage = Label(root, text="Aufbewahrung:")
		lbitem_storage.place(x=2, y=94)

		item_storage = ttk.Combobox(root, values=cases, textvariable=self.item_cases_value)
		item_storage.bind("<<ComboboxSelected>>", self.callback)
		item_storage.place(x=100, y=94, width=200)

		root.mainloop()

	def __init__(self):
		self.show_gui()


im = InventoryMaster()
