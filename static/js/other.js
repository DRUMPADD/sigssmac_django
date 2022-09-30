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
let boxForm = document.querySelectorAll(".update_hidden");
let btnShowForm = document.querySelectorAll(".btn");
let btnsClose = document.querySelectorAll(".btnClose");
let formSelected = document.querySelectorAll(".form_update");
let formProvider = document.querySelector(".form_update_prov");
let tBody = document.querySelectorAll(".t_body");


btnShowForm.forEach((element, index) => {
    element.addEventListener("click", () => {
        boxForm[index].style.visibility = "visible";
        boxForm[index].style.opacity = 1;
    })

})

function hideForm() {
    formSelected.forEach((element) => {
        element.reset();
        element["option"].value = "AGREGAR";
    })
    console.log("Reseteado");
}

btnsClose.forEach((el, i) => {
    el.addEventListener("click", () => {
        boxForm[i].style.visibility = "hidden";
        boxForm[i].style.opacity = 0;
        hideForm();
    })
})


formProvider.addEventListener("submit", (e) => {
    e.preventDefault();
    let option_selected = formProvider["option"].value;
    if(option_selected == "AGREGAR") {
        save_data("PROVEEDOR", {
            cod_prov: formProvider["id"].value,
            nombre: formProvider["name_p"].value,
            telefono: formProvider["phone_number"].value,
            email: formProvider["email"].value,
            pais: formProvider["country"].value,
        }) 
    } else {
        modify_data("PROVEEDOR", {
            cod_prov: formProvider["id"].value,
            nombre: formProvider["name_p"].value,
            telefono: formProvider["phone_number"].value,
            email: formProvider["email"].value,
            pais: formProvider["country"].value,
        })
    }

});

formSelected.forEach((form, i) => {
    if(i != 0) {
        form.addEventListener("submit", (e) => {
            e.preventDefault();
            let option_selected = form["option"].value;
            if(option_selected == "AGREGAR") {
                save_data(form["sl_where"].value, {
                    name: form["name"].value,
                }) 
            } else {
                modify_data(form["sl_where"].value, {
                    id: form["id"].value,
                    name: form["name"].value,
                })
            }
        })
    }
})

// ?? Providers 
async function getProviders() {
    let response = await fetch("/plataforma/proveedor/mostrarProveedores");
    let d = await response.json();
    return d.msg;
}

async function showProviders() {
    let providers = await getProviders();
    let ar_prov = new Array(providers);
    let str_info = "";
    ar_prov[0].forEach(el => {
        str_info += `
            <tr>
                <td>${el[0]}</td>
                <td>${el[1]}</td>
                <td>${el[2]}</td>
                <td>${el[3]}</td>
                <td>${el[4]}</td>
                <td class="flex-tr">
                    <a data-title="Modificar" class="btn-mod-prov">
                        <i class="i-mod fa-solid fa-pen-to-square"></i>
                    </a>
                    <a data-title="Eliminar" class="btn-del-prov">
                        <i class="i-del fa-solid fa-trash-can"></i>
                    </a>
                </td>
            </tr>
        `;
    })

    tBody[0].innerHTML = str_info;
    let btnMod = document.querySelectorAll(".btn-mod-prov");
    btnMod.forEach(element => {
        element.addEventListener("click", () => {
            const parentTR = element.parentElement.parentElement;
            boxForm[0].style.visibility = "visible";
            boxForm[0].style.opacity = 1;
            console.log(boxForm[0]);
            formProvider["id"].value = parentTR.getElementsByTagName("td")[0].innerText;
            formProvider["name_p"].value = parentTR.getElementsByTagName("td")[1].innerText;
            formProvider["phone_number"].value = parentTR.getElementsByTagName("td")[2].innerText;
            formProvider["email"].value = parentTR.getElementsByTagName("td")[3].innerText;
            formProvider["country"].value = parentTR.getElementsByTagName("td")[4].innerText;
            formProvider["option"].value = "MODIFICAR";
        })
    })
    let btnDel = document.querySelectorAll(".btn-del-prov");
    btnDel.forEach(element => {
        element.addEventListener("click", () => {
            const parentTR = element.parentElement.parentElement;
            delete_data("PROVEEDOR", parentTR.getElementsByTagName("td")[0].innerText);
        })
    })
}

// ?? Frequences
async function getFrequences() {
    let response = await fetch("/plataforma/frecuencia/mostrarFrecuencias");
    let d = await response.json();
    return d.msg;
}

