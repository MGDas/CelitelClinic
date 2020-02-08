<?php
header("Access-Control-Allow-Origin: *");

$Number = strtotime("now");
$Date = date('Y-m-d\TH:i:s');
$Name = explode(' ', $_POST['orderModalName'])[1];
$Surname = explode(' ', $_POST['orderModalName'])[0];
$Lastname = explode(' ', $_POST['orderModalName'])[2];
$Birthday = $_POST['orderModalBirthday'] . "T00:00:00";
$Gender = $_POST['orderModalGender'];
$Tel = $_POST['orderModalPhone'];
$ServiceCode = $_POST['orderModalService'];
$DocCode = explode('&', $_POST['doctorCode'])[0];
$DocName = explode('&', $_POST['doctorCode'])[1];
$Start = explode(' ', $_POST['appointmentTime'])[0];
$End = explode(' ', $_POST['appointmentTime'])[1];
$Agreement = $_POST['doctorAgreement'];

$formObject = '{"ID":"medsite.loc-s1-1414471395","Number":"' . $Number. '","Date":"' . $Date . '","Name":"' . $Name . '","Surname":"' . $Surname . '","LastName":"' . $Lastname . '","Birthday":"' . $Birthday . '","Gender":"' . $Gender . '","Tel":"' . $Tel . '","Mail": "","Scancode":"","Comment": "","Services":[{"ServiceCode":"' . $ServiceCode . '","DocCode":"' . $DocCode . '","Start":"' . $Start . '","End":"' . $End . '","Status":"Заказано","Agreement":"' . $Agreement . '"}]}';

$url = "http://91.205.128.70/MedicinePolic/hs/bitrixsite/CreateTalon/";
$username='vector';
$password='112233';

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

$htmlStart = "<html><head></head><body>";
$htmlEnd = "</body></html>";
$emess = $htmlStart . '<pre>' . '<p>Номер: ' . $Number. '</p><p>Дата: ' . $Date . '</p><p>Фамилия: ' . $Surname . '</p><p>Имя: ' . $Name . '</p><p>Отчество: ' . $Lastname . '</p><p>День рождения: ' . $Birthday . '</p><p>Пол: ' . $Gender . '</p><p>Телефон: ' . $Tel . '</p><p>Электронная почта: </p><p>Сканкод:</p><p>Комментарий: </p><p>Код услуги: ' . $ServiceCode . '</p><p>Доктор: ' . $DocName . '</p><p>Началао записи: ' . $Start . '</p><p>Конец записи: ' . $End . '</p><p>Статус ответа 1С сервера:Заказано</p><p>Соглашение: ' . $Agreement . '</p>' . '</pre>' . $htmlEnd;
$subj = "Запись на прием с сайта celitel05.ru";
$femail = "Site";
$ehead = "MIME-Version: 1.0" . "\r\n" . "Content-type: text/html; charset=UTF-8" . "\r\nFrom: it@celitel05.ru\r\n";
$mailsend = mail("crm@celitel05.ru", "$subj", "$emess", "$ehead");

echo $result;


?>
