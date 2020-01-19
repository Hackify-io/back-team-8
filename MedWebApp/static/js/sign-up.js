window.addEventListener('load',()=>{
    const typeEvent = 'ontouchstart' in window ? 'touchstart' : 'click';

    const username_element = document.getElementById('username'),
          email_element = document.getElementById('email'),
          password_element = document.getElementById('password'),
          password_element_confirmation = document.getElementById('password_confirmation');

    const xhttp = new XMLHttpRequest();
     document.getElementById('submit-button').addEventListener(typeEvent,()=>{
            if(password_element.value === password_element_confirmation.value) {
                const tokenValue = document.getElementsByName('csrfmiddlewaretoken')[0].value;
                let data_in = new FormData();
                data_in.append("username", username_element.value);
                data_in.append("email", email_element.value);
                data_in.append("password", password_element.value);
                data_in.append("password_confirmation",password_element_confirmation.value);
                xhttp.open("POST", "/signup/", false);
                xhttp.onreadystatechange = () => {
                    if (xhttp.readyState == 4 && xhttp.status == 200) {
                        //loading_spinner.classList.toggle('play');
                        if (JSON.parse(xhttp.responseText)['is_valid']) {
                            alert("WELCOME")
                        }
                    }
                };
                xhttp.setRequestHeader('X-CSRFToken', tokenValue);  /*X-CSRFToken: tokenValue*/
                xhttp.send(data_in);
                const data_out = JSON.parse(xhttp.responseText);
            }
     });
});