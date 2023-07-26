// import React,{useState} from 'react'
// import {useHistory} from 'react-router-dom'

function Register(){

    const[name,setName]=useState("")
    const[email,setEmail]=useState("")
    const[password,setPassword]=useState("")
    const history=useHistory();

    async function Signup(){
        let item={name,password,email}
        console.warn(item)

        fetch('http://192.168.0.102:8000/api/register/', {
          method: 'POST',
          body: JSON.stringify(item),
          headers: {
              'Content-Type': 'application/json',
              "Accept":  'application/json'
          }
          
      })
      result=await result.json()
      localStorage.setItem("user-info",JSON.stringify(result))
      history.push("/add")
    }
    return(
        <div>
                            
                            <label for="username">Username</label>
                            <input type="text" value={name} onChange={(e)=>setName(e.target.value)} placeholder="Enter Username" id="username" name="username"  />
                
                            
                             <label for="useremail">Useremail</label>
                             <input type="email" placeholder="Enter email" value={email} onChange={(e)=>setEmail(e.target.value)} />
                 
                            <br/>
                
                            
                            <label for="pswrd"> Password</label>
                            <input type="password"  placeholder="Enter Password" value={password} onChange={(e)=>setPassword(e.target.value)}  />
                
                          
                            
                            <div class="subcontainer">
                                <p class="forgotpsd"> <a href="#">Forgot Password?</a></p>
                            </div>
                
                
                           
                            <button  onclick = "Signup()" type="submit">SignUp</button><br/>
                
                         
                            <p class="register">Already a member?  <a class="" href="login.html">Login here!</a></p>
                            </div>
    )
   
}
export default Register