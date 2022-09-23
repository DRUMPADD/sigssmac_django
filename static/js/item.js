let sl_providers = document.querySelector(".sl_providers")
let form = document.querySelector(".form_create");
let box_update_form = document.getElementById("content-hidden");
let btnClose = document.querySelector(".btnClose");
let sl_prov = document.querySelector(".sl_providers");
let btn = document.querySelector(".select_option");
let selectBox = document.querySelector(".select_box");

let newProvBox = document.querySelector(".content-new-prov");
let prov_box = document.getElementById("provider-content");

let btnAppearForm = document.querySelector(".link-add");

btnAppearForm.addEventListener("click", () => {
    box_update_form.style.visibility = "visible";
    box_update_form.style.opacity = 1;
})

if(prov_box.getElementsByClassName("id").length == 0) {
    async function getProviders () {
        let response = await fetch("/plataforma/proveedor/mostrarProveedores");
        let data = await response.json();
        return data.msg;
    }
    
    async function showProviders () {
        let providers = await getProviders();
        let ar_prov = new Array(providers);
        let str_prov = "";
    
        str_prov += `<option selected disabled>--Seleccionar</option>`
        
        ar_prov[0].forEach(element => {
            if(element.length !== 0) {
                str_prov += `
                <option value="${element[0]}">${element[1]}</option>
                `
            }
        });
        
        str_prov += `<option value="NUEVO">Nuevo proveedor</option>`
        
        sl_providers.innerHTML = str_prov;
    
        btn.addEventListener("click", () => {
            if(sl_prov.value == "NUEVO") {
                console.log(sl_prov.value);
                selectBox.style.display == 'none';
                selectBox.style.visibility == 'hidden';
                selectBox.style.opacity == 0;
                newProvBox.style.display = "flex";
                newProvBox.style.visibility = "visible";
                newProvBox.style.opacity = 1;
            }
        })
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



function hideUpdateForm() {
    box_update_form.style.visibility = "hidden";
    box_update_form.style.opacity = 0;
    form.reset();
    if(prov_box.getElementsByClassName("id").length == 0) {
        selectBox.style.display == 'flex';
        selectBox.style.visibility == 'visible';
        selectBox.style.opacity == 1;
        if(newProvBox.style.visibility == 'visible') {
            newProvBox.style.display == 'none';
            newProvBox.style.visibility == 'hidden';
            newProvBox.style.opacity == 0;
        }
    }
}

btnClose.addEventListener("click", () => {
    hideUpdateForm();
});

form.addEventListener("submit", (e) => {
    e.preventDefault();

    for(let i = 0; i < form.elements.length - 1; i++) {
        console.log(form.elements[i].name + ":",form.elements[i].value);
    }
})