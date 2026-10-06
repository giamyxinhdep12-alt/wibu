import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Anime Clash",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Anime Clash</title>

<style>
*{
    box-sizing:border-box;
    margin:0;
    padding:0;
}

html,body{
    width:100%;
    height:100%;
    overflow:hidden;
    font-family:Arial,Helvetica,sans-serif;
    background:#050713;
    color:white;
}

body{
    display:flex;
    justify-content:center;
    align-items:center;
}

#game{
    position:relative;
    width:100vw;
    height:100vh;
    overflow:hidden;
    background:
        radial-gradient(circle at 50% 25%,rgba(90,80,255,.20),transparent 35%),
        linear-gradient(180deg,#090d20 0%,#11152d 55%,#050713 100%);
}

canvas{
    position:absolute;
    left:0;
    top:0;
    width:100%;
    height:100%;
    display:block;
}

/* ================= HOME ================= */

#mode{
    position:absolute;
    inset:0;
    z-index:50;
    display:flex;
    justify-content:center;
    align-items:center;
    background:
        radial-gradient(circle at 30% 30%,rgba(0,220,255,.18),transparent 28%),
        radial-gradient(circle at 70% 70%,rgba(255,50,120,.18),transparent 28%),
        rgba(3,5,18,.96);
}

.panel{
    width:min(900px,92vw);
    padding:38px;
    border-radius:28px;
    border:1px solid rgba(255,255,255,.15);
    background:rgba(12,16,40,.92);
    box-shadow:
        0 25px 80px rgba(0,0,0,.55),
        inset 0 0 40px rgba(100,100,255,.06);
    text-align:center;
}

.panel h1{
    font-size:clamp(38px,7vw,78px);
    letter-spacing:5px;
    margin-bottom:8px;
    background:linear-gradient(90deg,#37eaff,#fff,#ff62c7);
    -webkit-background-clip:text;
    color:transparent;
    text-shadow:0 0 30px rgba(60,220,255,.2);
}

.panel h2{
    color:#aeb9e8;
    font-size:18px;
    letter-spacing:4px;
    margin-bottom:28px;
}

.player-name{
    width:min(500px,100%);
    margin:0 auto 28px;
    text-align:left;
}

.player-name label{
    display:block;
    margin-bottom:9px;
    font-weight:bold;
    color:#dbe4ff;
}

#playerInput{
    width:100%;
    height:52px;
    border:1px solid rgba(255,255,255,.18);
    outline:none;
    border-radius:14px;
    padding:0 18px;
    color:white;
    background:#080c20;
    font-size:17px;
    transition:.2s;
}

#playerInput:focus{
    border-color:#42ddff;
    box-shadow:0 0 20px rgba(66,221,255,.15);
}

.modes{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:18px;
}

.mode{
    min-height:190px;
    border:1px solid rgba(255,255,255,.13);
    border-radius:22px;
    padding:25px;
    cursor:pointer;
    color:white;
    background:linear-gradient(
        145deg,
        rgba(25,34,80,.95),
        rgba(9,13,35,.95)
    );
    transition:.22s;
}

.mode:hover{
    transform:translateY(-6px);
    border-color:#54dfff;
    box-shadow:0 15px 40px rgba(0,200,255,.14);
}

.mode:nth-child(2):hover{
    border-color:#ff6b7e;
    box-shadow:0 15px 40px rgba(255,60,100,.14);
}

.mode b{
    display:block;
    font-size:28px;
    margin-bottom:15px;
}

.mode span{
    display:block;
    color:#aeb8db;
    line-height:1.7;
    font-size:14px;
}

/* ================= HUD ================= */

#hud{
    position:absolute;
    left:0;
    top:0;
    width:100%;
    z-index:10;
    padding:18px;
    display:flex;
    justify-content:space-between;
    pointer-events:none;
}

.hudBox{
    width:min(390px,35vw);
    padding:12px 15px;
    border-radius:16px;
    background:rgba(5,8,25,.82);
    border:1px solid rgba(255,255,255,.14);
    backdrop-filter:blur(8px);
}

.hudTop{
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:10px;
    margin-bottom:7px;
}

.name{
    font-weight:900;
    font-size:16px;
    max-width:230px;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
}

.hpText{
    font-size:12px;
    color:#aab6db;
}

.bar{
    height:12px;
    border-radius:20px;
    background:#171c34;
    overflow:hidden;
    margin-bottom:6px;
}

