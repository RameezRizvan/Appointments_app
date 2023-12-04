// Copyright (c) 2023, rameez and contributors
// For license information, please see license.txt

frappe.ui.form.on("Appointment", {
	refresh(frm) {
        frm.set_query('shift',(doc)=> {
            return {
                filters:{
                    "clinic":doc.clinic
                }
            }
        })

    },
 });
