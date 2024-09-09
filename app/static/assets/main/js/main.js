const error_div =  document.querySelector('.alert')


function remove_msg_error(){
    if (error_div) {
        error_div.remove()
    }
}

(function remove(){
    setTimeout(() => {
        remove_msg_error()
        console.log('removeu')
    }, 3000)
   
})()



