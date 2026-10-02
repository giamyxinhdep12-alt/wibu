import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Anime Clash 1v1",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">

<style>
html,body{
    margin:0;
    padding:0;
    width:100%;
    height:100%;
    overflow:hidden;
    background:#05060b;
    font-family:Arial,Helvetica,sans-serif;
}

*{
    box-sizing:border-box;
    user-select:none;
}

#game{
    position:fixed;
    inset:0;
    width:100vw;
    height:100vh;
    display:block;
}

#hud{
    position:fixed;
    top:12px;
    left:50%;
    transform:translateX(-50%);
    width:min(1180px,94vw);
    z-index:20;
    pointer-events:none;
}

#bars{
    display:grid;
    grid-template-columns:1fr 110px 1fr;
    gap:12px;
    align-items:center;
}

.bar{
    height:31px;
    background:#090b11;
    border:2px solid rgba(255,255,255,.9);
    border-radius:7px;
    overflow:hidden;
    box-shadow:0 0 14px rgba(0,0,0,.8);
}

.fill{
    height:100%;
    width:100%;
    transition:width .08s linear;
}

#hp1{
    background:linear-gradient(90deg,#007f91,#39f0ff);
}

#hp2{
    background:linear-gradient(90deg,#ff3b16,#ffbd32);
}

#timer{
    color:white;
    text-align:center;
    font-size:30px;
    font-weight:900;
    text-shadow:0 0 12px white;
}

.names{
    display:grid;
    grid-template-columns:1fr 110px 1fr;
    margin-top:4px;
    color:white;
    font-weight:bold;
    font-size:13px;
}

.names div:nth-child(1){
    text-align:left;
    color:#46eaff;
}

.names div:nth-child(3){
    text-align:right;
    color:#ff7138;
}

#energy{
    display:grid;
    grid-template-columns:1fr 110px 1fr;
    gap:12px;
    margin-top:6px;
}

.energybar{
    height:8px;
    background:#101116;
    border:1px solid rgba(255,255,255,.45);
    overflow:hidden;
    border-radius:5px;
}

.energyfill{
    width:0%;
    height:100%;
}

#en1{
    background:#38e8ff;
}

#en2{
    background:#ff682e;
}

#mute{
    position:fixed;
    right:16px;
    top:14px;
    z-index:50;
    color:white;
    background:rgba(10,10,16,.8);
    border:1px solid rgba(255,255,255,.5);
    border-radius:8px;
    padding:8px 12px;
    cursor:pointer;
}

#controls{
    position:fixed;
    left:50%;
    bottom:12px;
    transform:translateX(-50%);
    color:rgba(255,255,255,.72);
    font-size:12px;
    text-align:center;
    z-index:15;
    pointer-events:none;
}

#overlay{
    position:fixed;
    inset:0;
    z-index:40;
    display:flex;
    align-items:center;
    justify-content:center;
    background:
        radial-gradient(
            circle at center,
            rgba(20,30,65,.45),
            rgba(0,0,0,.88)
        );
}

.panel{
    width:min(720px,92vw);
    padding:32px;
    border-radius:18px;
    color:white;
    text-align:center;
    background:rgba(7,9,17,.95);
    border:1px solid rgba(255,255,255,.45);
    box-shadow:
        0 0 60px rgba(0,0,0,.9),
        inset 0 0 30px rgba(255,255,255,.03);
}

.panel h1{
    margin:0 0 8px;
    font-size:46px;
    letter-spacing:2px;
}

.panel h2{
    margin:8px 0 18px;
    color:#ddd;
}

.panel p{
    color:#bbb;
    line-height:1.65;
}

.start{
    margin-top:16px;
    padding:13px 34px;
    border:0;
    border-radius:9px;
    background:white;
    color:#111;
    font-weight:900;
    font-size:17px;
    cursor:pointer;
}

.start:hover{
    transform:scale(1.04);
}

#countdown{
    position:fixed;
    inset:0;
    z-index:35;
    display:none;
    align-items:center;
    justify-content:center;
    color:white;
    font-size:115px;
    font-weight:900;
    text-shadow:
        0 0 15px white,
        0 0 50px rgba(100,200,255,.8);
    pointer-events:none;
}

#flash{
    position:fixed;
    inset:0;
    z-index:34;
    pointer-events:none;
    opacity:0;
}
</style>
</head>

<body>

<canvas id="game"></canvas>

<div id="hud">

    <div id="bars">

        <div class="bar">
            <div id="hp1" class="fill"></div>
        </div>

        <div id="timer">60</div>

        <div class="bar">
            <div id="hp2" class="fill"></div>
        </div>

    </div>

    <div class="names">
        <div>WATER PLAYER</div>
        <div></div>
        <div>FLAME PLAYER</div>
    </div>

    <div id="energy">

        <div class="energybar">
            <div id="en1" class="energyfill"></div>
        </div>

        <div></div>

        <div class="energybar">
            <div id="en2" class="energyfill"></div>
        </div>

    </div>

</div>

<button id="mute">🔊</button>

<div id="countdown"></div>
<div id="flash"></div>

<div id="overlay">

    <div class="panel">

        <h1>⚔️ ANIME CLASH</h1>

        <h2>WATER VS FLAME</h2>

        <p>
            Japanese night arena · 1 VS 1
        </p>

        <p>
            <b>PLAYER 1 — WATER</b><br>
            A / D = Move<br>
            W = Jump · S = Fast Fall<br>
            J = Attack · K = Skill · L = Dash<br>
            U = Heavy · I = Ultimate<br>
            O = Recover · P = Power Up
        </p>

        <p>
            <b>PLAYER 2 — FLAME</b><br>
            ← / → = Move<br>
            ↑ = Jump · ↓ = Fast Fall<br>
            1 = Attack · 2 = Skill · 3 = Dash<br>
            4 = Heavy · 5 = Ultimate<br>
            6 = Recover · 7 = Power Up
        </p>

        <button class="start" onclick="startBattle()">
            START BATTLE
        </button>

    </div>

