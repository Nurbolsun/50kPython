const txt = document.getElementsByTagName('div')[0]
console.log(txt.innerText)
if ('counter' in localStorage){
    txt.innerText = localStorage.getItem('counter')
}
let btn = document.querySelector('button')
btn.addEventListener('click', myIncrement)

let reset = document.querySelectorAll('button')[1]
reset.addEventListener('click', () => {
    var txt = document.getElementById('counter')
    txt.innerText = 0
    localStorage.setItem('counter', 0)
})

function myIncrement(){
    var txt = document.getElementById('counter')
    txt.innerText = Number(txt.innerText) + 1
    localStorage.setItem('counter', txt.innerText)

}