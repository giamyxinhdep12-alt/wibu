import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Anime Clash",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">

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
    background:#02030b;
    font-family:Arial,Helvetica,sans-serif;
}

#game{
    position:relative;
    width:100vw;
    height:100vh;
    overflow:hidden;
    background:#02030b;
}

canvas{
    position:absolute;
    inset:0;
    width:100%;
    height:100%;
}

/* =========================================================
   HOME
========================================================= */

#home{
    position:absolute;
    inset:0;
    z-index:100;
    display:flex;
    justify-content:center;
    align-items:center;
    overflow:auto;

    background:
        radial-gradient(
            circle at 20% 30%,
            rgba(0,220,255,.16),
            transparent 30%
        ),
        radial-gradient(
            circle at 80% 65%,
            rgba(255,40,120,.15),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #02030b,
            #080d22 50%,
            #03040c
        );
}

.home-grid{
    position:absolute;
    inset:0;
    opacity:.13;
    background-image:
        linear-gradient(
            rgba(100,200,255,.2) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(100,200,255,.2) 1px,
            transparent 1px
        );
    background-size:60px 60px;
    transform:perspective(500px) rotateX(55deg) scale(1.5);
    transform-origin:center bottom;
}

.home-panel{
    position:relative;
    z-index:2;
    width:min(960px,94vw);
    padding:45px;
    border-radius:32px;

    background:
        linear-gradient(
            145deg,
            rgba(13,20,52,.94),
            rgba(5,8,24,.96)
        );

    border:1px solid rgba(120,210,255,.22);

    box-shadow:
        0 30px 100px rgba(0,0,0,.65),
        inset 0 0 50px rgba(50,150,255,.05);

    backdrop-filter:blur(18px);

    text-align:center;
}

.logo-small{
    color:#73eaff;
    font-size:13px;
    letter-spacing:7px;
    font-weight:bold;
    margin-bottom:12px;
}

.logo{
    font-size:clamp(45px,8vw,90px);
    line-height:1;
    font-weight:1000;
    letter-spacing:5px;

    background:
        linear-gradient(
            90deg,
            #31dcff,
            #ffffff 45%,
            #ff63c8
        );

    -webkit-background-clip:text;
    background-clip:text;
    color:transparent;

    filter:
        drop-shadow(0 0 25px rgba(40,220,255,.25));
}

.subtitle{
    margin-top:13px;
    color:#8795c6;
    letter-spacing:4px;
    font-size:14px;
}

.name-area{
    width:min(520px,100%);
    margin:35px auto 28px;
    text-align:left;
}

.name-label{
    color:#dbe7ff;
    font-size:14px;
    font-weight:bold;
    margin-bottom:9px;
}

.name-input{
    width:100%;
    height:54px;

    border-radius:15px;
    border:1px solid rgba(120,210,255,.22);

    background:#050817;
    color:white;

    outline:none;
    padding:0 18px;

    font-size:17px;

    box-shadow:
        inset 0 0 20px rgba(0,0,0,.3);

    transition:.2s;
}

.name-input:focus{
    border-color:#46dcff;
    box-shadow:
        0 0 25px rgba(40,210,255,.12),
        inset 0 0 20px rgba(0,0,0,.3);
}

.modes{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:20px;
}

.mode-card{
    position:relative;
    min-height:210px;

    border-radius:24px;
    border:1px solid rgba(255,255,255,.11);

    background:
        linear-gradient(
            145deg,
            rgba(19,29,69,.95),
            rgba(6,10,29,.96)
        );

    color:white;
    cursor:pointer;

    padding:28px;

    overflow:hidden;

    transition:
        transform .25s,
        border .25s,
        box-shadow .25s;
}

.mode-card::before{
    content:"";
    position:absolute;
    width:170px;
    height:170px;
    border-radius:50%;
    left:-70px;
    top:-70px;
    background:rgba(50,220,255,.09);
    filter:blur(5px);
}

.mode-card.cpu::before{
    background:rgba(255,70,110,.10);
}

.mode-card:hover{
    transform:translateY(-8px);
    border-color:#42ddff;
    box-shadow:
        0 20px 50px rgba(30,190,255,.12);
}

.mode-card.cpu:hover{
    border-color:#ff587b;
    box-shadow:
        0 20px 50px rgba(255,50,100,.12);
}

.mode-icon{
    position:relative;
    font-size:54px;
    margin-bottom:12px;
}

.mode-title{
    position:relative;
    font-size:27px;
    font-weight:1000;
    margin-bottom:12px;
}

.mode-desc{
    position:relative;
    color:#9ba8d1;
    font-size:14px;
    line-height:1.65;
}

.home-tip{
    margin-top:25px;
    color:#626f98;
    font-size:12px;
}

/* =========================================================
   HUD
========================================================= */

#hud{
    position:absolute;
    left:0;
    top:0;
    width:100%;
    z-index:20;

    padding:18px;

    display:flex;
    justify-content:space-between;

    pointer-events:none;
}

.hud{
    width:min(400px,37vw);

    padding:13px 16px;

    border-radius:17px;

    background:
        linear-gradient(
            145deg,
            rgba(5,9,28,.88),
            rgba(9,12,32,.72)
        );

    border:1px solid rgba(255,255,255,.11);

    box-shadow:
        0 12px 35px rgba(0,0,0,.28);

    backdrop-filter:blur(12px);
}