</div>

<div id="controls">
    P1: A D W S J K L U I O P
    &nbsp;&nbsp; | &nbsp;&nbsp;
    P2: ← → ↑ ↓ 1 2 3 4 5 6 7
</div>

<script>

"use strict";

/* =========================================================
   CANVAS
========================================================= */

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

let W = 0;
let H = 0;
let DPR = window.devicePixelRatio || 1;

function resize(){

    DPR = window.devicePixelRatio || 1;

    W = window.innerWidth;
    H = window.innerHeight;

    canvas.width = Math.floor(W * DPR);
    canvas.height = Math.floor(H * DPR);

    canvas.style.width = W + "px";
    canvas.style.height = H + "px";

    ctx.setTransform(DPR,0,0,DPR,0,0);
}

window.addEventListener("resize",resize);
resize();


/* =========================================================
   INPUT
========================================================= */

const keys = {};
const pressed = {};

window.addEventListener("keydown",(e)=>{

    const k = e.key.toLowerCase();

    keys[k] = true;

    if(!pressed[k]){
        pressed[k] = true;
    }

    const prevent = [
        "arrowleft",
        "arrowright",
        "arrowup",
        "arrowdown",
        " ",
        "w","a","s","d",
        "j","k","l","u","i","o","p"
    ];

    if(prevent.includes(k)){
        e.preventDefault();
    }

});

window.addEventListener("keyup",(e)=>{

    const k = e.key.toLowerCase();

    keys[k] = false;
    pressed[k] = false;

});


function down(k){
    return keys[k] === true;
}


/* =========================================================
   GAME STATE
========================================================= */

let gameStarted = false;
let gameOver = false;

let timeLeft = 60;

let lastTime = performance.now();

let screenShake = 0;
let hitStop = 0;

let muted = false;

let arenaTime = 0;


/* =========================================================
   UTILS
========================================================= */

function clamp(v,min,max){
    return Math.max(min,Math.min(max,v));
}

function rand(min,max){
    return Math.random()*(max-min)+min;
}

function dist(a,b){
    return Math.abs(a-b);
}


/* =========================================================
   EFFECT ARRAYS
========================================================= */

const particles = [];
const slashEffects = [];
const shockwaves = [];
const floatingTexts = [];
const waterEffects = [];
const flameEffects = [];
const projectiles = [];


/* =========================================================
   PARTICLES
========================================================= */

function particle(
    x,
    y,
    color,
    amount=10,
    power=4,
    sizeMin=2,
    sizeMax=6
){

    for(let i=0;i<amount;i++){

        particles.push({

            x:x,
            y:y,

            vx:rand(-power,power),
            vy:rand(-power,power),

            gravity:rand(.03,.12),

            life:rand(.25,.8),
            maxLife:.8,

            size:rand(sizeMin,sizeMax),

            color:color

        });

    }

}


/* =========================================================
   TEXT
========================================================= */

function textEffect(x,y,text,color){

    floatingTexts.push({

        x:x,
        y:y,

        text:text,

        color:color,

        life:1,
        maxLife:1,

        vy:-35

    });

}


/* =========================================================
   SHOCKWAVE
========================================================= */

function shockwave(x,y,color){

    shockwaves.push({

        x:x,
        y:y,

        radius:10,

        life:.5,
        maxLife:.5,

        color:color

    });

}


/* =========================================================
   SLASH
========================================================= */

function slash(x,y,dir,color,power=1){

    slashEffects.push({

        x:x,
        y:y,

        dir:dir,

        color:color,

        power:power,

        angle:dir===1
            ?rand(-.75,.65)
            :Math.PI+rand(-.65,.75),

        size:rand(45,85)*power,

        life:.28,
        maxLife:.28

    });

}


/* =========================================================
   WATER EFFECT
========================================================= */

function waterWave(x,y,dir){

    for(let i=0;i<25;i++){

        waterEffects.push({

            x:x,
            y:y,

            vx:dir*rand(2,7),
            vy:rand(-3,3),

            life:rand(.35,.8),
            maxLife:.8,

            size:rand(8,18)

        });

    }

}


/* =========================================================
   FLAME EFFECT
========================================================= */

function flameBurst(x,y,dir){

    for(let i=0;i<30;i++){

        flameEffects.push({

            x:x,
            y:y,

            vx:dir*rand(2,8),
            vy:rand(-5,3),

            life:rand(.25,.7),
            maxLife:.7,

            size:rand(7,16)

        });

    }

}


/* =========================================================
   PROJECTILE
========================================================= */

function projectile(x,y,dir,color,type,damage){

    projectiles.push({

        x:x,
        y:y,

        vx:dir*10,

        color:color,

        type:type,

        damage:damage,

        life:1.4,

        size:type==="water"?18:20

    });

}


/* =========================================================
   FIGHTER
========================================================= */

class Fighter{

