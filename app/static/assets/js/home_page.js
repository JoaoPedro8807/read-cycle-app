import get_location from "./get_location.js"

if (navigator.geolocation) {
    const data = await get_location() 
    const target = document.querySelector('#portfolio-container')
    const csrftoken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
    fetch(
        '/',
        {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data)
        }
    ).then(response => response.text())
    .then(html => target.innerHTML = html)
    .catch(
        error => console.log('error no fetch: ', error)
    )
}








    
    
    
    
    
    
    