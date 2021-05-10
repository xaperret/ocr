/**
 * ! GLOBAL VARIABLE !
 */
const canvasSize = 20;
const canvasId = "canvasOCR";
var canvasOCR = document.createElement("canvas");
canvasOCR.id = canvasId;
const ctx = canvasOCR.getContext("2d");
var coords = { x: 0, y: 0 };
var step = 0;

/**
 * ! FUNCTIONS !
 */

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
  document.addEventListener("mousemove", drawSquare);
  refreshCoords(e);
  drawSquare();
}

function endDrawing() {
  document.removeEventListener("mousemove", drawSquare);
}

function resizeDrawing(e) {}

function drawSquare(color = "black") {
  ctx.fillStyle = color;
  let x = Math.floor(coords.x / step) * step;
  let y = Math.floor(coords.y / step) * step;
  console.log("drawSquare -> drawing at x:", x, " y:", y, " step:", step);
  ctx.fillRect(x, y, step, step);
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

document.querySelector("main").append(canvasOCR);

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
