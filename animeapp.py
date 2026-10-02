import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Anime Clash 1v1",
    page_icon="⚡",
    layout="wide"
)

GAME_HTML = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>
* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
    overflow: hidden;
    background: #0b0e15;
    font-family: Arial, sans-serif;
}

#game {
    position: relative;
    width: 100%;
    max-width: 1150px;
    height: 700px;
    margin: auto;
    overflow: hidden;
    border-radius: 14px;
    background: #111722;
    outline: none;
}

canvas {
    display: block;
    width: 100%;
    height: 100%;
}

#hud {
    position: absolute;
    top: 15px;
    left: 20px;
    right: 20px;
    z-index: 20;
    pointer-events: none;
}

.hud-row {
    display: flex;
    align-items: center;
    gap: 14px;
}

.player-box {
    flex: 1;
}

.player-name {
    color: white;
    font-weight: bold;
    font-size: 18px;
    margin-bottom: 5px;
    text-shadow: 0 2px 5px black;
}

.bar {
    width: 100%;
    height: 22px;
    background: rgba(0,0,0,.65);
    border: 2px solid rgba(255,255,255,.25);
    border-radius: 20px;
    overflow: hidden;
}

.hp {
    width: 100%;
    height: 100%;
    background: #42e879;
    transition: width .1s;
}

#p2hp {
    background: #ff5570;
}

.mana-bar {
    height: 9px;
    margin-top: 5px;
}

.energy {
    width: 0%;
    height: 100%;
    background: #55c9ff;
    transition: width .1s;
}

#p2energy {
    background: #c16aff;
}

#timer {
    width: 80px;
    color: white;
    font-size: 34px;
    font-weight: bold;
    text-align: center;
    text-shadow: 0 3px 10px black;
}

#controls {
    position: absolute;
    bottom: 12px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 15;
    color: white;
    background: rgba(0,0,0,.68);
    border-radius: 12px;
    padding: 9px 16px;
    font-size: 13px;
    white-space: nowrap;
}

#countdown {
    position: absolute;
    inset: 0;
    z-index: 30;
    display: none;
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 115px;
    font-weight: bold;
    text-shadow: 0 5px 30px black;
    pointer-events: none;
}

#start {
    position: absolute;
    inset: 0;
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: center;
    background:
        radial-gradient(
            circle at center,
            rgba(50,75,130,.9),
            rgba(4,7,14,.98)
        );
    color: white;
    text-align: center;
}

.start-box h1 {
    margin: 0;
    font-size: 65px;
    color: #f5c84c;
    letter-spacing: 4px;
    text-shadow: 0 5px 25px black;
}

.start-box p {
    color: #d8deeb;
    font-size: 18px;
}

#startButton,
#again {
    border: 0;
    border-radius: 12px;
    padding: 14px 30px;
    background: #f5c84c;
    color: #111;
    font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    box-shadow: 0 8px 25px rgba(0,0,0,.4);
}

#startButton:hover,
#again:hover {
    transform: scale(1.05);
}

#message {
    position: absolute;
    inset: 0;
    z-index: 90;
    display: none;
    align-items: center;
    justify-content: center;
    background: rgba(2,4,9,.82);
    color: white;
    text-align: center;
}

.message-box h1 {
    font-size: 58px;
    margin: 0 0 10px;
}

.message-box p {
    font-size: 20px;
    margin-bottom: 25px;
}

.tip {
    opacity: .6;
    font-size: 13px !important;
}
</style>
</head>

<body>

