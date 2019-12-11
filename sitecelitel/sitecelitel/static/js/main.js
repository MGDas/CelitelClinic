var doctorPageShare = document.querySelector('.doctorPage__share button')

if(doctorPageShare){
	doctorPageShare.addEventListener('click', (event) => {
		event.currentTarget.nextElementSibling.classList.toggle('doctorPage__shareList--open')
	})
}

var faqQuestion = document.querySelectorAll('.faq__question')

if(faqQuestion.length){
	faqQuestion.forEach((link) => {
		link.addEventListener('click', (event) => {
			event.preventDefault()
			event.currentTarget.closest('.faq__item').classList.toggle('faq__item--open')
		})
	})
}

var faqBtn = document.querySelector('.faq__btn')
var faqModal = document.querySelector('.orderModal--addFaq')

if(faqBtn){
	faqBtn.addEventListener('click', (event) => {
		event.preventDefault()
		faqModal.classList.add('orderModal--view')
	})
}

var menuServicesTabs = document.querySelectorAll('.mainMenu__tabs--services a')

if(menuServicesTabs.length){
	menuServicesTabs.forEach((item) => {
		item.addEventListener('click', (event) => {
			event.preventDefault()
			document.querySelector('.mainMenu__tabs--services .mainMenu__activeTab').classList.remove('mainMenu__activeTab')
			event.currentTarget.parentNode.classList.add('mainMenu__activeTab')
			document.querySelector('.menuServices__section--active').classList.remove('menuServices__section--active')
			document.querySelector(`.menuServices__section[data-tab="${item.dataset.tab}"]`).classList.add('menuServices__section--active')
		})
	})
}

var menuClinicsTabs = document.querySelectorAll('.mainMenu__tabs--clinics a')

if(menuClinicsTabs.length){
	menuClinicsTabs.forEach((item) => {
		item.addEventListener('click', (event) => {
			event.preventDefault()
			document.querySelector('.mainMenu__tabs--clinics .mainMenu__activeTab').classList.remove('mainMenu__activeTab')
			event.currentTarget.parentNode.classList.add('mainMenu__activeTab')
			document.querySelector('.menuClinics__section--active').classList.remove('menuClinics__section--active')
			document.querySelector(`.menuClinics__section[data-tab="${item.dataset.tab}"]`).classList.add('menuClinics__section--active')
		})
	})
}

var mainMenuLinks = document.querySelectorAll('.mainMenu__link')

if(mainMenuLinks.length){
	mainMenuLinks.forEach((link) => {
		link.addEventListener('click', (event) => {
			event.preventDefault()
		})
	})
}

var subscribeForm = document.querySelector('#subscribeForm')

function subscribe(fileName, form) {
	var XHR = new XMLHttpRequest();
	var FD = new FormData(form);
	XHR.addEventListener("load", function(event) {
		console.log(this.responseText)
		if(JSON.parse(this.responseText).response == "1"){
			form.querySelector('button[type="submit"]').innerHTML = "Подписка оформлена"
		}
	});
	XHR.addEventListener("error", function(event) {
		alert('Ошибка!');
	});
	XHR.open("POST", fileName);
	XHR.send(FD);
}

if(subscribeForm){
	subscribeForm.addEventListener('submit', () => {
		event.preventDefault()
		subscribe(subscribeForm.getAttribute('action'), subscribeForm)
	})
}

