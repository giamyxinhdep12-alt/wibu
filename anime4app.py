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
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<style>
html,body{
    margin:0;
    padding:0;
    width:100%;
    height:100%;
    overflow:hidden;
    background:#05060b;
    font-family:Arial,sans-serif
}
*{
    box-sizing:border-box;
    user-select:none
}
#game{
    position:fixed;
    inset:0;
    width:100vw;
    height:100vh
}
#hud{
    position:fixed;
    top:10px;
    left:50%;
    transform:translateX(-50%);
    width:min(1200px,94vw);
    z-index:20;
    pointer-events:none
}
#top{
    display:grid;
    grid-template-columns:1fr 90px 1fr;
    gap:10px;
    align-items:center
}
.sidebox{
    background:rgba(5,7,13,.82);
    padding:7px;
    border:1px solid rgba(255,255,255,.3);
    border-radius:8px
}
.name{
    color:white;
    font-weight:900;
    font-size:13px;
    margin-bottom:4px
}
.bar{
    height:22px;
    background:#10121a;
    border:1px solid #fff;
    border-radius:5px;
    overflow:hidden
}
.fill{
    height:100%;
    width:100%;
    transition:width .08s linear
}
#hp1{
    background:linear-gradient(90deg,#00a6bd,#45f3ff)
}
#hp2{
    background:linear-gradient(90deg,#e72e14,#ffbf32)
}
.energy{
    height:6px;
    margin-top:5px;
    background:#151820;
    border-radius:4px;
    overflow:hidden
}
.efill{
    height:100%;
    width:0
}
#en1{
    background:#38e8ff
}
#en2{
    background:#ff682e
}
#timer{
    text-align:center;
    color:#fff;
    font-size:28px;
    font-weight:900;
    text-shadow:0 0 12px #fff
}
#mute{
    position:fixed;
    right:14px;
    top:12px;
    z-index:60;
    background:#0b0d14;
    color:#fff;
    border:1px solid #777;
    border-radius:8px;
    padding:8px 11px;
    cursor:pointer
}
#mode{
    position:fixed;
    inset:0;
    z-index:50;
    display:flex;
    align-items:center;
    justify-content:center;
    background:radial-gradient(circle,rgba(24,38,76,.6),rgba(0,0,0,.94))
}
.panel{
    width:min(760px,92vw);
    padding:30px;
    border-radius:20px;
    text-align:center;
    color:#fff;
    background:rgba(7,9,17,.97);
    border:1px solid rgba(255,255,255,.35);
    box-shadow:0 0 70px #000
}
.panel h1{
    font-size:46px;
    margin:0 0 5px;
    letter-spacing:2px
}
.panel h2{
    margin:5px 0 20px;
    color:#bbb
}
.modes{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:14px
}
.mode{
    padding:22px 14px;
    border-radius:14px;
    background:#111521;
    border:1px solid #454b5d;
    color:#fff;
    cursor:pointer;
    transition:.15s
}
.mode:hover{
    transform:translateY(-3px);
    border-color:#fff;
    background:#171c2b
}
.mode b{
    display:block;
    font-size:22px;
    margin-bottom:8px
}
.mode span{
    color:#aaa;
    font-size:13px;
    line-height:1.5
}
#count{
    position:fixed;
    inset:0;
    z-index:40;
    display:none;
    align-items:center;
    justify-content:center;
    color:#fff;
    font-size:110px;
    font-weight:900;
    text-shadow:0 0 20px #fff;
    pointer-events:none
}
#result{
    position:fixed;
    inset:0;
    z-index:55;
    display:none;
    align-items:center;
    justify-content:center;
    background:rgba(0,0,0,.72)
}
.resultbox{
    padding:36px 55px;
    border-radius:18px;
    background:#090b12;
    color:#fff;
    text-align:center;
    border:1px solid #777
}
.resultbox h1{
    font-size:48px;
    margin:0 0 20px
}
.btn{
    border:0;
    border-radius:9px;
    padding:12px 25px;
    font-size:16px;
    font-weight:900;
    cursor:pointer
}
#controls{
    position:fixed;
    bottom:8px;
    left:50%;
    transform:translateX(-50%);
    color:#aaa;
    font-size:11px;
    z-index:15;
    text-align:center;
    pointer-events:none
}
@media(max-width:700px){
    .modes{
        grid-template-columns:1fr
    }
    .panel h1{
        font-size:34px
    }
    .panel{
        padding:22px
    }
}
</style>
</head>