async function showFrequences() {
    let frequences = await getFrequences();
    console.log(frequences);
    let ar_prov = new Array(frequences);
    let str_info = "";
    ar_prov[0].forEach(el => {
        str_info += `
            <tr>
                <td>${el[0]}</td>
                <td>${el[1]}</td>
                <td class="flex-tr">
                    <a data-title="Modificar" class="btn-mod-freq">
                        <i class="i-mod fa-solid fa-pen-to-square"></i>
                    </a>
                    <a data-title="Eliminar" class="btn-del-freq">
                        <i class="i-del fa-solid fa-trash-can"></i>
                    </a>
                </td>
            </tr>
        `;
    })

    tBody[1].innerHTML = str_info;
    let btnMod = document.querySelectorAll(".btn-mod-freq");
    btnMod.forEach(element => {
        element.addEventListener("click", () => {
            const parentTR = element.parentElement.parentElement;
            boxForm[1].style.visibility = "visible";
            boxForm[1].style.opacity = 1;
            formSelected[1]["id"].value = parentTR.getElementsByTagName("td")[0].innerText;
            formSelected[1]["name"].value = parentTR.getElementsByTagName("td")[1].innerText;
            formSelected[1]["option"].value = "MODIFICAR";
        })
    })
    let btnDel = document.querySelectorAll(".btn-del-freq");
    btnDel.forEach(element => {
        element.addEventListener("click", () => {
            const parentTR = element.parentElement.parentElement;
            delete_data(formSelected[1]["sl_where"].value, parentTR.getElementsByTagName("td")[0].innerText);
        })
    })
}


// ?? Novelties
async function getNovelties() {
    let response = await fetch("/plataforma/novedad/mostrarNovedades");
    let d = await response.json();
    return d.msg;
}

async function showNovelties() {
    let novelties = await getNovelties();
    let ar_prov = new Array(novelties);
    let str_info = "";
    ar_prov[0].forEach(el => {
        str_info += `
            <tr>
                <td>${el[0]}</td>
                <td>${el[1]}</td>
                <td class="flex-tr">
                    <a data-title="Modificar" class="btn-mod-nov">
                        <i class="i-mod fa-solid fa-pen-to-square"></i>
                    </a>
                    <a data-title="Eliminar" class="btn-del-nov">
                        <i class="i-del fa-solid fa-trash-can"></i>
                    </a>
                </td>
            </tr>
        `;
    })

    tBody[2].innerHTML = str_info;
    let btnMod = document.querySelectorAll(".btn-mod-nov");
    btnMod.forEach(element => {
        element.addEventListener("click", () => {
            const parentTR = element.parentElement.parentElement;
            boxForm[2].style.visibility = "visible";
            boxForm[2].style.opacity = 1;
            formSelected[2]["id"].value = parentTR.getElementsByTagName("td")[0].innerText;
            formSelected[2]["name"].value = parentTR.getElementsByTagName("td")[1].innerText;
            formSelected[2]["option"].value = "MODIFICAR";
        })
    })
    let btnDel = document.querySelectorAll(".btn-del-nov");
    btnDel.forEach(element => {
        element.addEventListener("click", () => {
            const parentTR = element.parentElement.parentElement;
            delete_data(formSelected[2]["sl_where"].value, parentTR.getElementsByTagName("td")[0].innerText);
        })
    })
}

// ?? Fail modes
async function getModes() {
    let response = await fetch("/plataforma/modoFallo/mostrarModos");
    let d = await response.json();
    console.log(d.msg);
    return d.msg;
}

async function showModes() {
    let modes = await getModes();
    console.log(modes);
    let ar_prov = new Array(modes);
    let str_info = "";
    ar_prov[0].forEach(el => {
        str_info += `
            <tr>
                <td>${el[0]}</td>
                <td>${el[1]}</td>
                <td class="flex-tr">
                    <a data-title="Modificar" class="btn-mod-fail">
                        <i class="i-mod fa-solid fa-pen-to-square"></i>
                    </a>
                    <a data-title="Eliminar" class="btn-del-fail">
                        <i class="i-del fa-solid fa-trash-can"></i>
                    </a>
                </td>
            </tr>
        `;
    })

    tBody[3].innerHTML = str_info;
    let btnMod = document.querySelectorAll(".btn-mod-fail");
    btnMod.forEach(element => {
        element.addEventListener("click", () => {
            const parentTR = element.parentElement.parentElement;
            boxForm[3].style.visibility = "visible";
            boxForm[3].style.opacity = 1;
            formSelected[3]["id"].value = parentTR.getElementsByTagName("td")[0].innerText;
            formSelected[3]["name"].value = parentTR.getElementsByTagName("td")[1].innerText;
            formSelected[3]["option"].value = "MODIFICAR";
        })
    })
    let btnDel = document.querySelectorAll(".btn-del-fail");
    btnDel.forEach(element => {
        element.addEventListener("click", () => {
            const parentTR = element.parentElement.parentElement;
            delete_data(formSelected[3]["sl_where"].value, parentTR.getElementsByTagName("td")[0].innerText);
        })
    })
}

