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
    margin:0;
    padding:0;
}

html,body{
    width:100%;
    height:100%;
    overflow:hidden;
    background:#050711;
    font-family:Arial,Helvetica,sans-serif;
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
    background:#050711;
    border:1px solid rgba(120,160,255,.25);
    border-radius:20px;
    box-shadow:
        0 0 35px rgba(70,110,255,.18),
        inset 0 0 50px rgba(0,0,0,.45);
}

canvas{
    position:absolute;
    inset:0;
    width:100%;
    height:100%;
    display:block;
}

.hidden{
    display:none !important;
}

/* ================= HOME ================= */

#home{
    position:absolute;
    inset:0;
    z-index:20;
    display:flex;
    flex-direction:column;
    align-items:center;
    padding:28px 25px;
    overflow-y:auto;
    background:
        radial-gradient(circle at 50% 18%,rgba(75,115,255,.17),transparent 32%),
        linear-gradient(180deg,rgba(5,7,18,.93),rgba(6,8,21,.98));
}

.logo{
    font-size:52px;
    font-weight:1000;
    letter-spacing:8px;
    color:white;
    text-align:center;
    text-shadow:
        0 0 8px #72c8ff,
        0 0 25px #477bff,
        0 0 55px rgba(70,100,255,.7);
}

.subtitle{
    margin-top:3px;
    color:#a9b9e9;
    font-size:12px;
    letter-spacing:4px;
    font-weight:800;
}

.homeGrid{
    width:min(1050px,100%);
    display:grid;
    grid-template-columns:1fr 1.35fr;
    gap:18px;
    margin-top:22px;
}

.panel{
    background:
        linear-gradient(145deg,rgba(20,27,58,.88),rgba(7,10,27,.93));
    border:1px solid rgba(130,160,255,.25);
    border-radius:18px;
    padding:18px;
    box-shadow:
        0 10px 30px rgba(0,0,0,.3),
        inset 0 0 30px rgba(70,100,200,.05);
}

.panelTitle{
    color:#eaf0ff;
    font-size:15px;
    font-weight:1000;
    letter-spacing:2px;
    margin-bottom:13px;
}

.inputLabel{
    color:#8998c8;
    font-size:11px;
    font-weight:800;
    margin-bottom:5px;
}

input{
    width:100%;
    border:none;
    outline:none;
    border-radius:10px;
    padding:11px 13px;
    color:white;
    background:#0b1027;
    border:1px solid rgba(120,150,255,.22);
    font-weight:800;
}

input:focus{
    border-color:#62bfff;
    box-shadow:0 0 15px rgba(80,170,255,.18);
}

.modeRow{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;
}

.modeBtn{
    border:1px solid rgba(130,160,255,.25);
    background:#0a0f26;
    color:#aebce9;
    border-radius:12px;
    padding:13px 8px;
    cursor:pointer;
    font-weight:1000;
    transition:.2s;
}

.modeBtn:hover{
    transform:translateY(-2px);
    border-color:#6bc5ff;
}

.modeBtn.active{
    color:white;
    background:linear-gradient(135deg,#153b76,#251a68);
    border-color:#62c7ff;
    box-shadow:0 0 20px rgba(80,180,255,.2);
}

#p2Box{
    margin-top:13px;
}

.charGrid{
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:9px;
}

.charBtn{
    position:relative;
    min-height:105px;
    border-radius:13px;
    padding:10px 7px;
    cursor:pointer;
    color:white;
    border:1px solid rgba(130,160,255,.18);
    background:linear-gradient(145deg,#10152e,#090c1d);
    overflow:hidden;
    transition:.2s;
}

.charBtn:hover{
    transform:translateY(-3px);
    border-color:rgba(150,200,255,.7);
}

.charBtn.selected{
    border-color:white;
    box-shadow:0 0 20px var(--glow);
    transform:translateY(-2px);
}

.charOrb{
    width:32px;
    height:32px;
    margin:0 auto 5px;
    border-radius:50%;
    background:var(--c);
    box-shadow:0 0 16px var(--c);
}

.charName{
    font-size:12px;
    font-weight:1000;
}

.charType{
    margin-top:2px;
    font-size:9px;
    color:#9caad2;
    font-weight:800;
}

.startBtn{
    width:min(520px,100%);
    margin-top:18px;
    border:0;
    border-radius:15px;
    padding:15px;
    cursor:pointer;
    color:white;
    font-size:16px;
    font-weight:1000;
    letter-spacing:2px;
    background:linear-gradient(90deg,#1479ff,#734cff,#c94cff);
    box-shadow:
        0 0 20px rgba(100,100,255,.35),
        0 8px 25px rgba(0,0,0,.3);
    transition:.2s;
}

.startBtn:hover{
    transform:translateY(-2px) scale(1.01);
}

.controls{
    width:min(1050px,100%);
    margin-top:13px;
    color:#7f8db7;
    text-align:center;
    font-size:10px;
    line-height:1.7;
}

.key{
    color:#dce8ff;
    background:#111832;
    padding:3px 6px;
    border-radius:5px;
    border:1px solid rgba(150,180,255,.15);
}

/* ================= SOUND ================= */

.soundBtn{
    position:absolute;
    top:14px;
    left:50%;
    transform:translateX(-50%);
    z-index:40;
    border:1px solid rgba(150,200,255,.35);
    background:rgba(9,14,35,.85);
    color:white;
    border-radius:12px;
    padding:8px 13px;
    cursor:pointer;
    font-weight:900;
    font-size:13px;
    box-shadow:0 0 15px rgba(80,150,255,.15);
    pointer-events:auto;
}

.soundBtn:hover{
    background:#172044;
}

/* ================= HUD ================= */

#hud{
    position:absolute;
    top:13px;
    left:15px;
    right:15px;
    z-index:10;
    display:flex;
    justify-content:space-between;
    align-items:flex-start;
    pointer-events:none;
}

.hudSide{
    width:37%;
}

.hudSide.right{
    text-align:right;
}

.hudName{
    color:white;
    font-weight:1000;
    font-size:14px;
    text-shadow:0 2px 5px black;
}

.hudHp{
    height:15px;
    margin-top:5px;
    border-radius:20px;
    overflow:hidden;
    background:#080b15;
    border:1px solid rgba(255,255,255,.15);
}

.hpFill{
    height:100%;
    width:100%;
    background:linear-gradient(90deg,#34e88b,#b9ff64);
    box-shadow:0 0 13px #4aff91;
    transition:.15s;
}

.right .hpFill{
    float:right;
    background:linear-gradient(90deg,#ff6b9a,#ff365f);
    box-shadow:0 0 13px #ff4c77;
}

.energy{
    height:6px;
    margin-top:4px;
    border-radius:10px;
    overflow:hidden;
    background:#080b15;
}

.energyFill{
    height:100%;
    width:0%;
    background:linear-gradient(90deg,#39b9ff,#9c70ff);
    box-shadow:0 0 10px #6b9dff;
    transition:.12s;
}

.right .energyFill{
    float:right;
}

.timer{
    min-width:90px;
    text-align:center;
    color:white;
    font-size:25px;
    font-weight:1000;
    text-shadow:0 0 12px #7bb9ff;
}

.timer small{
    display:block;
    color:#7583ae;
    font-size:8px;
    letter-spacing:2px;
}

#countdown{
    position:absolute;
    inset:0;
    z-index:15;
    display:flex;
    justify-content:center;
    align-items:center;
    pointer-events:none;
    font-size:105px;
    color:white;
    font-weight:1000;
    text-shadow:
        0 0 12px #fff,
        0 0 35px #5c9dff,
        0 0 70px #8c4cff;
}

#result{
    position:absolute;
    inset:0;
    z-index:30;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    background:rgba(3,5,15,.68);
    backdrop-filter:blur(5px);
}

.resultTitle{
    color:white;
    font-size:52px;
    font-weight:1000;
    letter-spacing:4px;
    text-align:center;
    text-shadow:0 0 25px #7e9dff;
}

.resultSub{
    color:#b6c4e9;
    margin-top:8px;
    font-size:15px;
    font-weight:800;
    text-align:center;
}

.backBtn{
    margin-top:22px;
    border:1px solid rgba(150,190,255,.4);
    background:#111833;
    color:white;
    border-radius:12px;
    padding:12px 24px;
    cursor:pointer;
    font-weight:1000;
}

/* ================= BALLOONS ================= */

#balloons{
    position:absolute;
    inset:0;
    z-index:29;
    pointer-events:none;
    overflow:hidden;
}

.balloon{
    position:absolute;
    bottom:-90px;
    width:24px;
    height:31px;
    border-radius:50% 50% 48% 48%;
    animation:rise 4.5s linear forwards;
    filter:drop-shadow(0 0 8px currentColor);
}

.balloon:after{
    content:"";
    position:absolute;
    width:1px;
    height:65px;
    top:29px;
    left:50%;
    background:rgba(255,255,255,.4);
}

@keyframes rise{
    0%{
        transform:translateY(0) rotate(-4deg);
        opacity:0;
    }
    10%{opacity:1;}
    50%{
        transform:translateY(-430px) translateX(30px) rotate(7deg);
    }
    100%{
        transform:translateY(-900px) translateX(-50px) rotate(-8deg);
        opacity:0;
    }
}

#help{
    position:absolute;
    bottom:12px;
    left:50%;
    transform:translateX(-50%);
    z-index:10;
    color:#68769e;
    font-size:9px;
    white-space:nowrap;
    pointer-events:none;
}

@media(max-width:900px){
    #gameWrap{
        height:100vh;
        border-radius:0;
    }

    .homeGrid{
        grid-template-columns:1fr;
    }

    .logo{
        font-size:38px;
    }
}

@media(max-width:600px){
    .charGrid{
        grid-template-columns:repeat(2,1fr);
    }

    #home{
        padding:18px 12px;
    }

    .resultTitle{
        font-size:35px;
    }
}
</style>
</head>

<body>

<div id="gameWrap">

