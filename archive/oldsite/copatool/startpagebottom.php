<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<link href="copatoolstyle.css" rel="stylesheet" type="text/css">
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<title>Copatool - Home</title>
	</head>
	
	<body style="margin: 10px; background: #D9A251; ">
		<form method="POST" action="copajavaphp.php">
			<p>Input ID numbers here:
			<input type="text" name="chosenIdentificationNumbers" size="80" id="IDField">
			Then select an area:
			<select name="chosenLink">
				<option value="1">Child Data Sheet</option>
				<option value="2">Family Data Sheet</option>
				<option value="3">Child Program Information Edit Sheet</option>
				<option value="4">Child Health History Edit Sheet</option>
				<option value="5">Child Medical Record Edit Sheet</option>
			</select>
			<input type="submit" value="Submit" name="submit"></p>
			<script language="JavaScript">
    			document.getElementById("IDField").maxLength = 10000;
			</script>
		</form>
	</body>
</html>
