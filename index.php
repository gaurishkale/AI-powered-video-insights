<?php

// exec('python ./ai.py', $output);
// output is: Array ( [0] => Hello amir ! )
// echo $output[0];
// echo file_get_contents( "text.txt" ); // get the contents, and echo it out.
// Hello My Friend!
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<form action="output.php" method="post" enctype="multipart/form-data">
  Select image to upload:
  <input type="file" name="fileToUpload" id="fileToUpload">
  <input type="submit" value="Upload Image" name="submit">
</form>
</body>
</html>