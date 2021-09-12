let MenuBtn = document.getElementById("MenuBtn")
    MenuBtn1 = document.getElementById("MenuBtn1")
    Span = document.querySelectorAll(".MenuBtn1-child")
    SideBar = document.getElementById("SideBar")
    LogoName = document.getElementById("IcoName")
    MenuIco = document.getElementById("MenuIco")
    SearchField = document.getElementById("SearchField")
    BtnLink = document.querySelectorAll(".BtnLink")
    Span2 = document.getElementsByClassName("MenuBtn1-child")
    Photo = document.querySelector(".Photo")
    FstName = document.querySelector(".fstName")
    Field3 = document.querySelector(".Field3")



MenuBtn.addEventListener("click", ()=>{
    SideBar.classList.toggle("open")
    IcoName.classList.toggle("open")
    SearchField.classList.toggle("open")
    MenuBtn1.classList.toggle("open")
    Photo.classList.toggle("open")
    FstName.classList.toggle("open")
    
    console.log(BtnLink)
    // for (let i = 0; i < BtnLink.length; i++) {
    //     BtnLink[i].setAttribute("class", "BtnLink open") 
    // }


    if (SideBar.classList.contains("open")) {
        MenuIco.classList.replace("bx-menu", "bx-menu-alt-right")
        Field3.style.width='105%'
        for (let i = 0; i < BtnLink.length; i++) {
            BtnLink[i].setAttribute("class", "BtnLink open")
            MenuBtn1.setAttribute("class","MenuBtn2")
        }

    }
    else{
        MenuIco.classList.replace("bx-menu-alt-right","bx-menu")
        Field3.style.width='100%'
        for (let i = 0; i < BtnLink.length; i++) {
            BtnLink[i].setAttribute("class", "BtnLink")
            Span2[i].setAttribute("class","MenuBtn1-child")
            MenuBtn1.setAttribute("class","MenuBtn1")
        }
    }

})
MenuBtn1.addEventListener("click", ()=>{
    SideBar.classList.toggle("open")
    IcoName.classList.toggle("open")
    SearchField.classList.toggle("open")
    MenuBtn1.classList.toggle("closed")
    Photo.classList.toggle("open")
    FstName.classList.toggle("open")
    console.log(BtnLink)


    if (SideBar.classList.contains("open")) {
        MenuIco.classList.replace("bx-menu", "bx-menu-alt-right")
        for (let i = 0; i < BtnLink.length; i++) {
            BtnLink[i].setAttribute("class", "BtnLink open")
            MenuBtn1.setAttribute("class","MenuBtn2")
        }

    }
    else{
        MenuIco.classList.replace("bx-menu-alt-right","bx-menu")
        for (let i = 0; i < BtnLink.length; i++) {
            BtnLink[i].setAttribute("class", "BtnLink")
            Span2[i].setAttribute("class","MenuBtn1-child")
            MenuBtn1.setAttribute("class","MenuBtn1")
        }
    }


    // if (SideBar.classList.contains("open")) {
    //     Span.classList.toggle("open")
    // }else{
    //     Span.classList.toggle("open")
    // }
})









