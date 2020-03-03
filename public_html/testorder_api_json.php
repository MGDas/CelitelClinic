<?php
	header("Content-Type: application/json; charset=UTF-8");
	
	$link = mysqli_connect("localhost", "studio3f_cel2020", "spR5v&FM","studio3f_cel2020");

	/* check connection */
	if (mysqli_connect_errno()) {
		printf("Connect failed: %s\n", mysqli_connect_error());
		exit();
	}
	
	$myDoctor = [];
	
	 
	if (isset($_GET['orderFiltersName'])) {
		$doctor = $_GET['orderFiltersName'];
		$doctor = mysqli_real_escape_string($link, $doctor);
		}
	else{
		$doctor = "";
		}
	
	if (isset($_GET['orderFiltersSpecialization'])) {
		$specialization = $_GET['orderFiltersSpecialization']; 
		$specialization = mysqli_real_escape_string($link,$specialization);
		}
	else{
		$specialization = "";
		}
	
	if (isset($_GET['orderFiltersAddress'])) {
		$address = $_GET['orderFiltersAddress']; 
		$address = mysqli_real_escape_string($link,$address);
		}
	else{
		$address = "";
		}
	
	//врачи с таким ФИО , профессией и адресом
	$sql = "SELECT 
			d.id,d.full_name,d.code,d.avatar,d.academic_degree,d.experience 
			FROM doctors as d 
			LEFT JOIN doctors_specialization as ds
			ON d.id = ds.doctor_id
			LEFT JOIN specialization as s
			ON ds.specialization_id=s.id
			LEFT JOIN doctors_department as dd 
			ON d.id=dd.doctor_id
			LEFT JOIN departments as dep
			ON dd.department_id=dep.id
			LEFT JOIN organizations as o
			ON dep.organization_id=o.id
			WHERE d.full_name Like '%$doctor%' AND s.name like '%$specialization' AND o.address LIKE '%$address' AND d.main_code='' AND d.public=1 
			GROUP BY d.id,d.full_name,d.code,d.academic_degree,d.experience
			ORDER BY d.full_name";
	
	$result = mysqli_query($link, $sql);
	
	if ($result) {
			$myDoctorFull = [];
			while ($row = mysqli_fetch_array($result)) {
			
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
				WHERE DD.`doctor_id`='.$row['id'].' AND AGR.public=1  
				GROUP BY Dep.`organization_id`,ORG.`name`,ORG.`address`,AGR.`code`';
			
			$resultdep = mysqli_query($link, $sql);
			
			if ($resultdep) {
				$myDepFull = [];
				while ($rowdep = mysqli_fetch_array($resultdep)) {
					
					$myDep["id"]= $rowdep['id'];
					$myDep["name"] = $rowdep['name'];
					$myDep["address"] = $rowdep['address'];
					$myDep["agreement"] = $rowdep['agreement'];
					
					//дни приема 
					$sql = 'SELECT `id`,`date` FROM `doctor_dates` WHERE `doctor_id`='.$row['id'].' AND `organization_id`='.$rowdep['id'];
					
					$resultdate = mysqli_query($link, $sql);
			
					if ($resultdate) {
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
				if ($myDepFull) { 
						$myDoctor["id"] = $row['id'];
						$myDoctor["code"] = $row['code'];
						$myDoctor["full_name"] = $row['full_name'];
						$myDoctor["avatar"] = "https://celitel05.ru/media/".$row['avatar'];
						$myDoctor["academic_degree"] = $row['academic_degree'];
						$myDoctor["experience"] = $row['experience'];
						$myDoctor["url"] = "/doctors/".$row['id'];
						$myDoctor["department"] = $myDepFull;
					}
			}
			if ($myDoctor) {
				//оказываемые услуги врачом
				$sql = 'SELECT S.id as id,S.code as code,S.name as name FROM services_doctors as SD
					LEFT JOIN services as S
					ON SD.service_id=S.id 
					WHERE SD.doctor_id='.$row['id'].' AND S.public=1
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
			$myDoctorFull[] = $myDoctor;
		}
	}
	$myJSON = json_encode($myDoctorFull,JSON_UNESCAPED_UNICODE);
	echo $myJSON;
	
?>