let box_update_form = document.getElementById("content-hidden");
let form_update = document.querySelector(".form_update");
let btnClose = document.querySelector(".btnClose");

function hideUpdateForm() {
    box_update_form.style.visibility = "hidden";
    box_update_form.style.opacity = 0;
    form_update.reset();
}

btnClose.addEventListener("click", () => {
    hideUpdateForm();
});
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
    let response = await fetch("/plataforma/actividades/motrarActividad");
    let data = await response.json();
    return data.msg;
}

// ?? Colocar datos obtenidos en tabla
async function showActivities() {
    let activities = await getActivities();
    let arr = new Array(activities);
    let str_datos = "";
    arr[0].forEach(el => {
        if(el.length !== 0) {
            str_datos += `
                <tr>
                    <td>${el[0]}</td>
                    <td>${el[1]}</td>
                    <td>${el[2]}</td>
                    <td>
                        <a class="btn-modificar" href="#content-hidden">
                            <i class="fa-solid fa-pencil"></i>
                        </a>
                    </td>
                    <td>
                        <a class="btn-eliminar" href="#">
                            <i class="fa-solid fa-trash-can"></i>
                        </a>
                    </td>
                </tr>
            `;
        }
    })
    t_body.innerHTML = str_datos;

    let btns_update = document.querySelectorAll(".btn-modificar");
    for(let i = 0; i < btns_update.length; i++) {
        btns_update[i].addEventListener("click", (e) => {
            box_update_form.style.visibility = "visible";
            box_update_form.style.opacity = 1;
            const parentTR = btns_update[i].parentElement.parentElement;
            form_update["id_act"].value = parentTR.getElementsByTagName("td")[0].innerText;
            form_update["new_name"].value = parentTR.getElementsByTagName("td")[1].innerText;
        });
    }
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
        console.log(response);
        return response.json();
    })
    .then(async data => {
        console.log(data);
        showActivities();
        await Swal.fire({
            position: 'center',
            icon: data.status,
            title: data.msg,
            confirmButtonColor: '#19ec27',
            confirmButtonText: 'ACEPTAR',
        })
    })
    .catch(e => {
        Swal.fire({
            position: 'center',
            icon: e.status,
            title: e.msg,
            confirmButtonColor: '#df1c11',
            confirmButtonText: 'ACEPTAR',
        })
    })
}

function modifyActivity() {
    fetch("/plataforma/actividades/modificarActividad", {
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            cod_act: form_update["id_act"].value,
            newName: form_update["new_name"].value,
        })
    })
    .then(result => {
        console.log(result);
        return result.json();
    })
    .then(async data => {
        console.log(data);
        await Swal.fire({
            position: 'center',
            icon: data.status,
            title: data.msg,
            confirmButtonColor: '#19ec27',
            confirmButtonText: 'ACEPTAR',
        })
        hideUpdateForm();
        showActivities();
    })
    .catch(e => {
        Swal.fire({
            position: 'center',
            icon: e.status,
            title: e.msg,
            confirmButtonColor: '#df1c11',
            confirmButtonText: 'ACEPTAR',
        })
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

form_update.addEventListener("submit", (e) => {
    e.preventDefault();
    let validForm = e.target.id_act.val !== '' && e.target.new_name.val !== '';
    if(validForm) {
        modifyActivity();
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