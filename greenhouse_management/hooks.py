# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "greenhouse_management"
app_title = "Greenhouse Management"
app_publisher = "Brandon Fox, Foxtrot"
app_description = "Custom app for managing the data entry, tracking and reporting for commercial greenhouse operations. This apps function is STRICTLY enviromental control.Will track gre"
app_icon = "octicon octicon-file-directory"
app_color = "green"
app_email = "company@foxtrot.email"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/greenhouse_management/css/greenhouse_management.css"
# app_include_js = "/assets/greenhouse_management/js/greenhouse_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/greenhouse_management/css/greenhouse_management.css"
# web_include_js = "/assets/greenhouse_management/js/greenhouse_management.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "greenhouse_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "greenhouse_management.install.before_install"
# after_install = "greenhouse_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "greenhouse_management.notifications.get_notification_config"

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
# 		"greenhouse_management.tasks.all"
# 	],
# 	"daily": [
# 		"greenhouse_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"greenhouse_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"greenhouse_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"greenhouse_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "greenhouse_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "greenhouse_management.event.get_events"
# }