    constructor(
        x,
        side,
        name,
        color,
        accent
    ){

        this.x=x;

        this.side=side;

        this.name=name;

        this.color=color;

        this.accent=accent;

        this.hp=100;

        this.energy=0;

        this.vx=0;
        this.vy=0;

        this.y=0;

        this.ground=true;

        this.facing=side;

        this.state="idle";

        this.anim=0;

        this.attackCooldown=0;

        this.skillCooldown=0;

        this.dashCooldown=0;

        this.heavyCooldown=0;

        this.ultimateCooldown=0;

        this.powerCooldown=0;

        this.recoverCooldown=0;

        this.attackTimer=0;

        this.skillTimer=0;

        this.dashTimer=0;

        this.heavyTimer=0;

        this.ultimateTimer=0;

        this.powerTimer=0;

        this.hitTimer=0;

        this.invincible=0;

        this.combo=0;

        this.comboTimer=0;

        this.maxSpeed=7;

    }


    reset(){

        this.hp=100;

        this.energy=0;

        this.vx=0;

        this.vy=0;

        this.y=0;

        this.ground=true;

        this.state="idle";

        this.attackCooldown=0;

        this.skillCooldown=0;

        this.dashCooldown=0;

        this.heavyCooldown=0;

        this.ultimateCooldown=0;

        this.powerCooldown=0;

        this.recoverCooldown=0;

        this.attackTimer=0;

        this.skillTimer=0;

        this.dashTimer=0;

        this.heavyTimer=0;

        this.ultimateTimer=0;

        this.powerTimer=0;

        this.hitTimer=0;

        this.invincible=0;

        this.combo=0;

        this.comboTimer=0;

    }


    controls(){

        const p1 = this.side === 1;

        const left =
            p1 ? down("a") : down("arrowleft");

        const right =
            p1 ? down("d") : down("arrowright");

        const jump =
            p1 ? down("w") : down("arrowup");

        const fastFall =
            p1 ? down("s") : down("arrowdown");

        const attack =
            p1 ? down("j") : down("1");

        const skill =
            p1 ? down("k") : down("2");

        const dash =
            p1 ? down("l") : down("3");

        const heavy =
            p1 ? down("u") : down("4");

        const ultimate =
            p1 ? down("i") : down("5");

        const recover =
            p1 ? down("o") : down("6");

        const power =
            p1 ? down("p") : down("7");


        if(left){

            this.vx -= 1.15;

            this.facing=-1;

        }

        if(right){

            this.vx += 1.15;

            this.facing=1;

        }


        if(!left && !right){

            this.vx *= .78;

        }


        this.vx = clamp(
            this.vx,
            -this.maxSpeed,
            this.maxSpeed
        );


        if(jump && this.ground){

            this.vy=-14;

            this.ground=false;

            this.state="jump";

            particle(
                this.x,
                this.groundY(),
                this.color,
                14,
                3
            );

        }


        if(fastFall && !this.ground){

            this.vy += 1.8;

        }


        if(attack){
            this.attack();
        }

        if(skill){
            this.skill();
        }

        if(dash){
            this.dash();
        }

        if(heavy){
            this.heavy();
        }

        if(ultimate){
            this.ultimate();
        }

        if(recover){
            this.recover();
        }

        if(power){
            this.powerUp();
        }

    }


    groundY(){

        return H-145;

    }


    attack(){

        if(this.attackCooldown>0)return;

        this.attackCooldown=.28;

        this.attackTimer=.16;

        this.state="attack";

        this.combo++;

        this.comboTimer=.85;

        const reach=72;

        slash(
            this.x + this.facing*40,
            this.groundY()+this.y-70,
            this.facing,
            this.color,
            1
        );

        particle(
            this.x + this.facing*65,
            this.groundY()+this.y-70,
            this.color,
            9,
            4
        );

        if(this.side===1){

            waterWave(
                this.x+this.facing*30,
                this.groundY()+this.y-55,
                this.facing
            );

        }else{

            flameBurst(
                this.x+this.facing*30,
                this.groundY()+this.y-55,
                this.facing
            );

        }

        hitTarget(
            this,
            12,
            reach,
            "attack"
        );

    }


    skill(){

        if(
            this.skillCooldown>0 ||
            this.energy<20
        )return;

        this.energy-=20;

        this.skillCooldown=.9;

        this.skillTimer=.55;

        this.state="skill";

        const x=
            this.x+this.facing*65;

        const y=
            this.groundY()+this.y-60;

        shockwave(
            x,
            y,
            this.color
        );

        projectile(
            x,
            y,
            this.facing,
            this.color,
            this.side===1?"water":"flame",
            18
        );

        textEffect(
            this.x,
            this.groundY()+this.y-130,
            this.side===1
                ?"WATER STYLE!"
                :"FLAME STYLE!",
            this.color
        );

    }


    dash(){

        if(this.dashCooldown>0)return;

        this.dashCooldown=.7;

        this.dashTimer=.16;

        this.state="dash";

        const oldX=this.x;

        this.x += this.facing*115;

        this.x=clamp(
            this.x,
            60,
            W-60
        );

        particle(
            oldX,
            this.groundY()+this.y-45,
            this.color,
            28,
            6
        );

        shockwave(
            this.x,
            this.groundY()+this.y-50,
            this.color
        );

        hitTarget(
            this,
            9,
            70,
            "dash"
        );

    }


    heavy(){

        if(
            this.heavyCooldown>0 ||
            this.energy<30
        )return;

        this.energy-=30;

        this.heavyCooldown=1;

        this.heavyTimer=.55;

        this.state="heavy";

        screenShake=Math.max(
            screenShake,
            8
        );

        const x=
            this.x+this.facing*70;

        const y=
            this.groundY()+this.y-65;

        slash(
            x,
            y,
            this.facing,
            this.color,
            1.8
        );

        shockwave(
            x,
            y,
            this.color
        );

        particle(
            x,
            y,
            this.color,
            30,
            8
        );

        hitTarget(
            this,
            30,
            120,
            "heavy"
        );

    }