<body>

<canvas id="game"></canvas>

<div id="hud">
    <div id="top">

        <div class="sidebox">
            <div class="name" id="leftName">WATER TEAM</div>

            <div class="bar">
                <div id="hp1" class="fill"></div>
            </div>

            <div class="energy">
                <div id="en1" class="efill"></div>
            </div>
        </div>

        <div id="timer">60</div>

        <div class="sidebox">
            <div class="name" id="rightName" style="text-align:right">
                FLAME TEAM
            </div>

            <div class="bar">
                <div id="hp2" class="fill"></div>
            </div>

            <div class="energy">
                <div id="en2" class="efill"></div>
            </div>
        </div>

    </div>
</div>

<button id="mute">🔊</button>

<div id="count"></div>

<div id="mode">

    <div class="panel">

        <h1>⚔️ ANIME CLASH</h1>

        <h2>CHỌN CHẾ ĐỘ ĐẤU</h2>

        <div class="modes">

            <button class="mode" onclick="chooseMode('cpu')">

                <b>🤖 ĐẤU VỚI MÁY</b>

                <span>
                    1 người chơi đấu với CPU.<br>
                    CPU tự di chuyển, né và dùng kỹ năng.
                </span>

            </button>

            <button class="mode" onclick="chooseMode('2v2')">

                <b>⚔️ ĐẤU 2V2</b>

                <span>
                    Mỗi đội có 2 chiến binh.<br>
                    Đồng đội AI tự chiến đấu cùng bạn.
                </span>

            </button>

        </div>

        <p style="color:#999;margin-top:20px">
            P1:
            A/D di chuyển · W nhảy · S rơi nhanh ·
            J đánh · K skill · L dash · U heavy ·
            I ultimate · O hồi máu · P power
        </p>

        <p style="color:#777;font-size:12px">
            P2 khi đấu 2V2:
            ←/→ ↑/↓ và 1 2 3 4 5 6 7
        </p>

    </div>

</div>

<div id="result">

    <div class="resultbox">

        <h1 id="resultTitle"></h1>

        <p id="resultInfo"></p>

        <button class="btn" onclick="location.reload()">
            🔄 ĐẤU LẠI
        </button>

    </div>

</div>

<div id="controls">
    WATER:
    A D W S J K L U I O P
    &nbsp; | &nbsp;
    FLAME:
    ← → ↑ ↓ 1 2 3 4 5 6 7
</div>

<script>

"use strict";

const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");

let W = innerWidth;
let H = innerHeight;
let DPR = devicePixelRatio || 1;

function resize(){

    W = innerWidth;
    H = innerHeight;
    DPR = devicePixelRatio || 1;

    canvas.width = W * DPR;
    canvas.height = H * DPR;

    canvas.style.width = W + "px";
    canvas.style.height = H + "px";

    ctx.setTransform(DPR,0,0,DPR,0,0);
}

addEventListener("resize",resize);

resize();

const keys = {};
const just = {};

addEventListener("keydown",e=>{

    const k = e.key.toLowerCase();

    keys[k] = true;

    if(!just[k]){
        just[k] = true;
    }

    if([
        "arrowleft",
        "arrowright",
        "arrowup",
        "arrowdown",
        " ",
        "w",
        "a",
        "s",
        "d",
        "j",
        "k",
        "l",
        "u",
        "i",
        "o",
        "p"
    ].includes(k)){
        e.preventDefault();
    }

});

addEventListener("keyup",e=>{
    keys[e.key.toLowerCase()] = false;
});

function down(k){
    return !!keys[k];
}

let mode = null;
let started = false;
let ended = false;

let timeLeft = 60;

let last = performance.now();

let shake = 0;
let hitStop = 0;
let muted = false;

const particles = [];
const slashes = [];
const waves = [];
const texts = [];
const shots = [];

function clamp(v,a,b){
    return Math.max(a,Math.min(b,v));
}

function rand(a,b){
    return Math.random()*(b-a)+a;
}

