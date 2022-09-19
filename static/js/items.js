let box_update_form = document.getElementById("content-hidden");
let form_update = document.querySelector(".form_update");
let btnClose = document.querySelector(".btnClose");
let t_body = document.getElementById("items");
let form = document.querySelector("#form_item");


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

function hideUpdateForm() {
    box_update_form.style.visibility = "hidden";
    box_update_form.style.opacity = 0;
    form_update.reset();
}

btnClose.addEventListener("click", () => {
    hideUpdateForm();
});

async function getItems() {
    let response = await fetch("/plataforma/equipo/mostrarItems");
    let data = await response.json();
    return data.msg;
}

async function showItems() {
    let items = await getItems();
    let ar_items = new Array(items);
    let str_items = "";

    ar_items[0].forEach(element => {
        if(element.length !== 0) {
            str_items += `
                <tr>
                    <td>${element[0]}</td>
                    <td>${element[1]}</td>
                    <td>${element[2]}</td>
                    <td style="display: flex; justify-content: center;">
                        <a href="/plataforma/equipo/${element[0]}" class="btn btn-see-charac">
                            <i class="fa-regular fa-file-lines"></i>
                        </a>
                        <a class="btn btn-modificar" href="#content-hidden">
                            <i class="fa-solid fa-pencil"></i>
                        </a>
                        <a class="btn btn-eliminar" href="#content-hidden">
                            <i class="fa-solid fa-trash-can"></i>
                        </a>
                    </td>
                </tr>
            `;
        }
    });

    t_body.innerHTML = str_items;
    let btns_update = document.querySelectorAll(".btn-modificar");
    for(let i = 0; i < btns_update.length; i++) {
        btns_update[i].addEventListener("click", (e) => {
            box_update_form.style.visibility = "visible";
            box_update_form.style.opacity = 1;
            const parentTR = btns_update[i].parentElement.parentElement;
            form_update["id_"].value = parentTR.getElementsByTagName("td")[0].innerText;
            form_update["new_name"].value = parentTR.getElementsByTagName("td")[1].innerText;
            form_update["new_stuck"].value = parentTR.getElementsByTagName("td")[2].innerText;
        });
    }
}

window.addEventListener("DOMContentLoaded", () => {
    showItems();
})

function checkId (inputId) {
    return inputId === '';
}

function checkName(name) {
    return name === '';
}

function checkQuantity(quantity) {
    return quantity === null || quantity === undefined;
}

function createItem () {
    fetch("/plataforma/equipo/registrarItem", {
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            cod_item: form["cod_item"].value,
            name_item: form["name_item"].value,
            quantity: form["quantity_item"].value
        })
    })
    .then(response => {
        let res = response.json();
        console.log(res);
        return res;
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
        showItems();
    })
    .catch(e => {
        console.log("Error:",e)
        Swal.fire({
            position: 'center',
            icon: "error",
            title: "Error al registrar los datos",
            confirmButtonColor: '#df1c11',
            confirmButtonText: 'ACEPTAR',
        })
    })
}

function modifyItem () {
    fetch("/plataforma/equipo/modificarItem", {
        method: 'POST',
        mode: 'same-origin',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            id_: form_update["id_"].value,
            new_name: form_update["new_name"].value,
            new_stuck: form_update["new_stuck"].value,
        })
    })
    .then(response => {
        return response.json();
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
        showItems();
    })
    .catch(e => {
        console.log("Error:",e)
        Swal.fire({
            position: 'center',
            icon: "error",
            title: "Error al modificar los datos",
            confirmButtonColor: '#df1c11',
            confirmButtonText: 'ACEPTAR',
        })
    })
}

form.addEventListener("submit", (e) => {
    e.preventDefault();

    let isIdValid = checkId(e.target.cod_item.value),
        isNameValid = checkName(e.target.name_item.value),
        isDescriptionValid = checkQuantity(e.target.quantity_item.value);
    let isFormValid = isIdValid && isNameValid && isDescriptionValid;
    if(!isFormValid) {
        createItem();
    } else {
        Swal.fire({
            position: 'center',
            icon: 'warning',
            title: 'Todos los campos son requeridos',
            confirmButtonColor: '#d33',
            confirmButtonText: 'Accept',
        })
    }
})

form_update.addEventListener("submit", (e) => {
    e.preventDefault();

    let isIdValid = checkId(e.target.id_.value),
        isNameValid = checkName(e.target.new_name.value),
        isDescriptionValid = checkQuantity(e.target.new_stuck.value);
    let isFormValid = isIdValid && isNameValid && isDescriptionValid;
    if(!isFormValid) {
        modifyItem();
    } else {
        Swal.fire({
            position: 'center',
            icon: 'warning',
            title: 'Todos los campos son requeridos',
            confirmButtonColor: '#d33',
            confirmButtonText: 'Accept',
        })
    }
})