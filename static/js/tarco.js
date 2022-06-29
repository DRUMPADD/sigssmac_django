const tb_info = document.querySelector("#info");
let sl_condicion = document.querySelector(".condicion");
var select_con = document.createElement("select");
select_con.name = "sl_cond";
select_con.className = "condicion form-select";
var values = ["Malo", "Regular", "Bueno"];


var table = document.getElementById("tb_items"), rIndex;
let btnEnviar = document.getElementById("btnEnviar");
let btnLimpiar = document.getElementById("btnLimpiar");

// Inputs
let inp_id = document.querySelector(".id_");
let inp_nombre = document.querySelector(".nombre");
let inp_car = document.querySelector(".caracteristicas");
let inp_ubi = document.querySelector(".ubicacion");
let inp_frec = document.querySelector(".frec");
let inp_fec_ins = document.querySelector(".fecha_ins");
let inp_conds = document.querySelector(".condiciones");
let inp_fec_col = document.querySelector(".fecha_col");
let inp_fec_reem = document.querySelector(".fecha_reem");
let inp_cond = document.querySelector(".sl_condicion");

let formulario = new FormData(document.getElementById("form_item"));
let form_r = document.getElementById("form_item");


function reload(key){
    var container = document.getElementById(key);
    var content = container.innerHTML;
    container.innerHTML= content; 
}

for(const val of values) {
    var op = document.createElement("option");
    op.value = val;
    op.text = val.charAt(0).toUpperCase() + val.slice(1);
    select_con.appendChild(op);
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

async function getItems2() {
    const response = await fetch("/getInfo")
    const data = await response.json();
    
    
    const items = data.info;

    items.forEach(element => {
        const tr = document.createElement("tr");

        const f_ac = element[5] != null ? element[5]: '';
        const fech_ac_formato = f_ac.split('-');
        const fecha_act = new Date(fech_ac_formato[0], fech_ac_formato[1], fech_ac_formato[2]);
        const cal_fech_ac = Math.round((fecha_act.getTime() - Date.now())/ (1000*60*60*24));
        tr.innerHTML += `
            <td>${element[0]}</td>
            <td>${element[1]}</td>
            <td>${element[2]}</td>
            <td>${element[3]}</td>
            <td>${element[4]}</td>
            <td class='bg-${cal_fech_ac > element[4] ? 'primary': 'dark '} text-white'>${element[5] == null ? '': element[5]}</td>
            <td>${element[6]}</td>
            <td>${element[7] == null ? '': element[7]}</td>
            <td>${element[8] == null ? '': element[8]}</td>
            <td class='bg-${element[9] == 'Malo' ? "primary": element[9] == 'Regular' ? "warning": "success"}'>${element[9]}</td>
        `;

        tb_info.appendChild(tr);
    });
    
    for(let i = 1; i < table.rows.length; i++) {
        if(table.rows[i].cells != 10) {
            table.rows[i].onclick = function(e) {
                inp_id.value = this.cells[0].innerHTML;
                inp_id.setAttribute("disabled", "");
                inp_nombre.value = this.cells[1].innerHTML;
                inp_car.value = this.cells[2].innerHTML;
                inp_ubi.value = this.cells[3].innerHTML;
                inp_frec.value = this.cells[4].innerHTML;
                inp_fec_ins.value = this.cells[5].innerHTML;
                inp_conds.value = this.cells[6].innerHTML;
                inp_fec_col.value = this.cells[7].innerHTML;
                inp_fec_reem.value = this.cells[8].innerHTML;
                inp_cond.value = this.cells[9].innerHTML;

                btnLimpiar.removeAttribute("disabled");
            }
        }
    }
}

window.addEventListener("DOMContentLoaded", () => {
    getItems2();
})

function validar() {
    return inp_id.value != '' && inp_nombre.value != '' && inp_car.value != null && inp_ubi.value != '' && inp_frec.value != '' && inp_fec_ins.value != '' && inp_conds.value != '' && inp_fec_col.value != '' && inp_fec_reem.value != '' && inp_cond.value != undefined;
}

function enviar() {
    fetch("/agregarItem", {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: JSON.stringify({
            id: inp_id.value,
            nombre: inp_nombre.value,
            car: inp_car.value,
            ubi: inp_ubi.value,
            frec: inp_frec.value,
            fec_ins: inp_fec_ins.value,
            conds: inp_conds.value,
            fec_col: inp_fec_col.value,
            fec_reem: inp_fec_reem.value,
            cond: inp_cond.value,
        })
    })
    .then(res => {
        return res.json();
    })
    .then(data => {
        alert(data.msg);
    })
    .catch(err => {
        return
    })

    console.log(formulario);
}

function limpiarForm() {
    inp_id.value = "";
    inp_nombre.value = "";
    inp_car.value = "";
    inp_ubi.value = "";
    inp_frec.value = "";
    inp_fec_ins.value = "";
    inp_conds.value = "";
    inp_fec_col.value = "";
    inp_fec_reem.value = "";
    inp_cond.value = "";
}


btnEnviar.addEventListener("click", (e) => {
    e.preventDefault();
    if(validar()) {
        enviar();
        form_r.reset();
        reload("tb_items");
    } else {
        alert("Debe llenar el formulario")
    }

})

btnLimpiar.addEventListener("click", () => {
    limpiarForm();
    btnLimpiar.setAttribute("disabled", "");
    inp_id.removeAttribute("disabled");
})