function part(x,y,c,n=12,p=5){

    for(let i=0;i<n;i++){

        particles.push({

            x:x,
            y:y,

            vx:rand(-p,p),
            vy:rand(-p,p),

            life:rand(.3,.8),

            size:rand(2,6),

            c:c

        });

    }

}

function txt(x,y,t,c){

    texts.push({

        x:x,
        y:y,

        t:t,
        c:c,

        life:1

    });

}

function wave(x,y,c){

    waves.push({

        x:x,
        y:y,

        r:8,

        life:.45,

        c:c

    });

}

function slash(x,y,d,c,s=1){

    slashes.push({

        x:x,
        y:y,

        d:d,

        c:c,

        s:s,

        a:d===1
            ?rand(-.7,.7)
            :Math.PI+rand(-.7,.7),

        life:.25

    });

}

function water(x,y,d){

    for(let i=0;i<20;i++){

        particles.push({

            x:x,
            y:y,

            vx:d*rand(2,7),
            vy:rand(-4,4),

            life:rand(.3,.7),

            size:rand(5,13),

            c:"#35eaff"

        });

    }

}

function fire(x,y,d){

    for(let i=0;i<24;i++){

        particles.push({

            x:x,
            y:y,

            vx:d*rand(2,8),
            vy:rand(-5,3),

            life:rand(.25,.65),

            size:rand(5,14),

            c:Math.random()>.4
                ?"#ff4b20"
                :"#ffc02e"

        });

    }

}

class Fighter{

    constructor(
        id,
        team,
        x,
        color,
        accent,
        name,
        ai=false
    ){

        this.id=id;

        this.team=team;

        this.x=x;

        this.color=color;

        this.accent=accent;

        this.name=name;

        this.ai=ai;

        this.hp=100;

        this.energy=0;

        this.y=0;

        this.vx=0;

        this.vy=0;

        this.ground=true;

        this.facing=team===1?1:-1;

        this.attackCd=0;
        this.skillCd=0;
        this.dashCd=0;
        this.heavyCd=0;
        this.ultCd=0;
        this.recoverCd=0;
        this.powerCd=0;

        this.anim=0;

        this.state="idle";

        this.hit=0;

        this.inv=0;

        this.aiThink=0;

    }

    groundY(){

        return H-145;

    }

    reset(x){

        this.x=x;

        this.hp=100;

        this.energy=0;

        this.y=0;

        this.vx=0;

        this.vy=0;

        this.ground=true;

    }

    input(){

        if(this.ai){

            this.cpu();

            return;

        }

        const p1=this.team===1;

        const L=p1
            ?down("a")
            :down("arrowleft");

        const R=p1
            ?down("d")
            :down("arrowright");

        if(L){

            this.vx-=1.15;
            this.facing=-1;

        }

        if(R){

            this.vx+=1.15;
            this.facing=1;

        }

        if(!L&&!R){

            this.vx*=.78;

        }

        this.vx=clamp(this.vx,-7,7);

        if(
            (p1?down("w"):down("arrowup"))
            &&
            this.ground
        ){

            this.vy=-14;
            this.ground=false;

        }

        if(
            p1?down("s"):down("arrowdown")
        ){

            if(!this.ground){

                this.vy+=1.8;

            }

        }

        if(p1?down("j"):down("1"))
            this.attack();

        if(p1?down("k"):down("2"))
            this.skill();

        if(p1?down("l"):down("3"))
            this.dash();

        if(p1?down("u"):down("4"))
            this.heavy();

        if(p1?down("i"):down("5"))
            this.ultimate();

        if(p1?down("o"):down("6"))
            this.recover();

        if(p1?down("p"):down("7"))
            this.power();

    }

