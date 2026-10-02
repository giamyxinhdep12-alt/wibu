import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Blade Breathing 1v1",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

GAME_HTML = r"""
<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">

<style>
*{
    box-sizing:border-box;
    user-select:none;
}

html,body{
    margin:0;
    padding:0;
    width:100%;
    height:100%;
    overflow:hidden;
    background:#02040b;
    font-family:Arial,Helvetica,sans-serif;
}

#game{
    position:relative;
    width:100%;
    height:100%;
    min-height:680px;
    overflow:hidden;
    outline:none;
    background:#050814;
}

canvas{
    position:absolute;
    inset:0;
    width:100%;
    height:100%;
}

#hud{
    position:absolute;
    inset:0;
    pointer-events:none;
}

.card{
    position:absolute;
    top:18px;
    width:370px;
    padding:12px 14px;
    border-radius:16px;
    background:linear-gradient(
        135deg,
        rgba(8,13,28,.95),
        rgba(15,20,38,.78)
    );
    border:1px solid rgba(255,255,255,.14);
    box-shadow:
        0 12px 35px rgba(0,0,0,.5),
        inset 0 1px rgba(255,255,255,.08);
    backdrop-filter:blur(10px);
}

#p1Card{left:18px}
#p2Card{right:18px;text-align:right}

.player{
    display:flex;
    align-items:center;
    gap:10px;
}

#p2Card .player{
    flex-direction:row-reverse;
}

.icon{
    width:43px;
    height:43px;
    border-radius:12px;
    display:grid;
    place-items:center;
    font-size:23px;
    font-weight:900;
    color:white;
}

.water{
    background:linear-gradient(135deg,#0adfff,#2862ff);
    box-shadow:0 0 18px rgba(20,170,255,.45);
}

.fire{
    background:linear-gradient(135deg,#ff263d,#ff8b00);
    box-shadow:0 0 18px rgba(255,80,20,.45);
}

.name{
    color:#fff;
    font-weight:1000;
    letter-spacing:1px;
    font-size:16px;
}

.sub{
    color:#7e89ac;
    font-size:9px;
    letter-spacing:1.8px;
    margin-top:2px;
}

.label{
    color:#7f8bab;
    font-size:8px;
    font-weight:bold;
    letter-spacing:2px;
    margin-top:8px;
    margin-bottom:4px;
}

.bar{
    width:100%;
    height:12px;
    border-radius:99px;
    background:rgba(0,0,0,.55);
    border:1px solid rgba(255,255,255,.08);
    overflow:hidden;
    box-shadow:inset 0 2px 5px rgba(0,0,0,.7);
}

.fill{
    height:100%;
    width:100%;
    border-radius:99px;
    transition:width .12s linear;
}

.hp1{
    background:linear-gradient(90deg,#00cfff,#2588ff);
    box-shadow:0 0 12px #00bfff;
}

.hp2{
    background:linear-gradient(90deg,#ff244d,#ff8b00);
    box-shadow:0 0 12px #ff4a28;
}

.energy{
    background:linear-gradient(90deg,#7e3cff,#d72fff,#ff74db);
    box-shadow:0 0 13px #bb38ff;
}

.energyLine{
    display:flex;
    gap:7px;
    align-items:center;
}

.energyLine .bar{
    flex:1;
}

.energyNumber{
    color:#e5baff;
    font-size:9px;
    font-weight:900;
    width:28px;
}

.auto{
    pointer-events:auto;
    border:1px solid rgba(255,255,255,.15);
    border-radius:8px;
    background:rgba(255,255,255,.06);
    color:#b8c1dc;
    padding:5px 8px;
    font-size:8px;
    font-weight:1000;
    cursor:pointer;
    transition:.15s;
}

.auto:hover{
    transform:translateY(-1px);
    background:rgba(255,255,255,.12);
}

.auto.on{
    color:white;
    background:linear-gradient(135deg,#7a28ff,#dd27d8);
    border-color:#ec91ff;
    box-shadow:0 0 15px rgba(207,40,255,.55);
}

#timerBox{
    position:absolute;
    top:18px;
    left:50%;
    transform:translateX(-50%);
    width:108px;
    height:73px;
    border-radius:18px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    background:linear-gradient(
        145deg,
        rgba(19,25,47,.97),
        rgba(4,7,17,.95)
    );
    border:1px solid rgba(255,255,255,.17);
    box-shadow:0 12px 35px rgba(0,0,0,.5);
}

#timer{
    color:white;
    font-size:30px;
    font-weight:1000;
    letter-spacing:2px;
    line-height:31px;
    text-shadow:0 0 15px rgba(255,255,255,.4);
}

.timerSmall{
    color:#717c9e;
    font-size:7px;
    letter-spacing:3px;
    font-weight:bold;
}

#mute{
    position:absolute;
    right:18px;
    bottom:18px;
    pointer-events:auto;
    border:1px solid rgba(255,255,255,.12);
    border-radius:9px;
    background:rgba(5,9,20,.75);
    color:#c7cee5;
    padding:7px 10px;
    font-size:10px;
    cursor:pointer;
    backdrop-filter:blur(8px);
}

#controls{
    position:absolute;
    bottom:18px;
    left:50%;
    transform:translateX(-50%);
    padding:8px 14px;
    border-radius:11px;
    background:rgba(4,7,17,.68);
    border:1px solid rgba(255,255,255,.1);
    color:#7f8bad;
    font-size:9px;
    text-align:center;
    backdrop-filter:blur(8px);
}

.key{
    display:inline-block;
    color:white;
    background:rgba(255,255,255,.08);
    border:1px solid rgba(255,255,255,.12);
    border-radius:4px;
    padding:2px 5px;
    margin:0 2px;
    font-weight:bold;
}

.overlay{
    position:absolute;
    inset:0;
    z-index:50;
    display:flex;
    justify-content:center;
    align-items:center;
    background:
        radial-gradient(
            circle at center,
            rgba(30,60,120,.28),
            rgba(2,4,12,.93) 70%
        );
    backdrop-filter:blur(5px);
}

.panel{
    width:min(590px,90%);
    padding:34px;
    border-radius:25px;
    text-align:center;
    background:linear-gradient(
        145deg,
        rgba(15,21,43,.97),
        rgba(4,7,18,.98)
    );
    border:1px solid rgba(255,255,255,.14);
    box-shadow:
        0 25px 90px rgba(0,0,0,.75),
        0 0 70px rgba(55,90,255,.12);
}

.logo{
    color:white;
    font-size:47px;
    font-weight:1000;
    font-style:italic;
    letter-spacing:-3px;
    text-shadow:
        0 0 14px #299aff,
        0 0 40px rgba(40,120,255,.65);
}

.logo span{
    color:#ff583b;
    text-shadow:0 0 20px rgba(255,70,40,.6);
}

.desc{
    color:#7f8baa;
    font-size:10px;
    letter-spacing:3px;
    margin:8px 0 25px;
}

.start{
    pointer-events:auto;
    cursor:pointer;
    border:0;
    border-radius:12px;
    color:white;
    padding:14px 40px;
    font-size:15px;
    font-weight:1000;
    letter-spacing:2px;
    background:linear-gradient(135deg,#226aff,#a52cff);
    box-shadow:0 10px 30px rgba(78,67,255,.45);
    transition:.18s;
}

.start:hover{
    transform:translateY(-3px) scale(1.03);
    box-shadow:0 15px 40px rgba(107,54,255,.6);
}

.rules{
    margin-top:22px;
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:8px;
}

.rule{
    padding:10px;
    border-radius:9px;
    background:rgba(255,255,255,.04);
    color:#8490b1;
    font-size:9px;
    text-align:left;
}

.rule b{
    color:white;
}

#countdown{
    position:absolute;
    inset:0;
    z-index:40;
    display:none;
    place-items:center;
    pointer-events:none;
    color:white;
    font-size:125px;
    font-weight:1000;
    font-style:italic;
    text-shadow:
        0 0 15px #3c9cff,
        0 0 45px #674bff,
        0 0 100px #d62fff;
}

#resultOverlay{
    display:none;
}

#winner{
    color:white;
    font-size:45px;
    font-weight:1000;
    margin-bottom:8px;
    text-shadow:0 0 30px #7e4dff;
}

#resultInfo{
    color:#8a94b4;
    font-size:12px;
    margin-bottom:23px;
}

@media(max-width:850px){
    .card{width:280px}
    #controls{display:none}
}
</style>
</head>

<body>

<div id="game" tabindex="0">

<canvas id="canvas"></canvas>

<div id="hud">

    <div class="card" id="p1Card">
        <div class="player">
            <div class="icon water">🌊</div>
            <div>
                <div class="name">PLAYER 1</div>
                <div class="sub">WATER BREATHING</div>
            </div>
        </div>

        <div class="label">VITALITY</div>
        <div class="bar">
            <div id="p1HP" class="fill hp1"></div>
        </div>

        <div class="label">BREATHING POWER</div>
        <div class="energyLine">
            <div class="bar">
                <div id="p1Energy" class="fill energy"></div>
            </div>
            <div id="p1EnergyNumber" class="energyNumber">0</div>
            <button id="p1Auto" class="auto">⚡ TỰ HỒI: OFF</button>
        </div>
    </div>

    <div id="timerBox">
        <div id="timer">60</div>
        <div class="timerSmall">BATTLE</div>
    </div>

    <div class="card" id="p2Card">
        <div class="player">
            <div class="icon fire">🔥</div>
            <div>
                <div class="name">PLAYER 2</div>
                <div class="sub">FLAME BREATHING</div>
            </div>
        </div>

        <div class="label">VITALITY</div>
        <div class="bar">
            <div id="p2HP" class="fill hp2"></div>
        </div>

        <div class="label">BREATHING POWER</div>
        <div class="energyLine">
            <button id="p2Auto" class="auto">⚡ TỰ HỒI: OFF</button>
            <div class="bar">
                <div id="p2Energy" class="fill energy"></div>
            </div>
            <div id="p2EnergyNumber" class="energyNumber">0</div>
        </div>
    </div>

    <button id="mute">🔊 SOUND</button>

    <div id="controls">
        P1:
        <span class="key">A/D</span> di chuyển
        <span class="key">W</span> nhảy
        <span class="key">F</span> chém
        <span class="key">G</span> skill
        <span class="key">H</span> ultimate
        &nbsp;&nbsp;|&nbsp;&nbsp;
        P2:
        <span class="key">←/→</span>
        <span class="key">↑</span>
        <span class="key">K</span>
        <span class="key">L</span>
        <span class="key">O</span>
    </div>
</div>

<div id="startOverlay" class="overlay">
    <div class="panel">
        <div class="logo">BLADE <span>BREATHING</span></div>
        <div class="desc">ANIME-STYLE 1V1 SWORD BATTLE</div>

        <button id="startButton" class="start">
            ⚔️ BẮT ĐẦU TRẬN ĐẤU
        </button>

        <div class="rules">
            <div class="rule">
                <b>🌊 P1</b><br>
                Hơi Thở Nước · tốc độ · kiếm thuật
            </div>
            <div class="rule">
                <b>🔥 P2</b><br>
                Hơi Thở Lửa · sát thương · bùng nổ
            </div>
            <div class="rule">
                <b>⚡ TỰ HỒI</b><br>
                Bật nút trên HUD để tự hồi năng lượng
            </div>
            <div class="rule">
                <b>💥 ULTIMATE</b><br>
                Cần đủ 100 năng lượng
            </div>
        </div>
    </div>
</div>

<div id="countdown">3</div>

<div id="resultOverlay" class="overlay">
    <div class="panel">
        <div id="winner">PLAYER 1 WINS</div>
        <div id="resultInfo">Chiến thắng!</div>
        <button id="restartButton" class="start">
            🔄 ĐÁNH LẠI
        </button>
    </div>
</div>

</div>

<script>
(() => {
"use strict";

const game = document.getElementById("game");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");

let W = 1200;
let H = 680;
let ground = 555;

let running = false;
let finished = false;
let countdownActive = false;
let timeLeft = 60;

let lastTime = 0;
let shake = 0;
let globalFlash = 0;

let keys = {};

let p1 = null;
let p2 = null;

let projectiles = [];
let effects = [];
let particles = [];
let slashWaves = [];

let muted = false;
let audioCtx = null;


/* =========================
   AUDIO
========================= */

function initAudio(){
    if(!audioCtx){
        const AC = window.AudioContext || window.webkitAudioContext;
        if(AC) audioCtx = new AC();
    }

    if(audioCtx && audioCtx.state === "suspended"){
        audioCtx.resume();
    }
}

function tone(freq, duration, type="sine", volume=.04, slide=0){
    if(muted || !audioCtx) return;

    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();

    osc.type = type;
    osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

    if(slide !== 0){
        osc.frequency.exponentialRampToValueAtTime(
            Math.max(20, freq + slide),
            audioCtx.currentTime + duration
        );
    }

    gain.gain.setValueAtTime(volume, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(
        .001,
        audioCtx.currentTime + duration
    );

    osc.connect(gain);
    gain.connect(audioCtx.destination);

    osc.start();
    osc.stop(audioCtx.currentTime + duration);
}

function noise(duration=.12, volume=.04){
    if(muted || !audioCtx) return;

    const buffer = audioCtx.createBuffer(
        1,
        audioCtx.sampleRate * duration,
        audioCtx.sampleRate
    );

    const data = buffer.getChannelData(0);

    for(let i=0;i<data.length;i++){
        data[i] = (Math.random()*2-1) * (1-i/data.length);
    }

    const src = audioCtx.createBufferSource();
    const gain = audioCtx.createGain();

    src.buffer = buffer;
    gain.gain.value = volume;

    src.connect(gain);
    gain.connect(audioCtx.destination);

    src.start();
}

function soundSword(){
    tone(430,.09,"sawtooth",.035,500);
    noise(.09,.025);
}

function soundHit(){
    tone(100,.12,"square",.06,-40);
    tone(210,.07,"triangle",.035,-100);
}

function soundSkill(who){
    if(who === 1){
        tone(170,.25,"sine",.045,500);
        tone(330,.18,"triangle",.03,300);
    }else{
        tone(90,.25,"sawtooth",.05,700);
        tone(180,.15,"square",.025,400);
    }
}

function soundUltimate(){
    tone(55,.5,"sawtooth",.06,900);
    tone(220,.35,"sine",.05,700);
    setTimeout(() => tone(600,.25,"triangle",.035,800),100);
}

function soundDash(){
    noise(.13,.035);
    tone(300,.1,"sine",.025,500);
}

function soundEnergy(){
    tone(330,.12,"sine",.035,250);
    tone(600,.18,"sine",.025,350);
}

function soundWin(){
    tone(440,.18,"triangle",.04,150);
    setTimeout(()=>tone(660,.2,"triangle",.04,180),140);
    setTimeout(()=>tone(880,.3,"triangle",.05,100),300);
}

function soundLose(){
    tone(260,.3,"sawtooth",.035,-150);
}


/* =========================
   RESIZE
========================= */

function resize(){
    const rect = game.getBoundingClientRect();

    W = Math.max(900, rect.width);
    H = Math.max(620, rect.height);

    canvas.width = W * devicePixelRatio;
    canvas.height = H * devicePixelRatio;

    canvas.style.width = W + "px";
    canvas.style.height = H + "px";

    ctx.setTransform(devicePixelRatio,0,0,devicePixelRatio,0,0);

    ground = H - 125;
}

window.addEventListener("resize", resize);
resize();


/* =========================
   FIGHTER
========================= */

function makeFighter(x, side, color){
    return {
        x:x,
        y:ground,
        vx:0,
        vy:0,

        side:side,
        color:color,

        hp:100,
        energy:0,

        autoEnergy:false,

        onGround:true,
        facing:side === 1 ? 1 : -1,

        attackTimer:0,
        skillTimer:0,
        ultimateTimer:0,

        attackAnim:0,
        skillAnim:0,
        hitFlash:0,

        invuln:0,

        combo:0,
        comboTimer:0
    };
}

function initPlayers(){
    p1 = makeFighter(W*.28,1,"water");
    p2 = makeFighter(W*.72,2,"fire");
    updateHUD();
    updateAutoButtons();
}


/* =========================
   EFFECT HELPERS
========================= */

function spawnParticle(x,y,color,count=10,speed=200){
    for(let i=0;i<count;i++){
        const a = Math.random()*Math.PI*2;
        const s = Math.random()*speed;

        particles.push({
            x:x,
            y:y,
            vx:Math.cos(a)*s,
            vy:Math.sin(a)*s,
            life:.35+Math.random()*.5,
            max:.35+Math.random()*.5,
            size:2+Math.random()*5,
            color:color
        });
    }
}

function spawnRing(x,y,color,size=50){
    effects.push({
        type:"ring",
        x:x,
        y:y,
        size:8,
        max:size,
        life:.35,
        maxLife:.35,
        color:color
    });
}

function spawnSlash(x,y,dir,color,large=false){
    slashWaves.push({
        x:x,
        y:y,
        dir:dir,
        color:color,
        life:.25,
        maxLife:.25,
        large:large
    });
}

function flash(amount=.35){
    globalFlash = Math.max(globalFlash,amount);
    shake = Math.max(shake,amount*25);
}


/* =========================
   ATTACKS
========================= */

function canAttack(f){
    return running &&
           !finished &&
           f.attackTimer <= 0 &&
           f.invuln <= 0;
}

function normalAttack(f,enemy){
    if(!canAttack(f)) return;

    f.attackTimer = .34;
    f.attackAnim = .25;

    soundSword();

    const distance = Math.abs(f.x-enemy.x);

    if(distance < 125){
        enemy.hp -= 8;
        enemy.energy = Math.min(100,enemy.energy+8);

        f.energy = Math.min(100,f.energy+8);

        enemy.hitFlash = .15;

        spawnParticle(
            enemy.x,
            enemy.y-70,
            enemy.side === 1 ? "#35dfff" : "#ff733b",
            14,
            250
        );

        spawnSlash(
            (f.x+enemy.x)/2,
            enemy.y-65,
            f.facing,
            f.side===1 ? "#36dfff" : "#ff6338"
        );

        soundHit();
        flash(.25);
    }
}

function skill(f,enemy){
    if(!running || finished) return;
    if(f.skillTimer > 0) return;
    if(f.energy < 25) return;

    f.energy -= 25;
    f.skillTimer = .65;
    f.skillAnim = .45;

    soundSkill(f.side);

    const dir = f.facing;

    projectiles.push({
        x:f.x + dir*42,
        y:f.y - 72,
        vx:dir*650,
        life:1.2,
        owner:f.side,
        color:f.side===1 ? "#35dfff" : "#ff6438",
        size:16
    });

    spawnRing(
        f.x,
        f.y-70,
        f.side===1 ? "#39dfff" : "#ff5935",
        85
    );

    spawnParticle(
        f.x,
        f.y-70,
        f.side===1 ? "#39dfff" : "#ff5935",
        22,
        300
    );
}

function ultimate(f,enemy){
    if(!running || finished) return;
    if(f.ultimateTimer > 0) return;
    if(f.energy < 100) return;

    f.energy = 0;
    f.ultimateTimer = 2;

    f.attackAnim = .9;

    soundUltimate();
    flash(.7);
    shake = 30;

    const distance = Math.abs(f.x-enemy.x);

    if(distance < 260){
        enemy.hp -= 35;
        enemy.hitFlash = .4;

        spawnRing(
            enemy.x,
            enemy.y-70,
            f.side===1 ? "#53eaff" : "#ff713c",
            210
        );

        spawnParticle(
            enemy.x,
            enemy.y-70,
            f.side===1 ? "#53eaff" : "#ff713c",
            60,
            600
        );

        spawnSlash(
            enemy.x,
            enemy.y-75,
            f.facing,
            f.side===1 ? "#62ecff" : "#ff7b42",
            true
        );
    }

    effects.push({
        type:"ultimate",
        x:f.x,
        y:f.y-70,
        life:.55,
        maxLife:.55,
        color:f.side===1 ? "#40e6ff" : "#ff623e"
    });
}


/* =========================
   PROJECTILE
========================= */

function updateProjectiles(dt){
    for(let i=projectiles.length-1;i>=0;i--){
        const p = projectiles[i];

        p.x += p.vx*dt;
        p.life -= dt;

        const enemy = p.owner === 1 ? p2 : p1;

        if(Math.abs(p.x-enemy.x)<55){
            enemy.hp -= 16;
            enemy.energy = Math.min(100,enemy.energy+12);

            enemy.hitFlash = .22;

            spawnParticle(
                enemy.x,
                enemy.y-75,
                p.color,
                25,
                330
            );

            spawnRing(
                enemy.x,
                enemy.y-70,
                p.color,
                80
            );

            soundHit();
            flash(.3);

            projectiles.splice(i,1);
            continue;
        }

        if(p.life<=0 || p.x<-100 || p.x>W+100){
            projectiles.splice(i,1);
        }
    }
}


/* =========================
   UPDATE
========================= */

function updateFighter(f,enemy,dt){
    if(f.attackTimer>0) f.attackTimer-=dt;
    if(f.skillTimer>0) f.skillTimer-=dt;
    if(f.ultimateTimer>0) f.ultimateTimer-=dt;
    if(f.attackAnim>0) f.attackAnim-=dt;
    if(f.skillAnim>0) f.skillAnim-=dt;
    if(f.hitFlash>0) f.hitFlash-=dt;
    if(f.invuln>0) f.invuln-=dt;
    if(f.comboTimer>0) f.comboTimer-=dt;

    if(f.comboTimer<=0){
        f.combo=0;
    }

    if(f.autoEnergy){
        f.energy = Math.min(100,f.energy+16*dt);
    }

    f.vy += 1700*dt;
    f.y += f.vy*dt;

    if(f.y>=ground){
        f.y=ground;
        f.vy=0;
        f.onGround=true;
    }else{
        f.onGround=false;
    }

    f.x += f.vx*dt;

    f.vx *= Math.pow(.001,dt);

    f.x = Math.max(80,Math.min(W-80,f.x));

    if(Math.abs(enemy.x-f.x)>15){
        f.facing = enemy.x>f.x ? 1 : -1;
    }
}

function controlPlayer1(){
    if(!running || finished) return;

    if(keys["a"]){
        p1.vx=-330;
        p1.facing=-1;
    }

    if(keys["d"]){
        p1.vx=330;
        p1.facing=1;
    }

    if(keys["w"] && p1.onGround){
        p1.vy=-700;
        p1.onGround=false;
        soundDash();
    }
}

function controlPlayer2(){
    if(!running || finished) return;

    if(keys["ArrowLeft"]){
        p2.vx=-330;
        p2.facing=-1;
    }

    if(keys["ArrowRight"]){
        p2.vx=330;
        p2.facing=1;
    }

    if(keys["ArrowUp"] && p2.onGround){
        p2.vy=-700;
        p2.onGround=false;
        soundDash();
    }
}

function updateParticles(dt){
    for(let i=particles.length-1;i>=0;i--){
        const p=particles[i];

        p.life-=dt;
        p.x+=p.vx*dt;
        p.y+=p.vy*dt;
        p.vy+=400*dt;

        if(p.life<=0){
            particles.splice(i,1);
        }
    }
}

function updateEffects(dt){
    for(let i=effects.length-1;i>=0;i--){
        const e=effects[i];

        e.life-=dt;

        if(e.type==="ring"){
            e.size += (e.max-e.size)*dt*8;
        }

        if(e.life<=0){
            effects.splice(i,1);
        }
    }

    for(let i=slashWaves.length-1;i>=0;i--){
        slashWaves[i].life-=dt;

        if(slashWaves[i].life<=0){
            slashWaves.splice(i,1);
        }
    }
}

function update(dt){
    if(!running || finished) return;

    timeLeft-=dt;

    if(timeLeft<=0){
        timeLeft=0;
        endGame();
        return;
    }

    controlPlayer1();
    controlPlayer2();

    updateFighter(p1,p2,dt);
    updateFighter(p2,p1,dt);

    updateProjectiles(dt);
    updateParticles(dt);
    updateEffects(dt);

    shake *= Math.pow(.001,dt);
    globalFlash *= Math.pow(.001,dt);

    if(p1.hp<=0 || p2.hp<=0){
        endGame();
    }

    updateHUD();
}


/* =========================
   HUD
========================= */

function updateHUD(){
    if(!p1 || !p2) return;

    document.getElementById("p1HP").style.width =
        Math.max(0,p1.hp)+"%";

    document.getElementById("p2HP").style.width =
        Math.max(0,p2.hp)+"%";

    document.getElementById("p1Energy").style.width =
        Math.max(0,p1.energy)+"%";

    document.getElementById("p2Energy").style.width =
        Math.max(0,p2.energy)+"%";

    document.getElementById("p1EnergyNumber").textContent =
        Math.floor(p1.energy);

    document.getElementById("p2EnergyNumber").textContent =
        Math.floor(p2.energy);

    document.getElementById("timer").textContent =
        Math.ceil(timeLeft);
}

function updateAutoButtons(){
    if(!p1 || !p2) return;

    const a=document.getElementById("p1Auto");
    const b=document.getElementById("p2Auto");

    a.textContent=p1.autoEnergy
        ? "⚡ TỰ HỒI: ON"
        : "⚡ TỰ HỒI: OFF";

    b.textContent=p2.autoEnergy
        ? "⚡ TỰ HỒI: ON"
        : "⚡ TỰ HỒI: OFF";

    a.classList.toggle("on",p1.autoEnergy);
    b.classList.toggle("on",p2.autoEnergy);
}


/* =========================
   DRAW BACKGROUND
========================= */

function drawBackground(){
    const g=ctx.createLinearGradient(0,0,0,H);

    g.addColorStop(0,"#030817");
    g.addColorStop(.48,"#0b1430");
    g.addColorStop(1,"#160b18");

    ctx.fillStyle=g;
    ctx.fillRect(0,0,W,H);

    /* moon */
    ctx.save();

    ctx.shadowBlur=45;
    ctx.shadowColor="rgba(190,215,255,.45)";

    ctx.fillStyle="#dceaff";
    ctx.beginPath();
    ctx.arc(W*.78,125,55,0,Math.PI*2);
    ctx.fill();

    ctx.shadowBlur=0;

    ctx.fillStyle="#0b1430";
    ctx.beginPath();
    ctx.arc(W*.805,110,53,0,Math.PI*2);
    ctx.fill();

    ctx.restore();

    /* stars */
    for(let i=0;i<70;i++){
        const x=(i*173)%W;
        const y=(i*71)%(ground-100);
        const r=(i%3)*.45+.5;

        ctx.globalAlpha=.25+(i%4)*.12;
        ctx.fillStyle="#d8e7ff";
        ctx.beginPath();
        ctx.arc(x,y,r,0,Math.PI*2);
        ctx.fill();
    }

    ctx.globalAlpha=1;

    /* mountain layers */
    drawMountain(0,ground-180,W*.33,ground-290,"#0b1730");
    drawMountain(W*.18,ground-170,W*.65,ground-300,"#0a1429");
    drawMountain(W*.45,ground-160,W,ground-275,"#091329");

    /* trees */
    for(let i=0;i<22;i++){
        const x=(i*87)%W;
        const h=65+(i%5)*18;

        ctx.fillStyle="#060c1b";
        ctx.fillRect(x-4,ground-h,8,h);

        ctx.beginPath();
        ctx.moveTo(x,ground-h-55);
        ctx.lineTo(x-30,ground-h+5);
        ctx.lineTo(x+30,ground-h+5);
        ctx.closePath();
        ctx.fill();
    }

    /* warm distant lights */
    for(let i=0;i<14;i++){
        const x=30+i*95;
        const y=ground-45-(i%3)*18;

        ctx.fillStyle="rgba(255,155,65,.7)";
        ctx.shadowBlur=12;
        ctx.shadowColor="#ff8b3d";
        ctx.fillRect(x,y,3,3);
    }

    ctx.shadowBlur=0;
}

function drawMountain(x1,y1,x2,y2,color){
    ctx.fillStyle=color;
    ctx.beginPath();
    ctx.moveTo(x1,H);
    ctx.lineTo(x1,y1);

    const mid=(x1+x2)/2;

    ctx.lineTo(mid,y2);
    ctx.lineTo(x2,y1);
    ctx.lineTo(x2,H);

    ctx.closePath();
    ctx.fill();
}


/* =========================
   DRAW ARENA
========================= */

function drawArena(){
    const floorGrad=ctx.createLinearGradient(0,ground,0,H);

    floorGrad.addColorStop(0,"#11182b");
    floorGrad.addColorStop(1,"#03050b");

    ctx.fillStyle=floorGrad;
    ctx.fillRect(0,ground,W,H-ground);

    /* horizon glow */
    const glow=ctx.createLinearGradient(0,ground-30,0,ground+50);
    glow.addColorStop(0,"rgba(70,130,255,.2)");
    glow.addColorStop(1,"rgba(0,0,0,0)");

    ctx.fillStyle=glow;
    ctx.fillRect(0,ground-40,W,100);

    /* floor grid */
    ctx.strokeStyle="rgba(80,145,220,.12)";
    ctx.lineWidth=1;

    for(let y=ground+10;y<H;y+=22){
        ctx.beginPath();
        ctx.moveTo(0,y);
        ctx.lineTo(W,y);
        ctx.stroke();
    }

    for(let x=-W;x<W*2;x+=55){
        ctx.beginPath();
        ctx.moveTo(W/2,ground);
        ctx.lineTo(x,H);
        ctx.stroke();
    }

    /* center line */
    ctx.strokeStyle="rgba(130,190,255,.2)";
    ctx.lineWidth=2;

    ctx.beginPath();
    ctx.moveTo(W/2,ground);
    ctx.lineTo(W/2,H);
    ctx.stroke();

    /* arena platform */
    ctx.fillStyle="rgba(20,35,62,.7)";
    ctx.beginPath();
    ctx.roundRect(
        W*.12,
        ground-8,
        W*.76,
        18,
        9
    );
    ctx.fill();

    ctx.strokeStyle="rgba(75,160,255,.3)";
    ctx.stroke();
}


/* =========================
   DRAW FIGHTER
========================= */

function drawFighter(f){
    const x=f.x;
    const y=f.y;

    const main=f.side===1 ? "#43dfff" : "#ff603d";
    const dark=f.side===1 ? "#146bb5" : "#a52d1d";
    const glow=f.side===1 ? "#2ddcff" : "#ff4e2e";

    /* shadow */
    ctx.save();

    ctx.globalAlpha=.35;
    ctx.fillStyle="#000";
    ctx.beginPath();
    ctx.ellipse(x,y+5,48,10,0,0,Math.PI*2);
    ctx.fill();

    ctx.restore();

    /* aura */
    if(f.energy>0 || f.autoEnergy){
        ctx.save();

        ctx.globalAlpha=.08 + Math.min(f.energy/100,.2);
        ctx.fillStyle=glow;
        ctx.shadowBlur=45;
        ctx.shadowColor=glow;

        ctx.beginPath();
        ctx.ellipse(
            x,
            y-72,
            55+f.energy*.15,
            100+f.energy*.2,
            0,
            0,
            Math.PI*2
        );
        ctx.fill();

        ctx.restore();
    }

    ctx.save();

    if(f.hitFlash>0){
        ctx.globalAlpha=.8;
    }

    /* legs */
    ctx.strokeStyle=dark;
    ctx.lineWidth=13;
    ctx.lineCap="round";

    ctx.beginPath();
    ctx.moveTo(x-12,y-35);
    ctx.lineTo(x-20,y);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(x+12,y-35);
    ctx.lineTo(x+20,y);
    ctx.stroke();

    /* body */
    ctx.fillStyle=dark;

    ctx.beginPath();
    ctx.roundRect(x-27,y-112,54,78,14);
    ctx.fill();

    /* haori */
    ctx.strokeStyle=main;
    ctx.lineWidth=4;

    ctx.beginPath();
    ctx.moveTo(x-25,y-103);
    ctx.lineTo(x-39,y-45);
    ctx.lineTo(x-23,y-35);

    ctx.moveTo(x+25,y-103);
    ctx.lineTo(x+39,y-45);
    ctx.lineTo(x+23,y-35);

    ctx.stroke();

    /* head */
    ctx.fillStyle="#ffd1b0";
    ctx.beginPath();
    ctx.arc(x,y-137,25,0,Math.PI*2);
    ctx.fill();

    /* hair */
    ctx.fillStyle=f.side===1 ? "#101b31" : "#20131a";

    ctx.beginPath();

    ctx.moveTo(x-25,y-141);
    ctx.lineTo(x-35,y-165);
    ctx.lineTo(x-18,y-157);
    ctx.lineTo(x-10,y-178);
    ctx.lineTo(x,y-158);
    ctx.lineTo(x+14,y-180);
    ctx.lineTo(x+18,y-157);
    ctx.lineTo(x+36,y-165);
    ctx.lineTo(x+25,y-139);

    ctx.closePath();
    ctx.fill();

    /* eye */
    ctx.fillStyle="#111";

    ctx.beginPath();
    ctx.arc(x+f.facing*9,y-137,3,0,Math.PI*2);
    ctx.fill();

    /* arm */
    ctx.strokeStyle="#ffd1b0";
    ctx.lineWidth=12;

    const armDir=f.facing;

    ctx.beginPath();
    ctx.moveTo(x+armDir*19,y-92);
    ctx.lineTo(
        x+armDir*(43+(f.attackAnim>0?22:0)),
        y-65-(f.attackAnim>0?20:0)
    );
    ctx.stroke();

    /* sword */
    const swordX=x+armDir*48;
    const swordY=y-72;

    ctx.save();

    ctx.translate(swordX,swordY);

    if(f.attackAnim>0){
        ctx.rotate(
            armDir *
            (-.65 + f.attackAnim*2.5)
        );
    }else{
        ctx.rotate(armDir*.12);
    }

    ctx.shadowBlur=18;
    ctx.shadowColor=main;

    ctx.strokeStyle="#e8f4ff";
    ctx.lineWidth=5;

    ctx.beginPath();
    ctx.moveTo(0,0);
    ctx.lineTo(0,-75);
    ctx.stroke();

    ctx.strokeStyle=main;
    ctx.lineWidth=2;

    ctx.beginPath();
    ctx.moveTo(0,-5);
    ctx.lineTo(0,-75);
    ctx.stroke();

    ctx.strokeStyle="#e7a94c";
    ctx.lineWidth=7;

    ctx.beginPath();
    ctx.moveTo(-8,0);
    ctx.lineTo(8,0);
    ctx.stroke();

    ctx.restore();

    ctx.restore();

    /* skill aura */
    if(f.skillAnim>0){
        ctx.save();

        ctx.globalAlpha=.55;

        ctx.strokeStyle=main;
        ctx.lineWidth=4;
        ctx.shadowBlur=25;
        ctx.shadowColor=main;

        ctx.beginPath();
        ctx.arc(
            x,
            y-72,
            48,
            -1.8,
            1.1
        );
        ctx.stroke();

        ctx.restore();
    }
}


/* =========================
   DRAW PROJECTILES
========================= */

function drawProjectiles(){
    for(const p of projectiles){
        ctx.save();

        ctx.translate(p.x,p.y);

        const color=p.color;

        ctx.shadowBlur=30;
        ctx.shadowColor=color;

        ctx.strokeStyle=color;
        ctx.lineWidth=p.size;

        ctx.beginPath();
        ctx.moveTo(0,0);
        ctx.lineTo(-p.vx*.08,0);
        ctx.stroke();

        ctx.fillStyle="#fff";

        ctx.beginPath();
        ctx.arc(0,0,p.size*.35,0,Math.PI*2);
        ctx.fill();

        /* water/flame tail */
        ctx.globalAlpha=.45;

        ctx.strokeStyle=color;
        ctx.lineWidth=5;

        for(let i=1;i<5;i++){
            ctx.beginPath();
            ctx.arc(
                -i*9,
                Math.sin(i*1.7)*6,
                5+i,
                0,
                Math.PI*2
            );
            ctx.stroke();
        }

        ctx.restore();
    }
}


/* =========================
   DRAW EFFECTS
========================= */

function drawEffects(){
    for(const e of effects){
        const alpha=Math.max(0,e.life/e.maxLife);

        if(e.type==="ring"){
            ctx.save();

            ctx.globalAlpha=alpha;
            ctx.strokeStyle=e.color;
            ctx.lineWidth=4;
            ctx.shadowBlur=25;
            ctx.shadowColor=e.color;

            ctx.beginPath();
            ctx.arc(e.x,e.y,e.size,0,Math.PI*2);
            ctx.stroke();

            ctx.restore();
        }

        if(e.type==="ultimate"){
            ctx.save();

            ctx.globalAlpha=alpha*.7;

            const g=ctx.createRadialGradient(
                e.x,e.y,10,
                e.x,e.y,250
            );

            g.addColorStop(0,e.color);
            g.addColorStop(.25,"rgba(255,255,255,.6)");
            g.addColorStop(1,"rgba(0,0,0,0)");

            ctx.fillStyle=g;
            ctx.beginPath();
            ctx.arc(e.x,e.y,250,0,Math.PI*2);
            ctx.fill();

            ctx.restore();
        }
    }

    for(const s of slashWaves){
        const alpha=s.life/s.maxLife;

        ctx.save();

        ctx.globalAlpha=alpha;
        ctx.translate(s.x,s.y);

        if(s.dir<0) ctx.scale(-1,1);

        ctx.strokeStyle=s.color;
        ctx.lineWidth=s.large?9:5;
        ctx.shadowBlur=25;
        ctx.shadowColor=s.color;

        ctx.beginPath();

        if(s.large){
            ctx.arc(0,0,170,-1.0,.9);
        }else{
            ctx.arc(0,0,85,-.9,.7);
        }

        ctx.stroke();

        ctx.restore();
    }
}

function drawParticles(){
    for(const p of particles){
        ctx.save();

        ctx.globalAlpha=Math.max(0,p.life/p.max);
        ctx.fillStyle=p.color;
        ctx.shadowBlur=10;
        ctx.shadowColor=p.color;

        ctx.beginPath();
        ctx.arc(p.x,p.y,p.size,0,Math.PI*2);
        ctx.fill();

        ctx.restore();
    }
}


/* =========================
   DRAW
========================= */

function draw(){
    ctx.clearRect(0,0,W,H);

    ctx.save();

    if(shake>0){
        ctx.translate(
            (Math.random()-.5)*shake,
            (Math.random()-.5)*shake
        );
    }

    drawBackground();
    drawArena();

    drawFighter(p1);
    drawFighter(p2);

    drawProjectiles();
    drawEffects();
    drawParticles();

    ctx.restore();

    if(globalFlash>0){
        ctx.fillStyle=`rgba(255,255,255,${Math.min(.45,globalFlash)})`;
        ctx.fillRect(0,0,W,H);
    }
}


/* =========================
   GAME END
========================= */

function endGame(){
    if(finished) return;

    finished=true;
    running=false;

    let winner="DRAW";
    let info="Hết thời gian!";

    if(p1.hp>p2.hp){
        winner="PLAYER 1 WINS";
        info="Hơi Thở Nước đã chiếm ưu thế!";
        soundWin();
    }else if(p2.hp>p1.hp){
        winner="PLAYER 2 WINS";
        info="Hơi Thở Lửa đã bùng cháy đến cuối!";
        soundWin();
    }else{
        tone(220,.4,"triangle",.05,-100);
    }

    document.getElementById("winner").textContent=winner;
    document.getElementById("resultInfo").textContent=info;
    document.getElementById("resultOverlay").style.display="flex";
}


/* =========================
   COUNTDOWN
========================= */

function countdown(){
    countdownActive=true;

    const box=document.getElementById("countdown");

    let n=3;

    box.style.display="grid";
    box.textContent=n;

    tone(500,.12,"square",.05);

    const interval=setInterval(()=>{
        n--;

        if(n>0){
            box.textContent=n;
            tone(500,.12,"square",.05);
        }else{
            clearInterval(interval);

            box.textContent="FIGHT!";
            tone(850,.2,"triangle",.06,300);

            setTimeout(()=>{
                box.style.display="none";
                countdownActive=false;
                running=true;
                game.focus();
            },650);
        }
    },850);
}


/* =========================
   RESET
========================= */

function resetGame(){
    resize();

    p1=makeFighter(W*.28,1,"water");
    p2=makeFighter(W*.72,2,"fire");

    projectiles=[];
    effects=[];
    particles=[];
    slashWaves=[];

    timeLeft=60;
    running=false;
    finished=false;

    document.getElementById("resultOverlay").style.display="none";
    document.getElementById("startOverlay").style.display="none";

    updateHUD();
    updateAutoButtons();

    countdown();
}


/* =========================
   KEYBOARD
========================= */

window.addEventListener("keydown",(e)=>{
    const k=e.key;

    keys[k]=true;
    keys[k.toLowerCase()]=true;

    if([
        "ArrowLeft",
        "ArrowRight",
        "ArrowUp",
        " "
    ].includes(k)){
        e.preventDefault();
    }

    if(!running || finished) return;

    if(k.toLowerCase()==="f"){
        normalAttack(p1,p2);
    }

    if(k.toLowerCase()==="g"){
        skill(p1,p2);
    }

    if(k.toLowerCase()==="h"){
        ultimate(p1,p2);
    }

    if(k.toLowerCase()==="k"){
        normalAttack(p2,p1);
    }

    if(k.toLowerCase()==="l"){
        skill(p2,p1);
    }

    if(k.toLowerCase()==="o"){
        ultimate(p2,p1);
    }
});

window.addEventListener("keyup",(e)=>{
    keys[e.key]=false;
    keys[e.key.toLowerCase()]=false;
});


/* =========================
   BUTTONS
========================= */

document.getElementById("startButton").addEventListener("click",()=>{
    initAudio();
    resetGame();
});

document.getElementById("restartButton").addEventListener("click",()=>{
    initAudio();
    resetGame();
});

document.getElementById("p1Auto").addEventListener("click",(e)=>{
    e.stopPropagation();

    if(!p1) return;

    initAudio();

    p1.autoEnergy=!p1.autoEnergy;

    updateAutoButtons();

    if(p1.autoEnergy) soundEnergy();

    setTimeout(()=>game.focus(),50);
});

document.getElementById("p2Auto").addEventListener("click",(e)=>{
    e.stopPropagation();

    if(!p2) return;

    initAudio();

    p2.autoEnergy=!p2.autoEnergy;

    updateAutoButtons();

    if(p2.autoEnergy) soundEnergy();

    setTimeout(()=>game.focus(),50);
});

document.getElementById("mute").addEventListener("click",(e)=>{
    e.stopPropagation();

    muted=!muted;

    document.getElementById("mute").textContent =
        muted ? "🔇 MUTED" : "🔊 SOUND";

    if(!muted){
        initAudio();
        tone(500,.1,"triangle",.04);
    }
});


/* =========================
   LOOP
========================= */

function loop(t){
    if(!lastTime) lastTime=t;

    let dt=(t-lastTime)/1000;

    lastTime=t;

    dt=Math.min(dt,.033);

    update(dt);

    draw();

    requestAnimationFrame(loop);
}


/* =========================
   START
========================= */

initPlayers();
updateHUD();
draw();
requestAnimationFrame(loop);

})();
</script>

</body>
</html>
"""

components.html(
    GAME_HTML,
    height=760,
    scrolling=False
)
