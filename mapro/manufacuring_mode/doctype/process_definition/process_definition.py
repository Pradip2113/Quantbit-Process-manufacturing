# Copyright (c) 2023, Pradip and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ProcessDefinition(Document):
	@frappe.whitelist()
	def itrate(self,doctype):
		for j in self.get('materials'):
			j.amount=j.quantity*j.rate
		for m in self.get('finished_products'):
			m.amount=m.quantity*m.rate
		for k in self.get('scrap'):
			k.amount=k.quantity*k.rate
