import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="AURA WAR",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
*{
    box-sizing:border-box;
}

html,body{
    margin:0;
    padding:0;
    width:100%;
    height:100%;
    overflow:hidden;
    font-family:Arial,Helvetica,sans-serif;
    background:#030511;
    color:#fff;
}

body{
    display:flex;
    justify-content:center;
    align-items:center;
}

#gameWrap{
    position:relative;
    width:100%;
    max-width:1250px;
    height:850px;
    overflow:hidden;
    border-radius:24px;
    background:#050817;
    border:1px solid rgba(120,160,255,.3);
    box-shadow:
        0 0 45px rgba(70,100,255,.3),
        inset 0 0 80px rgba(0,0,0,.65);
}

canvas{
    position:absolute;
    inset:0;
    width:100%;
    height:100%;
}

/* ================= HOME ================= */

.overlay{
    position:absolute;
    inset:0;
    z-index:20;
    display:flex;
    justify-content:center;
    align-items:center;
    background:
        radial-gradient(
            circle at 50% 20%,
            rgba(75,100,255,.3),
            transparent 38%
        ),
        rgba(2,4,15,.9);
    backdrop-filter:blur(8px);
}

.homeBox{
    width:min(1080px,94%);
    max-height:94%;
    overflow:auto;
    padding:30px;
    border-radius:28px;
    background:
        linear-gradient(
            145deg,
            rgba(18,27,67,.98),
            rgba(7,11,30,.99)
        );
    border:1px solid rgba(135,170,255,.35);
    box-shadow:
        0 0 55px rgba(70,100,255,.28),
        inset 0 1px 0 rgba(255,255,255,.08);
}

.logo{
    text-align:center;
    font-size:60px;
    line-height:1;
    font-weight:1000;
    letter-spacing:7px;
    color:white;
    text-shadow:
        0 0 8px #54c5ff,
        0 0 28px #4d73ff,
        0 0 60px rgba(110,70,255,.9);
}

.subtitle{
    text-align:center;
    margin-top:11px;
    color:#a9bbef;
    font-size:16px;
    letter-spacing:4px;
}

.nameArea{
    max-width:720px;
    margin:25px auto 18px;
}

.nameTitle{
    color:#a9bcec;
    font-size:13px;
    font-weight:900;
    margin-bottom:8px;
}

.nameInput{
    width:100%;
    height:52px;
    padding:0 17px;
    border-radius:14px;
    outline:none;
    border:1px solid rgba(130,170,255,.4);
    background:rgba(0,0,0,.25);
    color:white;
    font-size:17px;
}

.nameInput:focus{
    border-color:#62c5ff;
    box-shadow:0 0 22px rgba(70,160,255,.25);
}

.modeTitle{
    text-align:center;
    margin:17px 0 12px;
    color:#d9e5ff;
    font-size:15px;
    font-weight:1000;
}

.modeRow{
    display:flex;
    justify-content:center;
    gap:18px;
    flex-wrap:wrap;
}

.modeCard{
    width:300px;
    min-height:105px;
    padding:19px;
    cursor:pointer;
    border-radius:20px;
    background:rgba(255,255,255,.045);
    border:1px solid rgba(130,170,255,.25);
    transition:.2s;
}

.modeCard:hover{
    transform:translateY(-4px);
    border-color:#62c5ff;
    background:rgba(80,130,255,.12);
    box-shadow:0 12px 30px rgba(50,100,255,.22);
}

.modeCard.selected{
    border-color:#62c5ff;
    background:
        linear-gradient(
            145deg,
            rgba(55,140,255,.22),
            rgba(160,65,255,.13)
        );
    box-shadow:
        0 0 28px rgba(70,150,255,.24);
}

.modeIcon{
    font-size:30px;
}

.modeName{
    font-size:19px;
    font-weight:1000;
    margin-top:4px;
}

.modeDesc{
    margin-top:5px;
    color:#91a5d1;
    font-size:13px;
}

#p2Area{
    display:none;
    max-width:720px;
    margin:13px auto 0;
}

#p2Area.show{
    display:block;
}

/* ================= CONTROL BOX ================= */

.controlHome{
    max-width:930px;
    margin:24px auto 0;
    padding:18px;
    border-radius:20px;
    background:rgba(0,0,0,.18);
    border:1px solid rgba(120,165,255,.25);
}

.controlHeader{
    text-align:center;
    margin-bottom:14px;
    color:#dce7ff;
    font-size:15px;
    font-weight:1000;
}

.controlColumns{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:14px;
}

.controlSide{
    padding:13px;
    border-radius:15px;
    background:rgba(255,255,255,.035);
    border:1px solid rgba(255,255,255,.06);
}

.controlSideTitle{
    margin-bottom:9px;
    font-size:14px;
    font-weight:1000;
}

.p1title{
    color:#55c5ff;
}

.p2title{
    color:#dd82ff;
}

.controlList{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:6px;
}

.controlItem{
    color:#bac8e8;
    font-size:12px;
    line-height:1.4;
}

.key{
    display:inline-block;
    min-width:29px;
    margin-right:4px;
    padding:3px 6px;
    border-radius:6px;
    text-align:center;
    background:#111b3c;
    border:1px solid #324477;
    color:white;
    font-size:11px;
    font-weight:900;
}

.startBtn{
    display:block;
    width:310px;
    height:56px;
    margin:24px auto 0;
    border:0;
    border-radius:16px;
    cursor:pointer;
    color:white;
    font-size:17px;
    font-weight:1000;
    letter-spacing:1px;
    background:
        linear-gradient(
            90deg,
            #287eff,
            #7447ff,
            #bd48ff
        );
    box-shadow:0 8px 30px rgba(74,82,255,.4);
    transition:.2s;
}

.startBtn:hover{
    transform:translateY(-2px) scale(1.01);
    box-shadow:0 13px 38px rgba(74,82,255,.55);
}

.hint{
    margin-top:10px;
    text-align:center;
    color:#7183ae;
    font-size:11px;
}

/* ================= HUD ================= */

#hud{
    position:absolute;
    z-index:8;
    top:15px;
    left:18px;
    right:18px;
    display:none;
    pointer-events:none;
}

.hudRow{
    display:grid;
    grid-template-columns:1fr 120px 1fr;
    gap:14px;
    align-items:start;
}

