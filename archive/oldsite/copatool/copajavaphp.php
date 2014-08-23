<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
		<link href="copatoolstyle.css" rel="stylesheet" type="text/css">
		<title>Bottom</title>
		<?php
			echo "<script language=\"javascript\">
			<!--
			NextFrame = 0;
			function ChangeFrame()
			{
			 if (parent.frames['BODY']!=null) {
			  NextFrame++;\n";
			 $IDlist  = $_POST['chosenIdentificationNumbers'];
			 $ID = explode(",", $IDlist);
			 
			 $chosenLink = $_POST['chosenLink'];
			 if ($chosenLink == 1)
			 {
			  $goto = "/child/child/index.epl?ID=";
			 } 
			 else if ($chosenLink == 2)
			 {
			  $goto = "/family/family/index1.epl?FID=";
			 }
			 else if ($chosenLink == 3)
			 {
			  $goto = "/child/child/program/update.epl?childID=";
			 }
			 else if ($chosenLink == 4)
			 {
			  $goto = "/child/medicalHistory/healthHistory.epl?childID=";
			 }
			 else if ($chosenLink == 5)
			 {
			  $goto = "/child/medicalHistory/viewScreening.epl?childID=";
			 }
			  
			 
			 
			 echo "			 if (NextFrame > ", count($ID), ")
			  NextFrame == 1;\n";
			 
			 
			 for ($i = 0; $i < count($ID); $i++)
			 {
			  echo "			 if (NextFrame == ", $i+1, ")\n";
			  echo "			  parent.frames['BODY'].location.href=\"https://ccc.mycopa.com", $goto, $ID[$i], "\"\n";
			 }
			 
			 echo "			 }\n			}//--></script>\n";
		?>
	</head>

	<body style="background: #D9A251; ">
		<div id="back">
			<a href="startpagebottom.php">&laquo;&nbsp;Start Over</a>	
		</div>

		<div id="forward">
				<?php
					$to = "mlissner@ccccsd.org";
					$subject = "COPA Tool Used";
					$date = date('l dS \of F Y h:i:s A');
					mail($to, $subject,$date);
				?>		
					
			<form>
				<input type=button value="Next&nbsp;&raquo;" onClick="ChangeFrame()">
			</form>
		</div>
	</body>
</html>