<canvas id="gameCanvas"></canvas>

<div id="home">

    <div class="logo">AURA WAR</div>
    <div class="subtitle">ANIME SWORD ARENA</div>

    <div class="homeGrid">

        <div class="panel">

            <div class="panelTitle">⚔️ TRẬN ĐẤU</div>

            <div class="inputLabel">TÊN NGƯỜI CHƠI 1</div>
            <input id="p1Name" maxlength="20" value="Player 1">

            <div style="height:13px"></div>

            <div class="inputLabel">CHẾ ĐỘ</div>

            <div class="modeRow">
                <button class="modeBtn active" id="mode1v1">⚔️ 1V1</button>
                <button class="modeBtn" id="modeCPU">🤖 VS MÁY</button>
            </div>

            <div id="p2Box">
                <div class="inputLabel">TÊN NGƯỜI CHƠI 2</div>
                <input id="p2Name" maxlength="20" value="Player 2">
            </div>

            <div style="height:15px"></div>

            <div class="panelTitle">🎮 ĐIỀU KHIỂN</div>

            <div style="font-size:10px;color:#8290b8;line-height:2">
                P1:
                <span class="key">A</span><span class="key">D</span> di chuyển
                <span class="key">W</span> nhảy
                <span class="key">S</span> rơi nhanh
                <br>
                <span class="key">J</span> đánh
                <span class="key">K</span> skill
                <span class="key">L</span> dash
                <span class="key">U</span> heavy
                <span class="key">I</span> ultimate
                <br><br>
                P2:
                <span class="key">←</span><span class="key">→</span> di chuyển
                <span class="key">↑</span> nhảy
                <span class="key">↓</span> rơi
                <br>
                <span class="key">1</span> đánh
                <span class="key">2</span> skill
                <span class="key">3</span> dash
                <span class="key">4</span> heavy
                <span class="key">5</span> ultimate
            </div>

        </div>

        <div class="panel">

            <div class="panelTitle">👤 CHỌN NHÂN VẬT</div>

            <div class="charGrid">

                <button class="charBtn selected"
                    data-id="water"
                    style="--c:#31bfff;--glow:rgba(40,190,255,.6)">
                    <div class="charOrb"></div>
                    <div class="charName">KAIRO</div>
                    <div class="charType">🌊 THỦY</div>
                </button>

                <button class="charBtn"
                    data-id="fire"
                    style="--c:#ff5a36;--glow:rgba(255,80,40,.6)">
                    <div class="charOrb"></div>
                    <div class="charName">RENJI</div>
                    <div class="charType">🔥 VIÊM</div>
                </button>

                <button class="charBtn"
                    data-id="thunder"
                    style="--c:#ffe44a;--glow:rgba(255,220,50,.6)">
                    <div class="charOrb"></div>
                    <div class="charName">RAI</div>
                    <div class="charType">⚡ LÔI</div>
                </button>

                <button class="charBtn"
                    data-id="flower"
                    style="--c:#ff79c8;--glow:rgba(255,100,200,.6)">
                    <div class="charOrb"></div>
                    <div class="charName">MIZUHA</div>
                    <div class="charType">🌸 HOA</div>
                </button>

                <button class="charBtn"
                    data-id="rock"
                    style="--c:#b8a98e;--glow:rgba(180,160,120,.55)">
                    <div class="charOrb"></div>
                    <div class="charName">GARO</div>
                    <div class="charType">🪨 ĐÁ</div>
                </button>

                <button class="charBtn"
                    data-id="wind"
                    style="--c:#72f3d0;--glow:rgba(70,255,210,.75)">
                    <div class="charOrb"></div>
                    <div class="charName">KAZE</div>
                    <div class="charType">🌪️ GIÓ</div>
                </button>

            </div>

            <div style="
                margin-top:13px;
                padding:11px;
                border-radius:10px;
                background:rgba(60,100,180,.07);
                border:1px solid rgba(100,140,230,.12);
                color:#8e9dc8;
                font-size:10px;
                line-height:1.6;
            ">
                Mỗi nhân vật có bộ kỹ năng, aura và hiệu ứng riêng.
                <br>
                🌪️ <b style="color:#72f3d0">KAZE</b> sở hữu bộ hiệu ứng Gió đặc biệt.
            </div>

        </div>

    </div>

    <button class="startBtn" id="startBtn">
        ▶ BẮT ĐẦU TRẬN
    </button>

    <div class="controls">
        60 GIÂY • HP 100 • NĂNG LƯỢNG TỰ HỒI • DASH XA + AFTERIMAGE • 🔊 SOUND
    </div>

</div>

<div id="hud" class="hidden">

    <div class="hudSide">
        <div class="hudName" id="name1">PLAYER 1</div>
        <div class="hudHp">
            <div class="hpFill" id="hp1"></div>
        </div>
        <div class="energy">
            <div class="energyFill" id="energy1"></div>
        </div>
    </div>

    <div class="timer">
        <small>TIME</small>
        <span id="timer">60</span>
    </div>

    <div class="hudSide right">
        <div class="hudName" id="name2">PLAYER 2</div>
        <div class="hudHp">
            <div class="hpFill" id="hp2"></div>
        </div>
        <div class="energy">
            <div class="energyFill" id="energy2"></div>
        </div>
    </div>

</div>

<button id="soundBtn" class="soundBtn">🔊 ÂM THANH</button>

<div id="countdown" class="hidden"></div>

<div id="help" class="hidden">
    P1: A/D W S J K L U I &nbsp; • &nbsp;
    P2: ← → ↑ ↓ 1 2 3 4 5
</div>

<div id="balloons"></div>

<div id="result" class="hidden">
    <div class="resultTitle" id="resultTitle">VICTORY</div>
    <div class="resultSub" id="resultSub"></div>
    <button class="backBtn" id="backBtn">↩ VỀ MENU</button>
</div>

<script>

/* =========================================================
   AURA WAR
   ========================================================= */

const canvas=document.getElementById("gameCanvas");
const ctx=canvas.getContext("2d");

let W=1250;
let H=850;
let dpr=Math.min(window.devicePixelRatio||1,2);

function resizeCanvas(){
    const rect=canvas.getBoundingClientRect();

    W=rect.width;
    H=rect.height;

    canvas.width=Math.floor(W*dpr);
    canvas.height=Math.floor(H*dpr);

    ctx.setTransform(dpr,0,0,dpr,0,0);
}

window.addEventListener("resize",resizeCanvas);
resizeCanvas();

/* =========================================================
   ELEMENTS
   ========================================================= */

const home=document.getElementById("home");
const hud=document.getElementById("hud");
const countdownEl=document.getElementById("countdown");
const result=document.getElementById("result");
const resultTitle=document.getElementById("resultTitle");
const resultSub=document.getElementById("resultSub");
const balloons=document.getElementById("balloons");
const help=document.getElementById("help");
const soundBtn=document.getElementById("soundBtn");

const mode1v1=document.getElementById("mode1v1");
const modeCPU=document.getElementById("modeCPU");
const p2Box=document.getElementById("p2Box");

const name1El=document.getElementById("name1");
const name2El=document.getElementById("name2");
const hp1El=document.getElementById("hp1");
const hp2El=document.getElementById("hp2");
const energy1El=document.getElementById("energy1");
const energy2El=document.getElementById("energy2");
const timerEl=document.getElementById("timer");

let gameMode="1v1";
let selectedP1="water";
let selectedP2="fire";

/* =========================================================
   AUDIO SYSTEM
   ========================================================= */

let audioCtx=null;
let masterGain=null;
let soundEnabled=true;

function initAudio(){

    try{

        if(!audioCtx){

            audioCtx=new(
                window.AudioContext||
                window.webkitAudioContext
            )();

            masterGain=audioCtx.createGain();

            masterGain.gain.value=.24;

            masterGain.connect(audioCtx.destination);
        }

        if(audioCtx.state==="suspended"){
            audioCtx.resume();
        }

    }catch(err){
        soundEnabled=false;
    }
}

function tone(
    freq,
    duration,
    type="sine",
    gain=.08,
    endFreq=null
){

    if(!soundEnabled) return;

    initAudio();

    if(!audioCtx || !masterGain) return;

    const osc=audioCtx.createOscillator();
    const g=audioCtx.createGain();

    osc.type=type;

    osc.frequency.setValueAtTime(
        freq,
        audioCtx.currentTime
    );

    if(endFreq!==null){

        osc.frequency.exponentialRampToValueAtTime(
            Math.max(30,endFreq),
            audioCtx.currentTime+duration
        );
    }

    g.gain.setValueAtTime(
        .0001,
        audioCtx.currentTime
    );

    g.gain.exponentialRampToValueAtTime(
        gain,
        audioCtx.currentTime+.015
    );

    g.gain.exponentialRampToValueAtTime(
        .0001,
        audioCtx.currentTime+duration
    );

    osc.connect(g);
    g.connect(masterGain);

    osc.start();

    osc.stop(
        audioCtx.currentTime+
        duration+
        .03
    );
}

function noise(
    duration=.12,
    gain=.08,
    filterFreq=1800
){

    if(!soundEnabled) return;

    initAudio();

    if(!audioCtx || !masterGain) return;

    const length=Math.max(
        1,
        Math.floor(audioCtx.sampleRate*duration)
    );

    const buffer=audioCtx.createBuffer(
        1,
        length,
        audioCtx.sampleRate
    );

    const data=buffer.getChannelData(0);

    for(let i=0;i<data.length;i++){
        data[i]=Math.random()*2-1;
    }

    const source=audioCtx.createBufferSource();
    const filter=audioCtx.createBiquadFilter();
    const g=audioCtx.createGain();

    filter.type="bandpass";
    filter.frequency.value=filterFreq;
    filter.Q.value=.7;

    g.gain.setValueAtTime(
        gain,
        audioCtx.currentTime
    );

    g.gain.exponentialRampToValueAtTime(
        .0001,
        audioCtx.currentTime+duration
    );

    source.buffer=buffer;

    source.connect(filter);
    filter.connect(g);
    g.connect(masterGain);

    source.start();
}

