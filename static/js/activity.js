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
let t_body = document.getElementById("activities");
// let btnSend = document.getElementById("send");


let form = document.querySelector("#form_act");

// ?? Conseguir datos de tabla actividades desde servidor
async function getActivities() {
    let response = await fetch("/activities/getActivities");
    let data = await response.json();
    return data;
}

// ?? Colocar datos obtenidos en tabla
async function showActivities() {
    let activities = await getActivities();
    let arr = new Array(activities);

    let str_datos = "";
    arr.forEach(el => {
        str_datos += `
            <tr>
                <td>${el.codigo}</td>
                <td>${el.n_actividad}</td>
                <td>${el.descripcion}</td>
            </tr>
        `;
    })

    t_body.innerHTML = str_datos;
}

// ?? Mostrar datos cuando el contenido esté cargado
window.addEventListener("DOMContentLoaded", () => {
    showActivities();
})


function checkId (inputId) {
    return inputId === '';
}

function checkName(name) {
    return name === '';
}

function checkDescription(descrip) {
    return descrip === '';
}

function createActivity () {
    fetch("/plataforma/actividades/crear_actividad", {
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            cod_act: form["id"].value,
            name_act: form["name_act"].value,
            desc: form["description"].value,
        })
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        showActivities();
        Swal.fire({
            position: 'center',
            icon: data.status,
            title: data.msg,
            confirmButtonColor: '#19ec27',
            confirmButtonText: 'ACEPTAR',
        })
    })
    .catch(e => {
        console.log(e);
    })
}

form.addEventListener("submit", (e) => {
    e.preventDefault();

    let isIdValid = checkId(e.target.id.value),
        isNameValid = checkName(e.target.name_act.value),
        isDescriptionValid = checkDescription(e.target.description.value);
    let isFormValid = isIdValid && isNameValid && isDescriptionValid;
    if(!isFormValid) {
        createActivity();
    } else {
        Swal.fire({
            position: 'center',
            icon: 'warning',
            title: 'Todos los campos son requeridos',
            confirmButtonColor: '#d33',
            confirmButtonText: 'ACEPTAR',
        })
    }
})