let form = document.querySelector('.js-form'),
    formInputs = document.querySelectorAll('.js-input'),
    inputEmail = document.querySelector('.js-input-email'),
    inputPhone = document.querySelector('.js-input-phone'),
    inputLogin = document.querySelector('.js-input-login'),
    inputPassword = document.querySelector('.js-input-password'),
    inputPasswordAgain = document.querySelector('.js-input-password-again');


function validateEmail(email) {
    let re = /^[\w-\.]+@[\w-]+\.[a-z]{2,4}$/i;
    return re.test(String(email).toLowerCase());
}

function validatePhone(phone) {
    let re = /^[\d\+][\d\(\)\ -]{4,14}\d$/;
    return re.test(String(phone));
}

function validatePasswords(password) {
    let re = /(?=.*[a-z])(?=.*[A-Z])/
    return re.test(String(password))
}

form.onsubmit = function () {
    let emailVal = inputEmail.value,
        phoneVal = inputPhone.value,
        passVal = inputPassword.value,
        loginVal = inputLogin.value,
        passValAgain = inputPasswordAgain.value,
        emptyInputs = Array.from(formInputs).filter(input => input.value === '');

    formInputs.forEach(function (input) {
        if (input.value === '') {
            input.classList.add('error');

        } else {
            input.classList.remove('error');
        }
    });


    if (emptyInputs.length !== 0) {
        return false;
    }

    if (loginVal.length < 6) {
        inputLogin.classList.add('error');
        return false;
    } else {
        inputLogin.classList.remove('error');
    }


    if (!validateEmail(emailVal)) {
        inputEmail.classList.add('error');
        return false;
    } else {
        inputEmail.classList.remove('error');
    }


    if (!validatePhone(phoneVal)) {
        inputPhone.classList.add('error');
        return false;
    } else {
        inputPhone.classList.remove('error');
    }

    if (passVal !== passValAgain) {
        alert('try again');
        inputPassword.classList.add('error');
        inputPasswordAgain.classList.add('error');
        return false;
    }

    if (!validatePasswords(passVal)) {
        alert('try again');
        inputPassword.classList.add('error');
        inputPasswordAgain.classList.add('error');
        return false;
    } else {
        inputPassword.classList.remove('error');
        inputPasswordAgain.classList.remove('error');
    }

    if (emptyInputs.length === 0) {
        alert('registration was successful')
    }



}
