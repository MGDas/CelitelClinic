<?php
header("Access-Control-Allow-Origin: *");

$Number = strtotime("now");
$Date = date('Y-m-d\TH:i:s');
$Name = explode(' ', $_POST['orderModalName'])[0];
$Surname = explode(' ', $_POST['orderModalName'])[1];
$Lastname = explode(' ', $_POST['orderModalName'])[2];
$Birthday = $_POST['orderModalBirthday'] . "T00:00:00";
$Gender = $_POST['orderModalGender'];
$Tel = $_POST['orderModalPhone'];
$ServiceCode = $_POST['orderModalService'];
$DocCode = $_POST['doctorCode'];
$Start = explode(' ', $_POST['appointmentTime'])[0];
$End = explode(' ', $_POST['appointmentTime'])[1];
$Agreement = $_POST['doctorAgreement'];

$formObject = '{"ID":"medsite.loc-s1-1414471395","Number":"' . $Number. '","Date":"' . $Date . '","Name":"' . $Name . '","Surname":"' . $Surname . '","LastName":"' . $Lastname . '","Birthday":"' . $Birthday . '","Gender":"' . $Gender . '","Tel":"' . $Tel . '","Mail": "","Scancode":"","Comment": "","Services":[{"ServiceCode":"' . $ServiceCode . '","DocCode":"' . $DocCode . '","Start":"' . $Start . '","End":"' . $End . '","Status":"Заказано","Agreement":"' . $Agreement . '"}]}';

$url = "http://91.205.128.70/MedicinePolic/hs/bitrixsite/CreateTalon/";
$username='vector';
$password='112233';

//open connection
$ch = curl_init();

//set the url, number of POST vars, POST data
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $formObject);
curl_setopt($ch, CURLOPT_USERPWD, "$username:$password");
curl_setopt($ch, CURLOPT_TIMEOUT, 30);

//So that curl_exec returns the contents of the cURL; rather than echoing it
curl_setopt($ch,CURLOPT_RETURNTRANSFER, true); 

//execute post
$result = curl_exec($ch);
echo $result;


?>
