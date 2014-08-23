<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<link href="copatoolstyle.css" rel="stylesheet" type="text/css">
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<title>Copatool - Home</title>
	</head>
	
	<body onLoad="document.loginbox.username.focus();">
		<table width="100%" margin="0" bgcolor="#D9A251">
			<tr>
			<td><img src="logo_copa.gif">
			</td>
			</tr>
		</table>
		<div id="content">
		<h2>Welcome to the COPA Tool</h2>
		<h3>To proceed, please follow the directions below:</h3>
		<ul>
			<li>First, make sure you are logged into COPA. To do this, enter your COPA username and password below.</li>
			<li>Once you are logged in, paste the ID's you would like to work on in the box below, separated by commas (e.g. 120323,112032,123458). These can be Family or Child IDs.</li>
			<li>Next, select the area of COPA you would like to see for each of those children, and press submit.</li>
			<li>In the next window, press the next and previous buttons until you have finished your work.</li>
		</ul>
		
		<form action="http://ccc.mycopa.com/login.epl"  method="post" name="loginbox">
			<label for="username">COPA Username:</label><br><input id="username" name="username" type="text"  size="15" value=""><br>
			<label for="password">COPA Password:</label><br><input id="password" name="password" type="password"  size="15" value=""><br>
			<input type="submit" value="Continue" name="submit"></p>
		</form>
		
		<br>
		<p>Enjoy your time with this tool. Your life just got a little easier.</p>
		<h3><a href="mailto:mlissner@michaeljaylissner.com?subject=COPA Multi-Tool">Feedback? Click here.</a></h3>
		</div>
	</body>
</html>
