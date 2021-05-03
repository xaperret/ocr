/**
 * GLOBAL VARIABLE
 */
const CANVAS_SIZE = 20;

/**
 * FUNCTIONS
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
  size = size - (size % 10);
  size = size + ((size / 10) % 2);
  return size;
}

function drawSquare(eventObj, ctx, length) {
  ctx.beginPath();
  coords = findSquare(eventObj, length);
  console.log("after", coords);
  ctx.rect(coords[0], coords[1], length, length);
  ctx.fill();
}

function findSquare(eventObj, step, squareSize) {
  let coords = [];

  console.log("before", eventObj);

  coords.push(Math.round(squareSize / (eventObj.x / step)));
  coords.push(Math.round(squareSize / (eventObj.y / step)));
  return coords;
}

/**
 * MAIN
 */

// Get browser size
const vw = Math.max(
  document.documentElement.clientWidth || 0,
  window.innerWidth || 0
);
const vh = Math.max(
  document.documentElement.clientHeight || 0,
  window.innerHeight || 0
);

// create element canvas and append it to main
let canvasOCR = document.createElement("canvas");
canvasOCR.id = "canvasOCR";

if (vw > vh) {
  canvasOCR.width = makeDivisibleBy20(0.9 * vh);
  canvasOCR.height = makeDivisibleBy20(0.9 * vh);
} else {
  canvasOCR.width = makeDivisibleBy20(0.9 * vw);
  canvasOCR.height = makeDivisibleBy20(0.9 * vw);
}

document.querySelector("main").append(canvasOCR);

var c = document.getElementById("canvasOCR");
var ctx = c.getContext("2d");

let step = canvasOCR.width / CANVAS_SIZE;
let hSquare = 0;
let wSquare = 0;

for (let i = 0; i <= canvasOCR.width; i = i + step) {
  hSquare = canvasOCR.height;
  wSquare = canvasOCR.width;

  ctx.moveTo(i, 0);
  ctx.lineTo(i, hSquare);
  ctx.stroke();

  ctx.moveTo(0, i);
  ctx.lineTo(wSquare, i);
  ctx.stroke();
}

// canvasOCR.addEventListener("mouseover", (e) => drawSquare(e, ctx, step));

canvasOCR.addEventListener("mousedown", (e) => drawSquare(e, ctx, step));

// canvasOCR.addEventListener("mouseup", (e) => drawSquare(e, 0));
