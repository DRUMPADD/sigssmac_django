let box_update_form = document.getElementById("content-hidden");
let form_update = document.querySelector(".form_update");
let btnClose = document.querySelector(".btnClose");
let t_body = document.getElementById("items");
let form = document.querySelector("#form-item");

btnClose.addEventListener("click", () => {
    box_update_form.style.visibility = "hidden";
    box_update_form.style.opacity = 0;
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
        if(el.length !== 0) {
            str_items += `
                <tr>
                    <td>${element[0]}</td>
                    <td>${element[1]}</td>
                    <td>${element[2]}</td>
                    <td style="display: flex; justify-content: center;">
                        <a href="plataforma/equipo/${element[0]}" class="btn btn-see-charac">
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
            form_update["name_before"].value = parentTR.getElementsByTagName("td")[1].innerText;
            form_update["stuck_before"].value = parentTR.getElementsByTagName("td")[2].innerText;
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
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            cod_item: form["id_item"].value,
            name_item: form["name_item"].value,
            quantity: form["quantity_item"].value,
        })
    })
    .then(response => {
        return response.json();
    })
    .then(data => {
        showActivities();
        console.log(data);
    })
    .catch(e => {
        console.log(e);
    })
}

form.addEventListener("submit", (e) => {
    e.preventDefault();

    let isIdValid = checkId(e.target.id_item.value),
        isNameValid = checkName(e.target.name_item.value),
        isDescriptionValid = checkDescription(e.target.quantity_item.value);
    let isFormValid = isIdValid && isNameValid && isDescriptionValid;
    if(!isFormValid) {
        createActivity();
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