function sfxSlash(){

    tone(480,.08,"sawtooth",.055,950);
    noise(.055,.035,2800);
}

function sfxHeavy(){

    tone(120,.18,"square",.10,55);
    noise(.18,.12,700);
    tone(260,.12,"triangle",.05,80);
}

function sfxHit(){

    noise(.10,.09,950);
    tone(95,.10,"square",.055,45);
}

function sfxDash(style="normal"){

    if(style==="wind"){

        noise(.32,.075,3200);
        tone(500,.28,"sine",.035,1100);

    }else{

        noise(.18,.055,2400);
        tone(240,.16,"sawtooth",.035,800);
    }
}

function sfxSkill(style){

    if(style==="water"){

        tone(330,.35,"sine",.06,720);
        tone(520,.30,"sine",.045,980);
        noise(.16,.025,1800);

    }else if(style==="fire"){

        noise(.30,.09,900);
        tone(180,.25,"sawtooth",.055,70);
        tone(480,.18,"triangle",.04,120);

    }else if(style==="thunder"){

        tone(900,.12,"square",.07,180);
        tone(1450,.08,"square",.055,400);
        noise(.13,.07,4200);

    }else if(style==="flower"){

        tone(520,.35,"sine",.05,900);
        tone(780,.42,"sine",.04,1250);

    }else if(style==="rock"){

        tone(90,.32,"square",.09,45);
        noise(.28,.10,500);

    }else if(style==="wind"){

        noise(.55,.075,3800);
        tone(420,.48,"sine",.045,1200);
        tone(720,.35,"triangle",.025,1450);

    }else{

        tone(400,.25,"sine",.05,800);
    }
}

function sfxUltimate(style){

    tone(180,.30,"sine",.06,420);
    tone(360,.40,"sine",.055,900);

    setTimeout(function(){

        if(!soundEnabled) return;

        noise(.45,.16,1100);
        tone(75,.45,"square",.12,35);
        tone(600,.32,"sawtooth",.065,100);

        if(style==="wind"){

            noise(.65,.10,4500);
            tone(900,.60,"sine",.05,1600);

        }else if(style==="thunder"){

            tone(1100,.22,"square",.09,120);
            noise(.35,.10,5000);

        }else if(style==="fire"){

            noise(.55,.14,800);
            tone(180,.40,"sawtooth",.08,45);

        }else if(style==="water"){

            tone(300,.55,"sine",.07,950);
            noise(.35,.05,1800);

        }else if(style==="rock"){

            tone(65,.60,"square",.14,30);
            noise(.55,.13,450);

        }else if(style==="flower"){

            tone(600,.55,"sine",.06,1300);
            tone(900,.50,"sine",.04,1600);
        }

    },260);
}

function sfxJump(){
    tone(280,.10,"sine",.035,620);
}

function sfxCountdown(n){

    if(n===1){

        tone(880,.18,"square",.07,620);

    }else{

        tone(440,.18,"square",.065,320);
    }
}

function sfxFight(){

    tone(420,.16,"sawtooth",.08,900);
    tone(900,.35,"sine",.07,1500);
    noise(.12,.04,3000);
}

function sfxVictory(){

    tone(523,.18,"sine",.07,660);

    setTimeout(function(){
        tone(659,.18,"sine",.07,830);
    },140);

    setTimeout(function(){
        tone(784,.35,"sine",.09,1100);
    },280);
}

function sfxDefeat(){

    tone(320,.25,"sine",.06,220);

    setTimeout(function(){
        tone(220,.40,"sine",.065,100);
    },180);
}

function sfxDraw(){

    tone(430,.18,"triangle",.05,360);

    setTimeout(function(){
        tone(360,.28,"triangle",.05,300);
    },160);
}

function toggleSound(){

    soundEnabled=!soundEnabled;

    if(masterGain){

        masterGain.gain.value=
            soundEnabled?.24:0;
    }

    soundBtn.textContent=
        soundEnabled
        ?"🔊 ÂM THANH"
        :"🔇 TẮT ÂM THANH";

    if(soundEnabled){
        initAudio();
    }
}

soundBtn.onclick=toggleSound;

/* =========================================================
   CHARACTER DATA
   ========================================================= */

const CHARACTERS={

    water:{
        name:"KAIRO",
        element:"THỦY",
        color:"#36c8ff",
        dark:"#1268a4",
        light:"#a7edff",
        accent:"#227aff",
        skillName:"THỦY LONG",
        ultimateName:"HẢI LONG DIỆT",
        projectile:"water",
        style:"water"
    },

    fire:{
        name:"RENJI",
        element:"VIÊM",
        color:"#ff5638",
        dark:"#a92319",
        light:"#ffd09a",
        accent:"#ff9d24",
        skillName:"HỎA LƯU",
        ultimateName:"VIÊM LONG PHÁ",
        projectile:"fire",
        style:"fire"
    },

    thunder:{
        name:"RAI",
        element:"LÔI",
        color:"#ffe84b",
        dark:"#ad8610",
        light:"#fff9bd",
        accent:"#fff06a",
        skillName:"LÔI KÍCH",
        ultimateName:"THIÊN LÔI",
        projectile:"thunder",
        style:"thunder"
    },

    flower:{
        name:"MIZUHA",
        element:"HOA",
        color:"#ff7ccf",
        dark:"#a82e78",
        light:"#ffd8f0",
        accent:"#ffb0e3",
        skillName:"HOA VŨ",
        ultimateName:"BÁCH HOA LOẠN VŨ",
        projectile:"flower",
        style:"flower"
    },

    rock:{
        name:"GARO",
        element:"ĐÁ",
        color:"#b8a98e",
        dark:"#635848",
        light:"#e2d7bd",
        accent:"#8e8068",
        skillName:"NHAM KÍCH",
        ultimateName:"ĐẠI ĐỊA CHẤN",
        projectile:"rock",
        style:"rock"
    },

    wind:{
        name:"KAZE",
        element:"GIÓ",
        color:"#6ff5d0",
        dark:"#218c78",
        light:"#d5fff4",
        accent:"#9bffe9",
        skillName:"CUỒNG PHONG",
        ultimateName:"THIÊN PHONG LOẠN VŨ",
        projectile:"wind",
        style:"wind"
    }
};

/* =========================================================
   MODE
   ========================================================= */

mode1v1.onclick=function(){

    gameMode="1v1";

    mode1v1.classList.add("active");
    modeCPU.classList.remove("active");

    p2Box.style.display="block";
};

modeCPU.onclick=function(){

    gameMode="cpu";

    modeCPU.classList.add("active");
    mode1v1.classList.remove("active");

    p2Box.style.display="none";
};

/* =========================================================
   CHARACTER SELECT
   ========================================================= */

document.querySelectorAll(".charBtn").forEach(function(btn){

    btn.onclick=function(){

        if(gameStarted) return;

        const id=btn.dataset.id;

        selectedP1=id;

        document.querySelectorAll(".charBtn").forEach(function(x){
            x.classList.remove("selected");
        });

        btn.classList.add("selected");
    };

    btn.addEventListener("dblclick",function(){

        if(gameStarted) return;

        if(gameMode!=="1v1") return;

        const id=btn.dataset.id;

        selectedP2=id;

        document.querySelectorAll(".charBtn").forEach(function(x){
            x.style.outline="";
        });

        btn.style.outline="2px solid #ff75df";
    });
});

/* =========================================================
   INPUT
   ========================================================= */

const keys={};

window.addEventListener("keydown",function(e){

    const key=e.key.toLowerCase();

    keys[key]=true;

    if([
        "arrowleft",
        "arrowright",
        "arrowup",
        "arrowdown",
        " "
    ].includes(key)){
        e.preventDefault();
    }
});

window.addEventListener("keyup",function(e){

    keys[e.key.toLowerCase()]=false;
});

/* =========================================================
   UTIL
   ========================================================= */

function clamp(v,a,b){
    return Math.max(a,Math.min(b,v));
}

function rand(a,b){
    return Math.random()*(b-a)+a;
}

/* =========================================================
   EFFECTS
   ========================================================= */

const particles=[];
const projectiles=[];
const slashes=[];
const shockwaves=[];
const afterimages=[];
const windBlades=[];
const flowerPetals=[];

function particle(x,y,color,count=10,speed=120){

    for(let i=0;i<count;i++){

        const a=Math.random()*Math.PI*2;
        const s=Math.random()*speed;

        particles.push({
            x:x,
            y:y,
            vx:Math.cos(a)*s,
            vy:Math.sin(a)*s,
            life:.45+Math.random()*.55,
            max:1,
            size:2+Math.random()*4,
            color:color
        });
    }
}

function ring(x,y,color,size=30){

    shockwaves.push({
        x:x,
        y:y,
        r:5,
        max:size,
        life:.45,
        color:color
    });
}

function makeAfterimage(f){

    afterimages.push({
        x:f.x,
        y:f.y,
        facing:f.facing,
        color:f.data.color,
        life:.3,
        max:.3,
        style:f.data.style
    });
}

/* =========================================================
   FIGHTER
   ========================================================= */

class Fighter{

    constructor(x,side,id){

        this.x=x;
        this.y=0;

        this.vx=0;
        this.vy=0;

        this.side=side;
        this.id=id;
        this.data=CHARACTERS[id];

        this.hp=100;
        this.energy=0;

        this.width=58;
        this.height=112;

        this.facing=side===1?1:-1;

        this.grounded=true;

        this.attackTimer=0;
        this.attackCooldown=0;

        this.skillCooldown=0;
        this.dashCooldown=0;
        this.heavyCooldown=0;
        this.ultimateCooldown=0;

        this.dashTimer=0;
        this.dashInvincible=0;

        this.hitFlash=0;
        this.hitStun=0;

        this.state="idle";
        this.anim=0;

        this.combo=0;
        this.comboTimer=0;

        this.dead=false;

        this.cpuThink=0;
        this.cpuMove=0;
        this.cpuJump=false;

        this.lastAttackSound=0;
    }