    ultimate(){

        if(
            this.ultimateCooldown>0 ||
            this.energy<100
        )return;

        this.energy=0;

        this.ultimateCooldown=3;

        this.ultimateTimer=1.4;

        this.state="ultimate";

        screenShake=20;

        const x=this.x;

        const y=this.groundY()+this.y-70;

        shockwave(
            x,
            y,
            this.color
        );

        for(let i=0;i<55;i++){

            setTimeout(()=>{

                if(!gameOver){

                    particle(
                        x+rand(-120,120),
                        y+rand(-80,80),
                        this.color,
                        1,
                        10
                    );

                }

            },i*15);

        }


        if(this.side===1){

            waterWave(
                x,
                y,
                this.facing
            );

        }else{

            flameBurst(
                x,
                y,
                this.facing
            );

        }


        hitTarget(
            this,
            55,
            250,
            "ultimate"
        );


        flashScreen(
            this.color
        );

    }


    recover(){

        if(
            this.recoverCooldown>0 ||
            this.energy<15
        )return;

        this.energy-=15;

        this.recoverCooldown=1.2;

        this.hp=clamp(
            this.hp+7,
            0,
            100
        );

        textEffect(
            this.x,
            this.groundY()+this.y-130,
            "+7 HP",
            "#8aff9a"
        );

        particle(
            this.x,
            this.groundY()+this.y-60,
            "#8aff9a",
            20,
            3
        );

    }


    powerUp(){

        if(
            this.powerCooldown>0 ||
            this.energy<50
        )return;

        this.energy-=50;

        this.powerCooldown=2;

        this.powerTimer=1.2;

        this.hp=clamp(
            this.hp+15,
            0,
            100
        );

        this.maxSpeed=9;

        textEffect(
            this.x,
            this.groundY()+this.y-140,
            "POWER UP!",
            "#ffffff"
        );

        shockwave(
            this.x,
            this.groundY()+this.y-65,
            "#ffffff"
        );

        particle(
            this.x,
            this.groundY()+this.y-60,
            "#ffffff",
            35,
            5
        );

    }


    update(dt,enemy){

        if(!gameStarted || gameOver){
            return;
        }


        this.controls();


        this.attackCooldown=
            Math.max(
                0,
                this.attackCooldown-dt
            );

        this.skillCooldown=
            Math.max(
                0,
                this.skillCooldown-dt
            );

        this.dashCooldown=
            Math.max(
                0,
                this.dashCooldown-dt
            );

        this.heavyCooldown=
            Math.max(
                0,
                this.heavyCooldown-dt
            );

        this.ultimateCooldown=
            Math.max(
                0,
                this.ultimateCooldown-dt
            );

        this.powerCooldown=
            Math.max(
                0,
                this.powerCooldown-dt
            );

        this.recoverCooldown=
            Math.max(
                0,
                this.recoverCooldown-dt
            );

        this.attackTimer=
            Math.max(
                0,
                this.attackTimer-dt
            );

        this.skillTimer=
            Math.max(
                0,
                this.skillTimer-dt
            );

        this.dashTimer=
            Math.max(
                0,
                this.dashTimer-dt
            );

        this.heavyTimer=
            Math.max(
                0,
                this.heavyTimer-dt
            );

        this.ultimateTimer=
            Math.max(
                0,
                this.ultimateTimer-dt
            );

        this.powerTimer=
            Math.max(
                0,
                this.powerTimer-dt
            );

        this.hitTimer=
            Math.max(
                0,
                this.hitTimer-dt
            );

        this.invincible=
            Math.max(
                0,
                this.invincible-dt
            );


        if(this.comboTimer>0){

            this.comboTimer-=dt;

        }else{

            this.combo=0;

        }


        this.anim += dt*10;


        /* GRAVITY */

        this.vy += .65;

        this.y += this.vy;


        if(this.y>=0){

            this.y=0;

            this.vy=0;

            this.ground=true;

        }else{

            this.ground=false;

        }


        /* MOVE */

        this.x += this.vx;


        this.x=clamp(
            this.x,
            50,
            W-50
        );


        /* ENERGY */

        this.energy += dt*5.5;

        this.energy=clamp(
            this.energy,
            0,
            100
        );


        /* FACE ENEMY */

        if(enemy){

            if(
                Math.abs(
                    enemy.x-this.x
                )>20
            ){

                this.facing=
                    enemy.x>this.x
                        ?1
                        :-1;

            }

        }


        /* STATE */

        if(this.ultimateTimer>0){

            this.state="ultimate";

        }
        else if(this.heavyTimer>0){

            this.state="heavy";

        }
        else if(this.skillTimer>0){

            this.state="skill";

        }
        else if(this.dashTimer>0){

            this.state="dash";

        }
        else if(this.attackTimer>0){

            this.state="attack";

        }
        else if(!this.ground){

            this.state="jump";

        }
        else if(Math.abs(this.vx)>1){

            this.state="run";

        }
        else{

            this.state="idle";

        }


        if(
            this.powerTimer<=0
        ){

            this.maxSpeed=7;

        }

    }


