//Показ пароля при регистрации и вводе
function show_hide_password(target){
    let pass = document.getElementsByClassName('pass');
    for(let input of pass){
        if (input.getAttribute('type') == 'password') {
            target.classList.add('view');
            input.setAttribute('type', 'text');
        } else {
            target.classList.remove('view');
            input.setAttribute('type', 'password');
        }
    }
	
}
//Сравнение паролей
/* var button = document.getElementsById('sing_up');

function srav(){
    var diag_nap_uchr = document.getElementById('InputPassword');
    var diag_osn = document.getElementById('repeatPassword');
    if (diag_nap_uchr.value === diag_osn.value){
        alert ("Совпадение");
        button.disabled = false;
        button.removeAttribute("disabled");
      
    }
    if(diag_nap_uchr.value != diag_osn.value){
        button.setAttribute("disabled", "disabled");
        alert ("Совпадение");
    }
  } */