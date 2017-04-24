<?php
$tmp = fopen($_POST['fileName'], 'rb');
@flock($tmp, LOCK_SH);
$contents = file_get_contents($_POST['fileName']);
echo $contents;
@flock($tmp, LOCK_UN);
fclose($tmp);
?>