.hp{
    height:100%;
    width:100%;
    transition:width .15s linear;
}

.energy{
    height:7px;
    width:0%;
    transition:width .15s linear;
}

.hp1{
    background:linear-gradient(90deg,#16d9ff,#75f4ff);
}

.hp2{
    background:linear-gradient(90deg,#ff435f,#ff9b76);
}

.en1{
    background:linear-gradient(90deg,#3c9cff,#a5e8ff);
}

.en2{
    background:linear-gradient(90deg,#a64cff,#f0a1ff);
}

#timer{
    position:absolute;
    top:18px;
    left:50%;
    transform:translateX(-50%);
    z-index:12;
    min-width:75px;
    text-align:center;
    padding:9px 16px;
    border-radius:14px;
    background:rgba(5,8,25,.9);
    border:1px solid rgba(255,255,255,.16);
    font-weight:900;
    font-size:23px;
    box-shadow:0 0 30px rgba(100,100,255,.15);
}

/* ================= COUNTDOWN ================= */

#countdown{
    position:absolute;
    inset:0;
    z-index:25;
    display:none;
    justify-content:center;
    align-items:center;
    pointer-events:none;
}

#countText{
    font-size:clamp(80px,17vw,190px);
    font-weight:1000;
    font-style:italic;
    text-shadow:
        0 0 15px rgba(255,255,255,.7),
        0 0 60px rgba(70,210,255,.55);
    animation:countPop .55s ease;
}

@keyframes countPop{
    0%{
        transform:scale(.25);
        opacity:0;
    }
    70%{
        transform:scale(1.15);
        opacity:1;
    }
    100%{
        transform:scale(1);
        opacity:1;
    }
}

/* ================= RESULT ================= */

#result{
    position:absolute;
    inset:0;
    z-index:40;
    display:none;
    justify-content:center;
    align-items:center;
    background:rgba(2,4,15,.74);
    backdrop-filter:blur(6px);
}

#result.show{
    display:flex;
}

.resultPanel{
    width:min(700px,90vw);
    text-align:center;
    padding:40px 30px;
    border-radius:30px;
    background:rgba(12,17,43,.96);
    border:1px solid rgba(255,255,255,.15);
    box-shadow:0 25px 80px rgba(0,0,0,.65);
    animation:resultIn .5s ease;
}

@keyframes resultIn{
    from{
        transform:scale(.75);
        opacity:0;
    }
    to{
        transform:scale(1);
        opacity:1;
    }
}

#resultTitle{
    font-size:clamp(30px,5vw,55px);
    font-weight:1000;
    line-height:1.3;
    margin-bottom:25px;
}

#resultTitle small{
    display:block;
    margin-top:18px;
    color:#aeb8db;
    font-size:15px;
    font-weight:500;
}

.restart{
    border:0;
    border-radius:14px;
    padding:14px 30px;
    font-size:16px;
    font-weight:900;
    cursor:pointer;
    color:white;
    background:linear-gradient(90deg,#18bfe8,#9c50ff);
    box-shadow:0 10px 30px rgba(90,100,255,.2);
    transition:.2s;
}

.restart:hover{
    transform:translateY(-3px);
}

/* ================= CONTROLS ================= */

#controls{
    position:absolute;
    left:50%;
    bottom:13px;
    transform:translateX(-50%);
    z-index:10;
    padding:7px 13px;
    border-radius:12px;
    background:rgba(5,8,25,.66);
    border:1px solid rgba(255,255,255,.08);
    color:#aab6d9;
    font-size:11px;
    text-align:center;
    pointer-events:none;
}

/* ================= MOBILE ================= */

@media(max-width:750px){
    .panel{
        padding:25px 18px;
    }

    .modes{
        grid-template-columns:1fr;
    }

    .mode{
        min-height:145px;
    }

    .hudBox{
        width:38vw;
    }

    .name{
        font-size:12px;
    }

    #controls{
        display:none;
    }
}
</style>
</head>

<body>

<div id="game">

<canvas id="canvas"></canvas>