document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
    var makeAnAppointmentInputs = document.querySelectorAll('.makeAnAppointment__input ')
    
    if(makeAnAppointmentInputs){
    	makeAnAppointmentInputs.forEach((input) => {
    		input.addEventListener('change', (evt) => {
    			document.querySelector('.makeAnAppointment__wrapper--active').classList.remove('makeAnAppointment__wrapper--active')
    			document.querySelector(`.makeAnAppointment__wrapper[data-address="${evt.currentTarget.dataset.address}"]`).classList.add('makeAnAppointment__wrapper--active')
    		})
    	});
    }
    
    var makeAnAppointmentDateInputs = document.querySelectorAll('.makeAnAppointment__dateInput')
    
    if(makeAnAppointmentDateInputs){
    	makeAnAppointmentDateInputs.forEach((input) => {
    		input.addEventListener('change', (evt) => {
    			evt.currentTarget.parentNode.parentNode.querySelector('.makeAnAppointment__day--active').classList.remove('makeAnAppointment__day--active')
    			evt.currentTarget.parentNode.parentNode.querySelector(`.makeAnAppointment__day[data-appointmentday='${evt.currentTarget.dataset.appointmentdate}']`).classList.add('makeAnAppointment__day--active')
    		})
    	});
    }
    
    var makeAnAppointmentHoursInputs = document.querySelectorAll('.makeAnAppointment__hoursInput')
    
    if(makeAnAppointmentHoursInputs.length){
    	var orderModal1 = document.querySelector('.orderModal--step1');
    	var orderModalSuccess = document.querySelector('.orderModal--success');
    
    	makeAnAppointmentHoursInputs.forEach((input) => {
    		input.addEventListener('click', (evt) => {
    			var temp = evt.currentTarget.parentNode.parentNode.querySelector('.makeAnAppointment__time--selected');
    			if(temp){
    				temp.classList.remove('makeAnAppointment__time--selected')
    			}
    			evt.currentTarget.nextElementSibling.classList.add('makeAnAppointment__time--selected')
    
    			orderModal1.querySelector('#orderModalAddress').value = document.querySelector('.makeAnAppointment__input:checked').getAttribute('value')
    			orderModal1.querySelector('#orderModalTime').value = document.querySelector('.makeAnAppointment__hoursInput:checked').getAttribute('value').split(" ")[0].split("T")[1]
    
    			var tempForm = event.currentTarget.closest(".makeAnAppointment");
    			orderModal1.classList.add('orderModal--view')
    		})
    	});
    
    	var orderModalClose = document.querySelectorAll('.orderModal__close')
    
    	if(orderModalClose){
    		orderModalClose.forEach((btn) => {
    			btn.addEventListener('click', () => {
    				document.querySelector('.orderModal--view').classList.remove('orderModal--view')
    			})
    		});
    	}
    
    	var orderModalPay = document.querySelector('#orderModalPay')
    	var orderModalNoPay = document.querySelector('#orderModalNoPay')

function sendDataAppointment(fileName, form) {
	var XHR = new XMLHttpRequest();
	var FD = new FormData(form);
	XHR.addEventListener("load", function(event) {
        var responseServer = JSON.parse(this.responseText);
        
        try{
            if(!responseServer["Services"].length){
                console.error("Ошибка: ", responseServer)
                alert("Ошибка")
            } else {
                if(responseServer["Services"][0]["Status"] == "Подтверждена"){
                    console.log("Записан")
            		orderModalSuccess.classList.add('orderModal--view')
                } else if(responseServer["Services"][0]["Status"] == "Время занято"){
                    console.log("Время занято")
                    alert("Время занято. Пожалуйста, выберите другое время")                
                } else {
                    console.error("Ошибка!")
                    alert("Ошибка")
                }
            }
        }
        catch (e) {
            alert("Ошибка!")
            console.error("Ошибка: ", e)
        }


	});
	XHR.addEventListener("error", function(event) {
		alert('Ошибка!');
	});
	XHR.open("POST", fileName);
	XHR.send(FD);
}

    	function checkModalPaymentFields(action, form){
    		if(orderModalName.value.split(" ").length < 3 || !orderModalPhone.value || !orderModalBirthday.value){
    			if(orderModalName.value.split(" ").length < 3){
    				orderModalName.classList.add('error')
    			} else {
    				orderModalName.classList.remove('error')
    			}
    			if(!orderModalPhone.value){
    				orderModalPhone.classList.add('error')
    			} else {
    				orderModalPhone.classList.remove('error')
    			}
    			if(!orderModalBirthday.value){
    				orderModalBirthday.classList.add('error')
    			} else {
    				orderModalBirthday.classList.remove('error')
    			}
    		} else {
    			orderModal1.classList.remove('orderModal--view')
    			sendDataAppointment(action, form)
    		}
    	}
    
    	orderModalNoPay.addEventListener('click', () => {
    		var form = document.querySelector('.makeAnAppointment');
    		checkModalPaymentFields(form.getAttribute('data-action'), form)
    	})
    
    	orderModalPay.addEventListener('click', () => {
    		var form = document.querySelector('.makeAnAppointment');
    		checkModalPaymentFields(form.getAttribute('action'), form)
    	})
    }
    }, 1000)
})

