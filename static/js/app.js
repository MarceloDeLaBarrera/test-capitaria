function generaMatriz(Ini, Fin) {
  var ArrAgenda = [];
  Ini = Ini.split(":");
  Fin = Fin.split(":");

  var hhIni = parseInt(Ini[0], 10);
  var hhFin = parseInt(Fin[0], 10);

  var i = 0;
  while (hhIni <= hhFin) {
    x = i++;
    ArrAgenda[x] = hhIni + ":00";
    ArrAgenda[i] = hhIni + ":30";

    hhIni++;
    i++;
  }
  return ArrAgenda;
}

function VerificaDia(Dia, Hora, citas) {
  var txt = "<i class='icon ion-plus-circled txtVerde'></i>  ";
  var obj = JSON.parse(citas);

  if (Dia === 6 || Dia === 7) var txt = "<i></i>  ";

  if (Dia === 1)
    //Lunes
    for (var i in obj) {
      for (var x in obj[i]) {
        var arHora1 = obj[i][x].start_time.split(":");
        var arHora2 = obj[i][x].end_time.split(":");
        var arHora3 = Hora.split(":");
        var mm1 = parseInt(arHora1[1], 10);
        var mm2 = parseInt(arHora2[1], 10);
        var mm3 = parseInt(arHora3[1], 10);
        var hh1 = parseInt(arHora1[0], 10) * 60 + mm1;
        var hh2 = parseInt(arHora2[0], 10) * 60 + mm2;
        var hh3 = parseInt(arHora3[0], 10) * 60 + mm3;
        if (i === "monday")
          if (hh3 === hh1 || (hh2 >= hh3 && hh3 >= hh1))
            txt =
              "<i class='icon ion-calendar'> " +
              "<strong>" +
              obj[i][x].name +
              "</strong>" +
              "</i>";
      }
    }
  if (Dia === 2)
    //Martes
    for (var i in obj) {
      for (var x in obj[i]) {
        var arHora1 = obj[i][x].start_time.split(":");
        var arHora2 = obj[i][x].end_time.split(":");
        var arHora3 = Hora.split(":");
        var mm1 = parseInt(arHora1[1], 10);
        var mm2 = parseInt(arHora2[1], 10);
        var mm3 = parseInt(arHora3[1], 10);
        var hh1 = parseInt(arHora1[0], 10) * 60 + mm1;
        var hh2 = parseInt(arHora2[0], 10) * 60 + mm2;
        var hh3 = parseInt(arHora3[0], 10) * 60 + mm3;
        if (i === "tuesday")
          if (hh3 === hh1 || (hh2 >= hh3 && hh3 >= hh1))
            txt =
              "<i class='icon ion-calendar'> " +
              "<strong>" +
              obj[i][x].name +
              "</strong>" +
              "</i>";
      }
    }
  if (Dia === 3)
    //Miercoles
    for (var i in obj) {
      for (var x in obj[i]) {
        var arHora1 = obj[i][x].start_time.split(":");
        var arHora2 = obj[i][x].end_time.split(":");
        var arHora3 = Hora.split(":");
        var mm1 = parseInt(arHora1[1], 10);
        var mm2 = parseInt(arHora2[1], 10);
        var mm3 = parseInt(arHora3[1], 10);
        var hh1 = parseInt(arHora1[0], 10) * 60 + mm1;
        var hh2 = parseInt(arHora2[0], 10) * 60 + mm2;
        var hh3 = parseInt(arHora3[0], 10) * 60 + mm3;
        if (i === "wednesday")
          if (hh3 === hh1 || (hh2 >= hh3 && hh3 >= hh1))
            txt =
              "<i class='icon ion-calendar'> " +
              "<strong>" +
              obj[i][x].name +
              "</strong>" +
              "</i>";
      }
    }
  if (Dia === 4)
    //Jueves
    for (var i in obj) {
      for (var x in obj[i]) {
        var arHora1 = obj[i][x].start_time.split(":");
        var arHora2 = obj[i][x].end_time.split(":");
        var arHora3 = Hora.split(":");
        var mm1 = parseInt(arHora1[1], 10);
        var mm2 = parseInt(arHora2[1], 10);
        var mm3 = parseInt(arHora3[1], 10);
        var hh1 = parseInt(arHora1[0], 10) * 60 + mm1;
        var hh2 = parseInt(arHora2[0], 10) * 60 + mm2;
        var hh3 = parseInt(arHora3[0], 10) * 60 + mm3;
        if (i === "thursday")
          if (hh3 === hh1 || (hh2 >= hh3 && hh3 >= hh1))
            txt =
              "<i class='icon ion-calendar'> " +
              "<strong>" +
              obj[i][x].name +
              "</strong>" +
              "</i>";
      }
    }
  if (Dia === 5)
    //Viernes
    for (var i in obj) {
      for (var x in obj[i]) {
        var arHora1 = obj[i][x].start_time.split(":");
        var arHora2 = obj[i][x].end_time.split(":");
        var arHora3 = Hora.split(":");
        var mm1 = parseInt(arHora1[1], 10);
        var mm2 = parseInt(arHora2[1], 10);
        var mm3 = parseInt(arHora3[1], 10);
        var hh1 = parseInt(arHora1[0], 10) * 60 + mm1;
        var hh2 = parseInt(arHora2[0], 10) * 60 + mm2;
        var hh3 = parseInt(arHora3[0], 10) * 60 + mm3;
        if (i === "friday")
          if (hh3 === hh1 || (hh2 >= hh3 && hh3 >= hh1))
            txt =
              "<i class='icon ion-calendar'> " +
              "<strong>" +
              obj[i][x].name +
              "</strong>" +
              "</i>";
      }
    }
  if (Dia === 6)
    //Sabado
    for (var i in obj) {
      for (var x in obj[i]) {
        var arHora1 = obj[i][x].start_time.split(":");
        var arHora2 = obj[i][x].end_time.split(":");
        var arHora3 = Hora.split(":");
        var mm1 = parseInt(arHora1[1], 10);
        var mm2 = parseInt(arHora2[1], 10);
        var mm3 = parseInt(arHora3[1], 10);
        var hh1 = parseInt(arHora1[0], 10) * 60 + mm1;
        var hh2 = parseInt(arHora2[0], 10) * 60 + mm2;
        var hh3 = parseInt(arHora3[0], 10) * 60 + mm3;
        if (i === "saturday")
          if (hh3 === hh1 || (hh2 >= hh3 && hh3 >= hh1)) {
            txt =
              "<i class='icon ion-calendar'></i> " + obj[i][x].name + "</i>";
          }
      }
    }
  if (Dia === 7)
    //Domingo
    for (var i in obj) {
      for (var x in obj[i]) {
        var arHora1 = obj[i][x].start_time.split(":");
        var arHora2 = obj[i][x].end_time.split(":");
        var arHora3 = Hora.split(":");
        var mm1 = parseInt(arHora1[1], 10);
        var mm2 = parseInt(arHora2[1], 10);
        var mm3 = parseInt(arHora3[1], 10);
        var hh1 = parseInt(arHora1[0], 10) * 60 + mm1;
        var hh2 = parseInt(arHora2[0], 10) * 60 + mm2;
        var hh3 = parseInt(arHora3[0], 10) * 60 + mm3;
        if (i === "sunday")
          if (hh3 === hh1 || (hh2 >= hh3 && hh3 >= hh1))
            txt = "<i class='icon ion-calendar'></i> " + obj[i][x].name;
      }
    }

  return txt;
}