<!-- HOME -->
<div id="mode">
    <div class="panel">

        <h1>⚔️ ANIME CLASH</h1>
        <h2>CHỌN CHẾ ĐỘ CHƠI</h2>

        <div class="player-name">
            <label for="playerInput">👤 Nhập tên người chơi</label>
            <input
                id="playerInput"
                type="text"
                maxlength="20"
                placeholder="Ví dụ: NguyenVanAn"
                autocomplete="off"
            >
        </div>

        <div class="modes">

            <button class="mode" onclick="chooseMode('1v1')">
                <b>⚔️ 1V1</b>
                <span>
                    Hai người chơi đấu trực tiếp.<br>
                    P1: A D W S J K L U I O P<br>
                    P2: phím mũi tên + 1 → 7
                </span>
            </button>

            <button class="mode" onclick="chooseMode('cpu')">
                <b>🤖 ĐẤU VỚI MÁY</b>
                <span>
                    Người chơi đấu với CPU.<br>
                    CPU tự di chuyển và sử dụng kỹ năng.
                </span>
            </button>

        </div>
    </div>
</div>

<!-- HUD -->
<div id="hud">

    <div class="hudBox">

        <div class="hudTop">
            <div class="name" id="leftName">PLAYER 1</div>
            <div class="hpText" id="leftHP">100 HP</div>
        </div>

        <div class="bar">
            <div id="hp1" class="hp hp1"></div>
        </div>

        <div class="bar">
            <div id="en1" class="energy en1"></div>
        </div>

    </div>

    <div class="hudBox">

        <div class="hudTop">
            <div class="name" id="rightName">PLAYER 2</div>
            <div class="hpText" id="rightHP">100 HP</div>
        </div>

        <div class="bar">
            <div id="hp2" class="hp hp2"></div>
        </div>

        <div class="bar">
            <div id="en2" class="energy en2"></div>
        </div>

    </div>

</div>

<div id="timer">60</div>

<!-- COUNTDOWN -->
<div id="countdown">
    <div id="countText">3</div>
</div>

<!-- RESULT -->
<div id="result">

    <div class="resultPanel">

        <div id="resultTitle"></div>

        <button class="restart" onclick="location.reload()">
            🔄 CHƠI LẠI
        </button>

    </div>

</div>

<div id="controls">
    P1: A/D di chuyển • W nhảy • S rơi nhanh • J đánh • K skill • L dash • U heavy • I ultimate • O hồi • P power
    &nbsp;&nbsp;|&nbsp;&nbsp;
    P2: ←/→ di chuyển • ↑ nhảy • ↓ rơi • 1→7 kỹ năng
</div>

<script>

const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let W = window.innerWidth;
let H = window.innerHeight;

function resize(){

    W = window.innerWidth;
    H = window.innerHeight;

    canvas.width = W;
    canvas.height = H;
}

window.addEventListener("resize",resize);
resize();

/* ================= GAME STATE ================= */

let mode = null;
let playerName = "PLAYER 1";

let started = false;
let ended = false;

let p1 = null;
let p2 = null;

let fighters = [];
let particles = [];
let projectiles = [];

let keys = {};

let gameTime = 60;
let lastTime = performance.now();

window.addEventListener("keydown",(e)=>{

    keys[e.key.toLowerCase()] = true;

    if([
        "arrowup",
        "arrowdown",
        "arrowleft",
        "arrowright",
        " "
    ].includes(e.key.toLowerCase())){
        e.preventDefault();
    }
});

window.addEventListener("keyup",(e)=>{

    keys[e.key.toLowerCase()] = false;
});

/* ================= UTIL ================= */

function clamp(v,min,max){
    return Math.max(min,Math.min(max,v));
}

function distance(a,b){

    return Math.abs(a.x-b.x);
}

function random(min,max){

    return Math.random()*(max-min)+min;
}

/* ================= PARTICLES ================= */

function particle(x,y,color,count=8){

    for(let i=0;i<count;i++){

        particles.push({
            x:x,
            y:y,
            vx:random(-220,220),
            vy:random(-300,80),
            life:random(.3,.7),
            maxLife:.7,
            size:random(3,8),
            color:color
        });
    }
}

function updateParticles(dt){

    for(let i=particles.length-1;i>=0;i--){

        let p = particles[i];

        p.x += p.vx*dt;
        p.y += p.vy*dt;

        p.vy += 700*dt;
        p.life -= dt;

        if(p.life<=0){
            particles.splice(i,1);
        }
    }
}

function drawParticles(){

    for(const p of particles){

        ctx.globalAlpha = Math.max(0,p.life/p.maxLife);

        ctx.fillStyle = p.color;

        ctx.beginPath();
        ctx.arc(p.x,p.y,p.size,0,Math.PI*2);
        ctx.fill();
    }

    ctx.globalAlpha = 1;
}

