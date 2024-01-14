
var info1=fetch("dictionary.txt");
var info2=info1.then(response => response.text())
function proc1(){
    info2.then(proc2)
}
function proc2(str1){
    var qty=document.getElementById("qty").value;
    console.log(qty)
    var words1=str1.split("\r")
    for(let i=0;i<qty;i++){
        console.log(words1[i])
    }
}

