<?php
	header("Content-Type: application/json; charset=UTF-8");
	
	$link = mysqli_connect("localhost", "studio3f_cel2020", "spR5v&FM","studio3f_cel2020");

	/* check connection */
	if (mysqli_connect_errno()) {
		printf("Connect failed: %s\n", mysqli_connect_error());
		exit();
	}
	
	$myDoctor = [];
	
	$doctor = $_GET['doctor']; 
	$doctor = mysqli_real_escape_string($link, $doctor);
	
	//врачи с таким ID
	$sql = 'SELECT `id`,`full_name`,`code` FROM `doctors` WHERE `id`='.$doctor;
	
	$result = mysqli_query($link, $sql);
	
	if ($result == true) {
			while ($row = mysqli_fetch_array($result)) {
			
			$myDoctor["id"] = $row['id'];
			$myDoctor["code"] = $row['code'];
			$myDoctor["full_name"] = $row['full_name'];
			
			//поликлиники где ведет прием
			$sql = 'SELECT Dep.`organization_id` as id,ORG.`name` as name , 
				ORG.`address` as address , AGR.`code` as agreement
				FROM `doctors_department` AS DD 
				LEFT JOIN `departments` AS Dep
				ON DD.`department_id` = Dep.`id`
				LEFT JOIN `organizations` AS ORG
				ON Dep.`organization_id` = ORG.`id`
				LEFT JOIN `agreements` AS AGR
				ON Dep.`organization_id` = AGR.`organization_id`					
				WHERE DD.`doctor_id`='.$doctor;
			
			$resultdep = mysqli_query($link, $sql);
			
			if ($resultdep == true) {
				$myDepFull = [];
				while ($rowdep = mysqli_fetch_array($resultdep)) {
					
					$myDep["id"]= $rowdep['id'];
					$myDep["name"] = $rowdep['name'];
					$myDep["address"] = $rowdep['address'];
					$myDep["agreement"] = $rowdep['agreement'];
					
					//дни приема 
					$sql = 'SELECT `id`,`date` FROM `doctor_dates` WHERE `doctor_id`='.$row['id'].' AND `organization_id`='.$rowdep['id'];
					
					$resultdate = mysqli_query($link, $sql);
			
					if ($resultdate == true) {
						$myDepDateFull = [];
						while ($rowdate = mysqli_fetch_array($resultdate)) {		
							$myDepDate["date"] = $rowdate['date'];
							
							//время приема
							$sql = 'SELECT `start`,`end`,`free` FROM `doctor_times` WHERE `date_id`='.$rowdate['id'];
							
							$resultime = mysqli_query($link, $sql);
							
							if ($resultime == true) {
								$myDepTimeFull = [];
								while ($rowtime = mysqli_fetch_array($resultime)) {
									$myDepTime["start"] = $rowtime['start'];
									$myDepTime["end"] = $rowtime['end'];
									$myDepTime["free"] = $rowtime['free'];
									$myDepTimeFull[] = $myDepTime;	
								}
								$myDepDate["times"] = $myDepTimeFull;
							}	
							$myDepDateFull[] = $myDepDate;
						}
						$myDep["dates"] = $myDepDateFull;
					}
					if ($myDepDateFull) { 
						$myDepFull[] = $myDep;
					}
				}
				$myDoctor["department"] = $myDepFull;
			}
			//оказываемые услуги врачом
			$sql = 'SELECT S.id as id,S.code as code,S.name as name FROM services_doctors as SD
				LEFT JOIN services as S
				ON SD.service_id=S.id 
				WHERE SD.doctor_id='.$doctor.' AND S.public=1 
				ORDER BY S.name';
			
			$resultservices = mysqli_query($link, $sql);
					
			if ($resultservices == true) {
				$myServicesFull = [];
				while ($rowservices = mysqli_fetch_array($resultservices)) {
					$myServices["id"] = $rowservices['id'];
					$myServices["code"] = $rowservices['code'];
					$myServices["name"] = $rowservices['name'];
					$myServicesFull[] = $myServices;
				}
				$myDoctor["services"] = $myServicesFull;
			}
		}
	}
	$myJSON = json_encode($myDoctor,JSON_UNESCAPED_UNICODE);
	echo $myJSON;
	
?>