.playerHud{
    min-width:0;
}

.playerHud.right{
    text-align:right;
}

.playerName{
    margin-bottom:6px;
    font-size:17px;
    font-weight:1000;
    white-space:nowrap;
    overflow:hidden;
    text-overflow:ellipsis;
}

.p1Color{
    color:#5ec7ff;
    text-shadow:0 0 12px rgba(60,190,255,.7);
}

.p2Color{
    color:#df82ff;
    text-shadow:0 0 12px rgba(210,70,255,.7);
}

.bar{
    width:100%;
    height:16px;
    overflow:hidden;
    border-radius:9px;
    background:#080c1c;
    border:1px solid rgba(255,255,255,.14);
}

.hpFill{
    width:100%;
    height:100%;
    background:linear-gradient(90deg,#35ff91,#b8ff5c);
    transition:width .08s linear;
}

.right .hpFill{
    margin-left:auto;
    background:linear-gradient(90deg,#ff68a5,#ff4d63);
}

.energyBar{
    height:7px;
    margin-top:5px;
}

.energyFill{
    width:0%;
    height:100%;
    background:linear-gradient(90deg,#47bfff,#b75cff);
    transition:width .08s linear;
}

.timerBox{
    padding:5px 10px 9px;
    border-radius:13px;
    text-align:center;
    background:rgba(4,8,25,.72);
    border:1px solid rgba(140,170,255,.25);
}

.timer{
    font-size:30px;
    line-height:1;
    font-weight:1000;
}

.timerLabel{
    margin-top:4px;
    color:#7f94c4;
    font-size:8px;
    letter-spacing:2px;
}

/* ================= COUNTDOWN ================= */

#countdown{
    position:absolute;
    inset:0;
    z-index:15;
    display:none;
    justify-content:center;
    align-items:center;
    pointer-events:none;
}

.countText{
    color:white;
    font-size:110px;
    font-weight:1000;
    text-shadow:
        0 0 10px #53bfff,
        0 0 35px #526aff,
        0 0 75px rgba(105,70,255,.8);
    animation:countPop .7s ease;
}

@keyframes countPop{
    from{
        transform:scale(.35);
        opacity:0;
    }
    55%{
        transform:scale(1.12);
        opacity:1;
    }
    to{
        transform:scale(1);
        opacity:1;
    }
}

/* ================= RESULT ================= */

#result{
    display:none;
}

.resultBox{
    width:min(620px,90%);
    padding:38px;
    border-radius:28px;
    text-align:center;
    background:
        linear-gradient(
            145deg,
            rgba(22,31,75,.98),
            rgba(8,12,31,.99)
        );
    border:1px solid rgba(150,180,255,.3);
    box-shadow:0 0 55px rgba(75,95,255,.3);
}

.resultTitle{
    font-size:42px;
    font-weight:1000;
    line-height:1.15;
}

.resultSub{
    margin-top:12px;
    color:#aebde0;
    font-size:16px;
    line-height:1.6;
}

.resultBtn{
    margin-top:25px;
    padding:14px 30px;
    border:0;
    border-radius:13px;
    cursor:pointer;
    color:white;
    background:linear-gradient(90deg,#287eff,#9a46ff);
    font-size:15px;
    font-weight:1000;
}

/* ================= BALLOONS ================= */

#balloons{
    position:absolute;
    inset:0;
    z-index:25;
    overflow:hidden;
    pointer-events:none;
    display:none;
}

.balloon{
    position:absolute;
    bottom:-130px;
    width:48px;
    height:62px;
    border-radius:50% 50% 47% 47%;
    animation:balloonFly linear forwards;
    filter:
        drop-shadow(0 0 10px rgba(255,255,255,.25));
}

.balloon::before{
    content:"";
    position:absolute;
    left:50%;
    bottom:-8px;
    transform:translateX(-50%);
    width:0;
    height:0;
    border-left:6px solid transparent;
    border-right:6px solid transparent;
    border-top:10px solid currentColor;
}

.balloon::after{
    content:"";
    position:absolute;
    left:50%;
    top:58px;
    width:1px;
    height:95px;
    background:rgba(255,255,255,.55);
    transform-origin:top;
    transform:rotate(2deg);
}

@keyframes balloonFly{
    0%{
        transform:
            translateY(0)
            translateX(0)
            rotate(-5deg);
        opacity:0;
    }

    8%{
        opacity:1;
    }

    50%{
        transform:
            translateY(-470px)
            translateX(35px)
            rotate(8deg);
    }

    100%{
        transform:
            translateY(-1000px)
            translateX(-30px)
            rotate(-7deg);
        opacity:0;
    }
}

/* ================= GAME HELP ================= */

#gameHelp{
    position:absolute;
    left:18px;
    bottom:15px;
    z-index:7;
    display:none;
    padding:9px 12px;
    border-radius:12px;
    background:rgba(4,7,20,.68);
    border:1px solid rgba(130,160,255,.16);
    color:#9eafd6;
    font-size:10px;
    pointer-events:none;
}

#gameHelp b{
    color:#dbe7ff;
}

/* ================= RESPONSIVE ================= */

@media(max-width:800px){

    .logo{
        font-size:39px;
    }

    .homeBox{
        padding:20px;
    }

    .controlColumns{
        grid-template-columns:1fr;
    }

    .modeCard{
        width:100%;
    }

    .hudRow{
        grid-template-columns:1fr 85px 1fr;
    }

    .playerName{
        font-size:12px;
    }

    .timer{
        font-size:22px;
    }

}
</style>
</head>

<body>

<div id="gameWrap">

<canvas id="gameCanvas"></canvas>

<!-- ================= HOME ================= -->

