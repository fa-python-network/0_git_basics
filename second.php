<?
	if(isset($_REQUEST['github_login'])){
		$login = htmlspecialchars($_POST['login']);
		
		exit($login);
	}
?>