    cpu(){

        const enemies=fighters.filter(
            f=>f.team!==this.team&&f.hp>0
        );

        if(!enemies.length)
            return;

        let target=enemies.reduce(
            (a,b)=>
                Math.abs(a.x-this.x)
                <
                Math.abs(b.x-this.x)
                ?a:b
        );

        const dx=target.x-this.x;

        const ad=Math.abs(dx);

        this.facing=dx>=0?1:-1;

        if(ad>170){

            this.vx+=this.facing*.9;

        }
        else{

            this.vx*=.8;

        }

        this.vx=clamp(
            this.vx,
            -5.5,
            5.5
        );

        this.aiThink-=.016;

        if(this.aiThink<=0){

            this.aiThink=rand(.18,.42);

            if(ad<90)
                this.attack();

            else if(
                ad<260 &&
                this.energy>=20
            )
                this.skill();

            if(
                ad<130 &&
                this.energy>=30 &&
                Math.random()<.35
            )
                this.heavy();

            if(
                this.energy>=100 &&
                ad<280 &&
                Math.random()<.3
            )
                this.ultimate();

            if(
                Math.random()<.18 &&
                this.dashCd<=0
            )
                this.dash();

            if(
                this.hp<35 &&
                this.energy>=15 &&
                Math.random()<.25
            )
                this.recover();

        }

        if(
            this.ground &&
            Math.random()<.008 &&
            ad<180
        ){

            this.vy=-14;
            this.ground=false;

        }

    }

    cooldowns(dt){

        for(
            const k of [
                "attackCd",
                "skillCd",
                "dashCd",
                "heavyCd",
                "ultCd",
                "recoverCd",
                "powerCd",
                "hit",
                "inv"
            ]
        ){

            this[k]=Math.max(
                0,
                this[k]-dt
            );

        }

        this.energy=clamp(
            this.energy+dt*5.5,
            0,
            100
        );

        this.anim+=dt*10;

    }

    attack(){

        if(this.attackCd>0)
            return;

        this.attackCd=.28;

        this.state="attack";

        slash(
            this.x+this.facing*40,
            this.groundY()+this.y-65,
            this.facing,
            this.color
        );

        part(
            this.x+this.facing*55,
            this.groundY()+this.y-65,
            this.color,
            10,
            4
        );

        if(this.team===1)
            water(
                this.x+this.facing*35,
                this.groundY()+this.y-60,
                this.facing
            );
        else
            fire(
                this.x+this.facing*35,
                this.groundY()+this.y-60,
                this.facing
            );

        hit(this,10,82);

    }

    skill(){

        if(
            this.skillCd>0 ||
            this.energy<20
        )
            return;

        this.energy-=20;

        this.skillCd=.9;

        this.state="skill";

        const x=
            this.x+
            this.facing*65;

        const y=
            this.groundY()+
            this.y-
            65;

        shots.push({

            x:x,
            y:y,

            vx:this.facing*10,

            c:this.color,

            damage:18,

            team:this.team,

            life:1.5,

            size:18

        });

        wave(x,y,this.color);

        txt(
            this.x,
            this.groundY()+this.y-125,
            this.team===1
                ?"WATER STYLE!"
                :"FLAME STYLE!",
            this.color
        );

    }

    dash(){

        if(this.dashCd>0)
            return;

        const old=this.x;

        this.dashCd=.7;

        this.state="dash";

        this.x=clamp(
            this.x+
            this.facing*115,
            45,
            W-45
        );

        part(
            old,
            this.groundY()+this.y-40,
            this.color,
            25,
            6
        );

        wave(
            this.x,
            this.groundY()+this.y-55,
            this.color
        );

        hit(this,8,75);

    }

    heavy(){

        if(
            this.heavyCd>0 ||
            this.energy<30
        )
            return;

        this.energy-=30;

        this.heavyCd=1;

        this.state="heavy";

        shake=10;

        slash(
            this.x+this.facing*65,
            this.groundY()+this.y-65,
            this.facing,
            this.color,
            1.8
        );

        part(
            this.x+this.facing*70,
            this.groundY()+this.y-65,
            this.color,
            30,
            8
        );

        hit(this,28,125);

    }

    ultimate(){

        if(
            this.ultCd>0 ||
            this.energy<100
        )
            return;

        this.energy=0;

        this.ultCd=3;

        this.state="ultimate";

        shake=20;

        wave(
            this.x,
            this.groundY()+this.y-65,
            this.color
        );

        part(
            this.x,
            this.groundY()+this.y-65,
            this.color,
            55,
            10
        );

        hit(this,55,260);

        flash(this.color);

    }

