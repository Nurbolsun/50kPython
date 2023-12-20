function mysum(a, b){
    let result = a + b;
    return result
}
for (let i = 0; i < 5; i++){
    const c = mysum(i, i*3)
    console.log(c)
}