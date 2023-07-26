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
    function openCity(evt, cityName) {
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
   
    //LOGIN PAGE
    function Login(){
      
      // Get the value of the input field with id="username"
      const username = document.getElementById("username").value.trim();
      
      // Get the value of the input field with id="password"
      const password = document.getElementById("password").value.trim();
      // Get the value of the input field with id="confirmpassword"
      
      // Regular expression to check if the password is strong enough
      const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
      // Check if the username is empty
      if (username == "") {
        alert("Username field must be filled out");
        return false;
      }
      
          // Check if the password is empty
      if (password == "") {
        alert("Password field must be filled out");
        return false;
      }
      
      
        
    
        
        // Prepare the data to send to the login API
        const loginData = {
          username: name,
          password: password
      };

      // Make the API call to obtain the access token
      fetch('http://192.168.1.7:8000/login/', {
          method: 'GET',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(loginData)
      })
      .then(response => {
          if (!response.ok) {
              throw new Error('Login failed. Invalid credentials.');
          }
          return response.json();
      })
      .then(data => {
          // Handle the success response from the API
          const accessToken = data.access_token;
          console.log('Access Token:', accessToken);

          // Save the access token, e.g., in a session or local storage
          // You can use sessionStorage or localStorage depending on your requirements
          sessionStorage.setItem('accessToken', accessToken);

          // Redirect the user to the dashboard or homepage
          window.location.href = 'homepage.html'; 
      })
      .catch(error => {
          // Handle errors from the API or invalid credentials
          console.error('Login failed:', error);
          // Display an error message to the user here.
      });
  };

       
        
    //SIGNUP PAGE
    $(document).ready(function() {
      // Get the form element by its ID
      const form = document.getElementById('signupForm');
  
      // Add an event listener to the form for form submission
      form.addEventListener('submit', function(event) {
          event.preventDefault(); // Prevent the form from submitting normally
  
      // Get the value of the input field with id="username"
      const username = document.getElementById("username").value.trim();
      // Get the value of the input field with id="email"
      const email = document.getElementById("email").value.trim();
      // Get the value of the input field with id="password"
      const password = document.getElementById("password").value.trim();
      // Get the value of the input field with id="confirmpassword"
      const passwordConfirm = document.getElementById("confirmpassword").value.trim();
      // Regular expression to check if the email is in the correct format
      var emailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

      // Regular expression to check if the password is strong enough
      var passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$/;
      // Check if the username is empty
      if (username == "") {
        alert("Username field must be filled out");
        return false;
      }
      // Check if the email is empty
     else if (email == "") {
        alert("Email field must be filled out");
        return false;
      }
      // Check if the email is in the correct format
      else if (!email.match(emailRegex)) {
        alert("Please enter a valid email address");
        return false;
      }
          // Check if the password is empty
      else if (password == "") {
        alert(" field must be filled out");
        return false;
      }
      // Check if the password is strong enough
     else if (!password.match(passwordRegex)) {
        alert("Password must be at least 8 characters long and contain at least one lowercase letter, one uppercase letter, and one number");
        return false;
      }
           // Check if the password confirmation is empty
         else  if (passwordConfirm == "") {
            alert("Password confirmation field must be filled out");
            return false;
          }
          // Check if the passwords match
         else if (password != passwordConfirm) {
            alert("Passwords do not match");
            return false;
          } else
          {
 // Prepare the data to send to the API
         const userData = {
             username: name,
             email: email,
             password: password
            
         };
         const history=useHistory();
         
        // Make the API call using the Fetch API
        fetch('http://192.168.0.102:8000/api/register/', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify(userData)
      })
      .then(response => {
          if (!response.ok) {
              throw new Error('Network response was not ok');
          }
          return response.json();
      })
      .then(data => {
          // Handle the success response from the API
          console.log('Signup successful:', data);
          // Redirect the user to the login page
          window.location.href = 'login.html'; 
          history.push("/add")
      })
      .catch(error => {
          // Handle errors from the API
          console.error('Signup failed:', error);
         
      });
    }});
});

      //  // function Register (){
      //     const [username, setUserName] = useState("");
      //     const [useremail, setUserEmail] = useState("");
      //     const [password, setPassword] = useState("");
      //     const history=useHistory();

      //     async function signUp(){
      //       let item={name,email,password}
      //       console.warn(item)

      //       let result =await fetch('https://127.0.0.1:8000/movemanagement/register/', {
      //         method: 'POST',
      //         body:JSON.stringify(item)
      //         headers: {
      //           "Content-Type": 'application/json'
      //           'Accept':'application/json'
  
  
      //         }
      //     })
      //     result= await result.json()
      //     localStorage.setItem("user-info",JSON.stringify(result))
      //     window.location.href = "/login";
      //     history.push("/add")

      //   }
      // //
 function Projectshome(){
  fetch("http://192.168.1.20:8000/project/",{
                method: 'GET',
                mode:"cors"
            })
        
                .then((data) => {
                    return data.json();
                    
                })
                .then((objectdata)=>{
                    console.log(objectdata[0].projectname);
                    let userdata=""
                    objectdata.map((project)=>{
                        userdata +=` <li> ${project.projectname}</li>`;
                    });
                    document.getElementById("userData")
                    innerHTML=userdata;
                })
               
window.onload= Projectshome;
 }
       

      