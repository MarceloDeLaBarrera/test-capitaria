function mostrar() {
  var x = document.getElementById("row-promedio");
  var z = document.getElementById("row-promedio2");
  if (x.style.display === "none" && z.style.display === "block") {
    x.style.display = "block";
    z.style.display = "none";
  } else if (x.style.display === "block" && z.style.display === "none") {
    x.style.display = "none";
    z.style.display = "none";
  } else if (x.style.display === "none" && z.style.display === "none") {
    x.style.display = "block";
    z.style.display = "none";
  }
}

function mostrar2() {
  var x = document.getElementById("row-promedio");
  var z = document.getElementById("row-promedio2");
  if (x.style.display === "block" && z.style.display === "none") {
    x.style.display = "none";
    z.style.display = "block";
  } else if (x.style.display === "none" && z.style.display === "block") {
    x.style.display = "none";
    z.style.display = "none";
  } else if (x.style.display === "none" && z.style.display === "none") {
    x.style.display = "none";
    z.style.display = "block";
  }
}