var addFaqForm = document.querySelector('.orderModal--addFaq form')
var orderModalSuccess = document.querySelector('.orderModal--success');

if(addFaqForm){
	addFaqForm.addEventListener('submit', () => {
		event.preventDefault()
		sendData(addFaqForm.getAttribute('action'), addFaqForm)
	})

}

var addReviewForm = document.querySelector('.orderModal--addReview form')
var orderModalSuccess = document.querySelector('.orderModal--success');

if(addReviewForm){
	addReviewForm.addEventListener('submit', () => {
		event.preventDefault()
		sendData(addReviewForm.getAttribute('action'), addReviewForm)
	})

}

var orderFiltersSpecialization = document.getElementById("orderFiltersSpecialization");

if(orderFiltersSpecialization){
	var specializationLabels = document.querySelectorAll(".orderFilters__item--specialization label");

	specializationLabels.forEach((label) => {
		label.addEventListener('change', (evt) => {
			orderFiltersSpecialization.value = evt.currentTarget.querySelector('input').value
		})
	})

	function filterSpecialization() {
		var filter = orderFiltersSpecialization.value.toUpperCase();

		for (var i = 0; i < specializationLabels.length; i++) {
			var txtValue = specializationLabels[i].textContent || specializationLabels[i].innerText;
			if (txtValue.toUpperCase().indexOf(filter) > -1) {
				specializationLabels[i].style.display = "";
			} else {
				specializationLabels[i].style.display = "none";
			}
		}
	}
	orderFiltersSpecialization.addEventListener('keyup', filterSpecialization)
}

var orderFiltersAddress = document.getElementById("orderFiltersAddress");

if(orderFiltersAddress){
	var addressLabels = document.querySelectorAll(".orderFilters__item--address label");

	addressLabels.forEach((label) => {
		label.addEventListener('change', (evt) => {
			orderFiltersAddress.value = evt.currentTarget.querySelector('input').value
		})
	})

	function filterSpecialization() {
		var filter = orderFiltersAddress.value.toUpperCase();

		for (var i = 0; i < addressLabels.length; i++) {
			var txtValue = addressLabels[i].textContent || addressLabels[i].innerText;
			if (txtValue.toUpperCase().indexOf(filter) > -1) {
				addressLabels[i].style.display = "";
			} else {
				addressLabels[i].style.display = "none";
			}
		}
	}
	orderFiltersAddress.addEventListener('keyup', filterSpecialization)
}

var orderFiltersCheckers = document.querySelectorAll('.orderFilters__checker')

if(orderFiltersCheckers.length){
	orderFiltersCheckers.forEach((button) => {
		button.addEventListener('click', () => {
			button.nextElementSibling.focus()
		})
	})
}

var orderFiltersInputsPopup = document.querySelectorAll('.orderFilters__input--popup');

if(orderFiltersInputsPopup.length){
	orderFiltersInputsPopup.forEach((input) => {
		input.addEventListener('focus', () => {
			document.body.classList.add('noScroll-mobile')
			input.closest('.orderFilters__wrap').classList.add('orderFilters__wrap--active')
			input.closest('.orderFilters__item').classList.add('orderFilters__item--active')
			input.parentNode.querySelector('.orderFilters__dropDown').classList.add('orderFilters__dropDown--active')
		})
		input.addEventListener('blur', () => {
			setTimeout(() => {
				document.body.classList.remove('noScroll-mobile')
				input.closest('.orderFilters__wrap').classList.remove('orderFilters__wrap--active')
				input.closest('.orderFilters__item').classList.remove('orderFilters__item--active')
				input.parentNode.querySelector('.orderFilters__dropDown').classList.remove('orderFilters__dropDown--active')
			}, 100)
		})
	})
}

