window.addEventListener('load',()=>{

    const token_element = document.getElementById('token_key');
    const xhttp = new XMLHttpRequest();
    token_element.addEventListener('onchange',()=>{
         let xhttp = new XMLHttpRequest();
        const tokenValue = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        let data_in = new FormData();
        data_in.append("username",username.value);
        data_in.append("email",email.value);
        data_in.append("password",password.value);
        data_in.append("password_confirmation",password_confirmation.value);
        xhttp.open("POST", "/sign-up/", false);
        xhttp.onreadystatechange = () => {
            if (xhttp.readyState == 4 && xhttp.status == 200) {
                //loading_spinner.classList.toggle('play');
                        if(JSON.parse(xhttp.responseText)['is_valid']){
                        }
                 }
        };
        xhttp.setRequestHeader('X-CSRFToken', tokenValue);  /*X-CSRFToken: tokenValue*/
        xhttp.send(data_in);
        const data_out = JSON.parse(xhttp.responseText);
        console.log(data_out)
    });
});