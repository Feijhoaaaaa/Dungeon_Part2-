let SideBar = document.querySelector(".SideBar");
    closeBtn = document.querySelector("#btn");
    searchBtn = document.querySelector(".bx-search");

closeBtn.addEventListener("click", ()=>{
  SideBar.classList.toggle("open");
  if(SideBar.classList.contains("open")){
    closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
  }else {
    closeBtn.classList.replace("bx-menu-alt-right","bx-menu");
  }
});

searchBtn.addEventListener("click", ()=>{ 
  SideBar.classList.toggle("open");
 if(SideBar.classList.contains("open")){
   closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
 }else {
   closeBtn.classList.replace("bx-menu-alt-right","bx-menu");
 }
});
