contents = '''<!DOCTYPE >
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>HTML Form</title>

<style type="text/css">

* { margin: 0; padding: 0; }

html { height: 100%; font-size: 62.5% }

body { height: 100%; background-color: #FFFFFF; font: 1.2em Verdana, Arial, Helvetica, sans-serif; }


/* ==================== Form style sheet ==================== */

form { margin: 25px 0 0 29px; width: 450px; padding-bottom: 30px; }

fieldset { margin: 0 0 22px 0; border: 1px solid #2B6600; padding: 12px 17px; background-color: #DAF5C7; }
legend { font-size: 1.1em; background-color: #2B6600; color: #FFFFFF; font-weight: bold; padding: 4px 8px; }

label.float { float: left; display: block; width: 100px; margin: 4px 0 0 0; clear: left; }
label { display: block; width: auto; margin: 0 0 10px 0; }
label.spam-protection { display: inline; width: auto; margin: 0; }

input.inp-text, textarea, input.choose, input.answer { border: 1px solid #909090; padding: 3px; }
input.inp-text { width: 300px; margin: 0 0 8px 0; }
textarea { width: 400px; height: 150px; margin: 0 0 12px 0; display: block; }

input.choose { margin: 0 2px 0 0; }
input.answer { width: 40px; margin: 0 0 0 10px; }
input.submit-button { font: 1.4em Georgia, "Times New Roman", Times, serif; letter-spacing: 1px; display: block; margin: 23px 0 0 0; }

form br { display: none; }

/* ==================== Form style sheet END ==================== */

</style>

<!--[if IE]>
<style type="text/css">

/* ==================== Form style sheet for IE ==================== */

fieldset { padding: 22px 17px 12px 17px; position: relative; margin: 12px 0 34px 0; }
legend { position: absolute; top: -12px; left: 10px; }
label.float { margin: 5px 0 0 0; }
label { margin: 0 0 5px 0; }
label.spam-protection { display: inline; width: auto; position: relative; top: -3px; }
input.choose { border: 0; margin: 0; }
input.submit-button { margin: -10px 0 0 0; }
.image{position:absolute ;border:1px solid red ; top:0px ;left: 500px;height: 140px ; width: 638px ;padding:0px; }
               
/* ==================== Form style sheet for IE end ==================== */

</style>
<![endif]-->
<title>My First HTML</title>
  <meta charset="UTF-8">
</head>


<body> <br />
        <h1 align="center" style="font-size:40px;">Form Registration</h1> <br/>
	<form action="" method="post">
   
		<!-- ============================== Fieldset 1 ============================== -->
		<fieldset>
			<legend>Personal Details:</legend>
				<label for="Name" class="float"><strong>Name :</strong></label><br />
				<input class="inp-text" name="input-one-name" value="Nikhil" id="input-one" type="text" size="30" /><br />

				<label for="Age" class="float"><strong>Age :</strong></label><br />
				<input class="inp-text" name="input-two-name" value="21"  id="input-two" type="text" size="30" /><br />

                                <label for="Gender" class="float"><strong>Gender :</strong></label><br />
				<input class="inp-text" name="input-three-name" value="Male" id="input-three" type="text" size="30" /><br />

                                <label for="CGPA" class="float"><strong>CGPA :</strong></label><br />
				<input class="inp-text" name="input-four-name" value="9.6" id="input-four" type="text" size="30" />


		</fieldset>
		<!-- ============================== Fieldset 1 end ============================== -->

                <div class=image>
                <img src="dataSet/User.2.18.jpg" alt="autumn" width="200" height="140" >
		</div>

		<p><input class="submit-button" type="submit" alt="SUBMIT" name="SUBMIT" value="Login" /></p>
	</form>

</body>
</html>


'''

def main():
    browseLocal(contents)

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac

main()