/*
  Genera el html para pintar la agenda
  */
function GeneraHtml(MatrizHrs, citas) {
  var obj = JSON.parse(citas);
  var Header = "";
  var Body = "";
  Header =
    "<div class='contenedor_agenda'><div class='menu ico left'><<</div>" +
    "<div class='menu dia'><strong>Lunes</strong></div>" +
    "<div class='menu dia'><strong>Martes</strong></div>  " +
    "<div class='menu dia'><strong>Miercoles</strong></div>  " +
    "<div class='menu dia'><strong>Jueves</strong></div>  " +
    "<div class='menu dia'><strong>Viernes</strong></div>  " +
    "<div class='menu dia'><strong>Sabádo</strong></div>  " +
    "<div class='menu dia'><strong>Domingo</strong></div> " +
    "<div class='menu ico right'>>></div></div>";

  for (i = 0; i < MatrizHrs.length; i++) {
    Body +=
      "<div class='contenedor_agenda'><div class='menu horaAgenda left'>" +
      MatrizHrs[i] +
      "</div>" +
      "<div class='menu diaAgenda'>" +
      VerificaDia(1, MatrizHrs[i], citas) +
      "</div>" +
      "<div class='menu diaAgenda'>" +
      VerificaDia(2, MatrizHrs[i], citas) +
      "</div>  " +
      "<div class='menu diaAgenda'>" +
      VerificaDia(3, MatrizHrs[i], citas) +
      "</div>  " +
      "<div class='menu diaAgenda'>" +
      VerificaDia(4, MatrizHrs[i], citas) +
      "</div>  " +
      "<div class='menu diaAgenda'>" +
      VerificaDia(5, MatrizHrs[i], citas) +
      "</div>  " +
      "<div class='menu diaAgenda'>" +
      VerificaDia(6, MatrizHrs[i], citas) +
      "</div>  " +
      "<div class='menu diaAgenda'>" +
      VerificaDia(7, MatrizHrs[i], citas) +
      "</div> " +
      "<div class='menu horaAgenda right'>" +
      MatrizHrs[i] +
      "</div></div>";
  }

  return Header + Body;
}

