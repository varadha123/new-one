function validate_login(){
    email=document.getElementById('email').value
    password=document.getElementById('password').value
    if (email=="" || password==""){
        document.getElementById('msg').innerHTML='PLEASE ENTER YOUR NAME AND PASSWORD'
        return false
    }
    else
    {
    return true
    }
}