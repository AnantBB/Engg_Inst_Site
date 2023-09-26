function year_selection(option_sel) {
    document.getElementById("textarea1").value = document.getElementById(option_sel).innerHTML.trim();
    localStorage.setItem('txt1', document.getElementById("textarea1").value);
}

function branch_selection(btn_id) {
    var dept = document.getElementById(btn_id).innerHTML.trim();
    document.getElementById("textarea2").value = dept;
    document.getElementById("course").value = dept;
    localStorage.setItem('txt2', dept);
}

function class_selection(option_sel) {
    document.getElementById("textarea3").value = document.getElementById(option_sel).innerHTML.trim();
    localStorage.setItem('txt3', document.getElementById("textarea3").value);
}

function Person_selection(option_sel) {
    var role = document.getElementById(option_sel).innerHTML.trim();
    document.getElementById("textarea4").value = role;
    document.getElementById("dept_token").value = role;
    localStorage.setItem('txt4', role);

}

function User_status(option_sel) {
    var user = document.getElementById(option_sel).innerHTML.trim();
    document.getElementById("textarea5").value = user;
    localStorage.setItem('txt5', user);
    if (user == 'New User') {
        document.getElementById('action_text').value = 'Register';
        document.getElementById('action_text').disabled = false;
    }
    else if (user == 'Earlier User') {
        document.getElementById('action_text').value = 'Login';
        document.getElementById('action_text').disabled = false;
    }
}

function onpage_load() {   
    if (document.getElementById('action_text').value == 'Register' ||
            document.getElementById('action_text').value == 'Login') {
            document.getElementById('action_text').disabled = false;
        } else {
            document.getElementById("textarea1").value = localStorage.getItem('txt1');
            document.getElementById("textarea2").value = localStorage.getItem('txt2');
            document.getElementById("textarea3").value = localStorage.getItem('txt3');
            document.getElementById("textarea4").value = localStorage.getItem('txt4');
            document.getElementById("textarea5").value = localStorage.getItem('txt5');
            document.getElementById('action_text').disabled = false;
    }        
}