<div id="game" tabindex="0">

    <canvas id="canvas"></canvas>

    <div id="hud">
        <div class="hud-row">

            <div class="player-box">
                <div class="player-name">⚡ PLAYER 1</div>

                <div class="bar">
                    <div id="p1hp" class="hp"></div>
                </div>

                <div class="bar mana-bar">
                    <div id="p1energy" class="energy"></div>
                </div>
            </div>

            <div id="timer">60</div>

            <div class="player-box">
                <div class="player-name" style="text-align:right">
                    PLAYER 2 ⚡
                </div>

                <div class="bar">
                    <div id="p2hp" class="hp"></div>
                </div>

                <div class="bar mana-bar">
                    <div id="p2energy" class="energy"></div>
                </div>
            </div>

        </div>
    </div>

    <div id="countdown">3</div>

    <div id="controls">
        P1:
        <b>A/D</b> di chuyển
        • <b>W</b> nhảy
        • <b>F</b> đánh
        • <b>G</b> skill
        • <b>H</b> ulti
        &nbsp;&nbsp;|&nbsp;&nbsp;
        P2:
        <b>←/→</b> di chuyển
        • <b>↑</b> nhảy
        • <b>K</b> đánh
        • <b>L</b> skill
        • <b>O</b> ulti
    </div>

    <div id="start">
        <div class="start-box">

            <h1>ANIME CLASH</h1>

            <p>⚡ 1V1 ARENA ⚡</p>

            <p>
                Đấu đối kháng 2 người trên cùng bàn phím.
            </p>

            <button id="startButton">
                ▶ BẮT ĐẦU TRẬN
            </button>

            <p class="tip">
                Click vào game sau khi bắt đầu nếu bàn phím chưa nhận.
            </p>

        </div>
    </div>

    <div id="message">

        <div class="message-box">

            <h1 id="winner"></h1>

            <p id="resultText"></p>

            <button id="again">
                CHƠI LẠI
            </button>

        </div>

    </div>

</div>

<script>