    get floorY(){
        return H-150;
    }

    get bodyY(){
        return this.floorY-15;
    }

    update(dt,opponent){

        if(this.dead) return;

        this.anim+=dt;

        this.attackCooldown=Math.max(
            0,
            this.attackCooldown-dt
        );

        this.skillCooldown=Math.max(
            0,
            this.skillCooldown-dt
        );

        this.dashCooldown=Math.max(
            0,
            this.dashCooldown-dt
        );

        this.heavyCooldown=Math.max(
            0,
            this.heavyCooldown-dt
        );

        this.ultimateCooldown=Math.max(
            0,
            this.ultimateCooldown-dt
        );

        this.dashInvincible=Math.max(
            0,
            this.dashInvincible-dt
        );

        this.hitFlash=Math.max(
            0,
            this.hitFlash-dt
        );

        this.hitStun=Math.max(
            0,
            this.hitStun-dt
        );

        this.comboTimer=Math.max(
            0,
            this.comboTimer-dt
        );

        if(this.comboTimer<=0){
            this.combo=0;
        }

        this.energy=clamp(
            this.energy+8*dt,
            0,
            100
        );

        if(this.hitStun>0){

            this.vx*=.92;

            this.vy+=1450*dt;
            this.y+=this.vy*dt;

            if(this.y>=0){

                this.y=0;
                this.vy=0;
                this.grounded=true;
            }

            return;
        }

        if(this.dashTimer>0){

            this.dashTimer-=dt;

            this.x+=this.vx*dt;

            if(Math.random()<.8){
                makeAfterimage(this);
            }

            this.y=0;

        }else{

            this.control(dt,opponent);

            this.vy+=1450*dt;
            this.y+=this.vy*dt;

            if(this.y>=0){

                this.y=0;
                this.vy=0;
                this.grounded=true;

            }else{

                this.grounded=false;
            }

            this.x+=this.vx*dt;

            if(this.grounded){

                this.vx*=Math.pow(.0008,dt);

            }else{

                this.vx*=Math.pow(.08,dt);
            }
        }

        this.x=clamp(
            this.x,
            65,
            W-65
        );

        if(this.attackTimer>0){
            this.attackTimer-=dt;
        }

        if(this.x>opponent.x+4){
            this.facing=-1;
        }

        if(this.x<opponent.x-4){
            this.facing=1;
        }
    }

    control(dt,opponent){

        if(this.side===1){

            let move=0;

            if(keys["a"]) move-=1;
            if(keys["d"]) move+=1;

            if(move!==0){

                this.vx+=move*1500*dt;
                this.vx=clamp(this.vx,-285,285);
                this.state="run";

            }else{

                this.state=
                    this.grounded
                    ?"idle"
                    :"jump";
            }

            if(keys["w"]&&this.grounded){

                this.vy=-580;
                this.grounded=false;

                particle(
                    this.x,
                    this.bodyY+50,
                    this.data.color,
                    10,
                    80
                );

                sfxJump();
            }

            if(keys["s"]&&!this.grounded){
                this.vy+=1100*dt;
            }

            if(keys["j"]){
                this.normalAttack();
                keys["j"]=false;
            }

            if(keys["k"]){
                this.skill();
                keys["k"]=false;
            }

            if(keys["l"]){
                this.dash();
                keys["l"]=false;
            }

            if(keys["u"]){
                this.heavy();
                keys["u"]=false;
            }

            if(keys["i"]){
                this.ultimate(opponent);
                keys["i"]=false;
            }

        }else{

            if(gameMode==="cpu"){

                this.cpuControl(dt,opponent);

            }else{

                let move=0;

                if(keys["arrowleft"]) move-=1;
                if(keys["arrowright"]) move+=1;

                if(move!==0){

                    this.vx+=move*1500*dt;
                    this.vx=clamp(this.vx,-285,285);
                    this.state="run";

                }else{

                    this.state=
                        this.grounded
                        ?"idle"
                        :"jump";
                }

                if(keys["arrowup"]&&this.grounded){

                    this.vy=-580;
                    this.grounded=false;

                    particle(
                        this.x,
                        this.bodyY+50,
                        this.data.color,
                        10,
                        80
                    );

                    sfxJump();
                }

                if(keys["arrowdown"]&&!this.grounded){
                    this.vy+=1100*dt;
                }

                if(keys["1"]){
                    this.normalAttack();
                    keys["1"]=false;
                }

                if(keys["2"]){
                    this.skill();
                    keys["2"]=false;
                }

                if(keys["3"]){
                    this.dash();
                    keys["3"]=false;
                }

                if(keys["4"]){
                    this.heavy();
                    keys["4"]=false;
                }

                if(keys["5"]){
                    this.ultimate(opponent);
                    keys["5"]=false;
                }
            }
        }
    }

    cpuControl(dt,opponent){

        this.cpuThink-=dt;

        const d=opponent.x-this.x;
        const ad=Math.abs(d);

        if(this.cpuThink<=0){

            this.cpuThink=rand(.07,.16);

            if(ad>330){

                this.cpuMove=Math.sign(d);

            }else if(ad<120){

                this.cpuMove=
                    Math.random()<.55
                    ?-Math.sign(d)
                    :0;

            }else{

                this.cpuMove=
                    Math.random()<.65
                    ?Math.sign(d)
                    :0;
            }

            this.cpuJump=Math.random()<.12;
        }

        if(this.cpuMove!==0){

            this.vx+=this.cpuMove*1250*dt;
            this.vx=clamp(this.vx,-280,280);
            this.state="run";

        }else{

            this.state=
                this.grounded
                ?"idle"
                :"jump";
        }

        if(this.cpuJump&&this.grounded){

            this.vy=-570;
            this.grounded=false;
            this.cpuJump=false;
        }

        if(ad<125&&Math.random()<.055){
            this.normalAttack();
        }

        if(ad<230&&this.energy>=25&&Math.random()<.025){
            this.skill();
        }

        if(
            ad>160&&
            ad<390&&
            this.dashCooldown<=0&&
            Math.random()<.02
        ){
            this.dash();
        }

        if(
            ad<150&&
            this.heavyCooldown<=0&&
            Math.random()<.025
        ){
            this.heavy();
        }

        if(
            ad<330&&
            this.energy>=100&&
            this.ultimateCooldown<=0&&
            Math.random()<.018
        ){
            this.ultimate(opponent);
        }
    }

    normalAttack(){

        if(this.attackCooldown>0) return;

        this.attackCooldown=.30;
        this.attackTimer=.18;
        this.state="attack";

        this.combo++;

        if(this.combo>3){
            this.combo=1;
        }

        this.comboTimer=.65;

        const reach=108;
        const targetX=
            this.x+
            this.facing*reach;

        slash(
            this.x,
            this.bodyY-5,
            this.data.color,
            this.facing,
            42,
            .22
        );

        particle(
            this.x+this.facing*65,
            this.bodyY-10,
            this.data.color,
            9,
            100
        );

        if(
            Math.abs(targetX-enemy.x)<78&&
            Math.abs(this.bodyY-enemy.bodyY)<85
        ){

            let damage=7;

            if(this.combo===3){
                damage=9;
            }

            enemy.takeDamage(
                damage,
                this.facing
            );

            this.energy=clamp(
                this.energy+7,
                0,
                100
            );
        }

        sfxSlash();
    }

    skill(){

        if(this.skillCooldown>0) return;
        if(this.energy<25) return;

        this.energy-=25;

        this.skillCooldown=1.0;
        this.attackTimer=.3;
        this.state="skill";

        projectiles.push({
            owner:this,
            x:this.x+this.facing*55,
            y:this.bodyY-35,
            vx:this.facing*this.getProjectileSpeed(),
            life:1.4,
            damage:this.getSkillDamage(),
            type:this.data.projectile,
            size:this.data.style==="wind"?28:20,
            rot:0
        });

        particle(
            this.x+this.facing*40,
            this.bodyY-35,
            this.data.color,
            16,
            130
        );

        sfxSkill(this.data.style);
    }

    getProjectileSpeed(){

        if(this.data.style==="thunder") return 850;
        if(this.data.style==="wind") return 780;
        if(this.data.style==="fire") return 650;

        return 590;
    }

    getSkillDamage(){

        if(this.data.style==="rock") return 18;
        if(this.data.style==="thunder") return 17;
        if(this.data.style==="wind") return 16;

        return 15;
    }

    dash(){

        if(this.dashCooldown>0) return;

        this.dashCooldown=.70;

        this.dashTimer=.19;

        this.dashInvincible=.19;

        this.vx=this.facing*1200;

        this.state="dash";

        for(let i=0;i<5;i++){
            makeAfterimage(this);
        }

        particle(
            this.x-this.facing*25,
            this.bodyY,
            this.data.color,
            18,
            180
        );

        ring(
            this.x,
            this.bodyY,
            this.data.color,
            45
        );

        if(this.data.style==="wind"){

            for(let i=0;i<7;i++){

                windBlades.push({
                    x:this.x-this.facing*rand(0,100),
                    y:this.bodyY+rand(-45,35),
                    vx:this.facing*rand(100,250),
                    life:.5,
                    size:rand(20,45),
                    rot:rand(-.5,.5)
                });
            }
        }

        sfxDash(this.data.style);
    }

    heavy(){

        if(this.heavyCooldown>0) return;

        this.heavyCooldown=.72;
        this.attackTimer=.32;
        this.state="heavy";

        const reach=135;
        const targetX=
            this.x+
            this.facing*reach;

        slash(
            this.x,
            this.bodyY-5,
            this.data.color,
            this.facing,
            78,
            .34
        );

        ring(
            this.x+this.facing*75,
            this.bodyY,
            this.data.color,
            60
        );

        particle(
            this.x+this.facing*75,
            this.bodyY,
            this.data.color,
            22,
            170
        );

        if(
            Math.abs(targetX-enemy.x)<95&&
            Math.abs(this.bodyY-enemy.bodyY)<100
        ){

            enemy.takeDamage(
                13,
                this.facing
            );

            this.energy=clamp(
                this.energy+10,
                0,
                100
            );
        }

        sfxHeavy();
    }

