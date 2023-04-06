const loadUrl = (newLocation) => {
  window.open(newLocation, '_blank').focus();
}

//fetch("https://api.sncf.com/v1/coverage/sncf/journeys?min_nb_journeys=10&data_freshness=realtime&from=-0.556514;44.823462&to=2.317832062;48.837329984&datetime=20230405T100000", {
//   method: 'GET',
//   headers: {
//       'Content-Type': 'application/json',
//       'Authorization': `Basic ${btoa('b0aa53c3-fd81-4053-9113-bd8692d9062e:')}`,
//   },
// }).then(response => response.json())
// .then(data => {
// console.log(data);
// })

const form = document.querySelector('form')
console.log(form)
form.addEventListener('submit', (event) => {
  event.preventDefault();

  const inputlongitude = event.currentTarget.querySelector('#longitude').value
  const inputlatitude = event.currentTarget.querySelector('#latitude').value

  const now = new Date();
  const year = now.getFullYear();
  const month = ('0' + (now.getMonth() + 1)).slice(-2);
  const day = ('0' + now.getDate()).slice(-2);
  const hours = ('0' + now.getHours()).slice(-2);
  const formattedDateTime = `${year}${month}${day}T${hours}`;
  console.log(formattedDateTime);


  const url = `https://api.sncf.com/v1/coverage/sncf/journeys?min_nb_journeys=10&data_freshness=realtime&from=-0.556514;44.823462&to=${inputlongitude};${inputlatitude}&datetime=${formattedDateTime}`
  fetch(url, {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Basic ${btoa('b0aa53c3-fd81-4053-9113-bd8692d9062e:')}`,
    },
  })
    .then(response => response.json())
    .then(response => {
      const co2Emissions = response['journeys'][0]['co2_emission']['value'];
      console.log(`Emmissions CO2: ${co2Emissions} gEC`);
      document.getElementById('co2').innerHTML = `${co2Emissions} gEC`;
    })
})
