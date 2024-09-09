(()=>{

    const btn_excluir = document.querySelectorAll('.delete-btn')
    const dialogs = document.querySelectorAll('.delete-trade-dialog')
    const dialog_cancel = document.querySelectorAll('.dialog-cancel-btn')
    handleDialog(btn_excluir, dialogs, dialog_cancel)

    const give_up_btns = document.querySelectorAll('.give-up-btn')
    const give_up_dialogs = document.querySelectorAll('.give-up-dialog')
    const give_up_cancel = document.querySelectorAll('.give-up-cancel')
    handleDialog(give_up_btns, give_up_dialogs, give_up_cancel)

    function handleDialog(btns, dialogs, dialogs_cancel){
        btns.forEach((btn, i) => btn.addEventListener('click', (e) => {              
            dialogs[i].showModal()  
    
            dialogs_cancel[i].addEventListener('click', () => {
                dialogs[i].close()
            })
        }))
    }

})()
