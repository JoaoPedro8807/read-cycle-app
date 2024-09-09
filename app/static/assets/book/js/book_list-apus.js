import get_location from "../../js/get_location.js";
import toggle_class_on_click from "../../js/toggle_class_on_click.js";
(()=>{
        const loc_filter_btn = document.querySelector('#id_proximidade')
        const loc_input_form = document.querySelector('#direction')
        loc_filter_btn.addEventListener('click', async () => {
            const data = await get_location()
            if(data){
                loc_filter_btn.setAttribute('value', JSON.stringify(data))
                //`${data.latitude}, ${data.longitude}`
                console.log('DATA SETADA NO INPUT: ', data)
            }
        })
        const hamburger = document.querySelector('.hamburger');
        const nav = document.querySelector('.nav');
        const filter_btn = document.querySelector('#filter-btn'); 


        function click_to_nav_active(btn, btn_too=false){
            btn.addEventListener('click', function(e){
                nav.classList.toggle('active')
                if(btn_too){
                    this.classList.toggle('active')
                }
                console.log('ATIVA BTN DO CRL')
            })
        }
        click_to_nav_active(hamburger, true)
        click_to_nav_active(filter_btn, false)

        filter_btn.addEventListener('click', ()=>{
            toggle_class_on_click(hamburger, 'active')
        })

        
 
        
    }
)()


