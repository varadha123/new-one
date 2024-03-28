function validate_login(){
    doc_name=document.getElementById('name').value
    password=document.getElementById('password').value
    if (doc_name=="" || password==""){
        document.getElementById('msg').innerHTML='PLEASE ENTER YOUR NAME AND PASSWORD'
        return false
    }
    else
    {
    return true
    }
}