    draw(){

        const ground=this.groundY();

        const x=this.x;

        const y=
            ground+
            this.y;

        const bob=
            this.state==="idle"
                ?Math.sin(this.anim)*2
                :this.state==="run"
                    ?Math.sin(this.anim*1.8)*4
                    :0;


        const bodyY=
            y-62+bob;


        ctx.save();


        /* HIT FLASH */

        if(this.hitTimer>0){

            ctx.globalAlpha=
                Math.floor(
                    this.hitTimer*35
                )%2
                ?0.4
                :1;

        }


        /* POWER AURA */

        if(
            this.energy>=100 ||
            this.powerTimer>0 ||
            this.ultimateTimer>0
        ){

            const radius=
                72+
                Math.sin(
                    this.anim*1.5
                )*9;

            ctx.globalAlpha=.23;

            ctx.beginPath();

            ctx.arc(
                x,
                bodyY-5,
                radius,
                0,
                Math.PI*2
            );

            ctx.strokeStyle=
                this.ultimateTimer>0
                    ?"white"
                    :this.color;

            ctx.lineWidth=7;

            ctx.stroke();

            ctx.globalAlpha=1;

        }


        /* SHADOW */

        ctx.fillStyle=
            "rgba(0,0,0,.55)";

        ctx.beginPath();

        ctx.ellipse(
            x,
            ground+5,
            44,
            9,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();


        /* LEGS */

        let leg1=0;
        let leg2=0;

        if(this.state==="run"){

            leg1=
                Math.sin(
                    this.anim*1.7
                )*16;

            leg2=-leg1;

        }


        ctx.strokeStyle="#17171d";

        ctx.lineWidth=13;

        ctx.lineCap="round";

        ctx.beginPath();

        ctx.moveTo(
            x-12,
            bodyY+38
        );

        ctx.lineTo(
            x-16+leg1,
            bodyY+73
        );

        ctx.moveTo(
            x+12,
            bodyY+38
        );

        ctx.lineTo(
            x+16+leg2,
            bodyY+73
        );

        ctx.stroke();


        /* BODY */

        ctx.fillStyle=
            this.hitTimer>0
                ?"white"
                :this.color;

        roundRect(
            x-26,
            bodyY-4,
            52,
            56,
            12
        );

        ctx.fill();


        /* BELT */

        ctx.fillStyle="#15151b";

        ctx.fillRect(
            x-28,
            bodyY+31,
            56,
            8
        );


        /* HEAD */

        ctx.fillStyle="#ffd1b3";

        ctx.beginPath();

        ctx.arc(
            x,
            bodyY-28,
            24,
            0,
            Math.PI*2
        );

        ctx.fill();


        /* HAIR */

        ctx.fillStyle=
            this.side===1
                ?"rgba(12,100,115,1)"
                :"rgba(116,31,12,1)";

        ctx.beginPath();

        ctx.arc(
            x,
            bodyY-36,
            26,
            Math.PI,
            Math.PI*2
        );

        ctx.lineTo(
            x+21,
            bodyY-44
        );

        ctx.lineTo(
            x+9,
            bodyY-56
        );

        ctx.lineTo(
            x-4,
            bodyY-45
        );

        ctx.lineTo(
            x-20,
            bodyY-54
        );

        ctx.closePath();

        ctx.fill();


        /* EYES */

        ctx.fillStyle="#111";

        ctx.beginPath();

        ctx.arc(
            x-8,
            bodyY-28,
            3,
            0,
            Math.PI*2
        );

        ctx.arc(
            x+8,
            bodyY-28,
            3,
            0,
            Math.PI*2
        );

        ctx.fill();


        /* ARM */

        ctx.strokeStyle=
            this.color;

        ctx.lineWidth=11;

        ctx.beginPath();

        if(
            this.state==="attack" ||
            this.state==="heavy"
        ){

            ctx.moveTo(
                x+this.facing*14,
                bodyY+5
            );

            ctx.lineTo(
                x+this.facing*48,
                bodyY-20
            );

        }else{

            ctx.moveTo(
                x+this.facing*16,
                bodyY+8
            );

            ctx.lineTo(
                x+this.facing*38,
                bodyY+24
            );

        }

        ctx.stroke();


        /* SWORD */

        const swordStartX=
            x+this.facing*22;

        const swordStartY=
            bodyY+4;


        let swordTilt=0;

        if(
            this.state==="attack" ||
            this.state==="heavy"
        ){

            swordTilt=
                this.facing*.7;

        }


        ctx.strokeStyle="#dce7ed";

        ctx.lineWidth=
            this.state==="heavy"
                ?8
                :6;

        ctx.beginPath();

        ctx.moveTo(
            swordStartX,
            swordStartY
        );

        ctx.lineTo(
            swordStartX+
                this.facing*48,
            swordStartY-
                65+
                swordTilt*25
        );

        ctx.stroke();


        /* GUARD */

        ctx.strokeStyle="#292929";

        ctx.lineWidth=8;

        ctx.beginPath();

        ctx.moveTo(
            x+this.facing*17,
            bodyY+5
        );

        ctx.lineTo(
            x+this.facing*34,
            bodyY+18
        );

        ctx.stroke();


        /* SPECIAL GLOW */

        if(
            this.state==="skill" ||
            this.state==="dash" ||
            this.state==="heavy" ||
            this.state==="ultimate"
        ){

            ctx.globalAlpha=.35;

            ctx.strokeStyle=
                this.color;

            ctx.lineWidth=
                this.state==="ultimate"
                    ?15
                    :8;

            ctx.beginPath();

            ctx.arc(
                x+this.facing*30,
                bodyY-15,
                48+
                Math.sin(this.anim)*8,
                -1.2,
                1.2
            );

            ctx.stroke();

            ctx.globalAlpha=1;

        }


        /* NAME */

        ctx.font=
            "bold 13px Arial";

        ctx.textAlign="center";

        ctx.fillStyle="white";

        ctx.fillText(
            this.name,
            x,
            bodyY-86
        );


        ctx.restore();

    }

}


/* =========================================================
   RECT HELPER
========================================================= */

function roundRect(
    x,
    y,
    w,
    h,
    r
){

    const rr=
        Math.min(
            r,
            w/2,
            h/2
        );

    ctx.beginPath();

    ctx.moveTo(
        x+rr,
        y
    );

    ctx.arcTo(
        x+w,
        y,
        x+w,
        y+h,
        rr
    );

    ctx.arcTo(
        x+w,
        y+h,
        x,
        y+h,
        rr
    );

    ctx.arcTo(
        x,
        y+h,
        x,
        y,
        rr
    );

    ctx.arcTo(
        x,
        y,
        x+w,
        y,
        rr
    );

    ctx.closePath();

}


/* =========================================================
   FIGHTERS
========================================================= */

const p1 =
    new Fighter(
        0,
        1,
        "WATER",
        "#21ddec",
        "#bafaff"
    );

const p2 =
    new Fighter(
        0,
        -1,
        "FLAME",
        "#ff5528",
        "#ffd0a0"
    );


/* =========================================================
   HIT SYSTEM
========================================================= */

function hitTarget(
    attacker,
    damage,
    range,
    type
){

    const target =
        attacker===p1
            ?p2
            :p1;


    if(target.invincible>0){
        return;
    }


    const dx =
        target.x -
        attacker.x;


    const correctDirection =
        Math.sign(dx) ===
        attacker.facing ||
        Math.abs(dx)<35;


    if(
        Math.abs(dx)<=range &&
        Math.abs(
            target.y-
            attacker.y
        )<100 &&
        correctDirection
    ){

        target.hp=
            clamp(
                target.hp-damage,
                0,
                100
            );


        target.invincible=.22;

        target.hitTimer=.18;

        target.vx +=
            attacker.facing *
            damage *
            .13;


        target.vy -=
            type==="ultimate"
                ?5
                :2;


        screenShake=
            Math.max(
                screenShake,
                type==="ultimate"
                    ?22
                    :type==="heavy"
                        ?10
                        :5
            );


        hitStop=
            type==="ultimate"
                ?.08
                :.035;


        particle(
            target.x,
            target.groundY()+
            target.y-
            65,
            attacker.color,
            type==="ultimate"
                ?45
                :18,
            type==="ultimate"
                ?10
                :6
        );


        textEffect(
            target.x,
            target.groundY()+
            target.y-
            120,
            "-"+damage,
            attacker.color
        );


        if(type==="ultimate"){

            flashScreen(
                attacker.color
            );

        }


        if(target.hp<=0){

            target.hp=0;

            finishBattle(
                attacker===p1
                    ?"WATER WINS!"
                    :"FLAME WINS!"
            );

        }

    }

}


/* =========================================================
   PROJECTILE UPDATE
========================================================= */

function updateProjectiles(dt){

    for(
        let i=projectiles.length-1;
        i>=0;
        i--
    ){

        const p=
            projectiles[i];

        p.x+=p.vx;

        p.life-=dt;


        if(
            p.x<-100 ||
            p.x>W+100 ||
            p.life<=0
        ){

            projectiles.splice(i,1);

            continue;

        }


        const target=
            p.type==="water"
                ?p2
                :p1;


        if(
            Math.abs(
                target.x-p.x
            )<45 &&
            target.invincible<=0
        ){

            target.hp=
                clamp(
                    target.hp-p.damage,
                    0,
                    100
                );

            target.invincible=.2;

            target.hitTimer=.2;

            target.vx +=
                Math.sign(p.vx)*3;

            particle(
                target.x,
                target.groundY()-60,
                p.color,
                20,
                5
            );

            textEffect(
                target.x,
                target.groundY()-120,
                "-"+p.damage,
                p.color
            );

            projectiles.splice(i,1);

        }

    }

}


/* =========================================================
   EFFECT UPDATE
========================================================= */

function updateEffects(dt){

    for(
        let i=particles.length-1;
        i>=0;
        i--
    ){

        const p=particles[i];

        p.x+=p.vx;
        p.y+=p.vy;

        p.vy+=p.gravity;

        p.life-=dt;

        if(p.life<=0){

            particles.splice(i,1);

        }

    }


    for(
        let i=slashEffects.length-1;
        i>=0;
        i--
    ){

        const s=
            slashEffects[i];

        s.life-=dt;

        if(s.life<=0){

            slashEffects.splice(i,1);

        }

    }


    for(
        let i=shockwaves.length-1;
        i>=0;
        i--
    ){

        const s=
            shockwaves[i];

        s.radius+=
            300*dt;

        s.life-=dt;

        if(s.life<=0){

            shockwaves.splice(i,1);

        }

    }


    for(
        let i=floatingTexts.length-1;
        i>=0;
        i--
    ){

        const t=
            floatingTexts[i];

        t.y+=t.vy*dt;

        t.life-=dt;

        if(t.life<=0){

            floatingTexts.splice(i,1);

        }

    }


    for(
        let i=waterEffects.length-1;
        i>=0;
        i--
    ){

        const p=
            waterEffects[i];

        p.x+=p.vx;
        p.y+=p.vy;

        p.vy+=.05;

        p.life-=dt;

        if(p.life<=0){

            waterEffects.splice(i,1);

        }

    }


    for(
        let i=flameEffects.length-1;
        i>=0;
        i--
    ){

        const p=
            flameEffects[i];

        p.x+=p.vx;
        p.y+=p.vy;

        p.vy+=.08;

        p.life-=dt;

        if(p.life<=0){

            flameEffects.splice(i,1);

        }

    }

}


/* =========================================================
   DRAW EFFECTS
========================================================= */

function drawEffects(){

    /* particles */

    for(const p of particles){

        ctx.globalAlpha=
            clamp(
                p.life/p.maxLife,
                0,
                1
            );

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

    }


    /* water */

    for(const p of waterEffects){

        ctx.globalAlpha=
            clamp(
                p.life/p.maxLife,
                0,
                1
            );

        ctx.strokeStyle=
            "#36eaff";

        ctx.lineWidth=3;

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI
        );

        ctx.stroke();

    }