    recover(){

        if(
            this.recoverCd>0 ||
            this.energy<15
        )
            return;

        this.energy-=15;

        this.recoverCd=1.2;

        this.hp=clamp(
            this.hp+7,
            0,
            100
        );

        txt(
            this.x,
            this.groundY()+this.y-125,
            "+7 HP",
            "#8aff9a"
        );

        part(
            this.x,
            this.groundY()+this.y-60,
            "#8aff9a",
            20,
            3
        );

    }

    power(){

        if(
            this.powerCd>0 ||
            this.energy<50
        )
            return;

        this.energy-=50;

        this.powerCd=2;

        this.hp=clamp(
            this.hp+15,
            0,
            100
        );

        txt(
            this.x,
            this.groundY()+this.y-135,
            "POWER UP!",
            "#fff"
        );

        wave(
            this.x,
            this.groundY()+this.y-60,
            "#fff"
        );

    }

    update(dt){

        if(this.hp<=0)
            return;

        this.cooldowns(dt);

        this.input();

        this.vy+=.65;

        this.y+=this.vy;

        if(this.y>=0){

            this.y=0;

            this.vy=0;

            this.ground=true;

        }
        else{

            this.ground=false;

        }

        this.x+=this.vx;

        this.x=clamp(
            this.x,
            40,
            W-40
        );

        if(Math.abs(this.vx)<.4)
            this.vx=0;

        this.state=
            this.ultCd>2.7
            ?"ultimate"
            :
            this.heavyCd>.8
            ?"heavy"
            :
            this.skillCd>.7
            ?"skill"
            :
            this.dashCd>.5
            ?"dash"
            :
            !this.ground
            ?"jump"
            :
            Math.abs(this.vx)>1
            ?"run"
            :
            "idle";

    }

