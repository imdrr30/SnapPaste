<?php
$info = pathinfo($_FILES['upl']['name']);
$ext = $info['extension'];
$newname = "toClip.".$ext;
$target = 'uploads/'.$newname;
move_uploaded_file( $_FILES['upl']['tmp_name'], $target);
sleep(3);
header("Location: index.html");
?>