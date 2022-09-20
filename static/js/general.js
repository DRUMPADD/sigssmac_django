let t_body = document.querySelector(".t_body");

let form_mant = document.querySelector(".form-mant");

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
    return data.msg;
}

async function showGeneralManteinment () {
    let gen_info = await getGeneralManteinment();
    let ar_gen = new Array(gen_info);
    let str_info = "";

    ar_gen[0].forEach(element => {
        if(element.length !== 0) {
            str_info += `
                <tr>
                    <td>${element[0] != null ? element[0] : ""}</td>
                    <td>${element[1] != null ? element[1] : ""}</td>
                    <td>${element[2] != null ? element[2] : ""}</td>
                    <td>${element[3] != null ? element[3] : ""}</td>
                    <td>${element[4] != null ? element[4] : ""}</td>
                    <td>${element[5] != null ? element[5] : ""}</td>
                    <td>${element[6] != null ? element[6] : ""}</td>
                    <td>${element[7] != null ? element[7] : ""}</td>
                    <td>${element[8] != null ? element[8] : "Sin fecha"}</td>
                    <td>${element[9] != null ? element[9] : 0}</td>
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

function createManteinment (elements) {
    let {item_sl, frec_, act_, fecha_cre, fecha_prox} = elements;
    console.log(item_sl);
    console.log(frec_);
    console.log(act_);
    console.log(fecha_cre);
    console.log(fecha_prox);
    // fetch("plataforma/general/crearGeneral", {
    //     method: 'POST',
    //     headers: {
    //         'Accept': 'application/json',
    //         'X-Requested-With': 'XMLHttpRequest',
    //         'X-CSRFToken': getCookie("csrftoken")
    //     },
    //     body: JSON.stringify({

    //     })
    // })
    // .then(res => {
    //     return res.json();
    // })
    // .then(async d => {
    //     Swal.fire({
    //         position: 'center',
    //         icon: d.status,
    //         title: d.msg,
    //         confirmButtonColor: '#19ec27',
    //         confirmButtonText: 'ACEPTAR',
    //     })
    //     showGeneralManteinment()
    // })
    // .catch(err => {
    //     console.log("Error:",err)
    //     Swal.fire({
    //         position: 'center',
    //         icon: "error",
    //         title: "Error al registrar los datos",
    //         confirmButtonColor: '#df1c11',
    //         confirmButtonText: 'ACEPTAR',
    //     })
    // })
}

function modifyManteinment () {
    fetch("plataforma/general/modificarGeneral", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie("csrftoken")
        },
        body: JSON.stringify({

        })
    })
    .then(res => {
        return res.json();
    })
    .then(async d => {
        console.log(d);
        showGeneralManteinment();
    })
    .catch(err => {
        console.log(err);
    })
}

form_mant.addEventListener("submit", (e) => {
    e.preventDefault();
    let arr_els = new Array();
    for(let i = 0; i < form_mant.elements.length; i++) {
        console.log("Elemento "+ form_mant.elements[i].name+":",form_mant.elements[i].value);
        arr_els.push(form_mant.elements[i].value);
    }

    createManteinment(
        {
            item_sl: arr_els[0], 
            frec_: arr_els[1], 
            act_: arr_els[2], 
            fecha_cre: arr_els[3], 
            fecha_prox: arr_els[4]
        }
    );
})