/* ================= FIGHTER ================= */

class Fighter{

    constructor(id,team,x,mainColor,glowColor,name,isCPU){

        this.id = id;
        this.team = team;

        this.x = x;
        this.y = H-155;

        this.vx = 0;
        this.vy = 0;

        this.width = 58;
        this.height = 110;

        this.mainColor = mainColor;
        this.glowColor = glowColor;

        this.name = name;
        this.isCPU = isCPU;

        this.hp = 100;
        this.energy = 0;

        this.speed = 280;
        this.jumpPower = -600;
        this.gravity = 1450;

        this.facing = team===1 ? 1 : -1;

        this.attackCooldown = 0;
        this.skillCooldown = 0;
        this.dashCooldown = 0;
        this.heavyCooldown = 0;
        this.ultimateCooldown = 0;
        this.recoverCooldown = 0;
        this.powerCooldown = 0;

        this.attackTimer = 0;
        this.hitFlash = 0;

        this.onGround = true;

        this.cpuTimer = random(.2,.8);
        this.cpuActionTimer = 0;
    }

    alive(){

        return this.hp > 0;
    }

    updateCooldowns(dt){

        this.attackCooldown = Math.max(0,this.attackCooldown-dt);
        this.skillCooldown = Math.max(0,this.skillCooldown-dt);
        this.dashCooldown = Math.max(0,this.dashCooldown-dt);
        this.heavyCooldown = Math.max(0,this.heavyCooldown-dt);
        this.ultimateCooldown = Math.max(0,this.ultimateCooldown-dt);
        this.recoverCooldown = Math.max(0,this.recoverCooldown-dt);
        this.powerCooldown = Math.max(0,this.powerCooldown-dt);

        this.attackTimer = Math.max(0,this.attackTimer-dt);
        this.hitFlash = Math.max(0,this.hitFlash-dt);
    }

    move(){

        if(!this.alive()) return;

        let left = false;
        let right = false;

        if(this.id==="p1"){

            left = keys["a"];
            right = keys["d"];

            if(keys["w"] && this.onGround){
                this.vy = this.jumpPower;
                this.onGround = false;
            }

            if(keys["s"]){
                this.vy += 900;
            }

            if(keys["j"]) this.attack();
            if(keys["k"]) this.skill();
            if(keys["l"]) this.dash();
            if(keys["u"]) this.heavy();
            if(keys["i"]) this.ultimate();
            if(keys["o"]) this.recover();
            if(keys["p"]) this.power();

        }else if(!this.isCPU){

            left = keys["arrowleft"];
            right = keys["arrowright"];

            if(keys["arrowup"] && this.onGround){
                this.vy = this.jumpPower;
                this.onGround = false;
            }

            if(keys["arrowdown"]){
                this.vy += 900;
            }

            if(keys["1"]) this.attack();
            if(keys["2"]) this.skill();
            if(keys["3"]) this.dash();
            if(keys["4"]) this.heavy();
            if(keys["5"]) this.ultimate();
            if(keys["6"]) this.recover();
            if(keys["7"]) this.power();
        }

        if(left){

            this.vx = -this.speed;
            this.facing = -1;

        }else if(right){

            this.vx = this.speed;
            this.facing = 1;

        }else{

            this.vx *= .78;
        }
    }

    cpu(){

        if(!this.isCPU || !this.alive() || !p1 || !p1.alive()) return;

        const d = p1.x-this.x;

        this.cpuTimer -= 1/60;
        this.cpuActionTimer -= 1/60;

        if(this.cpuTimer<=0){

            this.cpuTimer = random(.12,.32);

            if(Math.abs(d)>150){

                if(d>0){

                    this.vx = this.speed*.72;
                    this.facing = 1;

                }else{

                    this.vx = -this.speed*.72;
                    this.facing = -1;
                }

            }else{

                this.vx *= .5;

                if(Math.random()<.7){

                    this.facing = d>=0 ? 1 : -1;
                }
            }

            if(this.onGround && Math.random()<.08){

                this.vy = this.jumpPower;
                this.onGround = false;
            }
        }

        if(this.cpuActionTimer<=0){

            this.cpuActionTimer = random(.35,.75);

            const ad = Math.abs(d);

            if(ad<110 && this.attackCooldown<=0){

                this.attack();

            }else if(ad<400 && this.energy>=25 && this.skillCooldown<=0){

                this.skill();

            }else if(ad<300 && this.energy>=100 && this.ultimateCooldown<=0){

                this.ultimate();

            }else if(ad<140 && this.heavyCooldown<=0 && Math.random()<.5){

                this.heavy();

            }else if(this.energy<100 && this.powerCooldown<=0 && Math.random()<.25){

                this.power();
            }
        }
    }

