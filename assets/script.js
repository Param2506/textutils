function run(){
let content = document.getElementById(`showhide`);
let btn = document.getElementById(`Videos`);
    if (content.style.display != 'none') {
        content.style.display = 'none';
    }else{
        content.style.display = 'block';
        }

}

let btn = document.getElementById(`sub`)
btn.addEventListener(`click`, sub)
function sub(){
    window.location.href="https://www.youtube.com/channel/UCabvAi0D6J9va4PWrvrAx2Q";
}


let user = document.getElementById(`member`)
user.addEventListener(`click`, membership)
function membership(){
    window.location.href="member.html";
}