var orderFiltersShowFields = document.querySelector('.orderFilters__showFields')

if(orderFiltersShowFields){

	var orderFiltersInputName = document.querySelector('.orderFilters__input--name')

	if(orderFiltersInputName){
		orderFiltersInputName.addEventListener('focus', () => {
			orderFiltersInputName.closest('.orderFilters').classList.add('orderFilters--on')
			orderFiltersShowFields.classList.add('orderFilters__showFields--active')
			orderFiltersInputName.closest('.orderFilters__wrap').classList.add('orderFilters__wrap--on')
			orderFiltersShowFields.parentNode.querySelector('.orderFilters__dropDown').classList.add('orderFilters__dropDown--on')
		})

		orderFiltersInputName.addEventListener('blur', () => {
			setTimeout(() => {
				if(!document.activeElement.closest('.orderFilters')){
					orderFiltersInputName.closest('.orderFilters').classList.remove('orderFilters--on')
					orderFiltersShowFields.classList.remove('orderFilters__showFields--active')
					orderFiltersInputName.closest('.orderFilters__wrap').classList.remove('orderFilters__wrap--on')
					orderFiltersShowFields.parentNode.querySelector('.orderFilters__dropDown').classList.remove('orderFilters__dropDown--on')
				}
			}, 100)
		})
	}

	orderFiltersShowFields.addEventListener('click', () => {
		orderFiltersShowFields.closest('.orderFilters').classList.toggle('orderFilters--on')
		orderFiltersShowFields.classList.toggle('orderFilters__showFields--active')
		orderFiltersInputName.closest('.orderFilters__wrap').classList.toggle('orderFilters__wrap--on')
		orderFiltersShowFields.parentNode.querySelector('.orderFilters__dropDown').classList.toggle('orderFilters__dropDown--on')
	})
}

var orderFiltersCheckboxDesktop = document.querySelectorAll('.orderFilters__input--checkbox')

if(orderFiltersCheckboxDesktop.length){
	orderFiltersCheckboxDesktop.forEach((checkbox) => {
		checkbox.addEventListener('change', () => {
			if(checkbox.checked){
				checkbox.closest('.orderFilters').classList.add('orderFilters--enabled')
			} else {
				checkbox.closest('.orderFilters').classList.remove('orderFilters--enabled')
			}
		})
	})
}

//.orderPage scripts goes here

var currentPartnersSlider;

window.addEventListener("resize", () => {
	if(window.innerWidth >= 1024){
		activateFrontClinicSLiders(document.querySelector('.partners__list'))
	} else {
		if(currentPartnersSlider){
			currentPartnersSlider.destroy()
		}
	}
});

window.addEventListener("DOMContentLoaded", () => {
	if(window.innerWidth >= 1024){
		activateFrontClinicSLiders(document.querySelector('.partners__list'))
	}
});


function activateFrontClinicSLiders(element){
	currentPartnersSlider = new Flickity( element, {
		// options
		cellAlign: 'left',
		contain: true,
		pageDots: false,
		arrowShape: 'M 10,50 L 60,100 L 70,90 L 30,50  L 70,10 L 60,0 Z',
		groupCells: 4
	});
}

var placeLooksLikePhoto = document.querySelector('.placeLooksLike__item--photo')
var placeLooksLikePano = document.querySelector('.placeLooksLike__item--pano')
var placeLooksLikeMap = document.querySelector('.placeLooksLike__item--map')

var placeLooksLikeControlPhoto = document.querySelector('.placeLooksLike__control--photo')
var placeLooksLikeControlPano = document.querySelector('.placeLooksLike__control--pano')
var placeLooksLikeControlMap = document.querySelector('.placeLooksLike__control--map')