    attack(){

        if(this.attackCooldown>0 || !this.alive()) return;

        this.attackCooldown = .38;
        this.attackTimer = .18;

        const target = this.enemy();

        if(!target || !target.alive()) return;

        const d = target.x-this.x;

        if(Math.abs(d)<105 && Math.sign(d)===this.facing){

            this.hit(target,7);

            particle(
                target.x,
                target.y-50,
                this.team===1 ? "#68efff" : "#ff6b58",
                12
            );
        }

        this.energy = clamp(this.energy+7,0,100);
    }

    skill(){

        if(this.skillCooldown>0 || this.energy<25 || !this.alive()) return;

        this.skillCooldown = .65;
        this.energy -= 25;

        const dir = this.facing;

        projectiles.push({
            owner:this,
            x:this.x+dir*40,
            y:this.y-62,
            vx:dir*720,
            life:1.2,
            damage:15,
            color:this.team===1 ? "#4cecff" : "#ff604b",
            size:10
        });

        particle(
            this.x+dir*35,
            this.y-60,
            this.glowColor,
            10
        );
    }

    dash(){

        if(this.dashCooldown>0 || !this.alive()) return;

        this.dashCooldown = .9;

        this.x += this.facing*130;

        this.x = clamp(
            this.x,
            45,
            W-45
        );

        particle(
            this.x,
            this.y-50,
            this.glowColor,
            16
        );
    }

    heavy(){

        if(this.heavyCooldown>0 || !this.alive()) return;

        this.heavyCooldown = 1.05;

        const target = this.enemy();

        if(!target || !target.alive()) return;

        const d = target.x-this.x;

        if(Math.abs(d)<135 && Math.sign(d)===this.facing){

            this.hit(target,12);

            particle(
                target.x,
                target.y-55,
                "#ffffff",
                20
            );
        }

        this.energy = clamp(this.energy+12,0,100);
    }

    ultimate(){

        if(
            this.ultimateCooldown>0 ||
            this.energy<100 ||
            !this.alive()
        ) return;

        this.ultimateCooldown = 4;
        this.energy = 0;

        const target = this.enemy();

        if(!target || !target.alive()) return;

        const d = target.x-this.x;

        if(Math.abs(d)<330 && Math.sign(d)===this.facing){

            this.hit(target,32);

            particle(
                target.x,
                target.y-60,
                "#fff3a0",
                45
            );
        }

        particle(
            this.x,
            this.y-60,
            this.glowColor,
            35
        );
    }

    recover(){

        if(
            this.recoverCooldown>0 ||
            this.energy<35 ||
            !this.alive()
        ) return;

        this.recoverCooldown = 3;
        this.energy -= 35;

        this.hp = clamp(this.hp+15,0,100);

        particle(
            this.x,
            this.y-55,
            "#65ffb4",
            25
        );
    }

    power(){

        if(
            this.powerCooldown>0 ||
            this.energy>=100 ||
            !this.alive()
        ) return;

        this.powerCooldown = 1.2;

        this.energy = clamp(
            this.energy+20,
            0,
            100
        );

        particle(
            this.x,
            this.y-55,
            this.glowColor,
            14
        );
    }

    hit(target,damage){

        if(!target || !target.alive()) return;

        target.hp = clamp(
            target.hp-damage,
            0,
            100
        );

        target.hitFlash = .12;

        target.x += this.facing*25;

        target.x = clamp(
            target.x,
            45,
            W-45
        );
    }

    enemy(){

        return this===p1 ? p2 : p1;
    }

    physics(dt){

        if(!this.alive()) return;

        this.x += this.vx*dt;

        this.vy += this.gravity*dt;

        this.y += this.vy*dt;

        const floor = H-155;

        if(this.y>=floor){

            this.y=floor;
            this.vy=0;
            this.onGround=true;

        }else{

            this.onGround=false;
        }

        this.x = clamp(
            this.x,
            45,
            W-45
        );
    }