.hud-info{
    display:flex;
    align-items:center;
    justify-content:space-between;
    margin-bottom:8px;
}

.hud-name{
    max-width:250px;

    color:white;
    font-weight:1000;
    font-size:15px;

    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
}

.hud-hp{
    color:#98a6cd;
    font-size:12px;
}

.bar{
    height:12px;
    overflow:hidden;

    border-radius:20px;

    background:#12172b;

    margin-bottom:6px;

    box-shadow:
        inset 0 1px 4px rgba(0,0,0,.6);
}

.hp{
    width:100%;
    height:100%;

    transition:width .15s linear;
}

.hp-blue{
    background:
        linear-gradient(
            90deg,
            #09bde9,
            #69f3ff
        );

    box-shadow:
        0 0 12px rgba(40,230,255,.55);
}

.hp-red{
    background:
        linear-gradient(
            90deg,
            #ff3b59,
            #ff8a68
        );

    box-shadow:
        0 0 12px rgba(255,70,90,.55);
}

.energy{
    height:6px;
    width:0%;
    transition:width .15s linear;
}

.en-blue{
    background:
        linear-gradient(
            90deg,
            #3d8cff,
            #b5e8ff
        );
}

.en-red{
    background:
        linear-gradient(
            90deg,
            #a43cff,
            #f4a0ff
        );
}

#timer{
    position:absolute;
    z-index:21;

    top:20px;
    left:50%;
    transform:translateX(-50%);

    min-width:78px;

    padding:10px 17px;

    border-radius:15px;

    background:
        rgba(5,8,23,.88);

    border:1px solid rgba(255,255,255,.13);

    color:white;

    text-align:center;

    font-size:23px;
    font-weight:1000;

    box-shadow:
        0 8px 30px rgba(0,0,0,.3);
}

/* =========================================================
   COUNTDOWN
========================================================= */

#countdown{
    position:absolute;
    inset:0;
    z-index:40;

    display:none;
    align-items:center;
    justify-content:center;

    pointer-events:none;
}

#countText{
    font-size:clamp(90px,18vw,190px);

    font-weight:1000;
    font-style:italic;

    color:white;

    text-shadow:
        0 0 10px white,
        0 0 35px #28dfff,
        0 0 80px rgba(50,180,255,.8);

    animation:count .65s ease;
}

@keyframes count{
    0%{
        opacity:0;
        transform:scale(.2) rotate(-8deg);
    }

    65%{
        opacity:1;
        transform:scale(1.15) rotate(2deg);
    }

    100%{
        transform:scale(1);
    }
}

/* =========================================================
   RESULT
========================================================= */

#result{
    position:absolute;
    inset:0;
    z-index:80;

    display:none;

    align-items:center;
    justify-content:center;

    background:
        radial-gradient(
            circle,
            rgba(20,30,75,.25),
            rgba(0,0,0,.78)
        );

    backdrop-filter:blur(8px);
}

#result.show{
    display:flex;
}

.result-panel{
    position:relative;

    width:min(720px,90vw);

    padding:45px 35px;

    text-align:center;

    border-radius:30px;

    background:
        linear-gradient(
            145deg,
            rgba(14,20,50,.97),
            rgba(5,8,23,.98)
        );

    border:1px solid rgba(255,255,255,.14);

    box-shadow:
        0 30px 100px rgba(0,0,0,.75);

    animation:resultIn .5s cubic-bezier(.2,.9,.2,1);
}

@keyframes resultIn{
    from{
        opacity:0;
        transform:translateY(40px) scale(.8);
    }

    to{
        opacity:1;
        transform:translateY(0) scale(1);
    }
}

.result-title{
    font-size:clamp(31px,5vw,58px);
    font-weight:1000;
    line-height:1.25;

    color:white;

    text-shadow:
        0 0 25px rgba(255,255,255,.12);
}

.result-title small{
    display:block;

    margin-top:18px;

    color:#8996bc;

    font-size:14px;
    font-weight:500;
}

.result-btn{
    margin-top:30px;

    padding:14px 30px;

    border:none;
    border-radius:14px;

    color:white;
    background:
        linear-gradient(
            90deg,
            #13c6ec,
            #9552ff
        );

    font-size:15px;
    font-weight:1000;

    cursor:pointer;

    box-shadow:
        0 10px 35px rgba(80,100,255,.2);

    transition:.2s;
}

.result-btn:hover{
    transform:translateY(-3px);
}

/* =========================================================
   CONTROLS
========================================================= */

#controls{
    position:absolute;
    z-index:15;

    bottom:12px;
    left:50%;

    transform:translateX(-50%);

    padding:7px 14px;

    border-radius:12px;

    color:#7582a8;

    background:
        rgba(4,7,20,.65);

    border:1px solid rgba(255,255,255,.07);

    font-size:10px;

    white-space:nowrap;
}

/* =========================================================
   RESPONSIVE
========================================================= */

