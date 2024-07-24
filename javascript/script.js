const canvas = document.getElementById("animationCanvas");
const ctx = canvas.getContext("2d");

let balls = [
  {
    x: canvas.width / 2,
    y: canvas.height / 2,
    dx: 5,
    dy: 4,
    radius: 20,
    color: "green",
  },
  //   {
  //     x: canvas.width / 2,
  //     y: canvas.height / 2,
  //     dx: 5,
  //     dy: 4,
  //     radius: 40,
  //     color: "red",
  //   },
  //   {
  //     x: canvas.width / 2,
  //     y: canvas.height / 2,
  //     dx: 4,
  //     dy: 4,
  //     radius: 15,
  //     color: "blue",
  //   },
];

function drawBall(ball) {
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI * 2);
  ctx.fillStyle = ball.color;
  ctx.fill();
  ctx.closePath();
}

function update() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  balls.forEach((ball) => {
    drawBall(ball);
    ball.x += ball.dx;
    ball.y += ball.dy;

    // Bounce off the walls
    if (ball.x + ball.radius > canvas.width || ball.x - ball.radius < 0) {
      ball.dx = -ball.dx;
    }
    if (ball.y + ball.radius > canvas.height || ball.y - ball.radius < 0) {
      ball.dy = -ball.dy;
    }
  });
  requestAnimationFrame(update);
}

update();
