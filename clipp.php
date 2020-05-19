<?php
                  
if(isset($_POST['textdata']))
{
$data=$_POST['textdata'];
$fp = fopen('Clipboards/clipcl.txt', 'a');
fwrite($fp, $data);
fclose($fp);
}
sleep(1);
header("Location: index.html");
?>