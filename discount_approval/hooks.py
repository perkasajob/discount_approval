# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "discount_approval"
app_title = "Discount Approval"
app_publisher = "Quantum Lambs"
app_description = "App for approval of proposed discount"
app_icon = "octicon octicon-tag"
app_color = "grey"
app_email = "perkasajob@quantum-laboratories.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/discount_approval/css/discount_approval.css"
# app_include_js = "/assets/discount_approval/js/discount_approval.js"

# include js, css files in header of web template
# web_include_css = "/assets/discount_approval/css/discount_approval.css"
# web_include_js = "/assets/discount_approval/js/discount_approval.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "discount_approval.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "discount_approval.install.before_install"
# after_install = "discount_approval.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "discount_approval.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"discount_approval.tasks.all"
# 	],
# 	"daily": [
# 		"discount_approval.tasks.daily"
# 	],
# 	"hourly": [
# 		"discount_approval.tasks.hourly"
# 	],
# 	"weekly": [
# 		"discount_approval.tasks.weekly"
# 	]
# 	"monthly": [
# 		"discount_approval.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "discount_approval.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "discount_approval.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "discount_approval.task.get_dashboard_data"
# }