if(placeLooksLikeControlPhoto){
	placeLooksLikeControlPhoto.addEventListener('click', () => {
		document.querySelector('.placeLooksLike__control--active').classList.remove('placeLooksLike__control--active')
		event.currentTarget.classList.add('placeLooksLike__control--active')
		document.querySelector('.placeLooksLike__item--active').classList.remove('placeLooksLike__item--active')
		placeLooksLikePhoto.classList.add('placeLooksLike__item--active')
	})
}
if(placeLooksLikeControlPano){
	var placeLooksLikePanoIframe = placeLooksLikePano.querySelector('iframe')
	placeLooksLikeControlPano.addEventListener('click', () => {
		document.querySelector('.placeLooksLike__control--active').classList.remove('placeLooksLike__control--active')
		event.currentTarget.classList.add('placeLooksLike__control--active')
		document.querySelector('.placeLooksLike__item--active').classList.remove('placeLooksLike__item--active')
		placeLooksLikePano.classList.add('placeLooksLike__item--active')
		if(!placeLooksLikePanoIframe.getAttribute('src')){
			placeLooksLikePanoIframe.setAttribute('src', placeLooksLikePano.dataset.src)
		}
	})
}
if(placeLooksLikeControlMap){
	var placeLooksLikeMapIframe = placeLooksLikeMap.querySelector('iframe')
	placeLooksLikeControlMap.addEventListener('click', () => {
		document.querySelector('.placeLooksLike__control--active').classList.remove('placeLooksLike__control--active')
		event.currentTarget.classList.add('placeLooksLike__control--active')
		document.querySelector('.placeLooksLike__item--active').classList.remove('placeLooksLike__item--active')
		placeLooksLikeMap.classList.add('placeLooksLike__item--active')
		if(!placeLooksLikeMapIframe.getAttribute('src')){
			placeLooksLikeMapIframe.setAttribute('src', placeLooksLikeMap.dataset.src)
		}
	})
}

var reviewsBtn = document.querySelector('.reviews__btn')
var reviewModal = document.querySelector('.orderModal--addReview')

if(reviewsBtn){
	reviewsBtn.addEventListener('click', (event) => {
		event.preventDefault()
		reviewModal.classList.add('orderModal--view')
	})
}

window.addEventListener("resize", () => {
	if(window.innerWidth >= 720){
		setTimeout(() => {
			var sliderHeight = document.querySelector('.slider__item').offsetHeight + 'px'
			document.querySelector('.slider__list').style.height = sliderHeight
		}, 50)
			if(!document.querySelector('.slider__list').classList.contains('mainSlider')){
			document.querySelector('.slider__list').classList.add('mainSlider')
		}
	} else {
		if(mainSlider){
			document.querySelector('.slider__list').classList.remove('mainSlider')
			document.querySelector('.slider__list').removeAttribute('style')
		}
	}
})

window.addEventListener("DOMContentLoaded", () => {
	if(window.innerWidth >= 720){
		document.querySelector('.slider__list').classList.add('mainSlider')
		setTimeout(() => {
			var sliderHeight = document.querySelector('.slider__item').offsetHeight + 'px'
			document.querySelector('.slider__list').style.height = sliderHeight
		}, 50)
	}
})

var sliderPrevButton = document.querySelector('.slider__btn--prev')
var sliderNextButton = document.querySelector('.slider__btn--next')