    /* flame */

    for(const p of flameEffects){

        ctx.globalAlpha=
            clamp(
                p.life/p.maxLife,
                0,
                1
            );

        ctx.fillStyle=
            Math.random()>.4
                ?"rgba(255,80,20,.9)"
                :"rgba(255,190,40,.9)";

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI*2
        );

        ctx.fill();

    }


    /* slashes */

    for(const s of slashEffects){

        ctx.save();

        ctx.translate(
            s.x,
            s.y
        );

        ctx.rotate(
            s.angle
        );

        ctx.globalAlpha=
            clamp(
                s.life/s.maxLife,
                0,
                1
            );

        ctx.strokeStyle=s.color;

        ctx.lineWidth=
            7*s.power;

        ctx.beginPath();

        ctx.arc(
            0,
            0,
            s.size,
            -.72,
            .72
        );

        ctx.stroke();

        ctx.restore();

    }


    /* shockwaves */

    for(const s of shockwaves){

        ctx.globalAlpha=
            clamp(
                s.life/s.maxLife,
                0,
                1
            );

        ctx.strokeStyle=s.color;

        ctx.lineWidth=5;

        ctx.beginPath();

        ctx.arc(
            s.x,
            s.y,
            s.radius,
            0,
            Math.PI*2
        );

        ctx.stroke();

    }


    /* projectiles */

    for(const p of projectiles){

        ctx.globalAlpha=.8;

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

        ctx.globalAlpha=.25;

        ctx.beginPath();

        ctx.arc(
            p.x-p.vx*2,
            p.y,
            p.size*1.8,
            0,
            Math.PI*2
        );

        ctx.fill();

    }


    /* floating text */

    for(const t of floatingTexts){

        ctx.globalAlpha=
            clamp(
                t.life/t.maxLife,
                0,
                1
            );

        ctx.font=
            "900 21px Arial";

        ctx.textAlign="center";

        ctx.fillStyle=t.color;

        ctx.fillText(
            t.text,
            t.x,
            t.y
        );

    }


    ctx.globalAlpha=1;

}