(function () {

"use strict";

/* =========================
   DOM
========================= */

var game = document.getElementById("game");
var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

var startScreen =
    document.getElementById("start");

var startButton =
    document.getElementById("startButton");

var message =
    document.getElementById("message");

var againButton =
    document.getElementById("again");

var countdown =
    document.getElementById("countdown");

var winner =
    document.getElementById("winner");

var resultText =
    document.getElementById("resultText");

var p1hp =
    document.getElementById("p1hp");

var p2hp =
    document.getElementById("p2hp");

var p1energy =
    document.getElementById("p1energy");

var p2energy =
    document.getElementById("p2energy");

var timerElement =
    document.getElementById("timer");


/* =========================
   GAME VARIABLES
========================= */

var W = 1150;
var H = 700;

var p1 = null;
var p2 = null;

var keys = {};

var particles = [];
var effects = [];
var projectiles = [];

var running = false;
var ended = false;

var timeLeft = 60;
var lastTime = 0;


/* =========================
   RESIZE
========================= */

function resize() {

    var rect =
        game.getBoundingClientRect();

    W = Math.max(700, rect.width);
    H = Math.max(500, rect.height);

    canvas.width = W;
    canvas.height = H;
}


/* =========================
   HELPERS
========================= */

function clamp(value, min, max) {

    return Math.max(
        min,
        Math.min(max, value)
    );
}


/* =========================
   FIGHTER
========================= */

function createFighter(
    x,
    color,
    facing
) {

    return {

        x: x,

        y: H - 145,

        vx: 0,

        vy: 0,

        width: 44,

        height: 82,

        hp: 100,

        energy: 0,

        color: color,

        facing: facing,

        grounded: true,

        attackTimer: 0,

        skillTimer: 0,

        ultimateTimer: 0,

        attackCooldown: 0,

        skillCooldown: 0,

        ultimateCooldown: 0,

        hitFlash: 0

    };
}


/* =========================
   INIT
========================= */

function initPlayers() {

    resize();

    p1 = createFighter(
        W * 0.28,
        "#45a8ff",
        1
    );

    p2 = createFighter(
        W * 0.72,
        "#d96cff",
        -1
    );
}


/* =========================
   RESET
========================= */

function resetGame() {

    initPlayers();

    particles = [];
    effects = [];
    projectiles = [];

    timeLeft = 60;

    running = false;
    ended = false;

    message.style.display = "none";

    startScreen.style.display = "none";

    updateHUD();

    startCountdown();
}


/* =========================
   COUNTDOWN
========================= */

function startCountdown() {

    var numbers = [
        "3",
        "2",
        "1",
        "FIGHT!"
    ];

    var index = 0;

    countdown.style.display = "flex";

    function next() {

        countdown.textContent =
            numbers[index];

        index++;

        if (index >= numbers.length) {

            setTimeout(
                function () {

                    countdown.style.display =
                        "none";

                    running = true;

                    game.focus();

                },
                650
            );

            return;
        }

        setTimeout(
            next,
            700
        );
    }

    next();
}


/* =========================
   MOVEMENT
========================= */

function moveFighter(
    f,
    leftKey,
    rightKey,
    jumpKey,
    dt
) {

    if (keys[leftKey]) {

        f.vx = -280;

        f.facing = -1;

    }
    else if (keys[rightKey]) {

        f.vx = 280;

        f.facing = 1;

    }
    else {

        f.vx *= 0.78;

    }


    if (
        keys[jumpKey] &&
        f.grounded
    ) {

        f.vy = -530;

        f.grounded = false;

    }


    f.vy += 1250 * dt;

    f.x += f.vx * dt;

    f.y += f.vy * dt;


    var floor =
        H - 145;


    if (f.y >= floor) {

        f.y = floor;

        f.vy = 0;

        f.grounded = true;

    }


    f.x =
        clamp(
            f.x,
            35,
            W - 35
        );


    f.attackCooldown =
        Math.max(
            0,
            f.attackCooldown - dt
        );

    f.skillCooldown =
        Math.max(
            0,
            f.skillCooldown - dt
        );

    f.ultimateCooldown =
        Math.max(
            0,
            f.ultimateCooldown - dt
        );

    f.attackTimer =
        Math.max(
            0,
            f.attackTimer - dt
        );

    f.skillTimer =
        Math.max(
            0,
            f.skillTimer - dt
        );

    f.ultimateTimer =
        Math.max(
            0,
            f.ultimateTimer - dt
        );

    f.hitFlash =
        Math.max(
            0,
            f.hitFlash - dt
        );
}


/* =========================
   NORMAL ATTACK
========================= */

function normalAttack(
    attacker,
    defender
) {

    if (
        attacker.attackCooldown > 0
    ) {
        return;
    }

    attacker.attackCooldown =
        0.3;

    attacker.attackTimer =
        0.18;


    var dx =
        defender.x -
        attacker.x;


    var correct =
        (
            attacker.facing === 1 &&
            dx > 0
        )
        ||
        (
            attacker.facing === -1 &&
            dx < 0
        );


    if (
        Math.abs(dx) < 90 &&
        Math.abs(
            defender.y -
            attacker.y
        ) < 75 &&
        correct
    ) {

        defender.hp -= 8;

        defender.hitFlash =
            0.15;

        attacker.energy =
            Math.min(
                100,
                attacker.energy + 8
            );

        hitEffect(
            defender.x,
            defender.y - 35,
            "#ffffff"
        );
    }
}


/* =========================
   SKILL
========================= */

function skill(
    attacker,
    defender
) {

    if (
        attacker.skillCooldown > 0
    ) {
        return;
    }

    if (
        attacker.energy < 25
    ) {
        return;
    }

    attacker.energy -= 25;

    attacker.skillCooldown =
        1;

    attacker.skillTimer =
        0.3;


    projectiles.push({

        x:
            attacker.x +
            attacker.facing * 40,

        y:
            attacker.y - 35,

        vx:
            attacker.facing * 720,

        radius: 16,

        damage: 16,

        color:
            attacker.color,

        owner:
            attacker

    });
}


/* =========================
   ULTIMATE
========================= */

function ultimate(
    attacker,
    defender
) {

    if (
        attacker.ultimateCooldown > 0
    ) {
        return;
    }

    if (
        attacker.energy < 100
    ) {
        return;
    }

    attacker.energy = 0;

    attacker.ultimateCooldown =
        4;

    attacker.ultimateTimer =
        0.7;


    var dx =
        defender.x -
        attacker.x;


    var correct =
        (
            attacker.facing === 1 &&
            dx > 0
        )
        ||
        (
            attacker.facing === -1 &&
            dx < 0
        );


    if (
        Math.abs(dx) < 300 &&
        correct
    ) {

        defender.hp -= 35;

        defender.hitFlash =
            0.35;

        bigEffect(
            defender.x,
            defender.y - 35,
            attacker.color
        );

    }
    else {

        bigEffect(
            attacker.x +
            attacker.facing * 130,
            attacker.y - 35,
            attacker.color
        );
    }
}


/* =========================
   PROJECTILES
========================= */

function updateProjectiles(dt) {

    for (
        var i = projectiles.length - 1;
        i >= 0;
        i--
    ) {

        var p =
            projectiles[i];

        p.x +=
            p.vx * dt;


        var target =
            p.owner === p1
            ? p2
            : p1;


        if (
            Math.abs(
                p.x -
                target.x
            ) <
            target.width / 2 +
            p.radius
        ) {

            target.hp -=
                p.damage;

            target.hitFlash =
                0.2;

            p.owner.energy =
                Math.min(
                    100,
                    p.owner.energy + 10
                );

            hitEffect(
                target.x,
                target.y - 35,
                p.color
            );

            projectiles.splice(
                i,
                1
            );

            continue;
        }


        if (
            p.x < -100 ||
            p.x > W + 100
        ) {

            projectiles.splice(
                i,
                1
            );
        }
    }
}


/* =========================
   EFFECTS
========================= */

function hitEffect(
    x,
    y,
    color
) {

    effects.push({

        x: x,

        y: y,

        radius: 10,

        maxRadius: 60,

        life: 0.25,

        maxLife: 0.25,

        color: color

    });


    for (
        var i = 0;
        i < 9;
        i++
    ) {

        particles.push({

            x: x,

            y: y,

            vx:
                (Math.random() - .5) *
                300,

            vy:
                (Math.random() - .5) *
                300,

            life: .4,

            color: color

        });
    }
}


function bigEffect(
    x,
    y,
    color
) {

    effects.push({

        x: x,

        y: y,

        radius: 20,

        maxRadius: 180,

        life: .65,

        maxLife: .65,

        color: color

    });


    for (
        var i = 0;
        i < 35;
        i++
    ) {

        particles.push({

            x: x,

            y: y,

            vx:
                (Math.random() - .5) *
                600,

            vy:
                (Math.random() - .5) *
                600,

            life: .8,

            color: color

        });
    }
}


/* =========================
   UPDATE EFFECTS
========================= */

function updateEffects(dt) {

    for (
        var i = particles.length - 1;
        i >= 0;
        i--
    ) {

        var p =
            particles[i];

        p.x +=
            p.vx * dt;

        p.y +=
            p.vy * dt;

        p.vy +=
            500 * dt;

        p.life -=
            dt;

        if (
            p.life <= 0
        ) {

            particles.splice(
                i,
                1
            );
        }
    }


    for (
        var j = effects.length - 1;
        j >= 0;
        j--
    ) {

        var e =
            effects[j];

        e.life -=
            dt;

        var progress =
            1 -
            e.life /
            e.maxLife;

        e.radius =
            10 +
            (
                e.maxRadius - 10
            ) *
            progress;

        if (
            e.life <= 0
        ) {

            effects.splice(
                j,
                1
            );
        }
    }
}


/* =========================
   GAME UPDATE
========================= */

function update(dt) {

    if (
        !running ||
        ended
    ) {
        return;
    }


    timeLeft -=
        dt;


    if (
        timeLeft <= 0
    ) {

        timeLeft = 0;


        if (
            p1.hp > p2.hp
        ) {

            finish(
                "PLAYER 1",
                "HP còn nhiều hơn!"
            );

        }
        else if (
            p2.hp > p1.hp
        ) {

            finish(
                "PLAYER 2",
                "HP còn nhiều hơn!"
            );

        }
        else {

            finish(
                "HÒA!",
                "Hai bên có cùng HP."
            );
        }

        return;
    }


    moveFighter(
        p1,
        "a",
        "d",
        "w",
        dt
    );


    moveFighter(
        p2,
        "arrowleft",
        "arrowright",
        "arrowup",
        dt
    );


    updateProjectiles(dt);

    updateEffects(dt);


    if (
        p1.hp <= 0
    ) {

        p1.hp = 0;

        finish(
            "PLAYER 2",
            "PLAYER 1 đã hết HP!"
        );
    }


    if (
        p2.hp <= 0
    ) {

        p2.hp = 0;

        finish(
            "PLAYER 1",
            "PLAYER 2 đã hết HP!"
        );
    }
}


/* =========================
   DRAW ARENA
========================= */

function drawArena() {

    var groundY =
        H - 95;


    var gradient =
        ctx.createLinearGradient(
            0,
            0,
            0,
            H
        );


    gradient.addColorStop(
        0,
        "#293b61"
    );

    gradient.addColorStop(
        1,
        "#0d121c"
    );


    ctx.fillStyle =
        gradient;

    ctx.fillRect(
        0,
        0,
        W,
        H
    );


    var glow =
        ctx.createRadialGradient(
            W / 2,
            H * .45,
            20,
            W / 2,
            H * .45,
            430
        );


    glow.addColorStop(
        0,
        "rgba(100,160,255,.2)"
    );

    glow.addColorStop(
        1,
        "rgba(0,0,0,0)"
    );


    ctx.fillStyle =
        glow;

    ctx.fillRect(
        0,
        0,
        W,
        H
    );


    ctx.fillStyle =
        "#161c27";

    ctx.fillRect(
        0,
        groundY,
        W,
        H - groundY
    );


    ctx.strokeStyle =
        "rgba(255,255,255,.1)";

    ctx.lineWidth = 2;


    for (
        var x = -H;
        x < W + H;
        x += 70
    ) {

        ctx.beginPath();

        ctx.moveTo(
            W / 2 +
            (x - W / 2) * .25,
            groundY
        );

        ctx.lineTo(
            x,
            H
        );

        ctx.stroke();
    }


    ctx.strokeStyle =
        "rgba(245,200,76,.35)";

    ctx.beginPath();

    ctx.moveTo(
        W / 2,
        groundY
    );

    ctx.lineTo(
        W / 2,
        H
    );

    ctx.stroke();
}


/* =========================
   DRAW FIGHTER
========================= */

function drawFighter(
    f,
    label
) {

    ctx.save();

    ctx.translate(
        f.x,
        f.y
    );


    /* shadow */

    ctx.fillStyle =
        "rgba(0,0,0,.4)";

    ctx.beginPath();

    ctx.ellipse(
        0,
        45,
        34,
        9,
        0,
        0,
        Math.PI * 2
    );

    ctx.fill();


    /* ultimate aura */

    if (
        f.energy >= 100
    ) {

        ctx.strokeStyle =
            f.color;

        ctx.globalAlpha =
            .45 +
            Math.sin(
                Date.now() / 100
            ) * .15;

        ctx.lineWidth = 5;

        ctx.beginPath();

        ctx.arc(
            0,
            0,
            58,
            0,
            Math.PI * 2
        );

        ctx.stroke();

        ctx.globalAlpha = 1;
    }


    /* body */

    ctx.fillStyle =
        f.hitFlash > 0
        ? "#ffffff"
        : f.color;

    ctx.beginPath();

    ctx.roundRect(
        -22,
        -32,
        44,
        65,
        12
    );

    ctx.fill();


    /* head */

    ctx.fillStyle =
        "#ffd1b3";

    ctx.beginPath();

    ctx.arc(
        0,
        -50,
        20,
        0,
        Math.PI * 2
    );

    ctx.fill();


    /* hair */

    ctx.fillStyle =
        "#20242e";

    ctx.beginPath();

    ctx.arc(
        0,
        -58,
        21,
        Math.PI,
        Math.PI * 2
    );

    ctx.fill();


    /* eye */

    ctx.fillStyle =
        "#111";

    ctx.beginPath();

    ctx.arc(
        f.facing * 8,
        -50,
        3,
        0,
        Math.PI * 2
    );

    ctx.fill();


    /* arm */

    ctx.strokeStyle =
        "#ffd1b3";

    ctx.lineWidth = 9;

    ctx.lineCap =
        "round";

    ctx.beginPath();

    ctx.moveTo(
        f.facing * 17,
        -18
    );

    ctx.lineTo(
        f.facing *
        (
            f.attackTimer > 0
            ? 48
            : 27
        ),
        -18
    );

    ctx.stroke();


    /* name */

    ctx.fillStyle =
        "white";

    ctx.font =
        "bold 13px Arial";

    ctx.textAlign =
        "center";

    ctx.fillText(
        label,
        0,
        56
    );


    ctx.restore();
}


/* =========================
   DRAW PROJECTILES
========================= */

function drawProjectiles() {

    for (
        var i = 0;
        i < projectiles.length;
        i++
    ) {

        var p =
            projectiles[i];

        ctx.save();

        ctx.shadowBlur = 22;

        ctx.shadowColor =
            p.color;

        ctx.fillStyle =
            p.color;

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.radius,
            0,
            Math.PI * 2
        );

        ctx.fill();

        ctx.restore();
    }
}


/* =========================
   DRAW EFFECTS
========================= */

function drawEffects() {

    for (
        var i = 0;
        i < effects.length;
        i++
    ) {

        var e =
            effects[i];

        ctx.save();

        ctx.globalAlpha =
            Math.max(
                0,
                e.life /
                e.maxLife
            );

        ctx.strokeStyle =
            e.color;

        ctx.lineWidth = 8;

        ctx.beginPath();

        ctx.arc(
            e.x,
            e.y,
            e.radius,
            0,
            Math.PI * 2
        );

        ctx.stroke();

        ctx.restore();
    }


    for (
        var j = 0;
        j < particles.length;
        j++
    ) {

        var p =
            particles[j];

        ctx.globalAlpha =
            Math.max(
                0,
                p.life / .8
            );

        ctx.fillStyle =
            p.color;

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            4,
            0,
            Math.PI * 2
        );

        ctx.fill();
    }

    ctx.globalAlpha = 1;
}


