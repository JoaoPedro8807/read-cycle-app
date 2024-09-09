
const get_location = () => {
  return new Promise((success, error) => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const latitude = position.coords.latitude;
          const longitude = position.coords.longitude;
          success({
            latitude: latitude,
            longitude: longitude
          })
        }, 
        (reject) => {
          console.log('ERRO AO PEGAR O POSITION: ', reject)  
        })
        
      } 
    })
  }
export default get_location