    ultimate(opponent){

        if(this.energy<100) return;
        if(this.ultimateCooldown>0) return;

        this.energy=0;
        this.ultimateCooldown=4;

        this.attackTimer=.8;
        this.state="ultimate";

        const distance=
            Math.abs(this.x-opponent.x);

        ultimateEffect(this);

        if(distance<310){

            opponent.takeDamage(
                32,
                this.facing
            );

            opponent.vx=this.facing*420;
            opponent.vy=-260;
        }

        sfxUltimate(this.data.style);
    }

    takeDamage(damage,dir){

        if(this.dashInvincible>0) return;
        if(this.dead) return;

        this.hp-=damage;

        this.hitFlash=.18;
        this.hitStun=.12;

        this.vx=dir*280;
        this.vy=-170;

        this.state="hit";

        particle(
            this.x,
            this.bodyY-30,
            "#ffffff",
            13,
            180
        );

        ring(
            this.x,
            this.bodyY-25,
            "#ffffff",
            32
        );

        sfxHit();

        if(this.hp<=0){

            this.hp=0;
            this.dead=true;

            particle(
                this.x,
                this.bodyY-30,
                this.data.color,
                50,
                300
            );
        }
    }

    draw(){

        const x=this.x;
        const y=this.bodyY+this.y;

        const bob=
            this.state==="idle"
            ?Math.sin(this.anim*4)*2
            :0;

        const yy=y+bob;

        ctx.save();

        if(this.hitFlash>0){
            ctx.globalAlpha=.78;
        }

        drawCharacterAura(this,x,yy);
        drawCharacterShadow(this,x,yy);
        drawCharacterBody(this,x,yy);
        drawCharacterWeapon(this,x,yy);

        if(
            this.state==="attack"||
            this.state==="heavy"
        ){
            drawAttackPose(this,x,yy);
        }

        if(this.state==="skill"){
            drawSkillPose(this,x,yy);
        }

        if(this.state==="ultimate"){
            drawUltimatePose(this,x,yy);
        }

        ctx.restore();
    }
}

/* =========================================================
   CHARACTER DRAW
   ========================================================= */

function drawCharacterAura(f,x,y){

    const c=f.data.color;

    const pulse=
        1+
        Math.sin(f.anim*6)*.08;

    if(f.data.style==="wind"){

        ctx.save();

        ctx.globalAlpha=.13;

        for(let i=0;i<5;i++){

            ctx.beginPath();

            ctx.ellipse(
                x,
                y-45,
                (48+i*13)*pulse,
                (78+i*15)*pulse,
                Math.sin(f.anim*1.4+i)*.4,
                0,
                Math.PI*2
            );

            ctx.strokeStyle=c;
            ctx.lineWidth=3;
            ctx.shadowBlur=18;
            ctx.shadowColor=c;

            ctx.stroke();
        }

        ctx.restore();

        return;
    }

    ctx.save();

    const g=ctx.createRadialGradient(
        x,
        y-50,
        5,
        x,
        y-50,
        105
    );

    g.addColorStop(0,c+"55");
    g.addColorStop(.45,c+"20");
    g.addColorStop(1,"transparent");

    ctx.fillStyle=g;

    ctx.beginPath();
    ctx.arc(
        x,
        y-45,
        105*pulse,
        0,
        Math.PI*2
    );

    ctx.fill();

    ctx.restore();
}

function drawCharacterShadow(f,x,y){

    ctx.save();

    ctx.globalAlpha=.35;
    ctx.fillStyle="#000";

    ctx.beginPath();

    ctx.ellipse(
        x,
        f.floorY+5,
        43,
        10,
        0,
        0,
        Math.PI*2
    );

    ctx.fill();

    ctx.restore();
}

function drawCharacterBody(f,x,y){

    const c=f.data.color;
    const dark=f.data.dark;
    const light=f.data.light;

    const moving=f.state==="run";

    const walk=
        moving
        ?Math.sin(f.anim*13)*9
        :0;

    ctx.save();

    ctx.translate(x,y);
    ctx.scale(f.facing,1);

    /* legs */

    ctx.strokeStyle="#171827";
    ctx.lineWidth=13;
    ctx.lineCap="round";

    ctx.beginPath();
    ctx.moveTo(-12,43);
    ctx.lineTo(-15+walk,76);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(12,43);
    ctx.lineTo(15-walk,76);
    ctx.stroke();

    /* boots */

    ctx.fillStyle="#090b16";

    ctx.beginPath();
    ctx.roundRect(-28+walk,69,27,11,5);
    ctx.fill();

    ctx.beginPath();
    ctx.roundRect(2-walk,69,27,11,5);
    ctx.fill();

    /* uniform */

    ctx.fillStyle="#151829";

    ctx.beginPath();
    ctx.moveTo(-27,-3);
    ctx.lineTo(27,-3);
    ctx.lineTo(24,48);
    ctx.lineTo(0,57);
    ctx.lineTo(-24,48);
    ctx.closePath();
    ctx.fill();

    /* collar */

    ctx.fillStyle=light;

    ctx.beginPath();
    ctx.moveTo(-15,-5);
    ctx.lineTo(0,13);
    ctx.lineTo(15,-5);
    ctx.lineTo(10,-12);
    ctx.lineTo(0,0);
    ctx.lineTo(-10,-12);
    ctx.closePath();
    ctx.fill();

    /* elemental clothing */

    if(f.data.style==="water"){

        ctx.fillStyle="#155d91";

        ctx.beginPath();
        ctx.moveTo(-33,-8);
        ctx.lineTo(-5,-2);
        ctx.lineTo(-13,54);
        ctx.lineTo(-39,42);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle="#1b85ba";

        ctx.beginPath();
        ctx.moveTo(33,-8);
        ctx.lineTo(5,-2);
        ctx.lineTo(13,54);
        ctx.lineTo(39,42);
        ctx.closePath();
        ctx.fill();

        drawWaterPattern(-30,10,c);
        drawWaterPattern(30,10,c);

    }else if(f.data.style==="fire"){

        ctx.fillStyle="#7e211d";

        ctx.beginPath();
        ctx.moveTo(-35,-9);
        ctx.lineTo(-4,-2);
        ctx.lineTo(-13,56);
        ctx.lineTo(-41,42);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle="#a93420";

        ctx.beginPath();
        ctx.moveTo(35,-9);
        ctx.lineTo(4,-2);
        ctx.lineTo(13,56);
        ctx.lineTo(41,42);
        ctx.closePath();
        ctx.fill();

        drawFlamePattern(-29,16);
        drawFlamePattern(29,16);

    }else if(f.data.style==="thunder"){

        ctx.fillStyle="#493d72";

        ctx.beginPath();
        ctx.moveTo(-35,-8);
        ctx.lineTo(-4,-2);
        ctx.lineTo(-14,55);
        ctx.lineTo(-41,41);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle="#65528f";

        ctx.beginPath();
        ctx.moveTo(35,-8);
        ctx.lineTo(4,-2);
        ctx.lineTo(14,55);
        ctx.lineTo(41,41);
        ctx.closePath();
        ctx.fill();

        drawLightningPattern(-28,18);
        drawLightningPattern(28,18);

    }else if(f.data.style==="flower"){

        ctx.fillStyle="#7b315f";

        ctx.beginPath();
        ctx.moveTo(-35,-8);
        ctx.lineTo(-4,-2);
        ctx.lineTo(-13,56);
        ctx.lineTo(-42,40);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle="#a94b82";

        ctx.beginPath();
        ctx.moveTo(35,-8);
        ctx.lineTo(4,-2);
        ctx.lineTo(13,56);
        ctx.lineTo(42,40);
        ctx.closePath();
        ctx.fill();

        drawFlowerPattern(-28,17);
        drawFlowerPattern(28,17);

    }else if(f.data.style==="rock"){

        ctx.fillStyle="#4e483f";

        ctx.beginPath();
        ctx.moveTo(-35,-8);
        ctx.lineTo(-4,-2);
        ctx.lineTo(-13,56);
        ctx.lineTo(-42,40);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle="#706556";

        ctx.beginPath();
        ctx.moveTo(35,-8);
        ctx.lineTo(4,-2);
        ctx.lineTo(13,56);
        ctx.lineTo(42,40);
        ctx.closePath();
        ctx.fill();

        drawRockPattern(-28,18);
        drawRockPattern(28,18);

    }else if(f.data.style==="wind"){

        ctx.fillStyle="#174f4b";

        ctx.beginPath();
        ctx.moveTo(-36,-10);
        ctx.lineTo(-4,-2);
        ctx.lineTo(-17,57);
        ctx.lineTo(-45,38);
        ctx.closePath();
        ctx.fill();

        ctx.fillStyle="#216d65";

        ctx.beginPath();
        ctx.moveTo(36,-10);
        ctx.lineTo(4,-2);
        ctx.lineTo(17,57);
        ctx.lineTo(45,38);
        ctx.closePath();
        ctx.fill();

        drawWindPattern(-29,17);
        drawWindPattern(29,17);

        ctx.strokeStyle="#8fffe9";
        ctx.globalAlpha=.65;
        ctx.lineWidth=3;

        ctx.beginPath();
        ctx.moveTo(32,4);
        ctx.bezierCurveTo(
            65,-12,
            75,16,
            103,2
        );
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(-32,14);
        ctx.bezierCurveTo(
            -60,2,
            -74,30,
            -98,13
        );
        ctx.stroke();

        ctx.globalAlpha=1;
    }

    /* belt */

    ctx.fillStyle=dark;
    ctx.fillRect(-27,35,54,7);

    ctx.fillStyle=light;

    ctx.beginPath();
    ctx.arc(0,39,5,0,Math.PI*2);
    ctx.fill();

    /* neck */

    ctx.fillStyle="#d39b7e";
    ctx.fillRect(-7,-18,14,15);

    /* head */

    ctx.fillStyle="#dca785";

    ctx.beginPath();
    ctx.arc(0,-43,25,0,Math.PI*2);
    ctx.fill();

    /* face */

    ctx.fillStyle="rgba(80,30,35,.18)";

    ctx.beginPath();
    ctx.arc(8,-37,17,0,Math.PI);
    ctx.fill();

    drawHair(f);
    drawEyes(f);

    /* nose */

    ctx.strokeStyle="#9a6358";
    ctx.lineWidth=1;

    ctx.beginPath();
    ctx.moveTo(5,-39);
    ctx.lineTo(7,-36);
    ctx.stroke();

    /* mouth */

    ctx.strokeStyle="#783f49";

    ctx.beginPath();
    ctx.moveTo(3,-28);
    ctx.lineTo(10,-28);
    ctx.stroke();

    /* arms */

    const armSwing=
        moving
        ?Math.sin(f.anim*13)*12
        :0;

    ctx.strokeStyle="#161824";
    ctx.lineWidth=12;

    ctx.beginPath();
    ctx.moveTo(-24,0);
    ctx.lineTo(-38,-5+armSwing);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(24,0);
    ctx.lineTo(38,-5-armSwing);
    ctx.stroke();

    ctx.strokeStyle=c;
    ctx.lineWidth=8;

    ctx.beginPath();
    ctx.moveTo(-24,0);
    ctx.lineTo(-39,-5+armSwing);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(24,0);
    ctx.lineTo(39,-5-armSwing);
    ctx.stroke();

    ctx.restore();
}