/* =========================
   DRAW
========================= */

function draw() {

    drawArena();

    drawEffects();

    drawProjectiles();

    if (p1) {
        drawFighter(
            p1,
            "P1"
        );
    }

    if (p2) {
        drawFighter(
            p2,
            "P2"
        );
    }
}


/* =========================
   HUD
========================= */

function updateHUD() {

    if (!p1 || !p2) {
        return;
    }


    p1hp.style.width =
        clamp(
            p1.hp,
            0,
            100
        ) + "%";


    p2hp.style.width =
        clamp(
            p2.hp,
            0,
            100
        ) + "%";


    p1energy.style.width =
        clamp(
            p1.energy,
            0,
            100
        ) + "%";


    p2energy.style.width =
        clamp(
            p2.energy,
            0,
            100
        ) + "%";


    timerElement.textContent =
        Math.ceil(timeLeft);
}


/* =========================
   FINISH
========================= */

function finish(
    who,
    reason
) {

    if (ended) {
        return;
    }

    ended = true;

    running = false;


    if (
        who === "HÒA!"
    ) {

        winner.textContent =
            "⚡ HÒA TRẬN ⚡";

    }
    else {

        winner.textContent =
            "🏆 " +
            who +
            " THẮNG!";
    }


    resultText.textContent =
        reason;


    message.style.display =
        "flex";
}


