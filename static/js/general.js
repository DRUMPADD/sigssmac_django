let t_body = document.querySelector(".t_body");

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function getGeneralManteinment () {
    let response = await fetch("/plataforma/general/mostrarGeneral");
    let data = await response.json();
    console.log(data.msg);
    return data.msg;
}

async function showGeneralManteinment () {
    let gen_info = await getGeneralManteinment();
    console.log(gen_info);
    let ar_gen = new Array(gen_info);
    let str_info = "";

    ar_gen[0].forEach(element => {
        if(element.length !== 0) {
            str_info += `
                <tr>
                    <td>${element[0]}</td>
                    <td>${element[1]}</td>
                    <td>${element[2]}</td>
                    <td>${element[3]}</td>
                    <td>${element[4]}</td>
                    <td>${element[5]}</td>
                    <td>${element[6]}</td>
                    <td>${element[7]}</td>
                    <td>${element[8]}</td>
                    <td>${element[9]}</td>
                    <td><a href="#" class="details"><i class="fa-solid fa-book"></i></a></td>
                </tr>
            `;
        }
    });

    t_body.innerHTML = str_info;
}


window.addEventListener("DOMContentLoaded", () => {
    showGeneralManteinment();
})