function drawHair(f){

    const style=f.data.style;

    let hair="#151728";

    if(style==="wind") hair="#163a3a";
    if(style==="thunder") hair="#22243b";
    if(style==="flower") hair="#241728";
    if(style==="fire") hair="#241313";
    if(style==="water") hair="#102433";
    if(style==="rock") hair="#25231f";

    ctx.fillStyle=hair;

    ctx.beginPath();

    ctx.moveTo(-25,-51);

    ctx.quadraticCurveTo(
        -20,-78,
        -2,-72
    );

    ctx.quadraticCurveTo(
        12,-84,
        25,-55
    );

    ctx.lineTo(20,-35);
    ctx.lineTo(12,-48);
    ctx.lineTo(6,-30);
    ctx.lineTo(0,-47);
    ctx.lineTo(-9,-31);
    ctx.lineTo(-12,-49);
    ctx.lineTo(-23,-35);

    ctx.closePath();
    ctx.fill();

    ctx.strokeStyle=f.data.color;
    ctx.lineWidth=3;
    ctx.globalAlpha=.65;

    ctx.beginPath();
    ctx.moveTo(-15,-60);
    ctx.quadraticCurveTo(-6,-72,4,-63);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(4,-63);
    ctx.quadraticCurveTo(13,-70,19,-55);
    ctx.stroke();

    ctx.globalAlpha=1;
}

function drawEyes(f){

    ctx.fillStyle="#121322";

    ctx.beginPath();
    ctx.ellipse(-9,-42,6,4,0,0,Math.PI*2);
    ctx.fill();

    ctx.beginPath();
    ctx.ellipse(9,-42,6,4,0,0,Math.PI*2);
    ctx.fill();

    ctx.fillStyle=f.data.light;

    ctx.beginPath();
    ctx.arc(-8,-43,2,0,Math.PI*2);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(10,-43,2,0,Math.PI*2);
    ctx.fill();
}

/* =========================================================
   PATTERNS
   ========================================================= */

function drawWaterPattern(x,y,c){

    ctx.strokeStyle=c;
    ctx.lineWidth=2;

    ctx.beginPath();
    ctx.arc(x,y,9,0,Math.PI);
    ctx.stroke();

    ctx.beginPath();
    ctx.arc(x+4,y+8,7,Math.PI,Math.PI*2);
    ctx.stroke();
}

function drawFlamePattern(x,y){

    ctx.fillStyle="#ffb126";

    ctx.beginPath();
    ctx.moveTo(x,y+12);
    ctx.quadraticCurveTo(x-8,y,x,y-7);
    ctx.quadraticCurveTo(x+8,y,x+2,y+12);
    ctx.fill();
}

function drawLightningPattern(x,y){

    ctx.strokeStyle="#ffe96b";
    ctx.lineWidth=2;

    ctx.beginPath();
    ctx.moveTo(x-4,y-9);
    ctx.lineTo(x+3,y);
    ctx.lineTo(x-3,y+2);
    ctx.lineTo(x+5,y+11);
    ctx.stroke();
}

function drawFlowerPattern(x,y){

    ctx.fillStyle="#ffb5e5";

    for(let i=0;i<5;i++){

        const a=i*Math.PI*2/5;

        ctx.beginPath();

        ctx.ellipse(
            x+Math.cos(a)*6,
            y+Math.sin(a)*6,
            4,
            7,
            a,
            0,
            Math.PI*2
        );

        ctx.fill();
    }
}

function drawRockPattern(x,y){

    ctx.strokeStyle="#b8aa8d";
    ctx.lineWidth=2;

    ctx.beginPath();
    ctx.moveTo(x-9,y-5);
    ctx.lineTo(x-2,y-10);
    ctx.lineTo(x+8,y-3);
    ctx.lineTo(x+3,y+8);
    ctx.lineTo(x-8,y+5);
    ctx.closePath();
    ctx.stroke();
}

function drawWindPattern(x,y){

    ctx.strokeStyle="#9affea";
    ctx.lineWidth=2;

    ctx.beginPath();

    ctx.arc(
        x,
        y,
        10,
        -.7,
        1.5
    );

    ctx.stroke();

    ctx.beginPath();

    ctx.arc(
        x+3,
        y+5,
        7,
        -.8,
        1.4
    );

    ctx.stroke();
}

/* =========================================================
   WEAPON
   ========================================================= */

function drawCharacterWeapon(f,x,y){

    ctx.save();

    ctx.translate(x,y);
    ctx.scale(f.facing,1);

    let bladeColor="#dfeeff";

    if(f.data.style==="wind") bladeColor="#b9fff2";
    if(f.data.style==="fire") bladeColor="#fff1cf";
    if(f.data.style==="thunder") bladeColor="#fffbd0";
    if(f.data.style==="flower") bladeColor="#ffe0f4";
    if(f.data.style==="rock") bladeColor="#d7d1c0";

    ctx.strokeStyle="#6e472f";
    ctx.lineWidth=5;

    ctx.beginPath();
    ctx.moveTo(37,-8);
    ctx.lineTo(63,-30);
    ctx.stroke();

    ctx.strokeStyle=bladeColor;
    ctx.lineWidth=4;

    ctx.shadowBlur=8;
    ctx.shadowColor=f.data.color;

    ctx.beginPath();
    ctx.moveTo(62,-31);
    ctx.lineTo(105,-72);
    ctx.stroke();

    ctx.shadowBlur=0;

    ctx.strokeStyle=f.data.color;
    ctx.lineWidth=2;

    ctx.beginPath();
    ctx.moveTo(64,-32);
    ctx.lineTo(105,-72);
    ctx.stroke();

    ctx.restore();
}

/* =========================================================
   POSES
   ========================================================= */

function drawAttackPose(f,x,y){

    ctx.save();

    ctx.translate(x,y);
    ctx.scale(f.facing,1);

    const strong=f.state==="heavy";

    ctx.strokeStyle=f.data.color;
    ctx.lineWidth=strong?7:5;
    ctx.globalAlpha=.72;

    ctx.beginPath();

    ctx.arc(
        25,
        -28,
        strong?90:65,
        strong?-1.05:-.8,
        .45
    );

    ctx.stroke();

    ctx.restore();
}

function drawSkillPose(f,x,y){

    ctx.save();

    ctx.translate(x,y);
    ctx.scale(f.facing,1);

    ctx.strokeStyle=f.data.color;
    ctx.lineWidth=4;
    ctx.globalAlpha=.7;

    ctx.beginPath();

    ctx.moveTo(20,-20);
    ctx.lineTo(62,-38);

    ctx.stroke();

    ctx.restore();
}

function drawUltimatePose(f,x,y){

    ctx.save();

    ctx.translate(x,y);

    ctx.globalAlpha=.28;

    ctx.strokeStyle=f.data.color;
    ctx.lineWidth=6;

    ctx.beginPath();

    ctx.arc(
        0,
        -40,
        100+Math.sin(f.anim*12)*10,
        0,
        Math.PI*2
    );

    ctx.stroke();

    ctx.globalAlpha=1;

    ctx.restore();
}

/* =========================================================
   SLASH
   ========================================================= */

function slash(
    x,
    y,
    color,
    facing,
    size,
    life
){

    slashes.push({
        x:x,
        y:y,
        color:color,
        facing:facing,
        size:size,
        life:life,
        max:life
    });
}

/* =========================================================
   PROJECTILES
   ========================================================= */

