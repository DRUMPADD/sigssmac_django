let sl_providers = document.querySelector(".sl_providers")
let form = document.querySelector(".form_create");
let btn = document.querySelector(".select_option");

let newProvBox = document.querySelector(".content-new-prov");
let prov_box = document.getElementById("provider-content");

if(prov_box.getElementsByClassName("id").length == 0) {
    btn.addEventListener("click", () => {
        if(sl_providers.value === "NUEVO") {
            newProvBox.style.display = "flex";
            newProvBox.style.visibility = "visible";
            newProvBox.style.opacity = 1;
        } else {
            newProvBox.style.display = "none";
            newProvBox.style.visibility = "hidden";
            newProvBox.style.opacity = 0;
        }
    })
    
    async function getProviders () {
        let response = await fetch("/plataforma/proveedor/mostrarProveedores");
        let data = await response.json();
        return data.msg;
    }
    
    async function showProviders () {
        let providers = await getProviders();
        let ar_prov = new Array(providers);
        let str_prov = "";
    
        str_prov += `<option selected disabled>--Seleccionar--</option>`
        
        ar_prov[0].forEach(element => {
            if(element.length !== 0) {
                str_prov += `
                <option value="${element[0]}">${element[1]}</option>
                `
            }
        });
        
        str_prov += `<option value="NUEVO">Nuevo proveedor</option>`
        
        sl_providers.innerHTML = str_prov;
    }

    window.addEventListener("DOMContentLoaded", () => {
        showProviders();
    })
}

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

function registerProvider(values) {
    fetch("/plataforma/proveedor/agregarProveedorAItem", {
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
    .then(async d => {
        Swal.fire({
            position: 'center',
            icon: d.status,
            title: d.msg,
            confirmButtonColor: '#19ec27',
            confirmButtonText: 'ACEPTAR',
        })
    })
    .catch(e => {
        console.log(e);
        Swal.fire({
            position: 'center',
            icon: "error",
            title: "Error al buscar actividad",
            confirmButtonColor: '#df1c11',
            confirmButtonText: 'ACEPTAR',
        })
    })
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    let ar_answers = new Array();
    if(form.elements[2].value != "--Seleccionar--" && form.elements[2].value == "NUEVO") {
        for(let i = 0; i < form.elements.length - 1; i++) {
            if(form.elements[i].type != "button" && form.elements[i].type != "submit") {
                ar_answers.push(form.elements[i].value)
            }
        }
    } else {
        for(let i = 0; i < form.elements.length - 6; i++) {
            if(form.elements[i].type != "button" && form.elements[i].type != "submit") {
                ar_answers.push(form.elements[i].value)
            }
        }
    }
    if(ar_answers.length > 3) {
        ar_answers.splice(2, 1)
        registerProvider({
            item_id: ar_answers[1],
            prov_id: ar_answers[2],
            p_nombre: ar_answers[3],
            numero_t: ar_answers[4],
            _email: ar_answers[5],
            country: ar_answers[6],
        })
    } else {
        registerProvider({
            item_id: ar_answers[1],
            prov_id: ar_answers[2]
        })
    }
})


let btn_mod = document.querySelector(".select-mod");
let btn_del = document.querySelector(".select-del");
let i_del = document.querySelector(".del");
let inputs_ = document.querySelectorAll(".input_prov");

btn_mod.addEventListener("click", () => {
    inputs_.forEach(element => {
        element.removeAttribute("disabled");
    })
    i_del.classList.remove("fa-trash-can");
    i_del.classList.add("fa-x");
})

btn_del.addEventListener("click", () => {
    inputs_.forEach(element => {
        element.setAttribute("disabled", "");
    })
    i_del.classList.remove("fa-x");
    i_del.classList.add("fa-trash-can");
})