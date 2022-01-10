// Setting the footer to exact position
var section = document.getElementById("bdy");
section.style.minHeight = `${window.innerHeight - 110}px`;
window.addEventListener("resize", () => {
    section.style.minHeight = `${window.innerHeight - 110}px`;
});


// Animations of blogs in blog list
var div=document.getElementsByClassName("animate__animated");
div=Array.from(div);
if(div.length){
    div[0].classList.add("animate__pulse")
}
window.addEventListener('scroll',()=>{
    for(let i=1;i<div.length;i++){
        let x=div[i].getBoundingClientRect();
        if(x.top>=100 && x.bottom<=window.innerHeight-100){
            div[i].classList.add("animate__pulse");
        }
    }
})

document.getElementById("cmtPOP").addEventListener('focus', () => {
    document.getElementById("cmtPOP").blur();
    swal("Please login to comment")
    .then(()=>{
        window.location.href='/account/signin/';
    })
})

dtlBlgs=document.getElementsByClassName("dltBlg");
Array.from(dtlBlgs).forEach((element)=>{
    element.addEventListener("click",(this)=>{
        window.location.href=`/blog/delete-blog/${this.id}`;
    })
})