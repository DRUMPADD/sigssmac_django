let t_body = document.querySelector(".t_body");
let form = document.querySelector(".form_manteinment")
let form_update = document.querySelector(".form_update")
let box_update_form = document.getElementById("content-hidden");
let btnClose = document.querySelector(".btnClose");

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

async function getCorMant () {
    let res = await fetch("/plataforma/correctivo/mostrarCorrectivo");
    let d = await res.json();
    return d.msg;
}


async function showCorMant () {
    let cor_mant = await getCorMant();
    let ar_cor_mant = new Array(cor_mant);
    let str_mant = "";

    ar_cor_mant[0].forEach(element => {
        if(element.length !== 0) {
            str_mant += `
                <tr>
                    <td>${element[1] != null ? element[1] : ""}</td>
                    <td>${element[2] != null ? element[2] : ""}</td>
                    <td>${element[3] != null ? element[3] : ""}</td>
                    <td>${element[4] != null ? element[4] : ""}</td>
                    <td>${element[5] != null ? element[5] : ""}</td>
                    <td>${element[6] != null ? element[6] : ""}</td>
                    <td>${element[7] != null ? element[7] : ""}</td>
                    <td>${element[8] != null ? element[8] : ""}</td>
                    <td>${element[9] != null ? element[9] : ""}</td>
                    <td>${element[10] != null ? element[10] : ""}</td>
                    <td>${element[11] != null ? element[11] : ""}</td>
                </tr>
            `
        }
    });

    t_body.innerHTML = str_mant;
}

window.addEventListener("DOMContentLoaded", () => {
    showCorMant();
})

function checkData (value_) {
    return value_ != "" || value_ != null || value_ != undefined;
}

function createManteinment (data_) {
    let { item, ubicacion, novedad, fail, report, rec_date, days, notes } = data_;

    console.log(data_);
    console.log(item);
    console.log(ubicacion);
    console.log(novedad);
    console.log(fail);
    console.log(report);
    console.log(rec_date);
    console.log(days);
    console.log(notes);
    
}

function modifyManteinment (data_) {
    let { mant_id, item, ubicacion, novedad, fail, report, rec_date, days, notes } = data_;

    console.log(data_);
    console.log(mant_id);
    console.log(item);
    console.log(ubicacion);
    console.log(novedad);
    console.log(fail);
    console.log(report);
    console.log(rec_date);
    console.log(days);
    console.log(notes);
    
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    let ar = new Array();
    for(let i = 0; i < form.elements.length; i++) {
        console.log(form.elements[i].name + ":", checkData(form.elements[i].value) + " - " + form.elements[i].value);
        ar.push(form.elements[i].value);
    }

    createManteinment({
        item: ar[0],
        ubicacion: ar[1],
        novedad: ar[2],
        fail: ar[3],
        report: ar[4],
        rec_date: ar[5],
        days: ar[6],
        notes: ar[7],
    })
})

form_update.addEventListener("submit", (e) => {
    e.preventDefault();
    let ar = new Array();
    for(let i = 0; i < form_update.elements.length; i++) {
        console.log(form_update.elements[i].name + ":", checkData(form_update.elements[i].value) + " - " + form_update.elements[i].value);
        ar.push(form_update.elements[i].value);
    }

    modifyManteinment({
        mant_id: ar[0],
        item: ar[1],
        ubicacion: ar[2],
        novedad: ar[3],
        fail: ar[4],
        report: ar[5],
        rec_date: ar[6],
        days: ar[7],
        notes: ar[8],
    })
})