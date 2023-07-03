from flask import Flask, render_template_string, request, redirect, url_for
import datetime

app = Flask(__name__)

q_no = 999


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        queue_number = request.form.get("queue_number").upper()
        current_time = datetime.datetime.now().strftime("%A, %d/%m/%Y, %I:%M:%S %p")
        if "LTR" in queue_number or "MSP" in queue_number or "DIY" in queue_number:
            logo =  "https://upload.wikimedia.org/wikipedia/en/d/d0/Singapore_Land_Authority.png"
        elif "ACR" in queue_number:
            logo = "https://kaiyangaccounting.com/wp-content/uploads/2014/11/acra.png"
        else:
            logo = "https://blog.nus.edu.sg/computingcareerfair/files/formidable/17/IRAS-logo-wrp8td.png"
        html = f"""<!DOCTYPE html>
<html>
<head>
	<title>TBSC Ticket Generator: Done!</title>
	<style>
		body {{
			font-family: Arial, sans-serif;
			font-size: 12px;
			line-height: 1.2;
			text-align: center;
			width: 3.125in;
			margin: 0;
			padding: 10px;
		}}
		.logo {{
			display: block;
			margin: 0 auto;
			max-width: 100%;
			height: auto;
		}}
		.welcome-message {{
			font-size: 25px;
			margin-top: 10px;
			margin-bottom: 5px;
		}}
		.queue-number{{
			font-size: 50px;
			font-weight: bold;
			margin-top: 15px;
			margin-bottom: 15px;
		}}
		p {{
			margin: 0;
		}}
		.secondary-message {{
			font-size: 16px;
			font-style: italic;
			margin-top: 10px;
			margin-bottom: 0px;
		}}
		.time {{
		    margin-bottom: 20px
		}}
	</style>
</head>
<body>
    <!-- <img class="logo" width="150px" src={logo}> -->
	<h1 class="welcome-message">Taxpayer and Business Service Centre</h1>
	<h1></h1>
	<p>Your queue number is:</p>
	<h1 class="queue-number">{queue_number}</h1>
	<p class="secondary-message"><b>Please note that queue numbers may not be called in sequence.</b></p>
	<h1></h1>
	<p class="time">{current_time}</p>
	</br>
	</br>
	</br>
	<h1></h1>
	<h1></h1>
	<h1></h1>
	<p>.</p>
</body>
</html>

"""
        return render_template_string(html)
    else:
        return render_template_string("""<!DOCTYPE html>
<html>
<head>
    <title>TBSC Ticket Generator</title>
    <style>
		body {
			font-family: Arial, sans-serif;
		}
    </style>
</head>
<body>
    <form method="post">
        <label for="queue_number">Enter queue number:</label>
        <input type="text" id="queue_number" name="queue_number">
        <input type="submit" value="Submit">
    </form>
    <h1></h1>
    <ol>
      <li>Enter Queue Number & click submit.</li>
      <li>Enter Ctrl + P to print.</li>
      <li><s>When print dialogue appears, click Enter to confirm.</s></li>
      <li>Click on bookmarks or Ctrl + L + Enter to issue new queue.</li>
    </ol>
    <h1></h1>
    <p>TBSC Ticket Generator: Version 1.3</p>
    <h1></h1>
    <p><i>Dev docs: Settings are Scale 84, Margins None, uncheck Print Headers & Footers.</i></p>
</body>
</html>""")


@app.route("/setq", methods=["GET", "POST"])
def setq():
    if request.method == "POST":
        global q_no
        q_no = int(request.form.get("queue_number")) - 1
        return redirect("/walk-in")
    return render_template_string("""<!DOCTYPE html>
<html>
<head>
    <title>TG: SetQ</title>
</head>
<body>
    <form method="post">
        <label for="queue_number">Set walkin queue number (number only):</label>
        <input type="text" id="queue_number" name="queue_number">
        <input type="submit" value="Submit">
    </form>
</body>
</html>""")


@app.route("/walk-in", methods=["GET", "POST"])
def walk_in():
    global q_no
    q_no += 1
    queue_number = f"F{q_no}"
    current_time = datetime.datetime.now().strftime("%A, %d/%m/%Y, %I:%M:%S %p")
    html = f"""<!DOCTYPE html>
<html>
<head>
	<title>TG: Walk-In</title>
	<style>
		body {{
			font-family: Arial, sans-serif;
			font-size: 12px;
			line-height: 1.2;
			text-align: center;
			width: 3.125in;
			margin: 0;
			padding: 0px;
		}}
		.queue-number{{
			font-size: 50px;
			font-weight: bold;
			margin-top: 0px;
			margin-bottom: 0px;
		}}
		p {{
			margin: 0;
		}}
	</style>
</head>
<body>
	<p>Your <b>walk-in</b> queue number is:</p>
	<h1 class="queue-number">{queue_number}</h1>
	<p><b>Please note that queue numbers may not be called in sequence.</b></p>
</body>
</html>

"""
    return render_template_string(html)

if __name__ == "__main__":
    app.run