/* =========================================================
   BACKGROUND
========================================================= */

function drawBackground(){

    arenaTime+=.01;


    /* SKY */

    const sky=
        ctx.createLinearGradient(
            0,
            0,
            0,
            H
        );

    sky.addColorStop(
        0,
        "#030617"
    );

    sky.addColorStop(
        .5,
        "#101c3c"
    );

    sky.addColorStop(
        1,
        "#070812"
    );

    ctx.fillStyle=sky;

    ctx.fillRect(
        0,
        0,
        W,
        H
    );


    /* MOON */

    ctx.fillStyle=
        "rgba(245,248,225,.9)";

    ctx.beginPath();

    ctx.arc(
        W*.78,
        H*.18,
        58,
        0,
        Math.PI*2
    );

    ctx.fill();


    ctx.fillStyle="#11182f";

    ctx.beginPath();

    ctx.arc(
        W*.80,
        H*.16,
        51,
        0,
        Math.PI*2
    );

    ctx.fill();


    /* STARS */

    for(let i=0;i<90;i++){

        const x=
            (i*193)%W;

        const y=
            (i*73)%(H*.55);

        const a=
            .35+
            .25*
            Math.sin(
                arenaTime*2+i
            );

        ctx.fillStyle=
            `rgba(255,255,255,${a})`;

        ctx.fillRect(
            x,
            y,
            2,
            2
        );

    }


    /* MOUNTAINS */

    ctx.fillStyle="#080b18";

    ctx.beginPath();

    ctx.moveTo(
        0,
        H-230
    );

    for(
        let x=0;
        x<=W;
        x+=100
    ){

        const peak=
            H-230-
            (60+
            40*
            Math.sin(
                x*.013
            ));

        ctx.lineTo(
            x,
            peak
        );

    }

    ctx.lineTo(
        W,
        H
    );

    ctx.lineTo(
        0,
        H
    );

    ctx.closePath();

    ctx.fill();


    /* TREES */

    for(
        let i=0;
        i<22;
        i++
    ){

        const x=
            (i/(21))*W;

        const treeH=
            90+
            ((i*43)%90);

        ctx.fillStyle="#05070e";

        ctx.fillRect(
            x-5,
            H-155-treeH*.2,
            10,
            treeH
        );

        ctx.beginPath();

        ctx.moveTo(
            x,
            H-155-treeH
        );

        ctx.lineTo(
            x-50,
            H-80
        );

        ctx.lineTo(
            x+50,
            H-80
        );

        ctx.closePath();

        ctx.fill();

    }


    /* GROUND */

    const floor=H-145;

    ctx.fillStyle="#11141e";

    ctx.fillRect(
        0,
        floor,
        W,
        H-floor
    );


    /* FLOOR GRID */

    ctx.strokeStyle=
        "rgba(100,130,170,.20)";

    ctx.lineWidth=1;


    for(
        let x=0;
        x<W;
        x+=70
    ){

        ctx.beginPath();

        ctx.moveTo(
            x,
            floor
        );

        ctx.lineTo(
            x+70,
            H
        );

        ctx.stroke();

    }


    for(
        let y=floor;
        y<H;
        y+=28
    ){

        ctx.beginPath();

        ctx.moveTo(
            0,
            y
        );

        ctx.lineTo(
            W,
            y
        );

        ctx.stroke();

    }


    /* CENTER */

    ctx.strokeStyle=
        "rgba(255,255,255,.10)";

    ctx.beginPath();

    ctx.moveTo(
        W/2,
        floor
    );

    ctx.lineTo(
        W/2,
        H
    );

    ctx.stroke();

}


