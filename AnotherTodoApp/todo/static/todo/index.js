let modalOpenButtons = document.querySelectorAll("#modalbutton");

modalOpenButtons.forEach( button => {
    button.addEventListener("click", (e) => {
        document.getElementById("modalbg").style.visibility = "visible";
    });
});

document.getElementById("modalClose").addEventListener("click", (e) => {
    document.getElementById("modalbg").style.visibility = "hidden"; 
});