function drawProjectile(p){

    ctx.save();

    ctx.translate(p.x,p.y);

    p.rot+=.12;

    if(p.type==="water"){

        ctx.fillStyle="#39d7ff";
        ctx.shadowBlur=20;
        ctx.shadowColor="#27bfff";

        ctx.beginPath();
        ctx.arc(0,0,p.size,0,Math.PI*2);
        ctx.fill();

        ctx.strokeStyle="#a8f5ff";
        ctx.lineWidth=3;

        ctx.beginPath();
        ctx.arc(
            0,
            0,
            p.size+5,
            p.rot,
            p.rot+4
        );
        ctx.stroke();

    }else if(p.type==="fire"){

        ctx.fillStyle="#ff532d";
        ctx.shadowBlur=25;
        ctx.shadowColor="#ff4b25";

        ctx.beginPath();

        ctx.moveTo(-p.size,0);

        ctx.quadraticCurveTo(
            0,
            -p.size*1.4,
            p.size*1.3,
            0
        );

        ctx.quadraticCurveTo(
            0,
            p.size*1.2,
            -p.size,
            0
        );

        ctx.fill();

        ctx.fillStyle="#ffd05a";

        ctx.beginPath();
        ctx.arc(-4,0,p.size*.45,0,Math.PI*2);
        ctx.fill();

    }else if(p.type==="thunder"){

        ctx.strokeStyle="#fff36c";
        ctx.shadowBlur=25;
        ctx.shadowColor="#ffe63d";
        ctx.lineWidth=6;

        ctx.beginPath();
        ctx.moveTo(-18,8);
        ctx.lineTo(-5,-9);
        ctx.lineTo(2,2);
        ctx.lineTo(16,-13);
        ctx.stroke();

    }else if(p.type==="flower"){

        ctx.fillStyle="#ff83cf";
        ctx.shadowBlur=18;
        ctx.shadowColor="#ff63bd";

        for(let i=0;i<5;i++){

            const a=i*Math.PI*2/5;

            ctx.beginPath();

            ctx.ellipse(
                Math.cos(a)*8,
                Math.sin(a)*8,
                8,
                13,
                a,
                0,
                Math.PI*2
            );

            ctx.fill();
        }

        ctx.fillStyle="#ffe66d";

        ctx.beginPath();
        ctx.arc(0,0,5,0,Math.PI*2);
        ctx.fill();

    }else if(p.type==="rock"){

        ctx.fillStyle="#9f9277";
        ctx.shadowBlur=15;
        ctx.shadowColor="#a89a7d";

        ctx.beginPath();

        ctx.moveTo(-20,-9);
        ctx.lineTo(-5,-19);
        ctx.lineTo(17,-10);
        ctx.lineTo(22,8);
        ctx.lineTo(2,19);
        ctx.lineTo(-19,11);

        ctx.closePath();
        ctx.fill();

    }else if(p.type==="wind"){

        ctx.strokeStyle="#83ffe4";
        ctx.shadowBlur=25;
        ctx.shadowColor="#59efd0";
        ctx.lineWidth=5;

        for(let i=0;i<3;i++){

            ctx.beginPath();

            ctx.arc(
                0,
                0,
                p.size-i*7,
                -.9+i*.2,
                1.1+i*.2
            );

            ctx.stroke();
        }

        ctx.strokeStyle="#d5fff7";
        ctx.lineWidth=2;

        ctx.beginPath();

        ctx.moveTo(-25,0);

        ctx.quadraticCurveTo(
            0,
            -20,
            25,
            0
        );

        ctx.stroke();
    }

    ctx.restore();
}

/* =========================================================
   ULTIMATE
   ========================================================= */

let ultimateTimer=0;
let ultimateFighter=null;

function ultimateEffect(f){

    ultimateTimer=1.15;
    ultimateFighter=f;

    ring(
        f.x,
        f.bodyY,
        f.data.color,
        180
    );

    particle(
        f.x,
        f.bodyY-50,
        f.data.color,
        70,
        400
    );

    if(f.data.style==="wind"){

        for(let i=0;i<20;i++){

            windBlades.push({
                x:f.x+rand(-120,120),
                y:f.bodyY+rand(-120,60),
                vx:rand(-250,250),
                life:1.2,
                size:rand(25,65),
                rot:rand(-1,1)
            });
        }
    }

    if(f.data.style==="flower"){

        for(let i=0;i<45;i++){

            flowerPetals.push({
                x:f.x+rand(-180,180),
                y:f.bodyY+rand(-130,80),
                vx:rand(-80,80),
                vy:rand(-180,-30),
                rot:rand(0,6),
                life:1.5
            });
        }
    }
}

/* =========================================================
   WORLD
   ========================================================= */