if(sliderPrevButton && sliderNextButton){
	var mainSlider = document.querySelector('.slider__list');

	sliderPrevButton.addEventListener('click', () => {
		document.querySelector('.slider__item--active').classList.remove('slider__item--active')

		if(document.querySelector('.slider__dots .active').previousElementSibling){
			document.querySelector('.slider__dots .active').previousElementSibling.classList.add('active')
			document.querySelector('.slider__dots .active').nextElementSibling.classList.remove('active')
		} else {
			document.querySelector('.slider__dots span').classList.remove('active')
			document.querySelector('.slider__dots span:last-of-type').classList.add('active')
		}

		mainSlider.prepend(document.querySelector('.slider__item:last-of-type'))
		document.querySelector('.slider__item').classList.add('slider__item--out')
		document.querySelector('.slider__item').classList.add('slider__item--active')
		setTimeout(() => {
			document.querySelector('.slider__item--out').classList.remove('slider__item--out')
		}, 300)
	})

	sliderNextButton.addEventListener('click', () => {
		document.querySelector('.slider__item--active').classList.add('slider__item--out')

		if(document.querySelector('.slider__dots .active').nextElementSibling){
			document.querySelector('.slider__dots .active').nextElementSibling.classList.add('active')
			document.querySelector('.slider__dots .active').classList.remove('active')
		} else {
			document.querySelector('.slider__dots span').classList.add('active')
			document.querySelector('.slider__dots span:last-of-type').classList.remove('active')
		}

		setTimeout(() => {
			mainSlider.append(document.querySelector('.slider__item--active'))
			document.querySelector('.slider__item--active').classList.remove('slider__item--active')
			document.querySelector('.slider__item--out').classList.remove('slider__item--out')
			document.querySelector('.slider__item').classList.add('slider__item--active')
		}, 300)
	})
}

//.statistics scripts goes here

var vacancies = document.querySelectorAll('.vacancies__title a')

if(vacancies.length){
	vacancies.forEach((item) => {
		item.addEventListener('click', (event) => {
			event.preventDefault()
			event.currentTarget.closest('.vacancies__item').classList.toggle('vacancies__item--active')
		})
	})
}

function sendData(fileName, form) {
	var XHR = new XMLHttpRequest();
	var FD = new FormData(form);
	XHR.addEventListener("load", function(event) {
		console.log(this.responseText)
		if(JSON.parse(this.responseText).response == "1"){
			orderModalSuccess.classList.add('orderModal--view')
		}
	});
	XHR.addEventListener("error", function(event) {
		alert('Ошибка!');
	});
	XHR.open("POST", fileName);
	XHR.send(FD);
}

var frontClinicsTabs = document.querySelectorAll('.mdWrap--frontClinics a')
var currentClinicSlider;

if(frontClinicsTabs.length){
	frontClinicsTabs.forEach((link) => {
		link.addEventListener('click', (event) => {
			event.preventDefault()
			event.currentTarget.closest('.mdWrap__links').querySelector('.mdWrap__link--active').classList.remove('mdWrap__link--active')
			event.currentTarget.closest('.mdWrap__link').classList.add('mdWrap__link--active')
			document.querySelector('.clinicsMD__body--active').classList.remove('clinicsMD__body--active')
			var targetBody = event.currentTarget.closest('.clinicsMD').querySelector(`.clinicsMD__body[data-city=${event.currentTarget.dataset.city}]`)
			targetBody.classList.add('clinicsMD__body--active')

			if(window.innerWidth >= 1200){
				if(currentClinicSlider){
					currentClinicSlider.destroy()
				}
				activateFrontClinicSLiders(targetBody)
			}
		})
	})
}

window.addEventListener("resize", () => {
	if(window.innerWidth >= 1200){
		activateFrontClinicSLiders(document.querySelector('.clinicsMD__body--active'))
	} else {
		if(currentClinicSlider){
			currentClinicSlider.destroy()
		}
	}
});

window.addEventListener("DOMContentLoaded", () => {
	if(window.innerWidth >= 1200){
		activateFrontClinicSLiders(document.querySelector('.clinicsMD__body--active'))
	}
});


function activateFrontClinicSLiders(element){
	currentClinicSlider = new Flickity( element, {
		// options
		cellAlign: 'left',
		contain: true,
		pageDots: false,
		arrowShape: 'M 10,50 L 60,100 L 70,90 L 30,50  L 70,10 L 60,0 Z',
		groupCells: 5
	});
}
