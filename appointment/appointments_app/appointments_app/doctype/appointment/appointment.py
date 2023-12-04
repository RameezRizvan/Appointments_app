# Copyright (c) 2023, rameez and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Appointment(Document):
	def on_update(self):
		print("your queue number is: abc")

	# def add_to_appointment_queue(self):
		
	# 	q= frappe.get_doc(
	# 		"Appointment Queue",
	# 		{
	# 		"date":self.date,
	# 		"shift":self.shift,
	# 		"clinic":self.clinic,
	# 	    },
	# 	)

	# 	q.queue.append("queue",{"appointment": self.name,"status":"Pending"})
	# 	q.save()
	# 	return len(q.queue)

