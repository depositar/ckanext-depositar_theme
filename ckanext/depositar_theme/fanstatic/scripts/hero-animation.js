var xBlock;
var yBlock;
var randomPosX;
var randomPosY;
var randomPosY2;
var randomPosY3;
var randomShow;
var numBlocks;
var BlockW;
var BlockH;

// LOGO AND FRAME
var OnOff;
var halfPeriod;
var currFrame;
var step;

// MOUSE EFFECT
var mouseBX;
var mouseBY;

// FONT
var f;
var message;
var rantext;
var rantsize;
var tsize;
var rantcolor;
var tcolor;

function setup() {
  initializeFields();
  frameRate(12);
  BlockW = 35;
  BlockH = 20;
  numBlocks = int(random(20, 100));
  createCanvas(350, 240).parent('hero-animation');
  background(1, 40, 25);
  cursor(CROSS);
}

function draw() {
  // FRAME SETTING
  currFrame++;
  if (currFrame % halfPeriod == 1) {
    if (step < 9) {
      step += 1;
    }
  }
  // SET LOGO FRAMING
  if (currFrame % (halfPeriod / 2) == 1) {
    OnOff = !OnOff;
  }
  // LOGO U
  if (OnOff == true) {
    noStroke();
    fill(0, 224, 155, 51);
    rect((step - 1) * BlockW, 10 * BlockH, 70, 40);
  } else {
    // ERASE LOGO U
    noStroke();
    fill(1, 40, 25, 255);
    rect((step - 1) * BlockW, 10 * BlockH, 70, 40);
  }
  // create array for location
  if (step > 1) {
    // draw green cells
    randomPosX = int(random(0, step - 2));
    randomPosY = int(random(0, yBlock));
    stroke(1, 40, 25);
    strokeJoin(ROUND);
    strokeWeight(2);
    fill(1, 40, 25);
    rect(randomPosX * BlockW, randomPosY * BlockH, BlockW, BlockH);
    // set mask
    rect(4 * BlockW, 0, 4 * BlockW, 2 * BlockH);
    rect(0, 8 * BlockH, 4 * BlockW, 2 * BlockH);
  }
  // set randoms
  randomShow = int(random(0, 15));
  randomPosX = int(random(0, step - 1));
  randomPosY = int(random(0, yBlock));
  randomPosY2 = int(random(0, yBlock - 2));
  randomPosY3 = int(random(0, yBlock - 3));
  if (step > 3) {
    if (randomShow == 0) {
      fill(249, 189, 189);
      triangle(randomPosX * BlockW, (randomPosY + 1) * BlockH, (randomPosX + 1) * BlockW, (randomPosY + 1) * BlockH, randomPosX * BlockW, (randomPosY) * BlockH);
    } else if (randomShow == 1) {
      fill(color(0x07, 0x7a, 0x48));
      rect((randomPosX - 2) * BlockW, randomPosY3 * BlockH, 3 * BlockW, 3 * BlockH);
    } else if (randomShow > 1 && randomShow < 6) {
      fill(0, 224, 155);
      rect(randomPosX * BlockW, randomPosY * BlockH, BlockW, BlockH);
    } else if (randomShow == 6) {
      if (randomPosX < 6) {
        fill(color(0xf4, 0x64, 0x64));
        rect(randomPosX * BlockW, randomPosY2 * BlockH, 2 * BlockW, 2 * BlockH);
      }
    } else if (randomShow == 7) {
      fill(color(0x07, 0x7a, 0x48));
      rect(randomPosX * BlockW, randomPosY * BlockH, BlockW, BlockH);
    } else if (randomShow == 8) {
      fill(color(0x72, 0x04, 0x04));
      rect(randomPosX * BlockW, randomPosY * BlockH, BlockW, BlockH);
    } else if (randomShow == 9) {
      fill(color(0xf4, 0x64, 0x64));
      rect(randomPosX * BlockW, randomPosY * BlockH, BlockW, BlockH);
    } else if (randomShow == 10) {
      fill(0, 224, 155);
      rect(randomPosX * BlockW, randomPosY * BlockH, BlockW / 2, BlockH / 2);
    } else if (randomShow == 11) {
      fill(color(0xe5, 0xc2, 0x2e));
      rect((randomPosX + 0.25) * BlockW, (randomPosY + 0.25) * BlockH, BlockW / 4, BlockH / 4);
    } else if (randomShow == 12) {
      fill(color(0x6f, 0xd5, 0xd8));
      rect((randomPosX + 0.25) * BlockW, (randomPosY) * BlockH, BlockW / 4, BlockH / 4);
    } else if (randomShow == 13) {
      fill(color(0xa5, 0x87, 0xdd));
      rect((randomPosX) * BlockW, (randomPosY + 0.25) * BlockH, BlockW / 4, BlockH / 4);
    } else if (randomShow == 14) {
      fill(color(0x93, 0xcc, 0x58));
      rect(randomPosX * BlockW, (randomPosY + 0.25) * BlockH, BlockW / 4, BlockH / 4);
    } else if (randomShow == 15) {
      fill(color(0xf4, 0x64, 0x64));
      rect((randomPosX + 0.25) * BlockW, randomPosY * BlockH, BlockW / 2, BlockH / 2);
    }
  }
  // MOUSE EFFECT
  mouseBX = int(mouseX / BlockW);
  mouseBY = int(mouseY / BlockH);
  rantext = int(random(0, 8));
  rantsize = int(random(0, 2));
  rantcolor = int(random(0, 2));
  if (mouseBX < step - 2 && mouseBY < yBlock) {
    stroke(1, 40, 25);
    fill(1, 40, 25);
    rect(mouseBX * BlockW, mouseBY * BlockH, BlockW, BlockH);
    fill(1, 40, 25, 122);
    rect((mouseBX - 1) * BlockW, (mouseBY - 1) * BlockH, 3 * BlockW, 3 * BlockH);
    // FONT
    // Set the font
    textFont('Courier');
    textAlign(LEFT);
    fill(255);
    textSize(tsize[rantsize]);
    fill(tcolor[rantcolor]);
    text(message[rantext], mouseBX * BlockW + 5, mouseBY * BlockH + 15);
    if (rantsize == 0) {
      text(currFrame, (mouseBX + 1) * BlockW + 5, mouseBY * BlockH + 15);
    }
  }
}

function initializeFields() {
  xBlock = 8;
  yBlock = 10;
  randomPosX = 0;
  randomPosY = 0;
  randomPosY2 = 0;
  randomPosY3 = 0;
  randomShow = 0;
  numBlocks = 0;
  BlockW = 0;
  BlockH = 0;
  OnOff = false;
  halfPeriod = 12;
  currFrame = 0;
  step = 0;
  mouseBX = 0;
  mouseBY = 0;
  f = null;
  message = [ 'data', 'WGS', 'GM_8', 'age', 'TR8A', 'U2E', 'edu', 'gen', 'gis', 'type', 'yr', 'st' ];
  rantext = 0;
  rantsize = 0;
  tsize = [ 8, 13 ];
  rantcolor = 0;
  tcolor = [ 220, 255 ];
}
