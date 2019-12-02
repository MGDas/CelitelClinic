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
    			orderModal1.querySelector('#orderModalTime').value = document.querySelector('.makeAnAppointment__hoursInput:checked').getAttribute('value')
    
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
    
    	function checkModalPaymentFields(action, form){
    		if(!orderModalName.value || !orderModalPhone.value){
    			if(!orderModalName.value){
    				orderModalName.classList.add('error')
    			} else {
    				orderModalName.classList.remove('error')
    			}
    			if(!orderModalPhone.value){
    				orderModalPhone.classList.add('error')
    			} else {
    				orderModalPhone.classList.remove('error')
    			}
    		} else {
    			orderModal1.classList.remove('orderModal--view')
    			sendData(action, form)
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

//# sourceMappingURL=data:application/json;charset=utf8;base64,eyJ2ZXJzaW9uIjozLCJzb3VyY2VzIjpbImRvY3RvclBhZ2UvZG9jdG9yUGFnZS5qcyIsImZhcS9mYXEuanMiLCJoZWFkZXIvaGVhZGVyLmpzIiwiaW5mb0Jsb2Nrcy9pbmZvQmxvY2tzLmpzIiwibWFrZUFuQXBwb2ludG1lbnQvbWFrZUFuQXBwb2ludG1lbnQuanMiLCJtb2RhbEZhcS9tb2RhbEZhcS5qcyIsIm1vZGFsUmV2aWV3L21vZGFsUmV2aWV3LmpzIiwib3JkZXJGaWx0ZXJzL29yZGVyRmlsdGVycy5qcyIsIm9yZGVyUGFnZS9vcmRlclBhZ2UuanMiLCJwYXJ0bmVycy9wYXJ0bmVycy5qcyIsInBsYWNlTG9va3NMaWtlL3BsYWNlTG9va3NMaWtlLmpzIiwicmV2aWV3cy9yZXZpZXdzLmpzIiwic2xpZGVyL3NsaWRlci5qcyIsInN0YXRpc3RpY3Mvc3RhdGlzdGljcy5qcyIsInZhY2FuY2llcy92YWNhbmNpZXMuanMiLCJjb21tb24uanMiXSwibmFtZXMiOltdLCJtYXBwaW5ncyI6IkFBQUE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQ1BBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQ3BCQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FDckNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FDeEJBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQ3pGQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FDVkE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQ1ZBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUNsSUE7QUFDQTtBQ0RBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQzdCQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FDeENBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FDVEE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FDdkVBO0FBQ0E7QUNEQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FDVkE7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0E7QUFDQTtBQUNBO0FBQ0EiLCJmaWxlIjoibWFpbi5qcyIsInNvdXJjZXNDb250ZW50IjpbInZhciBkb2N0b3JQYWdlU2hhcmUgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcuZG9jdG9yUGFnZV9fc2hhcmUgYnV0dG9uJylcblxuaWYoZG9jdG9yUGFnZVNoYXJlKXtcblx0ZG9jdG9yUGFnZVNoYXJlLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgKGV2ZW50KSA9PiB7XG5cdFx0ZXZlbnQuY3VycmVudFRhcmdldC5uZXh0RWxlbWVudFNpYmxpbmcuY2xhc3NMaXN0LnRvZ2dsZSgnZG9jdG9yUGFnZV9fc2hhcmVMaXN0LS1vcGVuJylcblx0fSlcbn1cbiIsInZhciBmYXFRdWVzdGlvbiA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJy5mYXFfX3F1ZXN0aW9uJylcblxuaWYoZmFxUXVlc3Rpb24ubGVuZ3RoKXtcblx0ZmFxUXVlc3Rpb24uZm9yRWFjaCgobGluaykgPT4ge1xuXHRcdGxpbmsuYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCAoZXZlbnQpID0+IHtcblx0XHRcdGV2ZW50LnByZXZlbnREZWZhdWx0KClcblx0XHRcdGV2ZW50LmN1cnJlbnRUYXJnZXQuY2xvc2VzdCgnLmZhcV9faXRlbScpLmNsYXNzTGlzdC50b2dnbGUoJ2ZhcV9faXRlbS0tb3BlbicpXG5cdFx0fSlcblx0fSlcbn1cblxudmFyIGZhcUJ0biA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5mYXFfX2J0bicpXG52YXIgZmFxTW9kYWwgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcub3JkZXJNb2RhbC0tYWRkRmFxJylcblxuaWYoZmFxQnRuKXtcblx0ZmFxQnRuLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgKGV2ZW50KSA9PiB7XG5cdFx0ZXZlbnQucHJldmVudERlZmF1bHQoKVxuXHRcdGZhcU1vZGFsLmNsYXNzTGlzdC5hZGQoJ29yZGVyTW9kYWwtLXZpZXcnKVxuXHR9KVxufVxuIiwidmFyIG1lbnVTZXJ2aWNlc1RhYnMgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcubWFpbk1lbnVfX3RhYnMtLXNlcnZpY2VzIGEnKVxuXG5pZihtZW51U2VydmljZXNUYWJzLmxlbmd0aCl7XG5cdG1lbnVTZXJ2aWNlc1RhYnMuZm9yRWFjaCgoaXRlbSkgPT4ge1xuXHRcdGl0ZW0uYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCAoZXZlbnQpID0+IHtcblx0XHRcdGV2ZW50LnByZXZlbnREZWZhdWx0KClcblx0XHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5tYWluTWVudV9fdGFicy0tc2VydmljZXMgLm1haW5NZW51X19hY3RpdmVUYWInKS5jbGFzc0xpc3QucmVtb3ZlKCdtYWluTWVudV9fYWN0aXZlVGFiJylcblx0XHRcdGV2ZW50LmN1cnJlbnRUYXJnZXQucGFyZW50Tm9kZS5jbGFzc0xpc3QuYWRkKCdtYWluTWVudV9fYWN0aXZlVGFiJylcblx0XHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5tZW51U2VydmljZXNfX3NlY3Rpb24tLWFjdGl2ZScpLmNsYXNzTGlzdC5yZW1vdmUoJ21lbnVTZXJ2aWNlc19fc2VjdGlvbi0tYWN0aXZlJylcblx0XHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoYC5tZW51U2VydmljZXNfX3NlY3Rpb25bZGF0YS10YWI9XCIke2l0ZW0uZGF0YXNldC50YWJ9XCJdYCkuY2xhc3NMaXN0LmFkZCgnbWVudVNlcnZpY2VzX19zZWN0aW9uLS1hY3RpdmUnKVxuXHRcdH0pXG5cdH0pXG59XG5cbnZhciBtZW51Q2xpbmljc1RhYnMgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcubWFpbk1lbnVfX3RhYnMtLWNsaW5pY3MgYScpXG5cbmlmKG1lbnVDbGluaWNzVGFicy5sZW5ndGgpe1xuXHRtZW51Q2xpbmljc1RhYnMuZm9yRWFjaCgoaXRlbSkgPT4ge1xuXHRcdGl0ZW0uYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCAoZXZlbnQpID0+IHtcblx0XHRcdGV2ZW50LnByZXZlbnREZWZhdWx0KClcblx0XHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5tYWluTWVudV9fdGFicy0tY2xpbmljcyAubWFpbk1lbnVfX2FjdGl2ZVRhYicpLmNsYXNzTGlzdC5yZW1vdmUoJ21haW5NZW51X19hY3RpdmVUYWInKVxuXHRcdFx0ZXZlbnQuY3VycmVudFRhcmdldC5wYXJlbnROb2RlLmNsYXNzTGlzdC5hZGQoJ21haW5NZW51X19hY3RpdmVUYWInKVxuXHRcdFx0ZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLm1lbnVDbGluaWNzX19zZWN0aW9uLS1hY3RpdmUnKS5jbGFzc0xpc3QucmVtb3ZlKCdtZW51Q2xpbmljc19fc2VjdGlvbi0tYWN0aXZlJylcblx0XHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoYC5tZW51Q2xpbmljc19fc2VjdGlvbltkYXRhLXRhYj1cIiR7aXRlbS5kYXRhc2V0LnRhYn1cIl1gKS5jbGFzc0xpc3QuYWRkKCdtZW51Q2xpbmljc19fc2VjdGlvbi0tYWN0aXZlJylcblx0XHR9KVxuXHR9KVxufVxuXG52YXIgbWFpbk1lbnVMaW5rcyA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJy5tYWluTWVudV9fbGluaycpXG5cbmlmKG1haW5NZW51TGlua3MubGVuZ3RoKXtcblx0bWFpbk1lbnVMaW5rcy5mb3JFYWNoKChsaW5rKSA9PiB7XG5cdFx0bGluay5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIChldmVudCkgPT4ge1xuXHRcdFx0ZXZlbnQucHJldmVudERlZmF1bHQoKVxuXHRcdH0pXG5cdH0pXG59XG4iLCJ2YXIgc3Vic2NyaWJlRm9ybSA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJyNzdWJzY3JpYmVGb3JtJylcblxuZnVuY3Rpb24gc3Vic2NyaWJlKGZpbGVOYW1lLCBmb3JtKSB7XG5cdHZhciBYSFIgPSBuZXcgWE1MSHR0cFJlcXVlc3QoKTtcblx0dmFyIEZEID0gbmV3IEZvcm1EYXRhKGZvcm0pO1xuXHRYSFIuYWRkRXZlbnRMaXN0ZW5lcihcImxvYWRcIiwgZnVuY3Rpb24oZXZlbnQpIHtcblx0XHRjb25zb2xlLmxvZyh0aGlzLnJlc3BvbnNlVGV4dClcblx0XHRpZihKU09OLnBhcnNlKHRoaXMucmVzcG9uc2VUZXh0KS5yZXNwb25zZSA9PSBcIjFcIil7XG5cdFx0XHRmb3JtLnF1ZXJ5U2VsZWN0b3IoJ2J1dHRvblt0eXBlPVwic3VibWl0XCJdJykuaW5uZXJIVE1MID0gXCLQn9C+0LTQv9C40YHQutCwINC+0YTQvtGA0LzQu9C10L3QsFwiXG5cdFx0fVxuXHR9KTtcblx0WEhSLmFkZEV2ZW50TGlzdGVuZXIoXCJlcnJvclwiLCBmdW5jdGlvbihldmVudCkge1xuXHRcdGFsZXJ0KCfQntGI0LjQsdC60LAhJyk7XG5cdH0pO1xuXHRYSFIub3BlbihcIlBPU1RcIiwgZmlsZU5hbWUpO1xuXHRYSFIuc2VuZChGRCk7XG59XG5cbmlmKHN1YnNjcmliZUZvcm0pe1xuXHRzdWJzY3JpYmVGb3JtLmFkZEV2ZW50TGlzdGVuZXIoJ3N1Ym1pdCcsICgpID0+IHtcblx0XHRldmVudC5wcmV2ZW50RGVmYXVsdCgpXG5cdFx0c3Vic2NyaWJlKHN1YnNjcmliZUZvcm0uZ2V0QXR0cmlidXRlKCdhY3Rpb24nKSwgc3Vic2NyaWJlRm9ybSlcblx0fSlcbn1cbiIsInZhciBtYWtlQW5BcHBvaW50bWVudElucHV0cyA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJy5tYWtlQW5BcHBvaW50bWVudF9faW5wdXQgJylcblxuaWYobWFrZUFuQXBwb2ludG1lbnRJbnB1dHMpe1xuXHRtYWtlQW5BcHBvaW50bWVudElucHV0cy5mb3JFYWNoKChpbnB1dCkgPT4ge1xuXHRcdGlucHV0LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChldnQpID0+IHtcblx0XHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5tYWtlQW5BcHBvaW50bWVudF9fd3JhcHBlci0tYWN0aXZlJykuY2xhc3NMaXN0LnJlbW92ZSgnbWFrZUFuQXBwb2ludG1lbnRfX3dyYXBwZXItLWFjdGl2ZScpXG5cdFx0XHRkb2N1bWVudC5xdWVyeVNlbGVjdG9yKGAubWFrZUFuQXBwb2ludG1lbnRfX3dyYXBwZXJbZGF0YS1hZGRyZXNzPVwiJHtldnQuY3VycmVudFRhcmdldC5kYXRhc2V0LmFkZHJlc3N9XCJdYCkuY2xhc3NMaXN0LmFkZCgnbWFrZUFuQXBwb2ludG1lbnRfX3dyYXBwZXItLWFjdGl2ZScpXG5cdFx0fSlcblx0fSk7XG59XG5cbnZhciBtYWtlQW5BcHBvaW50bWVudERhdGVJbnB1dHMgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcubWFrZUFuQXBwb2ludG1lbnRfX2RhdGVJbnB1dCcpXG5cbmlmKG1ha2VBbkFwcG9pbnRtZW50RGF0ZUlucHV0cyl7XG5cdG1ha2VBbkFwcG9pbnRtZW50RGF0ZUlucHV0cy5mb3JFYWNoKChpbnB1dCkgPT4ge1xuXHRcdGlucHV0LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChldnQpID0+IHtcblx0XHRcdGV2dC5jdXJyZW50VGFyZ2V0LnBhcmVudE5vZGUucGFyZW50Tm9kZS5xdWVyeVNlbGVjdG9yKCcubWFrZUFuQXBwb2ludG1lbnRfX2RheS0tYWN0aXZlJykuY2xhc3NMaXN0LnJlbW92ZSgnbWFrZUFuQXBwb2ludG1lbnRfX2RheS0tYWN0aXZlJylcblx0XHRcdGV2dC5jdXJyZW50VGFyZ2V0LnBhcmVudE5vZGUucGFyZW50Tm9kZS5xdWVyeVNlbGVjdG9yKGAubWFrZUFuQXBwb2ludG1lbnRfX2RheVtkYXRhLWFwcG9pbnRtZW50ZGF5PScke2V2dC5jdXJyZW50VGFyZ2V0LmRhdGFzZXQuYXBwb2ludG1lbnRkYXRlfSddYCkuY2xhc3NMaXN0LmFkZCgnbWFrZUFuQXBwb2ludG1lbnRfX2RheS0tYWN0aXZlJylcblx0XHR9KVxuXHR9KTtcbn1cblxudmFyIG1ha2VBbkFwcG9pbnRtZW50SG91cnNJbnB1dHMgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcubWFrZUFuQXBwb2ludG1lbnRfX2hvdXJzSW5wdXQnKVxuXG5pZihtYWtlQW5BcHBvaW50bWVudEhvdXJzSW5wdXRzLmxlbmd0aCl7XG5cdHZhciBvcmRlck1vZGFsMSA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5vcmRlck1vZGFsLS1zdGVwMScpO1xuXHR2YXIgb3JkZXJNb2RhbFN1Y2Nlc3MgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcub3JkZXJNb2RhbC0tc3VjY2VzcycpO1xuXG5cdG1ha2VBbkFwcG9pbnRtZW50SG91cnNJbnB1dHMuZm9yRWFjaCgoaW5wdXQpID0+IHtcblx0XHRpbnB1dC5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIChldnQpID0+IHtcblx0XHRcdHZhciB0ZW1wID0gZXZ0LmN1cnJlbnRUYXJnZXQucGFyZW50Tm9kZS5wYXJlbnROb2RlLnF1ZXJ5U2VsZWN0b3IoJy5tYWtlQW5BcHBvaW50bWVudF9fdGltZS0tc2VsZWN0ZWQnKTtcblx0XHRcdGlmKHRlbXApe1xuXHRcdFx0XHR0ZW1wLmNsYXNzTGlzdC5yZW1vdmUoJ21ha2VBbkFwcG9pbnRtZW50X190aW1lLS1zZWxlY3RlZCcpXG5cdFx0XHR9XG5cdFx0XHRldnQuY3VycmVudFRhcmdldC5uZXh0RWxlbWVudFNpYmxpbmcuY2xhc3NMaXN0LmFkZCgnbWFrZUFuQXBwb2ludG1lbnRfX3RpbWUtLXNlbGVjdGVkJylcblxuXHRcdFx0b3JkZXJNb2RhbDEucXVlcnlTZWxlY3RvcignI29yZGVyTW9kYWxBZGRyZXNzJykudmFsdWUgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcubWFrZUFuQXBwb2ludG1lbnRfX2lucHV0OmNoZWNrZWQnKS5nZXRBdHRyaWJ1dGUoJ3ZhbHVlJylcblx0XHRcdG9yZGVyTW9kYWwxLnF1ZXJ5U2VsZWN0b3IoJyNvcmRlck1vZGFsVGltZScpLnZhbHVlID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLm1ha2VBbkFwcG9pbnRtZW50X19ob3Vyc0lucHV0OmNoZWNrZWQnKS5nZXRBdHRyaWJ1dGUoJ3ZhbHVlJylcblxuXHRcdFx0dmFyIHRlbXBGb3JtID0gZXZlbnQuY3VycmVudFRhcmdldC5jbG9zZXN0KFwiLm1ha2VBbkFwcG9pbnRtZW50XCIpO1xuXHRcdFx0b3JkZXJNb2RhbDEucXVlcnlTZWxlY3RvcignLm9yZGVyTW9kYWxfX25hbWUnKS5pbm5lckhUTUwgPSB0ZW1wRm9ybS5nZXRBdHRyaWJ1dGUoJ2RhdGEtbmFtZScpXG5cdFx0XHRvcmRlck1vZGFsMS5xdWVyeVNlbGVjdG9yKCcub3JkZXJNb2RhbF9fZGVzYycpLmlubmVySFRNTCA9IHRlbXBGb3JtLmdldEF0dHJpYnV0ZSgnZGF0YS1kZXNrJylcblx0XHRcdG9yZGVyTW9kYWwxLnF1ZXJ5U2VsZWN0b3IoJy5vcmRlck1vZGFsX19waG90byBpbWcnKS5zcmMgPSB0ZW1wRm9ybS5nZXRBdHRyaWJ1dGUoJ2RhdGEtcGhvdG8nKVxuXG5cdFx0XHRvcmRlck1vZGFsMS5jbGFzc0xpc3QuYWRkKCdvcmRlck1vZGFsLS12aWV3Jylcblx0XHR9KVxuXHR9KTtcblxuXHR2YXIgb3JkZXJNb2RhbENsb3NlID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgnLm9yZGVyTW9kYWxfX2Nsb3NlJylcblxuXHRpZihvcmRlck1vZGFsQ2xvc2Upe1xuXHRcdG9yZGVyTW9kYWxDbG9zZS5mb3JFYWNoKChidG4pID0+IHtcblx0XHRcdGJ0bi5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsICgpID0+IHtcblx0XHRcdFx0ZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLm9yZGVyTW9kYWwtLXZpZXcnKS5jbGFzc0xpc3QucmVtb3ZlKCdvcmRlck1vZGFsLS12aWV3Jylcblx0XHRcdH0pXG5cdFx0fSk7XG5cdH1cblxuXHR2YXIgb3JkZXJNb2RhbFBheSA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJyNvcmRlck1vZGFsUGF5Jylcblx0dmFyIG9yZGVyTW9kYWxOb1BheSA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJyNvcmRlck1vZGFsTm9QYXknKVxuXG5cdGZ1bmN0aW9uIGNoZWNrTW9kYWxQYXltZW50RmllbGRzKGFjdGlvbiwgZm9ybSl7XG5cdFx0aWYoIW9yZGVyTW9kYWxOYW1lLnZhbHVlIHx8ICFvcmRlck1vZGFsUGhvbmUudmFsdWUpe1xuXHRcdFx0aWYoIW9yZGVyTW9kYWxOYW1lLnZhbHVlKXtcblx0XHRcdFx0b3JkZXJNb2RhbE5hbWUuY2xhc3NMaXN0LmFkZCgnZXJyb3InKVxuXHRcdFx0fSBlbHNlIHtcblx0XHRcdFx0b3JkZXJNb2RhbE5hbWUuY2xhc3NMaXN0LnJlbW92ZSgnZXJyb3InKVxuXHRcdFx0fVxuXHRcdFx0aWYoIW9yZGVyTW9kYWxQaG9uZS52YWx1ZSl7XG5cdFx0XHRcdG9yZGVyTW9kYWxQaG9uZS5jbGFzc0xpc3QuYWRkKCdlcnJvcicpXG5cdFx0XHR9IGVsc2Uge1xuXHRcdFx0XHRvcmRlck1vZGFsUGhvbmUuY2xhc3NMaXN0LnJlbW92ZSgnZXJyb3InKVxuXHRcdFx0fVxuXHRcdH0gZWxzZSB7XG5cdFx0XHRvcmRlck1vZGFsMS5jbGFzc0xpc3QucmVtb3ZlKCdvcmRlck1vZGFsLS12aWV3Jylcblx0XHRcdHNlbmREYXRhKGFjdGlvbiwgZm9ybSlcblx0XHR9XG5cdH1cblxuXHRvcmRlck1vZGFsTm9QYXkuYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCAoKSA9PiB7XG5cdFx0dmFyIGZvcm0gPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcubWFrZUFuQXBwb2ludG1lbnQnKTtcblx0XHRjaGVja01vZGFsUGF5bWVudEZpZWxkcyhmb3JtLmdldEF0dHJpYnV0ZSgnZGF0YS1hY3Rpb24nKSwgZm9ybSlcblx0fSlcblxuXHRvcmRlck1vZGFsUGF5LmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgKCkgPT4ge1xuXHRcdHZhciBmb3JtID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLm1ha2VBbkFwcG9pbnRtZW50Jyk7XG5cdFx0Y2hlY2tNb2RhbFBheW1lbnRGaWVsZHMoZm9ybS5nZXRBdHRyaWJ1dGUoJ2FjdGlvbicpLCBmb3JtKVxuXHR9KVxufVxuIiwidmFyIGFkZEZhcUZvcm0gPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcub3JkZXJNb2RhbC0tYWRkRmFxIGZvcm0nKVxudmFyIG9yZGVyTW9kYWxTdWNjZXNzID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLm9yZGVyTW9kYWwtLXN1Y2Nlc3MnKTtcblxuaWYoYWRkRmFxRm9ybSl7XG5cdGFkZEZhcUZvcm0uYWRkRXZlbnRMaXN0ZW5lcignc3VibWl0JywgKCkgPT4ge1xuXHRcdGV2ZW50LnByZXZlbnREZWZhdWx0KClcblx0XHRzZW5kRGF0YShhZGRGYXFGb3JtLmdldEF0dHJpYnV0ZSgnYWN0aW9uJyksIGFkZEZhcUZvcm0pXG5cdH0pXG5cbn1cbiIsInZhciBhZGRSZXZpZXdGb3JtID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLm9yZGVyTW9kYWwtLWFkZFJldmlldyBmb3JtJylcbnZhciBvcmRlck1vZGFsU3VjY2VzcyA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5vcmRlck1vZGFsLS1zdWNjZXNzJyk7XG5cbmlmKGFkZFJldmlld0Zvcm0pe1xuXHRhZGRSZXZpZXdGb3JtLmFkZEV2ZW50TGlzdGVuZXIoJ3N1Ym1pdCcsICgpID0+IHtcblx0XHRldmVudC5wcmV2ZW50RGVmYXVsdCgpXG5cdFx0c2VuZERhdGEoYWRkUmV2aWV3Rm9ybS5nZXRBdHRyaWJ1dGUoJ2FjdGlvbicpLCBhZGRSZXZpZXdGb3JtKVxuXHR9KVxuXG59XG4iLCJ2YXIgb3JkZXJGaWx0ZXJzU3BlY2lhbGl6YXRpb24gPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcIm9yZGVyRmlsdGVyc1NwZWNpYWxpemF0aW9uXCIpO1xuXG5pZihvcmRlckZpbHRlcnNTcGVjaWFsaXphdGlvbil7XG5cdHZhciBzcGVjaWFsaXphdGlvbkxhYmVscyA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoXCIub3JkZXJGaWx0ZXJzX19pdGVtLS1zcGVjaWFsaXphdGlvbiBsYWJlbFwiKTtcblxuXHRzcGVjaWFsaXphdGlvbkxhYmVscy5mb3JFYWNoKChsYWJlbCkgPT4ge1xuXHRcdGxhYmVsLmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChldnQpID0+IHtcblx0XHRcdG9yZGVyRmlsdGVyc1NwZWNpYWxpemF0aW9uLnZhbHVlID0gZXZ0LmN1cnJlbnRUYXJnZXQucXVlcnlTZWxlY3RvcignaW5wdXQnKS52YWx1ZVxuXHRcdH0pXG5cdH0pXG5cblx0ZnVuY3Rpb24gZmlsdGVyU3BlY2lhbGl6YXRpb24oKSB7XG5cdFx0dmFyIGZpbHRlciA9IG9yZGVyRmlsdGVyc1NwZWNpYWxpemF0aW9uLnZhbHVlLnRvVXBwZXJDYXNlKCk7XG5cblx0XHRmb3IgKHZhciBpID0gMDsgaSA8IHNwZWNpYWxpemF0aW9uTGFiZWxzLmxlbmd0aDsgaSsrKSB7XG5cdFx0XHR2YXIgdHh0VmFsdWUgPSBzcGVjaWFsaXphdGlvbkxhYmVsc1tpXS50ZXh0Q29udGVudCB8fCBzcGVjaWFsaXphdGlvbkxhYmVsc1tpXS5pbm5lclRleHQ7XG5cdFx0XHRpZiAodHh0VmFsdWUudG9VcHBlckNhc2UoKS5pbmRleE9mKGZpbHRlcikgPiAtMSkge1xuXHRcdFx0XHRzcGVjaWFsaXphdGlvbkxhYmVsc1tpXS5zdHlsZS5kaXNwbGF5ID0gXCJcIjtcblx0XHRcdH0gZWxzZSB7XG5cdFx0XHRcdHNwZWNpYWxpemF0aW9uTGFiZWxzW2ldLnN0eWxlLmRpc3BsYXkgPSBcIm5vbmVcIjtcblx0XHRcdH1cblx0XHR9XG5cdH1cblx0b3JkZXJGaWx0ZXJzU3BlY2lhbGl6YXRpb24uYWRkRXZlbnRMaXN0ZW5lcigna2V5dXAnLCBmaWx0ZXJTcGVjaWFsaXphdGlvbilcbn1cblxudmFyIG9yZGVyRmlsdGVyc0FkZHJlc3MgPSBkb2N1bWVudC5nZXRFbGVtZW50QnlJZChcIm9yZGVyRmlsdGVyc0FkZHJlc3NcIik7XG5cbmlmKG9yZGVyRmlsdGVyc0FkZHJlc3Mpe1xuXHR2YXIgYWRkcmVzc0xhYmVscyA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoXCIub3JkZXJGaWx0ZXJzX19pdGVtLS1hZGRyZXNzIGxhYmVsXCIpO1xuXG5cdGFkZHJlc3NMYWJlbHMuZm9yRWFjaCgobGFiZWwpID0+IHtcblx0XHRsYWJlbC5hZGRFdmVudExpc3RlbmVyKCdjaGFuZ2UnLCAoZXZ0KSA9PiB7XG5cdFx0XHRvcmRlckZpbHRlcnNBZGRyZXNzLnZhbHVlID0gZXZ0LmN1cnJlbnRUYXJnZXQucXVlcnlTZWxlY3RvcignaW5wdXQnKS52YWx1ZVxuXHRcdH0pXG5cdH0pXG5cblx0ZnVuY3Rpb24gZmlsdGVyU3BlY2lhbGl6YXRpb24oKSB7XG5cdFx0dmFyIGZpbHRlciA9IG9yZGVyRmlsdGVyc0FkZHJlc3MudmFsdWUudG9VcHBlckNhc2UoKTtcblxuXHRcdGZvciAodmFyIGkgPSAwOyBpIDwgYWRkcmVzc0xhYmVscy5sZW5ndGg7IGkrKykge1xuXHRcdFx0dmFyIHR4dFZhbHVlID0gYWRkcmVzc0xhYmVsc1tpXS50ZXh0Q29udGVudCB8fCBhZGRyZXNzTGFiZWxzW2ldLmlubmVyVGV4dDtcblx0XHRcdGlmICh0eHRWYWx1ZS50b1VwcGVyQ2FzZSgpLmluZGV4T2YoZmlsdGVyKSA+IC0xKSB7XG5cdFx0XHRcdGFkZHJlc3NMYWJlbHNbaV0uc3R5bGUuZGlzcGxheSA9IFwiXCI7XG5cdFx0XHR9IGVsc2Uge1xuXHRcdFx0XHRhZGRyZXNzTGFiZWxzW2ldLnN0eWxlLmRpc3BsYXkgPSBcIm5vbmVcIjtcblx0XHRcdH1cblx0XHR9XG5cdH1cblx0b3JkZXJGaWx0ZXJzQWRkcmVzcy5hZGRFdmVudExpc3RlbmVyKCdrZXl1cCcsIGZpbHRlclNwZWNpYWxpemF0aW9uKVxufVxuXG52YXIgb3JkZXJGaWx0ZXJzQ2hlY2tlcnMgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcub3JkZXJGaWx0ZXJzX19jaGVja2VyJylcblxuaWYob3JkZXJGaWx0ZXJzQ2hlY2tlcnMubGVuZ3RoKXtcblx0b3JkZXJGaWx0ZXJzQ2hlY2tlcnMuZm9yRWFjaCgoYnV0dG9uKSA9PiB7XG5cdFx0YnV0dG9uLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgKCkgPT4ge1xuXHRcdFx0YnV0dG9uLm5leHRFbGVtZW50U2libGluZy5mb2N1cygpXG5cdFx0fSlcblx0fSlcbn1cblxudmFyIG9yZGVyRmlsdGVyc0lucHV0c1BvcHVwID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgnLm9yZGVyRmlsdGVyc19faW5wdXQtLXBvcHVwJyk7XG5cbmlmKG9yZGVyRmlsdGVyc0lucHV0c1BvcHVwLmxlbmd0aCl7XG5cdG9yZGVyRmlsdGVyc0lucHV0c1BvcHVwLmZvckVhY2goKGlucHV0KSA9PiB7XG5cdFx0aW5wdXQuYWRkRXZlbnRMaXN0ZW5lcignZm9jdXMnLCAoKSA9PiB7XG5cdFx0XHRkb2N1bWVudC5ib2R5LmNsYXNzTGlzdC5hZGQoJ25vU2Nyb2xsLW1vYmlsZScpXG5cdFx0XHRpbnB1dC5jbG9zZXN0KCcub3JkZXJGaWx0ZXJzX193cmFwJykuY2xhc3NMaXN0LmFkZCgnb3JkZXJGaWx0ZXJzX193cmFwLS1hY3RpdmUnKVxuXHRcdFx0aW5wdXQuY2xvc2VzdCgnLm9yZGVyRmlsdGVyc19faXRlbScpLmNsYXNzTGlzdC5hZGQoJ29yZGVyRmlsdGVyc19faXRlbS0tYWN0aXZlJylcblx0XHRcdGlucHV0LnBhcmVudE5vZGUucXVlcnlTZWxlY3RvcignLm9yZGVyRmlsdGVyc19fZHJvcERvd24nKS5jbGFzc0xpc3QuYWRkKCdvcmRlckZpbHRlcnNfX2Ryb3BEb3duLS1hY3RpdmUnKVxuXHRcdH0pXG5cdFx0aW5wdXQuYWRkRXZlbnRMaXN0ZW5lcignYmx1cicsICgpID0+IHtcblx0XHRcdHNldFRpbWVvdXQoKCkgPT4ge1xuXHRcdFx0XHRkb2N1bWVudC5ib2R5LmNsYXNzTGlzdC5yZW1vdmUoJ25vU2Nyb2xsLW1vYmlsZScpXG5cdFx0XHRcdGlucHV0LmNsb3Nlc3QoJy5vcmRlckZpbHRlcnNfX3dyYXAnKS5jbGFzc0xpc3QucmVtb3ZlKCdvcmRlckZpbHRlcnNfX3dyYXAtLWFjdGl2ZScpXG5cdFx0XHRcdGlucHV0LmNsb3Nlc3QoJy5vcmRlckZpbHRlcnNfX2l0ZW0nKS5jbGFzc0xpc3QucmVtb3ZlKCdvcmRlckZpbHRlcnNfX2l0ZW0tLWFjdGl2ZScpXG5cdFx0XHRcdGlucHV0LnBhcmVudE5vZGUucXVlcnlTZWxlY3RvcignLm9yZGVyRmlsdGVyc19fZHJvcERvd24nKS5jbGFzc0xpc3QucmVtb3ZlKCdvcmRlckZpbHRlcnNfX2Ryb3BEb3duLS1hY3RpdmUnKVxuXHRcdFx0fSwgMTAwKVxuXHRcdH0pXG5cdH0pXG59XG5cbnZhciBvcmRlckZpbHRlcnNTaG93RmllbGRzID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLm9yZGVyRmlsdGVyc19fc2hvd0ZpZWxkcycpXG5cbmlmKG9yZGVyRmlsdGVyc1Nob3dGaWVsZHMpe1xuXG5cdHZhciBvcmRlckZpbHRlcnNJbnB1dE5hbWUgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcub3JkZXJGaWx0ZXJzX19pbnB1dC0tbmFtZScpXG5cblx0aWYob3JkZXJGaWx0ZXJzSW5wdXROYW1lKXtcblx0XHRvcmRlckZpbHRlcnNJbnB1dE5hbWUuYWRkRXZlbnRMaXN0ZW5lcignZm9jdXMnLCAoKSA9PiB7XG5cdFx0XHRvcmRlckZpbHRlcnNJbnB1dE5hbWUuY2xvc2VzdCgnLm9yZGVyRmlsdGVycycpLmNsYXNzTGlzdC5hZGQoJ29yZGVyRmlsdGVycy0tb24nKVxuXHRcdFx0b3JkZXJGaWx0ZXJzU2hvd0ZpZWxkcy5jbGFzc0xpc3QuYWRkKCdvcmRlckZpbHRlcnNfX3Nob3dGaWVsZHMtLWFjdGl2ZScpXG5cdFx0XHRvcmRlckZpbHRlcnNJbnB1dE5hbWUuY2xvc2VzdCgnLm9yZGVyRmlsdGVyc19fd3JhcCcpLmNsYXNzTGlzdC5hZGQoJ29yZGVyRmlsdGVyc19fd3JhcC0tb24nKVxuXHRcdFx0b3JkZXJGaWx0ZXJzU2hvd0ZpZWxkcy5wYXJlbnROb2RlLnF1ZXJ5U2VsZWN0b3IoJy5vcmRlckZpbHRlcnNfX2Ryb3BEb3duJykuY2xhc3NMaXN0LmFkZCgnb3JkZXJGaWx0ZXJzX19kcm9wRG93bi0tb24nKVxuXHRcdH0pXG5cblx0XHRvcmRlckZpbHRlcnNJbnB1dE5hbWUuYWRkRXZlbnRMaXN0ZW5lcignYmx1cicsICgpID0+IHtcblx0XHRcdHNldFRpbWVvdXQoKCkgPT4ge1xuXHRcdFx0XHRpZighZG9jdW1lbnQuYWN0aXZlRWxlbWVudC5jbG9zZXN0KCcub3JkZXJGaWx0ZXJzJykpe1xuXHRcdFx0XHRcdG9yZGVyRmlsdGVyc0lucHV0TmFtZS5jbG9zZXN0KCcub3JkZXJGaWx0ZXJzJykuY2xhc3NMaXN0LnJlbW92ZSgnb3JkZXJGaWx0ZXJzLS1vbicpXG5cdFx0XHRcdFx0b3JkZXJGaWx0ZXJzU2hvd0ZpZWxkcy5jbGFzc0xpc3QucmVtb3ZlKCdvcmRlckZpbHRlcnNfX3Nob3dGaWVsZHMtLWFjdGl2ZScpXG5cdFx0XHRcdFx0b3JkZXJGaWx0ZXJzSW5wdXROYW1lLmNsb3Nlc3QoJy5vcmRlckZpbHRlcnNfX3dyYXAnKS5jbGFzc0xpc3QucmVtb3ZlKCdvcmRlckZpbHRlcnNfX3dyYXAtLW9uJylcblx0XHRcdFx0XHRvcmRlckZpbHRlcnNTaG93RmllbGRzLnBhcmVudE5vZGUucXVlcnlTZWxlY3RvcignLm9yZGVyRmlsdGVyc19fZHJvcERvd24nKS5jbGFzc0xpc3QucmVtb3ZlKCdvcmRlckZpbHRlcnNfX2Ryb3BEb3duLS1vbicpXG5cdFx0XHRcdH1cblx0XHRcdH0sIDEwMClcblx0XHR9KVxuXHR9XG5cblx0b3JkZXJGaWx0ZXJzU2hvd0ZpZWxkcy5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsICgpID0+IHtcblx0XHRvcmRlckZpbHRlcnNTaG93RmllbGRzLmNsb3Nlc3QoJy5vcmRlckZpbHRlcnMnKS5jbGFzc0xpc3QudG9nZ2xlKCdvcmRlckZpbHRlcnMtLW9uJylcblx0XHRvcmRlckZpbHRlcnNTaG93RmllbGRzLmNsYXNzTGlzdC50b2dnbGUoJ29yZGVyRmlsdGVyc19fc2hvd0ZpZWxkcy0tYWN0aXZlJylcblx0XHRvcmRlckZpbHRlcnNJbnB1dE5hbWUuY2xvc2VzdCgnLm9yZGVyRmlsdGVyc19fd3JhcCcpLmNsYXNzTGlzdC50b2dnbGUoJ29yZGVyRmlsdGVyc19fd3JhcC0tb24nKVxuXHRcdG9yZGVyRmlsdGVyc1Nob3dGaWVsZHMucGFyZW50Tm9kZS5xdWVyeVNlbGVjdG9yKCcub3JkZXJGaWx0ZXJzX19kcm9wRG93bicpLmNsYXNzTGlzdC50b2dnbGUoJ29yZGVyRmlsdGVyc19fZHJvcERvd24tLW9uJylcblx0fSlcbn1cblxudmFyIG9yZGVyRmlsdGVyc0NoZWNrYm94RGVza3RvcCA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3JBbGwoJy5vcmRlckZpbHRlcnNfX2lucHV0LS1jaGVja2JveCcpXG5cbmlmKG9yZGVyRmlsdGVyc0NoZWNrYm94RGVza3RvcC5sZW5ndGgpe1xuXHRvcmRlckZpbHRlcnNDaGVja2JveERlc2t0b3AuZm9yRWFjaCgoY2hlY2tib3gpID0+IHtcblx0XHRjaGVja2JveC5hZGRFdmVudExpc3RlbmVyKCdjaGFuZ2UnLCAoKSA9PiB7XG5cdFx0XHRpZihjaGVja2JveC5jaGVja2VkKXtcblx0XHRcdFx0Y2hlY2tib3guY2xvc2VzdCgnLm9yZGVyRmlsdGVycycpLmNsYXNzTGlzdC5hZGQoJ29yZGVyRmlsdGVycy0tZW5hYmxlZCcpXG5cdFx0XHR9IGVsc2Uge1xuXHRcdFx0XHRjaGVja2JveC5jbG9zZXN0KCcub3JkZXJGaWx0ZXJzJykuY2xhc3NMaXN0LnJlbW92ZSgnb3JkZXJGaWx0ZXJzLS1lbmFibGVkJylcblx0XHRcdH1cblx0XHR9KVxuXHR9KVxufVxuIiwiLy8ub3JkZXJQYWdlIHNjcmlwdHMgZ29lcyBoZXJlXG4iLCJ2YXIgY3VycmVudFBhcnRuZXJzU2xpZGVyO1xuXG53aW5kb3cuYWRkRXZlbnRMaXN0ZW5lcihcInJlc2l6ZVwiLCAoKSA9PiB7XG5cdGlmKHdpbmRvdy5pbm5lcldpZHRoID49IDEwMjQpe1xuXHRcdGFjdGl2YXRlRnJvbnRDbGluaWNTTGlkZXJzKGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5wYXJ0bmVyc19fbGlzdCcpKVxuXHR9IGVsc2Uge1xuXHRcdGlmKGN1cnJlbnRQYXJ0bmVyc1NsaWRlcil7XG5cdFx0XHRjdXJyZW50UGFydG5lcnNTbGlkZXIuZGVzdHJveSgpXG5cdFx0fVxuXHR9XG59KTtcblxud2luZG93LmFkZEV2ZW50TGlzdGVuZXIoXCJET01Db250ZW50TG9hZGVkXCIsICgpID0+IHtcblx0aWYod2luZG93LmlubmVyV2lkdGggPj0gMTAyNCl7XG5cdFx0YWN0aXZhdGVGcm9udENsaW5pY1NMaWRlcnMoZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnBhcnRuZXJzX19saXN0JykpXG5cdH1cbn0pO1xuXG5cbmZ1bmN0aW9uIGFjdGl2YXRlRnJvbnRDbGluaWNTTGlkZXJzKGVsZW1lbnQpe1xuXHRjdXJyZW50UGFydG5lcnNTbGlkZXIgPSBuZXcgRmxpY2tpdHkoIGVsZW1lbnQsIHtcblx0XHQvLyBvcHRpb25zXG5cdFx0Y2VsbEFsaWduOiAnbGVmdCcsXG5cdFx0Y29udGFpbjogdHJ1ZSxcblx0XHRwYWdlRG90czogZmFsc2UsXG5cdFx0YXJyb3dTaGFwZTogJ00gMTAsNTAgTCA2MCwxMDAgTCA3MCw5MCBMIDMwLDUwICBMIDcwLDEwIEwgNjAsMCBaJyxcblx0XHRncm91cENlbGxzOiA0XG5cdH0pO1xufVxuIiwidmFyIHBsYWNlTG9va3NMaWtlUGhvdG8gPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcucGxhY2VMb29rc0xpa2VfX2l0ZW0tLXBob3RvJylcbnZhciBwbGFjZUxvb2tzTGlrZVBhbm8gPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcucGxhY2VMb29rc0xpa2VfX2l0ZW0tLXBhbm8nKVxudmFyIHBsYWNlTG9va3NMaWtlTWFwID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnBsYWNlTG9va3NMaWtlX19pdGVtLS1tYXAnKVxuXG52YXIgcGxhY2VMb29rc0xpa2VDb250cm9sUGhvdG8gPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcucGxhY2VMb29rc0xpa2VfX2NvbnRyb2wtLXBob3RvJylcbnZhciBwbGFjZUxvb2tzTGlrZUNvbnRyb2xQYW5vID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnBsYWNlTG9va3NMaWtlX19jb250cm9sLS1wYW5vJylcbnZhciBwbGFjZUxvb2tzTGlrZUNvbnRyb2xNYXAgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcucGxhY2VMb29rc0xpa2VfX2NvbnRyb2wtLW1hcCcpXG5cbmlmKHBsYWNlTG9va3NMaWtlQ29udHJvbFBob3RvKXtcblx0cGxhY2VMb29rc0xpa2VDb250cm9sUGhvdG8uYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCAoKSA9PiB7XG5cdFx0ZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnBsYWNlTG9va3NMaWtlX19jb250cm9sLS1hY3RpdmUnKS5jbGFzc0xpc3QucmVtb3ZlKCdwbGFjZUxvb2tzTGlrZV9fY29udHJvbC0tYWN0aXZlJylcblx0XHRldmVudC5jdXJyZW50VGFyZ2V0LmNsYXNzTGlzdC5hZGQoJ3BsYWNlTG9va3NMaWtlX19jb250cm9sLS1hY3RpdmUnKVxuXHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5wbGFjZUxvb2tzTGlrZV9faXRlbS0tYWN0aXZlJykuY2xhc3NMaXN0LnJlbW92ZSgncGxhY2VMb29rc0xpa2VfX2l0ZW0tLWFjdGl2ZScpXG5cdFx0cGxhY2VMb29rc0xpa2VQaG90by5jbGFzc0xpc3QuYWRkKCdwbGFjZUxvb2tzTGlrZV9faXRlbS0tYWN0aXZlJylcblx0fSlcbn1cbmlmKHBsYWNlTG9va3NMaWtlQ29udHJvbFBhbm8pe1xuXHR2YXIgcGxhY2VMb29rc0xpa2VQYW5vSWZyYW1lID0gcGxhY2VMb29rc0xpa2VQYW5vLnF1ZXJ5U2VsZWN0b3IoJ2lmcmFtZScpXG5cdHBsYWNlTG9va3NMaWtlQ29udHJvbFBhbm8uYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCAoKSA9PiB7XG5cdFx0ZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnBsYWNlTG9va3NMaWtlX19jb250cm9sLS1hY3RpdmUnKS5jbGFzc0xpc3QucmVtb3ZlKCdwbGFjZUxvb2tzTGlrZV9fY29udHJvbC0tYWN0aXZlJylcblx0XHRldmVudC5jdXJyZW50VGFyZ2V0LmNsYXNzTGlzdC5hZGQoJ3BsYWNlTG9va3NMaWtlX19jb250cm9sLS1hY3RpdmUnKVxuXHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5wbGFjZUxvb2tzTGlrZV9faXRlbS0tYWN0aXZlJykuY2xhc3NMaXN0LnJlbW92ZSgncGxhY2VMb29rc0xpa2VfX2l0ZW0tLWFjdGl2ZScpXG5cdFx0cGxhY2VMb29rc0xpa2VQYW5vLmNsYXNzTGlzdC5hZGQoJ3BsYWNlTG9va3NMaWtlX19pdGVtLS1hY3RpdmUnKVxuXHRcdGlmKCFwbGFjZUxvb2tzTGlrZVBhbm9JZnJhbWUuZ2V0QXR0cmlidXRlKCdzcmMnKSl7XG5cdFx0XHRwbGFjZUxvb2tzTGlrZVBhbm9JZnJhbWUuc2V0QXR0cmlidXRlKCdzcmMnLCBwbGFjZUxvb2tzTGlrZVBhbm8uZGF0YXNldC5zcmMpXG5cdFx0fVxuXHR9KVxufVxuaWYocGxhY2VMb29rc0xpa2VDb250cm9sTWFwKXtcblx0dmFyIHBsYWNlTG9va3NMaWtlTWFwSWZyYW1lID0gcGxhY2VMb29rc0xpa2VNYXAucXVlcnlTZWxlY3RvcignaWZyYW1lJylcblx0cGxhY2VMb29rc0xpa2VDb250cm9sTWFwLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgKCkgPT4ge1xuXHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5wbGFjZUxvb2tzTGlrZV9fY29udHJvbC0tYWN0aXZlJykuY2xhc3NMaXN0LnJlbW92ZSgncGxhY2VMb29rc0xpa2VfX2NvbnRyb2wtLWFjdGl2ZScpXG5cdFx0ZXZlbnQuY3VycmVudFRhcmdldC5jbGFzc0xpc3QuYWRkKCdwbGFjZUxvb2tzTGlrZV9fY29udHJvbC0tYWN0aXZlJylcblx0XHRkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcucGxhY2VMb29rc0xpa2VfX2l0ZW0tLWFjdGl2ZScpLmNsYXNzTGlzdC5yZW1vdmUoJ3BsYWNlTG9va3NMaWtlX19pdGVtLS1hY3RpdmUnKVxuXHRcdHBsYWNlTG9va3NMaWtlTWFwLmNsYXNzTGlzdC5hZGQoJ3BsYWNlTG9va3NMaWtlX19pdGVtLS1hY3RpdmUnKVxuXHRcdGlmKCFwbGFjZUxvb2tzTGlrZU1hcElmcmFtZS5nZXRBdHRyaWJ1dGUoJ3NyYycpKXtcblx0XHRcdHBsYWNlTG9va3NMaWtlTWFwSWZyYW1lLnNldEF0dHJpYnV0ZSgnc3JjJywgcGxhY2VMb29rc0xpa2VNYXAuZGF0YXNldC5zcmMpXG5cdFx0fVxuXHR9KVxufVxuIiwidmFyIHJldmlld3NCdG4gPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcucmV2aWV3c19fYnRuJylcbnZhciByZXZpZXdNb2RhbCA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5vcmRlck1vZGFsLS1hZGRSZXZpZXcnKVxuXG5pZihyZXZpZXdzQnRuKXtcblx0cmV2aWV3c0J0bi5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIChldmVudCkgPT4ge1xuXHRcdGV2ZW50LnByZXZlbnREZWZhdWx0KClcblx0XHRyZXZpZXdNb2RhbC5jbGFzc0xpc3QuYWRkKCdvcmRlck1vZGFsLS12aWV3Jylcblx0fSlcbn1cbiIsIndpbmRvdy5hZGRFdmVudExpc3RlbmVyKFwicmVzaXplXCIsICgpID0+IHtcblx0aWYod2luZG93LmlubmVyV2lkdGggPj0gNzIwKXtcblx0XHRzZXRUaW1lb3V0KCgpID0+IHtcblx0XHRcdHZhciBzbGlkZXJIZWlnaHQgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcuc2xpZGVyX19pdGVtJykub2Zmc2V0SGVpZ2h0ICsgJ3B4J1xuXHRcdFx0ZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnNsaWRlcl9fbGlzdCcpLnN0eWxlLmhlaWdodCA9IHNsaWRlckhlaWdodFxuXHRcdH0sIDUwKVxuXHRcdFx0aWYoIWRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5zbGlkZXJfX2xpc3QnKS5jbGFzc0xpc3QuY29udGFpbnMoJ21haW5TbGlkZXInKSl7XG5cdFx0XHRkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcuc2xpZGVyX19saXN0JykuY2xhc3NMaXN0LmFkZCgnbWFpblNsaWRlcicpXG5cdFx0fVxuXHR9IGVsc2Uge1xuXHRcdGlmKG1haW5TbGlkZXIpe1xuXHRcdFx0ZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnNsaWRlcl9fbGlzdCcpLmNsYXNzTGlzdC5yZW1vdmUoJ21haW5TbGlkZXInKVxuXHRcdFx0ZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnNsaWRlcl9fbGlzdCcpLnJlbW92ZUF0dHJpYnV0ZSgnc3R5bGUnKVxuXHRcdH1cblx0fVxufSlcblxud2luZG93LmFkZEV2ZW50TGlzdGVuZXIoXCJET01Db250ZW50TG9hZGVkXCIsICgpID0+IHtcblx0aWYod2luZG93LmlubmVyV2lkdGggPj0gNzIwKXtcblx0XHRkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcuc2xpZGVyX19saXN0JykuY2xhc3NMaXN0LmFkZCgnbWFpblNsaWRlcicpXG5cdFx0c2V0VGltZW91dCgoKSA9PiB7XG5cdFx0XHR2YXIgc2xpZGVySGVpZ2h0ID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnNsaWRlcl9faXRlbScpLm9mZnNldEhlaWdodCArICdweCdcblx0XHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5zbGlkZXJfX2xpc3QnKS5zdHlsZS5oZWlnaHQgPSBzbGlkZXJIZWlnaHRcblx0XHR9LCA1MClcblx0fVxufSlcblxudmFyIHNsaWRlclByZXZCdXR0b24gPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcuc2xpZGVyX19idG4tLXByZXYnKVxudmFyIHNsaWRlck5leHRCdXR0b24gPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcuc2xpZGVyX19idG4tLW5leHQnKVxuXG5pZihzbGlkZXJQcmV2QnV0dG9uICYmIHNsaWRlck5leHRCdXR0b24pe1xuXHR2YXIgbWFpblNsaWRlciA9IGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5zbGlkZXJfX2xpc3QnKTtcblxuXHRzbGlkZXJQcmV2QnV0dG9uLmFkZEV2ZW50TGlzdGVuZXIoJ2NsaWNrJywgKCkgPT4ge1xuXHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5zbGlkZXJfX2l0ZW0tLWFjdGl2ZScpLmNsYXNzTGlzdC5yZW1vdmUoJ3NsaWRlcl9faXRlbS0tYWN0aXZlJylcblxuXHRcdGlmKGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5zbGlkZXJfX2RvdHMgLmFjdGl2ZScpLnByZXZpb3VzRWxlbWVudFNpYmxpbmcpe1xuXHRcdFx0ZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnNsaWRlcl9fZG90cyAuYWN0aXZlJykucHJldmlvdXNFbGVtZW50U2libGluZy5jbGFzc0xpc3QuYWRkKCdhY3RpdmUnKVxuXHRcdFx0ZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnNsaWRlcl9fZG90cyAuYWN0aXZlJykubmV4dEVsZW1lbnRTaWJsaW5nLmNsYXNzTGlzdC5yZW1vdmUoJ2FjdGl2ZScpXG5cdFx0fSBlbHNlIHtcblx0XHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5zbGlkZXJfX2RvdHMgc3BhbicpLmNsYXNzTGlzdC5yZW1vdmUoJ2FjdGl2ZScpXG5cdFx0XHRkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcuc2xpZGVyX19kb3RzIHNwYW46bGFzdC1vZi10eXBlJykuY2xhc3NMaXN0LmFkZCgnYWN0aXZlJylcblx0XHR9XG5cblx0XHRtYWluU2xpZGVyLnByZXBlbmQoZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnNsaWRlcl9faXRlbTpsYXN0LW9mLXR5cGUnKSlcblx0XHRkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcuc2xpZGVyX19pdGVtJykuY2xhc3NMaXN0LmFkZCgnc2xpZGVyX19pdGVtLS1vdXQnKVxuXHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5zbGlkZXJfX2l0ZW0nKS5jbGFzc0xpc3QuYWRkKCdzbGlkZXJfX2l0ZW0tLWFjdGl2ZScpXG5cdFx0c2V0VGltZW91dCgoKSA9PiB7XG5cdFx0XHRkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcuc2xpZGVyX19pdGVtLS1vdXQnKS5jbGFzc0xpc3QucmVtb3ZlKCdzbGlkZXJfX2l0ZW0tLW91dCcpXG5cdFx0fSwgMzAwKVxuXHR9KVxuXG5cdHNsaWRlck5leHRCdXR0b24uYWRkRXZlbnRMaXN0ZW5lcignY2xpY2snLCAoKSA9PiB7XG5cdFx0ZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnNsaWRlcl9faXRlbS0tYWN0aXZlJykuY2xhc3NMaXN0LmFkZCgnc2xpZGVyX19pdGVtLS1vdXQnKVxuXG5cdFx0aWYoZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnNsaWRlcl9fZG90cyAuYWN0aXZlJykubmV4dEVsZW1lbnRTaWJsaW5nKXtcblx0XHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5zbGlkZXJfX2RvdHMgLmFjdGl2ZScpLm5leHRFbGVtZW50U2libGluZy5jbGFzc0xpc3QuYWRkKCdhY3RpdmUnKVxuXHRcdFx0ZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnNsaWRlcl9fZG90cyAuYWN0aXZlJykuY2xhc3NMaXN0LnJlbW92ZSgnYWN0aXZlJylcblx0XHR9IGVsc2Uge1xuXHRcdFx0ZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnNsaWRlcl9fZG90cyBzcGFuJykuY2xhc3NMaXN0LmFkZCgnYWN0aXZlJylcblx0XHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5zbGlkZXJfX2RvdHMgc3BhbjpsYXN0LW9mLXR5cGUnKS5jbGFzc0xpc3QucmVtb3ZlKCdhY3RpdmUnKVxuXHRcdH1cblxuXHRcdHNldFRpbWVvdXQoKCkgPT4ge1xuXHRcdFx0bWFpblNsaWRlci5hcHBlbmQoZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLnNsaWRlcl9faXRlbS0tYWN0aXZlJykpXG5cdFx0XHRkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcuc2xpZGVyX19pdGVtLS1hY3RpdmUnKS5jbGFzc0xpc3QucmVtb3ZlKCdzbGlkZXJfX2l0ZW0tLWFjdGl2ZScpXG5cdFx0XHRkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcuc2xpZGVyX19pdGVtLS1vdXQnKS5jbGFzc0xpc3QucmVtb3ZlKCdzbGlkZXJfX2l0ZW0tLW91dCcpXG5cdFx0XHRkb2N1bWVudC5xdWVyeVNlbGVjdG9yKCcuc2xpZGVyX19pdGVtJykuY2xhc3NMaXN0LmFkZCgnc2xpZGVyX19pdGVtLS1hY3RpdmUnKVxuXHRcdH0sIDMwMClcblx0fSlcbn1cbiIsIi8vLnN0YXRpc3RpY3Mgc2NyaXB0cyBnb2VzIGhlcmVcbiIsInZhciB2YWNhbmNpZXMgPSBkb2N1bWVudC5xdWVyeVNlbGVjdG9yQWxsKCcudmFjYW5jaWVzX190aXRsZSBhJylcblxuaWYodmFjYW5jaWVzLmxlbmd0aCl7XG5cdHZhY2FuY2llcy5mb3JFYWNoKChpdGVtKSA9PiB7XG5cdFx0aXRlbS5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIChldmVudCkgPT4ge1xuXHRcdFx0ZXZlbnQucHJldmVudERlZmF1bHQoKVxuXHRcdFx0ZXZlbnQuY3VycmVudFRhcmdldC5jbG9zZXN0KCcudmFjYW5jaWVzX19pdGVtJykuY2xhc3NMaXN0LnRvZ2dsZSgndmFjYW5jaWVzX19pdGVtLS1hY3RpdmUnKVxuXHRcdH0pXG5cdH0pXG59XG4iLCJmdW5jdGlvbiBzZW5kRGF0YShmaWxlTmFtZSwgZm9ybSkge1xuXHR2YXIgWEhSID0gbmV3IFhNTEh0dHBSZXF1ZXN0KCk7XG5cdHZhciBGRCA9IG5ldyBGb3JtRGF0YShmb3JtKTtcblx0WEhSLmFkZEV2ZW50TGlzdGVuZXIoXCJsb2FkXCIsIGZ1bmN0aW9uKGV2ZW50KSB7XG5cdFx0Y29uc29sZS5sb2codGhpcy5yZXNwb25zZVRleHQpXG5cdFx0aWYoSlNPTi5wYXJzZSh0aGlzLnJlc3BvbnNlVGV4dCkucmVzcG9uc2UgPT0gXCIxXCIpe1xuXHRcdFx0b3JkZXJNb2RhbFN1Y2Nlc3MuY2xhc3NMaXN0LmFkZCgnb3JkZXJNb2RhbC0tdmlldycpXG5cdFx0fVxuXHR9KTtcblx0WEhSLmFkZEV2ZW50TGlzdGVuZXIoXCJlcnJvclwiLCBmdW5jdGlvbihldmVudCkge1xuXHRcdGFsZXJ0KCfQntGI0LjQsdC60LAhJyk7XG5cdH0pO1xuXHRYSFIub3BlbihcIlBPU1RcIiwgZmlsZU5hbWUpO1xuXHRYSFIuc2VuZChGRCk7XG59XG5cbnZhciBmcm9udENsaW5pY3NUYWJzID0gZG9jdW1lbnQucXVlcnlTZWxlY3RvckFsbCgnLm1kV3JhcC0tZnJvbnRDbGluaWNzIGEnKVxudmFyIGN1cnJlbnRDbGluaWNTbGlkZXI7XG5cbmlmKGZyb250Q2xpbmljc1RhYnMubGVuZ3RoKXtcblx0ZnJvbnRDbGluaWNzVGFicy5mb3JFYWNoKChsaW5rKSA9PiB7XG5cdFx0bGluay5hZGRFdmVudExpc3RlbmVyKCdjbGljaycsIChldmVudCkgPT4ge1xuXHRcdFx0ZXZlbnQucHJldmVudERlZmF1bHQoKVxuXHRcdFx0ZXZlbnQuY3VycmVudFRhcmdldC5jbG9zZXN0KCcubWRXcmFwX19saW5rcycpLnF1ZXJ5U2VsZWN0b3IoJy5tZFdyYXBfX2xpbmstLWFjdGl2ZScpLmNsYXNzTGlzdC5yZW1vdmUoJ21kV3JhcF9fbGluay0tYWN0aXZlJylcblx0XHRcdGV2ZW50LmN1cnJlbnRUYXJnZXQuY2xvc2VzdCgnLm1kV3JhcF9fbGluaycpLmNsYXNzTGlzdC5hZGQoJ21kV3JhcF9fbGluay0tYWN0aXZlJylcblx0XHRcdGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5jbGluaWNzTURfX2JvZHktLWFjdGl2ZScpLmNsYXNzTGlzdC5yZW1vdmUoJ2NsaW5pY3NNRF9fYm9keS0tYWN0aXZlJylcblx0XHRcdHZhciB0YXJnZXRCb2R5ID0gZXZlbnQuY3VycmVudFRhcmdldC5jbG9zZXN0KCcuY2xpbmljc01EJykucXVlcnlTZWxlY3RvcihgLmNsaW5pY3NNRF9fYm9keVtkYXRhLWNpdHk9JHtldmVudC5jdXJyZW50VGFyZ2V0LmRhdGFzZXQuY2l0eX1dYClcblx0XHRcdHRhcmdldEJvZHkuY2xhc3NMaXN0LmFkZCgnY2xpbmljc01EX19ib2R5LS1hY3RpdmUnKVxuXG5cdFx0XHRpZih3aW5kb3cuaW5uZXJXaWR0aCA+PSAxMjAwKXtcblx0XHRcdFx0aWYoY3VycmVudENsaW5pY1NsaWRlcil7XG5cdFx0XHRcdFx0Y3VycmVudENsaW5pY1NsaWRlci5kZXN0cm95KClcblx0XHRcdFx0fVxuXHRcdFx0XHRhY3RpdmF0ZUZyb250Q2xpbmljU0xpZGVycyh0YXJnZXRCb2R5KVxuXHRcdFx0fVxuXHRcdH0pXG5cdH0pXG59XG5cbndpbmRvdy5hZGRFdmVudExpc3RlbmVyKFwicmVzaXplXCIsICgpID0+IHtcblx0aWYod2luZG93LmlubmVyV2lkdGggPj0gMTIwMCl7XG5cdFx0YWN0aXZhdGVGcm9udENsaW5pY1NMaWRlcnMoZG9jdW1lbnQucXVlcnlTZWxlY3RvcignLmNsaW5pY3NNRF9fYm9keS0tYWN0aXZlJykpXG5cdH0gZWxzZSB7XG5cdFx0aWYoY3VycmVudENsaW5pY1NsaWRlcil7XG5cdFx0XHRjdXJyZW50Q2xpbmljU2xpZGVyLmRlc3Ryb3koKVxuXHRcdH1cblx0fVxufSk7XG5cbndpbmRvdy5hZGRFdmVudExpc3RlbmVyKFwiRE9NQ29udGVudExvYWRlZFwiLCAoKSA9PiB7XG5cdGlmKHdpbmRvdy5pbm5lcldpZHRoID49IDEyMDApe1xuXHRcdGFjdGl2YXRlRnJvbnRDbGluaWNTTGlkZXJzKGRvY3VtZW50LnF1ZXJ5U2VsZWN0b3IoJy5jbGluaWNzTURfX2JvZHktLWFjdGl2ZScpKVxuXHR9XG59KTtcblxuXG5mdW5jdGlvbiBhY3RpdmF0ZUZyb250Q2xpbmljU0xpZGVycyhlbGVtZW50KXtcblx0Y3VycmVudENsaW5pY1NsaWRlciA9IG5ldyBGbGlja2l0eSggZWxlbWVudCwge1xuXHRcdC8vIG9wdGlvbnNcblx0XHRjZWxsQWxpZ246ICdsZWZ0Jyxcblx0XHRjb250YWluOiB0cnVlLFxuXHRcdHBhZ2VEb3RzOiBmYWxzZSxcblx0XHRhcnJvd1NoYXBlOiAnTSAxMCw1MCBMIDYwLDEwMCBMIDcwLDkwIEwgMzAsNTAgIEwgNzAsMTAgTCA2MCwwIFonLFxuXHRcdGdyb3VwQ2VsbHM6IDVcblx0fSk7XG59XG4iXX0=