    draw(){

        if(this.hp<=0)
            return;

        const x=this.x;

        const y=
            this.groundY()+
            this.y;

        const bob=
            this.state==="run"
            ?Math.sin(this.anim*1.8)*4
            :Math.sin(this.anim)*2;

        const by=
            y-62+bob;

        ctx.save();

        if(this.hit>0){

            ctx.globalAlpha=
                Math.floor(this.hit*35)%2
                ?.45
                :1;

        }

        if(this.energy>=100){

            ctx.globalAlpha=.22;

            ctx.strokeStyle=this.color;

            ctx.lineWidth=8;

            ctx.beginPath();

            ctx.arc(
                x,
                by-5,
                70+Math.sin(this.anim)*8,
                0,
                Math.PI*2
            );

            ctx.stroke();

            ctx.globalAlpha=1;

        }

        ctx.fillStyle="rgba(0,0,0,.55)";

        ctx.beginPath();

        ctx.ellipse(
            x,
            y+5,
            44,
            9,
            0,
            0,
            Math.PI*2
        );

        ctx.fill();

        let a=
            Math.sin(this.anim*1.7)*14;

        ctx.strokeStyle="#17171d";

        ctx.lineWidth=13;

        ctx.lineCap="round";

        ctx.beginPath();

        ctx.moveTo(
            x-12,
            by+38
        );

        ctx.lineTo(
            x-16+
            (this.state==="run"?a:0),
            by+73
        );

        ctx.moveTo(
            x+12,
            by+38
        );

        ctx.lineTo(
            x+16+
            (this.state==="run"?-a:0),
            by+73
        );

        ctx.stroke();

        ctx.fillStyle=this.color;

        round(
            x-26,
            by-4,
            52,
            56,
            12
        );

        ctx.fill();

        ctx.fillStyle="#15151b";

        ctx.fillRect(
            x-28,
            by+31,
            56,
            8
        );

        ctx.fillStyle="#ffd1b3";

        ctx.beginPath();

        ctx.arc(
            x,
            by-28,
            24,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.fillStyle=
            this.team===1
            ?"#0c6473"
            :"#74200d";

        ctx.beginPath();

        ctx.arc(
            x,
            by-36,
            26,
            Math.PI,
            Math.PI*2
        );

        ctx.lineTo(
            x+21,
            by-44
        );

        ctx.lineTo(
            x+8,
            by-56
        );

        ctx.lineTo(
            x-5,
            by-45
        );

        ctx.lineTo(
            x-20,
            by-54
        );

        ctx.closePath();

        ctx.fill();

        ctx.fillStyle="#111";

        ctx.beginPath();

        ctx.arc(
            x-8,
            by-28,
            3,
            0,
            Math.PI*2
        );

        ctx.arc(
            x+8,
            by-28,
            3,
            0,
            Math.PI*2
        );

        ctx.fill();

        ctx.strokeStyle=this.color;

        ctx.lineWidth=11;

        ctx.beginPath();

        ctx.moveTo(
            x+this.facing*14,
            by+5
        );

        ctx.lineTo(
            x+
            this.facing*
            (
                this.state==="attack" ||
                this.state==="heavy"
                ?48
                :38
            ),
            by+
            (
                this.state==="attack" ||
                this.state==="heavy"
                ?-20
                :24
            )
        );

        ctx.stroke();

        ctx.strokeStyle="#e8eef2";

        ctx.lineWidth=
            this.state==="heavy"
            ?8
            :6;

        ctx.beginPath();

        ctx.moveTo(
            x+this.facing*22,
            by+4
        );

        ctx.lineTo(
            x+this.facing*70,
            by-60
        );

        ctx.stroke();

        ctx.font="bold 12px Arial";

        ctx.textAlign="center";

        ctx.fillStyle="#fff";

        ctx.fillText(
            this.name,
            x,
            by-86
        );

        ctx.restore();

    }

}

function round(x,y,w,h,r){

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

let fighters=[];

let p1,p2,p3,p4;

function setup(modeName){

    mode=modeName;

    fighters=[];

    p1=new Fighter(
        "p1",
        1,
        W*.25,
        "#21ddec",
        "#bafaff",
        "WATER",
        false
    );

    if(mode==="cpu"){

        p2=new Fighter(
            "p2",
            2,
            W*.75,
            "#ff5528",
            "#ffd0a0",
            "CPU",
            true
        );

        fighters=[
            p1,
            p2
        ];

    }
    else{

        p2=new Fighter(
            "p2",
            2,
            W*.72,
            "#ff5528",
            "#ffd0a0",
            "FLAME",
            false
        );

        p3=new Fighter(
            "p3",
            1,
            W*.15,
            "#6aa9ff",
            "#fff",
            "WATER AI",
            true
        );

        p4=new Fighter(
            "p4",
            2,
            W*.85,
            "#ff8b3d",
            "#fff",
            "FLAME AI",
            true
        );

        fighters=[
            p1,
            p2,
            p3,
            p4
        ];

    }

    started=false;

    ended=false;

    timeLeft=60;

    document.getElementById("leftName").textContent=
        mode==="2v2"
        ?"WATER TEAM"
        :"WATER";

    document.getElementById("rightName").textContent=
        mode==="2v2"
        ?"FLAME TEAM"
        :"CPU";

    document.getElementById("mode").style.display="none";

    countdown();

}

function chooseMode(m){

    setup(m);

}

function countdown(){

    const el=
        document.getElementById("count");

    el.style.display="flex";

    let n=3;

    el.textContent=n;

    const id=setInterval(()=>{

        n--;

        if(n>0){

            el.textContent=n;

        }
        else{

            el.textContent="FIGHT!";

            setTimeout(
                ()=>el.style.display="none",
                450
            );

            started=true;

            clearInterval(id);

        }

    },700);

}

function enemies(attacker){

    return fighters.filter(
        f=>
            f.team!==attacker.team &&
            f.hp>0
    );

}

function hit(attacker,damage,range){

    const es=enemies(attacker);

    if(!es.length)
        return;

    const target=
        es.reduce(
            (a,b)=>
                Math.abs(a.x-attacker.x)
                <
                Math.abs(b.x-attacker.x)
                ?a:b
        );

    if(
        Math.abs(target.x-attacker.x)<=range &&
        Math.abs(target.y-attacker.y)<105 &&
        target.inv<=0
    ){

        target.hp=
            clamp(
                target.hp-damage,
                0,
                100
            );

        target.inv=.22;

        target.hit=.18;

        target.vx+=
            attacker.facing*
            damage*
            .13;

        target.vy-=2;

        shake=
            Math.max(
                shake,
                damage>40?18:5
            );

        hitStop=.035;

        part(
            target.x,
            target.groundY()+
            target.y-
            60,
            attacker.color,
            damage>40?40:18,
            6
        );

        txt(
            target.x,
            target.groundY()+
            target.y-
            115,
            "-"+damage,
            attacker.color
        );

    }

}

function updateShots(dt){

    for(
        let i=shots.length-1;
        i>=0;
        i--
    ){

        const s=shots[i];

        s.x+=s.vx;

        s.life-=dt;

        const es=
            fighters.filter(
                f=>
                    f.team!==s.team &&
                    f.hp>0
            );

        let hitOne=false;

        for(const t of es){

            if(
                Math.abs(t.x-s.x)<42 &&
                t.inv<=0
            ){

                t.hp=
                    clamp(
                        t.hp-s.damage,
                        0,
                        100
                    );

                t.inv=.2;

                t.hit=.2;

                part(
                    t.x,
                    t.groundY()-60,
                    s.c,
                    20,
                    5
                );

                txt(
                    t.x,
                    t.groundY()-115,
                    "-"+s.damage,
                    s.c
                );

                hitOne=true;

                break;

            }

        }

        if(
            hitOne ||
            s.life<=0 ||
            s.x<-100 ||
            s.x>W+100
        ){

            shots.splice(i,1);

        }

    }

}

function effects(dt){

    for(
        let i=particles.length-1;
        i>=0;
        i--
    ){

        const p=particles[i];

        p.x+=p.vx;

        p.y+=p.vy;

        p.vy+=.08;

        p.life-=dt;

        if(p.life<=0)
            particles.splice(i,1);

    }

    for(
        let i=slashes.length-1;
        i>=0;
        i--
    ){

        slashes[i].life-=dt;

        if(slashes[i].life<=0)
            slashes.splice(i,1);

    }

    for(
        let i=waves.length-1;
        i>=0;
        i--
    ){

        waves[i].r+=300*dt;

        waves[i].life-=dt;

        if(waves[i].life<=0)
            waves.splice(i,1);

    }

    for(
        let i=texts.length-1;
        i>=0;
        i--
    ){

        let t=texts[i];

        t.y-=35*dt;

        t.life-=dt;

        if(t.life<=0)
            texts.splice(i,1);

    }

}

function drawEffects(){

    for(const p of particles){

        ctx.globalAlpha=
            clamp(
                p.life/.8,
                0,
                1
            );

        ctx.fillStyle=p.c;

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

    for(const s of slashes){

        ctx.save();

        ctx.translate(
            s.x,
            s.y
        );

        ctx.rotate(s.a);

        ctx.globalAlpha=
            clamp(
                s.life/.25,
                0,
                1
            );

        ctx.strokeStyle=s.c;

        ctx.lineWidth=
            7*s.s;

        ctx.beginPath();

        ctx.arc(
            0,
            0,
            55*s.s,
            -.7,
            .7
        );

        ctx.stroke();

        ctx.restore();

    }

    for(const w of waves){

        ctx.globalAlpha=
            clamp(
                w.life/.45,
                0,
                1
            );

        ctx.strokeStyle=w.c;

        ctx.lineWidth=5;

        ctx.beginPath();

        ctx.arc(
            w.x,
            w.y,
            w.r,
            0,
            Math.PI*2
        );

        ctx.stroke();

    }

    for(const s of shots){

        ctx.globalAlpha=.8;

        ctx.fillStyle=s.c;

        ctx.beginPath();

        ctx.arc(
            s.x,
            s.y,
            s.size,
            0,
            Math.PI*2
        );

        ctx.fill();

    }

    for(const t of texts){

        ctx.globalAlpha=
            clamp(
                t.life,
                0,
                1
            );

        ctx.fillStyle=t.c;

        ctx.font="900 20px Arial";

        ctx.textAlign="center";

        ctx.fillText(
            t.t,
            t.x,
            t.y
        );

    }

    ctx.globalAlpha=1;

}

function background(){

    const g=
        ctx.createLinearGradient(
            0,
            0,
            0,
            H
        );

    g.addColorStop(
        0,
        "#030617"
    );

    g.addColorStop(
        .55,
        "#101c3c"
    );

    g.addColorStop(
        1,
        "#070812"
    );

    ctx.fillStyle=g;

    ctx.fillRect(
        0,
        0,
        W,
        H
    );

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

    for(let i=0;i<80;i++){

        ctx.fillStyle=
            `rgba(255,255,255,${.25+.25*Math.sin(i)})`;

        ctx.fillRect(
            (i*193)%W,
            (i*73)%(H*.55),
            2,
            2
        );

    }

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

        ctx.lineTo(
            x,
            H-230-
            (
                60+
                40*Math.sin(x*.013)
            )
        );

    }

    ctx.lineTo(W,H);

    ctx.lineTo(0,H);

    ctx.fill();

    const floor=H-145;

    ctx.fillStyle="#11141e";

    ctx.fillRect(
        0,
        floor,
        W,
        H-floor
    );

    ctx.strokeStyle=
        "rgba(100,130,170,.2)";

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

}

function updateHUD(){

    const t1=
        fighters.filter(
            f=>f.team===1
        );

    const t2=
        fighters.filter(
            f=>f.team===2
        );

    const hp1=
        t1.reduce(
            (s,f)=>s+f.hp,
            0
        )/
        (100*t1.length)*
        100;

    const hp2=
        t2.reduce(
            (s,f)=>s+f.hp,
            0
        )/
        (100*t2.length)*
        100;

    document.getElementById(
        "hp1"
    ).style.width=hp1+"%";

    document.getElementById(
        "hp2"
    ).style.width=hp2+"%";

    document.getElementById(
        "en1"
    ).style.width=
        (p1?p1.energy:0)+"%";

    document.getElementById(
        "en2"
    ).style.width=
        (p2?p2.energy:0)+"%";

    document.getElementById(
        "timer"
    ).textContent=
        Math.max(
            0,
            Math.ceil(timeLeft)
        );

}

function flash(c){

    document.body.style.boxShadow=
        "inset 0 0 120px "+c;

    setTimeout(
        ()=>{
            document.body.style.boxShadow="";
        },
        180
    );

}

function alive(team){

    return fighters.some(
        f=>
            f.team===team &&
            f.hp>0
    );

}

function finish(title){

    if(ended)
        return;

    ended=true;

    started=false;

    document.getElementById(
        "resultTitle"
    ).textContent=title;

    const a=
        fighters
        .filter(f=>f.team===1)
        .reduce(
            (s,f)=>s+Math.round(f.hp),
            0
        );

    const b=
        fighters
        .filter(f=>f.team===2)
        .reduce(
            (s,f)=>s+Math.round(f.hp),
            0
        );

    document.getElementById(
        "resultInfo"
    ).textContent=
        `WATER TEAM: ${a} HP  •  FLAME TEAM: ${b} HP`;

    document.getElementById(
        "result"
    ).style.display="flex";

}

function update(dt){

    if(!started || ended){

        effects(dt);

        return;

    }

    if(hitStop>0){

        hitStop-=dt;

        effects(dt);

        return;

    }

    timeLeft-=dt;

    for(const f of fighters)
        f.update(dt);

    updateShots(dt);

    effects(dt);

    if(!alive(1)){

        finish(
            "🔥 FLAME TEAM WINS!"
        );

    }
    else if(!alive(2)){

        finish(
            "🌊 WATER TEAM WINS!"
        );

    }
    else if(timeLeft<=0){

        const a=
            fighters
            .filter(f=>f.team===1)
            .reduce(
                (s,f)=>s+f.hp,
                0
            );

        const b=
            fighters
            .filter(f=>f.team===2)
            .reduce(
                (s,f)=>s+f.hp,
                0
            );

        finish(
            a>b
            ?"🌊 WATER TEAM WINS!"
            :
            b>a
            ?"🔥 FLAME TEAM WINS!"
            :
            "⚔️ DRAW!"
        );

    }

    updateHUD();

}

function draw(){

    ctx.save();

    if(shake>0){

        ctx.translate(
            rand(-shake,shake),
            rand(-shake,shake)
        );

        shake*=.86;

        if(shake<.2)
            shake=0;

    }

    background();

    for(const f of fighters)
        f.draw();

    drawEffects();

    ctx.restore();

}

function loop(now){

    const dt=
        Math.min(
            .033,
            (now-last)/1000
        );

    last=now;

    update(dt);

    draw();

    requestAnimationFrame(loop);

}

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

requestAnimationFrame(loop);

</script>

</body>
</html>
"""

components.html(
    HTML,
    height=900,
    scrolling=False
)
