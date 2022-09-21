let t_body = document.querySelector(".t_body");

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