    draw(){

        if(!this.alive()) return;

        const x=this.x;
        const y=this.y;

        /* shadow */

        ctx.save();

        ctx.globalAlpha=.28;

        ctx.fillStyle="#000";

        ctx.beginPath();

        ctx.ellipse(
            x,
            y+7,
            48,
            11,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.restore();

        /* glow */

        ctx.save();

        ctx.globalAlpha=.22;

        ctx.fillStyle=this.glowColor;

        ctx.beginPath();

        ctx.arc(
            x,
            y-58,
            58,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.restore();

        /* body */

        ctx.save();

        if(this.hitFlash>0){

            ctx.fillStyle="#ffffff";

        }else{

            ctx.fillStyle=this.mainColor;
        }

        ctx.shadowColor=this.glowColor;
        ctx.shadowBlur=18;

        roundRect(
            ctx,
            x-25,
            y-82,
            50,
            76,
            14
        );

        ctx.fill();

        ctx.shadowBlur=0;

        /* head */

        ctx.beginPath();

        ctx.arc(
            x,
            y-105,
            27,
            0,
            Math.PI*2
        );

        ctx.fill();

        /* hair */

        ctx.fillStyle=this.team===1
            ? "#071d37"
            : "#39100d";

        ctx.beginPath();

        ctx.moveTo(x-27,y-108);
        ctx.lineTo(x-20,y-132);
        ctx.lineTo(x-8,y-121);
        ctx.lineTo(x+2,y-139);
        ctx.lineTo(x+13,y-120);
        ctx.lineTo(x+28,y-129);
        ctx.lineTo(x+25,y-103);
        ctx.closePath();

        ctx.fill();

        /* eyes */

        ctx.fillStyle="#ffffff";

        ctx.beginPath();

        ctx.ellipse(
            x+this.facing*10,
            y-105,
            6,
            4,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

        /* arm */

        ctx.strokeStyle=this.glowColor;
        ctx.lineWidth=10;
        ctx.lineCap="round";

        ctx.beginPath();

        ctx.moveTo(
            x+this.facing*18,
            y-63
        );

        ctx.lineTo(
            x+this.facing*47,
            y-55
        );

        ctx.stroke();

        /* attack effect */

        if(this.attackTimer>0){

            ctx.strokeStyle="#ffffff";
            ctx.lineWidth=6;
            ctx.globalAlpha=.8;

            ctx.beginPath();

            ctx.arc(
                x+this.facing*15,
                y-62,
                55,
                this.facing===1 ? -.7 : Math.PI+.7,
                this.facing===1 ? .7 : Math.PI-.7
            );

            ctx.stroke();

            ctx.globalAlpha=1;
        }

        ctx.restore();

        /* name */

        ctx.save();

        ctx.textAlign="center";
        ctx.font="bold 13px Arial";

        ctx.fillStyle="#ffffff";
        ctx.shadowColor="#000";
        ctx.shadowBlur=5;

        ctx.fillText(
            this.name,
            x,
            y-145
        );

        ctx.restore();
    }
}

/* ================= ROUND RECT ================= */

function roundRect(ctx,x,y,w,h,r){

    ctx.beginPath();

    ctx.moveTo(x+r,y);

    ctx.arcTo(
        x+w,y,
        x+w,y+h,
        r
    );

    ctx.arcTo(
        x+w,y+h,
        x,y+h,
        r
    );

    ctx.arcTo(
        x,y+h,
        x,y,
        r
    );

    ctx.arcTo(
        x,y,
        x+w,y,
        r
    );

    ctx.closePath();
}

/* ================= BACKGROUND ================= */

function background(){

    const sky = ctx.createLinearGradient(
        0,
        0,
        0,
        H
    );

    sky.addColorStop(0,"#080b22");
    sky.addColorStop(.55,"#111735");
    sky.addColorStop(1,"#050611");

    ctx.fillStyle=sky;

    ctx.fillRect(
        0,
        0,
        W,
        H
    );

    /* moon */

    ctx.save();

    ctx.globalAlpha=.12;

    ctx.fillStyle="#b6caff";

    ctx.beginPath();

    ctx.arc(
        W*.5,
        H*.24,
        Math.min(W,H)*.12,
        0,
        Math.PI*2
    );

    ctx.fill();

    ctx.restore();

    /* stars */

    ctx.save();

    ctx.globalAlpha=.5;

    for(let i=0;i<70;i++){

        const x=(i*173)%W;
        const y=(i*97)%(H*.6);

        const s=(i%3)+1;

        ctx.fillStyle="#ffffff";

        ctx.fillRect(
            x,
            y,
            s,
            s
        );
    }

    ctx.restore();

    /* distant city */

    ctx.fillStyle="rgba(18,23,50,.85)";

    for(let i=0;i<25;i++){

        const bw=30+(i%5)*15;
        const bh=50+(i%7)*25;
        const bx=i*(W/25);

        ctx.fillRect(
            bx,
            H-145-bh,
            bw,
            bh
        );
    }

    /* arena */

    const floorY=H-145;

    const floor = ctx.createLinearGradient(
        0,
        floorY,
        0,
        H
    );

    floor.addColorStop(0,"#151d3b");
    floor.addColorStop(1,"#050611");

    ctx.fillStyle=floor;

    ctx.fillRect(
        0,
        floorY,
        W,
        H-floorY
    );

    ctx.strokeStyle="rgba(100,190,255,.12)";
    ctx.lineWidth=1;

    for(let x=0;x<W;x+=60){

        ctx.beginPath();

        ctx.moveTo(x,floorY);
        ctx.lineTo(
            W/2+(x-W/2)*.45,
            H
        );

        ctx.stroke();
    }

    for(let y=floorY;y<H;y+=35){

        ctx.beginPath();

        ctx.moveTo(0,y);
        ctx.lineTo(W,y);

        ctx.stroke();
    }

    ctx.strokeStyle="rgba(100,220,255,.25)";
    ctx.lineWidth=3;

    ctx.beginPath();

    ctx.moveTo(
        0,
        floorY
    );

    ctx.lineTo(
        W,
        floorY
    );

    ctx.stroke();
}

/* ================= PROJECTILES ================= */

function updateProjectiles(dt){

    for(let i=projectiles.length-1;i>=0;i--){

        const p=projectiles[i];

        p.x += p.vx*dt;
        p.life -= dt;

        const target =
            p.owner===p1 ? p2 : p1;

        if(
            target &&
            target.alive() &&
            Math.abs(target.x-p.x)<45 &&
            Math.abs((target.y-60)-p.y)<75
        ){

            p.owner.hit(
                target,
                p.damage
            );

            particle(
                target.x,
                target.y-55,
                p.color,
                18
            );

            projectiles.splice(i,1);
            continue;
        }

        if(
            p.life<=0 ||
            p.x<-100 ||
            p.x>W+100
        ){

            projectiles.splice(i,1);
        }
    }
}

function drawProjectiles(){

    for(const p of projectiles){

        ctx.save();

        ctx.shadowColor=p.color;
        ctx.shadowBlur=25;

        ctx.fillStyle=p.color;

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.restore();
    }
}

/* ================= HUD ================= */

function updateHUD(){

    if(!p1 || !p2) return;

    document.getElementById("leftName").textContent =
        p1.name;

    document.getElementById("rightName").textContent =
        p2.name;

    document.getElementById("leftHP").textContent =
        Math.round(p1.hp)+" HP";

    document.getElementById("rightHP").textContent =
        Math.round(p2.hp)+" HP";

    document.getElementById("hp1").style.width =
        p1.hp+"%";

    document.getElementById("hp2").style.width =
        p2.hp+"%";

    document.getElementById("en1").style.width =
        p1.energy+"%";

    document.getElementById("en2").style.width =
        p2.energy+"%";

    document.getElementById("timer").textContent =
        Math.max(0,Math.ceil(gameTime));
}

/* ================= SETUP ================= */

function setup(modeName){

    mode=modeName;

    started=false;
    ended=false;

    gameTime=60;

    particles=[];
    projectiles=[];
    fighters=[];

    p1 = new Fighter(
        "p1",
        1,
        W*.25,
        "#16d7e8",
        "#82f6ff",
        playerName,
        false
    );

    if(mode==="cpu"){

        p2 = new Fighter(
            "p2",
            2,
            W*.75,
            "#ff553d",
            "#ff9d77",
            "CPU",
            true
        );

    }else{

        p2 = new Fighter(
            "p2",
            2,
            W*.75,
            "#ff553d",
            "#ff9d77",
            "PLAYER 2",
            false
        );
    }

    fighters=[
        p1,
        p2
    ];

    document.getElementById("leftName").textContent =
        p1.name;

    document.getElementById("rightName").textContent =
        p2.name;

    document.getElementById("mode").style.display="none";

    startCountdown();
}

/* ================= CHOOSE MODE ================= */

function chooseMode(selectedMode){

    const input =
        document.getElementById("playerInput");

    let entered =
        input.value.trim();

    entered =
        entered
        .replace(/[<>]/g,"")
        .slice(0,20);

    if(entered.length===0){

        playerName="PLAYER 1";

    }else{

        playerName=entered;
    }

    setup(selectedMode);
}

/* ================= COUNTDOWN ================= */

function startCountdown(){

    const box =
        document.getElementById("countdown");

    const text =
        document.getElementById("countText");

    box.style.display="flex";

    const sequence=[
        "3",
        "2",
        "1",
        "FIGHT!"
    ];

    let index=0;

    function next(){

        if(index>=sequence.length){

            box.style.display="none";

            started=true;
            lastTime=performance.now();

            return;
        }

        text.textContent=
            sequence[index];

        text.style.animation="none";

        void text.offsetWidth;

        text.style.animation=
            "countPop .55s ease";

        index++;

        setTimeout(
            next,
            index===sequence.length ? 700 : 800
        );
    }

    next();
}

/* ================= FINISH ================= */

function finish(){

    if(ended) return;

    ended=true;

    let title="";

    const playerWon =
        p1.hp>0 &&
        p2.hp<=0;

    const playerLost =
        p1.hp<=0 &&
        p2.hp>0;

    if(playerWon){

        title =
            "🎉 CHÚC MỪNG " +
            p1.name +
            "!<br>" +
            "🏆 BẠN ĐÃ CHIẾN THẮNG!";

    }else if(playerLost){

        title =
            "💔 RẤT TIẾC " +
            p1.name +
            "!<br>" +
            "😭 CHIA BUỒN, BẠN ĐÃ THUA!";

    }else{

        if(p1.hp>p2.hp){

            title =
                "🎉 CHÚC MỪNG " +
                p1.name +
                "!<br>" +
                "🏆 BẠN THẮNG THEO ĐIỂM!";

        }else if(p2.hp>p1.hp){

            title =
                "💔 RẤT TIẾC " +
                p1.name +
                "!<br>" +
                "😭 CHIA BUỒN, BẠN ĐÃ THUA!";

        }else{

            title =
                "🤝 TRẬN ĐẤU HÒA!";
        }
    }

    title +=
        `<small>
        ${p1.name}: ${Math.round(p1.hp)} HP
        &nbsp; • &nbsp;
        ${p2.name}: ${Math.round(p2.hp)} HP
        </small>`;

    document.getElementById(
        "resultTitle"
    ).innerHTML=title;

    document.getElementById(
        "result"
    ).classList.add("show");

    /* hiệu ứng chúc mừng */

    if(playerWon){

        for(let i=0;i<90;i++){

            setTimeout(()=>{

                particle(
                    random(0,W),
                    random(0,H*.7),
                    [
                        "#ffe66d",
                        "#ff69b4",
                        "#6ee7ff",
                        "#8aff80",
                        "#ffffff"
                    ][
                        Math.floor(
                            Math.random()*5
                        )
                    ],
                    3
                );

            },i*12);
        }
    }
}

/* ================= UPDATE ================= */

function update(dt){

    if(!started || ended) return;

    gameTime -= dt;

    if(gameTime<=0){

        gameTime=0;

        if(p1.hp>p2.hp){

            p2.hp=0;

        }else if(p2.hp>p1.hp){

            p1.hp=0;
        }

        finish();

        return;
    }

    for(const f of fighters){

        f.updateCooldowns(dt);
        f.move();
        f.cpu();
        f.physics(dt);
    }

    updateProjectiles(dt);
    updateParticles(dt);

    if(!p1.alive() || !p2.alive()){

        finish();
    }

    updateHUD();
}

/* ================= DRAW ================= */

function draw(){

    background();

    drawProjectiles();

    for(const f of fighters){

        f.draw();
    }

    drawParticles();
}

/* ================= LOOP ================= */

function loop(now){

    const dt =
        Math.min(
            .033,
            (now-lastTime)/1000
        );

    lastTime=now;

    update(dt);
    draw();

    requestAnimationFrame(loop);
}

requestAnimationFrame(loop);

</script>

</div>

</body>
</html>
"""

components.html(
    HTML,
    height=850,
    scrolling=False
)