/* =========================================================
   HUD
========================================================= */

function updateHUD(){

    document.getElementById(
        "hp1"
    ).style.width=
        p1.hp+"%";


    document.getElementById(
        "hp2"
    ).style.width=
        p2.hp+"%";


    document.getElementById(
        "en1"
    ).style.width=
        p1.energy+"%";


    document.getElementById(
        "en2"
    ).style.width=
        p2.energy+"%";


    document.getElementById(
        "timer"
    ).textContent=
        Math.max(
            0,
            Math.ceil(timeLeft)
        );

}


/* =========================================================
   SCREEN FLASH
========================================================= */

function flashScreen(color){

    const el=
        document.getElementById(
            "flash"
        );

    el.style.background=color;

    el.style.opacity=.20;

    setTimeout(()=>{

        el.style.opacity=0;

    },90);

}


/* =========================================================
   START
========================================================= */

function startBattle(){

    document.getElementById(
        "overlay"
    ).style.display="none";


    gameStarted=true;

    gameOver=false;

    timeLeft=60;


    p1.reset();
    p2.reset();


    p1.x=W*.25;
    p2.x=W*.75;


    const cd=
        document.getElementById(
            "countdown"
        );


    cd.style.display="flex";


    let number=3;

    cd.textContent=number;


    const interval=
        setInterval(()=>{

            number--;

            if(number>0){

                cd.textContent=
                    number;

            }
            else{

                cd.textContent=
                    "FIGHT!";

                setTimeout(()=>{

                    cd.style.display=
                        "none";

                },450);

                clearInterval(
                    interval
                );

            }

        },700);

}


/* =========================================================
   FINISH
========================================================= */

function finishBattle(title){

    if(gameOver){
        return;
    }

    gameOver=true;

    const overlay=
        document.getElementById(
            "overlay"
        );

    overlay.style.display=
        "flex";


    document.querySelector(
        ".panel"
    ).innerHTML=`

        <h1>${title}</h1>

        <h2>⚔️ BATTLE FINISHED</h2>

        <p>
            WATER HP:
            ${Math.round(p1.hp)}
        </p>

        <p>
            FLAME HP:
            ${Math.round(p2.hp)}
        </p>

        <button
            class="start"
            onclick="location.reload()"
        >
            REMATCH
        </button>

    `;

}


/* =========================================================
   GAME UPDATE
========================================================= */

function update(dt){

    if(!gameStarted || gameOver){

        updateEffects(dt);

        return;

    }


    if(hitStop>0){

        hitStop-=dt;

        updateEffects(dt);

        return;

    }


    timeLeft-=dt;


    if(timeLeft<=0){

        timeLeft=0;

        if(
            p1.hp>
            p2.hp
        ){

            finishBattle(
                "WATER WINS!"
            );

        }
        else if(
            p2.hp>
            p1.hp
        ){

            finishBattle(
                "FLAME WINS!"
            );

        }
        else{

            finishBattle(
                "DRAW!"
            );

        }

    }


    p1.update(
        dt,
        p2
    );

    p2.update(
        dt,
        p1
    );


    updateProjectiles(dt);

    updateEffects(dt);


    if(
        p1.hp<=0 &&
        !gameOver
    ){

        finishBattle(
            "FLAME WINS!"
        );

    }


    if(
        p2.hp<=0 &&
        !gameOver
    ){

        finishBattle(
            "WATER WINS!"
        );

    }


    updateHUD();

}


/* =========================================================
   DRAW
========================================================= */

function draw(){

    ctx.save();


    if(screenShake>0){

        ctx.translate(
            rand(
                -screenShake,
                screenShake
            ),
            rand(
                -screenShake,
                screenShake
            )
        );

        screenShake*=.86;

        if(screenShake<.2){

            screenShake=0;

        }

    }


    drawBackground();


    p1.draw();

    p2.draw();


    drawEffects();


    ctx.restore();

}


/* =========================================================
   LOOP
========================================================= */

function loop(now){

    const dt=
        Math.min(
            .033,
            (now-lastTime)/1000
        );

    lastTime=now;


    update(dt);

    draw();


    requestAnimationFrame(
        loop
    );

}


/* =========================================================
   MUTE
========================================================= */

document.getElementById(
    "mute"
).onclick=()=>{

    muted=!muted;

    document.getElementById(
        "mute"
    ).textContent=
        muted
            ?"🔇"
            :"🔊";

};


/* =========================================================
   INIT
========================================================= */

p1.x=W*.25;
p2.x=W*.75;

updateHUD();

requestAnimationFrame(
    loop
);

</script>

</body>
</html>
"""

components.html(
    HTML,
    height=900,
    scrolling=False
)
