(function remove(){
    const close_btn = document.querySelector('.btn-close')
    const error_div =  document.querySelector('.msg-container')
    close_btn.addEventListener('click', () => remove_div(error_div))
    setTimeout(() => {
         remove_msg_error()
     }, 50000)
   
    function remove_div(div){
        if (div) {
            div.remove()
        }
    
     }
    }
)()   