function CalculaRangos(citas) {
  var obj = JSON.parse(citas);
  var arrayRangos = [];
  var horaIni, horaFin;

  for (var i in obj) {
    for (var x in obj[i]) {
      if (horaIni === undefined) horaIni = obj[i][x].start_time;

      if (horaFin === undefined) horaFin = obj[i][x].start_time;
      else horaFin = obj[i][x].end_time;
    }
    arrayRangos["inicio"] = horaIni;
    arrayRangos["termino"] = horaFin;
  }
  return arrayRangos;
}

function Agenda(citas) {
  var obj = JSON.parse(citas);
  var Rangos = CalculaRangos(citas);
  console.log("horaIni:" + Rangos["inicio"]);
  console.log("horaIni:" + Rangos["termino"]);
  var Matriz = generaMatriz(Rangos["inicio"], Rangos["termino"]);

  return GeneraHtml(Matriz, citas);
}

var citas =
  '{"monday": [' +
  '      {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},' +
  '      {"name": "Jorge", "start_time": "09:30", "end_time": "11:00"},' +
  '      {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},' +
  '      {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}],' +
  '  "tuesday": [' +
  '      {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},' +
  '      {"name": "Jorge", "start_time": "11:30", "end_time": "12:00"},' +
  '      {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},' +
  '      {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}],' +
  '  "wednesday": [' +
  '      {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},' +
  '      {"name": "Jorge", "start_time": "10:30", "end_time": "12:00"},' +
  '      {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},' +
  '      {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}],' +
  '  "thursday": [' +
  '      {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},' +
  '      {"name": "Jorge", "start_time": "09:30", "end_time": "12:00"},' +
  '      {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},' +
  '      {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}],' +
  '  "friday": [' +
  '      {"name": "Jorge", "start_time": "08:00", "end_time": "09:00"},' +
  '      {"name": "Jorge", "start_time": "09:30", "end_time": "12:00"},' +
  '      {"name": "Jorge", "start_time": "15:00", "end_time": "16:00"},' +
  '      {"name": "Jorge", "start_time": "17:00", "end_time": "19:30"}]}';

document.getElementById("containerData").innerHTML = Agenda(citas);