function drawWorld(){

    const grad=ctx.createLinearGradient(
        0,
        0,
        0,
        H
    );

    grad.addColorStop(0,"#050714");
    grad.addColorStop(.48,"#0a1030");
    grad.addColorStop(1,"#15132b");

    ctx.fillStyle=grad;
    ctx.fillRect(0,0,W,H);

    /* moon */

    const mx=W*.5;
    const my=130;

    ctx.save();

    ctx.shadowBlur=40;
    ctx.shadowColor="rgba(160,200,255,.45)";
    ctx.fillStyle="#dceaff";

    ctx.beginPath();
    ctx.arc(mx,my,58,0,Math.PI*2);
    ctx.fill();

    ctx.restore();

    ctx.fillStyle="#101635";

    ctx.beginPath();
    ctx.arc(
        mx+22,
        my-13,
        56,
        0,
        Math.PI*2
    );

    ctx.fill();

    /* clouds */

    for(let i=0;i<5;i++){

        const cx=
            (i*280+80)-
            ((performance.now()/1000*7)%300);

        const cy=
            190+
            (i%2)*50;

        ctx.fillStyle=
            "rgba(110,140,210,.07)";

        ctx.beginPath();

        ctx.ellipse(
            cx,
            cy,
            100,
            22,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.beginPath();

        ctx.ellipse(
            cx+80,
            cy-8,
            80,
            18,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();
    }

    /* city */

    for(let i=0;i<30;i++){

        const bw=25+((i*17)%60);
        const bh=40+((i*43)%140);
        const bx=i*55;

        ctx.fillStyle="#080b1c";

        ctx.fillRect(
            bx,
            H-150-bh,
            bw,
            bh
        );

        ctx.fillStyle=
            "rgba(90,130,255,.13)";

        for(let wy=0;wy<4;wy++){

            ctx.fillRect(
                bx+8,
                H-145-bh+wy*20,
                4,
                7
            );
        }
    }

    /* floor */

    const floorY=H-145;

    const floorGrad=ctx.createLinearGradient(
        0,
        floorY,
        0,
        H
    );

    floorGrad.addColorStop(
        0,
        "#191d43"
    );

    floorGrad.addColorStop(
        1,
        "#080a18"
    );

    ctx.fillStyle=floorGrad;

    ctx.fillRect(
        0,
        floorY,
        W,
        H-floorY
    );

    ctx.strokeStyle=
        "rgba(100,170,255,.32)";

    ctx.lineWidth=2;

    ctx.beginPath();
    ctx.moveTo(0,floorY);
    ctx.lineTo(W,floorY);
    ctx.stroke();

    ctx.strokeStyle=
        "rgba(110,150,255,.08)";

    ctx.lineWidth=1;

    for(let x=0;x<W;x+=80){

        ctx.beginPath();

        ctx.moveTo(x,floorY);
        ctx.lineTo(x+80,H);

        ctx.stroke();
    }

    for(
        let y=floorY+30;
        y<H;
        y+=30
    ){

        ctx.beginPath();

        ctx.moveTo(0,y);
        ctx.lineTo(W,y);

        ctx.stroke();
    }
}

/* =========================================================
   EFFECT UPDATE
   ========================================================= */

function updateEffects(dt){

    for(let i=particles.length-1;i>=0;i--){

        const p=particles[i];

        p.life-=dt;

        p.x+=p.vx*dt;
        p.y+=p.vy*dt;

        p.vy+=300*dt;

        if(p.life<=0){
            particles.splice(i,1);
        }
    }

    for(let i=slashes.length-1;i>=0;i--){

        const s=slashes[i];

        s.life-=dt;

        if(s.life<=0){
            slashes.splice(i,1);
        }
    }

    for(let i=shockwaves.length-1;i>=0;i--){

        const s=shockwaves[i];

        s.life-=dt;
        s.r+=(s.max-s.r)*dt*8;

        if(s.life<=0){
            shockwaves.splice(i,1);
        }
    }

    for(let i=afterimages.length-1;i>=0;i--){

        const a=afterimages[i];

        a.life-=dt;

        if(a.life<=0){
            afterimages.splice(i,1);
        }
    }

    for(let i=windBlades.length-1;i>=0;i--){

        const b=windBlades[i];

        b.life-=dt;
        b.x+=b.vx*dt;

        b.y+=
            Math.sin(
                performance.now()/150+b.x
            )*
            20*
            dt;

        if(b.life<=0){
            windBlades.splice(i,1);
        }
    }

    for(let i=flowerPetals.length-1;i>=0;i--){

        const p=flowerPetals[i];

        p.life-=dt;

        p.x+=p.vx*dt;
        p.y+=p.vy*dt;
        p.vy+=120*dt;
        p.rot+=dt*4;

        if(p.life<=0){
            flowerPetals.splice(i,1);
        }
    }

    if(ultimateTimer>0){

        ultimateTimer-=dt;

        if(ultimateTimer<=0){
            ultimateFighter=null;
        }
    }
}

/* =========================================================
   DRAW EFFECTS
   ========================================================= */

function drawEffects(){

    afterimages.forEach(function(a){

        ctx.save();

        ctx.globalAlpha=
            (a.life/a.max)*.20;

        ctx.translate(a.x,a.y);
        ctx.scale(a.facing,1);

        ctx.fillStyle=a.color;

        ctx.beginPath();

        ctx.ellipse(
            0,
            -40,
            31,
            65,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.restore();
    });

    projectiles.forEach(drawProjectile);

    slashes.forEach(function(s){

        ctx.save();

        ctx.translate(s.x,s.y);
        ctx.scale(s.facing,1);

        ctx.globalAlpha=
            s.life/s.max;

        ctx.strokeStyle=s.color;
        ctx.shadowBlur=22;
        ctx.shadowColor=s.color;
        ctx.lineWidth=6;

        ctx.beginPath();

        ctx.arc(
            15,
            -30,
            s.size,
            -.95,
            .55
        );

        ctx.stroke();

        ctx.restore();
    });

    shockwaves.forEach(function(s){

        ctx.save();

        ctx.globalAlpha=s.life/.45;

        ctx.strokeStyle=s.color;
        ctx.shadowBlur=20;
        ctx.shadowColor=s.color;
        ctx.lineWidth=4;

        ctx.beginPath();
        ctx.arc(
            s.x,
            s.y,
            s.r,
            0,
            Math.PI*2
        );
        ctx.stroke();

        ctx.restore();
    });

    windBlades.forEach(function(b){

        ctx.save();

        ctx.globalAlpha=
            Math.min(1,b.life*2);

        ctx.translate(b.x,b.y);
        ctx.rotate(b.rot);

        ctx.strokeStyle="#8dffe9";
        ctx.shadowBlur=18;
        ctx.shadowColor="#5cf2d1";
        ctx.lineWidth=4;

        ctx.beginPath();

        ctx.arc(
            0,
            0,
            b.size,
            -.9,
            .8
        );

        ctx.stroke();

        ctx.restore();
    });

    flowerPetals.forEach(function(p){

        ctx.save();

        ctx.globalAlpha=
            Math.min(1,p.life);

        ctx.translate(p.x,p.y);
        ctx.rotate(p.rot);

        ctx.fillStyle="#ff91d4";

        ctx.beginPath();

        ctx.ellipse(
            0,
            0,
            5,
            10,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.restore();
    });

    if(
        ultimateTimer>0&&
        ultimateFighter
    ){

        const f=ultimateFighter;

        ctx.save();

        ctx.globalAlpha=
            Math.min(.45,ultimateTimer*.4);

        ctx.strokeStyle=f.data.color;
        ctx.lineWidth=8;

        ctx.beginPath();

        ctx.arc(
            f.x,
            f.bodyY-45,
            170+
            (1.15-ultimateTimer)*90,
            0,
            Math.PI*2
        );

        ctx.stroke();

        ctx.restore();

        if(f.data.style==="wind"){

            ctx.save();

            ctx.globalAlpha=.55;
            ctx.strokeStyle="#9ffff0";
            ctx.lineWidth=5;

            for(let i=0;i<8;i++){

                ctx.beginPath();

                ctx.arc(
                    f.x,
                    f.bodyY-40,
                    80+i*20,
                    i*.7+ultimateTimer,
                    i*.7+
                    ultimateTimer+
                    1.8
                );

                ctx.stroke();
            }

            ctx.restore();
        }
    }
}

/* =========================================================
   PROJECTILE UPDATE
   ========================================================= */

function updateProjectiles(dt){

    for(let i=projectiles.length-1;i>=0;i--){

        const p=projectiles[i];

        p.life-=dt;
        p.x+=p.vx*dt;
        p.rot+=dt*5;

        const target=
            p.owner===player2
            ?player1
            :player2;

        if(
            Math.abs(p.x-target.x)<45&&
            Math.abs(p.y-target.bodyY)<70
        ){

            target.takeDamage(
                p.damage,
                Math.sign(p.vx)
            );

            particle(
                p.x,
                p.y,
                p.owner.data.color,
                15,
                150
            );

            projectiles.splice(i,1);

            continue;
        }

        if(
            p.life<=0||
            p.x<-100||
            p.x>W+100
        ){

            projectiles.splice(i,1);
        }
    }
}

/* =========================================================
   GAME STATE
   ========================================================= */

let player1=null;
let player2=null;

let enemy=null;

let gameStarted=false;
let running=false;
let ending=false;

let timeLeft=60;

let lastTime=performance.now();

/* =========================================================
   START
   ========================================================= */

function startGame(){

    initAudio();

    const n1=
        document
        .getElementById("p1Name")
        .value
        .trim()
        .substring(0,20)
        ||
        "Player 1";

    const n2=
        document
        .getElementById("p2Name")
        .value
        .trim()
        .substring(0,20)
        ||
        "Player 2";

    player1=
        new Fighter(
            W*.30,
            1,
            selectedP1
        );

    player2=
        new Fighter(
            W*.70,
            2,
            gameMode==="cpu"
            ?getRandomEnemy(selectedP1)
            :selectedP2
        );

    player1.name=n1;

    player2.name=
        gameMode==="cpu"
        ?"CPU"
        :n2;

    enemy=player2;

    gameStarted=true;
    running=false;
    ending=false;

    timeLeft=60;

    home.classList.add("hidden");
    hud.classList.remove("hidden");
    help.classList.remove("hidden");
    result.classList.add("hidden");

    name1El.textContent=
        player1.name+
        " • "+
        player1.data.name;

    name2El.textContent=
        player2.name+
        " • "+
        player2.data.name;

    countdown();
}

function getRandomEnemy(except){

    const ids=
        Object.keys(CHARACTERS)
        .filter(function(x){
            return x!==except;
        });

    return ids[
        Math.floor(
            Math.random()*ids.length
        )
    ];
}

/* =========================================================
   COUNTDOWN
   ========================================================= */

function countdown(){

    countdownEl.classList.remove("hidden");

    const nums=[
        "3",
        "2",
        "1",
        "FIGHT!"
    ];

    let i=0;

    countdownEl.textContent=nums[i];

    sfxCountdown(3);

    const interval=setInterval(function(){

        i++;

        if(i>=nums.length){

            clearInterval(interval);

            sfxFight();

            setTimeout(function(){

                countdownEl.classList.add("hidden");

                running=true;

            },500);

            return;
        }

        countdownEl.textContent=nums[i];

        if(nums[i]==="2"){
            sfxCountdown(2);
        }

        if(nums[i]==="1"){
            sfxCountdown(1);
        }

    },650);
}

/* =========================================================
   END GAME
   ========================================================= */

function endGame(){

    if(!gameStarted) return;
    if(ending) return;

    ending=true;
    running=false;

    let winner=null;

    if(
        player1.hp<=0&&
        player2.hp<=0
    ){

        resultTitle.textContent="DRAW";

        resultSub.textContent=
            "Cả hai đã chiến đấu đến cùng!";

        sfxDraw();

    }else if(player1.hp<=0){

        winner=player2;

        resultTitle.textContent=
            gameMode==="cpu"
            ?"YOU LOSE"
            :"PLAYER 2 VICTORY";

        resultSub.textContent=
            winner.name+
            " • "+
            winner.data.name+
            " thắng trận!";

        sfxDefeat();

    }else if(player2.hp<=0){

        winner=player1;

        resultTitle.textContent="VICTORY";

        resultSub.textContent=
            winner.name+
            " • "+
            winner.data.name+
            " đã chiến thắng!";

        sfxVictory();
        createBalloons();

    }else{

        if(player1.hp>player2.hp){

            winner=player1;

            resultTitle.textContent="VICTORY";

            resultSub.textContent=
                winner.name+
                " thắng nhờ HP cao hơn!";

            sfxVictory();
            createBalloons();

        }else if(player2.hp>player1.hp){

            winner=player2;

            resultTitle.textContent=
                gameMode==="cpu"
                ?"YOU LOSE"
                :"PLAYER 2 VICTORY";

            resultSub.textContent=
                winner.name+
                " thắng nhờ HP cao hơn!";

            sfxDefeat();

        }else{

            resultTitle.textContent="DRAW";

            resultSub.textContent=
                "Hai bên hòa!";

            sfxDraw();
        }
    }

    result.classList.remove("hidden");
}

function createBalloons(){

    balloons.innerHTML="";

    const colors=[
        "#ff4f7b",
        "#5cc8ff",
        "#ffd84f",
        "#7aff9a",
        "#c57aff",
        "#ff8c54"
    ];

    for(let i=0;i<28;i++){

        const b=
            document.createElement("div");

        b.className="balloon";

        b.style.left=
            Math.random()*100+
            "%";

        b.style.background=
            colors[
                Math.floor(
                    Math.random()*colors.length
                )
            ];

        b.style.color=b.style.background;

        b.style.animationDelay=
            Math.random()*1.6+
            "s";

        b.style.transform=
            "scale("+
            (.7+Math.random()*.7)+
            ")";

        balloons.appendChild(b);
    }
}

/* =========================================================
   BUTTONS
   ========================================================= */

document.getElementById("startBtn").onclick=
    startGame;

document.getElementById("backBtn").onclick=
    function(){

        gameStarted=false;
        running=false;
        ending=false;

        result.classList.add("hidden");
        hud.classList.add("hidden");
        help.classList.add("hidden");

        home.classList.remove("hidden");

        countdownEl.classList.add("hidden");

        balloons.innerHTML="";

        particles.length=0;
        projectiles.length=0;
        slashes.length=0;
        shockwaves.length=0;
        afterimages.length=0;
        windBlades.length=0;
        flowerPetals.length=0;

        player1=null;
        player2=null;
        enemy=null;
    };

/* =========================================================
   HUD
   ========================================================= */

function updateHUD(){

    if(!player1||!player2) return;

    hp1El.style.width=
        clamp(
            player1.hp,
            0,
            100
        )+
        "%";

    hp2El.style.width=
        clamp(
            player2.hp,
            0,
            100
        )+
        "%";

    energy1El.style.width=
        clamp(
            player1.energy,
            0,
            100
        )+
        "%";

    energy2El.style.width=
        clamp(
            player2.energy,
            0,
            100
        )+
        "%";

    timerEl.textContent=
        Math.ceil(timeLeft);
}

/* =========================================================
   GAME LOOP
   ========================================================= */

function gameLoop(now){

    const dt=Math.min(
        .033,
        (now-lastTime)/1000
    );

    lastTime=now;

    drawWorld();

    updateEffects(dt);

    if(gameStarted){

        if(running){

            player1.update(
                dt,
                player2
            );

            player2.update(
                dt,
                player1
            );

            updateProjectiles(dt);

            timeLeft-=dt;

            if(timeLeft<=0){

                timeLeft=0;

                endGame();
            }

            if(
                !ending&&
                (player1.dead||
                player2.dead)
            ){

                running=false;

                setTimeout(function(){
                    endGame();
                },350);
            }
        }

        drawEffects();

        if(player1){
            player1.draw();
        }

        if(player2){
            player2.draw();
        }

        updateHUD();

    }else{

        drawEffects();
    }

    requestAnimationFrame(gameLoop);
}

requestAnimationFrame(gameLoop);

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
