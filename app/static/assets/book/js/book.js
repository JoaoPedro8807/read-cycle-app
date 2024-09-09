(() => {
    const msg_div =  document.querySelector('.alert-success')
    const close_btn = document.querySelector('.btn-close')

    const dialogs = document.querySelectorAll('dialog')
    const btn_excluir = document.querySelectorAll('.trash-btn')

    const dialog_btn_cancel = document.querySelectorAll('.dialog-cancel-btn')
    const dialog_btn_confirm = document.querySelectorAll('.dialog-confirm-btn')

    btn_excluir.forEach((btn, i) => btn.addEventListener('click', (e) => {              
        dialogs[i].showModal()  

        dialog_btn_cancel[i].addEventListener('click', () => {
            dialogs[i].close()
        })

    }))

    close_btn.addEventListener('click', () => remove_msg_error())
    function remove_msg_error(){
        if (msg_div) {
            msg_div.remove()
        }
    }
    setTimeout(() => {
        remove_msg_error()
    }, 3000)





})()

    