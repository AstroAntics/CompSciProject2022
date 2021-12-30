#################################################################################################
#               Abstractor function file. Really, this only exists so that I can                #
#   stop typing the same code 500 times because it annoys me. Also, despite the file location,  #
#         the abstractor also handles template rendering, redirecting, and trivial stuff.       #
# Basically, since I don't want to type everything over and over (I want to keep the code DRY), #
#                         we have the abstractor. It exists for a reason.                       #
#################################################################################################
from flask import render_template
from app import *


# hacky database stuff
def query_by_id(item, _id, get_first):
    if get_first:
        # take the first item we receive
        _var = item.query.filter_by(id=_id).first()
    else:
        # or just take all of the items that match, get_first is only the specifier
        _var = item.query.filter_by(id=_id)
    return _var


# Handle situations where the user specified a "/" at the end of the URL
# We can't let this happen since Flask will throw a 404 error
def strip_end_slashes(url):
    if url.endswith("/"):
        _new_url = url.strip("/")
        return _new_url
    else:
        # Just spit out the raw URL value
        return url


# DISREGARD THIS
# this stuff doesn't actually work!!
# # FLASK FUNCTIONS
# # Template rendering
# def render_page(name, vars=None):
#     if vars is None:
#         vars = []
#         return render_template(name.html)
#     else:
#         return render_template(name.html, vars=[])