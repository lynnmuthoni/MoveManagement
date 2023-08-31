console.log("Anything")

document.addEventListener("DOMContentLoaded", function(event) {
   
    const showNavbar = (toggleId, navId, bodyId, headerId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId)
    
    // Validate that all variables exist
    if(toggle && nav && bodypd && headerpd){
    toggle.addEventListener('click', ()=>{
    // show navbar
    nav.classList.toggle('show')
    // change icon
    toggle.classList.toggle('bx-x')
    // add padding to body
    bodypd.classList.toggle('body-pd')
    // add padding to header
    headerpd.classList.toggle('body-pd')
    })
    }
    }
    
    showNavbar('header-toggle','nav-bar','body-pd','header')
    
    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')
    
    function colorLink(){
    if(linkColor){
    linkColor.forEach(l=> l.classList.remove('active'))
    this.classList.add('active')
    }
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))
    
     // Your code to run since DOM is loaded and ready
    });

    // Projects page
    // tabs
    function City(evt, cityName) {
      // Declare all variables
      var i, tabcontent, tablinks;
    
      // Get all elements with class="tabcontent" and hide them
      tabcontent = document.getElementsByClassName("tabcontent");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }
    
      // Get all elements with class="tablinks" and remove the class "active"
      tablinks = document.getElementsByClassName("tablinks");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
      }
    
      // Show the current tab, and add an "active" class to the button that opened the tab
      document.getElementById(cityName).style.display = "block";
      evt.currentTarget.className += " active";
    }
   
  function Logout() {

    
      const token = sessionStorage.getItem('token');
      var form={
        "Authorization":`Token ${token}` ,
      }
      // console.log(form)
  //     .$.ajax( {
  //       type: "POST",
  //       url:"http://192.168.1.10:8000/logout/",
  //       dataType:"json",
  //       data:JSON.stringify(form),        
  //       "timeout": 0,
  //       "headers": {
  //                  "Authorization": `Bearer ${token}`,
  //                  contentType: "application/json",
  //                 }
  //       })
  // .done(function (response) {
  //       console.log(response);
  //     });


  // var settings = {
  //   "url": "http://192.168.1.10:8000/logout/",
  //   "method": "POST",
  //   "timeout": 0,
  //   "headers": {
  //     "Authorization": `Token ${token}`
  //   },
  // };
  
  // $.ajax(settings)
  // .done(function (response) {
  //   console.log(response);
  // });


  // var settings = {
  //   "url": "http://192.168.1.10:8000/logout/",
  //   "type": "POST",
  //   "timeout": 0,
  //   //"mode":"no-cors",
  //   "headers": {
  //     "Authorization": "Token 5f836af9ba724cec7e588781ad1f809c1a08d7abc99b8cdda8aeec42fdc8a406",
      
  //   },
  // };
  
  // $.ajax(settings).done(function (response) {
  //   console.log(response);
  // });

  // var settings = {
  //   "url": "http://192.168.1.10:8000/logout/",
  //   "method": "POST",
  //   "timeout": 0,
  //   "headers": {
  //     "Authorization": "Token dcf3356209e0176abd494305370aa36ed63902b99c96821c79f3d163624e7af3"
  //   },
  // };
  
  // $.ajax(settings).done(function (response) {
  //   console.log(response);
  // });

  $.ajax(console.log("details"),{
    type: "POST",
    url:"http://192.168.1.10:8000/logout/",
    timeout: 0,
    headers: {
      Authorization: `Token ${token}`
    },
    dataType:"json",
    data:JSON.stringify(form),
    contentType: "application/json",
    success: function(response){
      
        console.log(response)
        window.location.href = 'login.html'; 
        
        alert("Successfully logout")

        
    },

        error: function(xhr, status, error) {
                alert("Logout failed. ");
            }
        
    })
    }