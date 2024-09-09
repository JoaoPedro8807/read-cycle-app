const div_select = document.querySelector('#id_payment_method')
const user_books_container = document.querySelector('.offer_book-container') 

div_select.addEventListener('change', function() {
    const selectedValue = this.value;
    
    if (selectedValue === 'BT') {
        user_books_container.classList.remove('hidden')
    }else{
        user_books_container.classList.add('hidden')
    }
    
});