<div id="home" class="overlay">

    <div class="homeBox">

        <div class="logo">AURA WAR</div>

        <div class="subtitle">
            ⚡ AURA BATTLE • 1V1 ARENA ⚡
        </div>

        <div class="nameArea">

            <div class="nameTitle">
                👤 TÊN NGƯỜI CHƠI 1
            </div>

            <input
                id="playerInput"
                class="nameInput"
                maxlength="20"
                autocomplete="off"
                placeholder="Nhập tên Người chơi 1..."
            >

        </div>

        <div class="modeTitle">
            CHỌN CHẾ ĐỘ
        </div>

        <div class="modeRow">

            <div
                id="mode1v1"
                class="modeCard"
                onclick="chooseMode('1v1')"
            >

                <div class="modeIcon">⚔️</div>

                <div class="modeName">
                    1V1
                </div>

                <div class="modeDesc">
                    Hai người chơi đấu trực tiếp
                    trên cùng bàn phím.
                </div>

            </div>

            <div
                id="modeCPU"
                class="modeCard"
                onclick="chooseMode('cpu')"
            >

                <div class="modeIcon">🤖</div>

                <div class="modeName">
                    VS MÁY
                </div>

                <div class="modeDesc">
                    Đấu với CPU có AI tự di chuyển
                    và chiến đấu.
                </div>

            </div>

        </div>

        <!-- P2 -->

        <div id="p2Area">

            <div class="nameTitle">
                👤 TÊN NGƯỜI CHƠI 2
            </div>

            <input
                id="player2Input"
                class="nameInput"
                maxlength="20"
                autocomplete="off"
                placeholder="Nhập tên Người chơi 2..."
            >

        </div>

        <!-- CONTROL -->

        <div class="controlHome">

            <div class="controlHeader">
                🎮 HƯỚNG DẪN ĐIỀU KHIỂN
            </div>

            <div class="controlColumns">

                <div class="controlSide">

                    <div class="controlSideTitle p1title">
                        🔵 NGƯỜI CHƠI 1
                    </div>

                    <div class="controlList">

                        <div class="controlItem">
                            <span class="key">A</span>
                            Trái
                        </div>

                        <div class="controlItem">
                            <span class="key">D</span>
                            Phải
                        </div>

                        <div class="controlItem">
                            <span class="key">W</span>
                            Nhảy
                        </div>

                        <div class="controlItem">
                            <span class="key">S</span>
                            Rơi nhanh
                        </div>

                        <div class="controlItem">
                            <span class="key">J</span>
                            Đánh
                        </div>

                        <div class="controlItem">
                            <span class="key">K</span>
                            Skill
                        </div>

                        <div class="controlItem">
                            <span class="key">L</span>
                            Dash
                        </div>

                        <div class="controlItem">
                            <span class="key">U</span>
                            Đánh mạnh
                        </div>

                        <div class="controlItem">
                            <span class="key">I</span>
                            Tuyệt kỹ
                        </div>

                    </div>

                </div>

                <div id="p2Control" class="controlSide">

                    <div class="controlSideTitle p2title">
                        🟣 NGƯỜI CHƠI 2
                    </div>

                    <div class="controlList">

                        <div class="controlItem">
                            <span class="key">←</span>
                            Trái
                        </div>

                        <div class="controlItem">
                            <span class="key">→</span>
                            Phải
                        </div>

                        <div class="controlItem">
                            <span class="key">↑</span>
                            Nhảy
                        </div>

                        <div class="controlItem">
                            <span class="key">↓</span>
                            Rơi nhanh
                        </div>

                        <div class="controlItem">
                            <span class="key">1</span>
                            Đánh
                        </div>

                        <div class="controlItem">
                            <span class="key">2</span>
                            Skill
                        </div>

                        <div class="controlItem">
                            <span class="key">3</span>
                            Dash
                        </div>

                        <div class="controlItem">
                            <span class="key">4</span>
                            Đánh mạnh
                        </div>

                        <div class="controlItem">
                            <span class="key">5</span>
                            Tuyệt kỹ
                        </div>

                    </div>

                </div>

            </div>

        </div>

        <button
            class="startBtn"
            onclick="startGame()"
        >
            ⚔️ BẮT ĐẦU TRẬN
        </button>

        <div class="hint">
            Không cần ảnh hay file ngoài • Tên tối đa 20 ký tự
        </div>

    </div>

</div>

<!-- ================= HUD ================= -->

<div id="hud">

    <div class="hudRow">

        <div class="playerHud">

            <div
                id="p1Name"
                class="playerName p1Color"
            >
                PLAYER 1
            </div>

            <div class="bar">
                <div
                    id="p1Hp"
                    class="hpFill"
                ></div>
            </div>

            <div class="bar energyBar">
                <div
                    id="p1Energy"
                    class="energyFill"
                ></div>
            </div>

        </div>

        <div class="timerBox">

            <div
                id="timer"
                class="timer"
            >
                60
            </div>

            <div class="timerLabel">
                TIME
            </div>

        </div>

        <div class="playerHud right">

            <div
                id="p2Name"
                class="playerName p2Color"
            >
                PLAYER 2
            </div>

            <div class="bar">
                <div
                    id="p2Hp"
                    class="hpFill"
                ></div>
            </div>

            <div class="bar energyBar">
                <div
                    id="p2Energy"
                    class="energyFill"
                ></div>
            </div>

        </div>

    </div>

</div>

<!-- COUNTDOWN -->

<div id="countdown">

    <div
        id="countText"
        class="countText"
    >
        3
    </div>

</div>

<!-- HELP -->

<div id="gameHelp">

    <b>P1:</b>
    A/D trái/phải • W nhảy • J đánh • K skill • L dash • U mạnh • I ulti

    &nbsp;&nbsp;|&nbsp;&nbsp;

    <b>P2:</b>
    ←/→ trái/phải • ↑ nhảy • 1 đánh • 2 skill • 3 dash • 4 mạnh • 5 ulti

</div>

<!-- BALLOONS -->

<div id="balloons"></div>

<!-- RESULT -->

<div id="result" class="overlay">

    <div class="resultBox">

        <div
            id="resultTitle"
            class="resultTitle"
        >
            🏆 CHIẾN THẮNG!
        </div>

        <div
            id="resultSub"
            class="resultSub"
        >
            Bạn đã chiến thắng!
        </div>

        <button
            class="resultBtn"
            onclick="location.reload()"
        >
            🔄 CHƠI LẠI
        </button>

    </div>

</div>

</div>

<script>

/* =========================================================
   CANVAS
========================================================= */

const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

let W = 1200;
let H = 850;

function resizeCanvas(){

    const rect = canvas.getBoundingClientRect();

    W = Math.max(760, rect.width);
    H = Math.max(550, rect.height);

    const dpr =
        Math.min(window.devicePixelRatio || 1, 2);

    canvas.width = Math.floor(W * dpr);
    canvas.height = Math.floor(H * dpr);

    ctx.setTransform(
        dpr,
        0,
        0,
        dpr,
        0,
        0
    );
}

