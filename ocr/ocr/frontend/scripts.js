/* jshint esversion: 6 */
/* version 0.9 */
/**
 * ! GLOBAL VARIABLE !
 */
/* ! API RELATED ! */
const apiURL = "http://127.0.0.1:8000";

/* ! CANVAS RELATED ! */
const canvasSize = 20;
const canvasId = "canvasOCR";
var canvasOCR = document.createElement("canvas");
canvasOCR.id = canvasId;
const ctx = canvasOCR.getContext("2d");
var coords = { x: 0, y: 0 };
var step = 0;

var matrixOCR = new Array(canvasSize); // initializing matrix
for (let i = 0; i < canvasSize; i++) {
  // 2d matrix
  matrixOCR[i] = new Array(canvasSize);
  matrixOCR[i].fill(0);
}

/**
 * ! FUNCTIONS !
 */

/**
 * This function either destroy(true) or create(false) a canvas
 *
 * @param {* boolean} destroyCreate
 */
function destroyChart(destroyCreate) {
  if (destroyCreate) {
    console.log("hideChartHtml -> true");
    document.getElementById("predictChart").remove();
  } else {
    let chart = document.createElement("canvas");
    chart.setAttribute("id", "predictChart");
    document.querySelector("main").appendChild(chart);
  }
}

/**
 * This function takes the matrixOCR that has been filled and send it to the api
 */
function addImage() {
  let apiCall = apiURL + "/add";
  console.log("Making request to ", apiCall);

  let character = document.getElementById("range").value;
  let data = { title: character, content: matrixOCR };
  console.log("Containing ", data);

  fetch(apiCall, {
    method: "POST",
    body: JSON.stringify(data),
  });

  clearDrawing();
  destroyChart(true);
}

/**
 * This function ask the backend to train the model
 */
function trainModel() {
  let apiCall = apiURL + "/train";
  console.log("Making request to ", apiCall);

  fetch(apiCall, {
    method: "POST",
  });
  destroyChart(true);
}

/**
 * This function send the matrixOCR (drawings) and ask api to make a prediction
 *
 * This will make a call to the backend so that it makes a prediction based
 * upon the given data. It will then create a chart based on the response the
 * backend has given
 */
function predictFromModel() {
  let apiCall = apiURL + "/predict";
  console.log("Making request to ", apiCall);

  let data = { title: "", content: matrixOCR };
  console.log("Containing ", data);

  let labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
  destroyChart(false);

  fetch(apiCall, {
    method: "POST",
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      data = data.split(" ").join();
      data = data.split("[").join();
      data = data.split("]").join();
      data = data.split(",").filter((x) => x != "");
      data = data.map((x) => parseFloat(x));
      console.log(data);
      let backgroundColors = data.map((element) => "rgba(163, 190, 140, 0.2)");
      let max = -1;
      let tmp = -1;
      for (let i = 0; i < data.length; i++) {
        if (data[i] > max) {
          max = data[i];
          tmp = i;
        }
      }
      backgroundColors[tmp] = "rgba(163, 190, 140, 1)";
      const predictChart = new Chart(document.getElementById("predictChart"), {
        type: "bar",
        data: {
          labels: labels,
          datasets: [
            {
              label: "My First Dataset",
              data: data,
              backgroundColor: backgroundColors,
            },
          ],
        },
      });
    });
  destroyChart(false);
}

/**
 * Function that takes a number and return a close number that is divisible by 20
 *
 * Useful to make creating the canvas a bit responsive
 *
 * @param {*} size  is the number that needs to be divisible by 20
 * @returns a number close to original size that is divisible by 20
 */
function makeDivisibleBy20(size) {
  console.log("generating canvas");
  size = size - (size % 10);
  size = size + ((size / 10) % 2);
  return size;
}

/**
 * This function refreshes the global variable containing the client mouse position
 * @param {*} e
 *
 * @see end of script.js to see how is added this function
 */
function refreshCoords(e) {
  coords.x = e.clientX - canvasOCR.offsetLeft;
  coords.y = e.clientY - canvasOCR.offsetTop;
  console.log(e);
}

/**
 * As long as the client's mouse is on the canvas it will call this function
 * @param {*} e
 *
 * @see end of script.js to see how is added this function
 */
function startDrawing(e) {
  document.addEventListener("mousemove", mouseIsMoving);
  refreshCoords(e);
  drawSquare();
}
/**
 * Useful to keep track of the mouse when holding down the button mouse
 * @param {*} e
 *
 * @see end of script.js to see how is added this function
 */
function mouseIsMoving(e) {
  refreshCoords(e);
  drawSquare();
}

/**
 * @see end of script.js to see how is added this function
 */
function endDrawing() {
  document.removeEventListener("mousemove", mouseIsMoving);
}

/**
 * This function will draw a square at the client's mouse position or fill one of the grid squares
 * if given x/yPixel
 *
 * @param {string} color
 * @param {int} xPixel
 * @param {int} yPixel
 * @returns
 */
function drawSquare(color = "black", xPixel = -1, yPixel = -1) {
  console.log("drawSquare called ");

  ctx.fillStyle = color;
  let x = 0;
  let y = 0;
  if (xPixel < 0 || yPixel < 0) {
    x = Math.floor(coords.x / step) * step;
    y = Math.floor(coords.y / step) * step;
  } else {
    x = Math.floor(xPixel * step);
    y = Math.floor(yPixel * step);
  }
  if (x < 0 || y < 0) {
    console.log(" -> mouse out of bounds");
    return;
  }

  console.log(" -> drawing at x:", x, " y:", y, " step:", step);
  ctx.fillRect(x, y, step, step);

  let col = y / step;
  let li = x / step;
  console.log(" -> changing state of matrixOCR at ", col, ":", li);
  col = Math.round(col);
  li = Math.round(li);
  if (li >= canvasSize) {
    li = canvasSize - 1;
  }
  if (col >= canvasSize) {
    col = canvasSize - 1;
  }
  if (li < 0) {
    li = 0;
  }
  if (col < 0) {
    col = 0;
  }

  console.log(" -> rounded values ", col, ":", li);
  matrixOCR[col][li] = 1;
}

