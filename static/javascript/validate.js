/*
 Script for generate password page. Created by Mayank Pandey on Feb. 15, 2020
 */
 function checkPassword()
 {
     var p = document.myForm.createpassword.value;
    if(p=="")
    {   document.getElementById("createpassword").innerHTML = "Password cannot be blank!";
        document.myForm.createpassword.focus();

    }else
    {
      if(p.length >=8)
      {
        re = /[0-9]/;
        if(!re.test(document.myForm.createpassword.value)) {
        document.getElementById("createpassword").innerHTML = "password must contain at least one number (0-9)!";
        document.myForm.createpassword.focus();
        return false;
        }else
        {
             re = /[a-z]/;
            if(!re.test(document.myForm.createpassword.value)) {
            document.getElementById("createpassword").innerHTML = "password must contain at least one lowercase letter (a-z)!";
            document.myForm.createpassword.focus();
            }else
            {
                 re = /[A-Z]/;
                if(!re.test(document.myForm.createpassword.value)) {
                document.getElementById("createpassword").innerHTML = "password must contain at least one uppercase letter (A-Z)!";
                document.myForm.createpassword.focus();
                 }else
                 {
                    re=/[!|@|#|$|%|^|&|*|(|)|-|_]/;
                    if(!re.test(document.myForm.createpassword.value)) {
                    document.getElementById("createpassword").innerHTML = "password must contain at least one Special Character(!|@|#|$|%|^|&|*|(|)|-|_)!";
                     document.myForm.createpassword.focus();
                    }else
                    document.getElementById("createpassword").innerHTML = "";
                }
            }
        }
    }
     else
     {
       document.getElementById("createpassword").innerHTML = "Password must contain at least eight characters!";
       document.myForm.createpassword.focus();
     }
    }
 }
 function checkRPassword()
 {  var p = document.myForm.createpassword.value;
     var rp = document.myForm.confirmpassword.value;
    if(rp=="")
    {
        document.getElementById("confirmpassword").innerHTML = "Please ReEnter your Password";
        document.myForm.confirmpassword.focus();

    }else
    {
       if(p==rp)
       document.getElementById("confirmpassword").innerHTML = "";
       else{
        document.getElementById("confirmpassword").innerHTML = "Mismatch Password";
        document.myForm.confirmpassword.focus();

        }
    }

 }
/*End of Script for generate password page.*/







function myFunction() {
  document.getElementById("my").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
/*
window.onclick = function(event) {
  if (!event.target.matches('.d-btn')) {
    var dropdowns = document.getElementsByClassName("drops");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
*/