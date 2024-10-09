const div_select = document.querySelector('#id_payment_method')
const user_books_container = document.querySelector('.offer_book-container') 
const book_select = document.querySelector('#id_offer_book')

div_select.addEventListener('change', function() {
    const selectedValue = this.value;
    
    if (selectedValue === 'BT') {
        user_books_container.classList.remove('hidden')
        book_select.setAttribute('required', '')
        console.log('ALTEROU')
    }else{
        user_books_container.classList.add('hidden')
        book_select.removeAttribute('required')
    }
    
});