/* =========================
   MAIN LOOP
========================= */

function loop(timestamp) {

    var dt =
        lastTime
        ? (
            timestamp -
            lastTime
        ) / 1000
        : 0;

    lastTime =
        timestamp;

    dt =
        Math.min(
            dt,
            .033
        );


    update(dt);

    updateHUD();

    draw();


    requestAnimationFrame(
        loop
    );
}


/* =========================
   KEYBOARD
========================= */

document.addEventListener(
    "keydown",
    function (e) {

        var key =
            e.key.toLowerCase();

        keys[key] = true;


        if (
            [
                "arrowup",
                "arrowdown",
                "arrowleft",
                "arrowright",
                " "
            ].indexOf(key) >= 0
        ) {

            e.preventDefault();
        }


        if (!running) {
            return;
        }


        if (key === "f") {
            normalAttack(
                p1,
                p2
            );
        }


        if (key === "g") {
            skill(
                p1,
                p2
            );
        }


        if (key === "h") {
            ultimate(
                p1,
                p2
            );
        }


        if (key === "k") {
            normalAttack(
                p2,
                p1
            );
        }


        if (key === "l") {
            skill(
                p2,
                p1
            );
        }


        if (key === "o") {
            ultimate(
                p2,
                p1
            );
        }

    }
);


document.addEventListener(
    "keyup",
    function (e) {

        keys[
            e.key.toLowerCase()
        ] = false;

    }
);


/* =========================
   BUTTONS
========================= */

startButton.addEventListener(
    "click",
    function (e) {

        e.preventDefault();

        e.stopPropagation();

        resetGame();

        game.focus();

    }
);


againButton.addEventListener(
    "click",
    function (e) {

        e.preventDefault();

        e.stopPropagation();

        resetGame();

        game.focus();

    }
);


/* =========================
   GAME CLICK
========================= */

game.addEventListener(
    "click",
    function () {

        game.focus();

    }
);


/* =========================
   START
========================= */

initPlayers();

updateHUD();

draw();

requestAnimationFrame(
    loop
);

})();

</script>

</body>
</html>
"""

components.html(
    GAME_HTML,
    height=710,
    scrolling=False
)
