/* jshint esversion: 6 */
/* version 0.1 */
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
}

function trainModel() {
  let apiCall = apiURL + "/train";
  console.log("Making request to ", apiCall);

  fetch(apiCall, {
    method: "POST",
  });
}

function predictFromModel() {
  let apiCall = apiURL + "/predict";
  console.log("Making request to ", apiCall);

  let data = { title: "", content: matrixOCR };
  console.log("Containing ", data);

  fetch(apiCall, {
    method: "POST",
  });
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

function refreshCoords(e) {
  coords.x = e.clientX - canvasOCR.offsetLeft;
  coords.y = e.clientY - canvasOCR.offsetTop;
  console.log(e);
}

function startDrawing(e) {
  document.addEventListener("mousemove", mouseIsMoving);
  refreshCoords(e);
  drawSquare();
}

function mouseIsMoving(e) {
  refreshCoords(e);
  drawSquare();
}

function endDrawing() {
  document.removeEventListener("mousemove", mouseIsMoving);
}

function resizeDrawing(e) {}

function drawSquare(color = "black") {
  ctx.fillStyle = color;
  let x = Math.floor(coords.x / step) * step;
  let y = Math.floor(coords.y / step) * step;
  console.log("drawSquare -> drawing at x:", x, " y:", y, " step:", step);
  ctx.fillRect(x, y, step, step);
  console.log(
    "drawSquare -> changing state of matrixOCR at ",
    y / step,
    ":",
    x / step
  );
  matrixOCR[y / step][x / step] = 1;
}

function clearDrawing() {
  let step = canvasOCR.width / canvasSize;
  for (let i = 0; i < canvasOCR.width; i = i + step) {
    for (let j = 0; j < canvasOCR.height; j = j + step) {
      coords.x = i;
      coords.y = j;
      drawSquare("white");
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
}

function printMatrix(mat) {
  let s = "";
  let i = 0;
  mat.forEach((element) => {
    s = i.toString() + " => ";
    element.forEach((element) => {
      s += " " + element.toString();
    });
    console.log(s);
    i++;
  });
}

function clearMatrix(mat) {
  console.log("Matrix cleared");
  mat.forEach((element) => {
    element.fill(0);
  });
}

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

let formBtnClearModels = document.createElement("input");
form.appendChild(formBtnClearModels);
formBtnClearModels.className = "btn";
formBtnClearModels.setAttribute("type", "button");
formBtnClearModels.setAttribute("value", "Effacer modèle");
formBtnClearModels.setAttribute("onclick", "clearDrawing()");

let formBtnLoad = document.createElement("input");
form.appendChild(formBtnLoad);
formBtnLoad.className = "btn";
formBtnLoad.setAttribute("type", "button");
formBtnLoad.setAttribute("value", "Charger les datasets");
formBtnLoad.setAttribute("onclick", "clearDrawing()");

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
//canvasOCR.addEventListener("resize", (e) => resizeDrawing(e));
