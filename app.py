from flask import Flask, render_template, request, send_from_directory, url_for
import requests
import os
import json

app = Flask(__name__)
filename = os.path.join(app.static_folder,'linux.json')
with open(filename) as json_file:
    json_file = json.load(json_file)
    
#page for linux command searching 
@app.route('/',  methods=["GET","POST"])
def index():       
    list_of_commands = list(map(lambda x:x['command'], json_file))
    return render_template("index.html",
                           data = list_of_commands)
 
@app.route('/search',  methods=["GET","POST"])
def search():
    if request.method == "POST":
        command = request.form["search_bar"]
    elif request.method == "GET":
        command = request.args["cmd"]
        
    
    search_data = list(filter(lambda x : x['command'] == command,
                                  json_file))
    if len(search_data):
        search_data = search_data[0]
    else:
        search_data = None
        
    return render_template("search.html",
                            data = search_data)
app.run(host='0.0.0.0', port=8080, debug=True)