@media(max-width:760px){

    .home-panel{
        padding:28px 18px;
    }

    .modes{
        grid-template-columns:1fr;
    }

    .mode-card{
        min-height:160px;
    }

    .hud{
        width:39vw;
        padding:10px;
    }

    .hud-name{
        font-size:11px;
    }

    .hud-hp{
        font-size:9px;
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

<!-- =====================================================
     HOME
===================================================== -->

<div id="home">

    <div class="home-grid"></div>

    <div class="home-panel">

        <div class="logo-small">
            ⚡ WELCOME TO THE ARENA ⚡
        </div>

        <div class="logo">
            ANIME CLASH
        </div>

        <div class="subtitle">
            1V1 BATTLE • ENTER THE FIGHT
        </div>

        <div class="name-area">

            <div class="name-label">
                👤 TÊN NGƯỜI CHƠI
            </div>

            <input
                id="playerInput"
                class="name-input"
                maxlength="20"
                type="text"
                placeholder="Nhập tên của bạn..."
                autocomplete="off"
            >

        </div>

        <div class="modes">

            <button
                class="mode-card"
                onclick="chooseMode('1v1')"
            >

                <div class="mode-icon">
                    ⚔️
                </div>

                <div class="mode-title">
                    1 V 1
                </div>

                <div class="mode-desc">
                    Đấu trực tiếp với người chơi thứ 2.
                    Hai bên cùng bàn phím và chiến đấu
                    cho đến khi một người bị hạ.
                </div>

            </button>

            <button
                class="mode-card cpu"
                onclick="chooseMode('cpu')"
            >

                <div class="mode-icon">
                    🤖
                </div>

                <div class="mode-title">
                    ĐẤU VỚI MÁY
                </div>

                <div class="mode-desc">
                    Đối đầu với CPU có khả năng di chuyển,
                    tấn công, dùng skill và ultimate.
                </div>

            </button>

        </div>

        <div class="home-tip">
            🎮 Không cần ảnh hoặc file ngoài • Tối đa 20 ký tự cho tên
        </div>

    </div>

</div>

<!-- =====================================================
     HUD
===================================================== -->

<div id="hud">

    <div class="hud">

        <div class="hud-info">
            <div id="leftName" class="hud-name">
                PLAYER 1
            </div>

            <div id="leftHP" class="hud-hp">
                100 HP
            </div>
        </div>

        <div class="bar">
            <div
                id="hp1"
                class="hp hp-blue"
            ></div>
        </div>

        <div class="bar">
            <div
                id="en1"
                class="energy en-blue"
            ></div>
        </div>

    </div>

    <div class="hud">

        <div class="hud-info">
            <div id="rightName" class="hud-name">
                PLAYER 2
            </div>

            <div id="rightHP" class="hud-hp">
                100 HP
            </div>
        </div>

        <div class="bar">
            <div
                id="hp2"
                class="hp hp-red"
            ></div>
        </div>

        <div class="bar">
            <div
                id="en2"
                class="energy en-red"
            ></div>
        </div>

    </div>

</div>

<div id="timer">
    60
</div>

<!-- =====================================================
     COUNTDOWN
===================================================== -->

<div id="countdown">

    <div id="countText">
        3
    </div>

</div>

<!-- =====================================================
     RESULT
===================================================== -->

<div id="result">

    <div class="result-panel">

        <div
            id="resultTitle"
            class="result-title"
        ></div>

        <button
            class="result-btn"
            onclick="location.reload()"
        >
            🔄 CHƠI LẠI
        </button>

    </div>

</div>

<div id="controls">
    P1: A D W S J K L U I O P
    &nbsp;•&nbsp;
    P2: ← → ↑ ↓ + 1 2 3 4 5 6 7
</div>

<script>

/* =========================================================
   CANVAS
========================================================= */

const canvas =
    document.getElementById("canvas");

const ctx =
    canvas.getContext("2d");

let W =
    window.innerWidth;

let H =
    window.innerHeight;

function resize(){

    W =
        window.innerWidth;

    H =
        window.innerHeight;

    canvas.width=W;
    canvas.height=H;
}

window.addEventListener(
    "resize",
    resize
);

resize();

/* =========================================================
   GAME STATE
========================================================= */

let mode=null;

let playerName="PLAYER 1";

let started=false;
let ended=false;

let p1=null;
let p2=null;

let fighters=[];

let particles=[];
let projectiles=[];

let keys={};

let gameTime=60;

let lastTime=
    performance.now();

/* =========================================================
   INPUT
========================================================= */

window.addEventListener(
    "keydown",
    e=>{

        keys[
            e.key.toLowerCase()
        ]=true;

        if(
            [
                "arrowup",
                "arrowdown",
                "arrowleft",
                "arrowright",
                " "
            ].includes(
                e.key.toLowerCase()
            )
        ){
            e.preventDefault();
        }
    }
);

window.addEventListener(
    "keyup",
    e=>{

        keys[
            e.key.toLowerCase()
        ]=false;
    }
);

/* =========================================================
   UTILS
========================================================= */

function clamp(
    value,
    min,
    max
){

    return Math.max(
        min,
        Math.min(max,value)
    );
}

function rand(
    min,
    max
){

    return Math.random()*
        (max-min)+min;
}

/* =========================================================
   PARTICLES
========================================================= */

function burst(
    x,
    y,
    color,
    count=10,
    power=250
){

    for(
        let i=0;
        i<count;
        i++
    ){

        const a =
            Math.random()*
            Math.PI*2;

        const speed =
            rand(power*.3,power);

        particles.push({

            x:x,
            y:y,

            vx:
                Math.cos(a)*speed,

            vy:
                Math.sin(a)*speed,

            life:
                rand(.35,.8),

            maxLife:.8,

            size:
                rand(2,7),

            color:color
        });
    }
}

function updateParticles(dt){

    for(
        let i=particles.length-1;
        i>=0;
        i--
    ){

        const p=
            particles[i];

        p.x += p.vx*dt;
        p.y += p.vy*dt;

        p.vy += 550*dt;

        p.life -= dt;

        if(p.life<=0){

            particles.splice(i,1);
        }
    }
}

function drawParticles(){

    for(
        const p of particles
    ){

        ctx.save();

        ctx.globalAlpha =
            clamp(
                p.life/p.maxLife,
                0,
                1
            );

        ctx.fillStyle =
            p.color;

        ctx.shadowColor =
            p.color;

        ctx.shadowBlur=12;

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

/* =========================================================
   FIGHTER
========================================================= */

class Fighter{

    constructor(
        id,
        team,
        x,
        primary,
        glow,
        name,
        cpu
    ){

        this.id=id;
        this.team=team;

        this.x=x;
        this.y=H-165;

        this.vx=0;
        this.vy=0;

        this.primary=primary;
        this.glow=glow;

        this.name=name;

        this.cpu=cpu;

        this.hp=100;
        this.energy=0;

        this.speed=285;

        this.jumpPower=-610;
        this.gravity=1500;

        this.facing=
            team===1
            ?1
            :-1;

        this.onGround=true;

        this.attackCD=0;
        this.skillCD=0;
        this.dashCD=0;
        this.heavyCD=0;
        this.ultCD=0;
        this.recoverCD=0;
        this.powerCD=0;

        this.attackFX=0;
        this.flash=0;

        this.cpuMoveTimer=
            rand(.1,.3);

        this.cpuAttackTimer=
            rand(.25,.7);
    }

    alive(){

        return this.hp>0;
    }

    enemy(){

        return this===p1
            ?p2
            :p1;
    }

    cooldowns(dt){

        this.attackCD=
            Math.max(
                0,
                this.attackCD-dt
            );

        this.skillCD=
            Math.max(
                0,
                this.skillCD-dt
            );

        this.dashCD=
            Math.max(
                0,
                this.dashCD-dt
            );

        this.heavyCD=
            Math.max(
                0,
                this.heavyCD-dt
            );

        this.ultCD=
            Math.max(
                0,
                this.ultCD-dt
            );

        this.recoverCD=
            Math.max(
                0,
                this.recoverCD-dt
            );

        this.powerCD=
            Math.max(
                0,
                this.powerCD-dt
            );

        this.attackFX=
            Math.max(
                0,
                this.attackFX-dt
            );

        this.flash=
            Math.max(
                0,
                this.flash-dt
            );
    }

    controls(){

        if(
            !this.alive()
        ){
            return;
        }

        let left=false;
        let right=false;

        if(this.id==="p1"){

            left=keys["a"];
            right=keys["d"];

            if(
                keys["w"] &&
                this.onGround
            ){

                this.vy=
                    this.jumpPower;

                this.onGround=false;
            }

            if(keys["s"]){
                this.vy+=800;
            }

            if(keys["j"]){
                this.attack();
            }

            if(keys["k"]){
                this.skill();
            }

            if(keys["l"]){
                this.dash();
            }

            if(keys["u"]){
                this.heavy();
            }

            if(keys["i"]){
                this.ultimate();
            }

            if(keys["o"]){
                this.recover();
            }

            if(keys["p"]){
                this.power();
            }

        }else if(!this.cpu){

            left=keys["arrowleft"];
            right=keys["arrowright"];

            if(
                keys["arrowup"] &&
                this.onGround
            ){

                this.vy=
                    this.jumpPower;

                this.onGround=false;
            }

            if(keys["arrowdown"]){
                this.vy+=800;
            }

            if(keys["1"]){
                this.attack();
            }

            if(keys["2"]){
                this.skill();
            }

            if(keys["3"]){
                this.dash();
            }

            if(keys["4"]){
                this.heavy();
            }

            if(keys["5"]){
                this.ultimate();
            }

            if(keys["6"]){
                this.recover();
            }

            if(keys["7"]){
                this.power();
            }
        }

        if(left){

            this.vx=
                -this.speed;

            this.facing=-1;

        }else if(right){

            this.vx=
                this.speed;

            this.facing=1;

        }else{

            this.vx*=.78;
        }
    }

    cpuAI(){

        if(
            !this.cpu ||
            !this.alive() ||
            !p1 ||
            !p1.alive()
        ){
            return;
        }

        const target=p1;

        const dx=
            target.x-this.x;

        const d=
            Math.abs(dx);

        this.cpuMoveTimer-=1/60;
        this.cpuAttackTimer-=1/60;

        if(
            this.cpuMoveTimer<=0
        ){

            this.cpuMoveTimer=
                rand(.08,.25);

            if(d>145){

                if(dx>0){

                    this.vx=
                        this.speed*.72;

                    this.facing=1;

                }else{

                    this.vx=
                        -this.speed*.72;

                    this.facing=-1;
                }

            }else{

                this.vx*=.45;

                this.facing=
                    dx>=0
                    ?1
                    :-1;
            }

            if(
                this.onGround &&
                Math.random()<.08
            ){

                this.vy=
                    this.jumpPower;

                this.onGround=false;
            }
        }

        if(
            this.cpuAttackTimer<=0
        ){

            this.cpuAttackTimer=
                rand(.28,.7);

            if(
                d<110 &&
                this.attackCD<=0
            ){

                this.attack();

            }else if(
                d<430 &&
                this.energy>=25 &&
                this.skillCD<=0
            ){

                this.skill();

            }else if(
                d<340 &&
                this.energy>=100 &&
                this.ultCD<=0
            ){

                this.ultimate();

            }else if(
                d<140 &&
                this.heavyCD<=0
            ){

                this.heavy();

            }else if(
                this.energy<75 &&
                this.powerCD<=0 &&
                Math.random()<.25
            ){

                this.power();
            }
        }
    }

    attack(){

        if(
            this.attackCD>0 ||
            !this.alive()
        ){
            return;
        }

        this.attackCD=.38;
        this.attackFX=.17;

        const target=
            this.enemy();

        if(
            target &&
            target.alive()
        ){

            const dx=
                target.x-this.x;

            if(
                Math.abs(dx)<110 &&
                Math.sign(dx)===this.facing
            ){

                this.damage(
                    target,
                    7
                );

                burst(
                    target.x,
                    target.y-60,
                    this.glow,
                    18,
                    300
                );
            }
        }

        this.energy=
            clamp(
                this.energy+7,
                0,
                100
            );
    }

    skill(){

        if(
            this.skillCD>0 ||
            this.energy<25 ||
            !this.alive()
        ){
            return;
        }

        this.skillCD=.7;

        this.energy-=25;

        const direction=
            this.facing;

        projectiles.push({

            owner:this,

            x:
                this.x+
                direction*40,

            y:
                this.y-70,

            vx:
                direction*760,

            life:1.3,

            damage:15,

            color:this.glow,

            radius:12
        });

        burst(
            this.x+
            direction*40,
            this.y-70,
            this.glow,
            15,
            220
        );
    }

    dash(){

        if(
            this.dashCD>0 ||
            !this.alive()
        ){
            return;
        }

        this.dashCD=.9;

        burst(
            this.x,
            this.y-50,
            this.glow,
            18,
            220
        );

        this.x +=
            this.facing*135;

        this.x=
            clamp(
                this.x,
                45,
                W-45
            );
    }

    heavy(){

        if(
            this.heavyCD>0 ||
            !this.alive()
        ){
            return;
        }

        this.heavyCD=1;

        const target=
            this.enemy();

        if(
            target &&
            target.alive()
        ){

            const dx=
                target.x-this.x;

            if(
                Math.abs(dx)<145 &&
                Math.sign(dx)===this.facing
            ){

                this.damage(
                    target,
                    12
                );

                burst(
                    target.x,
                    target.y-55,
                    "#ffffff",
                    30,
                    420
                );
            }
        }

        this.energy=
            clamp(
                this.energy+12,
                0,
                100
            );
    }

    ultimate(){

        if(
            this.ultCD>0 ||
            this.energy<100 ||
            !this.alive()
        ){
            return;
        }

        this.ultCD=4;
        this.energy=0;

        const target=
            this.enemy();

        if(
            target &&
            target.alive()
        ){

            const dx=
                target.x-this.x;

            if(
                Math.abs(dx)<350 &&
                Math.sign(dx)===this.facing
            ){

                this.damage(
                    target,
                    32
                );

                for(
                    let i=0;
                    i<60;
                    i++
                ){

                    setTimeout(
                        ()=>{

                            burst(
                                target.x+
                                rand(-40,40),

                                target.y+
                                rand(-80,30),

                                i%2
                                    ?this.glow
                                    :"#ffffff",

                                3,
                                500
                            );

                        },
                        i*8
                    );
                }
            }
        }

        burst(
            this.x,
            this.y-60,
            this.glow,
            45,
            400
        );
    }

    recover(){

        if(
            this.recoverCD>0 ||
            this.energy<35 ||
            !this.alive()
        ){
            return;
        }

        this.recoverCD=3;

        this.energy-=35;

        this.hp=
            clamp(
                this.hp+15,
                0,
                100
            );

        burst(
            this.x,
            this.y-55,
            "#65ffb4",
            28,
            180
        );
    }

    power(){

        if(
            this.powerCD>0 ||
            this.energy>=100 ||
            !this.alive()
        ){
            return;
        }

        this.powerCD=1.2;

        this.energy=
            clamp(
                this.energy+20,
                0,
                100
            );

        burst(
            this.x,
            this.y-55,
            this.glow,
            18,
            170
        );
    }

    damage(
        target,
        amount
    ){

        if(
            !target ||
            !target.alive()
        ){
            return;
        }

        target.hp=
            clamp(
                target.hp-amount,
                0,
                100
            );

        target.flash=.13;

        target.x +=
            this.facing*28;

        target.x=
            clamp(
                target.x,
                45,
                W-45
            );
    }

    physics(dt){

        if(
            !this.alive()
        ){
            return;
        }

        this.x +=
            this.vx*dt;

        this.vy +=
            this.gravity*dt;

        this.y +=
            this.vy*dt;

        const floor=
            H-165;

        if(
            this.y>=floor
        ){

            this.y=floor;

            this.vy=0;

            this.onGround=true;

        }else{

            this.onGround=false;
        }

        this.x=
            clamp(
                this.x,
                45,
                W-45
            );
    }

    draw(){

        if(
            !this.alive()
        ){
            return;
        }

        const x=this.x;
        const y=this.y;

        /* shadow */

        ctx.save();

        ctx.globalAlpha=.28;

        ctx.fillStyle="#000";

        ctx.beginPath();

        ctx.ellipse(
            x,
            y+5,
            48,
            10,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.restore();

        /* aura */

        ctx.save();

        ctx.globalAlpha=.11;

        ctx.fillStyle=
            this.glow;

        ctx.shadowColor=
            this.glow;

        ctx.shadowBlur=35;

        ctx.beginPath();

        ctx.arc(
            x,
            y-62,
            72,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.restore();

        /* body */

        ctx.save();

        if(
            this.flash>0
        ){

            ctx.fillStyle="#ffffff";

        }else{

            ctx.fillStyle=
                this.primary;
        }

        ctx.shadowColor=
            this.glow;

        ctx.shadowBlur=20;

        roundRect(
            ctx,
            x-26,
            y-84,
            52,
            79,
            14
        );

        ctx.fill();

        ctx.shadowBlur=0;

        /* chest */

        ctx.fillStyle=
            "rgba(255,255,255,.15)";

        roundRect(
            ctx,
            x-17,
            y-73,
            34,
            40,
            9
        );

        ctx.fill();

        /* head */

        ctx.fillStyle=
            this.flash>0
            ?"#ffffff"
            :"#f1d0bd";

        ctx.beginPath();

        ctx.arc(
            x,
            y-107,
            27,
            0,
            Math.PI*2
        );

        ctx.fill();

        /* hair */

        ctx.fillStyle=
            this.team===1
            ?" #07172d"
            :"#270b12";

        ctx.beginPath();

        ctx.moveTo(
            x-28,
            y-107
        );

        ctx.lineTo(
            x-21,
            y-132
        );

        ctx.lineTo(
            x-9,
            y-122
        );

        ctx.lineTo(
            x,
            y-141
        );

        ctx.lineTo(
            x+10,
            y-122
        );

        ctx.lineTo(
            x+25,
            y-132
        );

        ctx.lineTo(
            x+28,
            y-105
        );

        ctx.closePath();

        ctx.fill();

        /* eye */

        ctx.fillStyle=
            "#ffffff";

        ctx.shadowColor=
            this.glow;

        ctx.shadowBlur=10;

        ctx.beginPath();

        ctx.ellipse(
            x+
            this.facing*10,
            y-105,
            6,
            4,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

        /* arm */

        ctx.strokeStyle=
            this.glow;

        ctx.lineWidth=10;

        ctx.lineCap="round";

        ctx.beginPath();

        ctx.moveTo(
            x+
            this.facing*17,
            y-64
        );

        ctx.lineTo(
            x+
            this.facing*47,
            y-53
        );

        ctx.stroke();

        /* attack slash */

        if(
            this.attackFX>0
        ){

            ctx.strokeStyle=
                "#ffffff";

            ctx.shadowColor=
                this.glow;

            ctx.shadowBlur=20;

            ctx.lineWidth=7;

            ctx.beginPath();

            if(
                this.facing===1
            ){

                ctx.arc(
                    x+15,
                    y-60,
                    55,
                    -.8,
                    .8
                );

            }else{

                ctx.arc(
                    x-15,
                    y-60,
                    55,
                    Math.PI-.8,
                    Math.PI+.8
                );
            }

            ctx.stroke();
        }

        ctx.restore();

        /* name */

        ctx.save();

        ctx.textAlign="center";

        ctx.font=
            "bold 13px Arial";

        ctx.fillStyle="#ffffff";

        ctx.shadowColor="#000";

        ctx.shadowBlur=7;

        ctx.fillText(
            this.name,
            x,
            y-148
        );

        ctx.restore();
    }
}

/* =========================================================
   ROUND RECT
========================================================= */

function roundRect(
    ctx,
    x,
    y,
    w,
    h,
    r
){

    ctx.beginPath();

    ctx.moveTo(
        x+r,
        y
    );

    ctx.arcTo(
        x+w,
        y,
        x+w,
        y+h,
        r
    );

    ctx.arcTo(
        x+w,
        y+h,
        x,
        y+h,
        r
    );

    ctx.arcTo(
        x,
        y+h,
        x,
        y,
        r
    );

    ctx.arcTo(
        x,
        y,
        x+w,
        y,
        r
    );

    ctx.closePath();
}

/* =========================================================
   PROJECTILES
========================================================= */

function updateProjectiles(dt){

    for(
        let i=projectiles.length-1;
        i>=0;
        i--
    ){

        const p=
            projectiles[i];

        p.x +=
            p.vx*dt;

        p.life -= dt;

        const target=
            p.owner===p1
            ?p2
            :p1;

        if(
            target &&
            target.alive() &&
            Math.abs(
                target.x-p.x
            )<48 &&
            Math.abs(
                target.y-65-p.y
            )<75
        ){

            p.owner.damage(
                target,
                p.damage
            );

            burst(
                target.x,
                target.y-60,
                p.color,
                25,
                350
            );

            projectiles.splice(
                i,
                1
            );

            continue;
        }

        if(
            p.life<=0 ||
            p.x<-100 ||
            p.x>W+100
        ){

            projectiles.splice(
                i,
                1
            );
        }
    }
}

function drawProjectiles(){

    for(
        const p of projectiles
    ){

        ctx.save();

        ctx.shadowColor=
            p.color;

        ctx.shadowBlur=28;

        ctx.fillStyle=
            p.color;

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.radius,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.restore();
    }
}

/* =========================================================
   BACKGROUND
========================================================= */

function drawBackground(){

    /* sky */

    const sky=
        ctx.createLinearGradient(
            0,
            0,
            0,
            H
        );

    sky.addColorStop(
        0,
        "#020514"
    );

    sky.addColorStop(
        .48,
        "#0a1230"
    );

    sky.addColorStop(
        1,
        "#03040b"
    );

    ctx.fillStyle=sky;

    ctx.fillRect(
        0,
        0,
        W,
        H
    );

    /* moon glow */

    const moonGlow=
        ctx.createRadialGradient(
            W*.72,
            H*.22,
            5,
            W*.72,
            H*.22,
            170
        );

    moonGlow.addColorStop(
        0,
        "rgba(180,220,255,.18)"
    );

    moonGlow.addColorStop(
        1,
        "rgba(180,220,255,0)"
    );

    ctx.fillStyle=
        moonGlow;

    ctx.fillRect(
        0,
        0,
        W,
        H*.55
    );

    /* moon */

    ctx.fillStyle=
        "rgba(215,235,255,.88)";

    ctx.shadowColor=
        "#9bdcff";

    ctx.shadowBlur=35;

    ctx.beginPath();

    ctx.arc(
        W*.72,
        H*.22,
        Math.min(W,H)*.075,
        0,
        Math.PI*2
    );

    ctx.fill();

    ctx.shadowBlur=0;

    /* stars */

    for(
        let i=0;
        i<100;
        i++
    ){

        const x=
            (i*193)%W;

        const y=
            (i*83)%(H*.58);

        const size=
            i%5===0
            ?2
            :1;

        ctx.globalAlpha=
            .25+
            (i%5)*.1;

        ctx.fillStyle=
            "#ffffff";

        ctx.fillRect(
            x,
            y,
            size,
            size
        );
    }

    ctx.globalAlpha=1;

    /* distant buildings */

    const horizon=
        H-170;

    for(
        let i=0;
        i<34;
        i++
    ){

        const bw=
            20+
            (i%5)*14;

        const bh=
            50+
            (i%8)*22;

        const bx=
            i*(W/34);

        ctx.fillStyle=
            i%3===0
            ?"rgba(10,17,40,.96)"
            :"rgba(6,10,27,.98)";

        ctx.fillRect(
            bx,
            horizon-bh,
            bw,
            bh
        );

        /* windows */

        ctx.fillStyle=
            "rgba(80,190,255,.16)";

        for(
            let wy=horizon-bh+10;
            wy<horizon-8;
            wy+=15
        ){

            if(
                (i+Math.floor(wy))%3===0
            ){

                ctx.fillRect(
                    bx+5,
                    wy,
                    4,
                    5
                );
            }
        }
    }

    /* arena floor */

    const floorY=
        H-165;

    const floor=
        ctx.createLinearGradient(
            0,
            floorY,
            0,
            H
        );

    floor.addColorStop(
        0,
        "#111a37"
    );

    floor.addColorStop(
        1,
        "#02030a"
    );

    ctx.fillStyle=floor;

    ctx.fillRect(
        0,
        floorY,
        W,
        H-floorY
    );

    /* floor grid */

    ctx.strokeStyle=
        "rgba(80,190,255,.10)";

    ctx.lineWidth=1;

    for(
        let x=0;
        x<W;
        x+=55
    ){

        ctx.beginPath();

        ctx.moveTo(
            x,
            floorY
        );

        ctx.lineTo(
            W/2+
            (x-W/2)*.38,
            H
        );

        ctx.stroke();
    }

    for(
        let y=floorY;
        y<H;
        y+=35
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

    /* arena line */

    ctx.strokeStyle=
        "rgba(80,220,255,.28)";

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

    /* center emblem */

    ctx.save();

    ctx.globalAlpha=.13;

    ctx.strokeStyle=
        "#50ddff";

    ctx.lineWidth=3;

    ctx.beginPath();

    ctx.arc(
        W/2,
        floorY+35,
        70,
        0,
        Math.PI*2
    );

    ctx.stroke();

    ctx.beginPath();

    ctx.moveTo(
        W/2-45,
        floorY+35
    );

    ctx.lineTo(
        W/2+45,
        floorY+35
    );

    ctx.moveTo(
        W/2,
        floorY-10
    );

    ctx.lineTo(
        W/2,
        floorY+80
    );

    ctx.stroke();

    ctx.restore();
}

/* =========================================================
   HUD
========================================================= */

function updateHUD(){

    if(
        !p1 ||
        !p2
    ){
        return;
    }

    document.getElementById(
        "leftName"
    ).textContent=
        p1.name;

    document.getElementById(
        "rightName"
    ).textContent=
        p2.name;

    document.getElementById(
        "leftHP"
    ).textContent=
        Math.round(p1.hp)+" HP";

    document.getElementById(
        "rightHP"
    ).textContent=
        Math.round(p2.hp)+" HP";

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
            Math.ceil(gameTime)
        );
}

/* =========================================================
   SETUP
========================================================= */

function setup(
    selectedMode
){

    mode=
        selectedMode;

    started=false;
    ended=false;

    gameTime=60;

    particles=[];
    projectiles=[];

    p1=
        new Fighter(
            "p1",
            1,
            W*.25,
            "#0fd7eb",
            "#65efff",
            playerName,
            false
        );

    if(
        mode==="cpu"
    ){

        p2=
            new Fighter(
                "p2",
                2,
                W*.75,
                "#ff4d57",
                "#ff795f",
                "CPU",
                true
            );

    }else{

        p2=
            new Fighter(
                "p2",
                2,
                W*.75,
                "#ff4d57",
                "#ff795f",
                "PLAYER 2",
                false
            );
    }

    fighters=[
        p1,
        p2
    ];

    document.getElementById(
        "leftName"
    ).textContent=
        p1.name;

    document.getElementById(
        "rightName"
    ).textContent=
        p2.name;

    document.getElementById(
        "home"
    ).style.display=
        "none";

    countdown();
}

/* =========================================================
   MODE
========================================================= */

function chooseMode(
    selectedMode
){

    const input=
        document.getElementById(
            "playerInput"
        );

    let name=
        input.value.trim();

    name=
        name
        .replace(/[<>]/g,"")
        .slice(0,20);

    if(
        name.length===0
    ){

        playerName=
            "PLAYER 1";

    }else{

        playerName=
            name;
    }

    setup(
        selectedMode
    );
}

/* =========================================================
   COUNTDOWN
========================================================= */

function countdown(){

    const box=
        document.getElementById(
            "countdown"
        );

    const text=
        document.getElementById(
            "countText"
        );

    box.style.display=
        "flex";

    const seq=[
        "3",
        "2",
        "1",
        "FIGHT!"
    ];

    let index=0;

    function next(){

        if(
            index>=seq.length
        ){

            box.style.display=
                "none";

            started=true;

            lastTime=
                performance.now();

            return;
        }

        text.textContent=
            seq[index];

        text.style.animation=
            "none";

        void text.offsetWidth;

        text.style.animation=
            "count .65s ease";

        index++;

        setTimeout(
            next,
            index===seq.length
                ?700
                :800
        );
    }

    next();
}

/* =========================================================
   FINISH
========================================================= */

function finish(){

    if(ended){
        return;
    }

    ended=true;

    const playerWon=
        p1.hp>0 &&
        p2.hp<=0;

    const playerLost=
        p1.hp<=0 &&
        p2.hp>0;

    let title="";

    if(
        playerWon
    ){

        title=
            "🎉 CHÚC MỪNG "+
            p1.name+
            "!<br>"+
            "🏆 BẠN ĐÃ CHIẾN THẮNG!";

        for(
            let i=0;
            i<100;
            i++
        ){

            setTimeout(
                ()=>{

                    burst(
                        rand(0,W),
                        rand(0,H*.75),
                        [
                            "#ffe66d",
                            "#ff63c8",
                            "#5ce8ff",
                            "#8cff9d",
                            "#ffffff"
                        ][
                            Math.floor(
                                Math.random()*5
                            )
                        ],
                        4,
                        500
                    );

                },
                i*10
            );
        }

    }else if(
        playerLost
    ){

        title=
            "💔 RẤT TIẾC "+
            p1.name+
            "!<br>"+
            "😭 CHIA BUỒN, BẠN ĐÃ THUA!";

    }else{

        if(
            p1.hp>p2.hp
        ){

            title=
                "🎉 CHÚC MỪNG "+
                p1.name+
                "!<br>"+
                "🏆 BẠN THẮNG THEO ĐIỂM!";

        }else if(
            p2.hp>p1.hp
        ){

            title=
                "💔 RẤT TIẾC "+
                p1.name+
                "!<br>"+
                "😭 CHIA BUỒN, BẠN ĐÃ THUA!";

        }else{

            title=
                "🤝 TRẬN ĐẤU HÒA!";
        }
    }

    title+=
        `<small>
        ${p1.name}: ${Math.round(p1.hp)} HP
        &nbsp; • &nbsp;
        ${p2.name}: ${Math.round(p2.hp)} HP
        </small>`;

    document.getElementById(
        "resultTitle"
    ).innerHTML=
        title;

    document.getElementById(
        "result"
    ).classList.add(
        "show"
    );
}

/* =========================================================
   UPDATE
========================================================= */

function update(dt){

    if(
        !started ||
        ended
    ){
        return;
    }

    gameTime-=dt;

    if(
        gameTime<=0
    ){

        gameTime=0;

        if(
            p1.hp>p2.hp
        ){

            p2.hp=0;

        }else if(
            p2.hp>p1.hp
        ){

            p1.hp=0;
        }

        finish();

        return;
    }

    for(
        const fighter
        of fighters
    ){

        fighter.cooldowns(dt);

        fighter.controls();

        fighter.cpuAI();

        fighter.physics(dt);
    }

    updateProjectiles(dt);

    updateParticles(dt);

    if(
        !p1.alive() ||
        !p2.alive()
    ){

        finish();
    }

    updateHUD();
}

/* =========================================================
   DRAW
========================================================= */

function draw(){

    drawBackground();

    drawProjectiles();

    for(
        const fighter
        of fighters
    ){

        fighter.draw();
    }

    drawParticles();
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

requestAnimationFrame(
    loop
);

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
