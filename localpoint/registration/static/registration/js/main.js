//Показ пароля при регистрации и вводе
function show_hide_password(target) {
    let pass = document.getElementsByClassName('pass');
    for (let input of pass) {
        if (input.getAttribute('type') === 'password') {
            target.classList.add('view');
            input.setAttribute('type', 'text');
        } else {
            target.classList.remove('view');
            input.setAttribute('type', 'password');
        }
    }

}
//Сравнение паролей

function srav(inppass, inprep) {
    let button = document.getElementById('sing_up');
    var pass = document.getElementById(inppass);
    var repeat_pass = document.getElementById(inprep);
    if (pass.value === repeat_pass.value && pass.value !== "") {
        button.classList.remove("disabled");
    }
    else {
        button.classList.add("disabled");
    }
}