window.addEventListener("DOMContentLoaded", () => {
    showProviders();
    showFrequences();
    showNovelties();
    showModes();
})


function reloadTag(where) {
    hideForm();
    if(where == 'PROVEEDOR') {
        showProviders();
    } else if (where == 'FRECUENCIA') {
        showFrequences();
    } else if (where == 'NOVEDAD') {
        showNovelties();
    } else {
        showModes();
    }
}

// ?? Post functions
function save_data(where, values) {
    let url = where == 'PROVEEDOR' ? "/plataforma/proveedor/agregarProveedor" : where == 'FRECUENCIA' ? "/plataforma/frecuencia/crearFrecuencia" : where == 'NOVEDAD' ? "/plataforma/novedad/crearNovedad" : "/plataforma/modoFallo/crearModo";
    fetch(url, {
        method: 'POST',
        headers: {
            "Accept": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify(values)
    })
    .then(res => {
        return res.json();
    })
    .then(d => {
        reloadTag(where);
        Swal.fire({
            position: 'center',
            icon: d.status,
            title: d.msg,
            confirmButtonColor: '#19ec27',
            confirmButtonText: 'ACEPTAR',
        })
    })
    .catch(er => {
        Swal.fire({
            position: 'center',
            icon: "error",
            title: "Error al hacer el registro",
            confirmButtonColor: '#19ec27',
            confirmButtonText: 'ACEPTAR',
        })
    })
}

function modify_data(where, values) {
    let url = where == 'PROVEEDOR' ? "/plataforma/proveedor/modificarProveedor" : where == 'FRECUENCIA' ? "/plataforma/frecuencia/modificarFrecuencia" : where == 'NOVEDAD' ? "/plataforma/novedad/modificarNovedad" : "/plataforma/modoFallo/modificarModo";
    fetch(url, {
        method: 'POST',
        headers: {
            "Accept": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify(values)
    })
    .then(res => {
        return res.json();
    })
    .then(d => {
        reloadTag(where);
        Swal.fire({
            position: 'center',
            icon: d.status,
            title: d.msg,
            confirmButtonColor: '#19ec27',
            confirmButtonText: 'ACEPTAR',
        })
    })
    .catch(er => {
        Swal.fire({
            position: 'center',
            icon: "error",
            title: "Error al hacer el registro",
            confirmButtonColor: '#19ec27',
            confirmButtonText: 'ACEPTAR',
        })
    })
}

function delete_data(where, value) {
    let url = where == 'PROVEEDOR' ? "/plataforma/proveedor/eliminarProveedor" : where == 'FRECUENCIA' ? "/plataforma/frecuencia/eliminarFrecuencia" : where == 'NOVEDAD' ? "/plataforma/novedad/eliminarNovedad" : "/plataforma/modoFallo/eliminarModo";
    Swal.fire({
        title: "¿Está seguro de eliminar este registro?",
        text: "Esta acción no podrá ser revertida",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminar',
        cancelButtonText: 'Cancelar',
    }).then(result => {
        if(result.isConfirmed) {
            fetch(url, {
                method: 'POST',
                headers: {
                    "Accept": "application/json",
                    "X-Requested-With": "XMLHttpRequest",
                    "X-CSRFToken": getCookie("csrftoken")
                },
                body: JSON.stringify({
                    id: value
                })
            })
            .then(res => {
                return res.json();
            })
            .then(d => {
                reloadTag(where);
                Swal.fire({
                    position: 'center',
                    icon: d.status,
                    title: d.msg,
                    confirmButtonColor: '#19ec27',
                    confirmButtonText: 'ACEPTAR',
                })
            })
            .catch(er => {
                Swal.fire({
                    position: 'center',
                    icon: "error",
                    title: "Error al eliminar el registro",
                    confirmButtonColor: '#19ec27',
                    confirmButtonText: 'ACEPTAR',
                })
            })
        }
    })
}