window.addEventListener(
    "resize",
    resizeCanvas
);

resizeCanvas();


/* =========================================================
   GAME VARIABLES
========================================================= */

let selectedMode = null;

let playerName = "PLAYER 1";
let player2Name = "PLAYER 2";

let started = false;
let ended = false;

let gameTime = 60;

let p1 = null;
let p2 = null;

let fighters = [];

let projectiles = [];
let particles = [];

let keys = {};

let lastTime = performance.now();

const GROUND = 650;

const ENERGY_REGEN = 8.0;


/* =========================================================
   INPUT
========================================================= */

window.addEventListener(
    "keydown",
    function(e){

        const key =
            e.key.toLowerCase();

        keys[key] = true;

        if([
            "arrowleft",
            "arrowright",
            "arrowup",
            "arrowdown",
            " "
        ].includes(key)){
            e.preventDefault();
        }

    }
);

window.addEventListener(
    "keyup",
    function(e){

        keys[e.key.toLowerCase()] = false;

    }
);


/* =========================================================
   HOME
========================================================= */

function chooseMode(mode){

    selectedMode = mode;

    document
        .getElementById("mode1v1")
        .classList.remove("selected");

    document
        .getElementById("modeCPU")
        .classList.remove("selected");

    if(mode === "1v1"){

        document
            .getElementById("mode1v1")
            .classList.add("selected");

        document
            .getElementById("p2Area")
            .classList.add("show");

        document
            .getElementById("p2Control")
            .style.display = "block";

    }else{

        document
            .getElementById("modeCPU")
            .classList.add("selected");

        document
            .getElementById("p2Area")
            .classList.remove("show");

        document
            .getElementById("p2Control")
            .style.display = "none";

    }

}


/* =========================================================
   START
========================================================= */

function startGame(){

    if(!selectedMode){
        chooseMode("1v1");
    }

    let name1 =
        document
        .getElementById("playerInput")
        .value
        .trim();

    let name2 =
        document
        .getElementById("player2Input")
        .value
        .trim();

    name1 =
        name1
        .replace(/[<>]/g,"")
        .slice(0,20);

    name2 =
        name2
        .replace(/[<>]/g,"")
        .slice(0,20);

    playerName =
        name1.length > 0
        ? name1
        : "PLAYER 1";

    if(selectedMode === "1v1"){

        player2Name =
            name2.length > 0
            ? name2
            : "PLAYER 2";

    }else{

        player2Name = "CPU";

    }

    setupGame();

    document
        .getElementById("home")
        .style.display = "none";

    document
        .getElementById("hud")
        .style.display = "block";

    document
        .getElementById("gameHelp")
        .style.display = "block";

    startCountdown();

}


/* =========================================================
   FIGHTER CLASS
========================================================= */

class Fighter{

    constructor(
        x,
        team,
        name,
        cpu
    ){

        this.x = x;
        this.y = GROUND;

        this.vx = 0;
        this.vy = 0;

        this.team = team;
        this.name = name;

        this.cpu = cpu;

        this.hp = 100;
        this.energy = 0;

        this.width = 56;
        this.height = 105;

        this.speed = 310;

        this.jumpPower = -630;

        this.gravity = 1650;

        this.grounded = true;

        this.facing =
            team === 1
            ? 1
            : -1;

        this.attackTimer = 0;
        this.attackCooldown = 0;

        this.skillCooldown = 0;
        this.dashCooldown = 0;
        this.heavyCooldown = 0;
        this.ultimateCooldown = 0;

        this.hitFlash = 0;

        this.invincible = 0;

        this.aiThink = 0;

        this.aiMove = 0;

        this.aiStrafe = 0;

    }

    alive(){

        return this.hp > 0;

    }

    centerX(){

        return this.x + this.width / 2;

    }

    centerY(){

        return this.y - this.height / 2;

    }

    cooldowns(dt){

        this.attackCooldown =
            Math.max(
                0,
                this.attackCooldown - dt
            );

        this.skillCooldown =
            Math.max(
                0,
                this.skillCooldown - dt
            );

        this.dashCooldown =
            Math.max(
                0,
                this.dashCooldown - dt
            );

        this.heavyCooldown =
            Math.max(
                0,
                this.heavyCooldown - dt
            );

        this.ultimateCooldown =
            Math.max(
                0,
                this.ultimateCooldown - dt
            );

        this.attackTimer =
            Math.max(
                0,
                this.attackTimer - dt
            );

        this.hitFlash =
            Math.max(
                0,
                this.hitFlash - dt
            );

        this.invincible =
            Math.max(
                0,
                this.invincible - dt
            );

    }