/**
 * Clear the content of both the canvas and matrix ocr
 */
function clearDrawing() {
  for (let i = 0; i < canvasSize; i++) {
    for (let j = 0; j < canvasSize; j++) {
      drawSquare("white", i, j);
    }
  }

  let hSquare = 0;
  let wSquare = 0;

  for (let i = 0; i < canvasOCR.width + 1; i = i + step) {
    hSquare = canvasOCR.height;
    wSquare = canvasOCR.width;

    ctx.moveTo(i, 0);
    ctx.lineTo(i, hSquare);
    ctx.stroke();

    ctx.moveTo(0, i);
    ctx.lineTo(wSquare, i);
    ctx.stroke();
  }
  clearMatrix(matrixOCR);
  destroyChart(true);
}

/**
 * Print the matrix
 * @param {*} mat
 */
function printMatrix(mat) {
  let s = "";
  let i = 0;
  mat.forEach((element) => {
    s = i.toString() + " => ";
    element.forEach((element) => {
      s += " " + element.toString();
    });
    s = s + mat[i].length.toString();
    console.log(s);
    i++;
  });
}

/**
 * Clear the content of the matrix
 * @param {*} mat
 */
function clearMatrix(mat) {
  console.log("Matrix cleared");
  mat.forEach((element) => {
    element.fill(0);
  });
  printMatrix(mat);
}

/**
 * Draw a line, deprecated
 * @param {*} event
 */
function draw(event) {
  ctx.beginPath();
  ctx.lineWidth = 5;
  ctx.lineCap = "round";
  ctx.strokeStyle = "#ACD3ED";
  ctx.moveTo(coords.x, coords.y);
  refreshCoords(event);
  ctx.lineTo(coords.x, coords.y);
  ctx.stroke();
}
/**
 * ! MAIN !
 */

/**  ! CANVAS CREATION !  */
let c = document.createElement("div");
c.appendChild(canvasOCR);
c.className = "container";

let form = document.createElement("form");
c.appendChild(form);
form.className = "container";
form.setAttribute("action", "../../backend/api.js");

let formBtnAddImage = document.createElement("input");
form.appendChild(formBtnAddImage);
formBtnAddImage.className = "btn";
formBtnAddImage.setAttribute("type", "button");
formBtnAddImage.setAttribute("value", "Envoyer");
formBtnAddImage.setAttribute("onClick", "addImage()");

let formBtnTrain = document.createElement("input");
form.appendChild(formBtnTrain);
formBtnTrain.className = "btn";
formBtnTrain.setAttribute("type", "button");
formBtnTrain.setAttribute("value", "Entrainer");
formBtnTrain.setAttribute("onClick", "trainModel()");

let formBtnEvaluate = document.createElement("input");
form.appendChild(formBtnEvaluate);
formBtnEvaluate.className = "btn";
formBtnEvaluate.setAttribute("type", "button");
formBtnEvaluate.setAttribute("value", "Evaluer");
formBtnEvaluate.setAttribute("onClick", "predictFromModel()");

let formBtnClear = document.createElement("input");
form.appendChild(formBtnClear);
formBtnClear.className = "btn";
formBtnClear.setAttribute("type", "button");
formBtnClear.setAttribute("value", "Effacer dessin");
formBtnClear.setAttribute("onclick", "clearDrawing()");

let formRange = document.createElement("select");
formRange.setAttribute("id", "range");
formRange.innerHTML =
  '<option value="0">0</option>' +
  '<option value="1">1</option>' +
  '<option value="2">2</option>' +
  '<option value="3">3</option>' +
  '<option value="4">4</option>' +
  '<option value="5">5</option>' +
  '<option value="6">6</option>' +
  '<option value="7">7</option>' +
  '<option value="8">8</option>' +
  '<option value="9">9</option>' +
  "</select>";
form.appendChild(formRange);

// Get browser size
const vw = Math.max(
  document.documentElement.clientWidth || 0,
  window.innerWidth || 0
);
const vh = Math.max(
  document.documentElement.clientHeight || 0,
  window.innerHeight || 0
);

if (vw > vh) {
  canvasOCR.width = makeDivisibleBy20(0.9 * vh);
  canvasOCR.height = makeDivisibleBy20(0.9 * vh);
} else {
  canvasOCR.width = makeDivisibleBy20(0.9 * vw);
  canvasOCR.height = makeDivisibleBy20(0.9 * vw);
}

document.querySelector("main").append(c);

step = canvasOCR.width / canvasSize;
let hSquare = 0;
let wSquare = 0;

for (let i = 0; i < canvasOCR.width + 1; i = i + step) {
  hSquare = canvasOCR.height;
  wSquare = canvasOCR.width;

  ctx.moveTo(i, 0);
  ctx.lineTo(i, hSquare);
  ctx.stroke();

  ctx.moveTo(0, i);
  ctx.lineTo(wSquare, i);
  ctx.stroke();
}

canvasOCR.addEventListener("mousedown", (e) => startDrawing(e));
canvasOCR.addEventListener("mouseup", endDrawing);
canvasOCR.addEventListener("focusout", endDrawing);
