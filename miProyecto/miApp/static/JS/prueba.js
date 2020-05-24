let loadBtn3 = document.getElementById("loadBtn2");

loadBtn3.addEventListener("click", (event) => {
  cargarJson2();
});

function cargarJson2() {
  fetch('http://127.0.0.1:8000/miApp/pedidosjs')
    .then((response) => response.json())
    .then((json) => {
    console.log(json);

      let opci1 = document.getElementById("op0");
      opci1.textContent = `${json[0].codigo}`;

      let opci2 = document.getElementById("op1");
      opci2.textContent = `${json[1].codigo}`;

      let opci3 = document.getElementById("op2");
      opci3.textContent = `${json[2].codigo}`;

      let opci4 = document.getElementById("op3");
      opci4.textContent = `${json[3].codigo}`;

    });
}