    controls(){

        if(this.cpu){
            return;
        }

        let left = false;
        let right = false;
        let jump = false;

        if(this.team === 1){

            left = keys["a"];
            right = keys["d"];
            jump = keys["w"];

            if(left && !right){
                this.vx = -this.speed;
                this.facing = -1;
            }
            else if(right && !left){
                this.vx = this.speed;
                this.facing = 1;
            }
            else{
                this.vx *= 0.78;
            }

            if(
                jump &&
                this.grounded
            ){
                this.vy =
                    this.jumpPower;

                this.grounded = false;
            }

            if(keys["s"]){
                this.vy += 900 * 0.016;
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

        }else{

            left = keys["arrowleft"];
            right = keys["arrowright"];
            jump = keys["arrowup"];

            if(left && !right){
                this.vx = -this.speed;
                this.facing = -1;
            }
            else if(right && !left){
                this.vx = this.speed;
                this.facing = 1;
            }
            else{
                this.vx *= 0.78;
            }

            if(
                jump &&
                this.grounded
            ){
                this.vy =
                    this.jumpPower;

                this.grounded = false;
            }

            if(keys["arrowdown"]){
                this.vy += 900 * 0.016;
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

        }

    }

    cpuAI(){

        if(!this.cpu || !p1){
            return;
        }

        const target = p1;

        const dx =
            target.centerX() -
            this.centerX();

        const distance =
            Math.abs(dx);

        const direction =
            dx > 0 ? 1 : -1;

        this.facing = direction;

        this.aiThink -= 0.016;

        if(this.aiThink <= 0){

            this.aiThink =
                0.12 +
                Math.random() * 0.16;

            if(distance > 250){

                this.aiMove =
                    direction;

            }
            else if(distance < 95){

                this.aiMove =
                    Math.random() < .65
                    ? -direction
                    : direction;

            }
            else{

                this.aiMove =
                    Math.random() < .55
                    ? direction
                    : 0;

            }

            this.aiStrafe =
                Math.random() * 2 - 1;

        }

        const targetSpeed =
            this.aiMove *
            this.speed *
            (
                distance > 180
                ? 1
                : .58
            );

        const acceleration = 10;

        this.vx +=
            (
                targetSpeed -
                this.vx
            ) *
            Math.min(
                1,
                acceleration * 0.016
            );

        if(Math.abs(this.vx) > 20){

            this.facing =
                this.vx > 0
                ? 1
                : -1;

        }

        if(
            this.grounded &&
            distance > 230 &&
            Math.random() < 0.012
        ){

            this.vy =
                this.jumpPower;

            this.grounded = false;

        }

        if(
            this.grounded &&
            distance < 120 &&
            Math.random() < 0.008
        ){

            this.vy =
                this.jumpPower * .82;

            this.grounded = false;

        }

        if(
            distance < 100 &&
            this.attackCooldown <= 0
        ){

            if(Math.random() < .78){

                this.attack();

            }

        }

        if(
            distance < 340 &&
            this.energy >= 25 &&
            this.skillCooldown <= 0
        ){

            if(Math.random() < .018){

                this.skill();

            }

        }

        if(
            distance < 170 &&
            this.dashCooldown <= 0
        ){

            if(Math.random() < .009){

                this.dash();

            }

        }

        if(
            distance < 120 &&
            this.heavyCooldown <= 0
        ){

            if(Math.random() < .008){

                this.heavy();

            }

        }

        if(
            distance < 320 &&
            this.energy >= 100 &&
            this.ultimateCooldown <= 0
        ){

            if(Math.random() < .025){

                this.ultimate();

            }

        }

    }

    physics(dt){

        this.x +=
            this.vx * dt;

        this.vy +=
            this.gravity * dt;

        this.y +=
            this.vy * dt;

        if(this.y >= GROUND){

            this.y = GROUND;

            this.vy = 0;

            this.grounded = true;

        }

        this.x =
            Math.max(
                50,
                Math.min(
                    W - this.width - 50,
                    this.x
                )
            );

        if(
            Math.abs(this.vx) < 2
        ){
            this.vx = 0;
        }

    }

    attack(){

        if(
            this.attackCooldown > 0 ||
            !this.alive()
        ){
            return;
        }

        this.attackCooldown =
            0.38;

        this.attackTimer =
            0.16;

        const target =
            this.team === 1
            ? p2
            : p1;

        if(
            !target ||
            !target.alive()
        ){
            return;
        }

        const dx =
            target.centerX() -
            this.centerX();

        const facingCorrect =
            Math.sign(dx) === this.facing;

        if(
            Math.abs(dx) < 105 &&
            facingCorrect
        ){

            target.takeDamage(
                7,
                this.facing * 180
            );

            this.energy =
                Math.min(
                    100,
                    this.energy + 7
                );

            spawnHit(
                target.centerX(),
                target.centerY()
            );

        }

    }

    skill(){

        if(
            this.energy < 25 ||
            this.skillCooldown > 0 ||
            !this.alive()
        ){
            return;
        }

        this.energy -= 25;

        this.skillCooldown =
            0.8;

        projectiles.push({

            x:
                this.centerX() +
                this.facing * 38,

            y:
                this.centerY() - 8,

            vx:
                this.facing * 720,

            team:this.team,

            damage:15,

            life:1.5,

            radius:12

        });

        spawnAura(
            this.centerX(),
            this.centerY(),
            this.team === 1
            ? "#42bfff"
            : "#d86cff"
        );

    }

    dash(){

        if(
            this.dashCooldown > 0 ||
            !this.alive()
        ){
            return;
        }

        this.dashCooldown =
            0.65;

        this.invincible =
            0.12;

        this.vx =
            this.facing * 820;

        spawnDash(
            this.centerX(),
            this.centerY(),
            this.team === 1
            ? "#45bfff"
            : "#d66cff"
        );

    }

    heavy(){

        if(
            this.heavyCooldown > 0 ||
            !this.alive()
        ){
            return;
        }

        this.heavyCooldown =
            0.8;

        this.attackTimer =
            0.25;

        const target =
            this.team === 1
            ? p2
            : p1;

        if(!target){
            return;
        }

        const dx =
            target.centerX() -
            this.centerX();

        if(
            Math.abs(dx) < 130 &&
            Math.sign(dx) === this.facing
        ){

            target.takeDamage(
                13,
                this.facing * 300
            );

            this.energy =
                Math.min(
                    100,
                    this.energy + 10
                );

            spawnBigHit(
                target.centerX(),
                target.centerY()
            );

        }

    }

    ultimate(){

        if(
            this.energy < 100 ||
            this.ultimateCooldown > 0 ||
            !this.alive()
        ){
            return;
        }

        this.energy = 0;

        this.ultimateCooldown =
            4;

        const target =
            this.team === 1
            ? p2
            : p1;

        if(!target){
            return;
        }

        const dx =
            target.centerX() -
            this.centerX();

        if(
            Math.abs(dx) < 310 &&
            Math.sign(dx) === this.facing
        ){

            target.takeDamage(
                32,
                this.facing * 500
            );

            spawnUltimate(
                target.centerX(),
                target.centerY(),
                this.team === 1
                ? "#47c8ff"
                : "#df6cff"
            );

        }

    }

    takeDamage(amount, knockback){

        if(
            this.invincible > 0 ||
            !this.alive()
        ){
            return;
        }

        this.hp =
            Math.max(
                0,
                this.hp - amount
            );

        this.vx +=
            knockback;

        this.vy =
            -180;

        this.hitFlash =
            0.12;

    }

    draw(){

        const x =
            this.centerX();

        const y =
            this.y;

        const auraColor =
            this.team === 1
            ? "#37bfff"
            : "#dc62ff";

        ctx.save();

        /* aura */

        const aura =
            ctx.createRadialGradient(
                x,
                y - 60,
                5,
                x,
                y - 60,
                90
            );

        aura.addColorStop(
            0,
            auraColor + "80"
        );

        aura.addColorStop(
            1,
            auraColor + "00"
        );

        ctx.fillStyle = aura;

        ctx.beginPath();

        ctx.arc(
            x,
            y - 60,
            90,
            0,
            Math.PI * 2
        );

        ctx.fill();

        /* shadow */

        ctx.fillStyle =
            "rgba(0,0,0,.4)";

        ctx.beginPath();

        ctx.ellipse(
            x,
            GROUND + 3,
            43,
            10,
            0,
            0,
            Math.PI * 2
        );

        ctx.fill();

        /* body */

        ctx.fillStyle =
            this.team === 1
            ? "#173f72"
            : "#64206f";

        ctx.beginPath();

        ctx.roundRect(
            x - 22,
            y - 88,
            44,
            58,
            12
        );

        ctx.fill();

        /* chest aura */

        ctx.strokeStyle =
            auraColor;

        ctx.lineWidth = 3;

        ctx.beginPath();

        ctx.roundRect(
            x - 22,
            y - 88,
            44,
            58,
            12
        );

        ctx.stroke();

        /* head */

        ctx.fillStyle =
            this.hitFlash > 0
            ? "#ffffff"
            : "#ffd8b0";

        ctx.beginPath();

        ctx.arc(
            x,
            y - 108,
            24,
            0,
            Math.PI * 2
        );

        ctx.fill();

        /* hair */

        ctx.fillStyle =
            this.team === 1
            ? "#07172d"
            : "#270b12";

        ctx.beginPath();

        ctx.moveTo(
            x - 24,
            y - 109
        );

        ctx.lineTo(
            x - 14,
            y - 135
        );

        ctx.lineTo(
            x - 3,
            y - 120
        );

        ctx.lineTo(
            x + 9,
            y - 138
        );

        ctx.lineTo(
            x + 20,
            y - 119
        );

        ctx.lineTo(
            x + 25,
            y - 102
        );

        ctx.lineTo(
            x - 24,
            y - 102
        );

        ctx.closePath();

        ctx.fill();

        /* eyes */

        ctx.fillStyle =
            auraColor;

        ctx.beginPath();

        ctx.arc(
            x + this.facing * 8,
            y - 108,
            3.5,
            0,
            Math.PI * 2
        );

        ctx.fill();

        /* arm */

        ctx.strokeStyle =
            "#ffd8b0";

        ctx.lineWidth = 9;

        ctx.lineCap = "round";

        ctx.beginPath();

        ctx.moveTo(
            x + this.facing * 17,
            y - 75
        );

        ctx.lineTo(
            x + this.facing * 40,
            y - 63
        );

        ctx.stroke();

        /* attack slash */

        if(this.attackTimer > 0){

            ctx.strokeStyle =
                auraColor;

            ctx.lineWidth = 7;

            ctx.shadowColor =
                auraColor;

            ctx.shadowBlur = 18;

            ctx.beginPath();

            ctx.arc(
                x + this.facing * 42,
                y - 76,
                38,
                this.facing === 1
                ? -1.15
                : 2.0,
                this.facing === 1
                ? 0.45
                : 3.85
            );

            ctx.stroke();

            ctx.shadowBlur = 0;

        }

        ctx.restore();

    }

}


/* =========================================================
   SETUP
========================================================= */

function setupGame(){

    p1 =
        new Fighter(
            W * .25,
            1,
            playerName,
            false
        );

    p2 =
        new Fighter(
            W * .75,
            2,
            player2Name,
            selectedMode === "cpu"
        );

    fighters = [
        p1,
        p2
    ];

    projectiles = [];
    particles = [];

    gameTime = 60;

    started = false;
    ended = false;

    updateHUD();

}


/* =========================================================
   COUNTDOWN
========================================================= */

function startCountdown(){

    const box =
        document.getElementById("countdown");

    const text =
        document.getElementById("countText");

    box.style.display = "flex";

    const values =
        ["3","2","1","FIGHT!"];

    let index = 0;

    function next(){

        if(index >= values.length){

            box.style.display =
                "none";

            started = true;

            return;
        }

        text.textContent =
            values[index];

        text.style.animation =
            "none";

        void text.offsetWidth;

        text.style.animation =
            "countPop .7s ease";

        index++;

        setTimeout(
            next,
            index === values.length
            ? 650
            : 700
        );

    }

    next();

}


/* =========================================================
   PROJECTILES
========================================================= */

function updateProjectiles(dt){

    for(
        let i = projectiles.length - 1;
        i >= 0;
        i--
    ){

        const p =
            projectiles[i];

        p.x +=
            p.vx * dt;

        p.life -= dt;

        spawnTrail(
            p.x,
            p.y,
            p.team === 1
            ? "#47c8ff"
            : "#df6cff"
        );

        const target =
            p.team === 1
            ? p2
            : p1;

        if(
            target &&
            target.alive()
        ){

            const dx =
                target.centerX() -
                p.x;

            const dy =
                target.centerY() -
                p.y;

            if(
                Math.abs(dx) < 45 &&
                Math.abs(dy) < 70
            ){

                target.takeDamage(
                    p.damage,
                    p.vx > 0
                    ? 240
                    : -240
                );

                spawnBigHit(
                    p.x,
                    p.y
                );

                projectiles.splice(
                    i,
                    1
                );

                continue;

            }

        }

        if(
            p.life <= 0 ||
            p.x < -100 ||
            p.x > W + 100
        ){

            projectiles.splice(
                i,
                1
            );

        }

    }

}


/* =========================================================
   PARTICLES
========================================================= */

function addParticle(
    x,
    y,
    color,
    size,
    life,
    vx,
    vy
){

    particles.push({

        x:x,
        y:y,

        vx:vx,
        vy:vy,

        color:color,

        size:size,

        life:life,

        maxLife:life

    });

}

function spawnHit(x,y){

    for(let i=0;i<12;i++){

        const a =
            Math.random() *
            Math.PI * 2;

        const s =
            70 +
            Math.random() * 170;

        addParticle(
            x,
            y,
            "#ffffff",
            2 +
            Math.random() * 3,
            .35 +
            Math.random() * .2,
            Math.cos(a) * s,
            Math.sin(a) * s
        );

    }

}

function spawnBigHit(x,y){

    for(let i=0;i<24;i++){

        const a =
            Math.random() *
            Math.PI * 2;

        const s =
            100 +
            Math.random() * 300;

        addParticle(
            x,
            y,
            Math.random() < .5
            ? "#fff"
            : "#62c5ff",
            3 +
            Math.random() * 4,
            .45 +
            Math.random() * .25,
            Math.cos(a) * s,
            Math.sin(a) * s
        );

    }

}

function spawnAura(x,y,color){

    for(let i=0;i<18;i++){

        const a =
            Math.random() *
            Math.PI * 2;

        const r =
            Math.random() * 30;

        addParticle(
            x + Math.cos(a) * r,
            y + Math.sin(a) * r,
            color,
            2 +
            Math.random() * 3,
            .5 +
            Math.random() * .4,
            Math.cos(a) * 100,
            Math.sin(a) * 100
        );

    }

}

function spawnDash(x,y,color){

    for(let i=0;i<12;i++){

        addParticle(
            x,
            y,
            color,
            3,
            .3,
            -Math.random() * 300,
            (Math.random() - .5) * 180
        );

    }

}

function spawnUltimate(x,y,color){

    for(let i=0;i<70;i++){

        const a =
            Math.random() *
            Math.PI * 2;

        const s =
            100 +
            Math.random() * 450;

        addParticle(
            x,
            y,
            i % 2 === 0
            ? color
            : "#ffffff",
            3 +
            Math.random() * 6,
            .7 +
            Math.random() * .7,
            Math.cos(a) * s,
            Math.sin(a) * s
        );

    }

}

function spawnTrail(x,y,color){

    if(Math.random() > .45){
        return;
    }

    addParticle(
        x,
        y,
        color,
        2,
        .2,
        -20,
        0
    );

}

function updateParticles(dt){

    for(
        let i = particles.length - 1;
        i >= 0;
        i--
    ){

        const p =
            particles[i];

        p.life -= dt;

        p.x +=
            p.vx * dt;

        p.y +=
            p.vy * dt;

        p.vy +=
            400 * dt;

        if(p.life <= 0){

            particles.splice(
                i,
                1
            );

        }

    }

}

function drawParticles(){

    for(const p of particles){

        const alpha =
            Math.max(
                0,
                p.life / p.maxLife
            );

        ctx.globalAlpha =
            alpha;

        ctx.fillStyle =
            p.color;

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.size,
            0,
            Math.PI * 2
        );

        ctx.fill();

    }

    ctx.globalAlpha = 1;

}


/* =========================================================
   BACKGROUND
========================================================= */

function drawBackground(){

    const grad =
        ctx.createLinearGradient(
            0,
            0,
            0,
            H
        );

    grad.addColorStop(
        0,
        "#070b28"
    );

    grad.addColorStop(
        .5,
        "#10144a"
    );

    grad.addColorStop(
        1,
        "#03040c"
    );

    ctx.fillStyle = grad;

    ctx.fillRect(
        0,
        0,
        W,
        H
    );

    /* moon */

    const moon =
        ctx.createRadialGradient(
            W * .5,
            155,
            10,
            W * .5,
            155,
            100
        );

    moon.addColorStop(
        0,
        "rgba(220,235,255,.95)"
    );

    moon.addColorStop(
        .3,
        "rgba(120,170,255,.45)"
    );

    moon.addColorStop(
        1,
        "rgba(90,120,255,0)"
    );

    ctx.fillStyle = moon;

    ctx.beginPath();

    ctx.arc(
        W * .5,
        155,
        100,
        0,
        Math.PI * 2
    );

    ctx.fill();

    /* stars */

    for(let i=0;i<100;i++){

        const sx =
            (i * 97) % W;

        const sy =
            60 +
            ((i * 53) % 310);

        const size =
            1 +
            ((i * 7) % 3);

        ctx.fillStyle =
            i % 4 === 0
            ? "rgba(110,200,255,.9)"
            : "rgba(255,255,255,.55)";

        ctx.fillRect(
            sx,
            sy,
            size,
            size
        );

    }

    /* city */

    const cityBase =
        GROUND - 120;

    for(let i=0;i<30;i++){

        const bw =
            25 +
            ((i * 37) % 55);

        const bh =
            60 +
            ((i * 71) % 150);

        const bx =
            i * (W / 29) -
            10;

        ctx.fillStyle =
            i % 2 === 0
            ? "#080d25"
            : "#0c1231";

        ctx.fillRect(
            bx,
            cityBase - bh,
            bw,
            bh
        );

        for(
            let wy=cityBase-bh+12;
            wy<cityBase-8;
            wy+=18
        ){

            if(
                ((i * 5) +
                Math.floor(wy)) % 3 !== 0
            ){

                ctx.fillStyle =
                    "rgba(90,180,255,.35)";

                ctx.fillRect(
                    bx + 7,
                    wy,
                    5,
                    4
                );

            }

        }

    }

    /* arena */

    const arenaGrad =
        ctx.createLinearGradient(
            0,
            GROUND,
            0,
            H
        );

    arenaGrad.addColorStop(
        0,
        "#10182e"
    );

    arenaGrad.addColorStop(
        1,
        "#04060e"
    );

    ctx.fillStyle =
        arenaGrad;

    ctx.fillRect(
        0,
        GROUND,
        W,
        H - GROUND
    );

    /* horizon */

    ctx.strokeStyle =
        "rgba(90,180,255,.22)";

    ctx.lineWidth = 2;

    ctx.beginPath();

    ctx.moveTo(
        0,
        GROUND
    );

    ctx.lineTo(
        W,
        GROUND
    );

    ctx.stroke();

    /* floor grid */

    ctx.strokeStyle =
        "rgba(90,130,255,.1)";

    ctx.lineWidth = 1;

    for(
        let y=GROUND+25;
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

    for(
        let x=-W;
        x<W*2;
        x+=70
    ){

        ctx.beginPath();

        ctx.moveTo(
            W/2 + (x-W/2)*.25,
            GROUND
        );

        ctx.lineTo(
            x,
            H
        );

        ctx.stroke();

    }

    /* center symbol */

    ctx.strokeStyle =
        "rgba(90,190,255,.2)";

    ctx.lineWidth = 3;

    ctx.beginPath();

    ctx.arc(
        W/2,
        GROUND+3,
        85,
        0,
        Math.PI*2
    );

    ctx.stroke();

    ctx.beginPath();

    ctx.moveTo(
        W/2-55,
        GROUND+3
    );

    ctx.lineTo(
        W/2+55,
        GROUND+3
    );

    ctx.stroke();

}


/* =========================================================
   HUD
========================================================= */

function updateHUD(){

    if(!p1 || !p2){
        return;
    }

    document
        .getElementById("p1Name")
        .textContent =
        p1.name;

    document
        .getElementById("p2Name")
        .textContent =
        p2.name;

    document
        .getElementById("p1Hp")
        .style.width =
        Math.max(
            0,
            p1.hp
        ) + "%";

    document
        .getElementById("p2Hp")
        .style.width =
        Math.max(
            0,
            p2.hp
        ) + "%";

    document
        .getElementById("p1Energy")
        .style.width =
        Math.max(
            0,
            p1.energy
        ) + "%";

    document
        .getElementById("p2Energy")
        .style.width =
        Math.max(
            0,
            p2.energy
        ) + "%";

    document
        .getElementById("timer")
        .textContent =
        Math.max(
            0,
            Math.ceil(gameTime)
        );

}


/* =========================================================
   BALLOONS
========================================================= */

function showVictoryBalloons(){

    const container =
        document.getElementById(
            "balloons"
        );

    container.innerHTML = "";

    container.style.display =
        "block";

    const balloonColors = [
        "#ff4f81",
        "#4cbcff",
        "#ffd447",
        "#9d67ff",
        "#4dff9a",
        "#ff7048"
    ];

    for(
        let i=0;
        i<32;
        i++
    ){

        const b =
            document.createElement(
                "div"
            );

        b.className =
            "balloon";

        const color =
            balloonColors[
                i % balloonColors.length
            ];

        b.style.background =
            color;

        b.style.color =
            color;

        b.style.left =
            (
                2 +
                Math.random() * 96
            ) + "%";

        b.style.animationDuration =
            (
                4 +
                Math.random() * 3
            ) + "s";

        b.style.animationDelay =
            (
                Math.random() * 1.4
            ) + "s";

        b.style.transform =
            "rotate(" +
            (
                Math.random()*20-10
            ) +
            "deg)";

        container.appendChild(b);

    }

}


/* =========================================================
   FINISH
========================================================= */

function finish(){

    if(ended){
        return;
    }

    ended = true;
    started = false;

    let title = "";
    let sub = "";

    if(
        p1.hp <= 0 &&
        p2.hp <= 0
    ){

        title =
            "⚖️ HÒA!";

        sub =
            "Cả hai chiến binh đã cùng gục ngã!";

    }
    else if(p2.hp <= 0){

        title =
            "🎉 CHÚC MỪNG " +
            p1.name +
            "!";

        sub =
            "🏆 BẠN ĐÃ CHIẾN THẮNG!";

        showVictoryBalloons();

    }
    else if(p1.hp <= 0){

        title =
            "💔 RẤT TIẾC " +
            p1.name +
            "!";

        sub =
            "😭 CHIA BUỒN, BẠN ĐÃ THUA!";

    }
    else{

        if(p1.hp > p2.hp){

            title =
                "🏆 " +
                p1.name +
                " THẮNG!";

            sub =
                "Hết giờ — P1 còn nhiều HP hơn.";

            showVictoryBalloons();

        }
        else if(p2.hp > p1.hp){

            title =
                "🏆 " +
                p2.name +
                " THẮNG!";

            sub =
                "Hết giờ — P2 còn nhiều HP hơn.";

            if(selectedMode === "cpu"){
                /* CPU thắng — không có bóng bay */
            }

        }
        else{

            title =
                "⚖️ HÒA!";

            sub =
                "Hai chiến binh có cùng lượng HP.";

        }

    }

    document
        .getElementById("resultTitle")
        .innerHTML =
        title;

    document
        .getElementById("resultSub")
        .innerHTML =
        sub;

    document
        .getElementById("result")
        .style.display =
        "flex";

    document
        .getElementById("hud")
        .style.display =
        "none";

    document
        .getElementById("gameHelp")
        .style.display =
        "none";

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

    gameTime -= dt;

    if(gameTime <= 0){

        gameTime = 0;

        updateHUD();

        finish();

        return;

    }

    for(const fighter of fighters){

        fighter.cooldowns(dt);

        fighter.controls();

        fighter.cpuAI();

        fighter.physics(dt);

    }

    /* energy auto regen */

    if(
        p1 &&
        p1.alive()
    ){

        p1.energy =
            Math.min(
                100,
                p1.energy +
                ENERGY_REGEN * dt
            );

    }

    if(
        p2 &&
        p2.alive()
    ){

        p2.energy =
            Math.min(
                100,
                p2.energy +
                ENERGY_REGEN * dt
            );

    }

    updateProjectiles(dt);

    updateParticles(dt);

    if(
        !p1.alive() ||
        !p2.alive()
    ){

        finish();

        return;

    }

    updateHUD();

}


/* =========================================================
   DRAW
========================================================= */

function draw(){

    drawBackground();

    if(p1){
        p1.draw();
    }

    if(p2){
        p2.draw();
    }

    /* projectiles */

    for(const p of projectiles){

        const color =
            p.team === 1
            ? "#47c8ff"
            : "#df6cff";

        const glow =
            ctx.createRadialGradient(
                p.x,
                p.y,
                2,
                p.x,
                p.y,
                28
            );

        glow.addColorStop(
            0,
            "#ffffff"
        );

        glow.addColorStop(
            .25,
            color
        );

        glow.addColorStop(
            1,
            color + "00"
        );

        ctx.fillStyle =
            glow;

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            28,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.fillStyle =
            color;

        ctx.beginPath();

        ctx.arc(
            p.x,
            p.y,
            p.radius,
            0,
            Math.PI*2
        );

        ctx.fill();

    }

    drawParticles();

}


/* =========================================================
   LOOP
========================================================= */

function loop(now){

    let dt =
        Math.min(
            0.033,
            (now - lastTime) / 1000
        );

    lastTime = now;

    update(dt);

    draw();

    requestAnimationFrame(loop);

}

requestAnimationFrame(loop);

</script>

</body>
</html>
"""

components.html(
    HTML,
    height=850,
    scrolling=False
)
