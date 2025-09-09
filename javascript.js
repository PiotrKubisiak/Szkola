function parzyste(x, y){
    x = 4
    y = 2
    if (x % y == 0){
        alert("liczba jest parzysta")
    }else{
        alert("liczba jest nie parzysta")
    }
}
parzyste()
function delta(a,b,c){
    a = 1
    b = 2
    c = 3
    delta = (b * b) - (4 * a * c)
    return delta
}
console.log(delta())

let a = document.getElementById("t1")
let b = document.getElementById("t2")
function lancuchy(a,b){
    toString(a)
    toString(b)
    c = a + b
    return(c)
}
let btn1 = document.getElementById("btn1")
btn1.addEventListener("click", lancuchy (t1,t2))
